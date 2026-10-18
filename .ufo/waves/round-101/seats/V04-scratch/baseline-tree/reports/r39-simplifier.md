# Round 39 simplifier — unknown source on ledger claim_b

## Smallest fixture mutation

Use a clean control copied from `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/` and one separate negative copy. In the negative, change only the Sella timeline event's `source_id` from `sella-bell7-note` to the absent ID `missing-sella-note` (`timeline.json:32-39`, especially `:38`). Leave source rows, event ID `sella-bell7-presence`, Tarin's event, and the contradiction ledger unchanged. The ledger's `claim_b` already uniquely points at that Sella event and `place_id` (`contradictions.json:8-10`); the control has its unique source row (`sources.json:21-25`). No new words, source row, event, or checker behavior is needed.

The checker first resolves a uniquely identified ledger event and then classifies its source (`check_bible.py:77-100`). An unknown event source should produce the ledger-side `contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id` finding (`:95-99`) and a timeline-local unknown-source diagnostic (`:97-98` via the timeline source check); inventory complete output. The control should exit 0; negative should exit 1. This isolates unknown-source handling from r38's duplicate-source ambiguity experiment.

## Novelty and audit disposition

**This is already tested elsewhere.** The specific ledger unknown-source branch is not novel: r7's reviewer temporarily probed unknown `archive-ledger` on `claim_a` (`.shokunin/lore/reports/r7-reviewer.md`, ledger bullet); r7 executor/reviewer describe unknown ledger source resolution (`r7-executor.md`, `r7-reviewer.md`). The older malformed-ledger fixture tests an unknown *event ID*, not a missing source (`r6-independent-verifier.md`, malformed-ledger row). R38 explicitly recognized that its `claim_b` ambiguity candidate repeated r7's `claim_a` ambiguity branch and rejected coverage (`.shokunin/lore/LOG.md:621, 632-634`). Here, opposite ledger side and Bell-7 data improve durable repeatability only; they do not establish new checker-branch coverage. Recommend **no-go / reject as a coverage move** unless an adjudicator identifies a materially distinct coverage target. Do not build/claim novelty merely because the missing-source status differs from ambiguous status without confirming r7's temporary probe's exact status and output.

## Risks and falsifiable check

A missing citation means the checker cannot resolve the source ID; it does not make Sella's account false, invalidate the fictional excerpt, resolve the Bell-7 reports, or establish canon. Do not claim the checker reads or verifies source text. The mutation may produce both ledger-local and timeline-local diagnostics; report all output, not just the target line. If investigated despite the no-go recommendation: run the checker on the control and negative and require clean exit 0 versus exit 1 with the exact `claim_b` no-resolvable-source finding and timeline-local unknown-source finding, while event IDs and ledger pointers remain identical and the only JSON delta is `timeline.json[3].source_id`. Any different branch, missing target diagnostic, or additional unexplained finding falsifies the proposed check.

Scope: report only; no fixture, checker, LOG, README, or commit edits.
