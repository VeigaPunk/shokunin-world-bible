# Round 26 screen scout — admitted entity rows and ID counts

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:21-43`: each section row is schema-checked; a failed required-field/type/nonempty-string check emits an error and sets `valid = False`. Only valid rows are appended to `data[section]`. For `entities`, the required fields are `id`, `kind`, `name`, `first_appearance`, and `claims` (`:8-14`); the `claims` value need only be a list at this screening stage.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-59`: `index('entities')` and downstream entity processing consume `data['entities']`; the index overwrites duplicate keys but separately emits a duplicate-ID error. The separate count is built from the same screened rows at `:118-121`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:123-130`: relation endpoints are labeled ambiguous only when their ID is present in the entity index and its screened-row count exceeds one. This means a malformed duplicate excluded at `:43` does not increase that count or trigger endpoint ambiguity by this path; its own schema failure remains a finding.
- `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/entities.json` (row 5): the existing duplicate `seal` control is complete and admitted, so it is an appropriate positive comparator. Its corresponding unique control is `r25-to-unique/entities.json` (one `seal`).

## Calibration / risk

The bounded claim is about this checker's structural screen and count, not source truth. A malformed duplicate row is still present in input and gets a schema error; absence of the endpoint-ambiguity diagnostic means only that this implementation counts admitted rows. It is not evidence that the malformed row is false, irrelevant, non-canonical, or absent from the fictional world. Avoid wording such as “the duplicate is ignored” without the precise qualifier “excluded from `data['entities']` and its ID count.”

One-field mutation should preserve `id: seal` and all other duplicate-row content, while deleting a required field (e.g. `name`) or changing its type. Prefer deletion of `name`: it gives the targeted `entities[4].name: required nonempty str` schema error, leaves the cited relation and first admitted target intact, and avoids introducing an invalid alternate value. Do not claim no ambiguity merely because the endpoint error is absent: verify the admitted positive control still emits `relations[0].to: ambiguous entity 'seal'`, and verify the malformed case retains the schema error and lacks that endpoint diagnostic. A `claims`-shape mutation is less discriminating because nested claim contents are checked later and the top-level field itself is only screened as a list.

## Test

Run `check_bible.py` on (1) the current `r25-to-unique`, (2) current `r25-to-ambiguous`, and (3) a copied matched case whose second `seal` row omits only `name`. Compare exact stdout/stderr/exit status. Expected: unique clean; admitted duplicate exits nonzero with duplicate-ID plus `relations[0].to` ambiguity; malformed duplicate exits nonzero with its missing-name schema finding (and duplicate-ID finding for the still-admitted duplicate? No: it is screened out, so no duplicate entity-ID finding), while preserving other applicable diagnostics and showing no `relations[0].to` ambiguity. Also replay all 75 baseline fixture directories against the declared baseline and compare the 374 existing JSON paths byte-for-byte before admitting any new fixture. Keep this as a report-only scout; no checker, fixture, LOG, or other document edits made.
