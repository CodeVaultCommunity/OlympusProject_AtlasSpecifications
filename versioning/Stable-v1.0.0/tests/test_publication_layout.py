"""Presentation changes must preserve editable content and legacy Stable inputs."""
import json
import re

import pytest

from atlas_spec import AtlasError, atlas_content_equal
from conftest import VERSION_ROOT


@pytest.mark.parametrize("name", ["minimal", "composition", "task-board"])
def test_legacy_stable_input_is_still_exact(registry, name):
    root = VERSION_ROOT / "examples" / name
    source = VERSION_ROOT / "tests/fixtures/legacy_stable" / f"{name}.atlas.tex"
    expected = json.loads((root / "example.atlas.json").read_text(encoding="utf-8"))
    recovered = registry.decode_to_atlas_json(source, source_format="latex", resource_root=root)
    assert atlas_content_equal(expected, recovered)
    new = registry.encode_from_atlas_json(recovered, target_format="latex", resource_root=root)
    assert atlas_content_equal(expected, registry.decode_to_atlas_json(new, source_format="latex", resource_root=root))
    for graph in expected["atlas"]["graphs"]:
        marker = f"% atlas:tikz:begin id=TIKZ-{graph['id']}\n"
        assert new.count(marker) == 1  # shared validations are drawn once
        assert new.index(graph["owner"]["id"]) < new.index(marker) < new.index("Appendix: graphs")


def test_long_tables_and_special_text_roundtrip(registry, minimal, minimal_dir):
    text = "A {literal} \\ % & _ # $ ^ ~\t accents: çã\r\nB\rC\n"
    minimal["atlas"]["title"]["text"] = text
    minimal["atlas"]["actors"][0]["name"]["text"] = text
    minimal["atlas"]["entities"][0]["fields"][0]["description"][0]["text"] = text * 70
    minimal["atlas"]["structure"][0]["blocks"].append({
        "type": "table", "columns": [{"text": "Long column"}, {"text": "Exact value"}],
        "rows": [[{"text": text * 90}, {"text": " \t\r\n"}]],
    })
    source = registry.encode_from_atlas_json(minimal, target_format="latex", resource_root=minimal_dir)
    assert "Table row 1" in source  # breakable details, no oversized table row
    assert atlas_content_equal(minimal, registry.decode_to_atlas_json(source, source_format="latex", resource_root=minimal_dir))


@pytest.mark.parametrize("legacy", [False, True])
def test_tampered_diagram_still_rejected(registry, minimal, minimal_dir, legacy):
    if legacy:
        source = (VERSION_ROOT / "tests/fixtures/legacy_stable/minimal.atlas.tex").read_text(encoding="utf-8")
    else:
        source = registry.encode_from_atlas_json(minimal, target_format="latex", resource_root=minimal_dir)
    source = source.replace("line width=0.65pt", "line width=0.66pt", 1)
    with pytest.raises(AtlasError) as exc:
        registry.decode_to_atlas_json(source, source_format="latex", resource_root=minimal_dir)
    assert "ATL-E-TIKZ-STALE" in {d.code for d in exc.value.diagnostics}


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "orphan", "malformed"])
def test_table_slots_still_checked(registry, minimal, minimal_dir, mutation):
    source = registry.encode_from_atlas_json(minimal, target_format="latex", resource_root=minimal_dir)
    match = re.search(r"\\AtlasCell\{T[0-9]{6}\}\{[^{}]*\}", source)
    assert match
    token = match.group()
    if mutation == "orphan":
        source = source.replace("% atlas:structure:begin", "\\AtlasCell{T999999}{orphan}\n% atlas:structure:begin")
    else:
        replacement = {"missing": "", "duplicate": token + token, "malformed": token[:-1]}[mutation]
        source = source[:match.start()] + replacement + source[match.end():]
    with pytest.raises(AtlasError):
        registry.decode_to_atlas_json(source, source_format="latex", resource_root=minimal_dir)


def test_editing_authoritative_cell_is_preserved(registry, minimal, minimal_dir):
    minimal["atlas"]["authors"][0]["name"]["text"] = "Neutral Author"
    source = registry.encode_from_atlas_json(minimal, target_format="latex", resource_root=minimal_dir)
    assert "Neutral Author" in source
    edited = source.replace("Neutral Author", "Edited Author", 1)
    minimal["atlas"]["authors"][0]["name"]["text"] = "Edited Author"
    assert atlas_content_equal(minimal, registry.decode_to_atlas_json(edited, source_format="latex", resource_root=minimal_dir))
