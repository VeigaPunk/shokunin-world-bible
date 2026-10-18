# Holder-assessment boundary: reading provenance ambiguity disclosures

> **PROPOSAL — not applied.** This file is round-88 seat CB1's refreshed
> version of `corpus/knowledge/holder-assessment-boundary.md` (329 lines at
> `dfd1fbc` and `2ea9ef1`, blob `6f252d79079b7a473c442da787ba0e3c1d48f20b`).
> CB1 holds no write scope on the tracked file; the drift inventory that
> motivates each change is in `.ufo/waves/round-88/followup/CB1.md`. Apply by
> replacing the tracked file with this content, or cherry-pick the sections
> marked in CB1.md §Findings (D1-D21).

source: fleet round-1 shared diagnostic contract (holder-disclosure move,
calibration axis), whose round-1 baseline paragraph is kept verbatim in "The
contract" below; static inspection of `corpus/fixtures/check_bible.py` at
baseline commit `5eb9451baff217c19d5786405f9b2aa500b7c1b7`; parent-reproduced
r85 probe outputs in `reports/round-1/current-baseline.json` and
`reports/round-1/baseline-probes.json`; round-85 evidence in
`reports/round-85/`; citation-discipline rules in
`corpus/fixtures/README.md:110-128`. Authored by seat R1Guide from file reads
only; the fictional probe entities and transfers are authored fixture inputs,
not recovered or verified source records. The provenance branch was revised
three times after that: round-87 seat C1 added the per-record disclosure
(commit `03c6746`, delivered tree `2b48ca7`), and round-88 seat C1 replaced
the holder-only latch with permanent first-stop cause tracking and armed the
stop from shape-invalid records (integrated in `2ea9ef1`). This revision was
rewritten by round-88 seat CB1 against the delivered checker at `2ea9ef1`
(`.ufo/waves/round-88/followup/CB1.md`); the r87 contract, decision table,
limits, and status sections it replaces are superseded, and the r87 replay
evidence at `2b48ca7` is preserved only in
`.ufo/waves/round-87/followup/I2.md`.

verified-at: RUNTIME REPLAYED on the delivered tree at `2ea9ef1` by round-88
seat CB1; exact commands and observed output are pasted under "Commands" and
in `.ufo/waves/round-88/followup/CB1.md`. The single `remain unassessed …
first stop:` disclosure form, every named first-stop cause, the cause
precedence order, and the emission-order asymmetry below are demonstrated by
that replay, not contract text. This verifies the listed checker behavior
only; it is not a five-gate score and not a claim about fictional truth. The
baseline (`5eb9451`) triples remain as recorded in
`reports/round-1/current-baseline.json` and `reports/round-1/baseline-probes.json`.

recheck: from the lane root, replay the five recorded r85 probe inputs with
the delivered checker (see "Commands"), and re-run any fixture that combines
`provenance` with a duplicated entity id. Re-verify whenever the provenance
branch of `corpus/fixtures/check_bible.py` changes, whenever the
`remain unassessed` template string or any named first-stop cause changes, or
whenever any `corpus/live/runs/round-85/probe-inputs/` JSON byte changes. The
`corpus/fixtures/measure_holder_disclosure.py` helper named by the round-1
contract does not exist at `2ea9ef1` (`python3
corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
`No such file or directory`); run it only in a revision that contains it, and
treat its five-gate sample as a ceiling, never as a score for a tree that has
not run it.

## The contract (round-1 baseline paragraph, kept)

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

The delivered checker (`2ea9ef1`) replaces the holder-only latch with a
permanent first-stop cause record:

1. **One disclosure form, one line per affected record.** A single template,
   verbatim (delivered `:194`):

   ```text
   {record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause} at {origin_label}
   ```

   It is emitted once at the record that arms the stop and once at every later
   record of that item. There is no separate item-level notice: the r87
   wording `… unassessed at this and all later records because holder identity
   is ambiguous` and the r87 per-record wording `… unassessed because
   ambiguous holder identity {field} {id!r} first occurred at {origin_label}`
   are both absent from the delivered checker.

2. **Any first cause arms the stop, and the disclosure names it.** `{cause}`
   is the first stop condition the checker reached, in the precedence order
   given under "Precise limits". `{origin_label}` is the record label that
   armed it (`entities[3].provenance[1]`) or, for the three item-level
   conditions, the item label (`entities[3].provenance`). Ambiguous holder
   identity is one cause among several, not the only one.

3. **Local `ambiguous entity` lines are unchanged in shape.** Both ambiguous
   holder references get
   `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}` and the
   record remains invalid (mirrors the relation-endpoint format at
   `check_bible.py:168`; delivered `:260` for `to_holder`, `:272` for
   `from_holder`). Several references at one record are joined by `, ` in the
   order `to_holder` then `from_holder` (`:277-280`).

4. **A shape-invalid dict record can arm the stop.** When a record fails the
   exact-key-set check, the checker still inspects its nonempty string
   `to_holder` / `from_holder` values for duplicated entity IDs
   (`:211-219`): each ambiguous field gets its own local `ambiguous entity`
   line, and — absent an earlier stop — the cause becomes
   `malformed record (unexpected field set); ambiguous holder identity {refs}`
   (`:227-230`). This is the only place two cause phrases are combined. A
   non-dict record cannot arm a holder-ambiguity cause: it hits
   `malformed record (expected object)` first (`:201-206`).

5. **The conservative permanent latch is preserved.** Comparisons do not
   resume within the run, and no break is inferred from ambiguity. All old
   diagnostics, exit behavior (`VIOLATION:` lines, `N violation(s); no canon
   changed`, `CLEAN: schema, citations, relations, timeline; 0 violations`),
   the comparison state machine, and every existing fictional JSON byte are
   preserved. No generic invalidity refactor. Verified by CB1 for the 149
   fixture directories at `2ea9ef1`: the baseline `dfd1fbc` checker and the
   delivered checker, run against the same 149 input directories, produced 0
   exit-code changes, 0 stderr changes, and 12 changed stdout tuples — the
   nine pre-existing disclosure deltas (`r61-independent-empty`,
   `r61-independent-unavailable`, `r87-masked-break-from-ambiguous`,
   `r87-masked-break-to-ambiguous`, `r87-probe-entry-shape`,
   `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`,
   `r87-probe-record-and-chain`, `r87-probe-shape-ambiguous`) plus the three
   new r88 fixtures (`r88-mixed-stop`, `r88-nonholder-stop`,
   `r88-shape-ambiguous-armed`). The fourth new directory,
   `r88-m3-maya-cluster`, carries no `provenance` and is tuple-identical
   (`.ufo/waves/round-88/followup/CB1.md` §4).

`{record_label}` is the existing provenance record path, e.g.
`entities[3].provenance[1]` for the `seal` item's second transfer.

## First-stop causes (delivered `2ea9ef1`)

Three item-level conditions are tested once, before the record loop
(`:183-189`); the rest are tested per record. Each is a literal `{cause}`
string, verbatim.

| # | Cause string | Trigger | Code |
|---|---|---|---|
| 1 | `source table unavailable` | `sources.json` missing or unparseable | `:184-185` |
| 2 | `provenance attached to a non-item entity` | `provenance` present on a non-`item` entity | `:186-187` |
| 3 | `duplicate item id {id!r}` | the item's own id appears more than once | `:188-189` |
| 4 | `malformed record (expected object)` | record is not a dict | `:201-206` |
| 5 | `malformed record (unexpected field set)` | record's key set ≠ `{tick, from_holder, to_holder, source_id}`; if the rejected dict also carries an ambiguous nonempty holder string the cause becomes `malformed record (unexpected field set); ambiguous holder identity {refs}` | `:208-234` |
| 6 | `malformed record (invalid tick)` | `tick` not a nonnegative `int` | `:243-246` |
| 7 | `malformed record (invalid from_holder)` | `from_holder` neither `null` nor a nonempty string | `:247-250` |
| 8 | `malformed record (invalid to_holder)` | `to_holder` not a nonempty string | `:251-254` |
| 9 | `dangling holder to_holder {id!r}` | `to_holder` absent from entities | `:255-258` |
| 10 | `dangling holder from_holder {id!r}` | `from_holder` absent from entities | `:267-270` |
| 11 | `ambiguous holder identity {refs}` | `to_holder` and/or `from_holder` matches ≥ 2 entity rows; `{refs}` is `to_holder 'x'`, `from_holder 'y'` joined `, ` in that field order | `:259-263`, `:271-281` |
| 12 | `malformed record (invalid source_id)` | `source_id` not a nonempty string | `:282-285` |
| 13 | `unknown source {id!r}` | `source_id` resolves to no source row | `:288-290` |
| 14 | `source table unavailable` | per-record source status is `unavailable` | `:291-293` |

## Decision table: reference state → output → next action

| Holder reference state | Output for that state (contract) | What the output does NOT say | Editor's safe action |
|---|---|---|---|
| Unique holder IDs; chain continuous; ticks strictly ascending | No holder findings; the item may contribute to `CLEAN` or unrelated findings elsewhere | Source text support, true custody, or canon — a citation resolves a fictional ID only (`corpus/fixtures/README.md:116-118`) | None on holders. |
| Unique holder IDs; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (delivered `:304-310`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE is a different mechanism from ambiguous holder identity and does NOT stop comparisons) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim; delivered evidence: `r87-chain-unique-broken` (1 violation), `r87-chain-unique-valid` (`CLEAN`) | Choose the editorially-intended field, edit, rerun. |
| Dangling holder, either field (`from_holder`/`to_holder` ID absent from entities) | Explicit `{record_label}.{from_holder|to_holder}: dangling entity {id!r}` (kept) PLUS `{record_label}: … remain unassessed … first stop: dangling holder {field} {id!r} at {record_label}` at that record and at every later record of the item | Ambiguity — nothing is duplicated; a dangling ID and an ambiguous ID are different states | Create or point to the intended single entity, rerun. No `ambiguous entity` line is owed. Delivered evidence: probes `F-dangling` / `O-dangling-from`, `r87-probe-record-and-chain` (`entities[3].provenance[6]`, `[7]`). |
| Ambiguous holder, either field (ID matches ≥ 2 entity rows) | Global duplicate `entities[j].id: duplicate entities id {id!r}` (kept) PLUS `{record_label}.{field}: ambiguous entity {id!r}` per ambiguous field PLUS the `… remain unassessed … first stop: ambiguous holder identity {refs} at {record_label}` disclosure at that record and at EVERY later record of the item. No definite chain-break or tick-order finding for that record or any later record of the item | A hidden break, a hidden clean result, or which duplicate row is "the real" vault. `r85-isolated-ambiguous` (internally consistent chain) and `r85-masked-ambiguous` (genuine downstream break) both hide the downstream state; delivered output differs only in how many records the disclosure names — 3 findings vs 4 — and the masked break stays unreported either way | Resolve identity (checklist below), rerun, review subsequent findings. |
| Ambiguity on a record that also fails the key-set check | `{record_label}: expected exactly tick, from_holder, to_holder, source_id` PLUS the local `ambiguous entity` line(s) PLUS the disclosure naming the combined cause `malformed record (unexpected field set); ambiguous holder identity {refs}` at that record and every later one | That the record was a usable provenance event, or that the shape violation alone caused the gap — both causes are named together, and neither is a lore fact | Repair the shape and the identity; rerun; treat the whole tail as unassessed until a clean comparison run. Delivered evidence: `r88-shape-ambiguous-armed`, `r87-probe-shape-ambiguous`. |
| A non-holder cause earlier in the item (unknown source, dangling holder, malformed record, duplicate item id, non-item, unavailable source table) | The disclosure names THAT cause, at the arming record and every later record. A different ambiguous holder introduced later still gets its own local `ambiguous entity` line but does not change the named cause | That the later ambiguity caused the earlier stop — the disclosure tracks the first stop, and later causes are not appended to it | Fix the named first cause first; rerun; then repair the later findings, which appear as their own `VIOLATION:` lines. Delivered evidence: `r88-mixed-stop` (unknown source at `[0]`, ambiguity at `[1]`), `r88-nonholder-stop`, probe `L-ambig-plus-unknownsrc`. |
| Two causes in one shape-valid record (e.g. bad tick AND ambiguous holder) | Every individual finding is emitted, but the named `first stop:` clause names only the FIRST check in precedence order — a bad tick masks a simultaneous ambiguity; an ambiguous holder masks a simultaneous unknown source | A complete list of the record's defects — the clause is an assessment-boundary statement, not a defect summary. Only the shape-invalid branch combines two cause phrases | Read the record's own `VIOLATION:` lines for the full defect list; repair them together. Delivered evidence: probes `J-tick-plus-ambiguity`, `L-ambig-plus-unknownsrc`. |
| Later valid records in an item whose chain is already unassessed | Ordinary record-level diagnostics continue (schema, keys, dangling-vs-unique identity, source status) PLUS the disclosure on each of them; continuity/tick comparisons do not run for the rest of the item, per run | Comparison passed — the repeated disclosure is not a new defect per record, and absence of comparison findings after the stop is NOT a pass | Repair the named first cause, rerun; the gate is per run, so a fresh run after repair can assess the full chain. |
| `provenance` present but not a list | `{item_label}.provenance: expected array` only — no disclosure is emitted for that item at all | That the (unreadable) contents would have been unassessed — the boundary is stated for the whole item instead | Repair the array shape; rerun. Delivered evidence: `r87-probe-entry-shape` (`entities[4].provenance: expected array`). |

## Editor checklist

1. Identify the holder: if output shows `…provenance[i].{field}: ambiguous
   entity 'x'`, find every `entities.json` row with id `x`. Neither the
   checker, the index, nor array order chooses a duplicate — same rule the
   lane already documents for source IDs (`corpus/fixtures/README.md:126-127`,
   "Both source rows remain untouched; array order does not choose one").
2. Read the `first stop:` clause before anything else. It names the actual
   reason comparisons stopped and where; if it is not a holder-ambiguity
   cause, do not start by deduping.
3. Resolve identity deliberately: rename the entity that should carry a
   different id, or merge the duplicate rows because they are one entity.
   Make only that structural choice; do not invent story facts, custody,
   or canon to justify the dedup. Do not delete records to silence a
   finding.
4. Rerun the same command against the same bible directory. Dedup is the
   prerequisite for detection, not the repair itself: the r85 sealed
   reviewer deduped on the masked output, believed the file had exactly one
   defect, and would have shipped the still-hidden chain break; only the
   rerun surfaces it verbatim (`reports/round-85/r85-sealed-reviewer.md`,
   Step 3; `reports/round-85/r85-axis-adjudicator.md`, "Bounds on the gain").
5. Review subsequent findings: new `provenance chain break` /
   `provenance tick` lines that appear AFTER your repair are comparisons
   now running, not regressions. Address them one at a time, rerunning
   after each repair.
6. Stop decision: stop only when a rerun exits 0 (`CLEAN`) or every finding
   is repaired or deliberately editorially accepted. A violation count —
   even `1 violation(s)` — does not mean "exactly one defect." Every record
   at or after the first stop carries its own
   `… remain unassessed (input-structural finding, not sourced-canon);
   first stop: …` disclosure, so one stop adds one line per later record;
   that repetition is one open item, never a pass, and never proof of a
   break.

## Precise limits of the disclosure

- Scope: exactly two assessments stop — provenance continuity (next
  `from_holder` equals previous `to_holder`; first record `from_holder`
  null) and tick order (strict increase) — at the first stop and ALL later
  records of that item. The stop is permanent for that run; no later valid
  record re-enables it (baseline `:234-237`, `:246-247`; preserved by the
  contract; delivered latch `:296-302`, comparison gate `:303`).
- One form, one boundary: the disclosure states the local status and the
  first stop on every affected record. It is not a finding about the chain —
  it reports that the comparison did not run. There is no separate item-level
  notice at `2ea9ef1`.
- Cause precedence inside a shape-valid record (first failing check wins, and
  later causes are NOT appended to the clause): `malformed record (invalid
  tick)` → `malformed record (invalid from_holder)` → `malformed record
  (invalid to_holder)` → `dangling holder to_holder` → `dangling holder
  from_holder` → `ambiguous holder identity` → `malformed record (invalid
  source_id)` → `unknown source` → `source table unavailable`. The only
  combined clause is the shape-invalid one, item 5 of the cause table.
- Emission order is asymmetric: on the record that arms the stop the
  disclosure is appended after that record's own findings (`:206`, `:233`,
  `:300-301`); on every later record it is emitted at the top of the record
  loop, before them (`:198-200`).
- Item-level causes outrank record causes: `source table unavailable`,
  `provenance attached to a non-item entity`, and `duplicate item id` are
  evaluated once before the loop, so an item whose provenance sits on a
  character entity is disclosed as `provenance attached to a non-item
  entity` even when its records also carry dangling holders and unknown
  sources (`r61-independent-empty`, `r61-independent-unavailable`).
- A duplicated item id arms a separate stop on each duplicate row, each
  naming its own origin (`entities[3].provenance` and
  `entities[4].provenance`; probe `C-dupitemid`, `r87-probe-entry-shape`).
- Everything else continues: JSON loading, field schema, key-set checks,
  holder shape validation, dangling-vs-duplicate classification, source
  citation status, global duplicate-ID findings, and all relation,
  timeline, and contradiction checks.
- Three states, not two: after the stop the affected comparisons are
  UNASSESSED — neither clean nor broken. Output alone cannot tell you
  whether the masked tail contains a break; only resolving the named cause
  and rerunning can. Do not resume, infer, or announce a break from the
  stopped input itself.
- No truth claims: nothing here asserts a hidden break, true custody,
  entity identity, canon, source-text support, rights, or game mechanics.
  The disclosure is about the checker's assessment boundary, not the
  fictional world. Probe fixtures are authored inputs; chain breaks inside
  them are injected test scaffolding, not lore.
- Ambiguous SOURCE is not a stop cause. A source ID resolving to ≥ 2 rows
  sets `chain_has_ambiguous_source` (`:294-295`) and only prefixes
  comparison findings with `input-structural finding, not sourced-canon; `;
  comparisons still run (`r7-item-ambiguous`, `r87-probe-source-prefix`).
- Chain eligibility is no longer orthogonal to the disclosure: the three
  conditions that used to disable the chain silently (no sources,
  non-item entity, duplicated item id) are now named first stops
  (`:183-189`). Comparisons require sources loaded, `kind == "item"`, and a
  unique item id — unchanged (`:183` baseline; delivered `:183-189`) — but a
  chain that was never eligible now says so per record instead of staying
  silent.
- Measurement ceiling: `score = 2 × passed` on the five-gate disclosure
  sample; 10/10 means 5/5 specified gates passed. It is not whole-domain
  calibration, not saturation, not promotion, and not evidence that an
  external reader changed behavior. No such score exists for `2ea9ef1`:
  the helper is absent there.

## Commands (self-contained, run from the lane root)

Delivered replay — the five recorded r85 probe inputs against the checker at
`2ea9ef1` (run from the lane root; baseline triples for the same five inputs
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
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
4 violation(s); no canon changed
[rc=1]
=== r85-isolated-ambiguous ===
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[2]
3 violation(s); no canon changed
[rc=1]
=== r85-harbor-repro ===
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
6 violation(s); no canon changed
[rc=1]
```

Against the pinned baseline this is 1 → 4 findings on `r85-masked-ambiguous`,
1 → 3 on `r85-isolated-ambiguous`, and 2 → 6 on `r85-harbor-repro`; the
control and the unique-holder break case are unchanged. Every baseline line
survives verbatim. The two in-tree direction fixtures replay symmetrically —
`python3 corpus/fixtures/check_bible.py
corpus/fixtures/r87-masked-break-from-ambiguous` gives `5 violation(s)` with
`first stop: ambiguous holder identity from_holder 'dup' at
entities[3].provenance[0]` on records [0], [1], and [2], and
`…r87-masked-break-to-ambiguous` gives the same shape with `to_holder`.

Durable fixtures for the non-holder causes, with their delivered output:

```sh
for f in r88-mixed-stop r88-nonholder-stop r88-shape-ambiguous-armed; do
  echo "=== $f ==="; python3 corpus/fixtures/check_bible.py corpus/fixtures/$f; echo "[rc=$?]"
done
```

```text
=== r88-mixed-stop ===
VIOLATION: entities[1].id: duplicate entities id 'f1-mixed-dup'
VIOLATION: entities[5].provenance[0].source_id: unknown in-world source 'f1-mixed-missing-source'
VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
VIOLATION: entities[5].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
6 violation(s); no canon changed
[rc=1]
=== r88-nonholder-stop ===
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'f1-nonholder-missing-source'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
4 violation(s); no canon changed
[rc=1]
=== r88-shape-ambiguous-armed ===
VIOLATION: entities[1].id: duplicate entities id 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
VIOLATION: entities[4].provenance[0].to_holder: ambiguous entity 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
5 violation(s); no canon changed
[rc=1]
```

The remaining cause families and the precedence pairs are verified by CB1's
scratch probes only (`/tmp/cb1/probes2`, `/tmp/cb1/probes3`; exact commands
and output in `.ufo/waves/round-88/followup/CB1.md` §3) — dangling
`to_holder`/`from_holder`, non-dict record, invalid tick, both-fields
ambiguity at one record, non-item provenance, duplicate item id, unavailable
source table, and the tick-masks-ambiguity / ambiguity-masks-unknown-source
pairs have no durable fixture in the tree yet.

Five-gate measurement entry point (clean chain; unique-holder real break;
dangling-holder explicitness both fields; ambiguous-to local disclosure plus
downstream scope/no definite comparisons; ambiguous-from symmetric behavior;
JSON with `measured_revision`, `total=5`, `passed`, `score=2*passed`, raw
returncode/stdout/stderr per case; tests the requested revision's checker AND
input data in isolated temporary trees):

```sh
python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>
```

That helper does not exist at `2ea9ef1` — `python3
corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
`can't open file ... No such file or directory` — so no five-gate score is
recorded for this tree. Run the helper only in a revision that contains it;
until then the delivered replays above are the behavioral evidence.

## Evidence and citations

- Checker at baseline `5eb9451`: `corpus/fixtures/check_bible.py` — holder
  count collection `:157-159`; dangling diagnostics `:212-214` (to) and
  `:220-222` (from); silent ambiguity branches `:215-216` and `:223-224`;
  permanent latch `:234-237`; comparison gate `:238-245`; no-resume
  previous-value update `:246-247`; relation-endpoint ambiguity precedent
  `:168`; CLI/exit behavior `:320-330`. These are the line refs the
  baseline paragraph of "The contract" cites.
- Checker at delivered `2ea9ef1` (`corpus/fixtures/check_bible.py`, 395
  lines, sha256 `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`):
  holder count collection `:157-159`; relation-endpoint ambiguity precedent
  `:168`; provenance loop `:171-312`; `only valid on item entities` `:177`;
  `expected array` + `continue` `:178-180`; item-level first-stop tests
  `:183-189`; disclosure template `:192-194`; top-of-loop emission
  `:198-200`; non-dict branch `:201-207`; key-set branch with the
  shape-invalid holder scan and combined cause `:208-234`; field validation
  and cause precedence `:239-295`; latch `:296-302`; comparison gate
  `:303-312`; CLI/exit behavior `:385-395`.
- Round-88 evidence: `.ufo/waves/round-88/followup/CB1.md` (drift inventory
  D1-D21, cause/precedence/emission-order probes, 149-directory preservation
  census, fixture inventory re-measurement) and the work-wave seat reports
  `.ufo/waves/round-88/X1.md` (primary implementer),
  `X3.md` (first-cause-only alternative), `X4.md` (rejected-record semantics
  challenger), `F1.md` (durable fixtures), with patches under
  `.ufo/waves/round-88/patches/`.
- Round-87 evidence (superseded behavior; kept for history):
  `.ufo/waves/round-87/followup/I2.md` (delivered-tree replay at `2b48ca7`,
  133-directory preservation check, census, scratch boundary probes
  `p1`-`p8`). `.ufo/waves/round-87/CB1.md` is a different artifact from the
  round-88 `CB1.md` despite the shared seat id: the round-87 file is a
  pre-C1 replay of the five probes at `28706dc`.
- Probe inputs: `corpus/live/runs/round-85/probe-inputs/{r85-control,
  r85-unique-break-control,r85-masked-ambiguous,r85-isolated-ambiguous,r85-harbor-repro}/`
  — masked `entities.json:49-93` and unique-control `entities.json:49-81`
  carry identical transfers `(null→mira,0)`, `(mira→vault,3)`,
  `(harbor→tower,4)`; masked adds a second `vault` row. Isolated carries a
  continuous chain ending in the duplicated `vault` at record `[2]`.
- In-tree provenance fixtures at `2ea9ef1`: 19 directories carry
  `provenance`; 11 provenance records across eight of them reference a
  duplicated holder id — `r87-masked-break-from-ambiguous`,
  `r87-masked-break-to-ambiguous`, `r87-probe-multi-invalid`,
  `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain`,
  `r87-probe-shape-ambiguous`, `r88-mixed-stop`,
  `r88-shape-ambiguous-armed` (plus the r85 live probes outside
  `corpus/fixtures`). `r7-item-ambiguous` is ambiguous SOURCE only;
  `r61-*` are dangling holders on a non-item entity. Measured by
  `.ufo/waves/round-88/followup/CB1.md` §5.
- Round-85 reports: `reports/round-85/r85-author.md` (probe design,
  `:38-75`), `r85-verifier.md`, `r85-sealed-reviewer.md` (operative danger:
  correct first action, false sense of finality),
  `r85-axis-adjudicator.md` (verdict ADMIT, bounded; repair reserved as a
  separate candidate needing tuple replay).
- Fleet round-1 evidence: `reports/round-1/current-baseline.json` and
  `reports/round-1/baseline-probes.json` (parent-recorded CLI triples at
  `5eb9451`; all recorded stderr empty); `reports/round-1/critic.md`
  (counterexample table this guidance encodes);
  `reports/round-1/current-dispatch.json` (seat write scopes — seat
  `R1Guide` holds the scope for this file).
- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline,
  no inferred history, citation ≠ support) and `:121-128` (round-7
  duplicate-source rule mirrored by this holder contract). The README has no
  `## Round 88` section, so this document is the only in-tree statement of
  the delivered provenance behavior.
- Lane declaration: `SCORECARD.md` fleet-round-1 calibration declaration
  (unmeasured tie, falsifiability tie-break).

## Status split

- OBSERVED on the delivered tree (round-88 seat CB1, `2ea9ef1`; exact
  commands and output in "Commands" and
  `.ufo/waves/round-88/followup/CB1.md`): the five r85 probe triples pasted
  above; the three r88 durable fixtures pasted above; the 149-directory
  preservation census (0 exit changes, 0 stderr changes, 12 changed stdout
  tuples); the 19-directory provenance inventory with 11 duplicated-holder
  records.
- OBSERVED only in scratch probes at `2ea9ef1` (no durable fixture): the
  cause strings for dangling `to_holder`/`from_holder`, non-dict record,
  invalid tick, both-fields ambiguity at one record, non-item provenance,
  duplicate item id, unavailable source table; and the cause-precedence pairs
  (tick masks ambiguity; ambiguity masks unknown source). Command form and
  output in `.ufo/waves/round-88/followup/CB1.md` §3.
- OBSERVED at baseline `5eb9451` (parent-recorded JSON): masked and
  isolated emitted ONLY the global duplicate; unique control emitted the
  definite record-2 break; control was CLEAN; harbor-repro showed
  timeline-endpoint ambiguity voiced while holder references stayed
  silent.
- SUPERSEDED: the r87 two-notice contract (`2b48ca7`) and its replay block;
  preserved in `.ufo/waves/round-87/followup/I2.md` and
  `corpus/knowledge/r87-provenance-chain-decision-table.md`. The latter still
  quotes both removed notice strings (`:54`, `:55`, `:93`, `:163`, `:164`,
  `:173`, `:210`) and is not marked as historical anywhere in the tree.
- REPLAYED, not scored: no five-gate `passed` count exists for `2ea9ef1`;
  the documented helper is absent at that revision.
- UNKNOWN / UNMEASURED: whether any fixture outside the 19 listed above
  combines `provenance` with a duplicated holder id (none does in
  `corpus/fixtures`); any external reader behavior change.

## Measured results (parent-owned slot)

No five-gate score is recorded for the delivered tree `2ea9ef1`: the
documented measurement helper is absent at that revision. The behavioral
replay that stands in for it is the five-case delivered output pasted under
"Commands", the three durable r88 fixture outputs pasted there, and CB1's
scratch cause/precedence probes recorded in
`.ufo/waves/round-88/followup/CB1.md`; every contract, table, and limits line
above is stated as-of that replay.
