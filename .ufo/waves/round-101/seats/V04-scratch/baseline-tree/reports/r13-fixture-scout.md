# Round 13 fixture scout — missing actor vs unique actor

## Observed baseline

I replayed the checked-in pair at `HEAD=97f7667` with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-ambiguous-actor
```

The unique fixture exits 1, stderr is empty, and stdout is exactly:

```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

Raw inputs: `.shokunin/lore/corpus/fixtures/r12-unique-actor/{entities.json,timeline.json}`. It has one `mira` character and two tick-7 events at `harbor` and `tower`. The ambiguous control exits 1 and emits duplicate-ID and per-event ambiguous-actor findings instead of a booking finding; raw inputs are `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/{entities.json,timeline.json}`.

To isolate the zero-row actor case, I made temporary, untracked copies under `/tmp/r13-fixture-scout/` from the unique case, removed the `mira` record, changed both event `entity_id` values to `unlisted`, and cleared the unrelated `relations.json` edge (otherwise the removed entity causes an extra dangling-relation finding). I left the two event rows' tick and place values untouched. Command:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r13-fixture-scout/missing-actor
```

It exits 1, stderr is empty; stdout is exactly:

```text
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1]: double-booked 'unlisted' at tick 7 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
```

The matching temp control `/tmp/r13-fixture-scout/unique-actor` uses the same two event rows and place/tick values with the one valid `mira` entity and no unrelated relation; it exits 1 with the exact unique-actor stdout shown above. Both temp probes used the repository checker at the current baseline `HEAD=97f7667`; they are not checked-in fixtures.

Relevant implementation evidence in `.shokunin/lore/corpus/fixtures/check_bible.py`: lines 225–251 walk `data['timeline']`; lines 228–229 report dangling actor/place IDs; lines 230–233 count and report only `actor_id_count > 1`; lines 245–251 skip occupancy only for ambiguous (>1) actors, otherwise key `(entity_id, tick)` in `occupied`. Thus zero-count and one-count IDs both reach occupancy, consistent with the observed dangling-plus-double-booked output. Round-13 premise is directly reproduced, not inferred from the r12 ambiguous case.

## Fixture recommendations (not implemented)

1. Check in a `missing-actor` / `unique-actor` pair cloned from the r12 pattern but keep unrelated relations valid (either clear that relation in both cases, or avoid removing the relation's target by designing a simpler fixture). Use the same two tick-7 events, same `harbor`/`tower` places, descriptions, dependencies, and source IDs. Change only the actor identity validity: zero matching schema-valid entity records (`unlisted`) versus exactly one (`mira`). Avoid duplicating `mira`; that tests the already-covered round-12 ambiguity branch.
2. For the missing actor fixture, expected post-change CLI exit remains 1, stderr empty; retain two local dangling findings and suppress only occupancy inference:

```text
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
2 violation(s); no canon changed
```

3. For unique actor, exact expected CLI output remains the baseline booking output above (exit 1, stderr empty). This is the positive control that unresolved-actor handling does not disable real unique-ID occupancy checks.
4. Preserve the current two-event order and tick/place values. Keep the existing `r12-ambiguous-actor` as a distinct regression control; its ambiguity behavior is not a substitute for this zero-match case.

The proposed missing-case output is a recommendation for the declared behavior, not a baseline observation. Suppressing a definite booking assertion does not imply the events belong to different people or that a real conflict is absent. No claims about canon or source truth.
