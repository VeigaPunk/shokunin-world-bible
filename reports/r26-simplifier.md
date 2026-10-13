# Round 26 simplifier: fixture-only proposal

## Smallest implementation

Add one `r26-to-malformed` fixture by copying `r25-to-ambiguous/` and changing exactly one field in its second `seal` row: remove `name` (the required field at `check_bible.py:11`). Keep the first valid `seal` row (`r25-to-ambiguous/entities.json:39-49`) and relation (`r25-to-ambiguous/relations.json:1-7`) untouched. The malformed row is currently `entities.json:51-56`; omitting `name` makes that row fail screening, while preserving its repeated ID and all other fields. No checker change and no additional control fixture are needed: existing `r25-to-ambiguous` is the admitted-duplicate positive control, and `r25-to-unique` is the unique control.

## Evidence, risk, and test

`check_bible.py:10-19` requires each entity field and appends only `valid` rows to `data['entities']`; `check_bible.py:33-40` and `:82-85` build entity indexes/counts from that screened list. Thus the mutation should yield `entities[4].name: required nonempty str`, but no duplicate-ID finding for the screened-out row and no `relations[0].to: ambiguous entity 'seal'` from that row. Do not characterize absence of ambiguity as proof that the malformed row is false, irrelevant, or non-canon; it shows only this checker excludes incomplete rows from its entity index.

Risk: removing a field tests the exact required-field gate, but does not establish handling of every malformed value or source-evidence validity. The copied fixture must keep every other byte unchanged; inspect the diff to confirm the one-field mutation. Run `check_bible.py` on the malformed fixture, r25 ambiguous, and r25 unique: expect malformed exit 1 with required-name error and without endpoint ambiguity; admitted duplicate keeps endpoint ambiguity; unique control has no endpoint ambiguity (and exits 0). Then replay all 75 pre-existing fixture directories and compare stdout, stderr, and exit status to the declared baseline; verify all 374 existing fixture JSON paths remain byte-identical. No relation/source claim or canon inference is tested.
