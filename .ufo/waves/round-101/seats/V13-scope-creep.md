# V13 — scope-creep (round 101, lore-shokunin)

**Bottom line: PASS — zero round-101 scope creep.** Tracked-byte changes are exactly the
four producer-owned paths; every report is exclusive, flat, and one-per-seat under
`.ufo/waves/round-101/seats/`; zero r101-attributable writes anywhere in the parent tree.
Three benign anomalies bucketed and evidenced: lane-root seat scratch (V02/v26), the
inherited r98 stray, and a one-report census surplus vs the declared 28-seat count
(`V25-receipt.md`, landed 00:44 — bookkeeping discrepancy, no byte-ownership violation).

- Seat: V13 (verifier, scope-creep axis), round 101, GLM closing pair 1/2, run 2026-10-18
  00:13–00:47 -03:00 from lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`.
- Axes named up front: (A) full git-status capture + bucketing, (B) report exclusivity,
  (C) parent-tree strays, (D) evidence quality, (E) poll latency.

## Poll timeline (protocol: 20s × ≤40 per poll; stall-escapes recorded, not fatal)

- Primary poll (00:13–00:28, 40/40 tries): producer artifacts complete from try 18
  (`readme_skill_mod=2`, `u2file=yes`); ended at 27 reports incl. U1. **Stall-escape #1.**
  (A first poll launch had a path bug — `seats/` instead of `.ufo/waves/round-101/seats/` —
  caught and relaunched at 00:14; its log is superseded, no finding lost.)
- Extension #1 (00:28–00:42, 40/40 tries): U2 report at try 11 (00:32); ended 27/28 reports.
  **Stall-escape #2.**
- Extension #2 (gate: 28 reports OR 10 stable tries): **complete at try 1 — 28/28 at 00:43:50**
  (V24, V25 landed 00:42–00:43). Endgame battery run 00:44–00:47.

## 1. Git status, bucketed (lane root; final, 00:44)

`git status --porcelain=v1` (verbatim):

```
 M SKILL.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .scratch/
?? .ufo/waves/round-101/
?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
?? corpus/knowledge/r101-r10-register-first-entry.md
```

- **Bucket A — producer-owned (expected, exclusive)**: the four `M` paths = exactly U1's
  declared set (`dependency_freeze.py`, `dependency-freeze-contract.json`,
  `corpus/tools/README.md`, `SKILL.md`). `git diff --stat`: 4 files, +223/−4. No other
  tracked path modified; nothing staged; no deletions.
- **Bucket B — U2-owned artifact (expected)**: `?? corpus/knowledge/r101-r10-register-first-entry.md`.
- **Bucket C — round-101 wave tree (expected)**: `?? .ufo/waves/round-101/` — 29 seat
  reports (28 seats + self; see §2 census) + per-seat scratch dirs. Untracked-by-design
  (baseline had wave tree uncommitted).
- **Bucket D — seat scratch at lane root (permitted, non-standard location)**:
  `?? .scratch/` — created 00:03 this round; contains only `V02/` (fixture + tool mirror
  under `scratch-root/`) and `v26/` (`poll.log`, `poll.sh`, `scratch-root/` mirror).
  Scratch is protocol-permitted per seat, but `.scratch/<SEAT>/` at lane root is a new
  untracked top-level dir, not covered by `.gitignore` (`check-ignore` empty; the
  gitignore's scratch convention is `*-self-test-*/`). Not creep — flagged as hygiene.
- **Bucket E — inherited stray (NOT r101)**:
  `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`, mtime
  `2026-10-17 22:32:40` — predates round start (00:02) by ~1.5h. Independently
  corroborated: kotodama r16 `reports/round-16/fixes/link-coverage.md` finding **F-X02-1**
  records the same lore path as "out-of-lane, informational … left for lore's own
  scope/integrator". Left untouched by r101 seats; listed for the integrator.

No sixth bucket exists: every untracked path in the repo falls under C/D/E or is bucket B.

## 2. Report exclusivity — held, with one recorded census surplus

- Census timeline (all counts `ls seats/*.md | wc -l`, verbatim):
  - 00:43:50 (ext2 gate): 28 files = 27 non-self + my stub → **exactly the declared
    complement** (28 declared seats − self(V13) = 27): `U1 U2 V01…V24 V26 V28`, with
    V25/V27 unassigned. At this instant the round matched the declaration perfectly.
  - 00:44 (endgame census run): still 28 files, same IDs.
  - 00:44+: `V25-receipt.md` (mtime Oct 18 00:44) landed → re-census at 00:46:
    **29 files = 28 non-self** (`U1 U2 V01…V26 V28`).
- **Count discrepancy vs declaration, reported exactly**: declaration counts 28 seats
  (2 producers + 26 verifiers). Final observed: 28 non-self reports = 2 producers + 26
  verifier-numbered files *if* one of {V25, V28} is surplus — one more non-self report
  than the declared complement (27). The surplus file is either `V28-late-bookkeeper.md`
  (00:19, named "late", suggesting a post-declaration bookkeeping seat) or
  `V25-receipt.md` (00:44). Under the first census the roster `U1 U2 V01–V24 V26 V28`
  (= 26 verifiers, V25/V27 skipped) fits the declaration exactly, which makes
  **V25-receipt.md the surplus**.
- Numbering is opaque IDs, not ordinals (round-98 had a `V58` seat), so numbering alone
  cannot adjudicate; the count is the evidence. Either way the surplus seat wrote ONLY
  its own report path (plus `V25-scratch/` present since 00:09) — no byte-ownership
  violation. Recorded as a declaration-vs-delivery bookkeeping discrepancy for the
  integrator, not creep.
- All 29 reports (28 seats + self) are flat in `seats/`, one per seat, unique `<SEAT>-`
  prefixes, no duplicates, none nested. The only seat-report-named files found at depth
  are r100
  report copies inside `V04-scratch/baseline-tree/.ufo/waves/round-100/seats/` — a
  baseline mirror in V04's scratch, not misfiled r101 reports (live r101 copies verified
  present at top level).
- Scratch dirs observed: `U1- U2- V03- V04- .v05- V06- V09- .V11- V13- .v14- .v16-
  V17- V20- V21- V23- V25- .v28-scratch/` + lane-root `.scratch/{V02,v26}` — all
  seat-owned, none contains another seat's report.
- Poll-side stability: report count rose monotonically (13→28 across 00:29–00:43), never
  a rewrite/overwrite of an existing report (counts only ever increased).

Limit, stated plainly: the filesystem cannot prove *authorship* — exclusivity here is
verified by location, naming, census, and count consistency, not by who ran which write.

## 3. Parent-tree strays (zero attributable to r101)

- `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1` → **empty** (parent repo
  clean on master `725330c`).
- `find /home/vgpnk/Projects/shokunin -newermt '2026-10-18 00:00'` excluding `.git` and
  `lore-shokunin` → only `kotodama-shokunin/reports/round-16/*` and
  `kotodama-shokunin/.scratch/r16-*` (+ `outside-secret.txt`, a guard fixture whose
  content begins "outside").
- Attribution to the concurrent **kotodama round-16** session, not r101: report header
  "R16-V01 — verifier … O lane, round 16 … run 2026-10-17 23:29–23:59"; all scratch
  `r16-*`-prefixed; coherent kotodama git status (`M tools/harness/packet_links.py`,
  untracked `reports/round-16/*`, `corpus/lessons/round-16.md`); and
  `grep -ril 'round-101|r101|lore-shokunin'` over every post-midnight kotodama file →
  **no matches** (earlier `lore` hits were "folklore" URL substrings and kotodama domain
  vocabulary, plus F-X02-1 itself observing lore's r98 stray without touching it).

## 4. This seat's own footprint (for the record)

Writes: `seats/V13-scope-creep.md` (this file; stub at 00:15, final now) and
`seats/V13-scratch/start.tsv` (round-start timestamp). Nothing else; no commits, no
pushes, no network.

## Per-axis verdicts

- **A capture/bucketing — improved/held**: full porcelain + `-uall` expansion captured
  (the `-uall` listing is ~12.6 MB of text because scratch mirrors tens of thousands of
  fixture files — bucketed by top-level entry, which is why §1 stays readable); every
  path assigned to a bucket; no sixth bucket.
- **B exclusivity — held, one discrepancy recorded**: one-per-seat, flat, unique
  prefixes, no duplicates, no misfiles; but final report count (28 non-self) exceeds the
  declared seat complement (27 expected non-self) by exactly one (`V25-receipt.md` per
  the 00:43:50 census fit) — benign in byte terms, logged for the integrator.
- **C parent tree — held**: zero r101-attributable writes outside `lore-shokunin/`;
  concurrent kotodama r16 activity positively attributed and excluded.
- **D evidence — held**: every claim above quotes the command and observed output.
- **E latency — harmed (self-inflicted, bounded)**: two full 40-try polls burned before
  the two-try completion (28th report arrived 00:42–00:43); ~29 min of the ~34-min seat
  was waiting. Bounded and recorded per endgame convention; no finding was delayed past
  00:47.

**PASS** — scope clean for admission; nothing for the integrator to revert. Carry-forward
notes only: (1) bucket D scratch hygiene (V02/v26 lane-root `.scratch/`), (2) inherited
r98 `V58-scratch` stray predates the round and awaits lore's own cleanup decision, (3) the
declaration-count-vs-delivery discrepancy of §2 (28 non-self reports vs 27 expected;
surplus `V25-receipt.md` under the 00:43:50 roster fit) — a bookkeeping question, not a
byte-ownership violation.
