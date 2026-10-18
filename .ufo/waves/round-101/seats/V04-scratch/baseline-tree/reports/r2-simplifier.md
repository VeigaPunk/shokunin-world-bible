# Round 2 simplifier review

## Smallest change

Implement the declared convention narrowly: for each relation whose `type` is exactly `allied_with`, require a separately present relation with swapped `from`/`to` and the same `type`. If missing, emit one violation at the original relation location. Do not rewrite rows or infer relationships from prose. Keep both claims independently sourced using the existing `source_id` validation; do not require reciprocal records to cite the same source.

This is a local predicate over the existing relation rows, not a new graph ontology. No new relation schema, aliases, generalized inverse metadata, normalization, or migration/compatibility layer is needed. Preserve all other relation types as currently accepted.

## Evidence

- `.shokunin/lore/LOG.md` Round 2 declares one exact `allied_with` symmetry rule, sourced fixture cases, no canon modification, and explicitly avoids inferring alliances from narrative text.
- `.shokunin/lore/corpus/fixtures/check_bible.py`: `KINDS` already includes `faction`; `FIELDS['relations']` already defines the four needed fields (`from`, `to`, `type`, `source_id`); relation validation already checks endpoint existence and source IDs. A targeted check after those validations needs no schema change.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json` has a single existing `carries` edge, so it should remain valid without acquiring new rules.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` presently has no faction, and `consistent/relations.json` has no `allied_with` edge. Add only the minimal two faction records and reciprocal sourced edges needed for a positive case; make the negative case differ by removing one reciprocal edge.
- `.shokunin/lore/corpus/fixtures/README.md` promises that the checker reports, rather than resolves, contradictions and makes no file modifications. A relation-local error preserves that contract.

## Cautions

- An edge-count or “every edge has an identical duplicate” check is wrong for directed relations; compare the endpoints in reverse and match only the declared relation type.
- Do not require all factions to be allied symmetrically in the absence of an explicit `allied_with` record. This rule tests only asserted alliances.
- Avoid asserting that alliance symmetry is universal canon truth: it is a fixture/checker convention declared for this round. Independent reverse records can have distinct citations.
- Keep unrelated malformed-row handling, duplicate IDs, and arbitrary relation types untouched; expanding their semantics would exceed the one-rule axis move.
