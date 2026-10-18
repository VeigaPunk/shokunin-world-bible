# Round 12 entity index scout

## Observed baseline (commit `954a1b7`)

Source inspected: `git show 954a1b7:.shokunin/lore/corpus/fixtures/check_bible.py`. The current working-tree checker also matches the baseline behavior for the probes below.

- Every section row is retained in `data[section]` only when it is a JSON object with every required field present, exact expected Python type (`type(value) is expected`), and nonblank strings. A schema-invalid row gets an indexed field/shape finding and is omitted from downstream indexing/counting. This is structural filtering, not a determination that a row is canonically true.
- `index('entities')` iterates the retained entity rows, emits `entities[i].id: duplicate entities id ...` on repeats, and assigns `result[id] = row` each time. Thus the dictionary value for a repeated ID is the last schema-valid row in input order. It does not filter by allowed semantic kind before indexing.
- Separately, `entity_id_counts` counts all retained/schema-valid entity rows by ID, including repeated IDs. The count is used to suppress or qualify certain relation/provenance/faction checks and the timeline **place** kind check. Timeline place lookup reports dangling at count zero, ambiguous at count >1, and consults `entities[id]['kind']` only at count one.
- Timeline `entity_id` currently gets only the general dangling membership check against `entities`. The occupancy map uses the raw `(row['entity_id'], row['tick'])` pair, without consulting the entity count or kind. Same key and different place yields `double-booked`; same key and same place is stored/accepted. So a duplicated schema-valid actor ID is treated as one actor by occupancy even though the count is available. Duplicate/malformed timeline rows themselves are omitted unless the full timeline required-field schema passes.

## Raw CLI observations

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`.

- `consistent`: exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations`.
- `r11-place-character`: exit 1; `entities[2].id: duplicate entities id 'harbor'`; `timeline[0].place_id: ambiguous place entity 'harbor'`; `2 violation(s); no canon changed`.
- `r11-character-place`: same exit and same two messages. Their entities rows swap the valid `harbor` place and character entries; their timeline refers to `harbor` as place. This confirms the existing place count guard is permutation-insensitive for its conclusion.
- `r11-unique-nonplace`: exit 1; `timeline[0].place_id: not a place 'mira'`; `1 violation(s); no canon changed`.
- `r11-dangling-place`: exit 1; `timeline[0].place_id: dangling entity 'unlisted'`; `1 violation(s); no canon changed`.

I did not create actor fixtures or run an actor-occupancy probe; the round-12 actor premise remains to be verified by its dedicated probe lane.

## Scoped recommendation (not observed behavior)

If the occupancy premise is confirmed, use the existing `entity_id_counts` for only `timeline[i].entity_id`: count zero preserves dangling behavior; count greater than one should add an indexed `ambiguous actor entity` finding and skip occupancy inference for that event; count one may enter the existing `(actor_id, tick)` occupancy logic unchanged. Do not use the last-wins entity dictionary to choose an actor, and do not broaden this to kind/name/canon validation. Keep duplicate-ID reports and every raw valid event. Invalid entity rows should remain excluded under current schema filtering, so a duplicate involving one invalid row is not a duplicate among indexed valid rows. This recommendation is conditional; verify pair and controls plus exact replay of prior outputs before adoption.
