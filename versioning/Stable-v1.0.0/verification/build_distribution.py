"""Archive the committed repository, including intentional derived artifacts.

Producer only: python verification/build_distribution.py --output /path/Atlas_Stable.zip
The extracted distribution and its integrity checker do not require Git.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path, PurePosixPath
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[3]
FORBIDDEN = {".git", ".venv", "__pycache__", ".pytest_cache", "build", "dist"}
TEMP_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"}


def unwanted(name: str) -> bool:
    path = PurePosixPath(name)
    return (any(p in FORBIDDEN or p.endswith(".egg-info") or p.startswith(("pytest-", ".atlas-pdf-")) for p in path.parts)
            or path.suffix in TEMP_SUFFIXES or name.endswith(".synctex.gz"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"Output already exists: {output}")
    subprocess.run(["git", "diff", "--exit-code", "--quiet", "HEAD", "--"], cwd=ROOT, check=True)
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "-z", "HEAD"], cwd=ROOT).decode("utf-8").split("\0")
    forbidden = [p for p in names if p and unwanted(p)]
    if forbidden:
        raise SystemExit("Tracked temporary files must be removed before packaging: " + ", ".join(forbidden))
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "archive", "--format=zip", "--prefix=Atlas_Stable/", "--output=" + str(output), "HEAD"], cwd=ROOT, check=True)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or any(unwanted(p) for p in archive.namelist()):
            raise SystemExit("Archive failed integrity or temporary-file inspection")
        files = sum(not info.is_dir() for info in archive.infolist())
    print(f"Archive: {output}\nFiles: {files}\nSHA-256: {hashlib.sha256(output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
