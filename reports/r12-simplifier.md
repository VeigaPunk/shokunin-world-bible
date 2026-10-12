# Round 12 simplifier: occupancy guard

## Observed raw paths and CLI output

The inspected checker is `.shokunin/lore/corpus/fixtures/check_bible.py`. It builds `entity_id_counts` from schema-valid rows in `data['entities']`, then its timeline loop currently records `slot = (row['entity_id'], row['tick'])` in `occupied`; on a second different `place_id` it emits `double-booked`. The loop already independently reports duplicate entity IDs in `index('entities')`. The occupancy logic currently does not consult the count, although the immediately preceding place-kind check does.

To test the declared premise without touching repository fixtures, I copied the `consistent` fixture to `/tmp/r12-probe/dup_actor` and `/tmp/r12-probe/unique_actor`; in the first copy I added a second schema-valid `mira` entity row. Both copies had two schema-valid same-tick `mira` events at `harbor` and `tower`, with otherwise valid references. Commands used:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r12-probe/dup_actor
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r12-probe/unique_actor
```

Observed stdout and exit status:

```text
dup_actor (exit 1):
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed

unique_actor (exit 1):
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

This reproduces a false-identity inference under the declared duplicate-ID premise, and confirms the unique-ID control currently reports the intended collision. The round-11 live run `.shokunin/lore/corpus/live/runs/20261012T174305Z/` contains 24 fixture output records; direct reruns of those fixtures returned the same violation text/clean result after removing the stored command/exit-code wrapper. No checker or fixture was changed for this probe.

## Recommendation (not implemented)

Use the already-computed `entity_id_counts` for an occupancy-only guard. In the timeline loop, after existing dangling-reference diagnostics and before occupancy comparison, when `entity_id_counts.get(row['entity_id'], 0) > 1`, append one local finding such as `f'{location}.entity_id: ambiguous actor entity {row["entity_id"]!r}'` and skip only the occupied-slot lookup/update for that event. Otherwise retain the current occupancy code verbatim.

This is narrower than suppressing duplicate events or changing the entity index: duplicate-ID diagnostics and raw rows stay intact; dangling actor handling stays intact; only an ambiguous actor's occupancy is not interpreted as one person's schedule. For a unique actor, same `(entity_id, tick)` and differing `place_id` still triggers the existing `double-booked` output. Do not alter place checks, event identity, occupancy key, or other diagnostics. For an ambiguous actor, emitting the local ambiguity per timeline reference makes the affected input location explicit; do not also emit `double-booked` for that actor. Re-run all 24 previous fixture CLIs byte-for-byte at stdout/stderr/exit status, excluding only newly designed ambiguous-actor cases, to validate the old-output constraint.

Scope is structural ID ambiguity only; neither duplicate row is selected as canon, and citations do not resolve entity identity. This is a guard recommendation, not implementation or a completed verifier result.
