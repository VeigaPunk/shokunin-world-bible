# Round 52 checker scout — source qualification / occupancy

## Scope and method
No repository inputs or checker files changed. I inspected `check_bible.py`, fixture README and round 12 occupancy controls, then made two temporary copies of `r12-unique-actor` outside the repo. The ambiguous copy appended an exact duplicate of its cited `courier-log` source row; JSON was written only in the temp directory. Raw stdout/stderr/exit are reproduced below.

## Source resolution versus occupancy
`check_bible.py:53-66` indexes sources, counts admitted source IDs, and returns `unknown` for zero, `unique` for one, `ambiguous` for >1. `:68-74` emits the local unknown/ambiguous-source finding without selecting a row. For every timeline event, `:242` calls this source check, but the return value is unused by occupancy. Separately, `:233-241` checks actor/place identity and place kind; `:243-252` admits nonnegative ticks and uniquely identified actor/valid place, then compares distinct places and emits raw `double-booked`. No source qualification is applied there.

### Temporary control and ambiguous-source collision (exact raw CLI output)
Command form: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-copy>`.

Unique `courier-log` control (exit 1; stderr empty):
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

Same rows, but a duplicate valid `courier-log` source row (exit 1; stderr empty):
```text
VIOLATION: sources[2].id: duplicate sources id 'courier-log'
VIOLATION: entities[0].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[0].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].first_appearance: ambiguous in-world source 'courier-log'
VIOLATION: entities[3].claims[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: relations[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[0].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[1].source_id: ambiguous in-world source 'courier-log'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
9 violation(s); no canon changed
```

The raw collision survives unchanged amid local source findings. Its message sounds definite, but what it establishes is only a structural conflict between eligible input fields; it does not establish either fictional location or source prose/support. Ambiguous source identity neither proves nor disproves location, source prose, or canon.

## Prior contract / risk
Fixtures README round 7 says repeated IDs retain duplicate and local ambiguity findings, without choosing a source or testing textual support. Round 12 README explicitly says a unique actor at two places/tick triggers the definite same-actor `double-booked` rule; its ambiguous actor control has no *definite* occupancy inference. It also says source IDs resolve identity only, not source-text support/canon. Thus a raw pairwise field collision is plausibly still valid when citations are ambiguous, but output risks being read as a sourced narrative contradiction. Adding a qualifier must not suppress/hide the collision or imply the rows are false. Existing precedent in checker `:202-206` qualifies item-chain structural findings with `input-structural finding, not sourced-canon` when source ambiguity is present, while preserving the reported chain break.

Round 12 fixture statement is at `.shokunin/lore/corpus/fixtures/README.md` round 12 (search heading `Round 12: uncertain actor identity in occupancy`); source uniqueness contract at same README round 7. Checker evidence is line-addressed above. The checker itself emits `no canon changed`; this is not proof of location truth.

## Falsifiable disposition
**Go, narrowly, for a calibration-only qualifier on the occupancy diagnostic when either colliding event has an ambiguous source ID; do not suppress the raw `double-booked` field collision.** A candidate qualifies if a controlled ambiguous-citation pair preserves the exact collision facts and adds an explicit input-structural/not-sourced-canon warning, while a uniquely cited control retains byte-for-byte current output and existing 95 fixture stdout/stderr/exit tuples and 474 JSON outputs remain unchanged. No claim that unique source IDs prove prose supports location.

**No-go** if this source-dependent distinction cannot be made without changing unique/unknown-source behavior, hiding the collision, breaking prior outputs, or implying that ambiguous source identity proves/disproves a location, prose assertion or canon. A skeptic can falsify the go rationale by showing existing user-facing wording already makes this boundary unmistakable, or that the qualifier materially obscures the useful input collision. This is a scout assessment only, not a proposed implementation or checker result.
