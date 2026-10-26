#!/usr/bin/env python3
"""Build the standalone Atlas skill from this edition's canonical sources.

Run from the edition directory: python skills/build.py [--check].
The check is read-only. Authored skill instructions are never overwritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tomllib
from pathlib import Path

EDITION = Path(__file__).resolve().parents[1]
SKILL = EDITION / "skills" / "atlas-specs"
RUNTIME = EDITION / "translator" / "src" / "atlas_spec"
IGNORED = {"__pycache__", ".pytest_cache"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def runtime_resources() -> dict[Path, Path]:
    return {
        RUNTIME / "schemas" / "atlas.schema.json": EDITION / "implementations/json/atlas.schema.json",
        RUNTIME / "templates" / "atlas.sty": EDITION / "implementations/latex/atlas.sty",
    }


def bundle_files() -> dict[str, bytes]:
    """Return reproducible generated files; preserve prose while relocating links."""
    expected: dict[str, bytes] = {}
    records = []

    def add(source: Path, target: str, data: bytes | None = None) -> None:
        original = source.read_bytes()
        payload = original if data is None else data
        expected[target] = payload
        records.append({"source": source.relative_to(EDITION).as_posix(),
                        "destination": target, "source_sha256": digest(original),
                        "bundled_sha256": digest(payload)})

    documents = {
        EDITION / "COMPATIBILITY.md": "references/compatibility.md",
        EDITION / "DIAGNOSTICS.md": "references/diagnostics.md",
        EDITION / "README.md": "references/atlas-specification.md",
        EDITION / "implementations/json/README.md": "references/atlas-json.md",
        EDITION / "implementations/markdown/README.md": "references/atlas-markdown.md",
        EDITION / "implementations/latex/README.md": "references/atlas-latex.md",
    }
    targets = {source.resolve(): name for source, name in documents.items()}
    targets[(EDITION / "implementations/json/starter.atlas.json").resolve()] = "assets/starter.atlas.json"
    targets[(EDITION / "implementations/latex/atlas-presentation.example.tex").resolve()] = "assets/atlas-presentation.example.tex"
    targets[(EDITION / "implementations/json/atlas.schema.json").resolve()] = "scripts/vendor/atlas_spec/schemas/atlas.schema.json"
    targets[(EDITION / "implementations/latex/atlas.sty").resolve()] = "scripts/vendor/atlas_spec/templates/atlas.sty"
    targets[(EDITION / "translator/atlas_translate.py").resolve()] = "scripts/atlas_translate.py"
    targets[(EDITION / "skills/atlas-specs/SKILL.md").resolve()] = "SKILL.md"
    targets[(EDITION / "LICENSE").resolve()] = "LICENSE"

    for source, target in documents.items():
        body = source.read_text(encoding="utf-8")
        body = re.sub(r"<img\b[^>]*>", "", body, flags=re.IGNORECASE)
        body = re.sub(r"!\[([^\]]*)\]\([^\n)]+\)", r"\1 (illustration in the edition)", body)
        body = re.sub(r"<p[^>]*>\s*</p>", "", body)

        def relocate(match: re.Match) -> str:
            label, url = match.group(1), match.group(2)
            if url.startswith(("https://", "http://", "mailto:", "#")):
                return match.group(0)
            path, mark, fragment = url.partition("#")
            found = targets.get((source.parent / path).resolve())
            if found is None:
                return label + " (edition source: `" + url + "`)"
            relative = Path(os.path.relpath(SKILL / found, (SKILL / target).parent)).as_posix()
            return "[" + label + "](" + relative + (mark + fragment if mark else "") + ")"

        # HTML language-navigation links need relocation as well. Normalize
        # anchors to Markdown before applying the same destination map.
        body = re.sub(r'<a\s+href="([^"]+)"\s*>(.*?)</a>', r'[\2](\1)', body)
        body = re.sub(r"\[([^\]]+)\]\(([^\s)]+)\)", relocate, body)
        prefix = "> Canonical English source: `" + source.relative_to(EDITION).as_posix() + "`. This snapshot relocates links for standalone use. Follow SKILL.md for commands inside this bundle.\n\n"
        add(source, target, (prefix + body).encode("utf-8"))

    add(EDITION / "translator/atlas_translate.py", "scripts/atlas_translate.py")
    config = EDITION / "pyproject.toml"
    dependencies = tomllib.loads(config.read_text(encoding="utf-8"))["project"]["dependencies"]
    add(config, "scripts/requirements.txt", ("\n".join(dependencies) + "\n").encode("utf-8"))
    overlays = runtime_resources()
    for source in sorted(RUNTIME.rglob("*")):
        if not source.is_file() or any(x in IGNORED for x in source.parts) or source.suffix == ".pyc":
            continue
        canonical = overlays.get(source, source)
        add(canonical, "scripts/vendor/atlas_spec/" + source.relative_to(RUNTIME).as_posix())
    add(EDITION / "implementations/json/starter.atlas.json", "assets/starter.atlas.json")
    add(EDITION / "implementations/latex/atlas-presentation.example.tex", "assets/atlas-presentation.example.tex")
    add(EDITION / "LICENSE", "LICENSE")
    expected["source-map.json"] = (json.dumps({
        "edition": "Stable-v1.0.0",
        "canonical_runtime": "translator/src/atlas_spec",
        "purpose": "Source correspondence for a generated standalone skill; not proof of semantic completeness.",
        "files": records,
    }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return expected


def synchronize(check: bool = False) -> bool:
    if not (SKILL / "SKILL.md").is_file():
        raise SystemExit("Missing authored skills/atlas-specs/SKILL.md")
    changes: list[str] = []
    for target, source in runtime_resources().items():
        data = source.read_bytes()
        if not target.is_file() or target.read_bytes() != data:
            changes.append(target.relative_to(EDITION).as_posix())
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
    expected = bundle_files()
    previous = SKILL / "source-map.json"
    owned = {"source-map.json"}
    if previous.is_file():
        owned.update(row["destination"] for row in json.loads(previous.read_text(encoding="utf-8"))["files"])
    for name in sorted(owned - set(expected)):
        target = SKILL / name
        if target.is_file():
            changes.append("obsolete " + name)
            if not check:
                target.unlink()
    for name, data in expected.items():
        target = SKILL / name
        if not target.is_file() or target.read_bytes() != data:
            changes.append(name)
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
    if not check:
        for cache in SKILL.rglob("__pycache__"):
            shutil.rmtree(cache)
        for directory in sorted((p for p in SKILL.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
            if not any(directory.iterdir()):
                directory.rmdir()
    if check and changes:
        print("Skill or packaged resources are stale:")
        for name in changes:
            print("  " + name)
        return False
    print(("Verified" if check else "Built") + f" standalone skill: {len(expected)} generated files")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare without modifying files")
    return 0 if synchronize(parser.parse_args().check) else 1


if __name__ == "__main__":
    raise SystemExit(main())
