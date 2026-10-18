# Round 27 simplifier: minimal fixture move

## Minimal pair

Copy the five JSON tables from `corpus/fixtures/r25-to-unique/` into two new directories: a both-endpoints case and its target-only control. In the control, append one admitted entity row duplicating `seal` (reuse the exact second `seal` row from `r25-to-ambiguous/entities.json`); in the both-endpoints case, additionally append one admitted entity row duplicating `mira` (copy the original `mira` row, changing no fields). Leave `relations.json` (`mira` → `seal`) and all other tables identical between pair. This minimizes the semantic difference to one extra admitted duplicate-ID row while the control already exercises duplicated `to`.

Evidence: `corpus/fixtures/r25-to-ambiguous/entities.json:1-17` is the existing admitted `mira` row; `.../entities.json:37-45` is the admitted duplicate `seal` row; `corpus/fixtures/r25-to-ambiguous/relations.json:1-8` has the single `mira` → `seal` relation. `corpus/fixtures/check_bible.py:119-130` counts admitted entity IDs and independently loops over `from` and `to`, emitting endpoint-local ambiguity diagnostics. The prior unique fixture provides the five-table base (`corpus/fixtures/r25-to-unique/`).

## Proposed test

Run checker on both new directories. Both must fail with duplicate-ID findings for their respective duplicated identifiers. The target-only control must report `relations[0].to: ambiguous entity 'seal'` and no `relations[0].from` ambiguity; both-endpoints must report exactly one ambiguity for each endpoint (`from`=`mira`, `to`=`seal`). Compare all unchanged tables byte-for-byte and ensure only the intended added admitted row(s) differ. Replay the prior 76 fixtures and compare stdout, stderr, exit status and all 379 prior JSON paths to the declared baseline.

## Risks / boundaries

The extra `mira` row may trigger additional checker findings outside the relation endpoint loop (for example entity-level duplicate checks); capture them rather than weakening expectations, and keep the claim strictly to endpoint coverage. Reusing a row with claims may cause unrelated citation or claim diagnostics; if so, use a minimal schema-valid duplicate `mira` row with empty claims, documenting the exact delta. No output here asserts either relation endpoint is true, identifies which duplicate row is canonical, or infers any lore/relation truth; fixtures test checker behavior only.
