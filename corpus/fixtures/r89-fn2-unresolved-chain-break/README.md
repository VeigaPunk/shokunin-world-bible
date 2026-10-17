# Round 89 F3: FN-2 unresolved-holder chain break

Purpose: exercise a real chain comparison when the prior `to_holder` id is not uniquely resolvable in the raw entity table. `f3-dup` occurs on two entity rows, but `entities[1]` is schema-rejected because `first_appearance` is empty; exactly one row remains in the resolved entity index. The next record's `from_holder` is `mira`, so the comparison would report a chain break against `f3-dup`.

## Expected after the FN-2 fix (integration verification pending)

- Checker exit: `1` (the invalid entity row and chain break remain findings).
- The finding at `entities[4].provenance[1]` remains visible and is qualified as an input-structural finding, not sourced-canon, because `f3-dup` is not uniquely resolvable.
- No other findings are expected.

The baseline replay is recorded in `.ufo/waves/round-89/F3.md`; rerun after integrating the X1 fix to verify the qualifier.
