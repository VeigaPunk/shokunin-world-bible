# Round 89 F3: FN-2 resolved-holder control

Purpose: pair with `r89-fn2-unresolved-chain-break`. This chain has the same expected holder `f3-dup` and the same `from_holder` mismatch, but `f3-dup` occurs exactly once in the entity table and resolves uniquely.

## Expected after the FN-2 fix (verified at closure — follow-up seats V2/JCAL3 line-by-line)

- Checker exit: `1` (one intentional provenance chain-break finding).
- The finding at `entities[3].provenance[1]` remains unqualified: `provenance chain break; expected from_holder 'f3-dup', got 'mira'`.
- No schema, citation, relation, timeline, or other provenance findings are expected.

The baseline replay is recorded in `.ufo/waves/round-89/F3.md`; rerun after integrating the X1 fix to verify the control remains unqualified.
