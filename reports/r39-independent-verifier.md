# Round 39 independent verifier

## Baseline replay (commit `793a3a8863b9361ca89a514069f3a4c46f739ebd`)

Archived the baseline checker and complete fixture tree with `git archive` into a separate root, then enumerated its fixture directories and JSON paths. The baseline has **90 active fixture directories** and **449 JSON paths**. For every fixture, ran the identical root-relative argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` once from the working-tree root and once from the archived root. Raw stdout, raw stderr, and exit code matched exactly for **90/90** invocations. Compared each JSON path byte-for-byte between baseline archive and working tree: **449/449 identical**. No baseline mismatch.

## Independent controls

Against `r35-bell7-conflict`, the clean `r39-ledger-source-unique` control has the same nine files, each byte-identical; no added files. The negative has the same nine files and only `timeline.json` differs. Inspection confirms the sole semantic edit is `timeline[3].source_id`, from `sella-bell7-note` to `missing-sella-note`; the timeline event IDs remain unique (4/4), including `sella-bell7-presence`. The source table, excerpts, and contradiction ledger are unchanged.

Checker command was run with complete captured streams and status:

Control exit **0**; stdout (exact):
```text
CLEAN: schema, citations, relations, timeline; 0 violations
```
stderr: empty.

Negative exit **1**; stdout (exact):
```text
VIOLATION: contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id
VIOLATION: timeline[3].source_id: unknown in-world source 'missing-sella-note'
2 violation(s); no canon changed
```
stderr: empty.

These are exactly two findings: ledger claim_b's event has no resolvable source, and timeline index 3 has an unknown source. The referenced event ID itself remains unique. The missing ID has zero matching rows in `sources.json`.

## Prior-art limits and interpretation

The r38 independent report records a duplicate-source probe producing the **ambiguous** source path. `reports/r7-reviewer.md` describes the unknown-source branch, but its executed temporary probe duplicated a source and observed ambiguity; description is not evidence that the zero-source ledger case was executed. The round log likewise identifies no earlier executed, uniquely resolved ledger endpoint with zero matching source rows. This validates a narrow observed unknown-status case, not a new checker rule and not a claim that no private/unrecorded probe ever existed.

The source excerpt remains present: the unresolved event citation does not erase or disprove that prose, establish that Sella lied, authenticate either account, resolve the fictional conflict, or select canon. No finding establishes truth; this is structural fixture/checker evidence only.
