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
inputs, not recovered or verified source records. The provenance branch was
then revised by round-87 seat C1 (commit `03c6746`, delivered tree
`2b48ca7`); round-87 seat I2 replayed the delivered checker and rewrote the
contract, decision-table, limits, and status sections below so they match
its observed output (`.ufo/waves/round-87/followup/I2.md`).

verified-at: RUNTIME REPLAYED on the delivered tree at `2b48ca7` by
round-87 seat I2; exact commands and observed output are pasted under
"Commands" and in `.ufo/waves/round-87/followup/I2.md`. The `ambiguous
entity` holder lines and both `unassessed` notice forms below are
demonstrated by that replay, not contract text. This verifies the listed
checker behavior only; it is not a five-gate score and not a claim about
fictional truth. The baseline (`5eb9451`) triples remain as recorded in
`reports/round-1/current-baseline.json` and `reports/round-1/baseline-probes.json`.

recheck: from the lane root, replay the five recorded r85 probe inputs with
the delivered checker (see "Commands"), and re-run any fixture that
combines `provenance` with a duplicated entity id. Re-verify whenever the
provenance branch of `corpus/fixtures/check_bible.py` changes, either
notice string or format changes, or any
`corpus/live/runs/round-85/probe-inputs/` JSON byte changes. The
`corpus/fixtures/measure_holder_disclosure.py` helper named by the round-1
contract does not exist at `2b48ca7` (`python3
corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
`No such file or directory`); run it only in a revision that contains it,
and treat its five-gate sample as a ceiling, never as a score for a tree
that has not run it.

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

The delivered checker (`2b48ca7`) adds disclosure only:

1. Both ambiguous holder references get
   `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}`
   and the record remains invalid (mirrors the existing relation-endpoint
   format at `check_bible.py:168`; delivered `:227` for `to_holder`,
   `:238` for `from_holder`).
2. Exactly one item-level notice per item, located at the FIRST
   ambiguous-holder record — even if an earlier invalid record already
   stopped comparisons. Notice text, verbatim (delivered `:243`):
   `{record_label}: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous`
   This notice states the scope once and never repeats for the item.
3. A per-record disclosure at that same stop record AND at every later
   record of the item, naming the ambiguous holder reference(s) and the
   origin record. Text, verbatim (delivered `:250` at the stop, `:189-195`
   for every later record):
   `{record_label}: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity {field} {id!r} first occurred at {origin_label}`
   Several references at one record are joined by `, ` in the order
   `to_holder` then `from_holder`. The disclosure repeats the ORIGIN cause
   on every later record: a different duplicated id introduced later still
   gets its own local `ambiguous entity` line, but the disclosure keeps
   naming the first stop (`.ufo/waves/round-87/followup/I2.md` probe `p2`).
   Because it is emitted at the top of the record loop, it also appears on
   later records that are not objects or lack the required keys, alongside
   their own `expected object` / `expected exactly …` finding (probe `p6`).
4. Emission does not depend on chain eligibility: the disclosures appear
   even when `can_check_chain` was already false, e.g. `provenance` on a
   non-item entity or an item whose own id is duplicated (probes `p8`,
   `p7`).
5. The conservative permanent latch is preserved: comparisons do not
   resume within the run, and no break is inferred from ambiguity. All old
   diagnostics, exit behavior (`VIOLATION:` lines, `N violation(s); no
   canon changed`, `CLEAN: schema, citations, relations, timeline; 0
   violations`), the comparison state machine, and every existing fictional
   JSON byte are preserved. No generic invalidity refactor. Verified for
   the 133 pre-round-87 fixture directories: the baseline `5eb9451` checker
   and the delivered checker, run against the same 133 input directories,
   produced 0 tuple changes (exit code, stdout, and stderr;
   `.ufo/waves/round-87/followup/I2.md` §2).

`{record_label}` is the existing provenance record path, e.g.
`entities[3].provenance[1]` for the `seal` item's second transfer.

## Decision table: reference state → output → next action

| Holder reference state | Output for that state (contract) | What the output does NOT say | Editor's safe action |
|---|---|---|---|
| Unique holder IDs; chain continuous; ticks strictly ascending | No holder findings; the item may contribute to `CLEAN` or unrelated findings elsewhere | Source text support, true custody, or canon — a citation resolves a fictional ID only (`corpus/fixtures/README.md:116-118`) | None on holders. |
| Unique holder IDs; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (baseline `:241-245`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE, a different mechanism from ambiguous holder identity) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim | Choose the editorially-intended field, edit, rerun. |
| Dangling holder, either field (`from_holder`/`to_holder` ID absent from entities) | Explicit `{record_label}.{from_holder|to_holder}: dangling entity {id!r}`; record invalid (baseline `:212-214`, `:220-222`, kept) | Ambiguity — nothing is duplicated; a dangling ID and an ambiguous ID are different states | Create or point to the intended single entity, rerun. No `ambiguous entity` line or `unassessed` notice is owed. |
| Ambiguous holder, either field (ID matches ≥ 2 entity rows) | Global duplicate `entities[j].id: duplicate entities id {id!r}` (kept) PLUS `{record_label}.{field}: ambiguous entity {id!r}` PLUS the item-level `…unassessed at this and all later records because holder identity is ambiguous` notice at the first ambiguous-holder record PLUS a per-record `…unassessed because ambiguous holder identity {field} {id!r} first occurred at {origin_label}` disclosure at that record and at EVERY later record of the item. No definite chain-break or tick-order finding for that record or any later record of the item | A hidden break, a hidden clean result, or which duplicate row is "the real" vault. `r85-isolated-ambiguous` (internally consistent chain) and `r85-masked-ambiguous` (genuine downstream break) both hide the downstream state; delivered output differs only in how many records the disclosure names — 4 findings vs 5 — and the masked break stays unreported either way (`I2.md` §1) | Resolve identity (checklist below), rerun, review subsequent findings. |
| Ambiguity after an earlier invalid record (malformed key set, bad tick, dangling, unknown source…) | Both stop notices still appear at the first ambiguous-holder record even though comparisons stopped earlier, and every later record carries the per-record disclosure. The item-level wording covers "this and all later records"; the per-record disclosure names only the holder-ambiguity origin, not the earlier cause | That ambiguity is where assessment first stopped — an earlier invalid record may have stopped it sooner, and the per-record disclosure names the ambiguity as cause even when an earlier invalidity had already latched the gate (`I2.md` probe `p3`) | Fix the earlier invalidity and the identity; rerun; treat the whole tail as unassessed until a clean comparison run. |
| Later valid records in an item whose chain is already unassessed | Ordinary record-level diagnostics continue (schema, keys, dangling-vs-unique identity, source status) PLUS the per-record disclosure on each of them; continuity/tick comparisons do not run for the rest of the item, per run | Comparison passed — the repeated disclosure is not a new defect per record, and absence of comparison findings after the notice is NOT a pass | Repair identity, rerun; the gate is per run, so a fresh run after dedup can assess the full chain. |

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
   even `1 violation(s)` — does not mean "exactly one defect." Every record
   at or after the ambiguous-holder stop carries its own
   `unassessed because ambiguous holder identity …` disclosure, so one
   ambiguous holder adds one line per later record; that repetition is one
   open item, never a pass, and never proof of a break.

## Precise limits of the disclosure

- Scope: exactly two assessments stop — provenance continuity (next
  `from_holder` equals previous `to_holder`; first record `from_holder`
  null) and tick order (strict increase) — at the ambiguous-holder record
  and ALL later records of that item. The stop is permanent for that run;
  no later valid record re-enables it (baseline `:234-237`, `:246-247`;
  preserved by the contract; delivered latch `:260-263`, gate `:264-271`).
- Two notice forms, one boundary: the item-level notice states the scope
  once ("at this and all later records"); the per-record disclosure states
  the local status and the origin stop on every affected record. Neither is
  a finding about the chain — both report that the comparison did not run.
- Everything else continues: JSON loading, field schema, key-set checks,
  holder shape validation, dangling-vs-duplicate classification, source
  citation status, global duplicate-ID findings, and all relation,
  timeline, and contradiction checks.
- Three states, not two: after the stop the affected comparisons are
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
  `:183`; delivered `:183`): comparisons require sources loaded,
  `kind == "item"`, and the item's own id unique. The disclosures are NOT
  gated by it — they are emitted on any item that carries `provenance`,
  even one whose chain was never eligible (delivered `:189-195,242-250`;
  `I2.md` probes `p7`, `p8`).
- Measurement ceiling: `score = 2 × passed` on the five-gate disclosure
  sample; 10/10 means 5/5 specified gates passed. It is not whole-domain
  calibration, not saturation, not promotion, and not evidence that an
  external reader changed behavior. No such score exists for `2b48ca7`:
  the helper is absent there.

## Commands (self-contained, run from the lane root)

Delivered replay — the five recorded r85 probe inputs against the checker at
`2b48ca7` (run from the lane root; baseline triples for the same five inputs
are pinned in `reports/round-1/current-baseline.json`):

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
```

Observed output (verbatim; stderr empty in all five):

```text
=== r85-control ===
CLEAN: schema, citations, relations, timeline; 0 violations
[rc=0]
=== r85-unique-break-control ===
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'
1 violation(s); no canon changed
[rc=1]
=== r85-masked-ambiguous ===
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[1]
5 violation(s); no canon changed
[rc=1]
=== r85-isolated-ambiguous ===
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault' first occurred at entities[3].provenance[2]
4 violation(s); no canon changed
[rc=1]
=== r85-harbor-repro ===
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'harbor' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'harbor' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
7 violation(s); no canon changed
[rc=1]
```

Against the pinned baseline this is 1 → 5 findings on `r85-masked-ambiguous`,
1 → 4 on `r85-isolated-ambiguous`, and 2 → 7 on `r85-harbor-repro`; the
control and the unique-holder break case are unchanged. Every baseline line
survives verbatim. The two in-tree direction fixtures added by C1 replay
symmetrically — `python3 corpus/fixtures/check_bible.py
corpus/fixtures/r87-masked-break-from-ambiguous` gives `6 violation(s)` with
`ambiguous holder identity from_holder 'dup' first occurred at
entities[3].provenance[0]` on records [0], [1], and [2], and
`…r87-masked-break-to-ambiguous` gives the same shape with `to_holder`.

Five-gate measurement entry point (clean chain; unique-holder real break;
dangling-holder explicitness both fields; ambiguous-to local disclosure plus
downstream scope/no definite comparisons; ambiguous-from symmetric behavior;
JSON with `measured_revision`, `total=5`, `passed`, `score=2*passed`, raw
returncode/stdout/stderr per case; tests the requested revision's checker AND
input data in isolated temporary trees):

```sh
python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>
```

That helper does not exist at `2b48ca7` — `python3
corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
`can't open file ... No such file or directory` — so no five-gate score is
recorded for this tree. Run the helper only in a revision that contains it;
until then the delivered replay above is the behavioral evidence.

## Evidence and citations

- Checker at baseline `5eb9451`: `corpus/fixtures/check_bible.py` — holder
  count collection `:157-159`; dangling diagnostics `:212-214` (to) and
  `:220-222` (from); silent ambiguity branches `:215-216` and `:223-224`;
  permanent latch `:234-237`; comparison gate `:238-245`; no-resume
  previous-value update `:246-247`; relation-endpoint ambiguity precedent
  `:168`; CLI/exit behavior `:320-330`. These are the line refs the
  baseline paragraph of "The contract" cites.
- Checker at delivered `2b48ca7` (`corpus/fixtures/check_bible.py`, 356
  lines): holder count collection `:157-159`; dangling diagnostics `:223-225`
  (to) and `:234-236` (from); ambiguity branches `:226-230` (to) and
  `:237-241` (from); item-level notice `:242-244`; per-record disclosure at
  the stop `:245-250` and at every later record `:189-195`; permanent latch
  `:260-263`; comparison gate `:264-271`; no-resume previous-value update
  `:272-273`; relation-endpoint ambiguity precedent `:168`; CLI/exit
  behavior `:346-356`.
- Round-87 evidence: `.ufo/waves/round-87/CB1.md` (pre-C1 replay of the
  same five probes at `28706dc`, plus the drift draft
  `patches/CB1-drift.json`) and `.ufo/waves/round-87/followup/I2.md`
  (delivered-tree replay, 133-directory preservation check, census,
  scratch boundary probes `p1`-`p8`, provenance-bearing fixture
  inventory).
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

- OBSERVED on the delivered tree (round-87 seat I2, `2b48ca7`; exact
  commands and output in "Commands" and
  `.ufo/waves/round-87/followup/I2.md`): the five r85 probe triples pasted
  above; masked and isolated disclose the ambiguous holder per record
  (5 and 4 findings), the unique control still reports the definite
  record-2 break, control is still CLEAN, and harbor-repro voices the
  timeline-endpoint ambiguity alongside two ambiguous-holder records
  (7 findings).
- OBSERVED at baseline `5eb9451` (parent-recorded JSON): masked and
  isolated emitted ONLY the global duplicate; unique control emitted the
  definite record-2 break; control was CLEAN; harbor-repro showed
  timeline-endpoint ambiguity voiced while holder references stayed
  silent.
- REPLAYED, not scored: no five-gate `passed` count exists for `2b48ca7`;
  the documented helper is absent at that revision.
- UNKNOWN / UNMEASURED: whether any in-tree fixture outside the r85 probes
  and the four `r87-masked-*` / `r87-chain-*` additions combines
  `provenance` with a duplicated holder id. Measured at `2b48ca7`: of the
  nine fixture directories containing `provenance`, none does
  (`I2.md` §5; `r7-item-ambiguous` is ambiguous SOURCE only, `r61-*` are
  dangling holders). Also unmeasured: any external reader behavior change.

## Measured results (parent-owned slot)

No five-gate score is recorded for the delivered tree `2b48ca7`: the
documented measurement helper is absent at that revision. The behavioral
replay that stands in for it is the five-case delivered output pasted under
"Commands" plus the scratch boundary probes `p1`-`p8` recorded in
`.ufo/waves/round-87/followup/I2.md`; every contract, table, and limits line
above is stated as-of that replay.
