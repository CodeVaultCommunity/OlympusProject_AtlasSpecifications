from __future__ import annotations

import os
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

import pytest

from conftest import VERSION_ROOT


def test_packaged_schema_matches_published_schema():
    published = VERSION_ROOT / "implementations" / "json" / "atlas.schema.json"
    packaged = VERSION_ROOT / "translator" / "src" / "atlas_spec" / "schemas" / "atlas.schema.json"
    assert published.read_bytes() == packaged.read_bytes()


def test_packaged_style_matches_published_style():
    published = VERSION_ROOT / "implementations" / "latex" / "atlas.sty"
    packaged = VERSION_ROOT / "translator" / "src" / "atlas_spec" / "templates" / "atlas.sty"
    assert published.read_bytes() == packaged.read_bytes()


@pytest.mark.parametrize("editable", [False, True], ids=["wheel", "editable"])
def test_install_console_script_and_package_data(tmp_path, editable):
    python = sys.executable
    target = tmp_path / "venv"
    result = subprocess.run(
        [python, "-m", "venv", "--system-site-packages", str(target)],
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    scripts = target / ("Scripts" if sys.platform == "win32" else "bin")
    environment_python = scripts / ("python.exe" if sys.platform == "win32" else "python")
    # A nested virtualenv's system-site-packages points to the base interpreter,
    # not the active test environment. Share only its dependency import path;
    # do not require a second network install merely to exercise entry points.
    environment = os.environ.copy()
    environment["PYTHONPATH"] = sysconfig.get_path("purelib")
    source = tmp_path / "edition-source"
    shutil.copytree(
        VERSION_ROOT, source,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.egg-info", ".pytest_cache", ".venv", "build", "dist", "work"),
    )
    command = [str(environment_python), "-m", "pip", "install", "--quiet", "--no-index", "--no-cache-dir", "--no-build-isolation", "--no-deps"]
    if editable:
        command.append("--editable")
    command.append(str(source))
    install = subprocess.run(
        command,
        text=True,
        capture_output=True,
        timeout=180,
        env=environment,
    )
    assert install.returncode == 0, install.stdout + install.stderr
    for name in ("atlas-spec",):
        executable = scripts / (name + ".exe" if sys.platform == "win32" else name)
        version = subprocess.run(
            [str(executable), "formats"],
            text=True,
            capture_output=True,
            env=environment,
        )
        assert version.returncode == 0, version.stdout + version.stderr
        assert "Alpha-v0.1.0" in version.stdout
        package = tmp_path / "document-package"
        result = subprocess.run(
            [str(executable), "package", str(VERSION_ROOT / "examples" / "minimal" / "example.atlas.json"),
             "--from", "json", "--output", str(package)],
            text=True,
            capture_output=True,
            env=environment,
            timeout=60,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        assert (package / "atlas.sty").read_bytes() == (
            VERSION_ROOT / "implementations" / "latex" / "atlas.sty"
        ).read_bytes()
