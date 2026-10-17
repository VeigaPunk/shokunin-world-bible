# PROPOSAL ONLY — Round 91 SCORECARD section (W2)

Do not append this draft to `SCORECARD.md` without integration and L1 review. All C1–C3 verdicts remain **PENDING-L1**; scores remain unassigned because no rubric exists. Baseline receipts and peer candidate artifacts are not a delivered/frozen after-state.

## Proposed section text for `SCORECARD.md`

### Round 91 — luna round 5 of 12 (2026-10-17)

Work wave declared as 32 seats on `openai-codex/gpt-6-luna-max`; follow-up is declared for `alibaba-token-plan/deepseek-v4.1-flash` with the persisted fallback chain. Spec: `.ufo/waves/round-91/wave-spec.md`; baseline: `a7c6a1773d5994246a76e4eff30d645f161920e0` (r90 closure). No work commit or L1 closure is asserted by this proposal. Scores remain unmeasured; each row is a claim with a bounded measurement requirement.

| LIVE axis | r91 verdict | Evidence and limit |
|---|---|---|
| calibration | **PENDING-L1** | W2's baseline census at `a7c6a17` is 164 fixture directories, exits `{0: 32, 1: 132}`, 417 violation lines, empty stderr; current checker SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. No `r91-c1-*` fixture directory or `corpus/knowledge/r91-c9-watch.md` existed at the baseline check. Required after-state is two durable fixtures whose stdout differs from the `e97613c` checker: later-record null-chain definite `got None`, and tick inversion under a genuinely unresolved compared holder definite while its chain-break remains qualified. The C9 watch must pin the shipped-checker hash and a concrete falsification probe. TODO: verify the delivered fixtures against both checker revisions, compare the full census tuples, and validate the watch on the frozen tree. |
| coverage | **PENDING-L1** | Baseline support receipts are r87 22/22 rows, r88-m3 10/10 rows, and paraphrase 0/0 source-support with one retelling-only anchor; all three commands exit 0. r87's 22 mapped rows are 14 JSON-fact rows plus 8 editorial hymn rows (two additional prose-crosswalk facts are disclosed separately, not extra rows). r88-m3 has 10 source-attributed JSON rows and two separate symbolism comparisons; four anchor occurrences repeat across the 10 fact rows. These are row receipts, not distinct-fact or distinct-anchor counts. TODO: verify map-declared versus parsed inventory, duplicate-row/distinct-anchor reporting, retelling-anchor-miss WARN, and the split JSON-facts/editorial/total receipt; run the M4 negative controls on the integrated command. |
| depth | **PENDING-L1** | The r90 R8/R9/R10 appendices exist at `corpus/knowledge/r88-sourced-inspiration-decision-table.md:28-59`, but JDEP2's three residuals remain the r91 claim: R8 failed-gate disposition plus element/detail withhold precedence; R9 later-reprint boundary plus a reliability criterion for the bibliographic tie; R10 `source_id` namespace scoping across clusters. No r91 decision has been measured by W2. TODO: verify each delivered decision names owner, trigger, worked example, and verification command; manually re-check cross-cluster source IDs and register disposition. An absent register file alone is not evidence of a correct empty register. |

Learning trends and axis verdicts are **not adjudicated** by this proposal. Preserve the capability table unless L1 adopts a demonstrated new capability; do not infer one from a patch or baseline receipt. Keep scores unassigned, saturation undeclared, and retirement unchanged. Planned r92 work remains TODO for Q1 and L1; do not select an axis by inference. No SHONEN promotion or checkmark is proposed.

### W2 baseline receipt commands (read-only; exact observed outputs are in `.ufo/waves/round-91/W2.md`)

- C1: `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ...` (full command and census result in W2.md). It measured only the baseline, not either new discriminator.
- C2: `PYTHONDONTWRITEBYTECODE=1 python3 corpus/tools/support_check.py corpus/fixtures/{r87-myth-cluster,r88-m3-maya-cluster,r89-inspiration-paraphrase}` was run as three explicit commands; exact per-case receipt lines and exits are in W2.md.
- C3: W2's inventory found the decision-table rows at lines 24–26 and `cross_cluster-contradictions.md` absent. This is path/row inventory only, not semantic cross-cluster verification.

All evidence and command/output pairs are retained in the phase-1 W2 report; this proposal intentionally does not copy a peer result into an L1 verdict.
