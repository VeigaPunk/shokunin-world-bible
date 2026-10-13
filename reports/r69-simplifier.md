# Round 69 simplifier — narrow same-reference guard

## Recommendation

The smallest safe candidate is to gate only the existing same-reference check in `.shokunin/lore/corpus/fixtures/check_bible.py:139–143`. Keep both sides' current independent validation at `:112–138`; emit `claim_a and claim_b references must differ` only when both sides are dictionaries, each has a nonempty string `event_id`, each `field` is one of `place_id`, `tick`, or `depends_on`, and the two `(event_id, field)` pairs are equal. This is the declaration's structural-validity gate, not a timeline-existence gate: preserve same-reference behavior even when a well-formed ID is unresolved or the timeline cannot be assessed. Do not alter any other diagnostics or the schema.

Conceptually, compute `a_valid` and `b_valid` from the exact predicates already checked at `:121–125`, then require `a_valid and b_valid` in addition to the current equality predicate. Avoid revalidating the timeline or coupling this ledger-shape check to event lookup. No checker or fixture change is made in this report.

## Evidence and expected delta

`check_bible.py:121–125` independently reports invalid/missing event IDs and invalid fields. The unconditional equality branch at `:139–143` nevertheless compares raw `.get()` values, so two missing IDs/fields (or two equal invalid fields) can add a same-reference finding without a usable reference pair.

The concrete old-output case is `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json`: both sides name `tarin-envelope-observation` but both fields are `bogus`; its `timeline.json` is malformed. Running `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r62-malformed-side` currently emits the timeline JSON load error, one invalid-field finding per side, and `contradictions[0]: claim_a and claim_b references must differ` (four total; exit 1). Under the proposed gate, the first three remain and only the unsupported same-reference finding disappears (three; still exit 1). The fixture name notwithstanding, this candidate concerns the two invalid ledger fields, not a conclusion about timeline content.

A read-only scan of all current fixture `contradictions.json` files found exactly one pair with equal raw references where at least one side fails the proposed validity predicate: the `r62-malformed-side` row above (both sides invalid). This scan is repository-state evidence, not a complete historical baseline replay. Valid identical references must continue to trigger the existing finding; valid different references must not. Malformed-one/malformed-both and missing/non-string ID controls should retain each applicable side-local error and omit only this pairwise finding. There is no observed output for those additional controls in this leaf.

## Risks and review needs

- The known old fixture output changes. Any compatibility claim that all 130 prior fixture raw tuples remain identical would be false if this fixture is among that set; pin and replay the declared baseline and explicitly review the changed expected case rather than treating the change as incidental. The existing `.shokunin/lore/reports/r62-executor.md` and `r62-independent-verifier.md` document an earlier 115-fixture baseline and their old-output preservation; they do not validate this r69 candidate or establish the current 130-fixture inventory.
- Suppressing the pairwise line removes a potentially useful indication of duplicate ledger intent, even when its field is malformed. The two local field errors still identify repair sites, but a reviewer should decide whether the additional line has independently useful repair value. If so, reject the calibration claim rather than retaining a pairwise assertion for invalid references without justification.
- Preserve the existing predicate's scope: structurally valid matching IDs/fields, whether or not they resolve to exactly one timeline event. Narrowing it to resolvable events would change unrelated behavior and exceed the declaration.
- The fixture scan does not establish that every declared control exists, prove that a candidate is materially better, or rule out changes outside fixtures. A candidate would require matched malformed-both, malformed-one, valid-identical and valid-different cases, plus a pinned raw-output replay and non-author review.

This is an input-ledger diagnostic-calibration proposal only. No inference about story contradictions, authored source text, event occurrence, chronology, truth, canon, rights, or game mechanics follows. Evidence is limited to checker code, fixture JSON, and reported CLI output.
