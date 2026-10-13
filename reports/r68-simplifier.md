# Round 68 simplifier review

## Smallest safe change

If the round proceeds, add one early guard inside the string-member loop in `.shokunin/lore/corpus/fixtures/check_bible.py` (around lines 299–316): after the existing non-string skip and `dep_location` construction, detect `not dep.strip()`, append a field-local diagnostic such as `...depends_on[i]: required nonempty event id`, and `continue`. Do not send blank values to self/repeated/unknown/cardinality/tick-order checks. Leave the existing row-level non-string diagnostic and all nonempty-ID logic unchanged. This is narrower than changing the aggregate `all(isinstance(...))` condition, which could add a generic row-level message and leave downstream blank-ID findings unless the loop also changed.

The target branch is precise: `check_bible.py` currently checks only `isinstance(dep, str)` at lines 296 and 300; every string then enters set and event-index lookup. A blank string can consequently be labeled `unknown event ''` at line 311. In contrast, existing required-nonempty patterns use `.strip()` for claim IDs and other fields (see the claim validator and holder/source checks in the same file); the declaration's nonempty policy is consistent with that local convention.

## Scope and overlap

`.shokunin/lore/corpus/fixtures/README.md` Round 20 documents preservation of self/repeated/unknown/ambiguous and inversion checks, and Round 22 documents that string siblings continue through those checks while malformed non-strings are skipped. The proposed early branch preserves those behaviors for every nonempty string and does not alter malformed non-string handling. `r20-*` fixtures cover valid ordering/inversions and negative tick edges; `r22-self-repeated/` and `r22-unknown-mixed/` cover those string-ID findings alongside malformed members. They do not appear to contain blank/whitespace dependency IDs. A matched empty/whitespace/nonempty-unknown fixture trio would be needed to evidence the declared distinction; no fixtures or CLI runs were performed for this review.

## Limits / gate

This is a minimal implementation sketch, not a recommendation to admit the move by itself. A blank ID is structurally malformed; the proposed wording should describe the supplied field, not assert an event is absent or that any fictional chronology is true. Round 22's existing tests make regression coverage lean if the candidate is built, but prior overlap means the non-author materiality check remains important. I did not inspect historical r20/r22 raw runs or execute the checker, so I cannot establish unchanged outcomes, material user repair value, or collateral behavior. No source-text, canon, rights, or game-mechanics conclusion is warranted.
