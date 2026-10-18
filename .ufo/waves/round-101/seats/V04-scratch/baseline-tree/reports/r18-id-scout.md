# Round 18 ID scout — duplicate place IDs

## Scope and method
Read-only scout of `corpus/fixtures/check_bible.py`, existing fixture inputs, and direct CLI observations. Temporary paired probe directories were created under `/tmp/r18-id-scout`; no repository fixture, checker, shared document, or commit was changed. Probe descriptions explicitly say they are fixture inputs, not source-text evidence.

## Raw code map (observation)
- `data["entities"]` includes required-field-valid entity rows. `index("entities")` emits a duplicate-ID diagnostic but assigns `result[row["id"]] = row` for each row, so the last valid row wins in the `entities` lookup. Separately, `entity_id_counts` counts every valid row by ID.
- For a timeline `place_id`, count `>1` emits `ambiguous place entity`; count `1` checks the indexed row's kind and can emit `not a place`. Count `0` has the earlier dangling check.
- Occupancy uses `comparable_place = place_id_count != 1 or entities[row["place_id"]]["kind"] == "place"`. Therefore count `>1` makes `comparable_place` true regardless of which duplicate row the index retained. Provided the actor ID count is exactly one and place count is nonzero, the raw place ID can be inserted into `occupied[(entity_id, tick)]` or compared against the prior raw place ID. The duplicate-ID diagnostic does not currently gate that path.
- Existing `r11-place-character` confirms the repository has a duplicate `harbor` ID (place + character), but its two events are different ticks; it is not a same-slot occupancy probe.

## Raw probes (observation)
All probes use copied consistent fixture data and two `mira` events at tick 7. The paired control changes only the presence of the second `harbor` entity row; order probes reverse the two event rows.

| Entity rows for `harbor` | Timeline order | Raw CLI findings |
|---|---|---|
| one `place` (control) | `harbor`, `tower` | `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'` |
| two `place` rows | `harbor`, `tower` | duplicate entity ID; `timeline[0]` ambiguous place; `timeline[1]` double-booked against raw `harbor` |
| `place` + `character` | `harbor`, `tower` | duplicate entity ID; `timeline[0]` ambiguous place; `timeline[1]` double-booked against raw `harbor` |
| two `place` rows | `tower`, `harbor` | duplicate entity ID; `timeline[1]` ambiguous place; `timeline[1]` double-booked against raw `harbor` |
| `place` + `character` | `tower`, `harbor` | duplicate entity ID; `timeline[1]` ambiguous place; `timeline[1]` double-booked against raw `harbor` |

The duplicate-order cases return exit code 1 and report 3 violations (duplicate entity ID, ambiguous place ID, and double-booking); the unique control returns exit code 1 with one double-booking violation. No source text was consulted or validated. This establishes checker behavior on these inputs, not actual locations, narrative truth, or whether a real conflict exists.

## Recommendation (not observation)
For the declared move, gate definite occupancy comparison **and insertion** on a uniquely indexed, correctly typed place (`place_id_count == 1` and indexed `kind == "place"`). Preserve the ambiguous-place diagnostic and raw timeline row. Re-run both row orders, the unique-place pair control, and prior baseline-output replay. Treat this as withholding a definite checker comparison, not as resolving the location or proving the absence of a conflict.
