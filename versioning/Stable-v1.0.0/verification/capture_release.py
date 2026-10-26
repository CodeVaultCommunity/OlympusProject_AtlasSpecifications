"""Capture/check release inputs before writing RELEASE.md; no circular hashes.

Run from the edition: python verification/capture_release.py [--check].
Requires the complete repository for root documentation/artwork/CI coverage.
Historical checkpoint inputs retain their original manifest and commit scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parents[1]
OUTPUT = EDITION / "verification/release-inputs.json"
SKIP = {".git", ".venv", "__pycache__", ".pytest_cache", "build", "dist", "work"}
SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".out", ".toc", ".gz"}
EXCLUDE = {"verification/RELEASE.md", "verification/RELEASE-DESCRIPTION.md",
           "verification/release-inputs.json"}


def inputs():
    paths = []
    roots = [EDITION, ROOT / "assets", ROOT / ".github"]
    for directory in roots:
        for path in directory.rglob("*"):
            rel = path.relative_to(directory)
            if any(x in SKIP or x.endswith(".egg-info") for x in rel.parts):
                continue
            if not path.is_file() or path.suffix in SUFFIXES:
                continue
            if directory == EDITION and (rel.as_posix() in EXCLUDE or rel.as_posix().startswith("verification/evidence/")):
                continue
            paths.append(path)
    paths += [p for p in ROOT.iterdir() if p.is_file()]
    return [{"path": p.relative_to(ROOT).as_posix(), "bytes": p.stat().st_size,
             "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(paths)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    actual = inputs()
    if args.check:
        expected = json.loads(OUTPUT.read_text(encoding="utf-8"))["files"]
        if expected != actual:
            raise SystemExit("Release inputs changed: rerun affected checks and recapture before updating the report.")
        print(f"Verified {len(actual)} release inputs")
    else:
        manifest = {
            "audited_source_commit": "ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04",
            "scope": "Actual Stable edition, root files, artwork and CI bytes; captured before final report.",
            "alpha_preservation": "Separate initial manifest including Windows ACLs; historical Alpha is excluded here.",
            "exclusions": sorted(EXCLUDE) + ["verification/evidence/**", "versioning/Alpha-v0.1.0/**", "*.egg-info"] + sorted(SKIP) + sorted("*"+s for s in SUFFIXES),
            "files": actual,
        }
        OUTPUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
        print(f"Captured {len(actual)} release inputs")


if __name__ == "__main__":
    main()
