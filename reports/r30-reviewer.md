# Round 30 non-author reviewer

## Manual three-way classification

I reviewed the authored excerpts, maps, and selected relation row. The three labels are distinct and excerpt-relative:

| Fixture | Clause | Classification of `relations[0].type=carries` | Boundary |
|---|---|---|---|
| r28 | “I, Mira, carried the blue seal.” | **Conditional lexical support.** “Carried” expresses the predicate and the seal is its object. | Mapping speaker/object to IDs `mira`/`seal` is an editorial stipulation, not lexical entailment or external verification. This supports only the selected row. |
| r29 | “The blue seal was near Mira.” | **Unsupported by this clause**, not contradicted. Proximity neither says she carried it nor says she did not. | No closed-world inference; lack of support is not falsity. The map correctly limits the assessment to `relations[0]`. |
| r30 | “I, Mira, did not carry the blue seal.” | **Explicit textual conflict** with the positive `carries` row, conditional on editorial ID alignment and on reading both as about the same proposition/occasion. | This is not a canon ruling, a finding that the row is false, or a claim that Mira never carried the seal. The sentence's negation has its own scope; it does not establish a global or all-time negative. |

## Map and structural-boundary review

The r30 map is appropriately narrow: it names only `relations[0].type=carries`, states both alignment conditions, distinguishes r28 support and r29 unsupported proximity, and disclaims canon/global conclusions. Its “same-proposition/occasion” condition matters because the row has no occasion/time specification; without that match, the sentence and row need not conflict. It does not overstate this as universal non-occurrence. The r28 and r29 maps likewise avoid treating editorial identity matching as a lexical fact.

The executor report records all five JSON tables copied byte-identically from r28 and all three checker invocations exiting 0. This preserves the structured row rather than resolving the prose/record tension. The checker explicitly does not read Markdown: its clean exits establish structural/schema/reference acceptance only, not the manual clause classifications, identity alignment, textual conflict, truth, or canon. I make no independent claim here that prior regression baselines were replayed; that is outside this review's classification scope.

## Verdict

The proposed three-way calibration is sound as stated: r28 = conditional lexical support; r29 = unsupported, not false; r30 = explicit textual conflict only under editorial ID and same-proposition/occasion alignment, not canon falsity or “never carried.” No production files were changed. This review report is the only file I wrote.
