# Round 16 occupancy scout — place references and zero-ID behavior

## Observed baseline

Inspected baseline commit `3995486def3c9fceb95449362f6e8dab8cc130f7`, file `.shokunin/lore/corpus/fixtures/check_bible.py` (no edits made). The checker first validates required fields in each entity row and keeps only rows that pass that required-field screen in `data["entities"]`; `index('entities')` builds `entities` from those rows and records duplicate-ID findings. Timeline place lookup then uses `entity_id_counts.get(row['place_id'], 0)`: zero produces `timeline[i].place_id: dangling entity ...`, count >1 produces `ambiguous place entity ...`, count 1 with kind other than `place` produces `not a place ...`. These findings do not remove the timeline row from occupancy processing.

Occupancy independently counts the actor ID and, when exactly one matching entity row exists, keys `occupied` by `(row['entity_id'], row['tick'])`. If that slot already exists and its stored raw place-ID string differs from the current raw place-ID string, it emits `double-booked`; it does not consult `place_id_counts`, the place kind, or resolution status before this comparison. The first row is stored as `(location, row['place_id'])` even if its place is dangling or non-place. Thus “zero-ID” here means zero matching required-field-screened entity rows, not an event ID; the raw reference string remains available and participates in comparison.

## Raw probe evidence

Ran the baseline CLI (`python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-probe-directory>`) against copies of the `consistent` fixture JSON, changing only probe timeline rows. Temporary directories were `/tmp/lore-r16-m9b684lw`, `/tmp/lore-r16-vhx5y9qy`, `/tmp/lore-r16-ge33gu_1`, `/tmp/lore-r16-4z5n845s`, and `/tmp/lore-r16-qk6n31dr`.

- `/tmp/lore-r16-m9b684lw`: `mira` at tick 1 in existing valid `harbor`, paired with `mira` at tick 1 in absent `ghost`. Exit 1; stdout includes both `timeline[1].place_id: dangling entity 'ghost'` and `timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'ghost'`. Reproduces the suspected assertion.
- `/tmp/lore-r16-vhx5y9qy`: same pair reversed in input order. Exit 1; dangling remains, and double-booked is emitted from the later valid row, citing stored raw place `'ghost'` then `'harbor'`. This confirms order changes the reporting location/order but not the unsupported comparison.
- `/tmp/lore-r16-ge33gu_1`: same actor/tick in two rows both using absent `ghost`. Exit 1; two dangling findings, no double-booked finding because the raw strings are equal. This is not evidence that both locations resolve to the same place.
- `/tmp/lore-r16-4z5n845s`: added a duplicate `harbor` entity row, paired with absent `ghost`. Exit 1; duplicate ID, ambiguous-place and dangling findings, plus double-booked comparing `'harbor'` and `'ghost'`. The occupancy check is gated by unique actor, not by unique place.
- `/tmp/lore-r16-qk6n31dr`: `mira` actor occupies valid `harbor` and the unique non-place entity `mira` at same tick. Exit 1; `not a place 'mira'` plus double-booked comparing `'harbor'` and `'mira'`. A uniquely indexed but wrong-kind row also reaches raw-string occupancy comparison.

These probes use authored fixture inputs and establish checker behavior only. They do not establish canonical places, actor whereabouts, or real-world truth.

## Recommendations (not implemented)

For the declared calibration move, preserve every dangling finding and input row, but compare occupancy locations only when both the current and stored place references resolve to exactly one entity row of kind `place`. In particular, zero matching rows must not support a *definite different resolved places* assertion. Keep the unique-actor guard and raw reference diagnostics. A focused regression pair should check valid+missing in both row orders; retain a control with two unique, distinct place IDs that still reports double-booked. Equal unresolved raw IDs should not be described as confirmed co-location. Consider wrong-kind and ambiguous place occupancy as separate explicit decisions/tests; current baseline compares raw strings in those cases too, and this probe does not decide their desired policy.
