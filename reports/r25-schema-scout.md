# Round 25 schema scout — duplicate entity rows

Scope: inspect structurally admitted duplicates only; no checker/fixture edits and no canon or game-mechanics claims.

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:8-14` defines required top-level fields and exact Python types; entity rows require `id`, `kind`, `name`, `first_appearance`, and `claims`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:32-42` admits a row to `data[section]` only if it is an object and all required fields have the right types and nonempty strings. Extra fields are not rejected.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-50,57` reports duplicate IDs but assigns each row to the index in sequence, so the later row replaces the earlier row for lookup. `.shokunin/lore/corpus/fixtures/check_bible.py:127-132` separately counts every admitted entity row; relation endpoint checks at `:137-143` use that count and report ambiguity when count exceeds one.
- `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/entities.json:3-12` has first `mira`, a character with a nonempty sourced claim; `:51-63` has the second `mira`, character “Mira of the second ledger,” also with a sourced claim. The second row is structurally admitted despite duplicate ID. `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/relations.json:2-7` references `mira` at `from` and `seal` at `to`.
- `.shokunin/lore/corpus/fixtures/r21-ambiguous-actor/entities.json:3-12,51-56` likewise has two admitted character rows with ID `mira`; the later row has a valid empty claims list. `.shokunin/lore/corpus/fixtures/r21-ambiguous-actor/relations.json:2-7` supplies the same endpoint shape.

## Risks / limits

- These fixtures support only the structural assertion “two admitted entity rows share this ID.” The second row’s claims, names, and source references do not establish whether the rows denote the same person or distinct people; do not select the later index winner or infer relationship truth.
- The validator allows arbitrary extra keys (`check_bible.py:32-42`), while its per-row validation checks only required fields. These examples have no extras, but a claimed schema guarantee must not overstate coverage of optional/extra data.
- Duplicate-ID diagnostic and dictionary overwrite behavior coexist; consumers using the entity index can observe only the later row unless they consult counts/raw rows. Endpoint ambiguity must be based on admitted-row counts, not whichever row survived indexing.
- `r12` and `r21` are not a controlled pair: their second duplicate differs (a sourced claim in r12, empty claims in r21). Neither is a duplicate-`to` test; each relation’s `to` is unique `seal`. Their existence alone does not validate the round’s requested `to` behavior.
- Citations here are fixture IDs and fictional strings only; this inspection verifies no source-text chronology, canon truth, or game mechanics.
