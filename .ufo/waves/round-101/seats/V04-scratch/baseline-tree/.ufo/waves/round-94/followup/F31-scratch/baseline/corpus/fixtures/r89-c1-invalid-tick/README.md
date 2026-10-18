# Round 89 F1: invalid-tick first stop

Purpose: pin the invalid-tick first-cause branch with an otherwise well-formed holder-linked provenance sequence. Record `[0]` is valid; record `[1]` has the only malformed field, a negative tick, while its holder transition remains connected. Valid records `[2]` and `[3]` follow.

## Expected after the C1 fix

- Checker exit: `1` (the negative tick remains an input finding).
- The first stop is `malformed record (invalid tick)` at `entities[3].provenance[1]`.
- Records `[1]`, `[2]`, and `[3]` each disclose that same first cause; no later continuity/tick comparisons are inferred after the stop.

This is fixture scaffolding, not sourced story evidence. After-state is an expectation for integration replay, not a baseline measurement.
