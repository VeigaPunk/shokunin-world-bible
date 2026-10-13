# Round 24 non-author reviewer report

## Scope and verdict

Reviewed the Round 24 LOG declaration and amendments, scout/critic/executor reports, checker diff, fixture README, and the `r12`/`r21` controls. The implemented endpoint rule is semantically correct on the inspected paths: it counts only schema-admitted entity rows and classifies each relation endpoint independently as zero, one, or multiple matches. It preserves dangling behavior at zero, emits no endpoint error at one, and emits a relation-local ambiguity at more than one. It does not resolve a duplicate to either indexed row or assert canon.

## Findings

- Structural admission is correctly inherited from `data['entities']`: rows with missing, blank, or wrong-typed required fields never enter the index/count, so invalid entity rows cannot inflate endpoint multiplicity. Relation rows likewise must pass required-field validation before endpoint processing; malformed rows receive their schema finding without a relation endpoint cascade.
- The count map is built from all admitted entity rows before relation traversal. The existing last-row-wins `entities` map remains unchanged for unrelated consumers. Membership guards the count lookup, so zero matches remain dangling and do not become ambiguous; unique matches pass; repeated admitted IDs get one finding at each affected endpoint field. A relation whose both sides name duplicate IDs is handled per side, not inferred as one semantic relationship.
- `r12-ambiguous-actor` produces the pre-existing duplicate-ID finding, the new `relations[0].from` ambiguity for `mira`, and its independent timeline ambiguity findings; its unique `to: seal` has no ambiguity. `r12-unique-actor` has no endpoint ambiguity and its output remains the pre-existing occupancy `double-booked` error (so it is not a clean whole-bible control). `consistent/` is the clean whole-bible control.
- `r21-ambiguous-actor` similarly adds exactly the local ambiguous `from` endpoint while retaining its duplicate entity, timeline, and malformed-dependency findings. It confirms this rule does not erase or mask independent invalid-row/list diagnostics.
- The README decision table accurately states precedence and limits the population to admitted entity rows. It does not claim source text support, truth, or canon; source citation validation remains independent.

The checker diff is limited to moving the existing admitted-row entity count before relation checks and adding the guarded `>1` branch. No semantic failure found in the requested zero/one/many precedence or invalid-row treatment. Independent regression replay and byte/path identity are assigned to the verifier; this report does not certify that separate regression claim.
