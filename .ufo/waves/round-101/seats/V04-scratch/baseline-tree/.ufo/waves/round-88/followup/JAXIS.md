# JAXIS — Axis-verdict synthesizer (round 88 follow-up, world-bible lane)

Seat: JAXIS. Judged tree: **delivered** `2ea9ef13a928475b13fd578740ea521bed4bd649`
(`2ea9ef1`), baseline `dfd1fbc3711f2b28597d74444819aca91fe6bc31`. Every verdict below is
taken on the delivered tree's artifacts, never on intent or on the scratch patches in
`.ufo/waves/round-88/patches/`. Scratch (`/tmp/lore-jaxis-base`, `/tmp/head-*.out`,
`/tmp/base-*.out`, `/tmp/*probe*.py`) was used only for baseline controls and probes.

**This file is a RECOMMENDATION to the L1, not the round's verdict.** The L1 owns the
admission decision and the SCORECARD wording.

## Work performed

- Read every `followup/J*.md` present: `JCAL5.md`, `JCOV3.md`, `JCOV4.md`, `JCOV5.md`,
  `JDEP1.md`, `JDEP2.md`, `JDEP3.md`, `JDEP4.md`, `JDEP5.md`. Also read the non-`J` seat
  reports `K1.md`, `V2.md`, `P2.md`, `P2-scorecard-r88.md`, `P4-shonen.md`, `Q2.md`,
  `SE2.md`, `P3-log-r88.md`, and the JSON receipts `JCAL1-delta.json`,
  `JCAL3-receipts.json`, `JCAL5-delta.json`, `JCOV1-measurements.json`,
  `JCOV2-support.json`, `JCOV3-probes.json`, `JDEP3-probes.json`, `JDEP4-drift.json`,
  `JDEP5-receipts.json`, `H2-delta.json`, `E1-message-inventory.json`.
- Wait-checks (my block: two, 60 s spacing): first at 03:12→03:13 (dir empty at launch,
  5 files after), second at 03:13→03:14. The lane was still landing at 03:16 — `JCOV4.md`,
  `JDEP5.md`, `P3-log-r88.md`, `Q2.md`, `SE2.md` arrived after I had drafted the verdict
  table, so I re-read the late `J*.md` and folded their bounds in (JDEP5's combined-cause
  scope, JCOV4's coverage concurrence). Gaps are listed under "Findings".
- Independently re-derived the whole-tree C1 delta on the delivered tree and on a
  `git archive dfd1fbc` control, without reading `B1-tuples.json` or `V1-delta.json`.
- Independently re-derived the C2 clause/anchor checks, the C3 ledger census, and the
  depth-harm mechanism (dead-string sweep, probe replay, doc inventory).
- Confirmed tree hygiene: `git status --porcelain --untracked-files=no` → ` M
  l0-questions.md` (K1's authorized one-line append). All `corpus/` artifacts are at
  `2ea9ef1`; no other tracked file differs.

## Before → after measurements

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless stated.

### Census and the C1 delta (independent of B1/V1)

```sh
for d in corpus/fixtures/*/; do n=$(basename "$d"); \
  python3 corpus/fixtures/check_bible.py "$d" >/tmp/head-$n.out 2>&1; echo "$? $n"; done > /tmp/head-exits.txt
```

Observed: `total: 149`. Control (same loop in a `git archive dfd1fbc` tree at
`/tmp/lore-jaxis-base`): `total: 145`.

```sh
cut -d' ' -f2- /tmp/base-exits.txt | sort > /tmp/base-names.txt   # and head-names.txt
comm -13 /tmp/base-names.txt /tmp/head-names.txt   # new dirs
comm -23 /tmp/base-names.txt /tmp/head-names.txt   # removed dirs
```

Observed: new = `r88-m3-maya-cluster`, `r88-mixed-stop`, `r88-nonholder-stop`,
`r88-shape-ambiguous-armed`; removed = **none**. Exit-code join over the 145 common
names: **no output** (0 exit changes).

Output-text diff over the 145 common names:

```sh
while read -r n; do diff -q "/tmp/base-$n.out" "/tmp/head-$n.out" >/dev/null || echo "CHANGED: $n"; done < /tmp/base-names.txt
```

Observed — exactly 9:

```text
CHANGED: r61-independent-empty            CHANGED: r87-probe-entry-shape
CHANGED: r61-independent-unavailable      CHANGED: r87-probe-multi-invalid
CHANGED: r87-masked-break-from-ambiguous  CHANGED: r87-probe-nonitem-kinds
CHANGED: r87-masked-break-to-ambiguous    CHANGED: r87-probe-record-and-chain
CHANGED: r87-probe-shape-ambiguous
```

So the seat-block claim **"9 changed + 4 new of 149 dirs, 0 exit changes"** reproduces
exactly, independently. Corroborated by P2 (`dirs=149 exits={"0": 31, "1": 118}
violations=367 changed=9 new=4 exit_changes=0`) and by JCAL5 with its own regenerated
baseline (`own_baseline ... sha256=76cf55c0…`, `changed_count=9 new_count=4
missing_count=0 exit_change_count=0`).

### Did any of the 9 changes lose a *finding* line?

Disclosure lines were stripped and the remainder compared:

```sh
for n in <the 9>; do b=$(grep -v 'provenance continuity and tick-order comparisons' "base-$n.out" | grep -v 'violation(s); no canon changed' | sort); \
  h=$(grep -v 'provenance continuity and tick-order comparisons' "head-$n.out" | grep -v 'violation(s); no canon changed' | sort); \
  [ "$b" != "$h" ] && { echo "NONDISCLOSURE-DIFF: $n"; diff <(echo "$b") <(echo "$h"); }; done
```

Observed: one hit, an **addition**, not a loss —

```text
NONDISCLOSURE-DIFF: r87-probe-shape-ambiguous
2a3
> VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
```

The two pre-r87 `r61-*` deltas are pure additions (`10a11` / `2a3` plus a `+1` count);
the reductions (`r87-masked-break-{to,from}-ambiguous` 6→5, `r87-probe-multi-invalid`
6→5, r85 probes 5→4 / 4→3 / 7→6) remove the superseded r87 *disclosure* wording only.
No non-disclosure finding line disappeared anywhere in the census.

### Disclosure coverage, over-disclosure, duplicates (my own probe)

`/tmp/disclosure_probe.py` parses each fixture's `entities.json` for provenance arrays,
parses the delivered output for `first stop: … at entities[i].provenance[j]`, and asserts
every record at index ≥ j carries a disclosure. Observed:

```text
expected disclosure slots: 35
missing: 0
```

`/tmp/overdisclose.py` checks the converse and duplicates. Observed:

```text
disclosure lines: 47
duplicate-line cases: 0
pre-stop over-disclosures: 0
```

JCAL5's independent sweep agrees: `origin_latches 17 / disclosure_lines 47 /
qualifier_missing 0 / fixtures_with_gaps 0 / disclosures_containing_causal_because 0`.

### The three C1 sub-claims and the qualifier

- (i) shape-invalid dict record arms the stop: `r87-probe-shape-ambiguous` 2 → 5 findings,
  `first stop: malformed record (unexpected field set); ambiguous holder identity
  to_holder 'dup' at entities[5].provenance[0]` on `[0]` and `[1]` (diff above).
- (ii) no over-attribution: `r88-mixed-stop` names
  `first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]`
  on `[0]`–`[2]`; the later ambiguity keeps its own local
  `entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'` line.
- (iii) non-holder causes disclose: `r88-nonholder-stop` → 4 findings, disclosures on
  `[0]`–`[2]`, no holder line.
- Bound on the claim's "combined same-record cause summary": the combination is implemented
  **only for the shape-invalid branch**. `r87-probe-multi-invalid` record `[1]` carries both
  `ambiguous entity 'vault'` and `unknown in-world source 'ghost-source'`, yet its summary
  names only `ambiguous holder identity from_holder 'vault'` (JDEP5 §2 conditions). That is
  not over-attribution — it names a cause that genuinely latched — but it is not a combined
  summary either, so the claim should be read as "combined for the shape-invalid branch".
- Qualifier: all 47 lines carry `(input-structural finding, not sourced-canon)`;
  `grep -c "first occurred at" corpus/fixtures/check_bible.py` → `0`;
  `grep -c "remain unassessed (input-structural finding, not sourced-canon)"` → `1`.
- Checker identity: `sha256sum corpus/fixtures/check_bible.py` →
  `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`, `wc -l` → `395`
  (r87 snapshot per JDEP4: `3ae4134d…`, 356 lines).

### C2 coverage checks

```sh
find corpus/fixtures -name inspiration-note.md | sort        # 2 files (baseline 1)
ls corpus/fixtures | wc -l                                   # 151 entries = 149 dirs + check_bible.py + README.md
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   # CLEAN … 0 violations, exit 0
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster      # CLEAN … 0 violations, exit 0
```

OBS-1 repair, all 8 clause rows of `symbolism-clause-map.md` against the delivered
excerpt (fixed-string):

```sh
grep -o '“\([^”]*\)”' symbolism-clause-map.md | sed 's/^“//; s/”$//' | while IFS= read -r c; do \
  grep -qF -- "$c" lowwater-hymn-excerpt.md && echo "MATCH: $c" || echo "NOMATCH: $c"; done
```

Observed: 8 × `MATCH` (`At low water`, `the shell ring`, `beside the bowl`,
`at the Mother-Tide Gate`, `The bowl keeps no name`, `no voice owns the tide`,
`pass the reed-bell hand to hand`, `let the water return it`). Maya in-world anchors
resolve 4/4 (`fictional-excerpts.md:10–11`) and the cited Spence clauses resolve 2/2
against the source text as written in the excerpt.

### C3 depth checks

```sh
grep -c -i spence corpus/knowledge/reference-ledger.md   # 0
grep -c -i etcsl  corpus/knowledge/reference-ledger.md   # 1
grep -c '^|'      corpus/knowledge/reference-ledger.md   # 6 = header + separator + 4 data rows
```

### The depth-harm mechanism (reproduced)

```sh
grep -rn "unassessed at this and all later records because holder identity is ambiguous" corpus/
grep -rn "unassessed because ambiguous holder identity" corpus/
grep -rln "remain unassessed (input-structural finding, not sourced-canon)" corpus/
```

Observed: the two dead strings occur in exactly two tracked corpus docs —
`corpus/knowledge/holder-assessment-boundary.md` (hits at `:64`, `:104`, `:201`, `:209`,
`:216` and `:70`, `:104`, `:134`, `:202`, `:203`, `:210`, `:217`, `:218`) and
`corpus/knowledge/r87-provenance-chain-decision-table.md` (rows 14/15/27 plus the whole
Receipts block, `:163`–`:277`). The live string occurs **only** in
`corpus/fixtures/check_bible.py`. Neither doc was touched by `2ea9ef1`.

Probe replay against the delivered checker, versus the outputs those docs paste:

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do \
  python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; done
```

| case | doc pastes (as `2b48ca7`) | delivered `2ea9ef1` |
|---|---|---|
| r85-control | `CLEAN`, rc 0 | `CLEAN`, rc 0 (unchanged) |
| r85-unique-break-control | 1 finding, rc 1 | 1 finding, rc 1 (unchanged) |
| r85-masked-ambiguous | 5 findings, old wording | **4 findings**, new wording |
| r85-isolated-ambiguous | 4 findings | **3 findings** |
| r85-harbor-repro | 7 findings | **6 findings** |

The doc's `recheck:` line reads "Re-verify whenever the provenance branch of
`corpus/fixtures/check_bible.py` changes, either notice string or format changes" — both
changed at `2ea9ef1`, so the trigger fired and was not honored.

## Findings & named debt

### Per-axis verdict table (recommendation to the L1)

| axis | verdict | one-line evidence pointer |
|---|---|---|
| **calibration** | **improved (bounded)** | Independent census reproduces `changed=9 new=4 exit_changes=0` of 149 dirs; disclosure probe `35/35` slots, `47` lines, `0` duplicates, `0` pre-stop; the 9 changed outputs lost no finding line (one addition only); V2 verifies 3/3 fixture READMEs line-by-line and shows each discriminates against baseline; JCAL5 reproduces the delta with an independently regenerated baseline. |
| **coverage** | **improved (bounded)** | Census 145→149 dirs, `inspiration-note.md` 1→2, both clusters `CLEAN` exit 0; OBS-1 repair verified `8/8` byte-exact clause matches (my grep); Maya in-world anchors 4/4; JCOV3/JCOV4/JCOV5 concur, and JCOV3 shows each cluster element fires exactly its own template under mutation while the unmutated cluster stays `CLEAN`. Bounds below. |
| **depth** | **harmed (bounded)** | Two `corpus/knowledge/` docs **and seven r87 fixture READMEs** describe superseded checker semantics; the dead notice strings occur in exactly those two docs and nowhere live; the probe outputs the docs paste no longer reproduce (5→4, 4→3, 7→6) and 10/19 of the r87 table's pasted receipts are stale; `r87-probe-shape-ambiguous/README.md` says "unchanged by C1" for the fixture C1 changed (2 → 5 findings). Both docs' own recheck triggers fired. The C3 gains (new decision table + ETCSL row) are real but do not net against the harm. |

Harm findings:

- **H1 (depth, blocking) — two surfaces, not one.** The C1 commit replaced the checker's
  disclosure family without updating the docs that describe it. Both surfaces are on the
  delivered tree and independently reproduced.

  **(a) Two knowledge docs** (`corpus/knowledge/holder-assessment-boundary.md`,
  `corpus/knowledge/r87-provenance-chain-decision-table.md`) state the r87 two-notice
  disclosure family as current delivered behavior and paste finding counts the delivered
  checker no longer produces. Reproduced by me, JCAL5 ("Documentation parity — harmed …
  the trade in the round"), JCAL4 (A5), JDEP4 (`axis_verdict.depth = "harmed"`, 15 + 7
  itemized drift rows), and JDEP5, which machine-replayed **every** pasted CLI receipt in
  the r87 decision table: `pasted_receipts=19 stale_receipts=10`, `exit_changed=false` in
  all ten, stale string occurrences `holder-assessment-boundary.md = 13`,
  `r87-provenance-chain-decision-table.md = 26`. Neither doc is a fabrication — both pin
  their snapshot commit — but no r88 successor exists, and
  `holder-assessment-boundary.md:316-318` now asserts a **wrong fixture census** (nine
  provenance-bearing dirs / "none" combining with a duplicated holder id; delivered:
  19 / 8 per JDEP4), the one stale line that would change an editor's action.

  **(b) Seven r87 fixture READMEs** (H5 F1/F2; JCAL4 A5 counts three as plainly
  contradicted, H5 enumerates seven). Six were accurate at `dfd1fbc` and are false at
  `2ea9ef1`; the seventh was already off by one and is now off by eleven. Sharpest receipt,
  reproduced here verbatim:

  ```sh
  cat corpus/fixtures/r87-probe-shape-ambiguous/README.md | tail -1
  # "Expected: 2 findings, exit 1: … Zero 'unassessed' lines. Pre-existing behavior, unchanged by C1"
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous | tail -1
  # 5 violation(s); no canon changed   (with 2 unassessed disclosure lines)
  ```

  The fixture whose README says "unchanged by C1" is the exact fixture C1 was built to
  change. The other six: `r87-probe-entry-shape` (2 → 8 findings), `r87-probe-record-and-chain`
  (35 → 46), `r87-probe-nonitem-kinds` (8 → 9), `r87-probe-multi-invalid` (6 → 5, and the
  stated emission order no longer holds), `r87-masked-break-from-ambiguous` and
  `r87-masked-break-to-ambiguous` (both still describe the removed item-level notice).
- **No other harm found on any axis.** H1–H4 (harm sweeps) and H5 all report no harm to the
  checker, the corpus, or the exit surface: 150/150 exits unchanged, 0 coverage loss, 0
  non-disclosure finding lost, 0 fabricated receipts. All 145 baseline fixtures keep their
  exit code and every non-disclosure finding line. The harm is confined to the
  documentation/expectation sub-surface, and it is a **trade against the calibration gain**,
  which is why it blocks a clean "improved".

Claim-verification notes (the seat-block claim text vs the delivered tree):

1. C1 — **verifies**, with one wording correction: "prior 145 fixture tuples preserved
   except the claimed deltas" is literally false (9 of the 145 changed), though the same
   sentence enumerates "9 changed + 4 new". `wave-spec.md:20-23` names only
   `r87-probe-shape-ambiguous` as a delta, so the spec's parenthetical under-describes the
   landed change (2 pre-r87 `r61-*` fixtures also changed). Both are additive disclosures;
   no harm, but the round record should state 9, not 1.
2. C2 — **verifies with a precision bound**: "occupied-slot near-miss" does not hold as
   worded. The occupancy key is `(entity_id, tick)`; the pair's keys are `('aru', 9)` and
   `('evin', 9)` — distinct — so the discriminating condition is never evaluated and the
   pair is clean because the actors *and* places differ, not because of tick equality
   (JCOV3 D1). This is claim precision, not a coverage loss. Second bound: the cluster
   delivers **one** printed-page locator (`printed p. 209`), not several passage locators
   (JCOV5 D-JCOV5-3), and its own clause map is `1/2` byte-exact because row 1 writes
   `He called out ‘Earth,’` (single curly) where the excerpt has `“Earth,”` (JCOV3 D2,
   JDEP1 debt 3). Also: this cluster carries no factions, no relation edges, no
   `depends_on` edges and no `contradictions` rows, so it is structurally thinner than the
   r87 cluster (JCOV3 D3, JCOV1 checklist FAILs).
3. C3 — **verifies as worded** (table present with the R1B scope note; ETCSL row
   registered, 4 populated columns, pure append `5a6`, prior rows md5-identical per JDEP2).
   Two gaps: the decision table's own row 6 instructs "register the selected new
   reference(s) at integration" and the same commit registers ETCSL (external-only) while
   leaving **Spence (delivered excerpt) unregistered** (`grep -ci spence
   corpus/knowledge/reference-ledger.md` → `0`); and rows 1/4/5/7 rest on M1/M2 evidence
   that does not exist on the delivered tree (JDEP1 counter-consideration).
4. The C1 claim's "combined same-record cause summary" is **claim-accurate only for the
   shape-invalid branch** (JCAL4 A3, JDEP5 §2): on valid-key-set records with several
   causes the summary names one and drops the rest (case A tick + ambiguous holder → only
   the tick; case B dangling holder + unknown source → only the dangling holder; and the
   shipped `r87-probe-multi-invalid`). The *landed string* never asserts completeness, so
   it is not false — but the claim text and
   `r88-shape-ambiguous-armed/README.md:9`'s "complete simultaneous causes" read as a
   general contract. JCAL4 records this as claim accuracy harmed, not a string defect.

Named debt to carry into the round record:

- **D-JAXIS-1 (blocking, from H1):** refresh the two knowledge docs **and the seven r87
  fixture READMEs** to `2ea9ef1` by fresh replay, not by find-and-replace of the two
  notice strings (JDEP4: ~15 + ~7 distinct drifted items; H5 F2 lists the seven README
  claims row by row). Until then the lane's stated contract and its fixture expectations
  contradict the shipped checker.
- **D-JAXIS-2:** register the Spence reference in `reference-ledger.md` (one row,
  four-column format, rights/training left open) and add the decision table's requested
  delivery-status / `external-only` marker to the ETCSL row (JDEP2 F2/F3, JDEP1 debt 1).
- **D-JAXIS-3:** the delivered decision table is still headed `Draft destination:` and its
  cells read as candidate-stage checks against M1/M2/M3, only one of which landed.
- **D-JAXIS-4:** no durable fixture exercises the `dangling holder …` first-stop cause, and
  no fixture combines two non-shape causes on one record (JCAL5 D-2/D-3).
- **D-JAXIS-5 (carried):** `corpus/fixtures/README.md` still has no `## Round 87` /
  `## Round 88` section (JCOV5 D-JCOV5-2, JCOV3 D4); the kotodama↔lore
  `worldbible-integration-contract.md` is still absent in both lanes (K1, JCOV5 D-JCOV5-1),
  now escalated to `l0-questions.md` by K1's authorized append.
- **D-JAXIS-6:** `corpus/README.md:6` still describes the ledger as "real-world method
  citations" while the delivered ledger is headed "Real-world references" and now carries a
  non-method motif row. Low severity; JDEP2 judged no live doc depends on the old heading
  string, and the stale quotes in `reports/r33…r42-*` are historical.
- **D-JAXIS-7 (process):** the follow-up lane was still landing while it was being judged.
  `K1.md` asserts "JCOV5 never delivered" while `followup/JCOV5.md` landed at 03:14; several
  seats delivered JSON receipts before their `.md` report (`JCAL1`, `JCAL3`, `JCOV1`,
  `JCOV2`, `H2`, `E1` were still JSON-only at my last check). Do not read a missing
  `J*.md` as a missing judgement — read its JSON — and do not freeze a verdict table
  before the lane's arrivals stop.

### Side recommendation: capability rows (JDEP5, reported for the L1's SCORECARD)

Not an axis verdict, but it interacts with the depth harm and belongs in the round record:

- **FOR** a `provenance stop-cause assessment` capability row. The capability runs on the
  delivered tree (14 stop-cause classes disclosed at the stop record and every later
  record), is replayable from the repo alone via the three durable r88 fixtures, and was
  demonstrated by a non-author judge (JDEP5 §2).
- **AGAINST** a `sourced-inspiration verification` capability row this round. The only
  runnable evidence pointer is the rule text, and running that rule literally against the
  cluster landed in the same commit fails `1/2` — the M3 map transcribes the excerpt's
  inner double quotes as single quotes (JDEP5 §3, JCOV3 D2). Entering it now would be
  pre-claiming. Carry JDEP5's three-step r89 path.
- If the CAP-1 row is entered, JDEP5 warns it would sit beside a decision table that
  contradicts the shipped checker, so D-JAXIS-1 should be discharged in the same
  integration commit.

### Admission recommendation to the L1

**Do not admit round 88 as-is.** The round's own rule is "admit only if every claim
verifies and no axis harmed; a trade is NOT an improvement". C1 and C2 verify with named
bounds, but the depth axis carries a reproduced, in-repo harm (H1) introduced by the same
commit that produced the calibration gain — the two knowledge docs that state the
provenance contract now contradict the shipped checker, and their recheck triggers fired.

Two acceptable resolutions, in cost order:

1. **Repair then admit (recommended).** Have a follow-up seat re-derive
   `holder-assessment-boundary.md`, `r87-provenance-chain-decision-table.md`, and the seven
   r87 fixture READMEs from a fresh replay at `2ea9ef1` (D-JAXIS-1), then admit with depth
   `improved (bounded)` and D-JAXIS-2…7 carried. This is a documentation refresh, not a
   checker change, so it cannot re-open the C1 census. (A `CB1-boundary-refresh.md` seat
   landed in `followup/` during this wave; check whether it already contains a usable
   refresh before commissioning a new one.)
2. **Admit with an explicit, recorded bounded harm.** If the L1 prefers not to reopen the
   round, admit with depth `harmed (bounded)` stated as such in the SCORECARD row and
   D-JAXIS-1 as the first r89 work item — never as `improved`, and never as a trade netted
   against the C3 gain.

Either way, calibration and coverage should be recorded as `improved (bounded)`, and the
C2 wording should be corrected from "occupied-slot near-miss" to "same-tick, distinct-slot
pair" (D-JAXIS-2's precision bound) rather than left as a claim the artifact does not
support. Note for the L1: P1's own draft round report leaves all three axis cells
`PENDING-L1` and explicitly refuses to rule the depth split (`P1.md:115-117, 150-151`), so
this table is the input it is waiting for.

## Handoff

- Deliverable: `lore-shokunin/.ufo/waves/round-88/followup/JAXIS.md` (this file). No other
  repo write; no commit; no push. `l0-questions.md`'s single modification is K1's
  authorized append, not mine.
- Reproduce my census in one pass: loop `python3 corpus/fixtures/check_bible.py` over
  `corpus/fixtures/*/` at HEAD and in a `git archive dfd1fbc` tree, then compare the
  `exit name` maps and the captured stdout files (expect 149 / 145 dirs, 0 exit changes,
  9 changed outputs, 4 new dirs, 0 removed).
- Reproduce the harm in one line:
  `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous`
  → 4 findings on the delivered tree, while `corpus/knowledge/holder-assessment-boundary.md:198-205`
  pastes 5.
- Blocker for a repair seat: D-JAXIS-1 is a re-derivation of two docs (strings, counts,
  line refs, fixture census), not a two-string find-and-replace.
- Bounds of this seat: I judged only the three owned axes and the delivered tree; I did not
  re-derive every C3 row, did not fetch external URLs (JDEP2/JCOV3 did), and did not
  adjudicate the 9 changed tuples tuple-by-tuple against their individual READMEs beyond
  the finding-line-preservation check above.
