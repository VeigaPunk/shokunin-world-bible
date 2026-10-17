# Conditional r93 proposal — Q1 follow-up

**Status: conditional, unselected.** This is not an axis verdict, score, or authorization to start a particular r93 claim. Do not select anything below until L1 records actual r92 per-axis verdict words against the frozen delivered tree (`c4d4823`).

## Selection gate (lowest-axis rule)

Apply the established ordering to L1's r92 verdicts: **harmed < unchanged < unprovable-but-better < improved**. Select one claim on the single weakest axis; if axes tie, prefer the axis with more open ledger rows. Do not infer an axis from patch counts, report volume, or candidate artifacts.

## Conditional pre-computation at c4d4823 (not a verdict)

If L1's verdicts land as the follow-up evidence proposes (P2-verdicts.json proposes all three axes "improved (bounded)"), the ordering is a three-way tie at `improved` and the tie-break selects **depth**:

- **depth** open set: Q91-002 (partially repaired), Q91-004, Q91-009 carried (6 sub-rows), DEP-H1 (independent certification FAILs on gate (b) as delivered), Q92-001, Q92-002, Q92-004, Q92-008 — and it carries the only documented blocking certification defect on the calibration instruction surface.
- **coverage** open set: Q92-003 (tools README drift), Q92-005 / CAL-D5, Q91-003 partial.
- **calibration** open set: Q92-010 only.

If L1 rules any axis below `improved`, that axis is selected as-is by the rule; this pre-computation does not override L1. Do not cite this section as the selection.

## Selected-claim candidate (depth): instruction-surface closure to certification

**Title:** Repair the delivered boundary doc and decision-table residue to a passing certification, and close the patch-space command.

**Completion contract:**

1. Boundary-doc F1 repair (JDEP1's blocking items): remove or re-head the orphan bullet tail `:545-556` (one bullet head or one tail deletion — JDEP1 measures 14 of its 21 anchor sites as mismatching); fix the stale range at `:330` (`:198-203` → `:200-205`); delete the duplicated provenance-census tail `:591-596` and the stranded `` `## Round 89` section at `1b09f3f` `` rules fragment `:615-619`; scope or re-attribute `:83` (`The delivered checker (\`1b09f3f\`)`) to the delivered checker `ff9fd2aa`; add an accurate r92 provenance line to the doc header.
2. Decision table: dedupe the doubled label at `:40`; move the manual-gate / required-record / receipt-boundary block from `:42-48` to inside `### R9 appendix` (`:50+`) per E1; replace the appendix's old Worked example (`:79`); add E1's missing R8 worked example; append the R9 evidence-cell receipt-boundary line ("per-claim R9 manual-review record"; "is not that receipt").
3. Re-anchor the R9 verification command (`:91`) to the delivered section text so it fails if that section drifts (closes Q91-004); the command must not read `.ufo/waves/**` patch files.
4. Re-run certification on the repaired tree — JDEP1's gates (a) block replay, (b) anchor resolution, (c) structure, (d) C9 semantics — and commit a certification receipt whose certifying seat is not the editing seat. Acceptance: zero stale delivered-context anchors, zero orphan sites, 3/3 blocks and 14/14 cases byte-identical, single H1, no duplicated headings.
5. Every repaired block carries a before→after measurement with exact commands and observed output.

**Does not:** no checker edit (`ff9fd2aa` frozen), no canon or spec change, no ruling change, no source/chronology claims. Carried Q89 rows (007/015/016/019/031/041) and the coverage/calibration rows above are out of this claim's scope.

## One exploratory claim (≤1): anchor-certification harness with a named non-author reviewer path

**Claim:** automate JDEP1's gates as a runnable, fail-closed script (block replay by diffing each ```sh loop against its following ```text block; anchor resolution by parsing `check_bible.py:NNN` sites against AST/derived spans; structure counts; C9 semantics) and run it on the frozen tree. Keep the script under the wave directory, not `corpus/tools/`, so a wrong gate cannot create a second documentation drift.

**Why exploratory:** its value is unprovable until r93 — the effect (faster, repeatable certification) cannot be measured on the r92 tree. It must not be folded into the selected depth claim.

**Named non-author reviewer path:** the harness is authored by one seat; its receipt must be reproduced on the frozen tree by a **different, L1-named certifier seat** (precedent: the r92 T1 → JDEP1 certifier class; neither may be the harness author or the document editor). The author's own run is not the receipt. If L1 cannot name a non-author reviewer, the script stays unlanded and the claim remains unscored. Precedent: Q89-046 (probe/doc-parity automation) stays exploratory under this same rule.

## Not selected (recorded only)

Q2's process improvements (freeze gate as a landing receipt, poll-helper v2, numeric scratch policy) map to rows Q92-006/007/009; they are process work, not axis claims, and are not folded into the selected claim.

## Gate discipline

No candidate is selected before L1's r92 per-axis verdict words arrive. Unselected rows stay open; the existence of candidate patches or sibling verdict proposals does not close them.
