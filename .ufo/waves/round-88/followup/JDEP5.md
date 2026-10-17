# JDEP5 — Depth judge #5 (capabilities assessment)

Judged on the DELIVERED tree at `2ea9ef1` (`2ea9ef13a928475b13fd578740ea521bed4bd649`,
parent `dfd1fbc`; `git status --porcelain` clean at start), never on intent or
scratch patches. Question per `AXES.md` §Capabilities: does r88 demonstrate a
lane capability that belongs in `SCORECARD.md`'s `capabilities:` table?

Candidates assessed:

- **CAP-1 `provenance stop-cause assessment`** — the checker + the three durable
  r88 fixture classes + the decision table now let the lane assess and disclose
  any stop cause.
- **CAP-2 `sourced-inspiration verification`** — the D1 rule (decision table) +
  grep-anchor checks.

Every measurement below is my own run on the delivered tree. Machine-readable
form of all receipts: `.ufo/waves/round-88/followup/JDEP5-receipts.json`.
Scratch probes live in `/tmp/jdep5-probe/`; no tracked file other than this
report and its receipts JSON was written.

## Work performed

- Confirmed the tree under judgement: `git log --oneline -3` → HEAD
  `2ea9ef1 lore r88: C1 stop-cause repair + C2 Maya cluster + C3 inspiration
  table — work wave (37 luna-max seats)`.
- Re-ran the **full 149-directory fixture census** myself against the r87
  baseline tuples (`.ufo/waves/round-88/patches/B1-tuples.json`, 145 dirs) and
  compared `(exit, sha256(stdout))` per directory.
- Ran the three durable r88 fixture classes and the changed r87 probes directly.
- Authored **scratch probes** (`/tmp/jdep5-probe/`) for every stop-cause class
  the checker can latch, plus two non-stop classes as controls, and ran the
  delivered checker on each. Probes are scratch-only per the wave rules.
- Replayed **all 19 pasted CLI receipts** in
  `corpus/knowledge/r87-provenance-chain-decision-table.md` against the
  delivered checker and diffed expected vs actual stdout and exit.
- Ran the **prose-anchor check** the delivered decision table prescribes
  (`grep -nF -- '<clause>' <excerpt>`) on both delivered cluster clause maps.
- Grepped the delivered checker and the two live knowledge docs for the r87
  notice strings.

## Before → after measurements

### 1. Census — the capability's blast radius (no axis harmed elsewhere)

Command (my own script, delivered tree vs `B1-tuples.json`):

```sh
python3 - <<'PY'   # full text in JDEP5-receipts.json
# per dir: python3 corpus/fixtures/check_bible.py <dir>; compare (exit, sha256(stdout)) to B1-tuples.json
PY
```

Observed:

```text
dirs_on_tree=149 baseline_dirs=145
exit_0=31 exit_nonzero=118
changed_tuples=9
exit_flips=0 []
new_dirs=4
   corpus/fixtures/r88-m3-maya-cluster          exit=0 violations=0
   corpus/fixtures/r88-mixed-stop               exit=1 violations=6
   corpus/fixtures/r88-nonholder-stop           exit=1 violations=4
   corpus/fixtures/r88-shape-ambiguous-armed    exit=1 violations=5
changed: r61-independent-empty, r61-independent-unavailable,
         r87-masked-break-from-ambiguous, r87-masked-break-to-ambiguous,
         r87-probe-entry-shape, r87-probe-multi-invalid,
         r87-probe-nonitem-kinds, r87-probe-record-and-chain,
         r87-probe-shape-ambiguous
```

This reproduces the declared C1 delta exactly (9 changed + 4 new of 149 dirs,
0 exit changes) and confirms the change is disclosure-only: no exit status
moved, stderr empty throughout, and the two pre-r87 `r61-*` directories change
by additive disclosure only.

### 2. CAP-1 — every stop cause is disclosed, at the stop record and after

Durable fixtures (in-repo, replayable by anyone):

```sh
for d in r88-shape-ambiguous-armed r88-mixed-stop r88-nonholder-stop; do
  echo "=== $d ==="; python3 corpus/fixtures/check_bible.py corpus/fixtures/$d; echo "EXIT=$?"
done
```

Observed (excerpts; full text in the receipts JSON):

```text
=== r88-shape-ambiguous-armed ===
VIOLATION: entities[4].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
VIOLATION: entities[4].provenance[0].to_holder: ambiguous entity 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: … first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
5 violation(s); no canon changed
EXIT=1

=== r88-mixed-stop ===
VIOLATION: entities[5].provenance[0].source_id: unknown in-world source 'f1-mixed-missing-source'
VIOLATION: entities[5].provenance[0]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
VIOLATION: entities[5].provenance[1]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[2]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
6 violation(s); no canon changed
EXIT=1

=== r88-nonholder-stop ===
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'f1-nonholder-missing-source'
VIOLATION: entities[3].provenance[0..2]: … first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
4 violation(s); no canon changed
EXIT=1
```

The r87 residual is closed on the delivered tree: the shape-invalid dict with
an ambiguous holder **arms** the stop and reports the combined same-record cause
(r87's `r87-probe-shape-ambiguous` went 2 → 5 findings, receipt below), and a
later ambiguity never displaces the actual earlier cause (`r88-mixed-stop`
keeps `unknown source` through `[1]` and `[2]`).

Scratch probes by cause class (`python3 corpus/fixtures/check_bible.py
/tmp/jdep5-probe/<probe>`; probe sources authored by me, scratch only):

| Probe | Cause class exercised | Distinct `first stop:` causes observed | exit |
|---|---|---|---|
| `probe-causes` | non-item provenance, duplicate item id, non-object record, invalid tick, dangling `to_holder`, invalid `source_id`, unknown source | `provenance attached to a non-item entity`, `duplicate item id 'p-dup'`, `malformed record (expected object)`, `malformed record (invalid tick)`, `dangling holder to_holder 'ghost'`, `malformed record (invalid source_id)`, `unknown source 'nope'` | 1 (21 findings) |
| `probe-causes2` | dangling `from_holder`, invalid `from_holder`, invalid `to_holder`, unexpected field set alone | `dangling holder from_holder 'ghost2'`, `malformed record (invalid from_holder)`, `malformed record (invalid to_holder)`, `malformed record (unexpected field set)` | 1 (12 findings) |
| `probe-unavailable` | sources table missing | `source table unavailable` | 1 (23 findings) |
| `probe-ambigsource` | **control** — duplicate source rows (not a stop) | *(none — comparisons continue, prefixed `input-structural finding, not sourced-canon;`)* | 1 (13 findings) |
| `probe-nonlist` | **control** — `provenance` is not a list | *(none — `entities[1].provenance: expected array` only)* | 1 (1 finding) |

Durable-fixture coverage of the two remaining classes:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
… first stop: ambiguous holder identity to_holder 'dup' at entities[3].provenance[0]   (5 findings, exit 1)
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-from-ambiguous
… first stop: ambiguous holder identity from_holder 'dup' at entities[3].provenance[0] (5 findings, exit 1)
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
… first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]  (5 findings, exit 1)
```

Controls behaved correctly: in every probe the clean entity emitted **no**
disclosure, and the 136 unchanged fixture tuples emitted byte-identical stdout.

**Verdict for CAP-1: the capability runs on the delivered tree.** 15 stop-cause
classes observed, each disclosed at the stop record and at every later record
of that provenance array, each naming the cause that actually latched the stop.
The demonstration is replayable from the repository alone via the three durable
r88 fixtures (no scratch needed for the core claim).

### 3. CAP-2 — the prescribed verification check does not pass on the delivered cluster

The delivered decision table's own rule
(`corpus/knowledge/r88-sourced-inspiration-decision-table.md`, in-world claim
row) is: *"record a distinctive exact phrase or named anchor, then run a
fixed-string, line-numbered search such as `grep -nF -- 'anchor phrase'
<excerpt-path>`; a missing excerpt or zero match fails."*

I ran exactly that on both delivered clause maps (extracting each map's cited
clause cell and grepping it literally against the delivered excerpt):

```sh
grep -nF -- 'He called out ‘Earth,’' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md
```

Observed:

```text
grep1 exit=1                       # MISS — excerpt uses double curly quotes:
5:> … He called out “Earth,” and the solid land appeared.
grep2 exit=0                       # 'and the solid land appeared.' matches
```

Aggregate over both delivered clusters:

```text
r87-myth-cluster:      literal grep -nF clause matches = 8/8
r88-m3-maya-cluster:   literal grep -nF clause matches = 1/2   (MISS: 'He called out ‘Earth,’')
```

The r87 side (the cluster whose OBS-1 excerpt was repaired this round) passes
8/8, and its delivered state is consistent: `gate_named=True;
first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=8/8`
and both clusters exit 0 (`CLEAN: schema, citations, relations, timeline; 0
violations`). The r88 M3 cluster — landed in the same commit — fails the
lane's own literal check on 1 of 2 map clauses because the map transcribes the
excerpt's inner double quotes as single quotes (`‘Earth,’` vs `“Earth,”`).

There is **no runnable checker** for this discipline on the delivered tree:
`check_bible.py` does not read Markdown/excerpts (its `CLEAN` result is
explicitly not prose verification), and no helper script for anchors exists
(`find . -name '*.py'` → `corpus/fixtures/check_bible.py`,
`corpus/live/rejected-r4/check_bible.py`, `reports/round-1/measure_preservation.py`,
`.ufo/rounds/r86/diagnose.py`; none checks prose anchors).

**Verdict for CAP-2: not yet demonstrated as a running capability.** The
delivered evidence is a documented procedure plus ad-hoc greps in seat reports;
the one place the procedure was applied to a delivered r88 artifact, it fails
1/2 literally.

### 4. Adjacent delivered-tree state discovered while judging (corroboration, not my seat's claim)

This is **not** a new claim: `JDEP4.md` F1/F2 and `JCAL5` D-1 already report the
same drift, and `P2-scorecard-r88.md` records it as the round's
`documentation parity — harmed (bounded)` trade. I re-measured it independently
because it is the context a capabilities row would sit in; my numbers are
per-receipt (replay of each pasted command) where JDEP4's are per-dead-string.
The r87 depth artifact's receipts no longer replay on the delivered tree:

```sh
# parse every '$ python3 corpus/fixtures/check_bible.py <path>' block in
# corpus/knowledge/r87-provenance-chain-decision-table.md, rerun it, diff
```

Observed: `pasted_receipts=19 stale_receipts=10`, `exit_changed=false` in all
ten. Stale entries (expected lines → delivered lines):

```text
r87-masked-break-to-ambiguous     7 → 6      r87-probe-shape-ambiguous      3 → 6
r87-masked-break-from-ambiguous   7 → 6      r87-probe-multi-invalid        7 → 6
r87-probe-entry-shape             3 → 9      r87-probe-nonitem-kinds        9 → 10
r87-probe-record-and-chain       35 → 47     r61-independent-empty         18 → 19
r85-masked-ambiguous              6 → 5      r61-independent-unavailable    7 → 8
```

The r87 notice family the table pastes is gone from the delivered checker and
still quoted in two live docs:

```text
$ grep -n "because holder identity is ambiguous\|first occurred at" corpus/fixtures/check_bible.py
(no output; grep exit=1)
stale string occurrences: corpus/knowledge/holder-assessment-boundary.md = 13
                          corpus/knowledge/r87-provenance-chain-decision-table.md = 26
```

`holder-assessment-boundary.md` still declares `verified-at: RUNTIME REPLAYED
… at 2b48ca7` and its contract items 1–3 describe the r87 item-level notice +
per-record disclosure strings; `r87-provenance-chain-decision-table.md` row 32
still asserts the shape-invalid-ambiguous case is *"never armed"* — the exact
residual r88 repaired. Both docs' own recheck trigger ("re-verify whenever the
provenance branch of `check_bible.py` changes") has fired.

## Findings & named debt

### Recommendation 1 — **FOR** a `provenance stop-cause assessment` capability row

The capability is real, runs on the delivered tree, is replayable from the repo
without scratch, and is demonstrated by a non-author judge (me) rather than
asserted by the implementer. Per `AXES.md` §Capabilities the row needs name →
what it can do → evidence pointer → first-working round:

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| provenance stop-cause assessment | For any provenance-chain stop the checker latches (15 cause classes), emit at the stop record and at every later record of that provenance array a disclosure naming the cause that actually latched the stop, never a later ambiguity | `for d in r88-shape-ambiguous-armed r88-mixed-stop r88-nonholder-stop; do python3 corpus/fixtures/check_bible.py corpus/fixtures/$d; done` → 5/6/4 findings, exit 1, disclosures quoted in `.ufo/waves/round-88/followup/JDEP5.md` §Before→after 2 | r88 |

Conditions the L1 should attach (they bound the row, they do not block it):

- **Non-stop classes are not covered and must be named in the row or the round
  record**, or a reader will read them as gaps: (a) a duplicate *source* id
  leaves comparisons running with an in-band `input-structural finding, not
  sourced-canon;` prefix and emits no stop disclosure (`probe-ambigsource`);
  (b) a non-list `provenance` emits `expected array` and no disclosure because
  there are no records to disclose on (`probe-nonlist`,
  `r87-probe-entry-shape` `entities[4]`).
- **The "first" cause is scoped per provenance array**, not per fixture: two
  entities in one directory each get their own first-stop disclosure. That is
  correct behaviour but the word "first" is ambiguous without the scope.
- **The same-record combination is only implemented for the shape-invalid
  branch.** `r87-probe-multi-invalid` record `[1]` carries both
  `ambiguous entity 'vault'` and `unknown in-world source 'ghost-source'`; the
  summary names only `ambiguous holder identity from_holder 'vault'`. This is
  **not** over-attribution (it names a cause that genuinely latched) but it is
  not a combined summary either; the decision table's row wording should say so.

### Recommendation 2 — **AGAINST** a `sourced-inspiration verification` capability row this round (defer to r89)

It would be pre-claiming under `AXES.md` §Capabilities ("a capability without a
passing demonstration in the round report is pre-claiming and does not enter
the table"): the only runnable evidence pointer available is the rule text
itself, and running that rule literally against the cluster landed in the same
round fails 1/2. Path to make it enter in r89:

1. Land a helper (e.g. `corpus/fixtures/check_prose_anchors.py`) that extracts
   each map's cited-clause cells, normalizes curly/straight quote variants,
   greps `-F` against the delivered excerpt, and exits non-zero on a zero match
   — that gives the row a real command pointer.
2. Fix the M3 map's inner-quote transcription (`‘Earth,’` → the excerpt's
   `“Earth,”`) or make normalization part of the rule, so the delivered cluster
   passes its own check.
3. Then the row can cite the helper plus
   `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster`
   (exit 0) and the r87 8/8 literal clause receipt.

### Named debt (for the round record / r89)

1. **Stale depth docs contradict the delivered checker — already carried; my
   measurement corroborates it, it is not a new claim of this seat.**
   `corpus/knowledge/r87-provenance-chain-decision-table.md`: 10/19 pasted
   receipts no longer replay; 26 occurrences of the superseded notice strings;
   row 32 asserts a residual that r88 fixed.
   `corpus/knowledge/holder-assessment-boundary.md`: 13 occurrences of the
   superseded strings; `verified-at` still pinned to `2b48ca7`. Both docs'
   own recheck trigger has fired. Recorded by `JDEP4` F1/F2, `JCAL5` D-1, and
   `P2-scorecard-r88.md`'s `documentation parity — harmed (bounded)` row. This
   does not invalidate the CAP-1 demonstration (the checker and durable
   fixtures are the evidence), but a capability row would sit next to a
   decision table that contradicts it — that is the calibration risk the L1
   should weigh when entering the row.
2. **M3 clause-map quote variance** blocks CAP-2 (receipt above).
3. **Spence reference unregistered** — `grep -c Spence
   corpus/knowledge/reference-ledger.md` → `0` while
   `corpus/fixtures/r88-m3-maya-cluster/inspiration-note.md` cites it with a
   delivered excerpt. Already named by JDEP2 (F2); flagged here only because it
   is the same integration-completeness surface as CAP-2. Not my seat's claim.
4. **My probe fixtures are scratch-only** (`/tmp/jdep5-probe/`): the 11 cause
   classes beyond the three durable r88 fixture classes are demonstrated but
   not durable. If the L1 wants the capability row to rest on in-repo fixtures
   alone, the core claim still holds (the three durable fixtures cover
   armed-shape-stop, mixed-stop first-cause, and non-holder stop), but the
   remaining classes rest on this report's scratch receipts.

## Handoff

- **Deliverables:** `.ufo/waves/round-88/followup/JDEP5.md` (this report) and
  `.ufo/waves/round-88/followup/JDEP5-receipts.json` (census, per-class
  stop-cause table, 19-receipt replay result, prose-anchor results, stale-string
  counts, HEAD). No other repository writes; no commit; no push; no registry
  write; sibling repos untouched.
- **Decision for the L1:** (a) enter the CAP-1 `provenance stop-cause
  assessment` row (recommended FOR) with the row text and evidence pointer
  above, attaching the three bounds. Note `P2-scorecard-r88.md` currently
  carries **no** `capabilities:` row for r88 (grep for `capabilit` in that
  proposal → no match), so this row must be added, not edited. (b) do **not**
  enter a CAP-2 `sourced-inspiration verification` row this round — carry the
  three-step r89 path. The two stale-doc refreshes are already carried by
  `JDEP4`/`JCAL5`/`P2` (documentation parity); if the CAP-1 row is entered
  before they are repaired, the round record should point at that trade row so
  the capability is not read as validating the superseded docs.
- **Verdicts recorded (never scalars):** CAP-1 demonstration — the capability
  runs; CAP-2 — not demonstrated running; delivered r87 decision table —
  receipts stale (10/19), exit statuses unchanged; census — 9 changed + 4 new
  of 149, 0 exit flips.
- **Gaps/limits:** I did not re-verify the three durable fixture READMEs'
  declared expectations line-by-line (seat V2 owns that; my checks are
  independent runs, and V2's report agrees with mine). I did not fetch the
  Spence page to confirm the p. 209 locator (JDEP2 flagged the same limit for
  ETCSL and I inherited it). My clause-map extraction regex reads only cells of
  the form `| “clause” |`; a map with a different cell shape would need a
  different extractor.
