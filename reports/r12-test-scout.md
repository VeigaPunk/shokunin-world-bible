# Round 12 test scout — baseline replay and actor probes

## Observed raw CLI runs

Commands used (from repository root): `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` for each of the 24 fixture directories; and the same checker with temporary probe directories under `/tmp/lore-r12-probe-b7aomag8/{unique,doubled,dangling}`. Exit status and stdout were captured separately. No checker or fixture files were changed.

The 24 cases and observed exit statuses:

| Fixture | Exit |
|---|---:|
| ally-one-way | 1 |
| ally-reciprocal | 0 |
| consistent | 0 |
| contradictions | 1 |
| contradictions-ledger-malformed | 1 |
| item-chain-broken | 1 |
| item-chain-valid | 0 |
| r10-registry-witness | 0 |
| r11-character-place | 1 |
| r11-dangling-place | 1 |
| r11-place-character | 1 |
| r11-unique-nonplace | 1 |
| r5-invalid-citation | 1 |
| r5-invalid-json | 1 |
| r5-missing-file | 1 |
| r5-row-shape | 1 |
| r5-wrong-top-level | 1 |
| r7-ally-reverse-ambiguous | 1 |
| r7-item-ambiguous | 1 |
| r8-deps-anomalous | 1 |
| r8-deps-distinct | 0 |
| r9-dup-high-low | 1 |
| r9-dup-low-high | 1 |
| r9-unique-control | 0 |

Stdout for all 24 replayed runs matched the stdout payload in `.shokunin/lore/corpus/live/runs/20261012T174305Z/<fixture>.txt` byte-for-byte. Those prior run records also state the same exit statuses; their first two lines are command/exit metadata, not checker stdout. I observed no baseline replay drift.

## Raw actor probes (baseline checker at HEAD 954a1b712590f9b89aed6757e72a8bd4af5c8848)

The three temporary bibles were copied from `consistent`, then given two same-tick timeline rows at `harbor` and `tower`; the actor ID was unique (`mira`), doubled by adding another schema-valid `mira` entity row, or dangling (`unlisted`). Each timeline source remained `courier-log`.

`unique` — exit 1:
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

`doubled` — exit 1:
```text
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
```

`dangling` — exit 1:
```text
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1]: double-booked 'unlisted' at tick 1 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
```

## Scout interpretation / recommendation (not observed behavior)

The premise is reproduced: occupancy is keyed by raw `(entity_id, tick)`, so doubled valid entity IDs and dangling IDs both produce the same `double-booked` conclusion as a unique actor. The unique control confirms the collision is presently reported for a uniquely identified actor. A narrowly scoped count guard for schema-valid entity IDs on timeline `entity_id` could report ambiguity and skip occupancy collision inference when count exceeds one; dangling IDs should retain their existing dangling findings and should not be inferred as one actor either. Preserve raw events and the duplicate-ID finding. This does not establish canonical identity or source truth.
