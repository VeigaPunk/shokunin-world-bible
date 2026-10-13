# Round 27 both-endpoint ambiguity scout

## Evidence

- `.shokunin/lore/LOG.md:405` declares the untested simultaneous case: one relation whose `from` and `to` IDs are each duplicated among admitted entities; it distinguishes that from the earlier separate endpoint probes.
- `.shokunin/lore/corpus/fixtures/check_bible.py:37-43` admits only rows passing every required field check into `data[section]`. Thus the test must make both duplicate rows schema-admitted; a malformed second entity would not exercise the simultaneous count.
- `.shokunin/lore/corpus/fixtures/check_bible.py:119-121` counts IDs over admitted `data['entities']` rows.
- `.shokunin/lore/corpus/fixtures/check_bible.py:123-130` iterates every admitted relation, then independently checks `('from', 'to')`; each endpoint is diagnosed against the same entity index/counts. This control flow predicts both endpoint-local diagnostics when both IDs have counts above one, but code inspection alone is not a replay.
- `.shokunin/lore/LOG.md:406` specifies a matched control duplicating only `seal`, preserving the `mira -> seal` relation, and the expected diagnostic distinction. This bounds the test; it does not establish relation truth.

## Risk

The main coverage risk is a test that duplicates `mira` and `seal` but accidentally changes the relation, source citation, or other tables between paired cases, making diagnostic differences hard to attribute. Another risk is using an incomplete duplicate row: it is screened out before ID counting, so it cannot establish simultaneous admitted-endpoint behavior. Do not treat validator output as deciding whether either relation is true, resolving which entity is intended, or establishing canon uniqueness.

## Proposed test

Use a byte-matched pair following LOG: preserve the same cited `mira -> seal` relation and all shared tables; both case has one additional fully valid `mira` row and one additional fully valid `seal` row, while control has only the additional valid `seal` row. Run the existing checker on both. Assert the both case contains duplicate-ID findings and exactly one ambiguity diagnostic for each `relations[0].from` and `.to`; assert control retains `.to` ambiguity and has no `.from` ambiguity. Compare exact stdout/stderr/exit and preserve the declared prior-fixture regression baseline. This tests simultaneous endpoint coverage only, not semantic or canon claims.
