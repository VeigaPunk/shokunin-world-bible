# Round 18 fixture scout — ambiguous place occupancy

## Raw observation (baseline CLI)

I invoked the current checker directly as `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-fixture-directory>`. The probe directories were created under `/tmp/r18-fixture-scout-bga165ba`; they are scratch inputs, not repository fixtures. Each event below is a constructed fixture row with `description: "Fixture input only; no narrative/source-text claim."` and a source ID only to satisfy checker structure. These outputs describe checker behavior on JSON inputs, not source text, story facts, or canon.

Minimal pair: one fixture has a single `mira` event at tick 9 each in unique `tower` and unique `harbor`; its paired input adds a second entity row with ID `harbor` (same `place` kind), leaving those events unchanged.

- Unique pair: exit 1; `VIOLATION: timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'`.
- Duplicate pair, known then ambiguous: exit 1; `VIOLATION: entities[4].id: duplicate entities id 'harbor'`; `VIOLATION: timeline[1].place_id: ambiguous place entity 'harbor'`; and still `VIOLATION: timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'`.
- Reverse-order duplicate pair (ambiguous then known): exit 1; same duplicate-entity and ambiguous-place diagnostics, and still `VIOLATION: timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('harbor') and 'tower'`.

Thus this raw baseline reproduces the declared round-18 condition independent of row order. It does not establish that either event occurred.

## Reverse/mixed controls

- A three-row known / ambiguous / known input uses unique places `tower`, duplicate-ID `harbor`, and fixture-only unique `quay`, all same actor/tick. Baseline reports both `tower` vs `harbor` and `tower` vs `quay` as `double-booked`. A proposed fix should suppress the ambiguous comparison/insertion while leaving the definite checker-ID comparison between the two unique place IDs (`tower` and `quay`). This checks that excluding one ambiguous row does not discard the rest of the slot.
- A mixed-kind duplicate control appends a `character` entity with the same `harbor` ID (instead of a second `place`). Baseline still reports duplicate ID, ambiguous `harbor` place ID, and the raw-ID double-booking. This probes duplicate identity across kinds; it says nothing about which row is the intended referent.

## Recommendation (not an observation)

Use the unique pair as the positive control and its same-row duplicate-ID variant as the single-variable negative pair. Reverse only the two timeline rows in a second negative case. Add the mixed-kind duplicate as a compact indexing-semantic control. Keep the three-row known/ambiguous/known case as a preservation control if in-scope; expected post-fix behavior is one known-known `tower`/`quay` conflict, with no comparison involving ambiguous `harbor`. Label every event prose field as fixture-only and never cite it as narrative support. Raw-ID diagnostics and suppression of an unsupported checker comparison do not prove actual locations, absence of another conflict, text support, or canon.
