# Fleet round 1 — current critic: disclose the boundary, do not recover it

## Scope, axes, and evidence status

Assigned review only; no admission, canonical judgment, implementation, or integration. Owned axes are **depth, coverage, calibration**. All remain historically **unmeasured**, so calibration is the declared most-falsifiable unresolved tie, not a numeric minimum (`SCORECARD.md:3-10,16-34`; fleet `../AXES.md:9-16`). This review owns only this report.

I statically read the shared assignment, fleet mission/axes, scorecard, inherited `reports/round-1/critic.md`, r56 adjudication, r85 sealed review/adjudication, current checker, provenance documentation, masked input, and parent-recorded baseline. **No checker, measurement, test, build, linter, formatter, other runtime probe, or judgment runtime was invoked.** I did not inspect a completed candidate implementation; recommendations below are behavioral falsifiers, not claims that candidate behavior passed or failed.

The inherited critic and declaration edits predate this review. Their existence is not evidence of a dispatch performed here. This report neither overwrites them nor adopts their stale measurement filename: the assigned entry point is **`python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>`**, with optional current-worktree mode. Inherited `critic.md:61` names a different script and is historical, not interface authority. The current assignment controls the interface.

## Strongest objection: r85 already taught the lesson

The adverse case against incremental calibration is substantial:

- r56 rejected accurate holder-local ambiguity messages because they changed neither the repair nor the guarded comparison, and supplied no material consumer decision improvement (`reports/r56-axis-adjudicator.md:21-41`). Extra lines alone do not establish gain.
- r85 already admitted discovery of permanent silent suppression. Its sealed reviewer chose the same first edit before and after unsealing; the wrong inference was the stopping decision, “one defect total, clean after dedup.” Mandatory rerunning neutralizes that danger (`reports/round-85/r85-sealed-reviewer.md:25-36,66-96`). The adjudicator explicitly separated admitted discovery from a future built repair (`reports/round-85/r85-axis-adjudicator.md:138-173`).
- A reader who has absorbed r85, or always regards failed runs as incomplete and reruns after every repair, need not change any decision on seeing the proposed notice. This round supplies no newly observed candidate-reader comparison. Do not report a newly demonstrated changed operator action, an independently repeated seal, or a second discovery.

**Narrow incremental claim that survives this objection:** move an established limitation from historical reports into the actual checker output at its consuming record. The global duplicate says which identity is not unique; it does not state that *both continuity and tick-order comparisons* are unassessed there and throughout the remaining item records. A precise notice makes the ordinary output's assessment boundary explicit without requiring r85's oral/report context. The supported improvement is truthful runtime disclosure, conditional on parent observation—not restored assessment, a newly detected hidden break, or demonstrated human behavior change.

That distinction is falsifiable. If the delivered output adds only field locations, or parent treats r85's old reader mistake as a new candidate-reader result, r56's materiality objection remains unanswered. Recommend rejecting that broader claim rather than crediting the discovery twice.

## Local evidence separating fact from inference

**Parent-recorded observations, not executions by this critic:** `reports/round-1/current-baseline.json:2-9` names baseline `5eb9451baff217c19d5786405f9b2aa500b7c1b7`. Clean control exits 0; unique break exits 1 with a record-2 continuity finding; masked and isolated ambiguity each exit 1 with only the global duplicate `vault`; harbor reproduction retains its independent timeline-place ambiguity. Recorded stderr is empty for all five. These five r85 outputs are **not** executions of the newly specified five measurement gates.

**Direct static evidence:** `corpus/fixtures/check_bible.py:181-247` initializes per-item comparison state, silently invalidates both ambiguous holder directions, permanently clears `can_check_chain` on invalidity, and places both continuity and tick comparisons behind that flag. Later valid records update previous values but never restore eligibility. Earlier malformed records can already disable the flag (`:187-197`), as can a negative tick (`:203-205,234-237`). Thus disclosure state cannot safely be equated with comparison eligibility.

The archived masked chain is `(null -> mira, 0)`, `(mira -> vault, 3)`, `(harbor -> tower, 4)`, with two `vault` rows (`corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous/entities.json:49-93`). It has **no later reversed-tick suffix**, so replaying that pair alone cannot establish tick-order suppression or catch a restart after one intervening valid record. r85 expressly did not exercise ambiguous-from (`r85-sealed-reviewer.md:102-103`).

## Strongest implementation counterexample for the parent

**[INFERENCE; proposed isolated temporary mutation, not executed.]** Start with that masked input, retain duplicate `vault`, and make this item's records:

| record | tick | from_holder | to_holder | source_id |
|---|---:|---|---|---|
| 0 | -1 | null | mira | courier-log |
| 1 | 3 | mira | vault | archive-ledger |
| 2 | 4 | harbor | tower | archive-ledger |
| 3 | 2 | mira | harbor | archive-ledger |

This combines two plausible implementation failures in one minimal chain:

1. Record 0 already stops comparisons. If the notice is emitted only while `can_check_chain` is true, the first actual holder ambiguity at record 1 receives no scope disclosure. If wording instead says “comparisons first stopped here,” it falsely attributes the initial stop to record 1.
2. Records 2 and 3 are individually valid and uniquely resolved. A mistaken restart after one good record makes record 3 emit *both* reversed-tick and continuity findings. A shorter ambiguity-followed-by-one-valid-record case may miss that restart because previous state was reset.

Required outcome: preserve record 0's existing tick diagnostic and the global duplicate; add the record-1 `.to_holder: ambiguous entity 'vault'` diagnostic and **exactly one** notice at record 1; emit no definite continuity or tick-order comparison at record 1 or any later record. The notice says unassessed **at this and all later records**, not that ambiguity was necessarily the first cause of suppression. Repeat the same suffix with a first ambiguous **from_holder** and otherwise unique to_holder. Parent must evaluate both directions without changing existing fictional JSON bytes.

This is an implementation falsifier, not a second domain move. It targets the promised disclosure and preserved state machine only.

## Additional parent falsifiers and smallest safe corrections

All rows below are **static adversarial recommendations, unrun here**.

| Falsifier | Impacted axes / evidence | Smallest safe correction |
|---|---|---|
| Both holder fields in one record reference duplicated IDs; ambiguity recurs in later records; a second affected item follows. | Calibration: missed local finding, repeated notice, or missing second-item notice. Both fields are separate branches inside the per-item loop (`check_bible.py:171-224`). | Emit each applicable field-local message; use one ambiguity-notice flag per item, independent of chain eligibility. First ambiguous record gets one notice even if both fields are ambiguous; later local findings remain. |
| Notice omits tick order, names only the current record, is attached to the global duplicate rather than its consumer, or is emitted on every ambiguous record. | Calibration: understated scope or misleading duplicate counts. Both comparisons are gated (`:238-245`); r56 rejected output-count-as-value. | Use the assigned exact record-local notice once per affected item: `{record_label}: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous`. |
| A local error is emitted but record is no longer invalid; a duplicate is chosen via an entity index; a later good record resumes comparisons. | Calibration harm through invented certainty; established checker decisions change. Existing latch and invalidation at `:215-247`. | Add messages without changing validity, the permanent latch, previous-state transitions, or identity resolution. Do not infer a break from the unique-holder control. |
| Independent source, holder-type, missing-holder, or timeline diagnostics disappear because disclosure uses an early return or generic invalidity refactor. | Calibration regression; preservation is not optional. Existing dangling messages at `:212-224`; source checking at `:225-233`; baseline harbor reproduction retains timeline ambiguity. | Keep existing branches and diagnostics; add only the two ambiguity messages and one notice. No generic invalidity redesign. |
| A measurement accepts any occurrence of “unassessed,” or omits a second valid suffix record, or tests only that no `chain break` appears. | Calibration: a false 5/5 can hide wrong location, repeated notice, omitted tick suppression, or resumed checks. The r85 pair alone cannot distinguish these. | Require exact field paths, exact notice/location/count, preserved global error, exit/stderr, and absence of both kinds of definite downstream comparison. Use later valid records in both directions whose continuity and tick order would fail if comparisons resumed. |
| `--revision` labels a historical commit while using current checker or fixture data; a preexisting output is relabeled as a newly measured gate. | Calibration / false provenance. Canonical evidence requires the tested revision, not intent; inherited script-name drift shows why assignment authority matters. | Extract checker **and input data** from the requested revision into isolated temporary trees. Keep the same frozen measurement implementation across revisions; retain `measured_revision` and raw returncode/stdout/stderr per gate. Label worktree runs as worktree, not the baseline commit. |

Fixable defects above can be corrected inside this one move. A proposal to knowingly keep a resumed comparison, lose old findings, alter fictional records, or mask a regression in exchange for a higher numerical result is instead an inadmissible trade under the assignment; recommend rejection to the canonical Rust judge, not averaging or weakened expectations. This critic does not issue that judgment.

## Numerical sample is not an axis verdict

The assigned sample has **five gates**, `total = 5`, `score = 2 * passed`: clean chain; unique-holder real break; dangling explicitness **in both fields**; ambiguous-to disclosure/scope/no definite downstream comparisons; symmetric ambiguous-from. The two ambiguity directions exercise the same mechanism and are correlated. The equal weights and fixed denominator are a targeted compatibility/disclosure rubric, not an independent estimate of lore expertise.

No exact baseline or candidate score was measured in this review. **6/10 -> 10/10 must remain a prediction unless both runs of this fixed rubric produce it.** The parent's five archived r85 runs have a different case set and cannot substitute. A measured 10 means only five specified behavioral gates passed; it does not cover every invalid-before-ambiguity, multi-item, repeat-notice, malformed-input, or preservation counterexample above. These can remain separate parent safety checks without changing the frozen denominator to manufacture an improvement.

Keep inherited whole-axis calibration, depth, and coverage scores unmeasured; record any measured holder-disclosure score in an explicitly separate sample metric with command and revision identity. Do not assign depth/coverage zero, retroactively give them calibration's baseline score, retire calibration, or call 10/10 saturation. Axis verdicts are per-axis evidence decisions, not the sample number (`SCORECARD.md:3-4,20-32`; `../AXES.md:11-16`).

## Narrow acceptance recommendation; no verdict

Recommend consideration **only after parent evidence** establishes exact local messages in both directions, the first-ambiguity one-notice-per-item rule even after an earlier stop, explicit permanent scope for both comparisons, no restarted comparisons, unchanged old diagnostics and exit behavior, all inherited fixture raw CLI triples preserved, and all existing fictional JSON bytes preserved. Keep raw outputs and measurement provenance; do not conceal unexpected output by silently weakening the rubric. One successful five-gate sample alone is insufficient to discharge all safety conditions.

- **Calibration:** bounded improvement is supportable only as disclosure of an existing assessment gap. Misleading scope or inferred certainty is harm; field-path convenience alone leaves r56's rejection rationale intact.
- **Depth and coverage:** recommend unchanged if their existing semantics and fictional records are preserved. More diagnostics, probes, or reports are not new supported domain detail or a coverage denominator.
- **Expansion and quality:** no improved learning-trend claim follows merely from this internal review or sample. Their canonical observables require admitted uncovered knowledge or stronger/reverified entries, respectively.
- **Discernment and promotion:** this dispatched critic is still lane-internal, not an outside admit-and-reject spot-check, SHONEN verifier, or promotion authority (`LEARNING.md:28-43`; canonical protocol promotion gate). No improved outside discernment or checked promotion box is supplied.

The smallest safe correction is the shared contract itself: two holder-local ambiguity messages, one independently tracked precise scope notice per item, no changed comparison/identity behavior, and an honestly bounded measurement. A source ID resolves only to an invented in-world record; it does not authenticate testimony, prove a transfer, establish canon, ownership, rights, or mechanics (`corpus/fixtures/README.md:110-119`). No second domain move is recommended.
