# Round 19 simplifier — negative-tick occupancy guard

## Raw observations

- The timeline field screen accepts only exact `int` values. A negative integer passes that screen and remains in `data["timeline"]`; bools and floats do not.
- In the timeline loop, a negative tick receives `must be nonnegative`, but that diagnostic does not skip later processing. Once `depends_on` has passed its list-of-strings check, occupancy currently uses `(entity_id, tick)` when the actor is uniquely indexed and the place is uniquely indexed with kind `place`.
- `r19-tick-scout.md` reports temporary-copy CLI probes based on `r18-unique-pair`: at `-1`, both nonnegative diagnostics and a `double-booked` diagnostic were emitted; at `0`, the pair emitted `double-booked` without the tick diagnostics. No repository fixture was changed for those probes.
- The code performs dependency checks after occupancy in the same timeline loop. An early `continue` for negative ticks placed before dependency validation would therefore change more than occupancy behavior.

## Recommendation (not an implementation)

Make the smallest occupancy-only change by extending the existing occupancy `if` condition with `row['tick'] >= 0`, e.g.:

```python
        if row['tick'] >= 0 and actor_id_count == 1 and comparable_place:
```

Place this in the existing occupancy condition only. It leaves the `must be nonnegative` diagnostic and raw row intact, prevents negative ticks from both comparing against and inserting into `occupied`, and preserves subsequent dependency validation. Do not add a `continue`, change tick schema, or alter actor/place-resolution rules. The stated paired `-1`/`0` probe supports the premise and the nonnegative control, but does not test post-negative valid pairs or establish preservation of all 45 prior outputs; those require implementation/replay evidence. This is only a checker-boundary calibration recommendation: it says nothing about whether an event occurred, source-text support, canon, or real-world conflict.
