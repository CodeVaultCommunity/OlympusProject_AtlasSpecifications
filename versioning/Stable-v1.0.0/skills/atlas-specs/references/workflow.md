# Workflow details and diagnostics

## Minimum context for useful authorship

Establish the goal, scope, initiating actors, caller-context origin, permitted actions, inputs, observable outcomes and available evidence. Identify provided facts, requested requirements, provisional assumptions and open decisions. Missing evidence must remain visible rather than becoming invented stakeholder intent.

An empty starter may validate while all domain obligations remain pending. Before declaring a useful case specification, supply its objective, permitted actor context, inputs, behavior/flow, domain validity, outcomes, failures, quality and observable acceptance. Keep the supported scope explicit.

## Requirement example

Given a supplied rule that only a library owner can register a book, a useful requirement states that the case receives a trusted resolved owner context and denies a missing, unresolved or unpermitted context before invoking the store. Acceptance names the attempted operation, input context, observed denial and absence of protected effects. A sentence such as “the application must be secure” does not establish these conditions.

Do not add response-time targets, transaction mechanisms, database vendors or web routes without a source or explicit design decision. A speculative numerical target must remain an identified assumption or open question.

## Common authoring checks

- Keep intrinsic entity validity canonical. Construction/hydration validates raw data; tools accept ready entities, and cases apply authorization and use-case rules.
- State abstract tool inputs and material results. Distinguish refusal, confirmed success, confirmed absence of a write and an unknown write outcome. Failure does not itself prove no write occurred.
- Preserve caller context across composition. A case-call retains its target identity and failure/authorization obligations.
- Trace sources to RF/RNF and acceptance to obligations. Keep scope targets meaningful; a validation ID is not automatically an allowed RF scope.
- Link RFs and graph elements reciprocally. A node referenced by an RF must also name that RF.
- Preserve opaque entity-example data, `meta` and `extensions`. A literal key named `text`, `id` or `@text` is not automatically an Atlas identity or prose slot.

## Diagnose before repairing

| Observation | Next step |
| --- | --- |
| Schema/type error | Read the field definition; correct the structure without inventing business values. |
| Duplicate or unresolved ID | Locate definitions and references; repair their mapping explicitly. |
| Stale derived region | Edit authoritative content and regenerate its display. |
| Missing resource or hash mismatch | Verify package root and original bytes; request a genuinely missing asset instead of inventing a replacement. |
| Unsupported version | Use the matching edition or propose a reviewed migration; never relabel a header to bypass validation. |
| Different round-trip payload | Stop and localize the changed text, field or type. |
| Empty or vague behavior | Report semantic incompleteness even if the schema accepts it. |
| LaTeX/layout problem | Preserve source and prior PDF, diagnose engine/style/resources, then render and inspect the corrected publication. |

## Completion evidence

For authoring, report sources, assumptions/open issues and revision. For review, locate findings by ID and field. For conversion, name actual formats and checks. For publication, name the engine and visually inspected pages. Keep document evidence separate from assertions about a future software implementation.

## Publication decoration

Treat colors, typography, cover ornament and purely decorative images as publication choices. Use the supplied LaTeX style and optional `atlas-presentation.tex` settings file; neither changes the Atlas payload. Do not put requirements or meaningful diagrams into decoration to avoid resource validation. Catalog images that explain specification information and retain their required text and bytes. Conversion recreates the default presentation and does not serialize local theme settings or decorative files into JSON; a sidecar already present in the publication directory can be reused when compiling. Copy those files separately when reproducing a custom publication. TeX loads the sidecar only during PDF compilation, so use intended local publication settings rather than treating an unreviewed file as specification data.
