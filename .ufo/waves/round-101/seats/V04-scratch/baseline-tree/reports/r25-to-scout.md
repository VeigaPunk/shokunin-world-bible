# Round 25 to-endpoint source/fixture scout

## Finding

The existing fixtures establish a useful, but partial, semantics for duplicate endpoint IDs. A relation endpoint is a string ID resolved against the admitted entity rows; if more than one admitted entity row has that ID, the endpoint is structurally ambiguous. The relation stays unchanged, and the checker diagnoses the endpoint side independently. The present data do **not** supply a duplicated `to` endpoint: existing r12/r21 duplicate-actor cases exercise only `from`. A `to` fixture should duplicate the target entity ID (`seal` here), leaving the relation and cited source intact; a matched unique-target control can then differ by only the duplicate entity row. This checks lookup ambiguity, not whether the cited relation is true.

## Evidence

- Round 25’s declaration says prior r12/r21 fixtures verify duplicate `from` and that no independent duplicate-`to` fixture exists: `.shokunin/lore/LOG.md:366-367` (round 25 section; line numbers as checked in current file).
- Checker iterates both endpoint labels and compares the ID count among entity rows: `.shokunin/lore/corpus/fixtures/check_bible.py:119-129`. A duplicate causes `<relation location>.<endpoint>: ambiguous entity ...`; no row-selection occurs in this branch.
- `r12-ambiguous-actor` has two `mira` rows (`entities.json:2-12,50-59`); its relation references `from: mira`, `to: seal` at `relations.json:2-6`. The second row is attributed to `archive-ledger`; the relation cites `courier-log` (`sources.json:1-11`). This is a from-side probe.
- `r21-ambiguous-actor` similarly adds a second `mira` row at `entities.json:50-57`; relation still has `from: mira`, `to: seal` at `relations.json:2-6`. Its added row has no claims. This too does not probe `to`.
- `r12-unique-actor` retains one `mira` and the same relation fields (`entities.json:2-48`; `relations.json:2-6`), but LOG round 24 records that the fixture has a pre-existing occupancy double-booking violation, so it is not a clean whole-output control: `.shokunin/lore/LOG.md:359`.
- `consistent` supplies a clean unique endpoint relation with `from: mira`, `to: seal`, `type: carries`, `source_id: courier-log` (`.shokunin/lore/corpus/fixtures/consistent/relations.json:2-6`). Its entity rows include one `seal` and one `mira` (`entities.json:2-48`). It is a general clean control, but not a matched duplicate-target pair by itself.
- Source ledger labels `courier-log` as a fictional first-person log and cautions it is not omniscient truth (`consistent/sources.json:7-11`). The entity claim “Mira carried the blue seal” and relation label `carries` are fixture text, not independent validation of world/canon truth (`consistent/entities.json:2-12`; `relations.json:2-6`).

## Fixture design implication / risks

For a clean paired probe, copy the same baseline fixture into two new fixture directories. Keep relation JSON and all sources identical; in the ambiguous member add exactly one admissible entity row with `id: seal` and appropriate structurally valid fields. In the unique member omit that row. Verify the intended change is specifically `relations[0].to: ambiguous entity 'seal'` (and no `from` ambiguity); do not assume the whole fixture exits clean unless baseline is actually clean. The duplicate row may have `claims: []`, as r21 demonstrates that shape, but its first-appearance source must still resolve. Avoid changing relation type, source ID, or endpoint string between pair members, since that would confound ID multiplicity with citation or schema behavior.

Risks: duplicate ID rows themselves may produce a global duplicate-ID diagnostic; that does not substitute for the endpoint-local result. Entity identity and the in-world relation’s truth remain unresolved; matching source IDs only demonstrate fixture attribution. Any “clean control” claim requires observed checker output, since prior controls may have unrelated violations. This scout makes no checker/fixture edits and establishes no canon truth or game mechanic.
