# Round 3 simplifier report — reference resolution

## Recommendation (not yet implementation)

Use the existing `entities[].claims[]` records as the sole target type for contradiction-ledger references. Give each claim a short, explicit `id` (unique across the bible), then let `claim_a` and `claim_b` contain those IDs. Validate only that each ID is a nonempty string, each referenced claim ID resolves exactly once, the two references are distinct, and `why` is a nonempty string. Keep the existing claim `statement` and `source_id` validation; do not duplicate statements or source citations inside the ledger. Report malformed references at the ledger record, and preserve all valid records as editorial assertions.

This is the smallest direct reference scheme that is stable when claims are reordered. Do not resolve free-form prose, match text or citations heuristically, infer that two claims conflict, or require a ledger entry to correspond to each checker diagnostic. The checker can validate that the references exist; a human asserts that they contradict. Do not make the ledger file mandatory for fixtures that do not use it unless the declared round-3 scope explicitly requires it.

## Evidence from the repository

- `.shokunin/lore/corpus/fixtures/check_bible.py` currently stores each claim as an object with `statement` and `source_id` under an entity; it validates both text and source resolution. The checker already indexes `sources`, `entities`, and `timeline` by explicit `id`, and reports duplicate IDs. Extending the same explicit-ID/reference pattern to claims avoids a second resolution mechanism.
- The same checker returns diagnostic strings for dangling relation endpoints, timeline inversion, and double booking. These diagnostics are not claim records and do not identify a pair of claim objects. Matching ledger entries to those strings would couple editorial data to implementation wording and impose semantic interpretation.
- `.shokunin/lore/corpus/fixtures/contradictions/entities.json` has sourced claims for Mira, the harbor, tower, and seal, while its seeded relation and timeline conflicts are represented in `relations.json` and `timeline.json`. Existing claim objects have no identifiers. `.shokunin/lore/corpus/fixtures/contradictions/timeline.json` includes `arrival` and `false-sighting` at distinct places for Mira at tick 2, but that is a structural conflict, not two existing entity-claim records; do not pretend those records already satisfy a claim-reference contract.
- `.shokunin/lore/corpus/fixtures/README.md` says contradictions require editorial review and the checker does not choose a canon answer. Explicit IDs plus existence checks preserve that boundary.

## Scope caveat

If the round requires each of the three seeded checker violations to be represented in the ledger, first give those assertions explicit claim records (with citations) rather than inventing references to diagnostics. That is a larger fixture/schema change, and the validator should still check only IDs and required fields—not whether the assertions are truly contradictory. The proposed entity-claim-only model is appropriate only if ledger records are allowed to document selected sourced claims rather than mechanically mirror every structural violation.
