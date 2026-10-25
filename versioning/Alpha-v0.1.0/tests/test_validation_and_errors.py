from __future__ import annotations

import copy
from pathlib import Path

import pytest

from atlas_spec.util import read_text_exact

from atlas_spec import AtlasError, AtlasParseError


def codes(exc: AtlasError) -> set[str]:
    return {diagnostic.code for diagnostic in exc.diagnostics}


def expect_code(exc_info, code: str) -> None:
    assert code in codes(exc_info.value), [d.format() for d in exc_info.value.diagnostics]


def test_duplicate_json_keys_are_rejected():
    from atlas_spec.util import strict_json_loads

    with pytest.raises(AtlasParseError) as info:
        strict_json_loads('{"a": 1, "a": 2}')
    expect_code(info, "ATL-E-DUPLICATE-KEY")


def test_binary_float_is_rejected():
    from atlas_spec.util import strict_json_loads

    with pytest.raises(AtlasParseError) as info:
        strict_json_loads('{"a": 1.5}')
    expect_code(info, "ATL-E-FLOAT")


def test_duplicate_ids(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["entities"][0]["fields"][0]["id"] = "ENT-REQUEST"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-DUPLICATE-ID")


def test_missing_reference(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["use_cases"][0]["actors"][0]["actor"] = "ACT-MISSING"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-REF")


def test_missing_required_text(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    del document["atlas"]["use_cases"][0]["functional_requirements"][0]["statement"]
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-SCHEMA")


def test_unknown_graph_endpoint(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    graph = next(g for g in document["atlas"]["graphs"] if g["id"] == "GRAPH-REQUEST-SUBMIT")
    graph["edges"][0]["to"] = "N-MISSING"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-GRAPH-EDGE")


def test_unknown_graph_node_call(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    graph = next(g for g in document["atlas"]["graphs"] if g["id"] == "GRAPH-REQUEST-SUBMIT")
    node = next(n for n in graph["nodes"] if n["id"] == "N-REQ-VALIDATE")
    node["call"]["id"] = "VLD-MISSING"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-GRAPH-CALL")


def test_unsupported_block_type(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["structure"][0]["blocks"].append(
        {"type": "video", "text": "unsupported", "src": "x"}
    )
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-SCHEMA")


def test_rf_list_and_graph_divergence(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["use_cases"][0]["functional_requirements"][0]["flow_refs"] = ["N-REQ-START"]
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-RF-FLOW")


def test_shared_rnf_reference_must_be_canonical(registry, composition, composition_dir):
    document = copy.deepcopy(composition)
    cancel = next(c for c in document["atlas"]["use_cases"] if c["id"] == "UC-BOOKING-CANCEL")
    cancel["nonfunctional_requirements"][0]["reference_to"] = "RNF-MISSING"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=composition_dir)
    expect_code(info, "ATL-E-REF")


def test_incompatible_markdown_version(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.md")
    text = text.replace("representation=Alpha-v0.1.0", "representation=Alpha-v0.9.0", 1)
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="markdown", resource_root=minimal_dir)
    expect_code(info, "ATL-E-VERSION")


def test_incompatible_latex_version(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    text = text.replace("representation=Alpha-v0.1.0", "representation=Alpha-v0.9.0", 1)
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="latex", resource_root=minimal_dir)
    expect_code(info, "ATL-E-VERSION")


def test_malformed_markdown_marker(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.md")
    text = text.replace(
        "<!-- atlas:text id=T000001 role=heading level=1 -->",
        "<!-- atlas:text T000001 heading -->",
        1,
    )
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="markdown", resource_root=minimal_dir)
    expect_code(info, "ATL-E-MARKDOWN")


def test_duplicate_text_record_in_markdown(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.md")
    text = text.replace(
        "<!-- atlas:text id=T000005 role=list-item ordered=no -->",
        "<!-- atlas:text id=T000001 role=list-item -->",
        1,
    )
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="markdown", resource_root=minimal_dir)
    expect_code(info, "ATL-E-MARKDOWN")


def test_missing_text_record(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.md")
    marker = "<!-- atlas:text id=T000005 role=list-item ordered=no -->"
    start = text.index(marker)
    end_marker = "<!-- /atlas:text id=T000005 -->"
    end = text.index(end_marker) + len(end_marker)
    text = text[:start] + text[end:]
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="markdown", resource_root=minimal_dir)
    expect_code(info, "ATL-E-SLOT-MISSING")


def test_derived_region_edit_is_diagnosed(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.md")
    text = text.replace(
        "Derived summary: 5 sections;",
        "Derived summary: 999 sections;",
        1,
    )
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="markdown", resource_root=minimal_dir)
    expect_code(info, "ATL-E-DERIVED-STALE")


def test_latex_derived_edit_is_diagnosed(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    text = text.replace(
        "\\begin{atlasderived}{DERIVED-SUMMARY}\nDerived summary: 5 sections;",
        "\\begin{atlasderived}{DERIVED-SUMMARY}\nDerived summary: 999 sections;",
        1,
    )
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="latex", resource_root=minimal_dir)
    expect_code(info, "ATL-E-DERIVED-STALE")


def test_embedded_image_text_requires_common_text(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["resources"][0]["embedded_text"].append(
        {"text": "A label that exists nowhere else"}
    )
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-RESOURCE-TEXT")


def test_resource_path_must_stay_inside_root(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["resources"][0]["path"] = "../outside.svg"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-RESOURCE-PATH")


def test_tikz_edit_is_diagnosed(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    assert "\\node[terminal]" in text
    text = text.replace("\\node[terminal]", "\\node[box]", 1)
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="latex", resource_root=minimal_dir)
    expect_code(info, "ATL-E-TIKZ-STALE")


def test_unknown_atlas_environment_is_rejected(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    text = text.replace(
        "\\begin{document}",
        "\\begin{document}\n\\begin{atlasunknown}{T999999}\nunsupported\n\\end{atlasunknown}\n",
        1,
    )
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="latex", resource_root=minimal_dir)
    expect_code(info, "ATL-E-LATEX")


def test_unterminated_latex_environment(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    text = text.replace("\\end{atlastitle}", "", 1)
    with pytest.raises(AtlasError) as info:
        registry.decode_to_atlas_json(text, source_format="latex", resource_root=minimal_dir)
    expect_code(info, "ATL-E-LATEX")


def test_resource_missing(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["resources"][0]["path"] = "assets/does-not-exist.svg"
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-RESOURCE-MISSING")


def test_resource_hash_mismatch(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["resources"][0]["sha256"] = "0" * 64
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-RESOURCE-HASH")


def test_stale_figure_against_graph(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    graph = next(g for g in document["atlas"]["graphs"] if g["id"] == "GRAPH-REQUEST-SUBMIT")
    graph["nodes"].append(
        {
            "id": "N-REQ-NEW",
            "type": "note",
            "label": {"text": "A new node changes the graph fingerprint"},
            "requirement_refs": [],
        }
    )
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    expect_code(info, "ATL-E-FIGURE-STALE")


def test_external_latex_command_outside_profile_is_ignored(registry, minimal_dir):
    text = read_text_exact(minimal_dir / "example.atlas.tex")
    text = text.replace(
        "\\begin{document}",
        "\\begin{document}\n% foreign presentation command, outside the Atlas profile\n\\providecommand{\\Foreign}{ignored}\n",
        1,
    )
    document = registry.decode_to_atlas_json(
        text, source_format="latex", resource_root=minimal_dir
    )
    assert document["atlas"]["document_id"] == "ATLAS-EX-MINIMAL"
