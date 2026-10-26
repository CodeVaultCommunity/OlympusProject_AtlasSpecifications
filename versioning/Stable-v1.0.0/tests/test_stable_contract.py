"""Release identity, editorial revision and public compatibility checks."""
from __future__ import annotations

import copy
import json

import pytest

from atlas_spec import AtlasError, atlas_content_equal
from conftest import VERSION_ROOT


@pytest.mark.parametrize("field,code", [("spec_version", "ATL-E-VERSION"),
                                        ("profile_version", "ATL-E-PROFILE-VERSION")])
@pytest.mark.parametrize("value", ["Alpha-v0.1.0", "Stable-v2.0.0"])
def test_incompatible_content_version_is_explicit(registry, minimal, field, code, value):
    minimal["atlas"][field] = value
    with pytest.raises(AtlasError) as error:
        registry.validator.validate(minimal)
    assert code in {d.code for d in error.value.diagnostics}
    assert "Stable-v1.0.0" in str(error.value)


@pytest.mark.parametrize("fmt", ["json", "markdown", "latex"])
def test_runtime_rejects_alpha_representation(registry, minimal, minimal_dir, fmt):
    text = registry.encode_from_atlas_json(minimal, target_format=fmt, resource_root=minimal_dir)
    # Only change the representation declaration, leaving the payload intact.
    token = "atlas-json/Stable-v1.0.0" if fmt == "json" else "representation=Stable-v1.0.0"
    text = text.replace(token, token.replace("Stable-v1.0.0", "Alpha-v0.1.0"), 1)
    with pytest.raises(AtlasError) as error:
        registry.decode_to_atlas_json(text, source_format=fmt, resource_root=minimal_dir)
    assert "ATL-E-VERSION" in {d.code for d in error.value.diagnostics}


@pytest.mark.parametrize("fmt", ["json", "markdown", "latex"])
def test_conversion_preserves_declared_producer_and_history(registry, minimal, minimal_dir, fmt):
    minimal["atlas"]["translator_version"] = "0.8.2"
    minimal["atlas"]["revision"] = "editorial-7"
    expected = copy.deepcopy(minimal)
    text = registry.encode_from_atlas_json(minimal, target_format=fmt, resource_root=minimal_dir)
    result = registry.decode_to_atlas_json(text, source_format=fmt, resource_root=minimal_dir)
    assert atlas_content_equal(expected, result)
    assert minimal == expected


def test_task_board_versioned_change_and_invalid_reference(registry, tmp_path):
    root = VERSION_ROOT / "examples/task-board"
    before = registry.decode_to_atlas_json(root / "revisions/revision-2.atlas.json", source_format="json")
    after = registry.decode_to_atlas_json(root / "revisions/revision-3.atlas.json", source_format="json")
    assert before["atlas"]["spec_version"] == after["atlas"]["spec_version"] == "Stable-v1.0.0"
    assert (root / "example.atlas.json").read_bytes() == (root / "revisions/revision-3.atlas.json").read_bytes()
    expected = copy.deepcopy(before)
    expected["atlas"]["revision"] = "3"
    expected["atlas"]["history"].append(after["atlas"]["history"][-1])
    assert expected["atlas"]["history"][-1]["id"] == "HIST-TASK-BOARD-03"
    assert expected["atlas"]["history"][-1]["version"] == "3"
    case = next(c for c in expected["atlas"]["use_cases"] if c["id"] == "UC-TASK-LIST")
    criterion = next(c for c in case["acceptance_criteria"] if c["id"] == "AC-TASK-LIST-EMPTY")
    criterion["statement"][0]["text"] = (
        "A successful consistent read of an empty authorized board returns an empty list and changes no task state "
        "or revision; an unavailable store instead returns failure, never a falsely empty success."
    )
    criterion["verifies"].append("RNF-TASK-LIST-CONSISTENCY")
    # Whole-document equality detects unintended identity, source or contract changes.
    assert atlas_content_equal(expected, after)
    assert before["atlas"]["history"] == after["atlas"]["history"][:-1]
    invalid = copy.deepcopy(after)
    invalid["atlas"]["use_cases"][0]["entities"][0]["entity"] = "ENT-UNKNOWN"
    source = tmp_path / "invalid.json"
    source.write_text(json.dumps(invalid), encoding="utf-8")
    output = tmp_path / "invalid.md"
    with pytest.raises(AtlasError) as error:
        registry.convert_file(source, output, source_format="json", target_format="markdown")
    assert "ATL-E-REF" in {d.code for d in error.value.diagnostics}
    assert not output.exists()
