# Holder-assessment boundary: reading provenance ambiguity disclosures

<!-- Reconstructed at round-91 integration from seat CB1's r90 section-replacement
     instructions (D1-D13) applied to the r89-landed contract (e97613c); replaces the
     mis-landed instruction sheet from the r90 closure (defect found by CB1, round 91).
     Skipped as named debt: D1 — Decision-table row 2 code refs. -->

# Holder-assessment boundary: reading provenance ambiguity disclosures
<!-- Refreshed at round-89 closure from seat CB1's verified proposal
     (.ufo/waves/round-89/followup/CB1-boundary-refresh.md) with seat E1's
     corrections applied; every anchor and pasted output re-derived from the
     delivered tree at 1b09f3f (checker e2bb9639). -->

> **Landed at round-89 closure** (replacing the r88-closure version). Drift inventory:
> `.ufo/waves/round-89/followup/CB1.md` (CB1-R1…R19); corrections per
> `.ufo/waves/round-89/followup/E1-boundary-update-proposal.md` §F applied.

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
(commit `03c6746`, delivered tree `2b48ca7`); round-88 seat C1 replaced the
holder-only latch with permanent first-stop cause tracking and armed the stop
from shape-invalid records (integrated in `2ea9ef1`); round-89 seat X1 added the multi-cause summary, the raw-vs-resolved-index cause wording,
and the not-uniquely-resolvable qualification of comparison findings (integrated in
`1b09f3f`); round-90 composed seat X2's null guard — a null holder field never produces an
identity clause — with seat X3's integer-only tick reading per seat C9's ruling: tick order
is an integer comparison and holder-identity uncertainty does not qualify it, while genuinely
unresolved non-null holder identities still qualify chain-continuity and first-record
findings (integrated in `ca7f9ef`, checker `ff9fd2aa`). This revision was rewritten by
round-90 seat CB1 against the delivered checker at `ca7f9ef`
(`.ufo/waves/round-90/followup/CB1.md`)
delivered checker at `1b09f3f`
(`.ufo/waves/round-89/followup/CB1.md`); the r88 contract, decision table,
limits, and status sections it replaces are superseded, and the r87 replay
evidence at `2b48ca7` is preserved only in
`.ufo/waves/round-87/followup/I2.md`.

verified-at: RUNTIME REPLAYED on the delivered tree at `1b09f3f` by round-89
seat CB1; exact commands and observed output are pasted under "Commands" and
in `.ufo/waves/round-89/followup/CB1.md`. The single `remain unassessed …
first stop:` disclosure form, every named first-stop cause (including both
raw-vs-resolved wordings), the multi-cause joining rule, the qualified
verified-at: RUNTIME REPLAYED on the delivered tree at `ca7f9ef` by round-90 seat CB1;
exact commands and observed output are pasted under "Commands" and in
`.ufo/waves/round-90/followup/CB1.md`. All fourteen pasted case blocks below replay
byte-identically through the delivered checker. The single `remain unassessed … first stop:`
disclosure form, every named first-stop cause (including both raw-vs-resolved wordings), the
multi-cause joining rule, the qualified chain-comparison forms, and the emission-order
asymmetry below are demonstrated by that replay, not contract text. This verifies the listed
checker behavior only; it is not a five-gate score and not a claim about fictional truth. The
baseline (`5eb9451`) triples remain as recorded in `reports/round-1/current-baseline.json`
and `reports/round-1/baseline-probes.json`.
`remain unassessed` template string or any named first-stop cause changes,
Re-verify whenever the provenance branch of `corpus/fixtures/check_bible.py` changes — in
particular the comparison gate (`:322`) and its branches, chain continuity (`:327-337`) and
tick order (`:323-326`) — whenever the `remain unassessed` template string or any named
first-stop cause changes, whenever the raw entity/source counters, the `is not uniquely
resolvable` detail string, the null guard in `holder_identity_detail` (`:169-170`), or the
`; ` cause-joining rule changes, or whenever any `corpus/live/runs/round-85/probe-inputs/`
JSON byte changes.
the chain gate `can_check_chain = False` for that item, and the ONLY output
is the global `entities[j].id: duplicate entities id {id!r}` finding — the
ambiguous reference itself gets no line, and continuity plus tick-order
comparisons silently stop at that record and every later record of that
item (`reports/round-1/current-baseline.json` cases
`r85-masked-ambiguous` / `r85-isolated-ambiguous`; mechanism at
`corpus/fixtures/check_bible.py:212-224` silent/dangling branches,
`:234-237` permanent latch, `:238-245` both comparisons inside one gate,
`:246-247` later valid records do not re-enable it; baseline line refs,
re-checked against `git show 5eb9451:corpus/fixtures/check_bible.py`).

The delivered checker (`1b09f3f`) replaces the holder-only latch with a
permanent first-stop cause record:

1. **One disclosure form, one line per affected record.** A single template,
   verbatim (delivered `:206-208`):

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
   is every stop condition the checker reached at that record, in check order,
   joined with `; ` (`:313-316`). `{origin_label}` is the record label that
   armed it (`entities[3].provenance[1]`) or, for the three item-level
   conditions, the item label (`entities[3].provenance`). Ambiguous holder
   identity is one cause among several, not the only one.

3. **Local `ambiguous entity` lines are unchanged in shape.** Both ambiguous
   holder references get
   `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}` and the
   record remains invalid (mirrors the relation-endpoint format at
   `check_bible.py:182`; delivered `:275` for `to_holder`, `:288` for
   `from_holder`). Several references at one record are joined by `, ` in the
   order `to_holder` then `from_holder` (`:292-297`).

4. **A shape-invalid dict record can arm the stop.** When a record fails the
   exact-key-set check, the checker still inspects its nonempty string
   `to_holder` / `from_holder` values for duplicated entity IDs
   (`:225-233`): each ambiguous field gets its own local `ambiguous entity`
   line, and — absent an earlier stop — the cause entry becomes
   `malformed record (unexpected field set); ambiguous holder identity {refs}`
   (`:236-244`). A non-dict record cannot arm a holder-ambiguity cause: it
   hits `malformed record (expected object)` first (`:215-221`).

5. **The conservative permanent latch is preserved.** Comparisons do not
   resume within the run, and no break is inferred from ambiguity. All old
   diagnostics, exit behavior (`VIOLATION:` lines, `N violation(s); no canon
   changed`, `CLEAN: schema, citations, relations, timeline; 0 violations`),
   the comparison state machine, and every existing fictional JSON byte are
Round-90 verification (seat CB1, `ca7f9ef`): the r89 checker (`e2bb9639`) and the delivered
checker (`ff9fd2aa`), run against the same 160 fixture directories, produced 0 exit-code
changes, 0 stderr changes, and 0 changed stdout tuples; four new directories
(`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
`r90-c1-three-causes`) were added in the same commit, making 164 fixture directories
(B1's 160-row tuple receipt replayed, 0 mismatches).
   (`:82-83`, `:85-91`, `:97`). Cause wording distinguishes "no raw row at
   all" from "raw rows exist but none reaches the resolved index" (items 9,
   10, 13 of the cause table).

`{record_label}` is the existing provenance record path, e.g.
`entities[3].provenance[1]` for the `seal` item's second transfer.

## First-stop causes (delivered `1b09f3f`)

Three item-level conditions are tested once, before the record loop
(`:198-203`); the rest are tested per record. Each is a literal cause entry,
verbatim. `{raw_presence}` is `present in raw entities but` when the raw
entity counter for the id is nonzero, otherwise `absent from raw entities and`
(`:272`, `:285`); the source form uses `raw sources` (`:306`).

| # | Cause string | Trigger | Code |
|---|---|---|---|
| 1 | `source table unavailable` | `sources.json` missing or unparseable | `:198-199` |
| 2 | `provenance attached to a non-item entity` | `provenance` present on a non-`item` entity | `:200-201` |
| 3 | `duplicate item id {id!r}` | the item's own id appears more than once | `:202-203` |
| 4 | `malformed record (expected object)` | record is not a dict | `:215-221` |
| 5 | `malformed record (unexpected field set)` | record's key set ≠ `{tick, from_holder, to_holder, source_id}`; if the rejected dict also carries an ambiguous nonempty holder string the entry becomes `malformed record (unexpected field set); ambiguous holder identity {refs}` | `:222-248` |
| 6 | `malformed record (invalid tick)` | `tick` not a nonnegative `int` | `:257-260` |
| 7 | `malformed record (invalid from_holder)` | `from_holder` neither `null` nor a nonempty string | `:261-264` |
| 8 | `malformed record (invalid to_holder)` | `to_holder` not a nonempty string | `:265-268` |
| 9 | `holder reference to_holder {id!r} {raw_presence} absent from the resolved index` | `to_holder` resolves to no entity in the resolved index; `{raw_presence}` says whether any raw entity row carries the id | `:269-273` |
| 10 | `holder reference from_holder {id!r} {raw_presence} absent from the resolved index` | same for `from_holder` | `:279-286` |
| 11 | `ambiguous holder identity {refs}` | `to_holder` and/or `from_holder` matches ≥ 2 entity rows in the resolved index; `{refs}` is `to_holder 'x'`, `from_holder 'y'` joined `, ` in that field order | `:274-278`, `:287-297` |
| 12 | `malformed record (invalid source_id)` | `source_id` not a nonempty string | `:298-301` |
| 13 | `source reference {id!r} {raw_presence} absent from the resolved index` | `source_id` resolves to no source row; `{raw_presence}` is `present in raw sources but` / `absent from raw sources and` | `:302-307` |
| 14 | `source table unavailable` | per-record source status is `unavailable` | `:308-310` |

**Several causes can be named at once.** Every cause the record reached is
appended to a list in check order and the whole list is joined with `; ` when
the record is the arming record (`:256`, `:313-316`). Order is still the order
of the checks, and item-level causes (rows 1-3) still pre-empt the record loop
entirely, so a row-1..3 item shows exactly one cause. The shape-invalid entry
(row 5) is one such entry, not a special case: it is itself a combined string,
and it can be followed by further entries only when it is the arming record —
which it always is, since a key-set failure ends the record.

## Decision table: reference state → output → next action

| Holder reference state | Output for that state (contract) | What the output does NOT say | Editor's safe action |
|---|---|---|---|
| Unique holder IDs; chain continuous; ticks strictly ascending | No holder findings; the item may contribute to `CLEAN` or unrelated findings elsewhere | Source text support, true custody, or canon — a citation resolves a fictional ID only (`corpus/fixtures/README.md:116-118`) | None on holders. |
| Holder IDs each uniquely resolvable in the raw table and the resolved index; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (delivered `:343-344`, `:349-350`, `:333`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE is a different mechanism from ambiguous holder identity and does NOT stop comparisons) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim; delivered evidence: `r87-chain-unique-broken` (1 violation), `r87-chain-unique-valid` (`CLEAN`), `r89-fn2-control` | Choose the editorially-intended field, edit, rerun. |
| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | The comparison still runs, but every finding that involves that ID is qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and for ticks `{record_label}.tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: {details}; provenance tick {…} must be greater than previous tick {…}` (`:327-333`, `:334-344`, `:345-350`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:168-173`) | That the chain is definitely broken, or definitely intact — the expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the comparison as a definite finding. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control). |
| Dangling holder, either field (the ID resolves to no entity in the resolved index) | Explicit `{record_label}.{from_holder|to_holder}: dangling entity {id!r}` (kept) PLUS `{record_label}: … remain unassessed … first stop: holder reference {field} {id!r} {raw_presence} absent from the resolved index at {record_label}` at that record and at every later record of the item | Ambiguity — nothing is duplicated; a dangling ID and an ambiguous ID are different states. The clause does not say "unknown": a raw row may exist and have been rejected by the field check | Create or point to the intended single entity, rerun. If the clause says `present in raw entities but`, the row exists but fails validation — repair that row rather than inventing an entity. No `ambiguous entity` line is owed. Delivered evidence: `r89-f2-dangling-to`, `r89-f2-dangling-from`, `r87-probe-record-and-chain` (`entities[3].provenance[6]`, `[7]`). |
| Ambiguous holder, either field (ID matches ≥ 2 entity rows in the resolved index) | Global duplicate `entities[j].id: duplicate entities id {id!r}` (kept) PLUS `{record_label}.{field}: ambiguous entity {id!r}` per ambiguous field PLUS the `… remain unassessed … first stop: ambiguous holder identity {refs} at {record_label}` disclosure at that record and at EVERY later record of the item. No definite chain-break or tick-order finding for that record or any later record of the item | A hidden break, a hidden clean result, or which duplicate row is "the real" vault. `r85-isolated-ambiguous` (internally consistent chain) and `r85-masked-ambiguous` (genuine downstream break) both hide the downstream state; delivered output differs only in how many records the disclosure names — 3 findings vs 4 — and the masked break stays unreported either way | Resolve identity (checklist below), rerun, review subsequent findings. |
| Ambiguity on a record that also fails the key-set check | `{record_label}: expected exactly tick, from_holder, to_holder, source_id` PLUS the local `ambiguous entity` line(s) PLUS the disclosure naming the combined cause `malformed record (unexpected field set); ambiguous holder identity {refs}` at that record and every later one | That the record was a usable provenance event, or that the shape violation alone caused the gap — both causes are named together, and neither is a lore fact | Repair the shape and the identity; rerun; treat the whole tail as unassessed until a clean comparison run. Delivered evidence: `r88-shape-ambiguous-armed`, `r87-probe-shape-ambiguous`. |
| A non-holder cause earlier in the item (dangling holder, unknown source, malformed record, duplicate item id, non-item, unavailable source table) | The disclosure names THAT cause, at the arming record and every later record. A different ambiguous holder introduced later still gets its own local `ambiguous entity` line but does not change the named cause | That the later ambiguity caused the earlier stop — the disclosure tracks the first stop, and later causes at *later* records are not appended to it (causes at the *same* record are: see the next row) | Fix the named first cause first; rerun; then repair the later findings, which appear as their own `VIOLATION:` lines. Delivered evidence: `r88-mixed-stop` (unknown source at `[0]`, ambiguity at `[1]`), `r88-nonholder-stop`. |
| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | Chain-continuity and first-record findings that involve that ID are qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and the first-record form `… possible provenance chain break, not a definite identity mismatch: {detail}; first record must have from_holder null` (`:330-335`, `:339-341`). Tick findings are NOT qualified: `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` with no identity note (`:323-326`). A null holder field contributes no clause and never triggers qualification (`:169-170`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:171-175`) | That the chain is definitely broken, or definitely intact — the chain finding's expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It does not make tick order, an integer comparison, uncertain. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the chain comparison as a definite finding. A tick line already reads as definite while the duplicate remains. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control); CB1's round-90 edge probe adds observed-side, null-observed/expected-unresolved, and unqualified-tick receipts (`CB1.md`) |
| Later valid records in an item whose chain is already unassessed | Ordinary record-level diagnostics continue (schema, keys, dangling-vs-unique identity, source status) PLUS the disclosure on each of them; continuity/tick comparisons do not run for the rest of the item, per run | Comparison passed — the repeated disclosure is not a new defect per record, and absence of comparison findings after the stop is NOT a pass | Repair the named first cause, rerun; the gate is per run, so a fresh run after repair can assess the full chain. |
| `provenance` present but not a list | `{item_label}.provenance: expected array` only — no disclosure is emitted for that item at all | That the (unreadable) contents would have been unassessed — the boundary is stated for the whole item instead | Repair the array shape; rerun. Delivered evidence: `r87-probe-entry-shape` (`entities[4].provenance: expected array`). |

## Editor checklist

1. Identify the holder: if output shows `…provenance[i].{field}: ambiguous
   entity 'x'`, find every `entities.json` row with id `x`. Neither the
   checker, the index, nor array order chooses a duplicate — same rule the
   lane already documents for source IDs (`corpus/fixtures/README.md:126-127`,
   "Both source rows remain untouched; array order does not choose one").
2. Read the `first stop:` clause before anything else. It names the actual
   reason comparisons stopped and where, and it may name several causes at
   once, joined with `; `. If no listed cause is a holder-ambiguity cause, do
   not start by deduping.
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
   now running, not regressions. A `possible provenance chain break, not a
   definite identity mismatch` line means a second, unresolved duplicate is
   still in play — repair that one before reading the comparison as final.
   Address them one at a time, rerunning after each repair.
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
- Comparison findings can be non-definite, but only for holder-identity comparisons. When a
  **non-null** holder id involved in a chain-continuity or first-record comparison has ≥ 2 raw
  entity rows of which exactly one is in the resolved index, the finding is rewritten as
  `input-structural finding, not sourced-canon; possible provenance chain break, not a
  definite identity mismatch: …` or, for the first record, `… : {detail}; first record must
  have from_holder null` (`:330-335`, `:339-341`). The expected and the observed side are both
  tested and either can trigger it (`:328-329`, `:339`); a `None` side contributes no clause
  (`:169-170`). Tick comparisons are not in this class: strict tick order is decided by the
  two validated integer tick values, so an unresolved holder id cannot qualify it — the only
  tick prefix comes from an independently ambiguous source citation (`:323-326`; seat C9's
  round-90 ruling). A plain duplicate whose rows both pass validation cannot reach a
  comparison at all: it makes the referencing record ambiguous and therefore invalid, which
  stops the chain instead.
are pinned in `reports/round-1/current-baseline.json`):

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
```

Observed output (verbatim; stderr empty in all five; byte-identical to the
r88 replay, so this block did not change with the r89 amendments):

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

Durable fixtures for the non-holder and raw-vs-resolved causes, with their
delivered output:

```sh
for f in r88-mixed-stop r88-nonholder-stop r88-shape-ambiguous-armed r89-f2-dangling-to r89-f2-dangling-from r89-f2-invalid-source-id; do
  echo "=== $f ==="; python3 corpus/fixtures/check_bible.py corpus/fixtures/$f; echo "[rc=$?]"
done
```

```text
=== r88-mixed-stop ===
VIOLATION: entities[1].id: duplicate entities id 'f1-mixed-dup'
VIOLATION: entities[5].provenance[0].source_id: unknown in-world source 'f1-mixed-missing-source'
VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-mixed-missing-source' absent from raw sources and absent from the resolved index at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-mixed-missing-source' absent from raw sources and absent from the resolved index at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
VIOLATION: entities[5].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-mixed-missing-source' absent from raw sources and absent from the resolved index at entities[5].provenance[0]
6 violation(s); no canon changed
[rc=1]
=== r88-nonholder-stop ===
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'f1-nonholder-missing-source'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-nonholder-missing-source' absent from raw sources and absent from the resolved index at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-nonholder-missing-source' absent from raw sources and absent from the resolved index at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'f1-nonholder-missing-source' absent from raw sources and absent from the resolved index at entities[3].provenance[0]
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
=== r89-f2-dangling-to ===
VIOLATION: entities[3].provenance[1].to_holder: dangling entity 'r89-f2-missing-to'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[3]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
4 violation(s); no canon changed
[rc=1]
=== r89-f2-dangling-from ===
VIOLATION: entities[3].provenance[1].from_holder: dangling entity 'r89-f2-missing-from'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[3]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
4 violation(s); no canon changed
[rc=1]
=== r89-f2-invalid-source-id ===
VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'r89-f2-unknown-source'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index at entities[3].provenance[1]
VIOLATION: entities[3].provenance[3]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index at entities[3].provenance[1]
4 violation(s); no canon changed
[rc=1]
```

Multi-cause summary and the FN-2 pair, with their delivered output:

```sh
for f in r89-c1-multi-cause-valid r89-fn2-unresolved-chain-break r89-fn2-control; do
  echo "=== $f ==="; python3 corpus/fixtures/check_bible.py corpus/fixtures/$f; echo "[rc=$?]"
done
```

```text
=== r89-c1-multi-cause-valid ===
VIOLATION: entities[1].id: duplicate entities id 'r89-c1-multi-cause-valid-ambiguous-holder'
VIOLATION: entities[2].provenance[0].tick: required nonnegative integer
VIOLATION: entities[2].provenance[0].to_holder: ambiguous entity 'r89-c1-multi-cause-valid-ambiguous-holder'
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder' at entities[2].provenance[0]
4 violation(s); no canon changed
[rc=1]
=== r89-fn2-unresolved-chain-break ===
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
2 violation(s); no canon changed
[rc=1]
=== r89-fn2-control ===
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
1 violation(s); no canon changed
[rc=1]
```

The six single-cause branches without their own durable fixture each have one
now, and replay as one cause plus one disclosure per affected record:
`r89-c1-invalid-tick` (`first stop: malformed record (invalid tick) at
entities[3].provenance[1]`, 4 violations), `r89-c1-invalid-from-holder` (3),
`r89-c1-invalid-to-holder` (3), `r89-c1-malformed-source-id`
The six single-cause branches without their own durable fixture each have one now, and replay
as one cause plus one disclosure per affected record: `r89-c1-invalid-tick` (`first stop:
malformed record (invalid tick) at entities[3].provenance[1]`, 4 violations),
`r89-c1-invalid-from-holder` (3), `r89-c1-invalid-to-holder` (3), `r89-c1-malformed-source-id`
(`entities[2].provenance[1]`, 3). Round-90 added durable fixtures for the two `present in raw …
but absent from the resolved index` wordings (`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`,
`r90-c1-rawpresent-source`) and for a three-cause valid-key record (`r90-c1-three-causes`,
`malformed record (invalid tick); holder reference to_holder … ; source reference …`); their
delivered output is pasted in the r90 work wave (`.ufo/waves/round-90/F1.md`) and replayed by
CB1 at `ca7f9ef`. Still scratch-only, with no durable fixture in the tree: the observed-side and
first-record FN-2 chain forms, and the null-chain definite form. The tick-under-unresolved-holder
FN-2 sub-branch no longer exists — r90's integer-only tick reading removed it (seat C9's ruling);
its would-be fixture was never built and is not owed. Evidence for the remaining shapes is
CB1's round-90 edge probe (`/__cb1_probe__`, receipts in
`.ufo/waves/round-90/followup/CB1.md`) and the r90 seats' probes (B3, C5, C9). Round-88's
scratch evidence for the remaining families (non-dict record, non-item provenance, duplicate
item id, unavailable source table, both-fields ambiguity at one record, tick-masks-ambiguity) is
recorded in `/tmp/cb1/probes2`, `/tmp/cb1/probes3` and
`.ufo/waves/round-88/followup/CB1.md` §3; note that `/tmp` reached inode exhaustion on
2026-10-17, so that scratch may not survive.
returncode/stdout/stderr per case; tests the requested revision's checker AND
input data in isolated temporary trees):

```sh
python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>
```

That helper does not exist at `1b09f3f` — `python3
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
  baseline paragraph of "The contract" cites; re-checked against
  `git show 5eb9451:corpus/fixtures/check_bible.py` (330 lines) by round-89
  seat CB1.
- Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435
  lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
  raw entity/source counters declared `:38-39`, accumulated `:72-76`;
  schema-valid rows collected `:82-83`; `index()` `:85-91`; sources index
  `:93`; entities index `:97`; holder count collection `:164-166`;
  `holder_identity_detail` `:168-173`; relation-endpoint ambiguity
  precedent `:182`; provenance loop `:185-352`; `only valid on item
  entities` `:191`; `expected array` + `continue` `:192-194`; item-level
  first-stop tests `:198-203`; disclosure template `:206-208`; top-of-loop
  emission `:212-214`; non-dict branch `:215-221`; key-set branch with the
  shape-invalid holder scan and combined cause `:222-248`; field validation
  and cause collection `:249-312`; latch `:313-319`; comparison gate and
  FN-2 qualification `:320-352`; CLI/exit behavior `:425-435`.
- Round-89 evidence: `.ufo/waves/round-89/followup/CB1.md` (drift inventory
  CB1-R1 … CB1-R19, two-revision census, fixture replays, scratch probes for
  the raw-presence wordings, the three-cause record, and the four FN-2
  sub-branches) and the work-wave artifacts it audits — `.ufo/waves/round-89/`
  seat reports (`F1.md`, `F2.md`, `F3.md`, `X1.md` where present) with patches
  under `.ufo/waves/round-89/patches/`.
- Round-88 evidence: `.ufo/waves/round-88/followup/CB1.md` (drift inventory
  D1-D21, cause/precedence/emission-order probes, 149-directory preservation
  census, fixture inventory re-measurement), and the work-wave seat reports
  `.ufo/waves/round-88/X1.md`, `X3.md`, `X4.md`, `F1.md`.
- Round-87 evidence (superseded behavior; kept for history):
  `.ufo/waves/round-87/followup/I2.md` (delivered-tree replay at `2b48ca7`,
  133-directory preservation check, census, scratch boundary probes
  `p1`-`p8`). `.ufo/waves/round-87/CB1.md` is a different artifact from the
  round-88 and round-89 `CB1.md` despite the shared seat id: the round-87 file
  is a pre-C1 replay of the five probes at `28706dc`.
- Probe inputs: `corpus/live/runs/round-85/probe-inputs/{r85-control,
  r85-unique-break-control,r85-masked-ambiguous,r85-isolated-ambiguous,r85-harbor-repro}/`
  — masked `entities.json:49-93` and unique-control `entities.json:49-81`
  carry identical transfers `(null→mira,0)`, `(mira→vault,3)`,
  `(harbor→tower,4)`; masked adds a second `vault` row. Isolated carries a
  continuous chain ending in the duplicated `vault` at record `[2]`.
- In-tree provenance fixtures at `1b09f3f`: 29 directories carry
  `provenance`; 13 provenance records across ten of them reference a
  duplicated holder id — `r87-masked-break-from-ambiguous`,
  `r87-masked-break-to-ambiguous`, `r87-probe-multi-invalid`,
  `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three records),
- In-tree provenance fixtures at `ca7f9ef`: 33 directories carry `provenance` (29 at
  `1b09f3f`); 13 provenance records across ten of them reference a duplicated holder id —
  `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
  `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three
  records), `r87-probe-shape-ambiguous`, `r88-mixed-stop`, `r88-shape-ambiguous-armed`,
  `r89-c1-multi-cause-valid`, `r89-fn2-unresolved-chain-break` (plus the r85 live probes
  outside `corpus/fixtures`). The four round-90 fixtures carry provenance but no duplicated
  holder references (dangling raw-present ids only). `r7-item-ambiguous` is ambiguous SOURCE
  only; `r61-*` are dangling holders on a non-item entity. Measured by
  `.ufo/waves/round-90/followup/CB1.md` (r90) and §M7 of the r89 CB1 report.
- Fleet round-1 evidence: `reports/round-1/current-baseline.json` and
  `reports/round-1/baseline-probes.json` (parent-recorded CLI triples at
  `5eb9451`; all recorded stderr empty); `reports/round-1/critic.md`
  (counterexample table this guidance encodes);
  `reports/round-1/current-dispatch.json` (seat write scopes — seat
  `R1Guide` holds the scope for this file).
- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline,
  no inferred history, citation ≠ support) and `:121-128` (round-7
  duplicate-source rule mirrored by this holder contract). The README's
  `## Round 88` section (`:1008-1012`) states the r88 stop-cause repair and
  points readers to this document as the contract; there is no
- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline, no inferred history,
  citation ≠ support) and `:121-128` (round-7 duplicate-source rule mirrored by this holder
  contract). The README carries `## Round 88` (`:1008-1011`) and `## Round 89` (`:1012-1015`)
  sections; the Round 89 section states the r89 cause branches and points readers to this
  document as the first-stop cause contract. There is no `## Round 90` section at `ca7f9ef`, so
  the r90 integer-only tick reading, the null guard, and the four new fixtures are stated only
  here (and in the r90 wave artifacts) until a Round 90 section lands. The r87 decision table
  (`corpus/knowledge/r87-provenance-chain-decision-table.md`) is superseded and still quotes
  removed strings; treat it as history.
- OBSERVED on the delivered tree (round-89 seat CB1, `1b09f3f`; exact
  commands and output in "Commands" and
  `.ufo/waves/round-89/followup/CB1.md`): the five r85 probe triples pasted
  above (byte-identical to the r88 replay); the six durable r88/r89
  non-holder-cause fixture outputs pasted above; the multi-cause fixture and
  the FN-2 fixture pair pasted above; the six r89 single-cause fixtures; the
  165-directory two-revision census (0 exit changes, 0 stderr changes, 9
  changed stdout tuples); the 29-directory provenance inventory with 13
  duplicated-holder records.
- OBSERVED only in scratch probes at `1b09f3f` (no durable fixture): both
  `present in raw … but absent from the resolved index` wordings; a
  three-cause valid-key record; the four FN-2 sub-branches (expected-side,
  observed-side, tick, first-record). Command form and output in
  `.ufo/waves/round-89/followup/CB1.md` §M5-§M6.
- OBSERVED only in round-88 scratch probes at `2ea9ef1` (no durable fixture
  of their own; some now covered by older fixtures): non-dict record
  (`r87-probe-record-and-chain`), both-fields ambiguity at one record
  (`r87-probe-record-and-chain`), non-item provenance and unavailable source
  table (`r61-*`), duplicate item id (`r87-probe-entry-shape`). Evidence in
  `.ufo/waves/round-88/followup/CB1.md` §3, scratch under `/tmp/cb1/`.
- OBSERVED at baseline `5eb9451` (parent-recorded JSON): masked and
  isolated emitted ONLY the global duplicate; unique control emitted the
  definite record-2 break; control was CLEAN; harbor-repro showed
  timeline-endpoint ambiguity voiced while holder references stayed
  silent.
- SUPERSEDED: the r87 two-notice contract (`2b48ca7`) and its replay block;
  preserved in `.ufo/waves/round-87/followup/I2.md` and
  `corpus/knowledge/r87-provenance-chain-decision-table.md`. The latter still
  quotes both removed notice strings (measured at `1b09f3f`: `:60`, `:61`,
  `:99`, `:169-172`, `:179-182`, `:216-218`, `:222-223`, `:238-240`,
  `:268-269`, `:271`, `:281-283`) and still expects r87-era output (row 33,
  `:104`: an `item-level notice` the delivered checker never prints); it is
  marked SUPERSEDED-and-pinned at its header (r88 closure) anywhere in the tree.
- REPLAYED, not scored: no five-gate `passed` count exists for `1b09f3f`;
  the documented helper is absent at that revision.
- UNKNOWN / UNMEASURED: whether any fixture outside the 29 listed above
  combines `provenance` with a duplicated holder id (none does in
  `corpus/fixtures`); any external reader behavior change; whether a raw row
  rejected for a non-`id` field can ever leave a dangling reference whose
  id it does not carry (it cannot, by construction — the raw counter is
  keyed on the row's own `id`).

## Measured results (parent-owned slot)

No five-gate score is recorded for the delivered tree `1b09f3f`: the
documented measurement helper is absent at that revision. The behavioral
replay that stands in for it is the five-case delivered output pasted under
"Commands", the durable fixture outputs pasted there, and CB1's scratch
cause/precedence/FN-2 probes recorded in
`.ufo/waves/round-89/followup/CB1.md`; every contract, table, and limits line
above is stated as-of that replay.
