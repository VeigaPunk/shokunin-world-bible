# Round 26 mutation scout — malformed duplicate target

## Recommendation

Use the existing `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/entities.json` duplicate `seal` row as the one-field mutation source. Change only the duplicate row’s `name` value from `Seal in courier ledger` to the empty string. This violates the required nonempty-string condition while retaining the duplicate `id`, kind, first-appearance citation, and claims. Do not change relation or source rows.

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:8-14` declares entity `name` a required `str` field.
- `.shokunin/lore/corpus/fixtures/check_bible.py:32-42` screens a row out of `data['entities']` when a required string is blank (`not row[field].strip()`); only rows with all required fields valid are appended.
- `.shokunin/lore/corpus/fixtures/check_bible.py:67-74` builds entity ID counts from the admitted `data['entities']` rows, not all raw JSON rows.
- `.shokhun/lore/corpus/fixtures/check_bible.py:137-143` (correct path: `.shokunin/lore/corpus/fixtures/check_bible.py:137-143`) diagnoses a relation endpoint as ambiguous only when that admitted-row count exceeds one; otherwise it does not choose an entity row based on the raw malformed duplicate.
- `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/entities.json:50-56` is the second `seal` row; its `name` is the single candidate field to blank. The first valid `seal` remains at `entities.json:37-46`.
- `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/relations.json:2-6` retains `mira -> seal`, cited by `courier-log`; `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/sources.json:7-11` identifies that source as fictional.
- `.shokunin/lore/corpus/fixtures/r25-to-unique/entities.json` and `relations.json` supply the clean unique-target control; `.shokunin/lore/LOG.md` round 25 closure reports the admitted duplicate case and its relation-local `to` ambiguity.

## Risk and test

Risk: screening out one malformed row is not proof that its assertion is false, that the target is canonically unique, or that the source lacks evidence. The expected distinction is strictly structural: malformed duplicate is reported at its row, but does not count as a second admitted endpoint. The matched admitted-duplicate r25 case should continue to emit `relations[0].to: ambiguous entity 'seal'`; the unique control should stay clean. Replay with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` and confirm the malformed case emits the required-name diagnostic and no relation-to ambiguity. Compare the matched fixture JSON files to ensure only that one `name` field changed. No checker, fixture, or other documentation edits are proposed by this scout.
