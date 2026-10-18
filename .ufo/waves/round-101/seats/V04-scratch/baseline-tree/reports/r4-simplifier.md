# Round 4 simplifier: exact duplicate display names

## Observed

- `.shokunin/lore/corpus/fixtures/check_bible.py` requires each entity to have a nonempty string `name`, indexes entities by `id`, and has no check grouping entity records by `name`.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` demonstrates the existing `id`/`name` fields (for example, `mira` / `Mira` and `seal` / `Blue Seal`). The schema has no alias or disambiguation field.
- `.shokunin/lore/LOG.md`, Round 4 declaration, scopes the claim to two distinct entity IDs with the same case-sensitive displayed `name`; it explicitly excludes case-folding, alias semantics, and merging canon.

## Recommendation

Use one exact comparison over structurally valid entity rows: when two records have different `id` values and identical `name` strings, emit one name-collision violation identifying both `entities[index]` locations and both IDs. Keep the records and IDs unchanged. This is the smallest diagnostic: reuse the required `name` and `id` fields, and do not add an alias ontology, normalization, name-resolution policy, or identity inference. Preserve case sensitivity (`Mira` and `mira` do not match).

Do not add an exception/disambiguation field for this round. If an exception is later required, separately document and source it; silently suppressing an exact duplicate would weaken this diagnostic. The check reports a data collision for review, not proof that the records denote the same person/entity or that duplicate names are impossible in canon.

## Separate recommendations (not part of this round's rule)

- Keep malformed/missing fields under the existing schema diagnostics; do not run the name comparison on records that failed required-field validation.
- Duplicate IDs are already handled by the entity ID index. Avoid producing a second name-collision message for rows with the same ID; this round's claim concerns distinct IDs.
- Do not extend this check to aliases, case folding, whitespace normalization, transliteration, or free-text mentions without a separate claim and evidence.
