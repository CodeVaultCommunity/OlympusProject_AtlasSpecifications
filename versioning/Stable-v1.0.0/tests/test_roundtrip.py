from __future__ import annotations

import copy
from pathlib import Path

import pytest

from atlas_spec.util import read_text_exact

from atlas_spec import AtlasError


FORMATS = ("json", "markdown", "latex")


def encode(registry, document, target, root, check_resources=True):
    return registry.encode_from_atlas_json(
        document,
        target_format=target,
        resource_root=root,
        check_resources=check_resources,
    )


def decode(registry, text, source, root, check_resources=True):
    return registry.decode_to_atlas_json(
        text,
        source_format=source,
        resource_root=root,
        check_resources=check_resources,
    )


@pytest.mark.parametrize("example_name", ["minimal", "composition", "task_board"])
@pytest.mark.parametrize("source,target", [
    ("markdown", "json"),
    ("json", "markdown"),
    ("latex", "json"),
    ("json", "latex"),
])
def test_four_fundamental_transformations(registry, example_name, source, target, request):
    directory = request.getfixturevalue(f"{example_name}_dir")
    document = request.getfixturevalue(example_name)
    if source == "json":
        encoded = encode(registry, document, target, directory)
    else:
        source_text = read_text_exact(directory / f"example.atlas.{'md' if source == 'markdown' else 'tex'}")
        decoded = decode(registry, source_text, source, directory)
        assert decoded == document
        encoded = encode(registry, decoded, target, directory)
    recovered = decode(registry, encoded, target, directory)
    assert recovered == document


@pytest.mark.parametrize("example_name", ["minimal", "composition", "task_board"])
@pytest.mark.parametrize("source,target", [
    ("markdown", "latex"),
    ("latex", "markdown"),
])
def test_six_directions_include_cross_format(registry, example_name, source, target, request, tmp_path):
    directory = request.getfixturevalue(f"{example_name}_dir")
    document = request.getfixturevalue(example_name)
    source_suffix = "md" if source == "markdown" else "tex"
    source_path = tmp_path / f"source.{source_suffix}"
    source_path.write_text(
        read_text_exact(directory / f"example.atlas.{source_suffix}"),
        encoding="utf-8",
        newline="",
    )
    target_path = tmp_path / f"target.{'md' if target == 'markdown' else 'tex'}"
    converted = registry.convert_file(
        source_path,
        target_path,
        source_format=source,
        target_format=target,
        resource_root=directory,
        check_resources=True,
    )
    assert converted == document
    recovered = decode(
        registry,
        read_text_exact(target_path),
        target,
        directory,
    )
    assert recovered == document


@pytest.mark.parametrize("example_name", ["minimal", "composition", "task_board"])
@pytest.mark.parametrize("path", [
    ("json", "markdown", "latex", "json"),
    ("json", "latex", "markdown", "json"),
    ("markdown", "latex", "markdown", "json"),
    ("latex", "markdown", "latex", "json"),
])
def test_cycles_through_all_formats(registry, example_name, path, request):
    directory = request.getfixturevalue(f"{example_name}_dir")
    document = request.getfixturevalue(example_name)
    current_text = None
    current_format = path[0]
    if current_format != "json":
        suffix = "md" if current_format == "markdown" else "tex"
        current_text = read_text_exact(directory / f"example.atlas.{suffix}")
    for target in path[1:]:
        source_document = (
            document
            if current_format == "json"
            else decode(registry, current_text, current_format, directory)
        )
        current_text = encode(registry, source_document, target, directory)
        current_format = target
    final = decode(registry, current_text, current_format, directory)
    assert final == document


@pytest.mark.parametrize("example_name", ["minimal", "composition", "task_board"])
def test_encoders_are_deterministic(registry, example_name, request):
    directory = request.getfixturevalue(f"{example_name}_dir")
    document = request.getfixturevalue(example_name)
    for target in ("markdown", "latex", "json"):
        first = encode(registry, document, target, directory)
        second = encode(registry, document, target, directory)
        assert first == second


@pytest.mark.parametrize("example_name", ["minimal", "composition", "task_board"])
def test_format_switch_is_not_a_version_migration(registry, example_name, request):
    directory = request.getfixturevalue(f"{example_name}_dir")
    document = request.getfixturevalue(example_name)
    original_meta = (
        document["atlas"]["spec_version"],
        document["atlas"]["profile_version"],
        document["atlas"]["translator_version"],
        document["atlas"]["revision"],
    )
    for target in FORMATS:
        encoded = encode(registry, document, target, directory)
        recovered = decode(registry, encoded, target, directory)
        assert (
            recovered["atlas"]["spec_version"],
            recovered["atlas"]["profile_version"],
            recovered["atlas"]["translator_version"],
            recovered["atlas"]["revision"],
        ) == original_meta


def test_tricky_text_markdown_and_latex(registry, tricky_document, minimal_dir):
    registry.validator.validate(tricky_document, resource_root=minimal_dir)
    for target in ("markdown", "latex"):
        text = encode(registry, tricky_document, target, minimal_dir)
        recovered = decode(registry, text, target, minimal_dir)
        assert recovered == tricky_document


def test_tricky_text_three_format_cycle(registry, tricky_document, minimal_dir):
    md = encode(registry, tricky_document, "markdown", minimal_dir)
    direct = decode(registry, md, "markdown", minimal_dir)
    tex = encode(registry, direct, "latex", minimal_dir)
    via = decode(registry, tex, "latex", minimal_dir)
    back = encode(registry, via, "markdown", minimal_dir)
    final = decode(registry, back, "markdown", minimal_dir)
    assert final == tricky_document


def test_source_without_final_newline(registry, minimal, minimal_dir):
    for fmt, suffix in (("markdown", "md"), ("latex", "tex")):
        original = read_text_exact(minimal_dir / f"example.atlas.{suffix}")
        assert original.endswith("\n")
        without_final = original[:-1]
        recovered = decode(registry, without_final, fmt, minimal_dir)
        assert recovered == minimal


def test_crlf_and_unicode_are_not_normalized(registry, tricky_document, minimal_dir):
    text = encode(registry, tricky_document, "markdown", minimal_dir)
    recovered = decode(registry, text, "markdown", minimal_dir)
    blocks = recovered["atlas"]["structure"][-1]["blocks"]
    values = [block.get("text") for block in blocks if block.get("type") == "paragraph"]
    assert "CRLF:\r\nnext line" in values
    assert "composed: \u00e9  decomposed: e\u0301" in values
    assert "\u00e9" != "e\u0301"


@pytest.mark.parametrize("variant", ["absent", "null", "empty"])
def test_missing_null_and_empty_subtitle(registry, minimal, minimal_dir, variant):
    document = copy.deepcopy(minimal)
    if variant == "absent":
        document["atlas"].pop("subtitle", None)
    elif variant == "null":
        document["atlas"]["subtitle"] = None
    else:
        document["atlas"]["subtitle"] = {"text": ""}
    for target in ("markdown", "latex", "json"):
        text = encode(registry, document, target, minimal_dir)
        assert decode(registry, text, target, minimal_dir) == document


@pytest.mark.parametrize("variant", ["absent", "empty"])
def test_missing_and_empty_optional_notes(registry, minimal, minimal_dir, variant):
    document = copy.deepcopy(minimal)
    if variant == "absent":
        document["atlas"].pop("notes", None)
    else:
        document["atlas"]["notes"] = []
    for target in ("markdown", "latex", "json"):
        text = encode(registry, document, target, minimal_dir)
        assert decode(registry, text, target, minimal_dir) == document


def test_latex_body_text_edit_is_imported(registry, minimal, minimal_dir):
    original = read_text_exact(minimal_dir / "example.atlas.tex")
    changed = original.replace("Minimal request register", "Edited title in LaTeX", 1)
    assert changed != original
    recovered = decode(registry, changed, "latex", minimal_dir)
    assert recovered["atlas"]["title"]["text"] == "Edited title in LaTeX"
    assert recovered["atlas"]["structure"] == minimal["atlas"]["structure"]


def test_body_text_edit_is_imported(registry, minimal, minimal_dir):
    original = read_text_exact(minimal_dir / "example.atlas.md")
    changed = original.replace("Minimal request register", "Edited title from the body", 1)
    assert changed != original
    recovered = decode(registry, changed, "markdown", minimal_dir)
    assert recovered["atlas"]["title"]["text"] == "Edited title from the body"
    assert recovered["atlas"]["structure"] == minimal["atlas"]["structure"]


def test_structure_edit_in_json_is_not_discarded(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["entities"][0]["fields"][0]["required"] = False
    for target in ("markdown", "latex"):
        text = encode(registry, document, target, minimal_dir)
        recovered = decode(registry, text, target, minimal_dir)
        assert recovered["atlas"]["entities"][0]["fields"][0]["required"] is False


def test_extension_content_is_opaque_and_preserved(registry, minimal, minimal_dir):
    document = copy.deepcopy(minimal)
    document["atlas"]["extensions"] = {
        "example.org/custom": {
            "text": "this text lives in an extension and is not a body record",
            "numbers": [1, 2, 3],
            "null": None,
        }
    }
    for target in ("markdown", "latex"):
        text = encode(registry, document, target, minimal_dir)
        recovered = decode(registry, text, target, minimal_dir)
        assert recovered == document
