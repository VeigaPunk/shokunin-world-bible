# V47 — dormancy-check (round 95)

Seat: V47 dormancy-check. Scope per seat spec: after all seats, verify (a) LOG.md
gained the r95 declaration this round (`git log --oneline -3`) and (b) the round
produced reports — the dormancy-rule inputs for the L1.

Baseline: HEAD `fb118c4` (r94 closure). All commands from repo root, read-only.
Observation window 16:16:44–16:31:59 local (2026-10-17). This report is the only
file this seat wrote.

## Method

- Initial recon of git state + LOG.md tail at ~16:16:44.
- Poll-wait window per protocol: 20 s cadence, 40 tries, 16:18:06 → 16:31:26,
  counting `.ufo/waves/round-95/seats/*.md` (seat reports at the declared
  exclusive path, root level only; `*-scratch/` subdirs and helper scripts
  excluded). Final snapshot at try 40 plus follow-up `ls` at 16:31:43 and
  16:31:59.

## Input 1 — LOG.md gained the r95 declaration this round: PRESENT

```
$ git log --oneline -3
fb118c4 lore r94: close round — SCORECARD admitted section + LOG closure (corrections, gaps, r95 handoff)
ac69044 lore r94: land admission conditions C-1..C-4,C-6 — map_obligations registry row, README addenda, C9 r94 re-check, filled follow-up receipt
65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch
```

Same output at 16:16:44 and 16:31:43: HEAD is still the r94 closure; no r95
commit exists — expected, since leaf seats must not commit and the round is not
closed. So "gained this round" can only be a working-tree fact, verified against
HEAD:

```
$ git show HEAD:LOG.md | grep -n "Round 95" ; echo "EXIT=$?"
EXIT=1                      # r95 section absent from HEAD's committed LOG.md

$ git diff --stat LOG.md
 LOG.md | 57 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 57 insertions(+)
```

The +57-line hunk is exactly the `## Round 95 — declaration before dispatch
(2026-10-17)` section (C1 calibration / C2 depth / C3 coverage, admission rule,
producer byte-ownership) — matching the round's declared claims. The declaration
is stable: LOG.md sha256 `051e12517c31cb8186911650abe95c613bce4d7dea9f4daaee467460259d00e5`
identical at 16:24 and 16:31:43.

Input 1: **PRESENT** (working-tree declaration gained this round; consistent
with the no-commit rule for open rounds).

## Input 2 — the round produced reports: PRESENT (41 and rising at 16:31:59)

Collection curve, `ls .ufo/waves/round-95/seats/*.md | wc -l` (counts at each
20 s try, 16:18:06 → 16:31:06):

```
try:   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
count: 0  1  1  1  1  1  1  3  3  3  3  5  6  7  8  8  8 11 11 12
try:  21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
count:12 14 15 15 16 16 16 16 17 20 20 21 22 24 27 31 33 35 35 37
```

Then: FINAL 16:31:26 `report_count=39`; 16:31:43 = 40; 16:31:59 = 41. Still
rising at cutoff (~+2/min); 24→35 in the 16:29–16:30 minute.

At 16:31:59 (41 reports; sorted):

```
P1-tool-code.md  P2-contract-docs.md  P3-fixture-json.md  P4-fixture-docs.md  P5-knowledge-note.md
V01-c1-before-after.md  V02-c1-selftest.md  V03-c1-regression.md  V04-c1-negative-rerun.md
V05-c3-dialect-r88.md  V06-c3-fail-closed.md  V07-c3-receipts-unchanged.md
V08-c2-checker.md  V10-c2-support-map.md  V11-c2-anchors.md  V12-c2-whole-claim.md
V13-c2-anti-overclaim.md  V14-c2-dependency-probe.md  V15-preservation-census.md
V16-preservation-mutations.md  V17-gates-boundary.md  V19-freshness.md  V20-doc-parity.md
V22-adjacency.md  V23-verdict-depth.md  V24-verdict-coverage.md  V35-anchor-replica-2.md
V36-whole-claim-replica-2.md  V38-contract-review.md  V39-dialect-audit-2.md
V40-negative-dialect.md  V42-fixture-readme.md  V43-knowledge-note.md  V44-exit-contract-c2.md
V45-census-paths.md  V48-pins-fresh.md  V50-byte-prefix.md  V51-relation-scope.md
V52-support-regression.md  V55-crosscheck-calibration.md  V58-claim-text-audit.md
```

Composition: 5/5 producer reports (P1–P5) present; 36 verifier reports at
16:31:59 (V01–V58 subset), i.e. the round is mid-flight (64 seats dispatched).
This seat's own report (V47) is written after this observation and is not
included in the count.

Supporting activity evidence (all read-only checks):

- Producer artifacts landed: `corpus/fixtures/r95-crossing-aftermath/` present
  from ~16:19 (10 files: `entities.json`, `relations.json`, `contradictions.json`,
  `sources.json`, `timeline.json`, `source-excerpt.md`, `inspiration-note.md`,
  `fictional-excerpts.md`, `README.md`, `claim-excerpt-map.md`);
  `corpus/knowledge/r95-aftermath-scope-note.md` (9718 bytes, mtime 16:25).
- `git status --short` at FINAL shows the expected producer surface:
  `M LOG.md`, `M corpus/tools/README.md`, `M corpus/tools/map-obligations-contract.json`,
  `M corpus/tools/map_obligations.py`, `?? .ufo/waves/round-95/`,
  `?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md`.
- 15 seat scratch dirs under `seats/*scratch*` by 16:24; wave scratch
  `.ufo/waves/round-95/scratch/V20/{census-pre,census-post}.json`.
- Genuineness spot-check (existence-level seat, but one sample inspected):
  `V38-contract-review.md` read at 16:19 contains real receipts — baseline
  sha256 pins and five CLI probes with exit codes — not placeholders.

Input 2: **PRESENT** (round produced reports; 41 at 16:31:59, count rising).

## Boundaries and limitations

- This is an existence-level check by design (cf. r94 note that the fleet
  watchdog's `report_of()` is existence-only). It does NOT adjudicate the truth
  of C1/C2/C3 — the verdict seats own that. Existence ≠ content completeness:
  e.g. V38's report was observed mid-flight at 16:19 with its Step 3 still
  marked "Pending"; reports are live documents.
- The round was still in flight at cutoff (41/64 reports). This snapshot proves
  activity (non-dormant), not round completion; the L1 should re-collect the
  full set at closure.
- HEAD unchanged all round (`fb118c4`); "gained the declaration this round" is
  therefore a working-tree fact — the correct reading of the check for an
  open, no-commit round.

## Bottom line

PASS — both dormancy inputs present: LOG.md gained the r95 declaration this
round (working tree +57 lines, absent in HEAD `fb118c4`; no r95 commit) and the
round produced reports (41 at 16:31:59, still rising; all 5 producer reports
present).
