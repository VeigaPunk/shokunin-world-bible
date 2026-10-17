# JAXIS — Axis-verdict synthesizer (round 89 follow-up, world-bible lane)

Seat JAXIS. Judged tree: **delivered** `1b09f3ff8016b26a2259e086f673d0112f4f54e5`
(`1b09f3f`), baseline `51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`. Every verdict below
rests on the delivered tree's artifacts: my own re-runs are pasted under "Before →
after measurements", and each seat-cited number names the follow-up report that carries
its receipt. Scratch `/tmp/jaxis/` only; no commit, no push.

**This file is a RECOMMENDATION to the L1, not the round's verdict.** The L1 owns the
admission decision and the SCORECARD wording. It is written against the lane's standing
rule: per-axis verdicts are `improved / harmed / unchanged / unprovable-but-better`, and
a trade anywhere is NOT an improvement.

## Work performed

- Read all eleven `followup/J*.md` present — `JCAL1`, `JCAL3`, `JCOV1`–`JCOV5`,
  `JDEP1`–`JDEP4`. `JCAL5` delivered a JSON receipt only (`JCAL5-delta.json`, an
  independently regenerated baseline: 149 keys, 0 differing rows; per the r88 JAXIS
  note, a JSON receipt counts as a delivered judgement). Also read the non-J follow-up
  seats whose findings bear on the verdicts: `E1` (drift inventory DR-1…DR-15),
  `CB1` + `CB1-boundary-refresh.md` (drift inventory + drafted contract refresh),
  `H1`, `H2`, `H5` (harm sweeps), `V2` (freeze-then-verify), `P4-shonen`, `K1`
  (L0 connector), and `Q2` (process audit).
- Two 60-second wait-checks per the seat block, timestamped in `/tmp/jaxis/polls.txt`:
  `04:27:38-03:00 → 04:28:38-03:00 → 04:29:38-03:00`. All eleven `J*.md` were present
  at every check and byte-stable across the span; no J-arrival landed during the run,
  so no gap is owed. (`JCAL5.md` does not exist; its seat's receipt is the JSON above.)
- Independent re-runs on the delivered tree (never on scratch patches): the 160-dir
  census; the S2-map anchor sweep; the r87-cluster and R9-demo replays; the combined
  first-stop check on `r89-c1-multi-cause-valid`; the three stale `r89-f2-*` README
  quotes vs delivered output; the boundary-doc replay-vs-pasted-output check against
  both checkers; the fixture-index census.

## Before → after measurements

All commands run from the repository root unless stated.

**Tree identity.**

```sh
git rev-parse HEAD
git status --porcelain
```

```text
1b09f3ff8016b26a2259e086f673d0112f4f54e5
 M l0-questions.md
?? .ufo/waves/round-89/followup/
```

`l0-questions.md` is K1's authorized one-line append (4 → 5 lines, premise correction
of the r88 kotodama line); the untracked entry is this wave's own delivery directory.
No other tracked path differs; sibling repos untouched.

**Census (my re-run, one fresh process per fixture directory).**

```sh
python3 - <<'PY'   # for every dir under corpus/fixtures/: python3 corpus/fixtures/check_bible.py <dir>
PY
```

```text
dirs 160 exits {1: 128, 0: 32} violations 399
```

Matches JCAL1 (`dirs: 160 / exit_counts: {1: 128, 0: 32} / total_violations: 399`) and
H2 (`160 / {1: 128, 0: 32} / 399`). The tree-level delta claim — 4 changed + 11 new of
160, 0 exit changes — reproduces independently in JCAL1, H2, H5, JCOV5, H1, and P4;
H2 adds the arithmetic identity `399 − 367 = 32` = the added dirs' finding sum (the 4
changed dirs contributed net 0).

**Anchor sweep (S2 map vs delivered excerpts).**

```sh
python3 - <<'PY'   # every anchor_phrase in patches/S2-fact-map.json grepped -F against <source_id>-excerpt.md
PY
```

```text
anchors 14 / 14
```

Matches JCOV1 (14/14, per-row locations), JCOV2 (own anchor derivation, 22/22),
JCOV4 (14/14), JDEP4 (14/14), P4 (14/14), H1 (14/14).

**Cluster and demo replays.**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "r87_exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase; echo "demo_exit=$?"
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
r87_exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
demo_exit=0
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
```

**Combined first-stop on a valid-key record (C1(ii) behavior).**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-c1-multi-cause-valid | grep -m1 'first stop'
```

```text
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder' at entities[2].provenance[0]
```

Both simultaneous causes named, `; `-joined, on a shape-valid record — the baseline
named only the tick (JCAL3's before/after table; V2 fixtures check; H2 line-class table).

**The three stale `r89-f2-*` README quotes vs delivered output.**

```sh
grep -n "dangling holder\|unknown source" corpus/fixtures/r89-f2-dangling-to/README.md \
  corpus/fixtures/r89-f2-dangling-from/README.md corpus/fixtures/r89-f2-invalid-source-id/README.md
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-f2-dangling-to | grep -m1 'first stop'
```

```text
r89-f2-dangling-to/README.md:9: … The expected first-stop disclosure names `dangling holder to_holder 'r89-f2-missing-to'` …
r89-f2-dangling-from/README.md:9: … names `dangling holder from_holder 'r89-f2-missing-from'` …
r89-f2-invalid-source-id/README.md:9: … names `unknown source 'r89-f2-unknown-source'` …
VIOLATION: entities[3].provenance[1]: … first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
```

Each README states an expectation the delivered checker does not emit. Reproduced
independently by JCAL3 (Debt 1), V2 (check 2), H2 (F3), H5 (§1), E1 (DR-8).

**Boundary contract doc vs the delivered checker.**

```sh
grep -nF -e 'only the shape-invalid branch' -e 'FIRST check in precedence order' \
  -e 'dangling holder to_holder' -e 'unknown source' corpus/knowledge/holder-assessment-boundary.md
git show 51b286b:corpus/fixtures/check_bible.py > /tmp/jaxis/base_check.py
python3 /tmp/jaxis/base_check.py corpus/fixtures/r88-mixed-stop | grep -m1 'first stop'
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop | grep -m1 'first stop'
```

```text
152:| 9 | `dangling holder to_holder {id!r}` | `to_holder` absent from entities | `:255-258` |
156:| 13 | `unknown source {id!r}` | `source_id` resolves to no source row | `:288-290` |
169:| Two causes in one shape-valid record (e.g. bad tick AND ambiguous holder) | … the named `first stop:` clause names only the FIRST check in precedence order … | … Only the shape-invalid branch combines two cause phrases | …
338–348: pasted "delivered output" blocks for r88-mixed-stop / r88-nonholder-stop, reading `first stop: unknown source 'f1-mixed-missing-source'`

baseline replay:  … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
delivered replay: … first stop: source reference 'f1-mixed-missing-source' absent from raw sources and absent from the resolved index at entities[5].provenance[0]
```

So the doc's pinned snapshot (r88 checker) still reproduces its pasted text, while the
delivered checker emits the FN-1 wording; and the doc's precedence assertion (`:169`,
`:222-227`) is directly falsified by the delivered `r89-c1-multi-cause-valid` output
above. E1 itemizes the drift as DR-1…DR-15 (H: cause rows 9/10/13, the precedence
claim, the "definite comparison findings" row, the stale fixture READMEs; M: anchors,
census, status banner; L: index/parity). CB1's separate inventory (CB1-R1 … CB1-R19+)
motivates the drafted refresh `CB1-boundary-refresh.md` (**proposal only — not
applied**; the tracked file still carries the r88 content and its leftover "PROPOSAL —
not applied" banner, CB1-R15).

**Fixture index.**

```sh
grep -c 'r89' corpus/fixtures/README.md; grep -n '^## ' corpus/fixtures/README.md | tail -3
```

```text
0
1000:## Round 83: Vela joint non-sighting scope
1004:## Round 87: provenance disclosure + myth cluster
1008:## Round 88: stop-cause disclosure + second cluster
```

Eleven `r89-*` dirs, the four new r87 excerpts, and the R9 demo are unindexed.
Precedent: the Round 87/88 sections were added at r88 **closure**, not at the work
commit (JCAL3 Debt 5) — so this is closure-scope, not a work-wave defect.

**Wait-checks.** `/tmp/jaxis/polls.txt`: three timestamps, identical 11-file `J*.md`
listing at each. The J-lane had stopped landing before my first check; no late
dependency is unaccounted for.

## Findings & named debt

### Per-axis verdict table (recommendation to the L1)

| axis | verdict at `1b09f3f` | one-line evidence pointer |
|---|---|---|
| **calibration** | **improved (bounded)** | Census 160 dirs / exits {0:32, 1:128} / 399 violations reproduces in six seats (JCAL1, H2, H5, JCOV5, H1, P4) and in my re-run; tree delta exactly 4 changed + 11 new, 0 exit flips, 0 violation-count changes on shared paths (H2 line-by-line: the 4 changes are FN-1 cause-clause substitutions inside existing disclosure lines); checker is byte-identical to `X1-c1.patch` applied to `51b286b` (V2 `IDENTICAL`, JCAL1 replay, H1); each of the 9 non-control fixtures is caught by at least one mutation of the delivered checker (JCAL3 matrix). Bounds below. |
| **coverage** | **improved (bounded)** | 14/14 delivered fixed-string anchors (my re-run; JCOV1/JCOV2/JCOV4/JDEP4/P4/H1 concur), 22/22 facts under the anchor form of the D1 rule (JCOV1 independent replay; JDEP4 runnable sweep), 6/6 first-appearance pointers resolve, r87 cluster and R9 demo replay `CLEAN` exit 0 (my re-run), ETCSL ledger row carries `external-only / text not delivered at lore` with cells 0–2 and prior rows byte-identical (JCOV2 own diff; JCOV5; H2). Bounds below. |
| **depth** | **harmed (bounded)** | The r88 harm class recurs on the delivered tree: the doc `corpus/fixtures/README.md:1006` names as "the current contract" — `holder-assessment-boundary.md` — is falsified by the delivered checker on exactly what C1 changed (my re-run above: precedence claim `:169`, cause rows `:152/:156`, pasted replay block `:338-348`), with E1's DR-1…DR-10 and CB1's inventory enumerating the drift; and three `r89-f2-*` fixture READMEs **delivered by this round** state pre-FN-1 expectations (my grep above). The C3 gains (R8–R10 rows + R9 demo + R10 worked example) are real and verified (JDEP1–JDEP4), but per the lane rule a trade is not an improvement and must not be netted silently. Repair artifacts are already drafted (CB1 refresh; E1/JCAL3/V2/H2/H5 diagnoses); on application at closure the axis becomes `improved (bounded)` — mirroring r88's sequence (follow-up ruled harmed; closure repaired; final record improved). |

No other axis harmed: H1–H5, JCOV5, V2 and P4 find no exit/stderr, coverage, corpus or
process harm beyond the documentation-parity surface above; the harm is entirely on the
documentation/expectation sub-surface and is bounded to it.

Attribution note (for the L1's wording): H2 argues the documentation-parity cost should
be counted against the calibration move; I assign it to depth because the r88 record
ruled the identical condition (knowledge doc + fixture READMEs contradicting the shipped
checker) under depth (r88 `JAXIS.md`: "depth: harmed (bounded)"). Under either
attribution the substantive instruction is identical: the cost is real, it is bounded,
and it must be discharged (or recorded) before "improved" is written anywhere it is
charged.

### Claim-verification notes (C1 / C2 / C3 vs the delivered tree)

1. **C1 verifies, with three wording corrections for the round record.** (a) "Delta 4
   changed + 11 new of 160 dirs" is the tree-level orientation; at checker-to-checker
   level on the same 160 dirs, **9** directories' stdout differs (4 pre-existing + 5 new
   r89 fixtures that only the new checker can render as intended) — E1 (`stdout_changed=9`)
   and P4 (`changed tuples: 9`) measured this second orientation; the record should state
   which it means. (b) "New combined cause summary" must be scoped: the shape-invalid
   branch already combined at baseline; what C1 adds is the **valid-key** branch
   (JCAL1 finding; H2). (c) FN-2 is invisible to the 149-dir manifest — re-running it
   cannot detect an FN-2 regression; only the two new `r89-fn2-*` fixtures can (JCAL1).
2. **C2 verifies under its own rule, but "22/22" must name the rule.** The wave's
   headline figure is the anchor form (14 anchors + 7 pointers + 1 hymn claim); M4's own
   recorded baseline script prints `OK=8` on both trees because it measures
   whole-statement containment (JCOV1-D1; JCOV5-F2; H1-F1; P4). The number is true under
   the rule the R5 row specifies; the receipt artifact is not reproducible from its own
   command and should not be cited alone.
3. **C3 verifies as delivered** (three rows, owner + prospective scoping present, R9
   fixture replays `CLEAN` with an accurate map pointer, R10 demo carries all R10-named
   fields and resolves its pointers — JDEP1's full command replay; JDEP3's 17/17 field
   parse). Bounds: the append renders **outside** the table (no header/delimiter row —
   JDEP1 D1, measured with a real GFM parser); each R8/R9/R10 row leaves one sub-case its
   own text cannot decide (JDEP2); the register has no scoping rule, format, or
   discoverability for its first real entry (JDEP3 F2/F3).

### Named debt (consolidated; receipts in the named seats)

**Calibration-side:**
- C-D1 **FN-1's raw-present branch has zero durable fixtures and zero README surfaces**
  (JCAL1, JCAL3 Debt 3, H5 §5; scratch-probed twice). Half the FN-1 claim is
  demonstrated only by scratch.
- C-D2 FN-2 manifest-invisibility (above).
- C-D3 Three `r89-f2-*` README clauses quote pre-FN-1 strings (**blocking repair**;
  JCAL3 Debt 1, V2, H2 F3, H5 §1, E1 DR-8). Related: `r89-f2-invalid-source-id` is a
  misnomer (it exercises *unknown* source; the `malformed record (invalid source_id)`
  branch is `r89-c1-malformed-source-id`) and the three F2 READMEs state no exit/finding
  count (E1 DR-8, H5 §7).
- C-D4 E1's code-polish items: DR-5 (null `from_holder` downgraded to "not uniquely
  resolvable"), DR-6 (duplicate identity clause when both sides carry the same
  unresolved id), DR-7 (unreachable `or 'malformed record'` fallback at
  `check_bible.py:316`).
- C-D5 Four of the eight cause-branch fixtures are not delta-discriminators against the
  baseline (they pin the vocabulary; only mutation-discriminating) — JCAL3 Debt 4.
- C-D6 The r89 SCORECARD r88 bound "combined same-record summary exists only on the
  shape-invalid branch" is discharged by C1 and must be retired in the closure record
  (E1 DR-14).

**Coverage-side:**
- V-D1 No in-corpus claim-to-excerpt map for the r87 cluster; the 22/22 mapping lives
  only in `.ufo/waves/round-89/patches/{M4-verify,S2-fact-map}.json` (JCOV4 D1, JCOV2
  #7, JDEP4 F5, P4 D1).
- V-D2 The four new r87 excerpts declare **no R9 delivery mode** although delivering
  them is a content touch of r87 (JCOV4 D2, JCOV2 #4, H5 §6, JDEP2 D-4, P4 D2).
- V-D3 r87-cluster README not updated; `corpus/fixtures/README.md` has no Round 89
  section (JCOV1-D2, JCOV4 D3, H2 F4, H5 §4 — closure-scope by precedent).
- V-D4 ETCSL marker literal diverges from the decision table's `external-only /
  unverified` token (JCOV4 D4, JCOV2 #2, JCOV5 F6).
- V-D5 Ledger Spence row sits after the table's closing prose (renders as paragraph;
  pre-existing) — JCOV2 #5, JCOV5 F5, JDEP1/JDEP3 flag.
- V-D6 Decision-table row-5 evidence cell stale; R9 row does not name its fixture path
  (JCOV1-D3, JCOV3 D1); `S2-fact-map.json.anchor_basis` still says M3 (JCOV1-D4, Q2).
- V-D7 Sibling-craft cross-references absent: R8/R9 re-derive chousa claim-vs-source
  limits and kotodama inspiration-boundary/translation-label craft without citing them
  (JCOV5 F3/F4); l0-questions r88 kotodama premise corrected by K1's append (F1/F3).
- V-D8 R9 demo map dispositions 1 of its bible's 2 support-rule facts (JCOV2 #6).

**Depth-side:**
- D-D1 **Blocking repair: refresh `holder-assessment-boundary.md`** against the
  delivered checker (CB1's drafted refresh, or equivalent; re-verify its anchors before
  applying; drop the leftover proposal banner). E1 DR-1…DR-12; H2 F5; H5 §4; JCAL3
  Debt 2; CB1-R1…R19+.
- D-D2 R8–R10 block renders as paragraph text; give it a header+delimiter row or fold
  into the main table; update the sixth-column label (JDEP1 D1/D4).
- D-D3 Governance sub-cases: R8 detection/trigger gap + unexercised element marker; R9
  translation-unknown-version disposition; R10 dismissed-overlap recording + identity
  test (JDEP2 D-1…D-6; JDEP1 D3/D2; JCOV2 #1; K1 F2).
- D-D4 Register readiness: scoping rule to landed clusters (not fixture dirs), register
  file/format/ID conventions, destination discoverability; singular demo vs plural
  register naming (JDEP3 F2/F3, E1 DR-15).
- D-D5 `holder-assessment-boundary.md:365-367/:462-465` still call three now-fixtured
  cause families fixture-less (P4 D3).
- D-D6 `r87-probe-source-prefix/README.md` code-line refs shifted +27/+36/+40 by the
  r89 checker growth (H5 §3).
- D-D7 Capability rows: the structured SCORECARD table still reads `— none yet —`
  although the r88 narrative claims row 1 entered; entering row 2 (in-world excerpt
  support verification) requires repairing the table with row 1 + row 2 in one edit and
  landing the evidence command in the round report (JDEP4 F3/F4, FOR with F5/F6 bounds).

### Side recommendations (not axis verdicts)

- **Capability row: FOR** `in-world excerpt support verification` (JDEP4), conditional
  on D-D7; state its bounds verbatim (procedure-shaped; wave-resident map; paraphrase
  demonstrated only negatively). Do not enter it into a table that still says "none
  yet".
- **SHONEN (P4)**: box 3 may move `[ ]` → `[~]` (two demonstrated D1 applications; r88
  blocker cleared); boxes 2/4 assertions retained with stale pointers; no `[x]` without
  a named non-author cold-run verifier.
- **Process (Q2, for r90)**: poll loop exceeds the 600 s tool cap by construction (fix
  I1); landing record should be hash-stamped (I2); publish roster/amendments as data
  (I3) — the three integrator edits (new fixture, composed table, map field) are exactly
  what I3's amendment log would carry.

### Admission recommendation to the L1

**Do not admit as-is; repair, then admit (recommended).** The round's rule is "admit
only if every claim verifies and no axis harmed; a trade is NOT an improvement" —
calibration and coverage verify with named bounds, but the depth axis carries a
reproduced, in-repo documentation harm (D-D1 + C-D3) introduced by the work commit, the
same condition the r88 follow-up ruled harmed and the r88 closure repaired. The repair
set is small, documentation-only, and already drafted:

1. **R1 (blocking):** apply a refreshed `holder-assessment-boundary.md` (CB1's
   `CB1-boundary-refresh.md` is a full replacement re-derived at `1b09f3f`; re-verify
   before applying) — cannot re-open the C1 census (no checker change).
2. **R2 (blocking):** reconcile the three `r89-f2-*` README clauses with the delivered
   FN-1 wording (one clause each; optionally add exit/finding counts and re-scope the
   misnamed `r89-f2-invalid-source-id`).
3. **R3 (closure-scope by precedent):** add the `## Round 89` section to
   `corpus/fixtures/README.md`; retire the SCORECARD shape-valid bound (C-D6); update
   the r87-cluster README (V-D3).
4. **R4 (cheap, non-blocking):** R8–R10 header/delimiter + column label (D-D2);
   `r87-probe-source-prefix` line refs (D-D6); R8 marker on the r87 note (D-D3);
   ETCSL literal alignment (V-D4).

Then record: **calibration improved (bounded), coverage improved (bounded), depth
improved (bounded)**, with C-D1…C-D6, V-D1…V-D8, D-D3…D-D5 carried as named debt. This
is the r88 resolution sequence verbatim, and both repair diagnostics are already in the
wave evidence.

**Alternative — admit with recorded harm:** if the L1 prefers not to reopen the round,
record depth **harmed (bounded)** explicitly (the contract doc contradicts the shipped
checker on the exact behavior C1 changed; three delivered fixtures' READMEs fail their
own replay) with R1–R4 as the first r90 items. Acceptable only as stated; do not record
depth as improved while D-D1/C-D3 stand, and do not net the C3 gains against the harm.

Either way, the C2 headline must cite the anchor rule (note 2), the C1 delta must state
its orientation (note 1a), and the C1(ii) claim must be scoped to the valid-key branch
(note 1b).

## Handoff

- Deliverable: `lore-shokunin/.ufo/waves/round-89/followup/JAXIS.md` (this file) and
  `lore-shokunin/.ufo/waves/round-89/followup/JAXIS-verdicts.json` (machine-readable
  verdict table, admission options, consolidated debt ids). No other repo write; no
  commit; no push. `l0-questions.md`'s working-tree modification is K1's authorized
  append, not mine.
- Reproduce my measurements in four commands: (1) loop `check_bible.py` over
  `corpus/fixtures/*/` (expect 160 / {0:32, 1:128} / 399); (2) replay
  `patches/S2-fact-map.json` anchors with `grep -nF` (expect 14/14); (3) grep the three
  `r89-f2-*` READMEs for `dangling holder|unknown source` and compare with each
  fixture's delivered `first stop:`; (4) diff the boundary doc's pasted blocks against
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop` (doc pastes
  the baseline wording; delivered emits FN-1).
- Claim status for the integrator: **C1 verifies (bounded, wording corrections 1a–1c);
  C2 verifies under the anchor rule (receipt-reproducibility caveat); C3 verifies in
  substance (rendering + governance sub-case bounds); one bounded documentation harm
  (depth) blocks a clean admission.**
- Not done here: I did not re-derive the baseline census tuple-by-tuple (five seats
  already did), did not re-render the table with a GFM parser (JDEP1's `marked` receipt
  is cited), did not audit the JSON receipts field-by-field, and did not rule on C2/C3
  sub-claims beyond the consolidated debts above. All remediation is the L1's decision.
