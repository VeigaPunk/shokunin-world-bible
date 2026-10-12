# Round 17 simplifier report — wrong-kind occupancy exclusion

## Observed raw CLI (baseline, no edits)

Checker inspected: `.shokunin/lore/corpus/fixtures/check_bible.py`; working-tree checker is unchanged by this lane. Command form used: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-directory>`.

- Checked-in `r11-unique-nonplace` exits 1 and prints `VIOLATION: timeline[0].place_id: not a place 'mira'` followed by `1 violation(s); no canon changed`. Its timeline places `mira` at a different tick from the valid-place event, so it does not itself test occupancy.
- To test the declared same-tick case without modifying repository fixtures, copied `r16-valid-places` to temporary `/tmp/r17probe-tszq1h3y/case`, changed only the second event's `place_id` from `tower` to `mira` (a uniquely indexed `character`) and retained the shared tick. Raw command exited 1 with:
  ```text
  VIOLATION: timeline[1].place_id: not a place 'mira'
  VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
  2 violation(s); no canon changed
  ```
  This reproduces the wrong-kind occupancy assertion in the declaration; it is a temporary probe, not a checked-in fixture.
- Checked-in `r16-valid-places` exits 1 with `VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`, followed by `1 violation(s); no canon changed`. Both IDs resolve uniquely to places.
- Checked-in `r16-missing-place` exits 1 with `VIOLATION: timeline[1].place_id: dangling entity 'unlisted'` and no double-booked finding. This is the round-16 count-zero behavior to preserve.
- Checked-in `r16-mixed-three` exits 1 with a dangling `unlisted` finding for the middle event and a double-booked finding between the known `harbor` and `tower` events. This confirms that the count-zero row does not erase the known pair under current code.

## Smallest guard recommendation

The existing occupancy eligibility condition is `actor_id_count == 1 and place_id_count != 0`. Keep the actor and count-zero behavior, and exclude only a **uniquely indexed non-place** ID from the occupancy comparison/storage:

```python
if (actor_id_count == 1 and place_id_count != 0
        and not (place_id_count == 1 and entities[row['place_id']]['kind'] != 'place')):
```

This is narrower than requiring `place_id_count == 1 and kind == 'place'`: it specifically removes the declared wrong-kind case while leaving duplicate-ID occupancy behavior unchanged as a separate issue. Existing dangling (`count == 0`) exclusion remains; unique valid places still participate and retain the harbor/tower collision. The current `not a place` diagnostic remains outside the guard. Since invalid wrong-kind rows neither compare nor enter `occupied`, whether the wrong-kind row precedes or follows a valid row cannot make that pair produce a definite different-place finding. Do not infer the actor's actual place, same-place status, or absence of a real conflict.

This is a recommendation only. I did not edit checker code, fixtures, shared docs, or commit anything; the raw observations above are not a post-change validation or baseline-wide replay.
