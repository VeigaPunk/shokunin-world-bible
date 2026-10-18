# V10 — preservation-census (round 102, capstone)

Seat: V10, verifier (preservation census). Lane: lore-shokunin; round 102; date 2026-10-18;
model zai-coding-plan/glm-5.3-flash-low. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Report path exclusive: `.ufo/waves/round-102/seats/V10-preservation.md`.
Scratch (declared): `.ufo/waves/round-102/seats/V10-scratch/` (raw evidence: `baseline-git-status.txt`,
`knowledge-inventory-baseline.txt`, `draft-evidence.md`).
Leaf seat: no nested agents, no commits, no pushes, no network.

## Method

All commands run from the lane root with `python3`-available system tools. Producer gate per the
poll-wait protocol: both producer reports AND all three r102 artifacts present before the final
census; checks every 20 s; census re-run only on the post-producer tree.

## 1. Fixture census — 174, no new fixture — VERIFIED

Observed (final sweep 06:43:12, identical at baseline 06:19):

```
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
174
$ ls corpus/fixtures | wc -l
176
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type f -exec ls -la {} \;
… corpus/fixtures/check_bible.py  (22880 B)
… corpus/fixtures/README.md       (85211 B)
$ git ls-files corpus/fixtures | wc -l
1050
$ git status --porcelain corpus/fixtures | wc -l
0
```

The raw `ls` count of 176 = 174 fixture **directories** + the 2 pre-existing top-level helper
files (`check_bible.py`, `README.md`). The census number 174 counts fixture dirs and matches the
repo's own record (LOG.md:3445 "census 174/40/134/421"; LOG.md:3541 "census 174 unchanged").
Expectation "174, no new fixture" — **met**. All 1050 fixture files tracked, zero dirty: no
fixture created, deleted, or modified this round.

## 2. Producer gate — reached after recorded stall-escapes

Poll log (20 s cadence): window 1 try=1 06:19:50 → try=30 06:29:30 (background task hit its own
600 s cap at try 30); window 1b try=31 06:30:18 → try=40 06:33:18 — **full 40-try budget exhausted
with producers absent** (`POLL-40-EXHAUSTED`). Three bounded stall-escape extensions were then
taken under the ENDGAME CONVENTION, each justified by observed producer progress, all recorded:

- ext2 (06:34:25–06:38:45): U2 artifact landed 06:35:45, U2 report 06:36:25, U1's
  `r102-debt-ledger.json` 06:38:25.
- ext3 (06:39:16–06:42:16): U1's `r102-push-synthesis-r95-r102.md` landed 06:41:36.
- ext4 (06:43:00): U1 report `U1-synthesis.md` present → **gate open**.

At census time all five existed: `U1-synthesis.md` (4918 B, 06:42), `U2-freshness.md`
(5019 B, 06:36), `r102-push-synthesis-r95-r102.md` (15804 B, 06:41), `r102-debt-ledger.json`
(122763 B, 06:39), `r102-freshness-sweep.md` (12093 B, 06:35). Census snapshot taken 06:43:12.
Both producer reports declare their write-sets closed ("no other file written or modified by this
seat" / "No other files written").

## 3. Inherited-change classification — every change declared, zero unexpected — VERIFIED

Full working-tree diff vs HEAD at 06:43:12:

```
$ git log --oneline -1
8fa2e87 lore r102: declare capstone round before dispatch — final round of the loop
$ git diff --name-only HEAD
corpus/knowledge/2026-10-12-malformed-error-patterns.md
corpus/knowledge/r91-c9-watch.md
$ git status --porcelain
 M corpus/knowledge/2026-10-12-malformed-error-patterns.md
 M corpus/knowledge/r91-c9-watch.md
?? .scratch/
?? .ufo/waves/round-102/
?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
?? corpus/knowledge/r102-debt-ledger.json
?? corpus/knowledge/r102-freshness-sweep.md
?? corpus/knowledge/r102-push-synthesis-r95-r102.md
```

Classification of every path:

| # | Path | Class | Declared by |
|---|------|-------|-------------|
| 1 | `M corpus/knowledge/2026-10-12-malformed-error-patterns.md` | U2 dated correction addendum (dangling `b6ca1e90…` pin) | U2 (owned byte #2) |
| 2 | `M corpus/knowledge/r91-c9-watch.md` | U2 dated r102 re-check addendum (C9 re-check 11) | U2 (owned byte #3) |
| 3 | `?? corpus/knowledge/r102-push-synthesis-r95-r102.md` | U1 artifact (C1) | U1 (owned byte #1) |
| 4 | `?? corpus/knowledge/r102-debt-ledger.json` | U1 artifact (C2) | U1 (owned byte #2) |
| 5 | `?? corpus/knowledge/r102-freshness-sweep.md` | U2 artifact (C3) | U2 (owned byte #1) |
| 6 | `?? .ufo/waves/round-102/` | seat reports + scratch (procedural surface, this file included) | round convention |
| 7 | `?? .scratch/` | pre-existing untracked noise — present at first baseline poll 06:19:50, before any seat wrote | recorded class |
| 8 | `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md` | pre-existing r98 leftover — present at first baseline poll 06:19:50 | recorded class |

Results:

- **Modified tracked files: exactly 2, exactly U2's two declared addenda.** Both are pure
  append-style corrections, not rewrites:
  `git diff --stat HEAD` → `…error-patterns.md | 15 +++++++`, `…r91-c9-watch.md | 46 ++++++++++++++++++`,
  `2 files changed, 61 insertions(+)` — zero deletions; both carry dated, signed headers
  ("## Correction addendum (2026-10-18, round 102, freshness seat U2)"; matching r102 re-check
  addendum in the C9 watch).
- **New files in `corpus/`: exactly 3, exactly the three declared r102 producer artifacts.**
  No undeclared knowledge file, no fixture, no tool, no index surface touched.
- **No modifications anywhere outside the two U2 addenda** (`git diff --name-only HEAD` is
  exhaustive over tracked files).
- **Producer cross-attribution agrees:** U1's report attributes the two `M` files to U2's
  declared ownership; U2 declares exactly those two addenda plus the sweep. No contradiction.
- **HEAD unmoved** at `8fa2e87` throughout (baseline `git rev-parse HEAD` =
  `8fa2e87b40b74f8f78864b7044ed0345712af605`; re-checked at census). This seat made no commits.
- Pre-existing untracked noise (#7, #8) predates the round's producer work (first observed
  06:19:50) and is unchanged in kind at census; it is not an inherited round-102 change.

**Zero unexpected changes.**

## 4. Residues recorded (evidence, not adjudication)

- The census is a snapshot at 06:43:12 after both producers declared their write-sets closed;
  any later byte would be outside this census (none observed through report writing).
- U2's own caveat stands: their sweep ran (06:35) before U1's artifacts landed (06:39/06:41);
  U2 explicitly scoped C1/C2 verification out — consistent with byte-ownership, noted for the
  integrator, not a preservation defect.
- U1's report phrases the census as "175 dirs listed minus self = 174"; this seat's direct count
  is 174 dirs — consistent with the r101-closure number either way.
- Poll protocol deviations: 3 recorded bounded stall-escape extensions beyond the 40-try budget
  (§2), each taken only on observed producer progress; no plan was ever verified.

## Bottom line

**PASS — fixture census 174 (no new fixture, 0 fixture files dirty); every inherited change is a
declared producer path (U1: 2 artifacts; U2: 1 artifact + exactly 2 dated addenda, 61 insertions /
0 deletions); zero unexpected changes on the delivered tree at HEAD `8fa2e87`.**
