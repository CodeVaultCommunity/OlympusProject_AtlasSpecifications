"""Keep publication decoration separate from authoritative Atlas content."""

from __future__ import annotations

import copy
import re
import subprocess

import pytest

from atlas_spec import AtlasError, atlas_content_equal
from atlas_spec.util import read_text_exact, write_text_exact


def decorated_source(registry, document, resource_root):
    text = registry.encode_from_atlas_json(
        document, target_format="latex", resource_root=resource_root
    )
    text = text.replace(
        r"\begin{document}",
        "\\AtlasTheme{plain}\n"
        "\\AtlasCoverImage{publication/missing-cover.png}\n"
        "\\begin{document}",
        1,
    )
    return text.replace(
        "\\AtlasEndCover\n",
        "\\AtlasEndCover\n"
        "\\AtlasDecorativeImage[width=0.4\\linewidth]"
        "{publication/missing-ornament.png}\n",
        1,
    )


@pytest.mark.parametrize(
    "target_format,suffix", [("json", "json"), ("markdown", "md"), ("latex", "tex")]
)
def test_decorated_latex_converts_without_images_or_new_resources(
    registry, minimal, minimal_dir, tmp_path, target_format, suffix
):
    source = tmp_path / "source" / "decorated.atlas.tex"
    target = tmp_path / "output" / f"converted.atlas.{suffix}"
    write_text_exact(source, decorated_source(registry, minimal, minimal_dir))

    registry.convert_file(
        source, target, source_format="latex", target_format=target_format,
        resource_root=minimal_dir,
    )
    recovered = registry.decode_to_atlas_json(
        target, source_format=target_format, resource_root=minimal_dir
    )
    assert atlas_content_equal(minimal, recovered)
    assert recovered["atlas"]["resources"] == minimal["atlas"]["resources"]
    assert "missing-cover.png" not in read_text_exact(target)
    assert "missing-ornament.png" not in read_text_exact(target)

    # Convert back to LaTeX, and independently read the generated source.
    returned = tmp_path / "returned" / "specification.atlas.tex"
    registry.convert_file(
        target, returned, source_format=target_format, target_format="latex",
        resource_root=minimal_dir,
    )
    assert atlas_content_equal(
        minimal,
        registry.decode_to_atlas_json(
            returned, source_format="latex", resource_root=minimal_dir
        ),
    )


def test_presentation_sidecar_is_not_read_or_executed(
    registry, minimal, minimal_dir, tmp_path, monkeypatch
):
    source = tmp_path / "specification.atlas.tex"
    write_text_exact(source, decorated_source(registry, minimal, minimal_dir))
    sidecar = tmp_path / "atlas-presentation.tex"
    # An invalid UTF-8 sidecar would fail if the decoder tried to read it.
    # Its TeX and Atlas-looking markers must not enter the payload either.
    sidecar.write_bytes(
        b"\xff\\input{absent-file}\n% atlas:structure:begin\n"
        b"\\begin{atlastext}{T999999}\nnot a requirement\n"
    )
    before = sidecar.read_bytes()

    def no_execution(*args, **kwargs):
        pytest.fail("Conversion must not execute a TeX compiler or sidecar")

    monkeypatch.setattr(subprocess, "run", no_execution)
    target = tmp_path / "converted.atlas.json"
    registry.convert_file(
        source, target, source_format="latex", target_format="json",
        resource_root=minimal_dir,
    )
    assert sidecar.read_bytes() == before
    assert atlas_content_equal(
        minimal,
        registry.decode_to_atlas_json(
            target, source_format="json", resource_root=minimal_dir
        ),
    )
    sidecar.unlink()
    assert atlas_content_equal(
        minimal,
        registry.decode_to_atlas_json(
            source, source_format="latex", resource_root=minimal_dir
        ),
    )


def test_decorations_do_not_make_semantic_resources_optional(
    registry, minimal, minimal_dir, tmp_path
):
    source = tmp_path / "specification.atlas.tex"
    write_text_exact(source, decorated_source(registry, minimal, minimal_dir))
    # No semantic assets were copied into this package. Their catalogued
    # requirements still apply even though decorative files need no catalog.
    with pytest.raises(AtlasError) as error:
        registry.decode_to_atlas_json(
            source, source_format="latex", resource_root=tmp_path
        )
    assert "ATL-E-RESOURCE-MISSING" in {d.code for d in error.value.diagnostics}


def test_decoration_does_not_replace_a_missing_authoritative_record(
    registry, minimal, minimal_dir
):
    text = decorated_source(registry, minimal, minimal_dir)
    text, removed = re.subn(
        r"\\begin\{atlastitle\}\{T[0-9]{6}\}\n.*?\n\\end\{atlastitle\}\n",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )
    assert removed == 1
    with pytest.raises(AtlasError) as error:
        registry.decode_to_atlas_json(
            text, source_format="latex", resource_root=minimal_dir
        )
    assert "ATL-E-SLOT-MISSING" in {d.code for d in error.value.diagnostics}


def test_decoration_commands_inside_authored_text_are_preserved(
    registry, minimal, minimal_dir
):
    document = copy.deepcopy(minimal)
    literal = (
        "This sentence quotes a presentation command literally:\n"
        "\\AtlasDecorativeImage[width=1cm]{publication/ornament.png}\n"
        "It remains authored text, including its final newline.\n"
    )
    document["atlas"]["structure"][0]["blocks"].append(
        {"type": "paragraph", "text": literal}
    )
    text = decorated_source(registry, document, minimal_dir)
    assert atlas_content_equal(
        document,
        registry.decode_to_atlas_json(
            text, source_format="latex", resource_root=minimal_dir
        ),
    )


def test_wrapping_table_preserves_every_cell_once(
    registry, minimal, minimal_dir
):
    document = copy.deepcopy(minimal)
    document["atlas"]["structure"][0]["blocks"].append(
        {
            "type": "table",
            "columns": [
                {"text": "Criterion | exact heading"},
                {"text": "Result & evidence"},
                {"text": "Notes"},
            ],
            "rows": [
                [
                    {"text": f"Long requirement {number}: " + "readable prose " * 24},
                    {"text": "line one\nline two\t% # { } \\"},
                    {"text": "ação, café; trailing spaces  "},
                ]
                for number in range(16)
            ],
            "caption": {"text": "All rows and cells remain authoritative."},
        }
    )
    latex = registry.encode_from_atlas_json(
        document, target_format="latex", resource_root=minimal_dir
    )
    recovered = registry.decode_to_atlas_json(
        latex, source_format="latex", resource_root=minimal_dir
    )
    assert atlas_content_equal(document, recovered)
    markdown = registry.encode_from_atlas_json(
        recovered, target_format="markdown", resource_root=minimal_dir
    )
    assert atlas_content_equal(
        document,
        registry.decode_to_atlas_json(
            markdown, source_format="markdown", resource_root=minimal_dir
        ),
    )
