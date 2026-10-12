# Round 11 entity index/count scout

Scope: read-only map of the active checker and CLI probes. The only file written by this scout is this report. Temporary mutated inputs were under `/tmp/r11-entity-scout-w87lttts/fixture`; no tracked fixture was changed.

## Active entity index and consumers

Raw source: `.shokunin/lore/corpus/fixtures/check_bible.py`.

- `index(section)` (lines 44–51) iterates schema-valid rows, emits a duplicate-ID diagnostic, and nevertheless assigns `result[row['id']] = row`. Thus the later *valid* row wins in the map while every valid raw row remains in `data[section]`.
- `entities = index('entities')` is at line 57. Direct map consumers:
  - Relations endpoint existence at lines 119–121 (membership only; no endpoint-kind decision).
  - Timeline `entity_id`/`place_id` existence at lines 226–229 (membership only).
  - Timeline place-kind classification at line 230: `entities[row['place_id']]['kind'] != 'place'`. It checks only map membership, not unique occurrence, so it is the confirmed last-wins hazard.
  - Alliance faction-kind classification at lines 212–215 also reads `entities[id]['kind']`, but first explicitly excludes endpoints whose `entity_id_counts` is not exactly one. This consumer is guarded against duplicate-ID order effects.
- `entity_id_counts` is independently built from all schema-valid entity rows at lines 125–127. It guards provenance at lines 141, 170–181 (item-chain eligibility and holder resolution), alliance endpoint eligibility at lines 212–213, and not display-name logic. The timeline place check does not currently use it.
- Other identifier paths that are not consumers of the **entity** index/count: `events = index('timeline')` and `event_id_counts` guard contradiction event references and timeline dependencies; `sources` has its own `source_id_counts` / uniqueness status. They are separate ID namespaces, not entity-index consumers.
- Row-wise entity passes at lines 107–116 and 129–205 preserve/inspect all valid entity rows; the latter optionally validates provenance. They do not resolve a referenced entity via `entities` except using the count guards.

## CLI evidence

Command form: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`.

1. Baseline raw fixture `.shokunin/lore/corpus/fixtures/consistent`: exit **0**, stdout `CLEAN: schema, citations, relations, timeline; 0 violations`, stderr empty.
2. On a temporary copy, inserted a schema-valid duplicate `harbor` entity of kind `character` adjacent to its existing `place` row, leaving timeline references unchanged. First order was character then place. Command on `/tmp/r11-entity-scout-w87lttts/fixture`: exit **1**, stdout only `VIOLATION: entities[2].id: duplicate entities id 'harbor'` and `1 violation(s); no canon changed`. The timeline place reference was therefore treated as a place, silently, by the last-wins map.
3. Swapped the duplicate `harbor` rows so the character was last, with all else unchanged. Same command/path: exit **1**, stdout `VIOLATION: entities[4].id: duplicate entities id 'harbor'`, `VIOLATION: timeline[0].place_id: not a place 'harbor'`, and `2 violation(s); no canon changed`.

This confirms the declared row-order premise: duplicate-ID diagnostics persist, but the timeline kind conclusion changes from no kind finding to `not a place`. The probe used schema-valid rows, and the only semantic mutation was duplicate entity kind/order; it establishes structural input behavior, not canon truth.

## Recommendations (separate from observations)

- Narrowly add an ambiguity branch to the timeline place-kind check: if the referenced ID occurs more than once among valid entity rows, report a local ambiguous place reference and skip kind classification; otherwise retain current unique-place acceptance, unique-non-place finding, and dangling-reference behavior. Keep `index('entities')` and all raw rows/duplicate-ID diagnostics unchanged.
- Paired fixtures should differ only by order of duplicate `harbor` place/character rows and should yield an identical ambiguity conclusion. Include controls for unique place, unique non-place, and dangling reference, then replay the existing fixture CLI outcomes. This recommendation is limited to timeline `place_id`; other identifier semantics should not be broadened in this change.
