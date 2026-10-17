# Holder-assessment boundary: reading provenance ambiguity disclosures

source: fleet round-1 shared final diagnostic contract (holder-disclosure
move, calibration axis), restated verbatim in "The contract" below; static
inspection of `corpus/fixtures/check_bible.py` at baseline commit
`5eb9451baff217c19d5786405f9b2aa500b7c1b7`; parent-reproduced r85 probe
outputs in `reports/round-1/current-baseline.json` and
`reports/round-1/baseline-probes.json`; round-85 evidence in
`reports/round-85/`; citation-discipline rules in
`corpus/fixtures/README.md:110-128`. Authored by seat R1Guide from file
reads only; the fictional probe entities and transfers are authored fixture
inputs, not recovered or verified source records.

verified-at: STATIC PENDING PARENT RUNTIME. The baseline behaviors and
recorded probe triples below were observed by the parent (not by this seat).
The new `ambiguous entity` holder lines and the `unassessed` notice are
contract-specified integrated-checker behavior — no execution has yet
demonstrated them, and this seat ran nothing. The parent's smoke of the
agreed measurement command owns that verification; measured results are
appended by the parent only.

recheck: from the lane root, `python3
corpus/fixtures/measure_holder_disclosure.py --revision <commit>` (frozen
five-gate sample against any revision's checker AND inputs, isolated
temporary trees), plus the recorded r85 probe invocations in "Commands" as
a matched-pair drift check. Re-verify whenever the provenance branch of
`corpus/fixtures/check_bible.py` changes, either notice string or format
changes, or any `corpus/live/runs/round-85/probe-inputs/` JSON byte
changes. Re-check before treating any "10/10" sample score as anything
other than the five-gate ceiling.

## The contract (shared, final, round-1 calibration move)

Baseline `5eb9451` behavior, kept: a duplicated holder ID inside an item's
`provenance` records silently invalidates that record, permanently latches
the chain gate `can_check_chain = False` for that item, and the ONLY output
is the global `entities[j].id: duplicate entities id {id!r}` finding — the
ambiguous reference itself gets no line, and continuity plus tick-order
comparisons silently stop at that record and every later record of that
item (`reports/round-1/current-baseline.json` cases
`r85-masked-ambiguous` / `r85-isolated-ambiguous`; mechanism at
`corpus/fixtures/check_bible.py:212-224` silent/dangling branches,
`:234-237` permanent latch, `:238-245` both comparisons inside one gate,
`:246-247` later valid records do not re-enable it; baseline line refs).

The integrated checker adds disclosure only:

1. Both ambiguous holder references get
   `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}`
   and the record remains invalid (mirrors the existing relation-endpoint
   format at `check_bible.py:168`).
2. Exactly one notice per item, located at the FIRST ambiguous-holder
   record — even if an earlier invalid record already stopped
   comparisons. Notice text, verbatim:
   `{record_label}: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous`
3. The conservative permanent latch is preserved: comparisons do not
   resume within the run, and no break is inferred from ambiguity. All old
   diagnostics, exit behavior (`VIOLATION:` lines, `N violation(s); no
   canon changed`, `CLEAN: schema, citations, relations, timeline; 0
   violations`), the comparison state machine, and every existing fictional
   JSON byte are preserved. No generic invalidity refactor.

`{record_label}` is the existing provenance record path, e.g.
`entities[3].provenance[1]` for the `seal` item's second transfer.

## Decision table: reference state → output → next action

| Holder reference state | Output for that state (contract) | What the output does NOT say | Editor's safe action |
|---|---|---|---|
| Unique holder IDs; chain continuous; ticks strictly ascending | No holder findings; the item may contribute to `CLEAN` or unrelated findings elsewhere | Source text support, true custody, or canon — a citation resolves a fictional ID only (`corpus/fixtures/README.md:116-118`) | None on holders. |
| Unique holder IDs; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (baseline `:241-245`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE, a different mechanism from ambiguous holder identity) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim | Choose the editorially-intended field, edit, rerun. |
| Dangling holder, either field (`from_holder`/`to_holder` ID absent from entities) | Explicit `{record_label}.{from_holder|to_holder}: dangling entity {id!r}`; record invalid (baseline `:212-214`, `:220-222`, kept) | Ambiguity — nothing is duplicated; a dangling ID and an ambiguous ID are different states | Create or point to the intended single entity, rerun. No `ambiguous entity` line or `unassessed` notice is owed. |
| Ambiguous holder, either field (ID matches ≥ 2 entity rows) | Global duplicate `entities[j].id: duplicate entities id {id!r}` (kept) PLUS `{record_label}.{field}: ambiguous entity {id!r}` PLUS, at the first ambiguous-holder record only, the single `…continuity and tick-order comparisons unassessed…` notice. No definite chain-break or tick-order finding for that record or any later record of the item | A hidden break, a hidden clean result, or which duplicate row is "the real" vault. `r85-isolated-ambiguous` (internally consistent chain) and `r85-masked-ambiguous` (genuine downstream break) are IDENTICAL in baseline output and differ post-contract only in what record [2]'s unassessed state hides either way | Resolve identity (checklist below), rerun, review subsequent findings. |
| Ambiguity after an earlier invalid record (malformed key set, bad tick, dangling, unknown source…) | The notice still appears at the first ambiguous-holder record even though comparisons stopped earlier; scope wording covers "this and all later records" | That ambiguity is where assessment first stopped — an earlier invalid record may have stopped it sooner | Fix the earlier invalidity and the identity; rerun; treat the whole tail as unassessed until a clean comparison run. |
| Later valid records in an item whose chain is already unassessed | Ordinary record-level diagnostics continue (schema, keys, dangling-vs-unique identity, source status); continuity/tick comparisons do not run for the rest of the item, per run | Comparison passed — absence of comparison findings after the notice is NOT a pass | Repair identity, rerun; the gate is per run, so a fresh run after dedup can assess the full chain. |

## Editor checklist

1. Identify the holder: if output shows `…provenance[i].{field}: ambiguous
   entity 'x'`, find every `entities.json` row with id `x`. Neither the
   checker, the index, nor array order chooses a duplicate — same rule the
   lane already documents for source IDs (`corpus/fixtures/README.md:126-127`,
   "Both source rows remain untouched; array order does not choose one").
2. Resolve identity deliberately: rename the entity that should carry a
   different id, or merge the duplicate rows because they are one entity.
   Make only that structural choice; do not invent story facts, custody,
   or canon to justify the dedup. Do not delete records to silence a
   finding.
3. Rerun the same command against the same bible directory. Dedup is the
   prerequisite for detection, not the repair itself: the r85 sealed
   reviewer deduped on the masked output, believed the file had exactly one
   defect, and would have shipped the still-hidden chain break; only the
   rerun surfaces it verbatim (`reports/round-85/r85-sealed-reviewer.md`,
   Step 3; `reports/round-85/r85-axis-adjudicator.md`, "Bounds on the gain").
4. Review subsequent findings: new `provenance chain break` /
   `provenance tick` lines that appear AFTER your dedup are comparisons
   now running, not regressions. Address them one at a time, rerunning
   after each repair.
5. Stop decision: stop only when a rerun exits 0 (`CLEAN`) or every finding
   is repaired or deliberately editorially accepted. A violation count —
   even `1 violation(s)` — does not mean "exactly one defect." Treat the
   `unassessed` notice as an open item, never as a pass, and never as
   proof of a break.

## Precise limits of the disclosure

- Scope: exactly two assessments stop — provenance continuity (next
  `from_holder` equals previous `to_holder`; first record `from_holder`
  null) and tick order (strict increase) — at the ambiguous-holder record
  and ALL later records of that item. The stop is permanent for that run;
  no later valid record re-enables it (baseline `:234-237`, `:246-247`;
  preserved by the contract).
- Everything else continues: JSON loading, field schema, key-set checks,
  holder shape validation, dangling-vs-duplicate classification, source
  citation status, global duplicate-ID findings, and all relation,
  timeline, and contradiction checks.
- Three states, not two: after the notice the affected comparisons are
  UNASSESSED — neither clean nor broken. Output alone cannot tell you
  whether the masked tail contains a break; only resolving identity and
  rerunning can. Do not resume, infer, or announce a break from the
  ambiguous input itself.
- No truth claims: nothing here asserts a hidden break, true custody,
  entity identity, canon, source-text support, rights, or game mechanics.
  The notice is about the checker's assessment boundary, not the fictional
  world. Probe fixtures are authored inputs; chain breaks inside them are
  injected test scaffolding, not lore.
- Chain eligibility upstream of this contract is unchanged (baseline
  `:183`): comparisons require sources loaded, `kind == "item"`, and the
  item's own id unique.
- Measurement ceiling: `score = 2 × passed` on the five-gate disclosure
  sample; 10/10 means 5/5 specified gates passed. It is not whole-domain
  calibration, not saturation, not promotion, and not evidence that an
  external reader changed behavior.

## Commands (self-contained, run from the lane root)

Recorded-baseline probe check (exit codes and outputs pinned in
`reports/round-1/current-baseline.json`):

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"
done
```

Agreed measurement entry point (five gates: clean chain; unique-holder real
break; dangling-holder explicitness both fields; ambiguous-to local
disclosure plus downstream scope/no definite comparisons; ambiguous-from
symmetric behavior; JSON with `measured_revision`, `total=5`, `passed`,
`score=2*passed`, raw returncode/stdout/stderr per case; tests the requested
revision's checker AND input data in isolated temporary trees):

```sh
python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>
```

Omitting `--revision` targets the current worktree (optional mode).

## Evidence and citations

- Checker: `corpus/fixtures/check_bible.py` — holder count collection
  `:157-159`; dangling diagnostics `:212-214` (to) and `:220-222` (from);
  silent ambiguity branches `:215-216` and `:223-224`; permanent latch
  `:234-237`; comparison gate `:238-245`; no-resume previous-value update
  `:246-247`; relation-endpoint ambiguity precedent `:168`; CLI/exit
  behavior `:320-330`. Baseline `5eb9451` line refs; integrated revision
  shifts them.
- Probe inputs: `corpus/live/runs/round-85/probe-inputs/{r85-control,
  r85-unique-break-control,r85-masked-ambiguous,r85-isolated-ambiguous,
  r85-harbor-repro}/` — masked `entities.json:49-93` and unique-control
  `entities.json:49-81` carry identical transfers `(null→mira,0)`,
  `(mira→vault,3)`, `(harbor→tower,4)`; masked adds a second `vault` row.
  Isolated carries a continuous chain ending in the duplicated `vault` at
  record `[2]`.
- Round-85 reports: `reports/round-85/r85-author.md` (probe design,
  `:38-75`), `r85-verifier.md`, `r85-sealed-reviewer.md` (operative danger:
  correct first action, false sense of finality),
  `r85-axis-adjudicator.md` (verdict ADMIT, bounded; repair reserved as a
  separate candidate needing tuple replay).
- Fleet round-1 evidence: `reports/round-1/current-baseline.json` and
  `reports/round-1/baseline-probes.json` (parent-recorded CLI triples at
  `5eb9451`; all recorded stderr empty); `reports/round-1/critic.md`
  (counterexample table this guidance encodes);
  `reports/round-1/current-dispatch.json` (seat write scopes).
- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline,
  no inferred history, citation ≠ support) and `:121-128` (round-7
  duplicate-source rule mirrored by this holder contract).
- Lane declaration: `SCORECARD.md` fleet-round-1 calibration declaration
  (unmeasured tie, falsifiability tie-break).

## Status split

- OBSERVED (by the parent; recorded JSON above): the five baseline probe
  triples at `5eb9451` — masked and isolated emit ONLY the global duplicate;
  unique control emits the definite record-2 break; control is CLEAN;
  harbor-repro shows timeline-endpoint ambiguity voiced while holder
  references stay silent.
- STATIC SOURCE READ (this seat): the code line refs and state-machine
  behavior above; no execution performed here.
- CONTRACT-SPECIFIED, PENDING PARENT RUNTIME: the `ambiguous entity` holder
  lines, the single per-item `unassessed` notice, and the existence and
  output of `corpus/fixtures/measure_holder_disclosure.py` (owned by seat
  R1Measure, checker edits by seat R1Checker).
- UNKNOWN / UNMEASURED: measured `passed` count and per-case triples from
  the disclosure harness; behavior of the `from_holder` direction under the
  integrated checker (no r85 probe exercises it; the harness's gate 5 is
  designed precisely to close this); whether any active fixture outside the
  r85 probes combines provenance with a duplicated holder.

## Measured results (parent-owned slot)

Nothing recorded by this seat. The parent appends measured
`measure_holder_disclosure.py` output here after the round-1 smoke; until
then every contract line above remains static-pending-runtime.
