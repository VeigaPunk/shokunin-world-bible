# V20 — preservation census (round 99)

**Seat:** V20 `preservation-census`. Scope: after all producers, enumerate `corpus/fixtures` (expect **173**); diff every inherited path against `4265df5`; expected wave changes ONLY `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/README.md`, `SKILL.md`, plus the new `r99-window-lapse` fixture and the two knowledge notes (`r99-gate-blind-spot-table.md`, `r99-lapse-scope-note.md`); any other inherited change is a finding.

**Axes named:** protocol fidelity (poll budget, never verify a plan); census completeness (173, only after producers); preservation fidelity (inherited-path diff vs `4265df5`); evidence quality (quoted commands).

**Report path (exclusive):** this file. Scratch (absolute `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V20-scratch/`): `poll.sh`, `poll-cont.sh`, `poll.log`, `census.py`, `census_inherited.py`, `census_inherited_receipts.json`, `compare.sh` (written, not used for a verdict), `archive/` (`git archive 4265df5` of `corpus` + `SKILL.md`). No commit, no push, no network, no nested agents. Commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` unless noted.

**Not done:** the preservation census itself. Producers were not all present at try 40. Per the poll-wait rule this seat does not verify a plan and does not issue a PASS/FAIL on inherited-path preservation.

## 1. Poll-wait record (20 s cadence, 40 tries; ABSENT, never verify a plan)

Watched `corpus/fixtures/r99-window-lapse/` (file count), both knowledge notes, and top-level `S{1..5}-*.md` reports. Ready required fixture files ≥ 10 AND both notes AND all five reports. This seat did not run an all-reports poll, so the subtract-SELF convention was not exercised.

Pre-script sighting (manual, before `poll.sh`):

```
date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-18T01:00:59Z
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
173
```

`r99-window-lapse/` already had files; both knowledge notes missing; no `S*.md` yet. Local stamp of scripted poll start: `2026-10-17T22:01:25-0300` (`V20-scratch/poll-start.txt`). First scripted line:

```
t=1 ts=2026-10-17T22:02:04-0300 dirs=173 fixture_files=10 notes=0,0 reports: S1:0 S2:0 S3:1 S4:0 S5:0
```

S4 report first seen at try 7:

```
t=7 ts=2026-10-17T22:04:04-0300 dirs=173 fixture_files=10 notes=0,0 reports: S1:0 S2:0 S3:1 S4:1 S5:0
```

**Bounded stall-escape (recorded, not fatal).** The first poller (`poll.sh`, pid 1680797) was killed by the host 600 s background cap after try 30 (`t=30 ts=2026-10-17T22:11:45-0300`, same absence pattern). Restarted as `poll-cont.sh` without truncating `poll.log`, continuing tries 31–40 only (not a new 40-try budget):

```
STALL-ESCAPE host-timeout-600s restart ts=2026-10-17T22:25:51-0300 continuing t=31..40
t=31 ts=2026-10-17T22:25:51-0300 dirs=173 fixture_files=10 notes=0,0 reports: S1:0 S2:0 S3:1 S4:1 S5:0
```

The wall-clock gap 22:11:45 → 22:25:51 is that kill plus restart latency. Try count stayed 40.

Exhaustion (exit 2):

```
t=40 ts=2026-10-17T22:28:51-0300 dirs=173 fixture_files=10 notes=0,0 reports: S1:0 S2:0 S3:1 S4:1 S5:0
EXHAUSTED ts=2026-10-17T22:28:51-0300
```

`grep -c '^t=' poll.log` → `40`. Every try: `dirs=173`, `fixture_files=10`, `notes=0,0`, `S1:0 S2:0 S5:0`. S3 present from try 1; S4 from try 7. S1, S2, S5 reports never appeared. Both knowledge notes never appeared.

## 2. Terminal absence snapshot (2026-10-17T22:30:42-0300)

Quoted from one command block at the lane root. This is evidence of absence, not a preservation verdict.

```
ls -la .ufo/waves/round-99/seats/S*.md
-rw-r--r-- 1 vgpnk vgpnk 5069 Oct 17 22:01 .ufo/waves/round-99/seats/S3-fixture-author.md
-rw-r--r-- 1 vgpnk vgpnk 9303 Oct 17 22:03 .ufo/waves/round-99/seats/S4-fixture-docs.md

ls -la corpus/knowledge/r99*
ls: cannot access 'corpus/knowledge/r99*': No such file or directory

find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
173

find corpus/fixtures/r99-window-lapse -maxdepth 1 -type f -printf '%f\n' | sort
claim-excerpt-map.md
contradictions.json
entities.json
fictional-excerpts.md
inspiration-note.md
README.md
relations.json
source-excerpt.md
sources.json
timeline.json

git status --porcelain=v1 | grep -v '.ufo/'
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/fixtures/r99-window-lapse/

git diff --name-status HEAD
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py

git diff --name-status 4265df5
M	LOG.md
M	SCORECARD.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py

git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
```

`cmp` of working-tree `SKILL.md` and `corpus/tools/README.md` against the `4265df5` archive printed `SKILL_IDENTICAL` and `TOOLS_README_IDENTICAL`. Those two declared S2 paths were not edited inside the budget.

`find .ufo/waves/round-99/seats -maxdepth 2 \( -iname 'S1*' -o -iname 'S2*' -o -iname 'S5*' \)` at 22:30:42 returned only `S1-scratch` and `S2-scratch` directories. No `S5*` path yet. `S2-scratch` was empty (mtime 22:00:49). `S1-scratch/before/mirror/` existed (mtime 22:08:46) and is scratch, not a corpus write.

## 3. What had landed, and what had not (not a verdict)

Present inside the budget: `corpus/fixtures/r99-window-lapse/` (10 files, dir count 173 on every try), `S3-fixture-author.md`, `S4-fixture-docs.md`, and in-progress edits to `dependency_freeze.py` (mtime `2026-10-17 22:07:33 -0300`) and `dependency-freeze-contract.json` (mtime `2026-10-17 22:08:46 -0300`). No `S1-*.md`.

Absent at try 40 and at the 22:30:42 snapshot: `S1` report, `S2` report, `S5` report, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and any edit to `corpus/tools/README.md` or `SKILL.md`.

Pre-wave commits vs `4265df5` (recorded so a later census does not treat them as wave writes). `git diff --stat 4265df5 HEAD` is only:

```
 LOG.md       | 91 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 SCORECARD.md | 32 +++++++++++++++++++++
 2 files changed, 123 insertions(+)
```

`111b9a3` (`lore r98: close round — SCORECARD admitted section`) touches `SCORECARD.md` only. `337f0fa` (`lore r99: record blocked dispatch attempt … — zero increment`) touches `LOG.md` only. `git diff --stat 4265df5 HEAD -- corpus SKILL.md` was empty (corpus and `SKILL.md` identical between those commits). Not classified here as a wave finding, because the wave census was not taken.

## 4. Mid-wait calibration only (not the seat census)

While waiting, and before producers were complete, a null-control counter over fixture dirs excluding `r99-window-lapse` reproduced the r98 closure figure. This does not satisfy "after all producers" and is not the 173 census.

```
PYTHONDONTWRITEBYTECODE=1 python3 .ufo/waves/round-99/seats/V20-scratch/census_inherited.py
{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}
```

Wall time 4.288 s. Receipts: `V20-scratch/census_inherited_receipts.json`. The full `census.py` (all dirs, including r99) was not run. `compare.sh` was not run. No inherited-path finding is issued.

## 5. Post-budget sighting (does not reopen the poll)

At `2026-10-17T22:37:58-0300`, after exhaustion, `S5-scratch` existed and was active (`replay.py` mtime 22:32:40, `replay-log.txt` and `work/` mtimes 22:37:38). Still no `S5-*.md` and still:

```
ls: cannot access '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r99*': No such file or directory
```

`S3-fixture-author.md` and `S4-fixture-docs.md` remained the only producer reports. That activity is noted so a later reader does not think S5 never started. It is outside the 40-try budget and was not used to verify the tree.

ABSENT: S1/S2/S5 reports and both r99 knowledge notes missing after 40 poll tries; preservation census not taken.
