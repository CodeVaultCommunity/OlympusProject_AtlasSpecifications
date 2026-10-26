# Atlas translator 0.1.0

[English](README.md) · [Português (Brasil)](README.pt-br.md)

Python 3.11+ implementation of the **Atlas JSON**, **Atlas Markdown** and **Atlas LaTeX** profiles for Atlas Specifications `Alpha-v0.1.0`. It translates representations of the same Atlas content; it does not derive OAL L2 artifacts, migrate specification versions, or import arbitrary Markdown/LaTeX.

## Install and run

Run all commands from the **edition directory**, which contains `pyproject.toml`. Create and activate a Python virtual environment first:

```bash
python -m pip install .
python translator/atlas_translate.py formats
python translator/atlas_translate.py validate examples/task-board/example.atlas.json
python translator/atlas_translate.py convert examples/task-board/example.atlas.json --from json --to markdown -o work/task-board.atlas.md
python translator/atlas_translate.py convert work/task-board.atlas.md --from markdown --to latex -o work/task-board.atlas.tex
```

The installed command `atlas-spec` exposes the same interface as the [Python launcher](atlas_translate.py). The launcher selects only the runtime beside it, so copying the edition preserves its behavior. The standalone [AI skill](../skills/atlas-specs/SKILL.md) carries an identical launcher and a generated copy of the same runtime.

## Translation contract

The four primitives are Markdown → JSON, JSON → Markdown, LaTeX → JSON and JSON → LaTeX. Markdown ↔ LaTeX is composed through validated Atlas JSON, giving six directed conversions. An intermediate disk file is unnecessary.

Every default CLI conversion and `AdapterRegistry.convert_file` validates the source, encodes the target, decodes that target again and compares the complete `atlas` payload before writing. The comparison ignores transport wrapper metadata (`format`, `$schema`), ignores object member order, and preserves array order, scalar types, absent/null/empty distinctions and exact authored text. It rejects content changes instead of reporting a successful conversion.

The CLI option `--no-verify` explicitly skips the final comparison and reports that limitation. `--no-check-resources` skips resource-byte checks and cannot establish resource preservation. Neither flag is needed for the supplied examples.

Resources are not rewritten by conversion. Keep the output in the same package, or pass `--resources PATH` to identify the shared resource root. To publish a self-contained folder:

```bash
python translator/atlas_translate.py package examples/minimal/example.atlas.json --from json -o work/request-package
python translator/atlas_translate.py convert work/request-package/example.atlas.json --from json --to latex -o work/request-package/example.atlas.tex
```

That folder includes the source instance, local resources and `atlas.sty`. PDF is a compiled view of Atlas LaTeX, not a fourth interchange profile. Rebuild the supplied PDFs with `python examples/build.py --pdf`; JSON/Markdown/LaTeX conversion itself needs no TeX installation. The [LaTeX guide](../implementations/latex/README.md) explains publication of other documents.

## Python API

```python
from pathlib import Path
from atlas_spec import AdapterRegistry, atlas_content_equal

registry = AdapterRegistry()
source = Path("examples/task-board/example.atlas.json")
document = registry.decode_to_atlas_json(source, source_format="json")
markdown = registry.encode_from_atlas_json(document, target_format="markdown")
recovered = registry.decode_to_atlas_json(markdown, source_format="markdown")
assert atlas_content_equal(document, recovered)
```

`encode_from_atlas_json` and `decode_to_atlas_json` are separate low-level operations. Use `convert_file` for conversion combined with the post-encoding check. The package also exports `Adapter`, `DecodeOptions`, `EncodeOptions`, `JsonAdapter`, `MarkdownAdapter`, `LatexAdapter`, `Validator`, `validate_document` and diagnostic classes derived from `AtlasError`. `Validator` checks the published structural/referential rules and local resources. It cannot prove that a project's prose is truthful or meets every OAL semantic obligation; that review is separate.

## Verification

From the edition directory:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python skills/build.py --check
```

The tests exercise conversion cycles, exact Unicode/line-ending preservation, diagnostics, resources, transport-wrapper handling, type-aware equality, reciprocal RF/flow links, package installation, starter equivalence and execution of copied edition/skill folders. The installation test uses a temporary virtual environment with network resolution disabled and reuses the test environment's dependency path; installation and entry-point failures fail the test.

Packaged schema and style copies must equal the published files in `implementations/`. `skills/build.py` updates the distribution copies; `--check` reports differences without changing them. The [edition manual](../README.md) defines the preservation contract, translation process and conformance scope.

**Author:** Douglas de Oliveira Alkimim. [MIT license](../LICENSE).
