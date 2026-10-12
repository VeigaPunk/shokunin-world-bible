# Round 12 citation and identity scout

## Observed raw paths and output

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py`, especially `index()`, `source_status()` / `source()`, the entity-claim loop, `entity_id_counts`, and the timeline occupancy loop. Inspected `.shokunin/lore/corpus/fixtures/consistent/{sources,entities,timeline}.json` and `.shokunin/lore/corpus/fixtures/README.md` (rounds 9–11). I ran:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations
```

The checker uses separate ID namespaces/counts: `source_id_counts` for source rows and `entity_id_counts` for schema-valid entity rows. `source()` reports unknown or ambiguous source IDs and otherwise returns `unique`; entity claims call it on `first_appearance` and each claim's `source_id`. Timeline rows likewise check their `source_id`. This checks identifier resolution/count only; the code does not open source text or compare claims with it.

Separately, `index('entities')` reports a repeated entity ID, while `entity_id_counts` counts matching schema-valid entity rows. Timeline occupancy is keyed by `(row['entity_id'], row['tick'])`. It does not currently gate that key on an unambiguous entity ID. Thus same-tick events attached to two valid rows with one duplicated entity ID can be grouped as one actor for the different-place `double-booked` finding. This is the round's plausible ambiguity boundary; this scout did not independently construct or execute a round-12 duplicate-actor probe.

The checker does not enforce unique entity display names. `name` is schema-checked as a nonempty string, but no name index or homonym comparison appears in the inspected code. Identical names on distinct entity IDs are therefore distinct from duplicate IDs; source citations do not disambiguate either entity identity or same-name referents.

## Recommendations (not observed checker behavior)

- Keep any proposed guard narrow to timeline `entity_id` occupancy: if its schema-valid entity-ID count exceeds one, report a local ambiguous actor-reference finding and do not infer same-actor occupancy collision from those rows. Preserve the duplicate-entity-ID finding and event rows. Verify against a paired duplicate-actor fixture and a unique-actor control before implementation; this report is not that verification.
- Keep source citation status orthogonal. A unique cited source ID means only that one schema-valid source row bears that ID, not that its text supports an actor, event, or occupancy conclusion.
- Keep name homonyms orthogonal too. Do not treat identical `name` strings as duplicate IDs or infer same person/place from them; do not add a name-uniqueness rule as part of the actor-occupancy move.

## Claim boundary

This is an input-structural diagnostic about ambiguous identifier use in one occupancy check. It does not select a canonical duplicate entity, establish source-text entailment or truth, resolve display-name homonyms, change relation endpoints / place checks / other identity uses, or verify game mechanics. The round's falsifiable paired test and prior-fixture replay remain necessary evidence for any behavior change.
