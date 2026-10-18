# Round 29 map-scout — unsupported is not false

## Decision

For a manual clause map, distinguish **supported**, **contradicted**, and **unsupported / unassessed**. “Unsupported” means the supplied clause does not entail the record; it is not evidence that the asserted proposition is false. Do not convert absence of entailment into an in-world negation, contradiction, or canon verdict. Reserve “contradicted” for an explicit incompatible statement in the inspected material, and even then describe the textual conflict rather than adjudicating which account is true.

For the round-29 near-miss, map `relations[0].type=carries` as **unsupported by this excerpt**: “The blue seal was near Mira” asserts proximity, not the action of carrying. It neither entails carrying nor says Mira did not carry the seal at another time. Keep the record intact and leave its truth unresolved. This classification is distinct from the checker’s structural acceptance: a clean exit only means the JSON passed its structural checks.

## Evidence (path:line)

- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:3` quotes “I, Mira, carried the blue seal,” explicitly describing its lexical content.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:5` states that speaker/name-to-ID alignments are editorial stipulations, not lexical entailment or external verification.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:7` maps “carried” to `type=carries` and limits the mapping to `relations[0]`.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:9` says other JSON claims/events are unsupported by that excerpt; it does not label them false.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:9` also says the near-miss “the seal was near Mira” would not entail carrying and would not support `carries`.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relations.json:2-7` records `mira` → `seal`, `carries`, cited to `courier-log`; this is the selected assertion at issue, not prose proof.
- `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3` contains the positive fictional clause, “I, Mira, carried the blue seal.”
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md:230` (Round 23 witnessed-absence row) expressly says a report is not proof and must not delete entities or clear occupancy. The broader policy supports preserving unresolved assertions, but the exact near-miss classification follows from the r28 map, not this unrelated absence example.

## Risk

If “not supported” is collapsed into “false,” the map overclaims what a negative-control sentence establishes and could silently erase a valid assertion whose evidence is simply outside the excerpt. Conversely, if a citation or structural pass is treated as semantic support, it overclaims the source: the relation’s `source_id` resolves a fictional source ID but does not demonstrate what its text says. These are separate questions: citation/shape validity, clause entailment, and truth/canon.

## Falsifiable test

Use a matched pair with all five JSON tables and source IDs byte-identical. Positive excerpt/map: “I, Mira, carried the blue seal.” must map the literal verb to `relations[0].type=carries`, conditional on the map’s editorial ID alignments. Negative-control excerpt/map: “The blue seal was near Mira.” must label that same field **unsupported by the clause**, explicitly **not contradicted/false**. A reviewer falsifies this decision if the negative sentence entails the carrying action, explicitly denies that Mira carried it, or the map calls it false without additional incompatible evidence. Both fixtures may pass structural validation while the prose classification differs; neither clean exit nor unsupported classification settles canon.
