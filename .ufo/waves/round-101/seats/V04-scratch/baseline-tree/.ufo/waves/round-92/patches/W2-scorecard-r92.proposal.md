# PROPOSAL ONLY — Round 92 SCORECARD section (W2)

Do not append this draft to `SCORECARD.md` without integration and L1 review. C1–C3 remain **PENDING-L1**; no numeric scores, admission, or closure are proposed. The branch is at the r91 baseline, and candidate patches/peer receipts are not an integrated or frozen after-state.

## Proposed section text for `SCORECARD.md`

### Round 92 — luna round 6 of 12 (2026-10-17)

Work-wave spec: `.ufo/waves/round-92/wave-spec.md`; baseline `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`. The spec declares C1 depth, C2 coverage, and C3 calibration. No delivered work revision or L1 closure is asserted by this proposal. Scores remain unassigned; every row below is a claim with bounded evidence and an explicit verification gap.

| LIVE axis | r92 verdict | Evidence and limit |
|---|---|---|
| depth | **PENDING-L1** | The required source is `git show e97613c:corpus/knowledge/holder-assessment-boundary.md`, SHA-256 `a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2` (630 lines, one H1); the tracked boundary file at baseline HEAD instead hashes to `c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9` (549 lines, two H1). `current_equals_e97613c=False`, contrary to the r91 SCORECARD/LOG closure wording. D2's candidate patch passes `git apply --check` (290 insertions/160 deletions), but no candidate replay, content-anchor certification, or delivered document is verified. B3 supplies a certifier specification, not an implementation or pass receipt. E1 proposes an inseparable-element whole-element hold and a per-claim R9 manual review gate; neither is adopted or integrated. Its report arrived after the poll and records textual checks of 6/6 R8 and 10/10 R9 fields only; D1.md, D2.md, and T1.md remained absent from the final inventory. TODO: reconcile the baseline discrepancy, re-derive from the pinned contract using content anchors, run the certifier/replays on the frozen candidate, and review R8/R9 governance wording. |
| coverage | **PENDING-L1** | Delivered baseline: r88-m3 has 10 JSON rows + 0 editorial rows (10 total, 6 distinct anchors), warns that `source-excerpt.md` is unreferenced, and exits 0 with `RESULT PASS WITH WARNINGS`; missing inventory exits 2 without `RESULT FAIL`, while missing map exits 2 without `RESULT ERROR`. M1/M2's composed candidate replay reports 10 JSON + 2 editorial rows (12 total, 8 distinct anchors), no warning, `RESULT PASS`/exit 0; tested candidate failures report `RESULT FAIL`/exit 1 for missing inventory and validation failures, and `RESULT ERROR`/exit 2 for a missing map. These are scratch-applied candidate receipts, not the delivered tree. Patch hashes: M1 `74ecdcdcc175f726c1afa9676c5d027d990b2aeb429320f752acec703360fd9a`; M2 `5291b14ed323066f9e51db28dafc3cf3bce1b37e0107f02ad6bc9270a0e35ce9`. `corpus/tools/README.md` still labels the two contract deviations as live; K1's README patch is unapplied. TODO: verify the exact selected patch stack against the frozen checker/map, including all failure classes, and align the README only after that verification. |
| calibration | **PENDING-L1** | B1/B2 independently replay 166 fixture tuples with zero tuple mismatches; both receipts are byte-identical (SHA-256 `185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf`). The baseline C9 watch probes reproduce the pinned checker behavior. X1 reports a first re-check and four semantic probes with no alarm, but its dated check-log is only a patch; X2's repo-relative path note is a separate unapplied patch to the watch note. The separate fixtures README path-census note is not present in the artifact set at the poll cutoff. TODO: apply/reconcile the watch changes and README note on the authorized integrated tree, then verify the dated log, exact argv-sensitive fixture list, and frozen result. |

Axis verdicts and learning trends remain unadjudicated. Keep the capabilities table, saturation, retired axes, and `planned` state unchanged unless L1 adopts a verified change. No SHONEN promotion or checkmark is proposed.

### Evidence pointers

- Exact baseline commands and observed outputs: `.ufo/waves/round-92/W2.md`.
- C1 baseline/candidate limits: `.ufo/waves/round-92/B3.md`, `.ufo/waves/round-92/S1.md`, `.ufo/waves/round-92/patches/D2-boundary-doc.md`, and `.ufo/waves/round-92/patches/E1-edges.md` plus `.ufo/waves/round-92/E1.md`.
- C2 baseline and candidate receipts: `.ufo/waves/round-92/S2.md`, `M1.md`, `M2.md`, and `M4.md`; candidate receipts are not delivered-tree measurements.
- C3 census/watch receipts: `.ufo/waves/round-92/B1.md`, `B2.md`, `X1.md`, and `X2.md`.

No numeric score is assigned: the scorecard contract requires a re-derivable, committed measurement, and no integrated r92 revision has been measured here.
