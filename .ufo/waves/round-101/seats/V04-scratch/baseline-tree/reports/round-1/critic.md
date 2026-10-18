# Fleet round 1 — critic: disclosure, not recovered assessment

## Scope and evidence status

This is a lane-internal, read-only static review of the proposed single **calibration** move. Owned axes are **depth, coverage, calibration**; all three inherited scores are unmeasured (`SCORECARD.md:3-10,16-34`). I ran no checker, runtime probe, test, build, formatter, or judgment runtime and changed no code or fixture. The observations below cite existing evidence; proposed counterexamples are explicitly static inferences. Conditional recommendations are not an admission or the canonical judge's verdict. This review supplies no outside-verifier, SHONEN, or external-discernment evidence.

## Strongest counterargument: r56 may still win on materiality

The strongest objection is not that the new messages are inaccurate. It is that they do not change the necessary repair, recover any assessment, or improve a consumer who already rechecks after every edit. r56 explicitly rejected two accurate holder-local ambiguity lines: the global duplicate was already reported, comparisons were already withheld, and field-path navigability did not demonstrate a changed decision (`reports/r56-axis-adjudicator.md:21-41`). Repeating that result with more violations would not establish this round's claim.

r85 bounds rather than eliminates this objection. Its sealed reviewer chose the same correct first physical action—resolve the duplicate—under both information states. The mistaken decision was to stop after that repair, believing the file had exactly one defect. The reviewer explicitly says iterative rechecking neutralizes this danger (`reports/round-85/r85-sealed-reviewer.md:25-36,66-96`). The prior adjudication accepted a **discovery**, not a repair, and explicitly reserved a built candidate and regression replay for a later round (`reports/round-85/r85-axis-adjudicator.md:138-173`). Do not count that discovery twice as a new gain merely because local diagnostics now exist.

The narrow, defensible incremental value is an executable disclosure of the assessment boundary: **resolve the duplicate, then rerun before deciding that continuity or tick order is clean**. This changes what a first-pass consumer is entitled to conclude, even when the first edit stays identical. A marker that names the affected record, both suppressed comparisons, and the permanent downstream scope provides information that field-local navigation alone did not. It can improve that real stopping/acceptance decision; it does not establish that a new reader has actually changed behavior. No candidate-reader experiment has been observed in this review.

A consumer who already assumes every failed run is incomplete and always reruns gets little incremental operational benefit. That is a genuine limit, not a reason to claim a different improvement. If parent evidence supports only added field paths, or describes the benefit as discovering a break in an ambiguous chain, recommend rejection of the claimed calibration gain on r56's original grounds.

## What the matched pair establishes—and does not

At baseline `5eb9451baff217c19d5786405f9b2aa500b7c1b7`, the parent's recorded CLI outputs are:

- clean unique control: exit 0, CLEAN;
- unique-holder break: exit 1, a record-2 continuity finding;
- masked ambiguous and isolated ambiguous: exit 1, only the global duplicate `vault` finding;
- r56 harbor reproduction: exit 1, global duplicate plus timeline-place ambiguity.

All five recorded stderr values are empty (`reports/round-1/baseline-probes.json:2-10`). These are supplied observations, not runs by this critic.

The masked and unique probes carry the same transfers: `(null → mira, 0)`, `(mira → vault, 3)`, `(harbor → tower, 4)`; the masked probe adds a second `vault` entity (`corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous/entities.json:49-93`; `corpus/live/runs/round-85/probe-inputs/r85-unique-break-control/entities.json:49-81`). The prior author and adjudicator distinguish the isolated consumer from r56's collateral timeline case (`reports/round-85/r85-author.md:38-75`; `reports/round-85/r85-axis-adjudicator.md:57-68,124-136`).

Static mechanism: duplicate counts are collected at `corpus/fixtures/check_bible.py:157-159`; ambiguous holders silently invalidate records at `:212-224`; invalidity permanently clears the chain gate at `:234-237`; **both** tick ordering and continuity are inside that gate at `:238-245`. A later valid record updates local previous values but does not re-enable the gate (`:246-247`).

The unique control proves a structural discontinuity is reportable **under unique resolution**. It is not authority to select either duplicate, repair a fictional transfer, or announce a definite break in the ambiguous input. The correct new result is “unassessed,” not “broken,” “clean,” or “will become broken after repair.” Resolving duplication could involve changing references or records, not necessarily deleting the appended row. In-world citations establish neither source-text support nor custody, identity, canon, rights, or mechanics (`corpus/fixtures/README.md:110-119`).

## Actionable falsifiers and smallest safe corrections

These are static adversarial cases for the parent's integrated measurement/regression work, not additional runs performed here.

| Counterexample / falsifier | Evidence and impacted axes | Smallest safe correction |
|---|---|---|
| **Only local holder errors are added.** A consumer sees more defects but still cannot tell whether later continuity/ticks were assessed. | r56 `:31-41`; r85 sealed reviewer `:76-96`. Calibration gain remains unestablished; no depth/coverage gain. | Add one record-located notice per affected item explicitly covering continuity **and tick-order comparison at that record and all later records**. Do not claim detection of the masked break. |
| **Ambiguity is at record 1, records 2 and 3 are unique, and record 3 has a mismatch or reversed tick.** A “resume after one good record” implementation emits a later definite comparison. | [INFERENCE] Baseline gate never restarts (`check_bible.py:234-247`). Calibration harmed by invented assessment; compatibility broken. | Preserve the permanent latch; add disclosure without changing the comparison state machine. Keep unrelated record validation active. |
| **An earlier malformed/dangling record has already disabled the latch before the first ambiguous holder.** A notice guarded solely by `can_check_chain` disappears; wording that says ambiguity is where assessment first stopped is also false. | [INFERENCE] Earlier stops exist at `check_bible.py:187-197,203-237`. Calibration harmed by absent or false scope disclosure. | Track “ambiguity notice emitted for this item” separately from chain eligibility. Locate it at the first ambiguous holder record, saying that comparisons there and later are unassessed, without falsely dating the original stop. Do not broaden this move into new notices for every old invalidity class. |
| **Both holder fields are ambiguous in one record, or ambiguity repeats later; a second item is also affected.** Two notices for one item create noise, while a global notice flag suppresses the second item's notice. | [INFERENCE] Both fields are independently checked inside the per-item loop (`check_bible.py:171-185,212-224`). Calibration may be harmed; output count is not an improvement. | Emit both field-local errors as applicable, but reset the single-notice flag per item. Keep the global duplicate and independent timeline/relation/source diagnostics. |
| **The marker says only “chain unassessed,” or a probe passes on that phrase alone.** Tick-order suppression, exact starting record, or the downstream extent can remain undisclosed. A terminal ambiguity cannot demonstrate permanent downstream suppression. | Gate covers both comparisons (`check_bible.py:238-245`); baseline r85 has no reversed downstream tick (`masked…/entities.json:57-66`). Calibration claim exceeds evidence. | Require explicit comparison scope and a later record in each ambiguity-direction gate. Parent safety evidence must also support preservation of tick suppression; five passing gate names alone are insufficient. |
| **A generic invalidity/source message replaces holder-local errors, or a dangling holder gets mislabeled ambiguous.** Missing and duplicate identities are different states. | Existing zero-count diagnostics are explicit (`check_bible.py:212-224`); source handling has separate semantics (`:225-233`). Calibration regresses. | Retain existing missing-holder errors and source behavior, add only the two duplicate-reference diagnostics and the bounded notice. Do not merge identity authorities or choose a duplicate via the index. |

A false assessment, latch restart, lost independent finding, or changed old fixture output is a fixable implementation defect: correct it within the single move before asking for adjudication. If preserving an invariant is instead presented as a tradeoff against a higher sample score, the canonical judge must reject that trade under the assignment; averaging the gain against harm is not a correction.

## Five-gate 6 → 10: permissible only as a bounded sample measurement

Use one frozen rubric on both revisions, with `score = 2 × passed`, `total = 5`:

1. clean unique chain;
2. real unique-holder break;
3. missing-holder explicitness;
4. ambiguous-to local error **and** explicit downstream unassessed scope, with no definite break;
5. the same invariant for ambiguous-from.

**6/10 → 10/10 is not yet a measurement in this review.** Baseline CLI evidence directly supports the first two behaviors and the masked-to reporting gap; static code supports existing dangling errors and symmetric silent branches. It does not supply executions of this exact five-gate rubric, particularly the missing-holder and ambiguous-from gates (`baseline-probes.json:5-10`; r85 sealed reviewer `:102-103`). Parent must obtain both scores from the same measurement artifact rather than relabel the old five r85 probe outputs as these five gates.

The stable interface is `python3 corpus/fixtures/measure_holder_calibration.py --revision <git-commit>` (optional worktree default). Parent evidence must retain `measured_revision`, all gate results, and raw CLI stdout/exit/stderr. The selected revision must supply **checker and input data**, with temporary mutations isolated outside the tree. A fixed probe implementation may test both revisions; revision labels must describe the inputs actually tested. Do not silently run a worktree checker or worktree fixtures while naming an old commit.

This is a deliberately targeted, equally weighted regression sample designed around the proposed fix. The two new success gates are correlated directions of the same mechanism, not independent estimates of domain-wide calibration. It has no random sampling, population denominator, confidence interval, lore-truth assessment, or external consumer study. A 10 means only **5/5 specified behavioral gates passed**. It neither retires calibration nor establishes saturation, promotion, full branch coverage, or freedom from the counterexamples above. The measurement's `passed`/score is not an admission or closure gate; old-fixture preservation remains separate.

## Conditional recommendations to the parent and canonical judge

Recommend acceptance consideration **only if** parent smoke evidence shows the exact bounded delta on both holder directions, explicit first-ambiguous-record/downstream scope for both comparisons, one notice per affected item, no definite break inferred from ambiguity, unchanged permanent latch and independent diagnostics, unchanged clean/unique-break behavior, all inherited raw CLI triples preserved, and every old fixture JSON byte preserved. Failures must be reported, not hidden by weakening expectations or reclassifying unexpected output as intended. Reject the claimed gain if only local navigability is demonstrated, or if passing the sample is used to override any harmed axis.

| Axis / trend | Conditional recommendation, not a verdict |
|---|---|
| **Calibration** | **Improved, bounded** only with the above evidence: output now discloses an existing assessment gap. Otherwise unchanged/unproven; misleading scope or altered identity semantics is harmed. |
| **Depth** | **Unchanged** if source/lore interpretation and established checker decisions remain untouched. More report lines are not technical-domain depth. |
| **Coverage** | **Unchanged** if this remains disclosure of the existing guarded surface. Testing both directions closes a measurement omission, not the domain's coverage denominator. |
| **Expansion** | **Unchanged** absent new admitted, previously uncovered domain knowledge. Probe/report count is not expansion. |
| **Quality** | **Unchanged** absent the required evidence of stronger/reverified admitted knowledge. A safer diagnostic alone does not prove the learning-trend criterion. Preservation failures must not be waved away as improvement. |
| **Discernment** | **Unproven by this round's internal review**; do not record improved. A dispatched critic is still lane-internal and supplies no outside admit-and-reject spot-check. See canonical `LEARNING.md:28-43`. |

Retain legacy **depth and coverage as unmeasured**, with their historical evidence pointers and reasons; do not assign zero, copy calibration's 6/10, invent retrospective numeric improvement, or rank them numerically against the sample. Keep calibration's inherited whole-axis score unmeasured too, while recording the new **holder-disclosure five-gate sample** in a distinctly labeled metric/column with command and measured revisions. If a numerical schema needs future depth/coverage values, define and run separate justified rubrics first. The unresolved tie and calibration falsifiability tie-break are already honestly documented (`SCORECARD.md:16-34`). No new retirement or domain-mastery claim follows from this repair.

**Smallest safe move:** voice both ambiguous references and one precise per-item assessment-boundary notice; preserve existing assessment behavior and fictional bytes; report measured sample performance separately from unmeasured expertise. The gain is a better statement of what the checker did not assess—not a newly discovered unassessable break.
