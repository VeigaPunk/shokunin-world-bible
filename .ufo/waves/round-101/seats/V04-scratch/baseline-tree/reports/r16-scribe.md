# Round 16 scribe draft — unresolved-place occupancy

**Draft scope.** This is proposed bounded documentation for the round-16 calibration change, not an account of a change already implemented. It covers only a timeline event whose `place_id` has zero matching entity rows and the resulting same-actor/same-tick occupancy comparison. It does not generalize to all malformed input or assert canon.

## Observed behavior (baseline)

At baseline commit `3995486def3c9fceb95449362f6e8dab8cc130f7`, `corpus/fixtures/check_bible.py` emits `dangling entity` when a timeline `place_id` is absent from the entity index (the CLI uses `entities` indexed from rows passing the required-field shape gate). Separately, the occupancy pass stores `(entity_id, tick)` and compares raw `place_id` strings for a uniquely identified actor; it does not require either place ID to resolve or have `kind == 'place'` before reporting `double-booked`.

Raw baseline examples and commands (repo root):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-dangling-place
# observed: VIOLATION: timeline[0].place_id: dangling entity 'unlisted'; exit 1

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
# observed: VIOLATION: timeline[1]: double-booked 'mira' at tick 7 ... ('harbor') and 'tower'; exit 1
```

The first raw fixture is not the proposed paired occupancy case: its events have different ticks. `r12-unique-actor` demonstrates a unique actor and two valid, distinct places, but also different event input from a dangling-place pair. These examples establish the independent baseline behaviors only; they do **not** establish the round-16 result. The relevant raw files are `corpus/fixtures/r11-dangling-place/{entities,timeline}.json`, `corpus/fixtures/r12-unique-actor/{entities,timeline}.json`, and the baseline checker above.

## Proposed decision table (for validation after the change)

| One same-actor, same-tick event pair | Place-ID state | Proposed diagnostic decision | What it does not mean |
|---|---|---|---|
| One event uses an absent place ID; the other uses a uniquely resolved `kind: "place"` ID | First has zero matching required-field-screened entity rows; second resolves as one place | Keep the absent event's dangling `place_id` finding; withhold a **definite different-resolved-place** `double-booked` assertion involving that event | No conclusion that the events share a place, that no conflict exists, or that either event is true |
| Both events use uniquely resolved, distinct place IDs | Each resolves to exactly one entity row of kind `place` | Retain the existing `double-booked` finding for the unique actor and tick | Does not choose a canonically correct event |
| Either place ID matches more than one entity row | Place identity is ambiguous | Preserve the existing ambiguous-place finding(s); do not select an entity row as the location | Does not show the events are at different or same actual places |
| A place ID matches one entity row whose kind is not `place` | ID resolves to a non-place; existing `not a place` finding applies | Outside the narrow zero-match round-16 claim; do not call this a resolved place in documentation | Does not imply missing location or prove any occupancy fact |
| Actor ID matches zero or multiple entity rows | Actor remains dangling or ambiguous under existing behavior | Keep the actor diagnostic; this draft makes no change to actor qualification | No definite identity or occupancy conclusion |

The proposed guard is intentionally narrow: it must not suppress the dangling-place diagnostic or alter the two-uniquely-resolved-distinct-places control. The declaration calls for exact replay of the prior 29 fixture outputs and preservation of rounds 11–13; those are validation requirements, not yet verified here. The implementation currently compares raw strings, so table rows marked proposed must not be presented as current behavior until a checker change and non-author replay verify them.

## Recommendations (separate from observed facts)

1. Add an isolated same-tick paired fixture with one uniquely resolved actor, one uniquely resolved place, and one absent place ID. Assert the dangling finding remains and no definite `double-booked` finding involving the absent place is emitted.
2. Retain a paired control with two uniquely resolved, different `kind: "place"` IDs and assert `double-booked` still appears.
3. In the eventual README/decision table, describe a missing location as **unassessed** for different-place occupancy—not as no conflict. Keep ambiguous/non-place cases explicitly outside this one move unless separately tested.
4. Label each table row as observed or proposed and cite the raw fixture, checker path, and exact CLI output. A clean run or structural ID resolution is not source-text verification or canon proof.
