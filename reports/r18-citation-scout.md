# Round 18 citation and identity scout

## Raw observations (baseline)

- The checker maintains separate identity namespaces/counts: `entity_id_counts` is built from schema-valid `entities` rows, while `source_id_counts` is built from schema-valid `sources` rows. Repeated `entities[].id` produces a duplicate-entity diagnostic and raises `place_id_count`; repeated `sources[].id` makes `source_status(...)` ambiguous. Neither count resolves the other namespace.
- For timeline place references, `place_id_count > 1` emits `ambiguous place entity`; a count of one is checked for `kind == 'place'`. The current occupancy gate is `place_id_count != 1 or kind == 'place'`, so a duplicate place ID still enters raw-ID occupancy comparison/insertion. The duplicate diagnostic is not a resolution of which entity row—or which kind/name—the ID denotes.
- `source_id` is checked for presence/uniqueness against `sources.json`. The checker does not load or compare source text, and does not establish that a citation supports a timeline description, entity claim, place, or event. A unique source ID is a uniquely indexed reference, not corroboration or narrative truth; an ambiguous source ID remains ambiguous even when its text/title looks familiar.
- Entity `id` and `name` are distinct fields. References use IDs; the checker does not resolve an entity by display name, require names to be unique, or infer that equal names mean equal entities. Likewise, two rows sharing an entity ID are input identity ambiguity, not evidence of two canon entities with that name. Source titles and source IDs are also distinct; a title is not a citation-resolution key.
- Existing fixture `r11-place-character` illustrates ID ambiguity with two rows sharing `id: harbor`, while the rows have different kinds and display names (`Lantern Harbor` / `Harbor Keeper`). Their `archive-ledger` references resolve uniquely as source IDs, but the checker does not inspect that source's text to settle the entity ambiguity. The timeline description/citation in that inherited fixture should not be used as independent evidence about which duplicate row is intended.

## Recommendations (not observations)

- Describe the round-18 case strictly as an ambiguous **entity ID / place reference in the fixture input**. Do not call it a source-citation ambiguity, a second canon place, a name collision, or proof the source is wrong.
- In paired fixture prose, say that the input row has `place_id: harbor` (or the selected duplicate ID), and explicitly avoid attributing that field/value to `courier-log` or `archive-ledger` text. A unique `source_id` on the row shows only reference identity.
- State the intended scope of any checker outcome as withholding or retaining a definite checker-ID occupancy diagnostic. It cannot determine the actual place, whether the source supports either row, whether either entity is true in canon, or whether a real conflict exists.
- Keep controls grounded in IDs/counts and fixture inputs: duplicate-ID case versus otherwise equivalent uniquely indexed place pair. Do not use display names to resolve the duplicate, and do not imply a source citation resolves it.
