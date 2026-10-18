# Round 20 scribe draft — dependency inversion and invalid ticks

This is a bounded documentation proposal, not a checker result or verification report. It does not edit README, the decision table, fixtures, checker, or shared documentation. Keep raw observations separate from any recommendation; merge the suggested claims only if the round's paired probes and non-author replay support them.

## Raw observations available to this scribe

- The round-20 declaration in `.shokunin/lore/LOG.md` identifies baseline report `47733bfa36216a28c639fd8d5dc891fb4d8de3f5`, says 49 prior stdout/stderr/exit results are the regression set, and describes a candidate policy. Those are declaration claims, not independently replayed evidence here.
- Reading the current checker source shows: schema-valid timeline rows are indexed by ID; `event_id_counts` counts such rows; for each distinct dependency token, count 0 reports unknown, count >1 reports ambiguous, and count 1 obtains the indexed target and compares `events[dep]['tick'] >= row['tick']` to report `timeline inversion`. The inversion comparison contains no nonnegative-tick guard. Self and repeated dependency diagnostics are evaluated separately. This is source inspection, not a fresh CLI observation.
- The existing round-19 decision-table entry says negative integer ticks remain available to dependency validation and that round 19 did not change its raw-tick inversion policy. This is established prior-round documentation; it does not prove current candidate fixtures or replay outcomes.
- No round-20 scout report or fresh CLI output was present in `.shokunin/lore/reports/r20-*` when this draft was prepared. Therefore no paired result, preservation result, or adjudicated axis claim is reported here.

## Proposed decision-table row (conditional on round evidence)

| Dependency endpoints, each resolving to exactly one schema-valid event | Proposed decision | Evidence and limit |
|---|---|---|
| Both endpoint ticks are nonnegative integers | Retain existing strict-order check: report inversion when prerequisite tick is greater than or equal to dependent tick; otherwise no inversion finding. | Existing valid-to-valid controls; this documents only the local checker convention. |
| Either endpoint has a negative integer tick | Retain the invalid-tick diagnostic and raw event/dependency data, but withhold the definite timeline-inversion comparison. | Add only after paired negative-endpoint and valid controls are replayed. A negative tick is outside the checker’s admitted numeric domain; withholding this finding does not establish that chronology is valid, that the dependency is satisfied, or that an event did not occur. |
| Dependency ID is absent or has multiple schema-valid rows | Preserve existing unknown-event or ambiguous-dependency handling; do not compare an arbitrarily selected tick. | Existing count-based resolution policy; separate from the proposed tick-domain rule. |
| Self or repeated dependency token | Preserve existing self/repeated findings independently of tick comparison. | This move must not suppress or rewrite these findings. |

**Boundary:** This proposal concerns only whether the checker emits a *definite inversion* for uniquely resolved dependency endpoints when either tick is negative. It does not change occupancy, tick validation, ID indexing, duplicate/missing-ID policy, dependency-list handling, source citations, event truth, or canon. An invalid endpoint is not evidence that an apparent inversion is absent in-world; it means this numeric convention cannot support this checker’s definite comparison. Do not call this a complete chronology or graph validation.

## Suggested README wording (conditional; not an edit)

The README currently routes behavior claims to the lore corpus. If round 20 is admitted, add a short pointer to the decision table rather than embedding the rule in the top-level setup README, for example:

> The lore decision table records the checker’s bounded dependency-ordering rules, including cases where an invalid negative tick prevents a definite inversion comparison; it describes input diagnostics, not source-text entailment or canon.

Avoid describing this checker as a general timeline/causality verifier. Do not add claims about all invalid numeric types, malformed inputs, complete dependency graphs, or semantic chronology from this round.

## Evidence required before merging

1. Paired valid/negative endpoint probes establish the behavior in both directions (negative prerequisite and negative dependent) and valid-to-valid controls retain the inversion policy.
2. Controls retain unknown, ambiguous, self, and repeated-dependency findings; raw event rows/references and negative-tick diagnostics remain.
3. Non-author replay confirms the declared 49 prior stdout/stderr/exit results are unchanged and all new saved outputs match the current checker.
4. Only then update the table with exact fixture names, captured outputs, and reviewer/verifier boundary. Do not treat this scribe proposal or source inspection as that evidence.
