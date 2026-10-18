# Round 90 fleet report skeleton (W2)

This is a scaffold, not a report or verdict. Fill it from the frozen delivered tree after independent replay. Retain the required heading order exactly. Every measurement must include the exact command, exit status, and observed output; distinguish inherited evidence, W2 baseline, peer scratch results, and delivered/frozen results.

## Work performed

- Axes: scribe completeness; measurement traceability; write-boundary compliance.
- State the persisted wave baseline and the final measured/frozen revision. Name the scratch archive/worktree under `/tmp` or report the exact reason it could not be created. State all paths written by W2; do not claim W2 integrated code or documents.
- Record the 60-second poll's first and final timestamps, every check timestamp, terminal seat-report inventory, terminal patch inventory, and whether the full 20-minute deadline was reached. An absent report at a check is not a seat failure. Include the exact poll command and output.
- List the actual C1/C2/C3 reports and artifacts read. Separate missing artifacts from reports inspected; do not infer a result from a filename.

## Before → after measurements

- **C1 CALIBRATION — PENDING-L1.** Give the exact baseline census command/output and the delivered-tree command/output. Compare the full prior 160 tuples; enumerate each added, removed, and changed tuple with stdout/finding-count and exit changes. Verify 0 exit changes. Replay FN-1 raw-present/schema-invalid `to_holder`, `from_holder`, and `source_id`; the ≥3-cause valid-key record; both FN-2 pair members and controls; and the canonical census entry. Do not reuse the inherited 160 count as an after-state.
- **C2 COVERAGE — PENDING-L1.** Show every r87 fact in its in-corpus claim→excerpt map (22 total), including path, line span, exact anchor, and R9 delivery mode; separately enumerate the four r89 excerpt labels and hymn mode. Show every r88-m3 source-attributed fact and mode. Give the single committed support command, its exit, exact `N/N` output, and a demonstrated rejection of paraphrase/summary-only source support. Separate lexical anchor hits from whole-claim prose review and checker `CLEAN` output.
- **C3 DEPTH — PENDING-L1.** For each R8/R9/R10 sub-case, quote the governed decision and identify the owner, trigger, and worked example: general motif with plausible but unrecorded influence; named translator with unknown translation version; same referent name across different occasions. Include exact verification commands/output for the rows and worked examples. Re-verify the clusters' shared-referent/occasion inventory and the register's correct empty state; an absent register file is not sufficient evidence.
- **Integrated measurements — [full revision].** For every receipt, identify baseline, candidate-only, or delivered/frozen provenance. Re-run checks after any integration amendment. If unavailable, write `NOT MEASURED` and name the missing artifact; do not estimate.

## Findings & named debt

- **C1 calibration — PENDING-L1:** [exact replay/delta evidence; both hedge repairs; FN-1 raw-present pins; ≥3-cause fixture; FN-2 census registration; limits/debt].
- **C2 coverage — PENDING-L1:** [r87 22-fact map; four excerpt labels + hymn; r88-m3 map; reproducible command and R9 rejection; limits/debt].
- **C3 depth — PENDING-L1:** [three governed sub-cases, owner/trigger/example each; correct empty-register verification; limits/debt].
- **Round/process debt:** [missing reports/artifacts, poll gaps, inode/scratch limitation if still applicable, post-freeze re-verification]. Do not claim closure, admission, or scores before L1.

## Handoff

- Baseline: `e97613cc276f5fa9cac49ff1900798cf6863c020`; delivered/frozen revision: [full SHA or unavailable].
- `/tmp` archive/worktree: [path or exact blocker].
- Integrated claim artifacts and delivered status: [paths].
- Exact replay receipts and reports reviewed: [paths].
- Remaining TODOs and named debt: [items].
- L1 decisions: [PENDING-L1 until authorized verdict; do not fill by inference].
