# JCAL3 — Calibration judge #3 (round-88 follow-up)

Judged tree: `2ea9ef1` (work commit), baseline `dfd1fbc`. Tree clean before judging;
after judging the only working-tree entry is `.ufo/waves/round-88/followup/`.
All receipts: `.ufo/waves/round-88/followup/JCAL3-receipts.json` (machine-readable) and the
command/observed-output pairs below. Baseline comparison tree is a `git archive dfd1fbc`
unpacked to `/tmp/JCAL3-base`; scratch probes live under `/tmp/JCAL3-probes*`.

## Work performed

1. Confirmed the delivered revision and cleanliness: `git rev-parse HEAD` → `2ea9ef1…`;
   `git status --porcelain` → clean.
2. Ran the three residual fixtures (`r88-shape-ambiguous-armed`, `r88-mixed-stop`,
   `r88-nonholder-stop`) on the delivered tree and read each `README.md` expectation.
3. Ran the 5 r85 live probes in both trees and compared exit code, full stdout and
   stdout sha256 (`/tmp/JCAL3-receipts.py`). Confirmed the probe inputs are byte-identical
   between revisions (`git rev-parse dfd1fbc:… 2ea9ef1:…` → same tree hash
   `b90fac93c9e559b08e83c666d76818a0a744483c`), so every probe delta is checker-only.
4. Ran an independent census (`/tmp/JCAL3-census.py`) over the 145 baseline fixture dirs in
   both trees — I did not reuse V1/X1/X3 output.
5. Audited the delivered disclosure grammar across all 149 fixture dirs: every disclosure
   line carries the qualifier, and every disclosure run is contiguous from the stop origin
   onward.
6. Reconstructed the three pre-r87 before-states from `patches/B3-before-state.json` and
   re-measured the two that are reproducible as scratch probes.
7. Ran 5 additional scratch probes for stop causes the durable fixtures do not cover
   (dangling holder, non-item provenance, duplicate item id, and two same-record
   multi-cause cases).

## Before → after measurements

### (a) `r88-shape-ambiguous-armed` — shape-invalid dict with ambiguous holder id arms the stop

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-shape-ambiguous-armed
VIOLATION: entities[1].id: duplicate entities id 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
VIOLATION: entities[4].provenance[0].to_holder: ambiguous entity 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
5 violation(s); no canon changed
EXIT=1
```

Record `[0]` carries the **combined same-record summary** (malformed + ambiguity); record `[1]`
carries the same first-cause summary and its otherwise-applicable first-record chain break is
correctly not reported. Claim (a) **confirmed**.

### (b) `r88-mixed-stop` — first stop is the unknown-source latch, not the later ambiguity

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop
VIOLATION: entities[1].id: duplicate entities id 'f1-mixed-dup'
VIOLATION: entities[5].provenance[0].source_id: unknown in-world source 'f1-mixed-missing-source'
VIOLATION: entities[5].provenance[0]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
VIOLATION: entities[5].provenance[2]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
6 violation(s); no canon changed
EXIT=1
```

All three records disclose the unknown-source latch; the later ambiguity is still reported as
its own finding but does **not** hijack the first-cause text. Record `[2]`'s hidden chain break
and decreasing tick stay unreported. Claim (b) **confirmed**.

### (c) `r88-nonholder-stop` — non-holder stop discloses per record

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-nonholder-stop
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'f1-nonholder-missing-source'
VIOLATION: entities[3].provenance[0]: … first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: … first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: … first stop: unknown source 'f1-nonholder-missing-source' at entities[3].provenance[0]
4 violation(s); no canon changed
EXIT=1
```

No holder ambiguity is reported (the fixture is otherwise well-formed). Claim (c) **confirmed**.

### (d) 5 r85 live probes vs `dfd1fbc`

| probe | before exit / lines | after exit / lines | identical? |
|---|---|---|---|
| `r85-control` | 0 / 0 | 0 / 0 | **yes** (stdout sha256 `afe570fc…` both) |
| `r85-harbor-repro` | 1 / 7 (1 legacy notice) | 1 / 6 (2 disclosures) | no |
| `r85-isolated-ambiguous` | 1 / 4 (1 legacy notice) | 1 / 3 (1 disclosure) | no |
| `r85-masked-ambiguous` | 1 / 5 (1 legacy notice) | 1 / 4 (2 disclosures) | no |
| `r85-unique-break-control` | 1 / 1 | 1 / 1 | **yes** (sha256 `1a218a9a…` both) |

**The "additions-only" part of the seat-block hypothesis does not hold, and "exits fixed" is not
observable.** What actually happens on the three ambiguity probes: the legacy global-notice line
(`…unassessed at this and all later records because holder identity is ambiguous`) is **removed**,
the per-record lines are reworded into the new grammar, and one non-disclosure finding survives.
Net line count goes **down** by one on each. Exit codes are `0,1,1,1,1` before and after, and they
also match the exits recorded at r85 in `corpus/live/runs/round-85/probe-r85-*.txt` — no exit
changed anywhere in this round. Coverage is preserved: the removed notice asserted scope
("and all later records") which the new grammar states extensionally, one line per affected record.

### Independent census (my own, not V1/X1/X3)

```
$ python3 /tmp/JCAL3-census.py
baseline dirs: 145  exit0 before=30 after=30
violation lines before=331 after=352
changed tuples: 9
   ('r61-independent-empty', 1, 1, 17, 18)
   ('r61-independent-unavailable', 1, 1, 6, 7)
   ('r87-masked-break-from-ambiguous', 1, 1, 6, 5)
   ('r87-masked-break-to-ambiguous', 1, 1, 6, 5)
   ('r87-probe-entry-shape', 1, 1, 2, 8)
   ('r87-probe-multi-invalid', 1, 1, 6, 5)
   ('r87-probe-nonitem-kinds', 1, 1, 8, 9)
   ('r87-probe-record-and-chain', 1, 1, 34, 46)
   ('r87-probe-shape-ambiguous', 1, 1, 2, 5)
```

Fixture dirs: 145 at `dfd1fbc` → **149** at `2ea9ef1` (`find … | wc -l`), the 4 new dirs being
`r88-m3-maya-cluster`, `r88-mixed-stop`, `r88-nonholder-stop`, `r88-shape-ambiguous-armed`.
This reproduces the C1 claim's "9 changed + 4 new of 149 dirs, 0 exit changes" exactly, and
reproduces the two pre-r87 additive r61 disclosures.

### Grammar audit (all 149 dirs)

```
total disclosure lines: 47
missing qualifier: 0
non-contiguous disclosure runs: 0
```

Every disclosure carries `(input-structural finding, not sourced-canon)`, and every disclosure
run starts at the stop origin and is contiguous — i.e. **every** record at/after the stop is
disclosed, with no gaps. 13 distinct first-stop causes observed.

### Pre-r87 before-states (reconstructed from `patches/B3-before-state.json`)

| residual | B3 before-state | after on `2ea9ef1` | closed? |
|---|---|---|---|
| (i) shape-invalid + ambiguous never arms | `r87-probe-shape-ambiguous`: 2 findings, 0 unassessed lines | 2 → **5** findings, ambiguity now reported, **2** disclosures | yes |
| (ii) mixed-stop over-attribution | scratch: 7 findings, 4 unassessed lines, global notice index 1, disclosed cause = the later ambiguity at `[1]` while `first_stop` was the unknown source at `[0]` | `r88-mixed-stop`: 6 findings, 3 disclosures, all naming the unknown source | yes |
| (iii) non-holder stop, no disclosure | scratch unknown-source-only (sources.json removed): 1 finding, 0 disclosures | reproduced as `/tmp/JCAL3-probes4/no-sources-json`: 1 → **4** findings, **3** disclosures (`source table unavailable`); durable `r88-nonholder-stop` covers the unknown-in-world-source sub-case (4 findings, 3 disclosures) | yes |

Note: the three r88 fixtures do not exist at `dfd1fbc`, so a baseline run against them returns
five `cannot load JSON` lines. That is an artifact and is **not** a before-state; the before-states
above are the B3 receipts, and the (i) before-state is re-measured directly on the pre-existing
`r87-probe-shape-ambiguous` (2 findings, sha256 `979ff05f…`, matching B3 exactly).

### Scratch probes for uncovered stop causes

| probe | constructed from | exit | disclosures | first stop |
|---|---|---|---|---|
| dangling-first | item-chain-valid, `[0].to_holder='ghost-holder'` | 1 | 3 | `dangling holder to_holder 'ghost-holder' at entities[3].provenance[0]` |
| nonitem-first | item-chain-valid, `seal.kind='relic'` | 1 | 3 | `provenance attached to a non-item entity at entities[3].provenance` |
| dupitem-first | item-chain-valid + second `seal` | 1 | 4 | `duplicate item id 'seal' at entities[3].provenance` |
| both-amb-and-unknown | duplicate `mira` + unknown source on `[0]` | 1 | 2 | `ambiguous holder identity to_holder 'mira' at entities[3].provenance[0]` |
| dangling-and-unknown | dangling `ghost` + unknown source on `[0]` | 1 | 2 | `dangling holder to_holder 'ghost' at entities[3].provenance[0]` |

The dangling-holder branch of residual (iii) — named in the wave spec but not covered by a
durable fixture — is closed.

## Findings & named debt

**Verdict recommendation for C1 (calibration): `improved`.**

All three r87 residuals are closed on the delivered tree, and the round's after-state matches the
wave-spec wording exactly: every record at/after any provenance stop carries a disclosure naming
the actual first cause; ambiguous holder ids on shape-invalid dict records arm the stop; the prior
145 fixture tuples are preserved except the enumerated deltas. No exit code, no stderr, and no
non-disclosure violation line was removed anywhere; 136 of 145 tuples are byte-identical, and the
two pre-r87 r61 changes are pure additions. The new detection on
`r87-probe-shape-ambiguous` (`…to_holder: ambiguous entity 'dup'`) is a genuine gain: that
ambiguity was previously reported nowhere.

Named debt (none of these reverses the verdict; they are follow-ups):

1. **Same-record multi-cause asymmetry (C1, worth a line in the round record).** The combined
   cause summary exists only on the shape-invalid dict branch. On a *shape-valid* record with two
   simultaneous causes the summary names one by precedence — holder ambiguity or dangling holder
   before unknown source — while the other cause is reported as its own finding. Probes:
   `both-amb-and-unknown` (first stop names the ambiguity, not the unknown source) and
   `dangling-and-unknown` (names the dangling holder, not the unknown source). No information is
   lost, but "the actual first cause" is a documented precedence choice on that branch rather than
   an exhaustive summary. Suggested fix: reuse the `record_stop_cause`-combination idiom from the
   shape-invalid branch, or record the precedence order in E1/SCORECARD so the choice is
   intentional rather than incidental.
2. **Counter inconsistency in the wave evidence.** `patches/V1-delta.json` reports
   `after_summary.violation_lines = 352` while `patches/X3-c1-firstcause-delta.json` reports
   `after_violation_total = 351`; X1 and my census both say 352. X3's `added`/`removed` counters
   count disclosure lines only, so they miss the one added non-disclosure finding
   (`r87-probe-shape-ambiguous …to_holder: ambiguous entity 'dup'`) that X3 itself lists under
   `added_non_disclosure_violation_lines`. Documentation-only; the tree is unaffected. The round
   record should carry 352, not 351.
3. **Wording note, not debt.** The seat-block hypothesis "(d) additions-only" is not literally
   true for the three ambiguity probes: a legacy global-notice line is removed and per-record
   lines reworded. If the round record claims "additions-only", it will be contradicted by the
   r85 probe outputs; the accurate statement is "wording replaced, scope now stated per record,
   net −1 finding on each of the three ambiguity probes, no exit or stderr change".
4. **Residual (iii) has no durable fixture for the dangling-holder sub-case** — only my scratch
   probe. The two durable r88 stop fixtures cover unknown-source and the shape-invalid mixed case.
   If the round wants a receipt in-tree, a fourth fixture (or a record row pointing at the
   dangling case inside `r88-mixed-stop`) would close it.

## Handoff

- Seat deliverable: `.ufo/waves/round-88/followup/JCAL3.md` and
  `.ufo/waves/round-88/followup/JCAL3-receipts.json`. No other repo writes; no commits; sibling
  repos untouched.
- **Verdict recommendation: C1 calibration = improved.** Claim wording (a)–(c) confirmed verbatim;
  claim (d) as stated in the seat block is **partly wrong** — the r85 probes are not
  additions-only and no exits were fixed or changed. The C1 claim's own enumerable-delta phrasing
  ("9 changed + 4 new, 0 exit changes, 2 pre-r87 r61 additive disclosures") is confirmed by my
  independent census and should be used in the round record instead of "additions-only".
- C1 evidence to cite in the round record: the three residual fixtures (5/6/4 findings, exits 1),
  the independent census table above, the 47-disclosure grammar audit (0 missing qualifier,
  0 non-contiguous runs), and the before→after table for the 5 r85 probes.
- Unverified by this seat: C2 (Maya cluster / OBS-1 repair) and C3 (inspiration decision table /
  ledger row) — judged by other seats. I did note that `r88-m3-maya-cluster` contributes the 4th
  new census dir and exits 0 as part of the 30 exit-0 fixtures, but I did not assess its content.
- Open for the round's integration seat: decide whether debt items 1 and 2 get fixed inside round
  88 or are carried to round 89; item 1 is a checker-code change and would invalidate this
  census's after-state if applied, so it must be re-judged if taken.
