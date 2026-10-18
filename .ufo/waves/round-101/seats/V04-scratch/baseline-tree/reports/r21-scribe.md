# Round 21 scribe draft — malformed dependency member and occupancy

This is a bounded documentation proposal, not a checker result, replay, or axis verdict. It does not edit README, the decision table, fixtures, checker, or shared documentation. Recommendations below are conditional on paired raw probes, legacy replay, and independent review.

## Raw observations available to this scribe

- The round-21 declaration in `.shokunin/lore/LOG.md` names baseline commit `64d2673fb87ffb25396948840a991ee88472f8bf`, and describes a candidate involving malformed `depends_on` members masking same-tick known-place occupancy. These are declaration claims; I have not independently replayed them.
- Source inspection of the current checker shows it first emits `expected event-id strings` when any dependency member is not a string, then `continue`s the timeline-row loop. The `continue` is before both occupied-slot comparison and per-member dependency diagnostics. For rows reaching occupancy, the checker uses uniquely indexed actors, exactly one indexed `place`, and nonnegative ticks to compare `(entity_id, tick)` slots. This is source inspection, not runtime output.
- The declaration proposes paired two-row inputs differing only in the second row's `depends_on` (`[]` versus `[null]`) and requires preservation of earlier outputs. No round-21 scout reports or raw CLI outputs were present when this draft was prepared. Therefore I make no claim that the pairing reproduces a masked occupancy finding, that the change is safe, or that legacy outputs are preserved.

## Proposed decision-table wording (conditional)

| Timeline-row inputs | Proposed checker decision | Evidence and limit |
|---|---|---|
| Actor is uniquely indexed; place is uniquely indexed with `kind == 'place'`; tick is a nonnegative integer; dependency list is well-formed | Retain existing same-actor/same-tick distinct-place occupancy check and dependency checks. | Existing behavior; add only with the round's named controls and outputs. |
| Same occupancy prerequisites, but at least one dependency member is not a string | Emit the malformed dependency-member diagnostic; still evaluate the independent occupancy check; do not perform string-ID lookup for malformed members. | Add only if paired `[]`/`[null]` raw outputs establish this behavior and controls show no unrelated changes. This is a proposed separation of checks, not an assertion about current behavior. |
| Actor or place is missing, duplicated/ambiguous, wrong-kind, or tick is negative | Preserve the existing applicable input diagnostic and do not treat the row as a definite occupied-slot participant. | Keep these guards distinct from the malformed-dependency case; selected controls do not imply exhaustive combinations. |

**Limit:** This proposed row concerns only whether an invalid dependency-list member suppresses a separately decidable occupancy diagnostic. It does not establish event truth, source-text chronology, canon, dependency satisfaction, or completeness of occupancy detection. A malformed member is not a usable event ID; retaining occupancy evaluation must not attempt member-wise lookup for it.

## Suggested README wording (conditional; not an edit)

For the corpus README, prefer a brief pointer instead of restating checker semantics:

> `knowledge/2026-10-12-lore-decision-table.md` records bounded checker decisions, including how malformed dependency members relate to independent occupancy checks. These are input-diagnostic conventions, not source-text or canon findings.

Only add the pointer after the behavior is supported by admitted round evidence. Avoid describing the checker as a general malformed-input, timeline, or canon validator.

## Evidence required before merging

1. Paired raw CLI probes establish the exact malformed-dependency diagnostic and whether the independent known-place occupancy finding is retained; include valid-list and malformed-list controls.
2. Controls show malformed members are not looked up as IDs, while valid dependency checks and actor/place/tick certainty guards remain intact.
3. Non-author replay checks the declared 56 prior outputs, inventorying any changed case rather than assuming byte-identical preservation.
4. Reviewer/verifier and axis adjudication support the bounded wording before it is merged. Record fixture names and captured-output paths in the table; do not convert this draft into evidence.
