# Round 11 fixture scout — duplicate harbor place/character order pair

Scope: fixture design and CLI observation only. I did not edit checker code, fixtures, shared documentation, or commit. Baseline inspected: `.shokunin/lore/corpus/fixtures/consistent/{sources,entities,relations,timeline,contradictions}.json`; checker: `.shokunin/lore/corpus/fixtures/check_bible.py`.

## Proposed pair and controls

Use copies of the baseline `consistent/` bible. In `entities.json`, retain the existing `harbor` place row and add a schema-valid `harbor` character row, with a distinct display name (e.g. `Harbor Keeper`), `first_appearance: "archive-ledger"`, and a claim whose `source_id` is `archive-ledger`. The existing source is unique and the row shape matches the entity schema. Keep every other entity and all other section rows unchanged. The two cases differ only in the ordering of those two `harbor` rows:

- **place-then-character**: original `harbor` place row, then the character row.
- **character-then-place**: character row, then original `harbor` place row.

The baseline departure event at `timeline[0]` has `place_id: "harbor"`, exercising the kind lookup. Controls: unchanged baseline `consistent/` with the uniquely identified `harbor` place; and a copy with only `timeline[0].place_id` changed to unique `mira` (a character), to retain a unique-non-place check.

## CLI probes and observed output

I wrote temporary copies under `/tmp/lore-r11-scout-5c38zxb2/` and ran the repository CLI as `python3 .shokunin/lore/corpus/fixtures/check_bible.py <absolute-probe-directory>`.

- `/tmp/lore-r11-scout-5c38zxb2/place-then-character`: exit 1:
  ```
  VIOLATION: entities[4].id: duplicate entities id 'harbor'
  VIOLATION: timeline[0].place_id: not a place 'harbor'
  2 violation(s); no canon changed
  ```
- `/tmp/lore-r11-scout-5c38zxb2/character-then-place`: exit 1:
  ```
  VIOLATION: entities[4].id: duplicate entities id 'harbor'
  1 violation(s); no canon changed
  ```
- `/tmp/lore-r11-scout-5c38zxb2/unique-place`: exit 0: `CLEAN: schema, citations, relations, timeline; 0 violations`
- `/tmp/lore-r11-scout-5c38zxb2/unique-character`: exit 1:
  ```
  VIOLATION: timeline[0].place_id: not a place 'mira'
  1 violation(s); no canon changed
  ```

This confirms the duplicate-ID report in either order, while the current last-row entity index changes the place-kind outcome: character-last yields `not a place`; place-last yields no kind violation. The unique place and non-place controls behave as expected. The pair demonstrates order-dependent classification in this probe; it is not evidence about canon, source-text truth, or other identifier consumers.

## Recommendations (not observed results)

1. For a duplicate `place_id` target, preserve the duplicate entity-ID finding and emit a local ambiguous place-reference finding for the affected timeline field; do not infer place-kind from either row. Make that ambiguity conclusion invariant to duplicate-row ordering.
2. Keep the unique-place case clean and the unique-character case `not a place`; avoid broad changes to non-place reference checks or all entity-ID consumers.
3. Retain both raw rows and do not merge, select, or resolve them. This test concerns identifier ambiguity only.
