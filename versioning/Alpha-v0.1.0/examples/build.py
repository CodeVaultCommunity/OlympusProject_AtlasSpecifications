#!/usr/bin/env python3
"""Regenerate readable examples and starters from their canonical JSON.

From the edition: python examples/build.py [--check | --pdf].
--check reads the distributed files and tests all six conversion directions.
--pdf also compiles the three example publications with pdfLaTeX.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EDITION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EDITION / "translator/src"))

from atlas_spec import AdapterRegistry, atlas_content_equal  # noqa: E402

FORMATS = ("json", "markdown", "latex")
EXTENSIONS = {"json": "json", "markdown": "md", "latex": "tex"}


def documents() -> list[tuple[str, dict[str, Path], Path]]:
    result = []
    for source in sorted((EDITION / "examples").glob("*/example.atlas.json")):
        paths = {fmt: source.parent / ("example.atlas." + EXTENSIONS[fmt]) for fmt in FORMATS}
        result.append((source.parent.name, paths, source.parent))
    paths = {fmt: EDITION / "implementations" / fmt / ("starter.atlas." + EXTENSIONS[fmt]) for fmt in FORMATS}
    result.append(("starter", paths, paths["json"].parent))
    return result


def traceability(document: dict) -> str:
    """Derive the reference example's matrix without inventing obligations."""
    atlas = document["atlas"]
    acceptance = [item for case in atlas["use_cases"] for item in case["acceptance_criteria"]]
    lines = [
        "# Task-board traceability / Rastreabilidade do quadro", "",
        "[English guide](README.md) · [Guia em português](README.pt-br.md) · [JSON](example.atlas.json)", "",
        "Generated from the JSON instance by `examples/build.py`. IDs are exact; this matrix records specification links and does not claim execution of a business application.", "",
        "Gerada a partir da instância JSON por `examples/build.py`. Os IDs são exatos; a matriz registra vínculos da especificação e não afirma execução de uma aplicação de negócio.", "",
        "**Origin / Origem:** `SRC-TASK-BRIEF`, revision / revisão 1 (synthetic / sintética).", "",
    ]
    def code(values: list[str]) -> str:
        return "<br>".join("`" + value + "`" for value in values) or "—"
    for case in atlas["use_cases"]:
        lines += ["## " + case["id"], "", "**" + case["name"]["text"] + "**", "",
                  "| Obligation / Obrigação | Graph elements / Elementos do grafo | Acceptance / Aceite | Canonical rules or operations / Regras ou operações |",
                  "| --- | --- | --- | --- |"]
        for requirement in case["functional_requirements"]:
            text = " ".join(block.get("text", "") for block in requirement["statement"])
            dependencies = sorted(set(re.findall(r"(?:VLD|OP)-[A-Z0-9-]+", text)))
            checks = [item["id"] for item in acceptance if requirement["id"] in item["verifies"]]
            lines.append("| " + " | ".join([code([requirement["id"]]), code(requirement["flow_refs"]), code(checks), code(dependencies)]) + " |")
        lines += ["", "| Quality obligation / Obrigação de qualidade | Scope and targets / Escopo e alvos | Canonical definition / Definição canônica | Acceptance / Aceite |", "| --- | --- | --- | --- |"]
        for requirement in case["nonfunctional_requirements"]:
            canonical = requirement.get("reference_to", requirement["id"])
            checks = [item["id"] for item in acceptance if requirement["id"] in item["verifies"] or canonical in item["verifies"]]
            lines.append("| " + " | ".join([code([requirement["id"]]), requirement["scope"] + ": " + code(requirement["applies_to"]), code([canonical]), code(checks)]) + " |")
        lines += [""]
    lines += ["## Interpretation / Interpretação", "",
              "- RF links are reciprocal: each referenced node or edge names the RF, and the RF lists those elements.",
              "- Os vínculos de RF são recíprocos: cada nó ou aresta referencia o RF, e o RF lista esses elementos.",
              "- RNFs retain their scope and origin; references point to a canonical definition.",
              "- RNFs preservam escopo e origem; referências apontam para uma definição canônica.",
              "- Acceptance descriptions are future implementation obligations. Translator tests check document consistency and preservation.",
              "- Critérios de aceite são obrigações da implementação futura. Testes do tradutor conferem consistência e preservação documental.", ""]
    return "\n".join(lines)


def check_documents(registry: AdapterRegistry) -> int:
    conversions = 0
    with tempfile.TemporaryDirectory(prefix="atlas-examples-check-") as temporary:
        for label, paths, resource_root in documents():
            decoded = {fmt: registry.decode_to_atlas_json(path, source_format=fmt, resource_root=resource_root) for fmt, path in paths.items()}
            if any(not atlas_content_equal(decoded["json"], value) for value in decoded.values()):
                raise ValueError(f"Distributed representations differ: {label}")
            for source_format in FORMATS:
                for target_format in FORMATS:
                    if source_format == target_format:
                        continue
                    target = Path(temporary) / f"{label}-{source_format}-to-{target_format}.{EXTENSIONS[target_format]}"
                    registry.convert_file(paths[source_format], target, source_format=source_format, target_format=target_format, resource_root=resource_root)
                    recovered = registry.decode_to_atlas_json(target, source_format=target_format, resource_root=resource_root)
                    if not atlas_content_equal(decoded["json"], recovered):
                        raise ValueError(f"Payload changed: {label} {source_format} -> {target_format}")
                    conversions += 1
            print(f"Verified {label}: three representations, six conversions")
    source = EDITION / "examples/task-board/example.atlas.json"
    expected = traceability(json.loads(source.read_text(encoding="utf-8")))
    if (source.parent / "traceability.md").read_text(encoding="utf-8") != expected:
        raise ValueError("Task-board traceability matrix is stale; run examples/build.py")
    return conversions


def compile_pdfs(explicit: str | None, keep: bool) -> None:
    executable = explicit or os.environ.get("ATLAS_PDFLATEX") or shutil.which("pdflatex")
    if not executable:
        raise RuntimeError("Install a TeX distribution with pdfLaTeX, or set ATLAS_PDFLATEX.")
    found = shutil.which(executable) or executable
    engine = str(Path(found).absolute())
    if not Path(engine).is_file():
        raise RuntimeError(f"pdfLaTeX executable not found: {engine}")
    style_root = EDITION / "implementations/latex"
    if not (style_root / "atlas.sty").is_file():
        raise RuntimeError("Missing implementations/latex/atlas.sty")
    environment = os.environ.copy()
    environment["TEXINPUTS"] = str(style_root) + os.pathsep + environment.get("TEXINPUTS", "")
    for tex in sorted((EDITION / "examples").glob("*/example.atlas.tex")):
        destination = tex.with_suffix(".pdf")
        with tempfile.TemporaryDirectory(prefix=f"atlas-pdf-{tex.parent.name}-") as temporary:
            build = Path(temporary)
            try:
                for number in (1, 2):
                    result = subprocess.run([engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape", "-output-directory=" + str(build), tex.name], cwd=tex.parent, env=environment, text=True, capture_output=True, timeout=120)
                    if result.returncode:
                        print(result.stdout[-4000:])
                        raise RuntimeError(f"LaTeX failed in pass {number}: {tex}; previous PDF preserved.")
                produced = build / destination.name
                if not produced.is_file() or not produced.read_bytes().startswith(b"%PDF-"):
                    raise RuntimeError(f"No PDF was produced for {tex}; previous PDF preserved.")
                with tempfile.NamedTemporaryFile(prefix=".atlas-pdf-", suffix=".tmp", dir=tex.parent, delete=False) as handle:
                    staged = Path(handle.name)
                try:
                    shutil.copyfile(produced, staged)
                    os.replace(staged, destination)
                finally:
                    staged.unlink(missing_ok=True)
                print(f"Published {tex.parent.name}/{destination.name}")
            finally:
                if keep:
                    for suffix in (".aux", ".log", ".out"):
                        diagnostic = build / (tex.stem + suffix)
                        if diagnostic.is_file():
                            shutil.copyfile(diagnostic, tex.parent / diagnostic.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify without modifying distributed files")
    mode.add_argument("--pdf", action="store_true", help="also compile all example PDFs")
    parser.add_argument("--pdflatex", help="pdfLaTeX executable for --pdf")
    parser.add_argument("--keep-intermediates", action="store_true", help="retain TeX diagnostics with --pdf")
    args = parser.parse_args()
    if (args.pdflatex or args.keep_intermediates) and not args.pdf:
        parser.error("--pdflatex and --keep-intermediates require --pdf")
    registry = AdapterRegistry()
    if args.check:
        print(f"Verified {check_documents(registry)} directed conversions, including the starter.")
        return 0
    for label, paths, resource_root in documents():
        for fmt in ("markdown", "latex"):
            registry.convert_file(paths["json"], paths[fmt], source_format="json", target_format=fmt, resource_root=resource_root)
        print(f"Built {label} Markdown and LaTeX from JSON")
    source = EDITION / "examples/task-board/example.atlas.json"
    (source.parent / "traceability.md").write_text(traceability(json.loads(source.read_text(encoding="utf-8"))), encoding="utf-8")
    if args.pdf:
        compile_pdfs(args.pdflatex, args.keep_intermediates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
