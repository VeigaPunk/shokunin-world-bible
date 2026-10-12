# Round 11 schema scout — duplicate candidates and timeline place type

## Observed facts (no changes recommended/applied)

Raw checker inspected: `.shokunin/lore/corpus/fixtures/check_bible.py`. The row schema is a required-field/type gate: only a row whose required fields have exact expected types and nonblank required strings is appended to `data[section]` (lines 37–43). `index('entities')` diagnoses repeated IDs, then unconditionally assigns `result[row['id']] = row` for every schema-valid row (lines 45–51), so its lookup is last-valid-row-wins. A separate `entity_id_counts` is built from all schema-valid entity rows (lines 125–127); other consumers already guard uniqueness in provenance and faction checks (lines 141, 211–215). The timeline place branch (lines 228–232) first reports a dangling ID if absent, then checks `entities[row['place_id']]['kind']` if present, without checking entity-ID count.

Raw baseline input: `.shokunin/lore/corpus/fixtures/consistent/entities.json` has one `harbor` entity of kind `place`; `.shokunin/lore/corpus/fixtures/consistent/timeline.json` uses `harbor` for `departure`. The baseline CLI probe `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` reports `CLEAN` (exit 0).

I made isolated temporary copies under `/tmp/r11-schema-probes/` from that baseline; no corpus files were edited. Each duplicate candidate copied the schema-valid harbor row, changed its name/kind to a character, and retained all required fields. CLI probes and exact observed outputs:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-schema-probes/valid-place-last` (place row then duplicate character): exit 1; `entities[4].id: duplicate entities id 'harbor'` and `timeline[0].place_id: not a place 'harbor'`.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-schema-probes/valid-place-first` (duplicate character then place row): exit 1; only `entities[2].id: duplicate entities id 'harbor'`. Thus the timeline type conclusion changes by valid-row order, though the duplicate diagnostic remains in both.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-schema-probes/invalid-duplicate` (duplicate row has integer `kind`, hence fails required type): exit 1; only `entities[4].kind: required nonempty str`. It is excluded before indexing/counting; no duplicate-ID or ambiguous-place conclusion arises. This distinguishes malformed rows from multiple schema-valid candidates.
- Controls on baseline copies: `unique-place` (`harbor`) exits 0/CLEAN; `unique-character` (`mira`) exits 1 with `timeline[0].place_id: not a place 'mira'`; `dangling` (`missing`) exits 1 with `timeline[0].place_id: dangling entity 'missing'`.

This confirms the LOG premise for duplicate **schema-valid** entity candidates. It does not show that malformed required-field rows should count as identity candidates; the existing checker excludes them from `data` and downstream semantic checks. Nor does it establish ambiguity handling elsewhere beyond inspected consumers.

## Recommendations (not implementation)

1. At timeline `place_id` validation, consult the raw schema-valid entity-ID count as well as the index. For count greater than one, emit a local ambiguous-place-reference finding and skip the kind classification; preserve the duplicate-ID diagnostic. Keep count zero as dangling and count one as existing kind validation.
2. Pair fixtures differing only in ordering of two schema-valid duplicate `harbor` rows (place/character) and assert equivalent ambiguous-place outcomes. Add unique-place, unique-non-place, dangling controls. A malformed duplicate candidate should remain a schema error, not be treated as an ambiguous valid entity.
3. Bound the finding to the timeline `place_id` type branch. Do not imply ambiguity is fixed for every entity-index consumer, and do not interpret it as canon or source-truth judgment.
