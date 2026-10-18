# Round 2 rule scout: symmetry edge cases

## Evidence inspected

- `.shokunin/lore/LOG.md` Round 2 declares a narrow convention: an `allied_with` relation between two factions requires an explicitly sourced reciprocal relation; one-way records should be reported, never repaired. It expressly excludes inferring alliances from narrative text or treating all missing relations as contradictions.
- `.shokunin/lore/corpus/fixtures/check_bible.py` defines each relation as `{from, to, type, source_id}`. Current validation checks endpoints against the entity ID index and source IDs against `sources.json`; it does not validate endpoint kinds, relation vocabularies, duplicate relations, or symmetry. Its dangling-endpoint check does not stop subsequent source validation.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json` contains a directed-looking `mira` → `seal` `carries` relation. This is a useful guard against accidentally making all relations reciprocal.
- `.shokunin/lore/corpus/fixtures/contradictions/relations.json` contains the valid `carries` edge plus a dangling `consults` target (`missing-map`), evidencing current invalid-endpoint behavior.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` currently has no faction entities. Existing fixtures cannot establish faction endpoint-kind behavior without adding factions.

## Edge cases for the declared rule

1. **Relation direction matters.** For distinct faction IDs A and B, `allied_with(A,B)` alone is the missing-reciprocal case. A matching `allied_with(B,A)` satisfies the stated convention. Do not reverse `carries`, `consults`, or other relation types: the existing `mira` → `seal` `carries` row is a regression guard.
2. **Do not accept a different type as the reciprocal.** `allied_with(B,A)` is not supplied by `enemy_of(B,A)` or any other type. The declared test is same type, reversed endpoints.
3. **Self-edge.** For `allied_with(A,A)`, the reversed endpoints are identical. Under a purely literal reciprocal-presence test, that row is its own reciprocal and should not be flagged. The declaration does not prohibit self-relations; rejecting them would add a separate rule and should not be smuggled in as symmetry. Document or test this interpretation if implementation touches it.
4. **Invalid endpoint.** If either endpoint ID is absent, the row already merits a dangling-endpoint error. Do not generate an additional “missing reciprocal” error for it: no valid counterpart can be established. Keep the current relation-local dangling diagnostic and continue checking its source citation as today. If an ID exists but is not a faction, the round declaration limits the symmetry rule to faction pairs; current schema has no endpoint-kind validation, so avoid silently extending this axis to add one. If the implementer does add a minimal guard, state whether non-faction `allied_with` is out of scope or invalid; do not infer factionhood from names.
5. **Duplicate rows.** Two identical A→B rows do not provide the reversed B→A edge; still report missing reciprocal. Conversely, one A→B and one B→A row meet reciprocal presence, even if either is repeated. Duplicate-relation policy is not declared; do not report duplicates as symmetry failures or add a generic deduplication rule in this round.
6. **Citations are per relation.** A reciprocal row must itself have a valid `source_id` under the existing schema. Do not treat a citation on A→B as citation for B→A, auto-create the other row, or suppress the symmetry warning because the forward row is cited. An invalid citation on an existing reverse row should yield its normal citation error; whether it also counts as reciprocal presence is a policy detail not specified by the LOG. Safest narrow interpretation: relation presence is structural, citation validation independent, and report both issues only if the independent checks each warrant them.
7. **Order and multiple edges.** Array order should not affect the result; matching should use exact IDs and exact relation type, not display names. If there are multiple faction pairs, report each unpaired directed edge at its own `relations[index]` location; do not report merely one summary for the whole table.
8. **Conflicting opposite records.** A pair of opposite `allied_with` rows satisfies this structural symmetry check even if their source claims conflict; this rule is not a claim-consistency resolver. Preserve cited assertions and leave conflicts for editorial review. Do not infer reciprocity from a prose claim, a different edge, or an absent row.

## Minimal test matrix to consider

| Rows / endpoints | Expected symmetry result | Caution |
|---|---|---|
| Valid faction A→B `allied_with`, no reverse | Report at forward row | No mutation |
| Valid A→B and B→A, same type | No symmetry violation | Check both citations independently |
| A→A `allied_with` | No violation under literal presence rule | Self-edge prohibition would be new policy |
| A→B `carries` only | No symmetry violation | Existing directed fixture is regression guard |
| A→B `allied_with`, B→A `enemy_of` | Missing reciprocal | Exact type match |
| A→unknown `allied_with` | Dangling endpoint only, not symmetry cascade | Existing endpoint validator applies |
| Duplicate A→B only | Missing reciprocal | Duplicates do not reverse direction |
| Reciprocal row exists but has unknown source | Symmetry structurally present; source error remains | Citation and symmetry are independent |
| Existing non-faction endpoint in `allied_with` | No conclusion from current declaration/schema | Endpoint-kind rule would be extra scope |

## Cautions

The current fixture schema accepts arbitrary relation `type` strings and only verifies that endpoint IDs exist; no faction fixture exists yet. A test of the new convention therefore needs explicit faction entities and sourced relation rows. Keep scope to exact `allied_with` records between faction IDs. This is a consistency convention for the invented fixture data, not a universal relation ontology. The checker should report findings and never insert reciprocal rows or alter canon. No gameplay or real-world rights claims are made here.
