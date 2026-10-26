# Atlas Specifications examples

[Português](README.pt-br.md) · [Version guide](../README.md) · [Implementations](../implementations/json/README.md)

These are **synthetic specifications**, not running business applications. Their product rules, actor policies and quality conditions are explicitly identified teaching choices. The files demonstrate Atlas content and representation preservation; passing a document validator does not prove the described application's behavior.

## Choose an example

| Example | Purpose | Stable use-case identities | Representations |
| --- | --- | --- | --- |
| [Task board](task-board/README.md) | Main reference: create, complete and list; caller context, ready entities, atomic persistence and uncertain write outcomes. | `UC-TASK-CREATE`, `UC-TASK-COMPLETE`, `UC-TASK-LIST` | [JSON](task-board/example.atlas.json), [Markdown](task-board/example.atlas.md), [LaTeX](task-board/example.atlas.tex), [PDF](task-board/example.atlas.pdf) |
| [Request register](minimal/README.md) | Smaller example with local image resources, canonical field validity, duplicate refusal and source-linked acceptance. | `UC-REQUEST-SUBMIT` | [JSON](minimal/example.atlas.json), [Markdown](minimal/example.atlas.md), [LaTeX](minimal/example.atlas.tex), [PDF](minimal/example.atlas.pdf) |
| [Booking composition](composition/README.md) | Shared entity/tool, composed case, canonical shared quality obligation and state transition. | `UC-BOOKING-LOOKUP`, `UC-BOOKING-CREATE`, `UC-BOOKING-CANCEL` | [JSON](composition/example.atlas.json), [Markdown](composition/example.atlas.md), [LaTeX](composition/example.atlas.tex), [PDF](composition/example.atlas.pdf) |

JSON, Markdown and LaTeX carry the same Atlas content. PDF is a compiled publication of LaTeX, not a fourth editable implementation. Technical diagrams are derived views; the graph records retain nodes, edges, labels, calls and requirement references. The default publication also has a decorative vector cover drawn by `atlas.sty`; that ornament carries no specification information and is outside the resource catalog. The [publication-style guide](../implementations/latex/README.md#publication-style) explains themes, optional local artwork and the separation between appearance and preserved content.

## Regenerate and verify

The JSON in each example directory is its canonical authored source. From the edition directory:

```bash
python examples/build.py
python examples/build.py --check
python examples/build.py --pdf
```

The first command regenerates Markdown, LaTeX and the task-board traceability matrix. It also generates the Markdown and LaTeX starters from `implementations/json/starter.atlas.json`. `--check` performs a read-only comparison of the distributed representations and exercises all six conversion directions for each example and the starter. `--pdf` regenerates the sources and compiles the three example PDFs with pdfLaTeX and `implementations/latex/atlas.sty`.

Install Python dependencies from this edition's `pyproject.toml`. A TeX distribution is required only for PDF compilation. Use `--pdflatex PATH` or `ATLAS_PDFLATEX` if the executable is not on PATH. Compilation uses a temporary build directory and replaces the existing PDF only after success. `--keep-intermediates` retains TeX diagnostics when used with `--pdf`.

## Scope and provenance

- `task-board/needs.md`, revision 1, is a synthetic teaching baseline. It supplies no evidence of stakeholder approval and asserts no real Needs-to-L1 derivation.
- The request-register source `SRC-REQUEST-BRIEF` and booking source `SRC-BOOKING-BRIEF` are embedded, versioned synthetic briefs. Their numeric timing examples remain didactic assumptions, not production SLAs.
- Every case's `traceability` connects source → RF/RNF and acceptance → obligation. RFs and graph nodes/edges have matching references in both directions.
- The request web form and booking command line are illustrative channel proposals. Their screen/command details do not become mandatory L1 requirements. The task board intentionally chooses no channel.
- A future application must implement and verify persistence, authorization and quality behavior. This repository supplies the specification, representations, translator and their checks.

The [task-board traceability matrix](task-board/traceability.md) gives an inspectable map of the primary reference. These examples belong to the first alpha edition, `Stable-v1.0.0`.

## Author

Douglas de Oliveira Alkimim.
