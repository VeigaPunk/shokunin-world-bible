# Round 88 F1: mixed first-stop attribution

Purpose: distinguish the actual first provenance stop from a later holder ambiguity. The three records are: unknown source at `[0]`, ambiguous `to_holder` at `[1]`, then at `[2]` a holder discontinuity and decreasing tick that the latched stop must leave unassessed.

## Expected after the C1 fix (integration verification pending)

- Checker exit: `1` (intentional duplicate entity id, unknown source, and ambiguous holder remain findings).
- The first stop is the unknown source `f1-mixed-missing-source` at `entities[5].provenance[0]`.
- Disclosures at `[0]`, `[1]`, and `[2]` name that actual first cause, not the later ambiguous holder at `[1]`.
- Record `[2]`'s hidden chain break and decreasing tick remain unreported as comparisons.

These are post-fix expectations, not measurements against the unpatched checker. The delivered baseline run is recorded in `.ufo/waves/round-88/F1.md`; recheck these expectations against the integrated revision.
