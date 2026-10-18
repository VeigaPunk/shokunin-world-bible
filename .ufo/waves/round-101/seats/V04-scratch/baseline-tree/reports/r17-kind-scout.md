# Round 17 kind/occupancy scout

## Scope and method

Read the declared round-17 claim in `.shokunin/lore/LOG.md` and inspected `check_bible.py` only. Ran the documented raw CLI against the existing valid harbor/tower fixture and a disposable copy of that fixture with the second event's `place_id` changed to the unique character entity ID `mira`. No checker, fixture, or shared documentation was changed. The only durable output from this scout is this report.

## Observed raw CLI

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-directory>`.

**Valid-place control** (`r16-valid-places`, Mira at `harbor` then `tower`, tick 7): exit 1, stderr empty; stdout:

```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

**Disposable kind probe** (same raw data except second event `place_id` is `mira`, which uniquely indexes a `character`): exit 1, stderr empty; stdout:

```text
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
2 violation(s); no canon changed
```

Thus the CLI retains the wrong-kind diagnostic but also compares the raw wrong-kind ID for occupied-place checking and emits `double-booked`. The harbor/tower control demonstrates the desired valid-place conflict is reported. This is a behavior observation, not a canon conclusion.

## Guard map and recommendations (not observed outcomes)

Observed checker ordering: entity ID counts are computed from required-field-screened entity rows. For each timeline row, dangling actor/place IDs are diagnosed; a place count greater than one yields `ambiguous place entity`; a count of one with kind other than `place` yields `not a place`. Occupancy currently runs later under `actor_id_count == 1 and place_id_count != 0`, comparing/storing raw `place_id` values by `(entity_id, tick)`. Therefore unique wrong-kind IDs (`count == 1`) participate, as demonstrated above. Duplicate IDs (`count > 1`) also meet the occupancy's nonzero count guard, but that case was not probed in this assignment. Missing IDs (`count == 0`) do not; round 16 separately established that behavior.

Recommendation for the declared narrow round-17 move: admit an occupancy slot only if the actor is uniquely indexed and the place is uniquely indexed **and** `entities[row['place_id']]['kind'] == 'place'` (or compute one equivalent resolved-place predicate). Keep the existing kind diagnostic. This avoids a definite different-place finding when one ID is known to be a character, while retaining the valid harbor/tower conflict. Do not alter entity indexing/schema or imply the malformed row has a known location. Duplicate/ambiguous-ID handling remains a distinct behavior and is outside this scout's probe.

The fixture's prose “Mira departs the harbor” while `place_id` is `mira` is inherited from the control and is not a checker resolution; a dedicated kind fixture should avoid implying the invalid ID is actually the harbor. No claim here verifies text-source truth or proves absence of a real conflict.
