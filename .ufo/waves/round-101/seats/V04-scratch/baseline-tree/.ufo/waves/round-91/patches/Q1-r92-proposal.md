# Conditional r92 proposal — Q1

Status: **conditional; not selected and not a verdict**. Do not start this claim until L1 records per-axis r91 verdicts on the frozen delivered tree.

## Selection gate

Use L1's actual verdict words, ordered by severity `harmed < unchanged < unprovable-but-better < improved`; assign one claim to the weakest axis. If axes tie, prefer the one with more open ledger rows. Do not infer an axis from candidate-patch count, report volume, or Q1's audit. If calibration is not the weakest axis under that rule, this proposal is not adopted and must not be relabeled as the selected claim.

## Single candidate claim, if calibration is weakest

**Q1-R92-C1 — Make the r90 repaired provenance rules regression-visible in the delivered corpus.**

Turn the currently scratch-tested r91 C1 candidate into durable, tracked evidence: integrate the two null-chain and unresolved-holder tick fixtures; integrate a C9 watch that pins the delivered checker hash and uses explicit prospective falsification/control paths (not generic placeholders); then verify both fixtures against the frozen baseline and delivered checker, including exact stdout, stderr, and exit status. Run the full fixture census after integration and demonstrate that the new fixtures change on the repaired checker while the shared baseline corpus stays stable. Reopen the C9 ruling only if a source-backed counterexample meets the watch's stated gates.

**Completion contract**

- Both fixture directories and the corrected watch are tracked in the delivered tree.
- For each fixture, baseline and delivered invocations are reproducible and preserve the README's complete expected output; the null-chain diagnostic is definite with `got None`, the integer tick inversion is definite, and the separate unresolved non-null chain-break remains qualified.
- The full census records command, checker hashes, all changed tuples/exits, and empty/nonempty stderr; no patch-only or scratch-only result counts as delivery.
- Close Q90-001 only after the delivered-tree evidence passes and a reviewer confirms the watch paths and falsification threshold.
- Keep source truth, story canon, and real-world chronology outside the claim; this is checker regression coverage only.

If L1 selects coverage or depth as the weakest axis, hold this candidate and write a new single-axis claim only after that verdict is recorded. No r92 axis or score is assigned here.
