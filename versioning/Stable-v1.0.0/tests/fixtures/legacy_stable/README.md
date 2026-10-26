# Legacy Stable LaTeX inputs

These three fixtures were generated on 2026-10-26 with the unchanged runtime
from Atlas commit `e3552b4508a3cd84aee153cb3920ca7314e851c7`.
They use the canonical JSON examples after the six-file
editorial corrections recorded in `verification/editorial-migration.json`, before
any publication renderer changes. They contain the legacy diagram layout and
authoritative text records without the removed editorial credits.

`test_publication_layout.py` imports each fixture with the current runtime and
compares its complete payload to the corresponding cleaned canonical example.
It then regenerates and reimports the current layout. Legacy and current TikZ
regions are each checked against their exact renderer; arbitrary edits remain
invalid. The legacy fixtures are deliberate inputs, not generated copies to
refresh when the current presenter changes.
