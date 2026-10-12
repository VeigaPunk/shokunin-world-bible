# Round 2 scribe note — decision-table scope

## Proposed scope wording

> This rule checks only relations whose type is exactly `allied_with` and whose endpoints are both entities of kind `faction`. For each such directed relation A → B, require a separately listed, explicitly sourced `allied_with` relation B → A. Report a missing reciprocal edge against the original relation; do not add edges, infer intent from prose, or select canon. Other relation types are outside this rule. A relation with a missing endpoint or non-faction endpoint is not evidence of a broken alliance pair; report it under the existing endpoint/schema checks (or state explicitly if that case remains unsupported).

## Compact decision table wording

| Input condition | Result |
|---|---|
| `allied_with` has valid faction endpoints and a reverse `allied_with` edge with a valid in-world source ID | Pass this rule |
| `allied_with` has valid faction endpoints but no reverse edge | Report missing reciprocal relation at the original relation's location; do not modify data |
| Reverse edge exists but lacks a valid source ID | Citation validation reports that edge; it does not satisfy the “explicitly sourced” condition |
| Relation type is not exactly `allied_with` | Outside this symmetry rule |
| Endpoint is missing or is not a faction | Do not classify as a reciprocal-symmetry failure; existing checks may report dangling references, but faction-kind enforcement must not be implied unless implemented |

“Reciprocal” here means an explicit reverse relation record, not a conclusion from narrative text. The rule encodes only the declared fixture convention; it does not claim that every fictional alliance must be symmetric, nor that absent relations are contradictions in general.

## Evidence paths and cautions

- `.shokunin/lore/LOG.md` — round-2 declaration: narrow `allied_with` rule, cited reciprocal edge, report-only/no canon mutation, with limits on narrative inference.
- `.shokunin/lore/corpus/fixtures/check_bible.py` — current relation checks validate entity endpoints and source IDs, but do not validate endpoint kinds or relation symmetry.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json` — current sole relation is `carries` (`mira` → `seal`); no alliance case exists in baseline.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` — baseline has no faction entities; fixture changes are required to demonstrate this rule.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json` — source IDs are fictional in-world records; reciprocal records need their own valid citation IDs.
- `.shokunin/lore/corpus/fixtures/README.md` — established report-not-resolve convention and separation of in-world citations from real-world references.

Caution: the table is specification wording, not evidence that implementation or fixtures already satisfy it. Do not make real-world rights claims, verify game mechanics, or silently resolve contradictions.
