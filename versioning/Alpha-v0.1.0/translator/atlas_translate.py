#!/usr/bin/env python3
"""Run the version-local Atlas translator, also when bundled inside its skill.

The file is deliberately identical in the public translator directory and skill.
It never installs dependencies, fetches resources, or migrates document versions.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    if sys.version_info < (3, 11):
        print("Atlas requires Python 3.11 or newer.", file=sys.stderr)
        return 2
    here = Path(__file__).resolve().parent
    candidates = (here / "vendor", here / "src")
    source = next((path for path in candidates if (path / "atlas_spec" / "cli.py").is_file()), None)
    if source is None:
        print("Atlas runtime missing: keep this launcher next to src/atlas_spec or vendor/atlas_spec.", file=sys.stderr)
        return 2
    sys.path.insert(0, str(source))
    try:
        from atlas_spec.cli import main as atlas_main
    except ModuleNotFoundError as exc:
        print(f"Missing dependency: {exc.name}. Install this edition with Python pip, or use scripts/requirements.txt inside the standalone skill.", file=sys.stderr)
        return 2
    return atlas_main()


if __name__ == "__main__":
    raise SystemExit(main())
