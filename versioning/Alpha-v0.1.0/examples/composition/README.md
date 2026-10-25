# Booking desk composition

[Português](README.pt-br.md) · [Examples](../README.md)

A synthetic three-case specification demonstrating reuse without losing the called contract: cancellation invokes lookup with the same trusted caller context and must also satisfy lookup authorization. Each case denies missing, unresolved or insufficient context before invoking collaborators.

| Case | Main obligation | Shared elements |
| --- | --- | --- |
| `UC-BOOKING-LOOKUP` | Validate code, load one ready Booking, distinguish confirmed absence and failure. | `ENT-BOOKING`, `VLD-BOOKING-CODE`, `OP-BOOKING-LOAD` |
| `UC-BOOKING-CREATE` | Validate code/title, create a ready active Booking, atomically insert using expected version zero. | `ENT-BOOKING`, `VLD-BOOKING-CODE`, `VLD-BOOKING-TITLE`, `OP-BOOKING-SAVE` |
| `UC-BOOKING-CANCEL` | Preserve lookup outcomes, apply the canonical transition and conditionally save using the observed version. | `UC-BOOKING-LOOKUP`, `VLD-BOOKING-CANCEL`, `OP-BOOKING-SAVE` |

Read the [JSON](example.atlas.json), [Markdown](example.atlas.md), [LaTeX](example.atlas.tex) or derived [PDF](example.atlas.pdf). The command-line boundary is an illustrative proposal, not a mandatory L1 choice.

`BOOK001` is the valid identifier example: the canonical rule allows uppercase letters and digits only, between 1 and 12 characters. A value such as `BOOK-001` violates that rule. Lowercase/punctuation examples remain explicitly invalid.

`SRC-BOOKING-BRIEF`, revision 2, records the synthetic origin. The shared two-second response condition and 30-request verification scenario demonstrate canonical definition plus reference; they are illustrative assumptions, not an approved SLA or an executed performance result.

The shared save contract explicitly distinguishes version zero (insert if absent) from a positive observed version (conditional replacement). A conflict guarantees that this invocation made no change; another invocation may have changed the record. Lost write confirmation preserves `unknown`, without automatic retry.

## Author

Douglas de Oliveira Alkimim.
