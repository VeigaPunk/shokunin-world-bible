# Round 89 F1: invalid-to-holder first stop

Purpose: pin the invalid-`to_holder` first-cause branch. Record `[0]` establishes a valid holder; record `[1]` has integer `to_holder` `17` and otherwise uses the expected fields; record `[2]` is valid-shaped and follows.

## Expected after the C1 fix

- Checker exit: `1` (the integer target remains an input finding).
- The first stop is `malformed record (invalid to_holder)` at `entities[3].provenance[1]`.
- Records `[1]` and `[2]` disclose that same first cause; record `[2]` is not compared across the stop.

This is fixture scaffolding, not sourced story evidence. After-state is an expectation for integration replay, not a baseline measurement.
