# Synthetic task-board brief

**Identity:** `SRC-TASK-BRIEF` · **Revision:** 1 · **Date:** 2026-10-25 · **Nature:** synthetic teaching baseline.

This brief was authored for the Atlas Specifications example. It is not an interview transcript, commissioned requirement, observation, external approval, or a claimed Needs-to-L1 derivation. A real derivation would require the actual source baseline, scope, added decisions and a named accountable person. No person is invented here.

## Objectives

A board member needs to remember a unit of work, mark an existing unit completed, and see the board's current tasks. The example contains exactly three case identities: `UC-TASK-CREATE`, `UC-TASK-COMPLETE`, and `UC-TASK-LIST`.

## Explicit didactic choices

1. Each invocation has one trusted board context. Task identifiers are unique within that board, compared exactly and retained through completion.
2. A Task contains identifier, non-empty meaningful title, status (`open` or `completed`) and revision. Creation starts at revision zero. Successful completion increases revision once and preserves identifier/title.
3. Each case requires its own resolved permission for an authenticated principal. Missing, unresolved, expired or insufficient context is denied before any tool invocation. No anonymous path is provided.
4. Request-supplied identities or role strings cannot override the trusted identity-and-permission authority. Its mechanism and the transport of context are deliberately unspecified here.
5. The entity owns validity and transition rules. Tools accept ready entities; they do not repeat their established invariants. Raw records must be hydrated through the canonical entity rules before being returned as ready entities.
6. Creation enforces uniqueness atomically. Completion compares the observed revision and writes atomically, preserving competing changes. A failed write distinguishes confirmed `not_applied` from `unknown`; unknown is not automatically retried.
7. Listing returns a complete snapshot of the authorized board in identifier order. Empty success means confirmed emptiness; an unavailable or malformed store is a failure, not an empty or partial success.
8. Confirmed creations survive a normal store restart. Concurrency and consistent-read obligations have observable criteria in the cases. No numerical latency or throughput target is supplied.
9. The interaction map is illustrative and channel-independent. No screen, command syntax, endpoint, HTTP status, protocol or database is selected.

## Explicit scope exclusions

Editing titles, deleting tasks, assigning tasks, multiple boards in one invocation, public/anonymous access, scheduling, notifications and implementing a storage or identity provider are outside this example. These exclusions keep the reference bounded; they do not define universal restrictions on Atlas implementations.

## Trace to the specification

Every case includes `SRC-TASK-BRIEF` in its sources and a source-to-obligation trace. Each RNF names this origin directly. Acceptance criteria describe what a future implementation must demonstrate; no application execution is asserted by this repository.
