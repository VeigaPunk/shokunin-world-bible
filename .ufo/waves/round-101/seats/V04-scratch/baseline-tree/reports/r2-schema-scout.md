# Round 2 relation-schema scout

## Findings

- Relation records are flat JSON objects with required fields `from`, `to`, `type`, and `source_id`; see `.shokunin/lore/corpus/fixtures/check_bible.py:8-13` (`FIELDS['relations']`). Each valid row is retained as `(location, row)` in `data['relations']`.
- Entity kinds are restricted to `character`, `place`, `faction`, and `item` at `.shokunin/lore/corpus/fixtures/check_bible.py:7`. `faction` is supported by the schema, but neither current fixture defines a faction: `.shokunin/lore/corpus/fixtures/consistent/entities.json:1-50` lists character/place/item only. The consistent relation is `mira -> seal`, type `carries`, sourced to `courier-log` (`consistent/relations.json:1-8`).
- The contradictions fixture currently has a normal `carries` relation and a `consults` relation from `mira` to a dangling `missing-map` endpoint (`contradictions/relations.json:1-14`). The checker reports dangling endpoints and unknown sources in the relation pass (`check_bible.py:71-75`); it does not currently interpret relation types or check reciprocal edges.
- Relation/source claims are individually cited: README states every relation must cite an in-world source (`.shokunin/lore/corpus/fixtures/README.md`, paragraphs 3-4). Source lookup builds `sources` before relation validation (`check_bible.py:52-58`).

## Exact insertion point

The narrow insertion point for a faction-only reciprocal `allied_with` convention is immediately after the existing relation loop at `.shokunin/lore/corpus/fixtures/check_bible.py:71-75` and before `occupied = {}` at line 77. At that point the `entities` and `sources` indexes already exist, and base relation endpoint/source checks have run. A second pass over valid `data['relations']` can identify eligible faction-to-faction `allied_with` rows, find a reverse row with the same relation type, and append a violation including the originating relation's `location` when absent. This preserves the current checker's report-only flow (returned `errors`, no mutation).

## Cautions for executor

1. Apply the convention only to rows whose type is exactly `allied_with` and whose two resolvable endpoints both have kind `faction`; do not impose symmetry on `carries`, `consults`, or other directed relations. Guard endpoint membership before indexing `entities`, since this fixture includes a dangling endpoint and the existing pass reports it rather than aborting.
2. Reciprocal presence is a relation-record check, not an inference from narrative, and not a general rule that every relationship needs a converse. Keep the restriction and fixture-specific convention explicit in documentation.
3. Require an actual reverse record, not merely the same unordered pair. Decide and state handling of a self-loop (`A -> A`): a naive reverse-key lookup matches itself, so either exempt self-loops or require a distinct reciprocal row. No current fixture covers this case.
4. Preserve citation validation on each relation. A reverse edge should itself carry a known `source_id`; avoid treating one direction's citation as covering the other.
5. Avoid cascaded symmetry errors for malformed endpoints. A missing reciprocal diagnostic should be anchored to the original relation location and should not hide the existing dangling-endpoint message.

Evidence is limited to the checked-in fixture schema and examples; no broader lore ontology is implied.
