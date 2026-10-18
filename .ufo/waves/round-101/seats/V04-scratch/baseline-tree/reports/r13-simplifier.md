# Round 13 simplifier: require exactly one actor for occupancy

## Observed raw paths and CLI probes

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` and `.shokunin/lore/LOG.md` Round 13 declaration. The checker counts only schema-valid entities in `entity_id_counts`; in the timeline loop it already computes `actor_id_count = entity_id_counts.get(row['entity_id'], 0)`, and emits `ambiguous actor entity` when that count is greater than one. The occupancy guard is currently `if not ambiguous_actor:`. Thus duplicate IDs are already excluded from occupancy, but zero-match IDs still enter `occupied` after their dangling-entity finding. The occupancy key and collision comparison are `(entity_id, tick)` and different `place_id` respectively.

Using copies of `.shokunin/lore/corpus/fixtures/consistent` under `/tmp/r13-simplifier-8q8haccd/`, I made otherwise valid two-event, tick-1, different-place probes. No repository fixtures were edited. Commands and raw results:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r13-simplifier-8q8haccd/zero-match
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1]: double-booked 'unlisted' at tick 1 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
[stderr empty; exit 1]

python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r13-simplifier-8q8haccd/one-match
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
[stderr empty; exit 1]
```

## Recommendation (not implemented)

Change only the occupancy condition from `if not ambiguous_actor:` to `if actor_id_count == 1:`. Leave the surrounding occupancy body unchanged. This is the smallest gating change: exactly-one actor rows continue to compare and update occupancy; zero-match actors keep their existing dangling findings but are neither compared nor inserted; duplicate actors remain excluded as before and retain the existing local ambiguity finding and duplicate-ID diagnostic. No extra zero-match diagnostic is needed because the existing dangling finding already marks each unresolved reference.

This does not resolve identity, assert the missing actors differ, or claim that no real conflict exists. Keep all unrelated behavior and output unchanged. Validation of broader fixture replay and the full round remains separate; this report is a recommendation, not an implementation or verifier claim.
