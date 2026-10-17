# Fleet round 1 — R1Guide executor report (holder-disclosure guidance seat)

## Scope and evidence status

Single calibration-move documentation seat under `reports/round-1/
current-dispatch.json`. I wrote only my two assigned paths:
`corpus/knowledge/holder-assessment-boundary.md` (new domain guidance) and
this report. I ran no checker, no measurement harness, no probe, no test,
no build, no lint, no formatter; every statement here is a static file read
of the repository at the inherited working state or a restatement of the
shared round-1 contract relayed by the parent. The guidance document's
`verified-at:` marks exactly that: baseline probe behavior is parent-recorded
evidence; the new diagnostics are contract-specified integrated behavior
PENDING the parent's runtime smoke. No measured result is claimed anywhere
by this seat; the parent appends measured results after smoke.

## Files changed

- `corpus/knowledge/holder-assessment-boundary.md` — NEW. Self-contained,
  lane-root usage guidance for the shared final diagnostic contract:
  - `source:` / `verified-at:` (static pending parent runtime) /
    `recheck:` header, with a recheck trigger list (provenance-branch edit,
    notice-string change, probe-byte change) and the frozen five-gate
    command.
  - "The contract" section restating verbatim: both ambiguous holder
    references get `{record_label}.{from_holder|to_holder}: ambiguous
    entity {id!r}` while remaining invalid; exactly one notice per item at
    the first ambiguous-holder record even if an earlier invalid record
    already stopped comparisons — `provenance continuity and tick-order
    comparisons unassessed at this and all later records because holder
    identity is ambiguous`; permanent latch preserved; all old diagnostics,
    exit behavior, state machine, and fictional JSON bytes preserved; no
    generic invalidity refactor.
  - Six-row decision table covering unique-clean, unique-broken (definite
    findings with the ambiguous-SOURCE `input-structural` prefix kept
    distinct from ambiguous holder identity), dangling-both-fields,
    ambiguous-both-fields, ambiguity-after-earlier-invalid, and later-valid
    records under an open unassessed state; each row pairs output with "not
    said" and the safe next action.
  - Five-step editor checklist: resolve identity deliberately (neither
    checker nor array order chooses a duplicate, mirroring
    `corpus/fixtures/README.md:126-127`), structural-only edits, rerun the
    same command, review subsequent findings (post-dedup break lines are
    comparisons now running, not regressions), and an explicit safe
    stopping decision (stop only on exit-0 CLEAN or addressed/accepted
    findings; `1 violation(s)` ≠ one defect; `unassessed` ≠ pass ≠ break).
  - Precise limits: continuity AND tick-order stop permanently for the
    remainder of that item within the run; everything else (schema,
    key-sets, dangling-vs-duplicate, source status, relations, timeline,
    contradictions, global duplicate IDs) continues; three-state honesty;
    no hidden break, true custody, canon, source-text support, rights, or
    mechanics asserted; unchanged upstream chain eligibility
    (`check_bible.py:183`); 10/10 = 5/5 sample gates only, not whole-domain
    calibration or promotion.
  - Commands block: the five recorded r85 probe invocations and the agreed
    measurement entry point `python3
    corpus/fixtures/measure_holder_disclosure.py --revision <commit>`
    (worktree mode = flag omitted), with its output contract
    (`measured_revision`, `total=5`, `passed`, `score=2*passed`, raw
    per-case triples). All commands are lane-root self-contained; the
    historical `.shokunin/lore/` prefix in older reports/README snippets is
    the pre-standalone path for the same files.
  - Evidence-and-citations block + an explicit OBSERVED / STATIC-READ /
    CONTRACT-SPECIFIED-PENDING / UNKNOWN status split.
- `reports/round-1/r1-current-guide.md` — NEW (this report). Advisory only.

No other file was created or modified: inherited
`reports/round-1/{dispatch.json,critic.md,baseline-probes.json,
current-baseline.json,current-dispatch.json}` are untouched and their
dispatch claims are not mine; LOG.md, SCORECARD.md, SHONEN.md, README,
PROVINCE, corpus indexes, `corpus/fixtures/check_bible.py`,
`corpus/fixtures/measure_holder_disclosure.py`, and every fixture/probe
JSON byte are outside my scope and unchanged here.

## Behavior delivered

None at runtime — this is a guidance deliverable. What changed is the
domain's knowledge surface: an editor facing a duplicated provenance
holder now has a written, command-backed decision path that (a) names the
two suppressed comparisons and their permanent downstream scope, (b) forbids
choosing a duplicate automatically or inferring a break, (c) makes
rerun-after-repair the mandated stopping discipline the r85 sealed reviewer
identified as the neutralizer of the false-finality danger
(`reports/round-85/r85-sealed-reviewer.md`, Step 3 and UNKNOWNs;
`reports/round-85/r85-axis-adjudicator.md`, "Bounds on the gain").

## Retained evidence (static reads supporting the guidance)

- Baseline mechanism, `corpus/fixtures/check_bible.py` at `5eb9451…`:
  counts `:157-159`; dangling voiced `:212-214`/`:220-222`; ambiguity
  silent `:215-216`/`:223-224`; permanent latch `:234-237`; both
  comparisons inside one gate `:238-245`; no-resume updates `:246-247`;
  relation-endpoint `ambiguous entity` precedent `:168`; CLI/exit
  `:320-330`.
- Parent-reproduced r85 triples: `reports/round-1/current-baseline.json`
  and `reports/round-1/baseline-probes.json` — masked and isolated emit
  ONLY `entities[5].id: duplicate entities id 'vault'`; unique control
  emits the record-2 break; all stderr empty.
- Probe data: `corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous/
  entities.json:49-93` vs `…/r85-unique-break-control/entities.json:49-81`
  (identical transfers; masked adds the second `vault` row);
  `…/r85-isolated-ambiguous/entities.json:49-94` (continuous chain ending
  at the duplicated `vault` — the proof that unassessed ≠ broken).
- Round-85 ADMIT bounds: `reports/round-85/r85-author.md:38-75`,
  `r85-sealed-reviewer.md`, `r85-axis-adjudicator.md` (repair reserved for
  a separate candidate with mandatory replay — the round-1 move this
  guidance documents).
- Rules mirrored: `corpus/fixtures/README.md:110-119` (citation resolves an
  invented record; checker never inspects its text) and `:121-128`
  (round-7 duplicate-source discipline).

## Risks and notes for the parent

1. Contract-vs-observation boundary is stated in the guidance itself; if
   the integrated checker's wording drifts from the shared contract, the
   doc's "verbatim" claims become false — the recheck header names that
   trigger. Parent should reconcile any wording drift at integration, not
   in this seat.
2. Line refs are labeled baseline `5eb9451` refs; R1Checker's edit will
   shift them. Acceptable as anchors, worth a one-line note only if the
   parent wants post-integration numbers instead.
3. Path-naming discrepancy: the inherited `reports/round-1/dispatch.json`
   names the documentation seat's write scope as
   `corpus/knowledge/round-1-holder-assessment.md`, while
   `current-dispatch.json` and this assignment name
   `corpus/knowledge/holder-assessment-boundary.md`. I followed the
   current dispatch/assignment. If any index or LOG line will point at the
   old name, the parent (index owner) should reconcile.
4. The `from_holder` ambiguity direction is disclosed in the doc as
   contract-specified and gate-5-measured; no existing r85 probe exercises
   it, and the doc says so under UNKNOWN. Expect that gate to be the
   first real evidence of symmetry.
5. Expected integrated output for `r85-masked-ambiguous` under the
   contract, derived from contract text (NOT an observation): global
   duplicate + `entities[3].provenance[1].to_holder: ambiguous entity
   'vault'` + the single unassessed notice at `entities[3].provenance[1]`,
   exit 1, no record-2 chain-break line. Parent smoke should treat this
   shape as a claim to check, not a recorded result.

## Unrun recommendations (parent-owned verification, once, after integration)

- `python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>`
  on baseline and integrated revisions; retain JSON with `measured_revision`
  and raw per-case triples.
- Re-run the five recorded r85 probe commands; confirm the two unchanged
  classes (control CLEAN; unique break verbatim), the two masked/isolated
  outputs gained exactly the two contract lines each, harbor-repro
  unchanged, and stderr stayed empty.
- Confirm all inherited fixture CLI triples and every existing fictional
  JSON byte preserved (parent already owns this check per the contract).

## Blockers

None. Assigned implementation is complete within scope; no runtime claim
made or required.
