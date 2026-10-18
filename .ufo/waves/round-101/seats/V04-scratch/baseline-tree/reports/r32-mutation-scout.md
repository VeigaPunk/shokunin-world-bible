# Round 32 mutation scout — blank-title duplicate source

## Recommendation

Use `.shokunin/lore/corpus/fixtures/r31-source-ambiguous/sources.json` as the mutation base. In its second `courier-log` row (lines 15–19), change only `title` from `Courier Log Registry Duplicate Index` to the empty string. This is the exact one-field mutation: retain the duplicate ID and all other fields/rows. The matched valid-duplicate case remains unchanged; `consistent/` is the unique-source control.

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:8-14` declares `sources` required fields, including `title: str`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:32-43` validates each raw row and admits it to `data[section]` only when every required field passes. At `:39-41`, blank/whitespace-only strings generate the row-local required-nonempty error and set `valid = False`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:53-56` constructs source multiplicities only from admitted `data['sources']` rows. `.shokunin/lore/corpus/fixtures/check_bible.py:64-74` maps count >1 to ambiguous and emits a location-specific citation diagnostic.
- `.shokunin/lore/corpus/fixtures/r31-source-ambiguous/sources.json:15-19` is the second duplicate row; its title is the one candidate field to blank. The valid first `courier-log` row is at `:8-13`.
- The seven unchanged citation references expected to lose ambiguity diagnostics are two `mira` fields and two `seal` fields in `.shokunin/lore/corpus/fixtures/r31-source-ambiguous/entities.json:4-11, 31-38`, `relations[0]` in `relations.json:2-7`, and timeline rows in `timeline.json:2-10, 11-19`. (The first appearance and claim source references each account for separate findings.)

## Risks and falsifiable test

Risk: absence of duplicate-ID/ambiguous-citation diagnostics after the malformed row is screened out describes this checker's admitted-row counting only. The raw duplicate remains in the input; this is not evidence of source uniqueness in-world, false evidence, canon, or rights.

Create a temporary copy of `r31-source-ambiguous/` and blank only `sources[2].title`; run `python3 .shokunin/lore/corpus/fixtures/check_bible.py <case>`. Falsifiable expected result: nonzero exit with `sources[2].title: required nonempty str`; no duplicate `sources` ID finding and no seven ambiguous-citation findings. The unmodified r31 duplicate must retain its eight findings, and the unique control must exit 0. Diff the matched source JSON to verify only that value changed. Regression acceptance is the declared exact replay: 83 pre-existing fixture stdout/stderr/exit tuples and 414 pre-existing JSON path bytes unchanged. No checker, fixture, LOG, or README edits are proposed here.
