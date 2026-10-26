# Request register

[Português](README.pt-br.md) · [Examples](../README.md)

A smaller synthetic specification centered on `UC-REQUEST-SUBMIT`: resolve authorization, validate the request code and quantity, and request one atomic retained write. It distinguishes invalid data, denial, duplicate identifier and storage uncertainty from confirmation.

- [Atlas JSON](example.atlas.json) is the build fixture and translator intermediate.
- [Atlas Markdown](example.atlas.md) and [Atlas LaTeX](example.atlas.tex) preserve the same content.
- [PDF](example.atlas.pdf) is a derived publication; its graphs are generated from structured graph records.
- [Form wireframe](assets/request-form.svg) is a channel illustration, outside the L1 claim.
- [Submission flow](assets/request-flow.svg) includes every node and edge, with the stable edge key.

The embedded source `SRC-REQUEST-BRIEF`, revision 2, is synthetic. The two-second response target and the 30-request scenario are didactic placeholders requiring real stakeholder and environment evidence before adoption; `OI-REQUEST-LATENCY` keeps that question visible. Authorization is semantic and deny-by-default; authentication implementation remains outside this example.

The example declares code-validity and duplicate-code paths, source provenance, trusted caller context and explicit write outcomes.

The resource catalog retains the original drawing generator name as provenance. Editable SVG sources and their original PNG variants are supplied in `assets/`; `examples/build.py` reuses and verifies these files when rebuilding the document representations.

## Author

Douglas de Oliveira Alkimim.
