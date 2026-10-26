"""Content-preservation and diagnostic regression tests."""

from __future__ import annotations

import copy
import json
import subprocess
import sys

import pytest

from atlas_spec import AtlasError, AtlasParseError, atlas_content_equal
from atlas_spec.util import strict_json_loads


@pytest.mark.parametrize("target,suffix", [("markdown", "md"), ("latex", "tex")])
def test_cli_preserves_payload_with_schema_wrapper(minimal, minimal_dir, tmp_path, target, suffix):
    document = copy.deepcopy(minimal)
    document["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    source = tmp_path / "with-schema.json"
    source.write_text(json.dumps(document), encoding="utf-8")
    output = tmp_path / f"out.{suffix}"
    result = subprocess.run(
        [sys.executable, "-m", "atlas_spec", "convert", str(source),
         "--from", "json", "--to", target, "--resources", str(minimal_dir),
         "--output", str(output)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.is_file()


def test_equality_ignores_transport_but_preserves_scalar_types(minimal):
    left = copy.deepcopy(minimal)
    right = copy.deepcopy(minimal)
    right["$schema"] = "local-profile-schema.json"
    assert atlas_content_equal(left, right)
    left["atlas"]["extensions"] = {"example.org/value": True}
    right["atlas"]["extensions"] = {"example.org/value": 1}
    assert not atlas_content_equal(left, right)


def test_convert_file_does_not_publish_changed_content(registry, minimal_dir, tmp_path, monkeypatch):
    original = registry.encode_from_atlas_json

    def changed(document, **kwargs):
        altered = copy.deepcopy(document)
        altered["atlas"]["title"]["text"] += " changed"
        return original(altered, **kwargs)

    monkeypatch.setattr(registry, "encode_from_atlas_json", changed)
    output = tmp_path / "changed.md"
    with pytest.raises(AtlasError, match="post-encode verification failed"):
        registry.convert_file(
            minimal_dir / "example.atlas.json", output,
            source_format="json", target_format="markdown", resource_root=minimal_dir,
        )
    assert not output.exists()


def test_graph_to_rf_link_must_be_reciprocal(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    case = document["atlas"]["use_cases"][0]
    requirement = case["functional_requirements"][0]
    graph = next(g for g in document["atlas"]["graphs"] if g["id"] == case["flows"]["main"])
    node = next(n for n in graph["nodes"] if n["id"] not in requirement["flow_refs"])
    node["requirement_refs"].append(requirement["id"])
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    assert "ATL-E-RF-FLOW" in {d.code for d in info.value.diagnostics}


@pytest.mark.parametrize("field", ["applies_to", "references"])
def test_rnf_references_must_resolve(registry, minimal, minimal_dir, field):
    document = copy.deepcopy(minimal)
    document["atlas"]["use_cases"][0]["nonfunctional_requirements"][0][field] = ["SRC-MISSING"]
    with pytest.raises(AtlasError) as info:
        registry.validator.validate(document, resource_root=minimal_dir)
    assert "ATL-E-REF" in {d.code for d in info.value.diagnostics}


@pytest.mark.parametrize("value", ["NaN", "Infinity", "-Infinity"])
def test_nonstandard_nonfinite_json_is_rejected(value):
    with pytest.raises(AtlasParseError):
        strict_json_loads('{"extension": ' + value + "}")


@pytest.mark.parametrize("format_name", ["markdown", "latex"])
def test_extension_with_reserved_text_keys_is_opaque(registry, minimal, minimal_dir, format_name):
    document = copy.deepcopy(minimal)
    document["atlas"]["extensions"] = {
        "example.org/opaque": {"@text": "literal", "text": [1, True], "nested": [{"@text": "T000001"}]}
    }
    encoded = registry.encode_from_atlas_json(document, target_format=format_name, resource_root=minimal_dir)
    restored = registry.decode_to_atlas_json(encoded, source_format=format_name, resource_root=minimal_dir)
    assert atlas_content_equal(document, restored)


def test_duplicate_skeleton_slot_is_rejected():
    from atlas_spec.slots import restore

    with pytest.raises(AtlasParseError) as info:
        restore([{"@text": "T000001"}, {"@text": "T000001"}], {"T000001": "one record"})
    assert "ATL-E-SLOT-DUPLICATE" in {d.code for d in info.value.diagnostics}


def test_package_name_cannot_escape_output(minimal_dir, tmp_path):
    output = tmp_path / "package"
    result = subprocess.run(
        [sys.executable, "-m", "atlas_spec", "package", str(minimal_dir / "example.atlas.json"),
         "--from", "json", "--output", str(output), "--name", "../outside.json"],
        capture_output=True, text=True,
    )
    assert result.returncode != 0
    assert "one file name" in result.stderr
    assert not (tmp_path / "outside.json").exists()
    assert not output.exists()


@pytest.mark.parametrize("format_name", ["markdown", "latex"])
@pytest.mark.parametrize("location", ["meta", "data"])
def test_literal_keys_in_metadata_and_example_data(registry, minimal, minimal_dir, format_name, location):
    document = copy.deepcopy(minimal)
    literal = {"id": "ENT-REQUEST", "@text": "literal", "text": 17, "nested": {"text": "domain value"}}
    if location == "meta":
        document["atlas"]["title"]["meta"] = literal
    else:
        document["atlas"]["entities"][0]["examples"][0]["data"] = literal
    encoded = registry.encode_from_atlas_json(document, target_format=format_name, resource_root=minimal_dir)
    restored = registry.decode_to_atlas_json(encoded, source_format=format_name, resource_root=minimal_dir)
    assert atlas_content_equal(document, restored)
