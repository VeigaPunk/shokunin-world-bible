# Round 13 dangling-actor scout — baseline map and reproduction

## Scope and baseline

I inspected the baseline checker at `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5` (`git rev-parse HEAD`), specifically `.shokunin/lore/corpus/fixtures/check_bible.py`. The checked-out checker is byte-identical to `git show 97f7667:.shokunin/lore/corpus/fixtures/check_bible.py`. No repository checker or fixture was changed. I replayed the CLI against all 26 directories under `.shokunin/lore/corpus/fixtures/` using `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`; stdout payloads match the saved payloads in `.shokunin/lore/corpus/live/runs/20261012T175244Z/<case>.txt`, and the observed exit codes match the run records (the clean cases exit 0; the others exit 1). This reproduces the current baseline rather than a proposed change.

## Relevant raw checker path

The checker first validates rows and appends only schema-valid entities to `data['entities']`. `entity_id_counts` is then built by counting every row in that list, so malformed rows do not contribute. In the timeline loop (`check_bible.py`, `occupied = {}` through dependency handling):

1. For `entity_id` and `place_id`, it tests `row[field] not in entities`; this emits a local `dangling entity` finding for a missing ID.
2. `actor_id_count = entity_id_counts.get(row['entity_id'], 0)` and `ambiguous_actor = actor_id_count > 1`. It emits `ambiguous actor entity` only when count exceeds one.
3. Place classification is separate: count >1 is ambiguous, count ==1 checks `entities[id]['kind']`, and count ==0 receives only the dangling finding.
4. Source and tick checks run. A non-string dependency causes `continue` before occupancy. Otherwise, if `not ambiguous_actor`, the checker uses `slot = (row['entity_id'], row['tick'])`. If that slot exists and the prior row's place differs, it reports `double-booked`; otherwise it stores `(location, place_id)` in `occupied`.
5. Dependency diagnostics follow occupancy.

Thus count zero and count one both pass the `not ambiguous_actor` gate. For zero, the missing entity's raw identifier is still used as an occupancy key. Two rows with that same absent ID and tick but differing place IDs therefore yield a definite-looking same-actor `double-booked` assertion, even though neither row resolves to an entity. The current guard is designed only for count >1 and does not stop this.

## Temporary CLI probes (baseline)

I copied the baseline checker and `consistent` fixture into `/tmp/lore-r13-dangling-scout/`; all alterations were confined to that temporary directory. Each probe had two timeline rows at tick 1, at `harbor` then `tower`, with the same source as a valid template row. The cases differed only in actor resolution: absent `unlisted`, unique `mira`, or duplicated schema-valid `mira` (a copy of the existing valid entity row was added). Raw command form: `python3 /tmp/lore-r13-dangling-scout/check_bible.py /tmp/lore-r13-dangling-scout/<case>`.

**Absent actor (`dangling`), exit 1:**
```text
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1]: double-booked 'unlisted' at tick 1 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
```

**Unique actor (`unique`), exit 1:**
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

**Multiple valid rows (`ambiguous`), exit 1:**
```text
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
3 violation(s); no canon changed
```

This confirms the count-specific boundary: unique actors retain occupancy inference; multiply represented actors get per-row ambiguity and skip occupancy; absent actors get dangling findings but still enter occupancy. The count is over schema-valid rows, not all raw entity rows.

## Recommendations (not observed behavior)

If implementing the declared move, leave each dangling actor's local finding and raw timeline row intact, but gate occupancy on **exactly one** schema-valid matching entity row rather than merely `not ambiguous_actor` (equivalently, skip when count is zero as well as when greater than one). Do not describe this as proving that the two rows are different actors, or that an actual conflict cannot exist. Preserve the unique-actor collision and the round-12 duplicate-ID ambiguity behavior. Keep the change scoped to timeline actor occupancy; this probe says nothing about resolving actor identity, canon, source truth, or place handling.
