# V27 — adjacency (round 99)

**Seat:** V27 (adjacency), round-99 single wave, lane `lore-shokunin`.
**Subject:** the delivered r99 working tree vs baseline r98 closure `4265df5` (lane HEAD `337f0fa` "lore r99: record blocked dispatch attempt — zero increment"; the wave tree is uncommitted).
**Scope of this seat:** `PROVINCE.md` byte-identity, no writes outside `lore-shokunin` (whole-tree write attribution vs the declared producer byte-ownership S1–S5), and a rights/mechanics language scan over every new r99 byte and every round diff. This seat makes **no** C1/C2 verdict, no admission verdict, and no lore-truth ruling.
**Gate:** artifacts AND all five producer reports must exist before any of that battery runs. They did not. The battery was not run. This report is the absence record, not a plan verification.

## Axes

1. Protocol compliance — poll-wait, 20 s cadence, 40 tries, never verify a plan. Exercised. One recorded stall (poller restart gap), not fatal to the absence conclusion.
2. `PROVINCE.md` byte-identity — not judged. Hash was stable through the window; that is an observation, not a delivered-revision verdict.
3. No outside writes / byte-ownership attribution — not judged. An early fleet-root scan was taken while waiting; it is not the post-report freeze.
4. Rights/mechanics scan — not run. Both S5 knowledge files were absent, so the scan set was incomplete.

## Poll-wait record (protocol compliance)

Poller `.ufo/waves/round-99/seats/V27-scratch/poll.sh` then `poll-cont.sh`. Log: `.ufo/waves/round-99/seats/V27-scratch/poll.log`.

```
POLL_START 2026-10-17 22:01:20 -0300
try=1  ts=2026-10-17 22:01:25 -0300 reports=0 sreps=[] fixfiles=10 table=ABSENT note=ABSENT freeze=03d04365cf00 contract=153ebc5b2092 toolsreadme=294dd56f29ce skill=22ffaa822ec7 province=94a7a77e1810
try=2  ts=2026-10-17 22:01:45 -0300 reports=1 sreps=[S3-fixture-author.md ] …
try=9  ts=2026-10-17 22:04:05 -0300 reports=4 sreps=[S3-fixture-author.md S4-fixture-docs.md ] fixfiles=10 table=ABSENT note=ABSENT freeze=1728ed892442 contract=153ebc5b2092 …
try=12 ts=2026-10-17 22:05:05 -0300 reports=5 sreps=[S3-fixture-author.md S4-fixture-docs.md ] fixfiles=10 table=ABSENT note=ABSENT freeze=1728ed892442 contract=8f9c1f531614 toolsreadme=294dd56f29ce skill=22ffaa822ec7 province=94a7a77e1810
POLL_RESTART 2026-10-17 22:07:59 -0300 reason=first-poller-killed-at-try12-to-extend-window
try=13 ts=2026-10-17 22:09:45 -0300 reports=7 sreps=[S3-fixture-author.md S4-fixture-docs.md ] fixfiles=10 table=ABSENT note=ABSENT freeze=6f81f8be1974 contract=8c2561b043c2 toolsreadme=294dd56f29ce skill=22ffaa822ec7 province=94a7a77e1810
try=40 ts=2026-10-17 22:18:45 -0300 reports=14 sreps=[S3-fixture-author.md S4-fixture-docs.md ] fixfiles=10 table=ABSENT note=ABSENT freeze=6f81f8be1974 contract=8c2561b043c2 toolsreadme=294dd56f29ce skill=22ffaa822ec7 province=94a7a77e1810
POLL_END 2026-10-17 22:19:05 -0300 tries=40
```

`reports=N` counts seat markdown matching `^(S[1-5]|V[0-9]+)-` and is not an all-reports poll. Producer count is `sreps`. Endgame convention: SELF (V27) was excluded by construction; no all-reports poll was taken. No stall-escape was used to declare readiness.

**Recorded stall, not fatal:** the first poller was started under a 300 s tool cap and was killed after try 12 (22:05:05) so the window could finish. Continuation started at 22:07:59; try 13 landed at 22:09:45. Unsampled gap ≈ 4 m 40 s. Tries still total 40. S1/S2/S5 reports and both knowledge files were absent on every sampled try, including both sides of the gap.

Post-window confirmation (same absence), lane root:

```
WRITE_CHECK 2026-10-17 22:36:02 -0300
ls -1 .ufo/waves/round-99/seats/S*.md
.ufo/waves/round-99/seats/S3-fixture-author.md
.ufo/waves/round-99/seats/S4-fixture-docs.md
ls corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
```

No `S1-*.md`, no `S2-*.md`, no `S5-*.md` under `.ufo/waves/round-99/seats/` (maxdepth 1). `S2-scratch/` is empty (mtime 22:00:49). `S5-scratch/` does not exist. `S1-scratch/before/mirror/` exists (mtime 22:08:46) and holds a tool/fixture mirror only — not a report.

## Gate result

| Required before the battery | At try 40 (22:18:45) | At write-check (22:36:02) |
|---|---|---|
| S1 report | ABSENT | ABSENT |
| S2 report | ABSENT | ABSENT |
| S3 report `S3-fixture-author.md` | present (22:01:40, 5069 B) | present |
| S4 report `S4-fixture-docs.md` | present (22:03:54, 9303 B) | present |
| S5 report | ABSENT | ABSENT |
| `corpus/fixtures/r99-window-lapse/` (10 files) | present | present |
| `corpus/knowledge/r99-gate-blind-spot-table.md` | ABSENT | ABSENT |
| `corpus/knowledge/r99-lapse-scope-note.md` | ABSENT | ABSENT |

S1's owned bytes moved during the window and then stopped (`dependency_freeze.py` `03d04365` → `65c1ae30` → `1728ed89` → `6f81f8be1974` by try 13; contract `153ebc5b` → `73b28933` → `8f9c1f53` → `8c2561b043c2` by try 13) and stayed at those hashes through try 40 and the 22:36 check. That is a mid-flight or unreported landing, not a producer report. Not verified.

S2's owned files did not move. `corpus/tools/README.md` `294dd56f29ce…` and `SKILL.md` `22ffaa822ec7…` are the same hashes as the 22:01:20 baseline snap, and `git diff --stat 4265df5 -- corpus/tools/README.md SKILL.md` is empty. No S2 artifact, no S2 report.

S5 produced neither knowledge file.

## Not run (never verify a plan)

- No post-report freeze manifest.
- No whole-tree blob audit offered as an adjacency verdict.
- `rights_scan.sh` was written to scratch and not executed. The scan set includes the two absent knowledge files.
- No attribution of the r99 fixture or the tool diff to a delivered revision. S3/S4 reports exist, but the declared ownership set is incomplete without S1/S2/S5, and those bytes were still moving while S3/S4 reported.

## Observations recorded, not verdicts

These measurements were taken. They do not clear the gate and are not an adjacency PASS/FAIL.

`PROVINCE.md` hash did not change across all 40 tries (`94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa`). At 22:36:02:

```
sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
git diff 4265df5 -- PROVINCE.md | wc -c
0
```

Blob at the 22:01:20 snap matched `git rev-parse 4265df5:PROVINCE.md` (`7c599c395e1710b6a7c7aca6d485c373bed6deb7`). SHONEN/SKILL/README/l0-questions were not re-audited after the gate failed.

Worktree vs `4265df5` on producer-owned paths, 22:36:02 (observation only):

```
git diff --stat 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  65 ++++++++++-
 2 files changed, 206 insertions(+), 22 deletions(-)
git status --porcelain -- corpus PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md LOG.md SCORECARD.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/fixtures/r99-window-lapse/
git rev-parse --short HEAD
337f0fa
git diff --stat HEAD -- LOG.md SCORECARD.md PROVINCE.md
(empty)
```

Committed delta `4265df5..HEAD` (pre-wave, already in git, measured 22:02) is `LOG.md` +91/−0 and `SCORECARD.md` +32/−0. Worktree `LOG.md` / `SCORECARD.md` / `PROVINCE.md` match HEAD. Not a wave write.

Early fleet-root scan while waiting (`outside_scan.sh` → `outside-early.txt`, since `2026-10-17 21:50`, run ~22:02). Not a post-report outside-write verdict:

```
== lore/r99-named files outside lane ==
(none)
== parent repo git status ==
(empty)
== parent .ufo/waves/round-99 presence ==
ls: cannot access '/home/vgpnk/Projects/shokunin/.ufo/waves/round-99': No such file or directory
```

The same scan listed concurrent `kotodama-shokunin` round-15 files (`reports/round-15/**`, `.scratch/**`). No lore/r99-named path outside the lane. Sibling `PROVINCE.md` mtimes are all pre-wave (latest `kotodama-shokunin` 2026-10-17 12:59; `lore-shokunin` 2026-10-15 01:49). `/tmp` in-window names included seat scratch (`/tmp/v102-poll.log`, `/tmp/v17-poll.log`, `/tmp/v55-base-*`, `/tmp/v83-*`, `/tmp/xai-tok-*`). This seat wrote none of those. This seat's only writes are this report and `.ufo/waves/round-99/seats/V27-scratch/`.

## Bottom line

**ABSENT** — after 40 poll tries (22:01:20–22:19:05, one recorded restart gap 22:05:05–22:09:45) and a 22:36:02 recheck, S1/S2/S5 reports and both knowledge artifacts (`r99-gate-blind-spot-table.md`, `r99-lapse-scope-note.md`) were still missing, so the adjacency battery (PROVINCE verdict, outside-write attribution, rights/mechanics scan) was not run.
