"""Exercise the edition and skill as independently copied distributions."""

from __future__ import annotations

import itertools
import os
import shutil
import subprocess
import sys
from pathlib import Path

from atlas_spec import atlas_content_equal
from conftest import VERSION_ROOT


FORMATS = {"json": "json", "markdown": "md", "latex": "tex"}
SKILL = VERSION_ROOT / "skills" / "atlas-specs"


def _cli(launcher: Path, *args: str, cwd: Path) -> subprocess.CompletedProcess:
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    # Isolated mode excludes the working directory and user site. The launcher's
    # own relative-runtime lookup must supply atlas_spec for these commands.
    result = subprocess.run(
        [sys.executable, "-I", str(launcher), *map(str, args)],
        cwd=cwd,
        env=environment,
        text=True,
        capture_output=True,
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return result


def _portable_roundtrips(launcher: Path, source: Path, work: Path, registry):
    work.mkdir()
    original = registry.decode_to_atlas_json(source, source_format="json")
    sources = {"json": source}
    for name in ("markdown", "latex"):
        target = work / f"source.atlas.{FORMATS[name]}"
        _cli(launcher, "convert", source, "--from", "json", "--to", name, "-o", target, cwd=work)
        sources[name] = target
    for source_format, target_format in itertools.permutations(FORMATS, 2):
        output = work / f"{source_format}-to-{target_format}.atlas.{FORMATS[target_format]}"
        _cli(
            launcher, "convert", sources[source_format], "--from", source_format,
            "--to", target_format, "-o", output, cwd=work,
        )
        # Read the actual written output with the reference runtime. Do not
        # infer preservation from the command's status or its success message.
        recovered = registry.decode_to_atlas_json(output, source_format=target_format)
        assert atlas_content_equal(original, recovered)


def test_starter_representations_recover_the_same_payload(registry, tmp_path):
    paths = {
        name: VERSION_ROOT / "implementations" / name / f"starter.atlas.{suffix}"
        for name, suffix in FORMATS.items()
    }
    original = registry.decode_to_atlas_json(paths["json"], source_format="json")
    for name, path in paths.items():
        recovered = registry.decode_to_atlas_json(path, source_format=name)
        assert atlas_content_equal(original, recovered)
    for source_format, target_format in itertools.permutations(FORMATS, 2):
        output = tmp_path / f"{source_format}-to-{target_format}.{FORMATS[target_format]}"
        registry.convert_file(
            paths[source_format], output,
            source_format=source_format, target_format=target_format,
        )
        recovered = registry.decode_to_atlas_json(output, source_format=target_format)
        assert atlas_content_equal(original, recovered)


def test_standalone_edition_has_its_runtime_and_resources(tmp_path, registry):
    edition = tmp_path / "edition"
    shutil.copytree(
        VERSION_ROOT, edition,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.egg-info", ".pytest_cache", "build", "dist", "work"),
    )
    launcher = edition / "translator" / "atlas_translate.py"
    listing = _cli(launcher, "formats", cwd=tmp_path)
    assert "Alpha-v0.1.0" in listing.stdout
    _cli(launcher, "validate", edition / "examples" / "minimal" / "example.atlas.json", cwd=tmp_path)
    _portable_roundtrips(
        launcher, edition / "implementations" / "json" / "starter.atlas.json",
        tmp_path / "edition-output", registry,
    )


def test_standalone_skill_executes_all_six_conversions(tmp_path, registry):
    skill = tmp_path / "atlas-specs"
    shutil.copytree(SKILL, skill, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "work"))
    launcher = skill / "scripts" / "atlas_translate.py"
    listing = _cli(launcher, "formats", cwd=tmp_path)
    assert "Alpha-v0.1.0" in listing.stdout
    _portable_roundtrips(
        launcher, skill / "assets" / "starter.atlas.json",
        tmp_path / "skill-output", registry,
    )


def test_skill_runtime_is_the_exact_generated_distribution():
    canonical = VERSION_ROOT / "translator" / "src" / "atlas_spec"
    bundled = SKILL / "scripts" / "vendor" / "atlas_spec"

    def files(root):
        return {
            path.relative_to(root): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file() and path.suffix in {".py", ".json", ".sty"}
        }

    assert files(canonical) == files(bundled)
    assert (VERSION_ROOT / "translator" / "atlas_translate.py").read_bytes() == (
        SKILL / "scripts" / "atlas_translate.py"
    ).read_bytes()
