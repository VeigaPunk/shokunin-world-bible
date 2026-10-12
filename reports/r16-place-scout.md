# Round 16 place-ID behavior scout

## Scope and method

Read the declared baseline checker with `git show 3995486def3c9fceb95449362f6e8dab8cc130f7:.shokunin/lore/corpus/fixtures/check_bible.py`. Executed the checked-in CLI as `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>` on existing place controls and on temporary paired inputs derived from `.shokunin/lore/corpus/fixtures/r12-unique-actor` (temporary copies under `/tmp/lore-r16-place-*`; no repository fixture was changed). The raw CLI prints `VIOLATION: ...`, counts, and `no canon changed`.

## Observed behavior

- **Zero matching entity rows:** existing `.shokunin/lore/corpus/fixtures/r11-dangling-place` reports `timeline[0].place_id: dangling entity 'unlisted'`. A paired same-tick input with this dangling row followed by Mira at uniquely resolved `tower` also reported a definite `double-booked` finding between the dangling `unlisted` and `tower` strings. The source logic: occupancy is keyed by unique actor and tick, then compares raw `place_id` inequality; it does not check place resolution before making that assertion.
- **One row, kind `place`:** `.shokunin/lore/corpus/fixtures/r11-place-character` and `r11-character-place` each report duplicate `entities` ID `harbor` plus `timeline[0].place_id: ambiguous place entity 'harbor'`. The baseline `index('entities')` overwrites duplicate IDs in the ID→row dict, but `entity_id_counts` retains multiplicity; place status is thus count-based, not rescued by whichever duplicate is last.
- **One row, wrong kind:** `.shokunin/lore/corpus/fixtures/r11-unique-nonplace` reports `timeline[0].place_id: not a place 'mira'`. A temporary uniquely-IDed entity with `kind: "planet"` likewise reports `entities[1].kind: unknown kind 'planet'` and place `not a place`, not dangling or ambiguous. Invalid kind does not prevent it entering the required-field-screened entity index.
- **One malformed row:** a temporary entity row `{ "id": "harbor", "kind": "place" }` emits required-field errors for `name`, `first_appearance`, `claims`, and the timeline use reports dangling `harbor`. The loader appends an entity to `data['entities']` only if all required fields pass; malformed rows are omitted from the later indexes/counts. With the original valid `harbor` plus this malformed duplicate, the malformed row errors appeared, but no duplicate/ambiguous-place finding did; the valid one still resolved. (Malformed-row behavior here means missing required fields/types, as exercised.)
- **More than one required-field-valid row:** a temporary second `harbor` entity, regardless of its kind, produced duplicate-ID and `ambiguous place entity` errors. In a same-tick pair using `harbor` and `tower`, the checker additionally reported definite `double-booked` because the occupancy branch still compares the raw strings despite the ambiguous resolution.

The relevant raw implementation is `check_bible.py`: loader's `valid` gate near the row loop; `index('entities')` and `entity_id_counts`; timeline dangling check (`row[field] not in entities`) and place count/kind checks; then independent occupancy block guarded only by `actor_id_count == 1`, comparing `occupied[slot][1] != row['place_id']`.

## Recommendations (not observed behavior)

1. For round 16's calibration question, do not infer a resolved different-place conflict from a zero-count place ID. Preserve the dangling finding and raw event. A focused occupancy guard should require both the current and prior place IDs to have exactly one screened entity row of kind `place`, while leaving existing invalid/ambiguous-place diagnostics intact. Confirm expected behavior for the prior occupied slot as well as current row.
2. Keep malformed-row semantics explicit: an invalid-required-field entity is excluded from resolution counts even when its `id`/`kind` happen to look usable. Avoid silently counting partial rows unless deliberately changing schema policy.
3. Invalid kinds currently get a direct `not a place` finding when unique, but an unknown kind value is not eligible as a place. Preserve the separate kind and reference findings; neither establishes a valid location.

No checker, fixtures, shared docs, or commits were changed.
