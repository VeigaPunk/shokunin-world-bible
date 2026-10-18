# PROPOSAL ONLY — Round 93 SCORECARD section (W2)

Do not append this draft to `SCORECARD.md` without integration and L1 review. C1–C3 remain **PENDING-L1**; no numeric scores, admission, or closure are proposed. The tracked tree remains at the r92 baseline; peer patches and scratch/in-memory receipts are not an integrated or frozen after-state.

## Proposed section text for `SCORECARD.md`

### Round 93 — luna round 7 of 12 (2026-10-17)

Work-wave spec: `.ufo/waves/round-93/wave-spec.md`; baseline `87779a00f25bd1855ede479e490123843e5f056e`. The spec declares C1 depth, C2 coverage, and C3 calibration. No delivered work revision or L1 closure is asserted by this proposal. Scores remain unassigned; each row is a claim with bounded evidence and an explicit verification gap.

| LIVE axis | r93 verdict | Evidence and limit |
|---|---|---|
| depth | **PENDING-L1** | The current boundary document (SHA-256 `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`, 648 lines) differs from `git show e97613c:corpus/knowledge/holder-assessment-boundary.md` (SHA-256 `a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2`, 630 lines). D1's R9/R8 venue patch applies cleanly and candidate structural checks pass; D2's illustrative R8 dossier has eight record fields, while its embedded replay asserts only five. CERT's patch candidate replays 14 checker cases and prints `CERTIFIED`, but CB-audit shows it also certifies a contradictory document and changed checker; it lacks B3's checker hash pin, content/AST anchor validation, and C9 contradiction gate. All C1 artifacts remain candidate-only. Reconcile the baseline, repair CERT to B3, integrate and verify the frozen table/dossier/tool, and review the named adjacent debt before any closure claim. |
| coverage | **PENDING-L1** | Baseline receipts: r87 14 JSON + 8 editorial / 22 rows / `RESULT PASS`; r88-m3 10 JSON + 2 editorial / 12 rows / `RESULT PASS`; paraphrase fixture 1 row, `SOURCE-SUPPORT 0/0`, one retelling-only entry / `RESULT PASS`. M1's Kojiki and M3's Ovid patches each report candidate scratch support passes and author-side normalized-key non-intersections. Neither is landed, and M6's independent semantic review, M4's combined receipt, C7b's discipline review, and M2/M5 convergence were absent at poll cutoff. TODO: select one family, integrate and replay it on the frozen tree, obtain the independent zero-referent and three-question reviews, and preserve separate attribution, rights, and AI-training answers. |
| calibration | **PENDING-L1** | Baseline C9 watch has one dated row; checker SHA-256 is `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. X1 reports a second four-scenario check; its unapplied row patch repeats the existing date/hash/result. X2's candidate tool returns `DISCRIMINATION HELD` / exit 0 and pre-fix simulation `REGRESSION-DETECTED` / exit 2 in scratch. C5 found an out-of-pair checker mutation detected by its hash pin and named a concurrency/input-pinning limit. The tool and watch update are not integrated; E3 is ordered after X1/X2. TODO: apply the authorized ordered stack and rerun the installed tool plus dated watch checks on the frozen tree. |

Axis verdicts and learning trends remain unadjudicated. Keep the capabilities table, saturation, retired axes, and `planned` state unchanged unless L1 adopts a verified change. No SHONEN promotion or checkmark is proposed.

### Evidence pointers

- Exact baseline commands, poll terminal inventory, and named evidence limits: `.ufo/waves/round-93/W2.md`.
- C1 candidates: `D1.md`, `D2.md`, `T1.md`, `CERT.md`, and `CB-audit.md`; patches remain unapplied.
- C2 candidates and family scout: `S2.md`, `M1.md`, and `M3.md`; no M6 independent review was available at cutoff.
- C3 evidence: `X1.md`, `X2.md`, `C5.md`, and `E3.md`; the lane tool/watch row remain unapplied.

No numeric score is assigned: the scorecard contract requires a re-derivable committed measurement, and no integrated r93 revision has been measured here.
