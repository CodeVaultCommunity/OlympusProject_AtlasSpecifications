"""Public-contract regressions reproduced on the unmodified Alpha runtime copy."""
from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path
import subprocess
import sys

import pytest

from atlas_spec import ALL_FORMATS, AtlasValidationError, atlas_content_equal


def roundtrips(registry, document, resource_root):
    encoded = {
        fmt: registry.encode_from_atlas_json(document, target_format=fmt, resource_root=resource_root)
        for fmt in ALL_FORMATS
    }
    for source, target in itertools.permutations(ALL_FORMATS, 2):
        decoded = registry.decode_to_atlas_json(encoded[source], source_format=source, resource_root=resource_root)
        output = registry.encode_from_atlas_json(decoded, target_format=target, resource_root=resource_root)
        recovered = registry.decode_to_atlas_json(output, source_format=target, resource_root=resource_root)
        assert atlas_content_equal(document, recovered), (source, target)


def cli(document, tmp_path, resource_root, *arguments):
    source = tmp_path / "input.json"
    source.write_text(json.dumps(document, ensure_ascii=False), encoding="utf-8")
    return subprocess.run(
        [sys.executable, "-m", "atlas_spec", *arguments, str(source), "--resources", str(resource_root)],
        capture_output=True, text=True, encoding="utf-8",
    )


@pytest.mark.parametrize("removed", [("assumptions",), ("open_issues",), ("assumptions", "open_issues")])
def test_optional_entity_records_preserve_absence(registry, minimal, minimal_dir, tmp_path, removed):
    document = copy.deepcopy(minimal)
    for field in removed:
        del document["atlas"]["entities"][0][field]
    before = copy.deepcopy(document)
    result = cli(document, tmp_path, minimal_dir, "validate")
    assert result.returncode == 0, result.stderr
    roundtrips(registry, document, minimal_dir)
    assert document == before  # Validation/presentation must not materialize empty arrays.


@pytest.mark.parametrize("field", ["assumptions", "open_issues"])
def test_optional_entity_records_reject_null(registry, minimal, minimal_dir, tmp_path, field):
    minimal["atlas"]["entities"][0][field] = None
    result = cli(minimal, tmp_path, minimal_dir, "validate")
    assert result.returncode == 2
    assert "ATL-E-SCHEMA" in result.stderr
    assert "Traceback" not in result.stderr


FIGURE_LOCATIONS = [
    ("structure", 0, "blocks"),
    ("entities", 0, "meaning"),
    ("entities", 0, "fields", 0, "constraints"),
    ("entities", 0, "validations", 0, "statement"),
    ("tools", 0, "operations", 0, "effects"),
    ("use_cases", 0, "outcomes", 0, "effects"),
    ("use_cases", 0, "nonfunctional_requirements", 0, "criterion"),
    ("boundaries", 0, "interactions", 0, "description"),
    ("graphs", 0, "nodes", 0, "details"),
    ("resources", 0, "caption"),
    ("sources", 0, "note"),
]


@pytest.mark.parametrize("location", FIGURE_LOCATIONS)
@pytest.mark.parametrize("target_kind", ["missing", "wrong", "valid"])
def test_nested_figure_reference_category(registry, minimal, minimal_dir, location, target_kind):
    atlas = minimal["atlas"]
    target = {"missing": "RES-NOT-FOUND", "wrong": atlas["entities"][0]["id"],
              "valid": atlas["resources"][0]["id"]}[target_kind]
    node = atlas
    for part in location[:-1]:
        node = node[part]
    node.setdefault(location[-1], []).append({"type": "figure", "resource": target})
    if target_kind == "valid":
        registry.validator.validate(minimal, resource_root=minimal_dir)
    else:
        with pytest.raises(AtlasValidationError) as exc:
            registry.validator.validate(minimal, resource_root=minimal_dir)
        assert "ATL-E-REF" in {d.code for d in exc.value.diagnostics}


RECORD_REFERENCES = [
    ("entities", "assumptions"), ("entities", "open_issues"),
    ("use_cases", "sources"), ("use_cases", "assumptions"), ("use_cases", "open_issues"),
    ("boundaries", "sources"), ("boundaries", "assumptions"), ("boundaries", "open_issues"),
]


@pytest.mark.parametrize("collection,field", RECORD_REFERENCES)
@pytest.mark.parametrize("valid", [False, True])
def test_record_references_use_declared_category(registry, minimal, minimal_dir, collection, field, valid):
    atlas = minimal["atlas"]
    if valid:
        record = copy.deepcopy(atlas[field][0])
        record["id"] = "UNCONVENTIONAL-IDENTITY"
        atlas[field].append(record)
        target = record["id"]
    else:
        target = atlas["entities"][0]["id"]
    atlas[collection][0][field] = [target]
    if valid:
        registry.validator.validate(minimal, resource_root=minimal_dir)
    else:
        with pytest.raises(AtlasValidationError) as exc:
            registry.validator.validate(minimal, resource_root=minimal_dir)
        assert "ATL-E-REF" in {d.code for d in exc.value.diagnostics}


@pytest.mark.parametrize("target", ["markdown", "latex"])
@pytest.mark.parametrize("existing", [False, True])
def test_cli_bad_figure_never_publishes(minimal, minimal_dir, tmp_path, target, existing):
    minimal["atlas"]["structure"][0]["blocks"].append({"type": "figure", "resource": "RES-NOT-FOUND"})
    output = tmp_path / "output.txt"
    if existing:
        output.write_bytes(b"previous valid publication")
    result = cli(minimal, tmp_path, minimal_dir, "convert", "--from", "json", "--to", target, "-o", str(output))
    assert result.returncode == 2, result.stdout + result.stderr
    assert "ATL-E-REF" in result.stderr
    assert "Traceback" not in result.stderr
    assert output.read_bytes() == b"previous valid publication" if existing else not output.exists()


NEWLINES = ["A\r\nB", "A\rB", "A\nB", " A\r\nB\rC\nD\t ação  \r\n", "\r", "\n", "\r\n",
            "literal \\AtlasCharCRLF{} \\AtlasCharCR{} \\AtlasCharNewline{} \\AtlasCharTab{}"]


@pytest.mark.parametrize("value", NEWLINES)
def test_table_cell_line_endings_exact(registry, minimal, minimal_dir, tmp_path, value):
    minimal["atlas"]["structure"][0]["blocks"].append(
        {"type": "table", "columns": [{"text": "Column"}], "rows": [[{"text": value}]]}
    )
    roundtrips(registry, minimal, minimal_dir)
    output = tmp_path / "output.tex"
    result = cli(minimal, tmp_path, minimal_dir, "convert", "--from", "json", "--to", "latex", "-o", str(output))
    assert result.returncode == 0, result.stderr
    assert atlas_content_equal(minimal, registry.decode_to_atlas_json(output, source_format="latex", resource_root=minimal_dir))


@pytest.mark.parametrize("kind", ["paragraph", "heading", "list", "code"])
def test_final_cr_does_not_merge_with_structural_separator(registry, minimal, minimal_dir, kind):
    value = "text\r"
    block = {"type": kind, "text": value}
    if kind == "heading":
        block["level"] = 2
    elif kind == "list":
        block = {"type": "list", "ordered": False, "items": [{"text": value}]}
    minimal["atlas"]["structure"][0]["blocks"].append(block)
    roundtrips(registry, minimal, minimal_dir)


@pytest.mark.parametrize("separator", ["\u0085", "\u2028", "\u2029"])
@pytest.mark.parametrize("location", ["extensions", "meta", "data", "text"])
def test_unicode_separators_and_opaque_reference_keys(registry, minimal, minimal_dir, separator, location):
    value = "A" + separator + "B"
    opaque = {"value": value, "text": value, "@text": value, "id": "ENT-REQUEST",
              "type": "figure", "resource": "RES-NOT-FOUND", "sources": ["ENT-REQUEST"],
              "nested": [{"text": value, "@text": "T000001"}]}
    atlas = minimal["atlas"]
    if location == "extensions":
        atlas["extensions"]["audit"] = opaque
    elif location == "meta":
        atlas["title"]["meta"] = opaque
    elif location == "data":
        atlas["entities"][0]["examples"][0]["data"] = opaque
    else:
        atlas["structure"][0]["blocks"].append({"type": "paragraph", "text": value})
    roundtrips(registry, minimal, minimal_dir)
