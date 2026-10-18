# Round 3 scribe — proposed README / decision-table boundary wording

## Evidence observed (not recommendations)

- `.shokunin/lore/corpus/fixtures/README.md` already says contradictions are evidence for editorial review, not permission for the checker to choose a canon answer, and that the checker modifies no files.
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md` bounds round 2's `allied_with` rule as a local invented-world convention, and says reciprocal records are sourced assertions, not editorial resolutions.
- `.shokunin/lore/corpus/fixtures/contradictions/timeline.json` contains the `arrival` / `false-sighting` disagreement and a dependency inversion. Its rows cite `courier-log` or `archive-ledger`; `.shokunin/lore/corpus/fixtures/contradictions/relations.json` also contains a dangling endpoint. These are concrete fixture records, not proof that source accounts are true.
- At inspection, those contradiction fixture files did not contain an explicit `claim_a` / `claim_b` / `why` ledger. The checker observed at `.shokunin/lore/corpus/fixtures/check_bible.py` had no ledger validation. This is a snapshot; do not treat it as evidence about later implementation.

## Suggested README boundary text (recommendation)

> An explicit contradiction-ledger entry is an editorial pointer between two cited claims, with a short explanation of the conflict. It records that both claims are retained for review; it does not establish either claim as true, prove that the cited sources are reliable, or select a winner. The checker may validate that each reference resolves and that `why` is nonempty, but it does not interpret the claims or rewrite the bible. A ledger entry is not a substitute for the ordinary schema and citation checks on the underlying records.

## Suggested decision-table rows (recommendation)

| Input condition | Decision / output | Boundary |
|---|---|---|
| Ledger entry has two claim references that resolve and a nonempty `why` | Accept the ledger entry; preserve both referenced claims | Structural acceptance only; not semantic proof, source adjudication, or canon resolution |
| Either claim reference does not resolve, or `why` is empty/missing | Report a ledger-local violation; do not discard or rewrite either claim | Ledger error does not decide which underlying claim is correct |
| Ledger entry is absent | Apply the existing schema, citation, and consistency checks normally | Absence is not evidence that no contradiction exists; do not claim the ledger is exhaustive |
| A ledger entry points to claims that appear inconsistent | Retain both claims and report any ordinary checker violations independently | The ledger does not replace nor suppress the original diagnostics |

Tie the table to the actual chosen reference syntax and paths only after implementation is stable. Avoid language implying references establish the disagreement automatically: they identify records for human review. Avoid claiming every contradiction is captured or that a clean result means the fictional canon is true. Keep this distinct from the real-world inspiration ledger and its attribution/rights/AI-training questions.
