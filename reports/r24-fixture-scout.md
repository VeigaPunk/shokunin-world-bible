# Round 24 fixture scout

## Finding
The smallest source-cited ambiguity fixture is a copy of `r12-ambiguous-actor`, changing no source/relation rows: it already has a duplicate `mira` entity ID and a cited `mira -> seal` `carries` relation. Use it as the ambiguous case, and `r12-unique-actor` as its unique control; the two directories differ only in the extra entity row. This isolates the exact relation-local endpoint resolution question while preserving the established source citation. Avoid adding a new source or inventing a new relation.

## Evidence
- `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/entities.json:1-8` starts the first `mira` entity; `:48-63` contains the second entity with `id: "mira"` (the duplicate row), whose claim cites `archive-ledger` at `:56-59`.
- `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/relations.json:2-7` contains one `carries` relation: `from: "mira"`, `to: "seal"`, cited by `courier-log`.
- `.shokunin/lore/corpus/fixtures/r12-unique-actor/entities.json:1-8` has the first `mira`; its file ends after the four unique entities (`:1-48`), so the duplicate is the only material fixture difference.
- `.shokunin/lore/corpus/fixtures/r12-unique-actor/relations.json:2-7` is the same cited relation.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-51` emits the duplicate-ID diagnostic but overwrites the index entry with the later row. At `:118-122`, the current relation endpoint check tests only membership in that index, so `mira` passes despite duplicate identity.
- `.shokunin/lore/corpus/fixtures/README.md:36-39` documents source IDs as in-world fictional records and cautions against inferring facts beyond the fixtures; retain this boundary.

## Risks
The duplicate row is labelled “Mira of the second ledger,” but the checker must not pick either row as the true referent. The desired new finding should be relation-local and say the endpoint ID is ambiguous, while leaving the existing duplicate-ID diagnostic intact. Do not claim that the relation is false, or that either source establishes canon; citations here establish fixture provenance only. The proposed control should remain clean under the new check.

## Suggested test
Run `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-ambiguous-actor` and the same command with `r12-unique-actor`. Assert the ambiguous fixture still has the existing duplicate-entity-ID finding and additionally has exactly the relation-local ambiguous `from` endpoint finding for `relations[0]`; assert no ambiguity finding on its unique `to` endpoint. Assert the unique control exits 0 with no ambiguity diagnostic. Compare all pre-existing fixture outputs against saved baseline before admitting the change; the new rule must not alter old outputs or resolve the endpoint.
