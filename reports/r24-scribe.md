# Round 24 scribe: relation-local ambiguous endpoint decision table

Scope: checker-input diagnostics only. Entity indexing retains its current duplicate-ID error and last-row lookup behavior; this proposal adds a relation-local finding when an endpoint ID occurs more than once. It does not identify which duplicate is intended or establish a real/canonical relation.

| Endpoint ID count | Existing endpoint result | Proposed relation-local result | Interpretation |
|---|---|---|---|
| 0 | dangling entity | unchanged dangling finding only | No matching entity row |
| 1 | accepted | unchanged | Unique ID in this fixture |
| >1 | currently accepted via indexed last row (plus duplicate-ID error elsewhere) | add `ambiguous entity endpoint <id>` at the relation endpoint location | Endpoint resolution is indeterminate; do not select a duplicate |

Evidence: `.shokunin/lore/corpus/fixtures/check_bible.py:40-45` builds the index, reports duplicate IDs, then overwrites the indexed value; `:118-122` checks relation endpoints only for dictionary membership, so duplicates pass. `.shokunin/lore/corpus/fixtures/r12-ambiguous-actor/entities.json:3,51` duplicates `mira`; `r12-ambiguous-actor/relations.json:3-4` uses it as `from`, with `seal` as `to`. The parallel r21 control has the same pattern (`r21-ambiguous-actor/entities.json:3,51`; `relations.json:3-4`). Unique-ID comparison: `corpus/fixtures/consistent/relations.json:2-5` references `mira` and `seal`.

Risks / bounds:
- Avoid treating index presence as uniqueness; use occurrence counts already computed for entity IDs (`check_bible.py:126-129`) or equivalent.
- Emit one finding per ambiguous endpoint, at its `.from`/`.to` location; if both are ambiguous, report both. Keep dangling behavior for zero matches and do not cascade into inferred relationship claims.
- Preserve current duplicate-ID diagnostic and other validations. This is a structural ambiguity warning, not a claim about source text, chronology, or canon.

Suggested test: run the existing `r12-ambiguous-actor` fixture and require both the duplicate-entity diagnostic and a relation-local `.from` ambiguity finding; verify `consistent` remains clean. Add a paired fixture probe where only the endpoint ID changes from duplicated to unique, and assert the endpoint ambiguity disappears while other output is unchanged. Replay saved baseline outputs and fixture paths byte-for-byte to check regression.
