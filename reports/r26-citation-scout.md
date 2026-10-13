# Round 26 citation and rights boundary scout

## Evidence

- `.shokunin/lore/LOG.md: Round 26 declaration` frames the proposed malformed duplicate as a screening test: only complete entity rows enter `data['entities']`; it explicitly disclaims claims about source evidence being false, missing, or canon. The same declaration specifies the preserved cited relation and expected non-ambiguity result.
- `.shokunin/lore/corpus/fixtures/check_bible.py:8-14,21-43` defines the entity required fields and appends rows only when every required field has the expected type/nonempty value. Thus a malformed duplicate is rejected as a row before `index('entities')` counts IDs (`:45-51`); this is a validation boundary, not an assertion about what the source says.
- `.shokunin/lore/corpus/fixtures/check_bible.py:64-74,107-117,228-232` checks source IDs against unique in-world source rows and checks the relation's cited source; these checks establish resolvability of an ID, not source-text support.
- `.shokunin/lore/corpus/fixtures/README.md:36-41` distinguishes in-world fictional citations from the separate real-world inspiration reference ledger, requires citations for entity claims/relations/events, and says entries are invented. `:536-552` describes the r25 pair as an ID-collision test, not a second established seal or endorsed relation; checker does not verify story text or resolve canon.
- `.shokunin/lore/corpus/fixtures/r25-to-ambiguous/entities.json:~1-50` has two schema-valid `seal` rows; both first appearances cite `courier-log`. `relations.json:1-6` cites `courier-log` for the same `mira -> seal` carries assertion. `sources.json:~1-20` supplies that fictional source ID and labels it as an in-world personal log. This is a local fictional citation, not an external citation.

## Boundary / risk

The malformed-row control can show only that the current schema screening excludes that row from entity-ID ambiguity counting while still reporting its required-field error. It cannot prove that the malformed row is absent from the fictional world, that its cited record does not exist, that the relation is true/false, or that the source text supports it. Do not describe the negative ambiguity diagnostic as canon proof or as evidence against the row's content. Keep the same valid first `seal` row and relation/source ID; mutate exactly one required field on the duplicate and avoid adding real-world material or rights-bearing source excerpts. No real-world rights conclusion follows from an in-world fictional source ID.

## Falsifiable test

Compare `r25-to-ambiguous` with the proposed one-field-malformed duplicate-target copy. Confirm only the targeted required field differs on the added row; preserve the first valid target, relation row and `courier-log` source. Run the checker: malformed case must emit the precise required-field error, exit nonzero, and omit `relations[0].to: ambiguous entity 'seal'`; unchanged admitted r25 case must retain duplicate-ID plus endpoint ambiguity. This tests row admission/counting only. Separately replay the declared prior fixture stdout/stderr/exit and JSON-path byte baselines; no source-text or rights inference is part of the oracle.
