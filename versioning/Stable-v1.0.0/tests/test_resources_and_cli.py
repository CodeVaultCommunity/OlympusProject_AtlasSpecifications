from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import MINIMAL_DIR, VERSION_ROOT


def test_conversion_does_not_touch_resource_bytes(registry, minimal, tmp_path):
    package = tmp_path / "package"
    shutil.copytree(MINIMAL_DIR / "assets", package / "assets")
    before = {
        path.relative_to(package).as_posix(): path.read_bytes()
        for path in (package / "assets").iterdir()
    }
    for target, suffix in (("json", "json"), ("markdown", "md"), ("latex", "tex")):
        registry.encode_from_atlas_json(
            minimal, target_format=target, resource_root=package
        )
    after = {
        path.relative_to(package).as_posix(): path.read_bytes()
        for path in (package / "assets").iterdir()
    }
    assert after == before


def test_conversion_works_without_network(registry, minimal, minimal_dir):
    text = registry.encode_from_atlas_json(
        minimal, target_format="markdown", resource_root=minimal_dir
    )
    decoded = registry.decode_to_atlas_json(
        text, source_format="markdown", resource_root=minimal_dir
    )
    assert decoded == minimal


def test_cli_validate():
    env = _env()
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "atlas_spec",
            "validate",
            str(MINIMAL_DIR / "example.atlas.md"),
            "--resources",
            str(MINIMAL_DIR),
        ],
        text=True,
        capture_output=True,
        env=env,
        cwd=str(VERSION_ROOT),
    )
    assert result.returncode == 0, result.stderr
    assert "valid:" in result.stdout


def test_cli_convert_markdown_to_latex(tmp_path):
    env = _env()
    output = tmp_path / "converted.tex"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "atlas_spec",
            "convert",
            str(MINIMAL_DIR / "example.atlas.md"),
            "--from",
            "markdown",
            "--to",
            "latex",
            "-o",
            str(output),
            "--resources",
            str(MINIMAL_DIR),
        ],
        text=True,
        capture_output=True,
        env=env,
        cwd=str(VERSION_ROOT),
    )
    assert result.returncode == 0, result.stderr
    assert output.is_file()
    assert "converted:" in result.stdout


def test_cli_rejects_stale_resource(tmp_path):
    package = tmp_path / "package"
    shutil.copytree(MINIMAL_DIR / "assets", package / "assets")
    data = json.loads((MINIMAL_DIR / "example.atlas.json").read_text(encoding="utf-8"))
    data["atlas"]["resources"][0]["sha256"] = "f" * 64
    source = package / "broken.atlas.json"
    source.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "atlas_spec",
            "validate",
            str(source),
        ],
        text=True,
        capture_output=True,
        env=_env(),
        cwd=str(VERSION_ROOT),
    )
    assert result.returncode != 0
    assert "ATL-E-RESOURCE-HASH" in result.stderr


def test_cli_package_copies_instance_and_resources(tmp_path):
    env = _env()
    package = tmp_path / "package"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "atlas_spec",
            "package",
            str(MINIMAL_DIR / "example.atlas.md"),
            "--from",
            "markdown",
            "-o",
            str(package),
            "--resources",
            str(MINIMAL_DIR),
        ],
        text=True,
        capture_output=True,
        env=env,
        cwd=str(VERSION_ROOT),
    )
    assert result.returncode == 0, result.stderr
    assert (package / "example.atlas.md").is_file()
    assert (package / "assets" / "request-form.svg").is_file()
    assert (package / "assets" / "request-form.png").is_file()
    assert (package / "atlas.sty").is_file()
    assert "packaged:" in result.stdout
    # The packaged copy validates against its own resource root.
    validate = subprocess.run(
        [
            sys.executable,
            "-m",
            "atlas_spec",
            "validate",
            str(package / "example.atlas.md"),
        ],
        text=True,
        capture_output=True,
        env=env,
        cwd=str(VERSION_ROOT),
    )
    assert validate.returncode == 0, validate.stderr


def test_cli_lists_formats():
    result = subprocess.run(
        [sys.executable, "-m", "atlas_spec", "formats"],
        text=True,
        capture_output=True,
        env=_env(),
        cwd=str(VERSION_ROOT),
    )
    assert result.returncode == 0, result.stderr
    assert "markdown/Alpha-v0.1.0" in result.stdout
    assert "latex/Alpha-v0.1.0" in result.stdout
    assert "json/Alpha-v0.1.0" in result.stdout


def _env() -> dict[str, str]:
    env = os.environ.copy()
    source = str(VERSION_ROOT / "translator" / "src")
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = source + (os.pathsep + existing if existing else "")
    return env
