"""Capture or check the actual working-copy bytes used by this checkpoint.

Run from the edition: python verification/capture_inputs.py [--check].
The report, this manifest, evidence outputs and local build caches are excluded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "verification/checkpoint-inputs.json"
EXCLUDED_NAMES = {".venv", "__pycache__", ".pytest_cache", "build", "dist", "work"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".out", ".toc"}


def inputs():
    result = []
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_NAMES or part.endswith(".egg-info") for part in relative.parts):
            continue
        if not path.is_file() or path.suffix in EXCLUDED_SUFFIXES:
            continue
        name = relative.as_posix()
        if name in {"verification/CHECKPOINT.md", "verification/checkpoint-inputs.json"}:
            continue
        if name.startswith("verification/evidence/"):
            continue
        data = path.read_bytes()
        result.append({"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    actual = inputs()
    if args.check:
        recorded = json.loads(OUTPUT.read_text(encoding="utf-8"))["files"]
        if actual != recorded:
            raise SystemExit("Checkpoint inputs changed; rerun affected checks and capture before revising the report.")
        print(f"Verified {len(actual)} checkpoint input files")
    else:
        manifest = {
            "audited_source_commit": "ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04",
            "working_copy_before_fixes_commit": "d3d485e66590add17cda50b391d657b53aeb127c",
            "scope": "Working bytes of the prepared edition; profiles are still Alpha at this paused checkpoint.",
            "exclusions": ["verification/CHECKPOINT.md", "verification/checkpoint-inputs.json",
                           "verification/evidence/**", *sorted(EXCLUDED_NAMES), "*.egg-info",
                           *sorted('*' + suffix for suffix in EXCLUDED_SUFFIXES)],
            "files": actual,
        }
        OUTPUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"Captured {len(actual)} checkpoint input files before writing the report")


if __name__ == "__main__":
    main()
