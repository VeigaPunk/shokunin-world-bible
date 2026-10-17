# JCOV2 — map-discipline judge, round 91 (follow-up)

Judged axis: C2 map discipline — the three maps' `## Inventory` lines against the
raw JSONs, the load-bearingness of the inventory assertion, and the r88-m3
unreferenced-declaration WARN as the surfacing of the Spence-bullets gap.

**Verdict on the judged axis: improved (bounded).** No blocking finding; no harm
observed. Evidence is the delivered tree at `c2ab3d0` (baseline `a7c6a17`); every
probe ran on scratch copies under `/tmp/jcov2/`; no tracked file was touched by
this seat.

## Work performed

1. Confirmed the judged tree: `c2ab3d0`, `git status` tracked-clean; checker
   hashes `support_check.py` = `9da149b8e51f5c6c39477f17b8b19d17da3568a1a7c72412079efccff1f330bf`,
   `check_bible.py` = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
   (the latter matches the C9 watch pin at `corpus/knowledge/r91-c9-watch.md:6`).
2. Two timestamped 60 s stability checks (no blocking dependency artifact was
   declared; the work was committed before this seat started, so these are
   stability receipts):

   ```text
   check#1 2026-10-17T08:34:23-03:00 HEAD=c2ab3d0 tracked_diff=0 untracked=1 support256=9da149b8 bible256=ff9fd2aa
   check#2 2026-10-17T08:35:23-03:00 HEAD=c2ab3d0 tracked_diff=0 untracked=1 support256=9da149b8 bible256=ff9fd2aa
   ```

   (`untracked=1` is the sibling-created `.ufo/waves/round-91/followup/` directory;
   HEAD and both hashes stable.)
3. Re-ran the delivered checker on all three clusters (r87, r88-m3,
   r89-inspiration-paraphrase) — receipts in the next section.
4. Independent recount and parse (own script, no repo writes): declared inventory
   vs independently parsed table rows vs the raw JSON census (`source_id` keys +
   `first_appearance` pointers), plus resolution of every backticked JSON pointer
   in fact rows and a source-cell-vs-raw-value comparison.
5. Seven scratch probes: A/B/C/E (inventory tampering), D (WARN direction
   control — add a referencing row), F (delete the declaration row), G (header
   rename). A/B/G were also run through the r90 checker
   (`git show a7c6a17:corpus/tools/support_check.py`, sha256 `66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472`)
   on identical inputs as the before side.
6. Read the delivered `corpus/tools/README.md` and the r90 `JCOV3.md` findings
   for the F-label mapping (see F3 below).

## Before → after measurements

**BEFORE — r90 checker (a7c6a17) on the delivered clusters and tampered inputs.**
Exact commands: `python3 /tmp/jcov2/old_support_check.py corpus/fixtures/<cluster>`.

```text
$ python3 /tmp/jcov2/old_support_check.py corpus/fixtures/r87-myth-cluster
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
exit=0
$ python3 /tmp/jcov2/old_support_check.py corpus/fixtures/r88-m3-maya-cluster
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
exit=0
$ python3 /tmp/jcov2/old_support_check.py corpus/fixtures/r89-inspiration-paraphrase
SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
RESULT PASS
exit=0
```

The r90 tool prints the aggregate `SOURCE-SUPPORT 22/22` (rows, not JSON facts),
no inventory line, and no warning for the unreferenced `source-excerpt.md`
declaration. On tampered inputs it stays silent: declared-count tamper (maps A/B)
→ `22/22` / `10/10` and `RESULT PASS`, exit 0; renamed `ID` header (map G) →
`SOURCE-SUPPORT 8/8` and `RESULT PASS`, exit 0 (reproducing the r90 JCOV4
header-rename vector on the delivered tree's inputs).

**AFTER — delivered checker (c2ab3d0), exact commands and observed output**
(per-row `PASS` lines omitted; 33 rows total across the three runs: 22 + 10 + 1):

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 0; TOTAL-ROWS 10
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10; VALIDATED-ROWS 10/10
WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
RESULT PASS WITH WARNINGS
exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
exit=0
```

**Inventory lines vs raw JSONs (independent recount).**

```text
r87-myth-cluster : declared (14, 8, 22, 22) == independent parse (14, 8, 22, 22) — MATCH
  raw source-attributed JSON facts (source_id OR first_appearance) = 22
  = 7 first_appearance + 7 claims + 4 relations + 4 timeline
  row pointer tokens 42/42 resolve; source cell agrees with raw value 14/14 rows;
  the 8 editorial rows carry 0 JSON pointer tokens
  raw coverage: 20 pointers row-level (6 claims + 4 relations + 4 events + 6
  co-mapped first_appearance) + 2 note-level (entities[2].first_appearance,
  entities[2].claims[0], both named at claim-excerpt-map.md:60) = 22/22 disclosed
r88-m3-maya-cluster : declared (10, 0, 10, 6) == independent parse — MATCH
  raw census = 10 exactly (4 first_appearance + 4 claims + 2 timeline) — bijection
  row tokens 10/10 resolve; source cell 10/10 agrees
r89-inspiration-paraphrase : declared (1, 0, 1, 1) == independent parse — MATCH
  row token entities.json#/0/claims/0 resolves; source cell agrees
  raw census = 2 (the mapped claim + an undeclared entities[0].first_appearance)
```

**Inventory-assertion probes** (scratch copies; commands
`python3 corpus/tools/support_check.py corpus/fixtures/<cluster> --map /tmp/jcov2/<file>`):

```text
A-r87-count   declared 14→13 / total 22→21 (sum kept):
  INVENTORY JSON-FACTS 14/13; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/21; DISTINCT-ANCHORS 22/22
  FAIL: inventory JSON facts mismatch: expected=13 parsed=14
  FAIL: inventory total mapped rows mismatch: expected=21 parsed=22
  exit=1
B-r88-count   declared 10→11 / total 10→11 (sum kept):
  INVENTORY JSON-FACTS 10/11; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/11; DISTINCT-ANCHORS 6/6
  FAIL: inventory JSON facts mismatch: expected=11 parsed=10
  FAIL: inventory total mapped rows mismatch: expected=11 parsed=10
  exit=1
C-r87-sum     declared total 22→23 (sum broken):
  stdout empty; STDERR: FAIL: expected JSON facts and editorial rows must sum to total mapped rows
  exit=2
E-r87-dropped H8 row deleted, declaration untouched:
  INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 7/8; TOTAL-ROWS 21/22; DISTINCT-ANCHORS 21/22
  FAIL: inventory editorial rows mismatch: expected=8 parsed=7
  FAIL: inventory total mapped rows mismatch: expected=22 parsed=21
  FAIL: inventory distinct excerpt anchors mismatch: expected=22 parsed=21
  exit=1
G-r87-header  `| ID |` → `| Row |` on the JSON-facts header:
  INVENTORY JSON-FACTS 0/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 8/22; DISTINCT-ANCHORS 8/22
  4 WARNs (unreferenced declarations gate-witness/dune-register/shell-charter/tide-bell-tally)
  FAIL: inventory JSON facts mismatch: expected=14 parsed=0
  FAIL: inventory total mapped rows mismatch: expected=22 parsed=8
  FAIL: inventory distinct excerpt anchors mismatch: expected=22 parsed=8
  exit=1
```

So the assertion fails a tampered count in both directions it exists to catch
(declaration too low: A; too high: B; a dropped row: E; a header rename that
silently dropped 14 rows in r90: G — `8/8` PASS before, `0/14` FAIL after), and
has a separate load-bearing sum guard (C, exit 2). Probe D below shows a
consistent map still passes.

**WARN direction controls.**

```text
D-r88-rowadd  one row added referencing source-excerpt.md:5 (verbatim, anchor
              `He called out “Earth,”`), declared 11/0/11/7:
  INVENTORY JSON-FACTS 11/11; EDITORIAL-ROWS 0/0; TOTAL-ROWS 11/11; DISTINCT-ANCHORS 7/7
  PASS S1: source-support; mode=verbatim; anchor=found; 5:> ... He called out “Earth,” ...
  SOURCE-SUPPORT 11/11; EDITORIAL-ANCHORS 0/0; MODES 11/11; VALIDATED-ROWS 11/11
  RESULT PASS        (no WARN lines at all)
  exit=0
F-r88-nodecl  the `source-excerpt.md:5` declaration row deleted:
  INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
  RESULT PASS        (no WARN line)
  exit=0
```

## Findings & named debt

- **F1 — the inventory assertion is load-bearing.** A/B/E/G fail non-zero with
  exact `expected=`/`parsed=` diagnostics on the delivered tree; C exercises the
  separate sum guard (exit 2, stderr only); D (consistent map) passes at exit 0.
  Bound (already named debt, `M2.md`): the inventory is **self-attested** — a
  coordinated row+declaration edit can still agree. The assertion catches
  accidental loss, header drift, and duplication, not adversarial self-consistency.
- **F2 — all three Inventory lines match the raw JSONs and the parsed tables.**
  r87 `14 JSON facts; 8 editorial rows; 22 total mapped rows; 22 distinct excerpt
  anchors.` — the 14 correspond to 6 claims + 4 relations + 4 events; the 8
  editorial rows are genuinely non-JSON (0 pointer tokens). The r87 raw census is
  22 source-attributed pointers, and the map itself discloses the set arithmetic
  at line 60 (20 row-level + 2 note-level); nothing is hidden. r88-m3
  `10; 0; 10; 6` is an exact raw-census bijection. Residual wording bound:
  `RECEIPT JSON-FACTS 14` is still the *mapped task-scope* count, not the raw
  22-pointer census — JCOV3's full ask (a raw-fact denominator) was surfaced but
  only the JSON/editorial split was implemented; minor named wording debt, no
  receipt effect. The paraphrase demo map's line (`1; 0; 1; 1`) was added in
  `c2ab3d0` and parses and passes.
- **F3 — WARN correctness; the mission's "JCOV3-F4" is the F5 text.** The
  bullets-not-rows finding is **F5** in the r90 report
  (`.ufo/waves/round-90/followup/JCOV3.md:188-194`: "The two Spence comparisons
  are map bullets, not rows"); r90 F4 (`:184-187`) is the R9-enforcement
  controls, and the r91-followup `JCOV3.md` carries no F-numbering. Judged
  against F5's wording: the delivered r88-m3 run emits exactly one WARN,
  `unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)`; all 10
  fact rows reference `fictional-excerpts.md`, and the two Spence comparisons
  are bullet lines (`claim-excerpt-map.md:38-39`) — so the WARN is precisely the
  map's declaration-without-any-referencing-row state, i.e. the correct
  surfacing of F5's symptom. Control D proves the direction (adding one row that
  references `source-excerpt.md:5` clears the WARN and the passage enters the
  receipt). Control F shows the bound: **the WARN is declaration-conditioned** —
  deleting the declaration row also clears it while the comparisons stay
  unrepresented, so the guard is "declaration without rows", not "editorial
  comparison not represented". Non-blocking by design (M2 named debt).
- **F4 — r92 row-add debt (named, per the commit message "r92" note).** Add the
  two Spence comparison pairs as mapped rows under a new `## Editorial rows`
  section (absent from the r88-m3 map today): source side `He called out
  “Earth,”` and `and the solid land appeared.` at `source-excerpt.md:5`; authored
  side `We leave its name unowned in the rain.` at `fictional-excerpts.md:8` and
  `The chalk stair stays a crossing, never a map.` at `fictional-excerpts.md:7`.
  Constraint: a row has one excerpt path/anchor, so the two-sided comparison
  shape (one row per side vs one row plus a note) is r92's design decision.
  Expected effect: the WARN clears because `source-excerpt.md` becomes
  referenced, and the comparisons enter `EDITORIAL-ROWS`/`EDITORIAL-ANCHORS`
  instead of living outside the receipt's denominator.
- **F4b — paraphrase demo map, two minor observations (no receipt effect).**
  (i) Its inventory line sits at `claim-to-excerpt-map.md:3` with no
  `## Inventory` heading, unlike r87/r88 — compliant with the parser and the
  README contract, cosmetically inconsistent; (ii) the raw fixture carries a
  second source-attributed pointer, `entities[0].first_appearance` (raw census 2
  vs declared 1), which no row references and no note names — consistent with
  the demo's declared "1 claim-pointer row" scope but an undisclosed omission if
  the demo is read as a census.
- **F5 — corroboration.** The two README-named M2 contract deviations (missing
  inventory exits 2; no terminal `RESULT FAIL`/`RESULT ERROR`) are documented at
  `corpus/tools/README.md:16-21` and match observed behavior; the sibling r91
  JCOV1 report ran overlapping attack cases (header rename, duplicate row, Spence
  flip, missing inventory) with matching results, independently of this seat.

## Handoff

- **Files written:** `.ufo/waves/round-91/followup/JCOV2.md` (this report) only.
  Scratch `/tmp/jcov2/` (8 files) was removed after reporting; the probe recipe
  is the substitutions and row insertion named in the measurements above.
  No commits, no pushes; no sibling repo touched.
- **Verdict:** C2 map-discipline angle — improved, bounded; no blocking finding.
  All verdict evidence is from the delivered tree at `c2ab3d0`; the a7c6a17
  checker runs are BEFORE context only.
- **Gaps:** `JCOV3-denominators.json` carries no F-numbered entries (grep empty),
  so F-labels are cited from `JCOV3.md` text; the mission's "JCOV3-F4" was
  judged as the F5 wording above. No timing gap — the dependency (work commit)
  predated this seat, and the two 60 s checks show the tree stable.
- **r92 candidates:** the Spence row-add (F4); optionally the raw-fact
  denominator wording (F2) and the demo map's heading/pointer disclosure (F4b).
  The self-attested-inventory bound (F1) has no cheap fix and stays named debt.