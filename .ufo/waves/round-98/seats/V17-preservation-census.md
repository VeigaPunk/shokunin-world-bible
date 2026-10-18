# V17 — preservation census (round 98)

**Seat:** V17 `preservation-census`. Scope per seat spec: after all producers,
enumerate `corpus/fixtures` (expect **172**); diff **every** inherited path
against `9a3d648`; expected changes ONLY `corpus/tools/dependency_freeze.py`,
`corpus/tools/dependency-freeze-contract.json`, `corpus/tools/README.md`, the
r95 `claim-excerpt-map.md` (one sentence), plus the new r98 fixture + r98
knowledge note + the two r95/r96 note addenda; **any other inherited change is a
finding**.

**Report path (only file this seat writes):** this file. Scratch (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V17-scratch/`):
`census.py`, `census_pre_receipts.json`, `census_final_receipts.json`,
`compare.sh`, `poll.sh`, `pincheck.py`, `dirs-base.txt`, `dirs-now.txt`,
`files-base.txt`, `files-now.txt`, `changed_paths.txt`, `snap-a.sha256`,
`snap-b.sha256`, `archive/` (extracted `9a3d648` corpus tree). No commit, no
push, no network, no nested agents. All commands ran from the lane repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

**Baseline:** r97 closure `9a3d648`. `git rev-parse HEAD` →
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`; `git diff --stat 9a3d648 HEAD` →
`SCORECARD.md | 33 +++` only (the r97 closure commit), so that one extra
inherited row is baseline-attributable, not an r98 write. `LOG.md` carried the
round-98 declaration (`+61` lines, append-only) before any seat ran.

## 1. Poll-wait record (20 s cadence, 40 tries max; never verify a plan)

Watched the r98 fixture dir, the r98 knowledge note, the r95/r96 note addenda and
the `S*.md` producer reports from 20:28:05 (-03:00; poll process start confirmed
with `ps -o lstart=` → `Sat Oct 17 20:28:05 2026`). First sightings:

| t | time | observation |
|---|---|---|
| 1 | 20:28:05 | fixture 0 files, no note, no reports |
| 2 | 20:28:25 | fixture 10 files (S3's byte copies landed; mtimes 20:28:24) |
| — | 20:31:25 | `S3-fixture-author.md` |
| — | 20:32:06 | `S4-fixture-docs.md` |
| — | 20:34:00 | `S5-knowledge-notes.md` (note + both addenda already on disk) |
| — | 20:34:53 | `S2-tools-docs.md` |
| — | 20:35:33 | `S1-freeze-hygiene.md` |

All five producer reports present by 20:35:33, **7 min 28 s** after the first
check — well inside the 40-try budget. **No stall escape was required and no
all-reports poll was needed by this seat** (the endgame subtraction convention
never had to be exercised: the seat's own wait ended on artifact presence, not
on an all-reports condition). Nothing in this seat's scope was ABSENT.

## 2. Snapshot stability (pre-condition for the verdict)

```sh
{ git diff --name-only 9a3d648; git ls-files --others --exclude-standard \
    | grep -v '^\.ufo/'; } | sort -u > .../changed_paths.txt   # → 19 paths
xargs -a changed_paths.txt sha256sum > snap-a.sha256   # 23:35:06Z
sleep 45; xargs -a changed_paths.txt sha256sum > snap-b.sha256   # 23:36:03Z
diff -q snap-a.sha256 snap-b.sha256
```

Observed: `SNAPSHOT STABLE (19/19 identical over 45s)`. The 19 paths are the 17
corpus rows of §4 plus `LOG.md` and `SCORECARD.md`; the changed set recomputed at
the end of the run is still exactly those 19. A third pass after this report was
written (23:37:56Z) re-diffs the changed set and re-hashes all 19 paths:
`CHANGED SET STILL 19 (identical)` and `HASHES UNCHANGED SINCE SNAPSHOT B`. The
verdict below is taken on a quiescent post-producer tree.

## 3. Census — 172 dirs, delta exactly +1

```sh
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l      # → 172
find corpus/fixtures -type f | wc -l                              # → 1030
git ls-tree -d --name-only 9a3d648:corpus/fixtures | wc -l        # → 171
git ls-tree -r --name-only 9a3d648 corpus/fixtures | wc -l        # → 1020
diff dirs-base.txt dirs-now.txt    # 168a169 > r98-clerk-filing
diff files-base.txt files-now.txt  # 1004a1005,1014 > the 10 r98 files
```

**171 → 172 dirs, 1020 → 1030 files, zero removed directories, zero removed
files.** `diff` output: one added dir line, ten added file lines, no `<` lines.

Independent `check_bible` census (fresh script `census.py`, repo-relative argv,
same counting convention as the r94–r97 census — violation lines = lines
containing `VIOLATION`):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 .../V17-scratch/census.py final
{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134,
 "violation_lines": 421, "non_0_1_exits": []}
```

**172 dirs / 38 clean / 134 negative / 421 VIOLATION lines / zero non-0/1
exits**, i.e. **+1 dir, +1 clean**, negative count and violation-line count
unchanged. The r98 dir's own receipt is `{"exit": 0, "stdout_sha256":
"d9bdf82d2b0cddb2a60734ad10dc69beb75e085f5fb4b13a007c6ec43ac8606b"}`; a direct
re-run in this pass prints `CLEAN: schema, citations, relations, timeline; 0
violations` (exit 0) and its stripped stdout hashes to the same `d9bdf82d…`.

**Null control:** the same counter restricted to the 171 inherited dirs
reproduces the r97 closure census exactly — `dirs 171 clean 37 neg 134
VIOLATION-lines 421`, zero non-0/1 exits. So the counter is calibrated against a
known figure and the new dir contributes 0 violation lines. **Stability control:**
a pre-run taken while the fixture was mid-write and the final run produce
byte-identical receipts for all 172 dirs (`identical receipts: 172, differing:
0`), so no directory's checker output moved between the two runs.

## 4. Inherited-path diff vs `9a3d648` — two independent methods

**Method A (git-native).**

```sh
git diff --name-status 9a3d648
M  LOG.md
M  SCORECARD.md
M  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
M  corpus/knowledge/r95-aftermath-scope-note.md
M  corpus/knowledge/r96-response-scope-note.md
M  corpus/tools/README.md
M  corpus/tools/dependency-freeze-contract.json
M  corpus/tools/dependency_freeze.py

git diff --name-status --diff-filter=DR 9a3d648 | wc -l   # → 0
git ls-files --others --exclude-standard | grep -v '^\.ufo/'
  # → exactly 11 new paths: the 10 r98 fixture files + r98-clerk-scope-note.md
```

**Method B (fresh implementation, archive + `diff -rq`).**

```sh
git archive 9a3d648 corpus | tar -x -C .../V17-scratch/ --one-top-level=archive
diff -rq .../V17-scratch/archive/corpus corpus | grep -v '__pycache__'
Files .../archive/corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md and corpus/... differ
Only in corpus/fixtures: r98-clerk-filing
Files .../archive/corpus/knowledge/r95-aftermath-scope-note.md and corpus/... differ
Files .../archive/corpus/knowledge/r96-response-scope-note.md and corpus/... differ
Only in corpus/knowledge: r98-clerk-scope-note.md
Files .../archive/corpus/tools/dependency-freeze-contract.json and corpus/... differ
Files .../archive/corpus/tools/dependency_freeze.py and corpus/... differ
Files .../archive/corpus/tools/README.md and corpus/... differ
```

Both methods agree: **6 modified inherited files (exactly the declared set), 2
new paths (r98 fixture dir + knowledge note), 0 deletions, 0 renames.** File
arithmetic: archive 1815 files vs worktree 1826 (`find corpus -type f` excluding
`__pycache__`) = +11 = the 10 fixture files + the knowledge note.

Line arithmetic (`git diff --numstat 9a3d648 -- corpus/ LOG.md SCORECARD.md`):

```
61  0  LOG.md
33  0  SCORECARD.md
1   1  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
14  0  corpus/knowledge/r95-aftermath-scope-note.md
14  0  corpus/knowledge/r96-response-scope-note.md
56  0  corpus/tools/README.md
190 3  corpus/tools/dependency-freeze-contract.json
35  7  corpus/tools/dependency_freeze.py
```

The r95 map row is **1 added + 1 removed line** (single-sentence repair, §6);
both note addenda are pure appends (14/0 each); the three tools files carry
281 insertions / 10 deletions total. Tool hashes at the frozen snapshot:
`dependency_freeze.py` `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`,
`dependency-freeze-contract.json`
`153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`,
`README.md` `1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84`.

**Classification of the two extra inherited rows:** `SCORECARD.md` (+33 lines)
is from the pre-round r97 closure commit `dd4df1b`, i.e. baseline-attributable;
`LOG.md` (+61 lines) is the append-only round-98 declaration written before
dispatch. Neither is a producer write and neither touches corpus bytes. **No
undeclared inherited change exists: no finding of the r94-F01 stray-write class
inside the lane.** Every one of the 170 other inherited fixture directories is
byte-identical to `9a3d648` (`diff -rq` reports no other fixture path).

## 5. Declared-set conformance

| Declared change (C1/C2/C3) | Observed | Verdict |
|---|---|---|
| `corpus/tools/dependency_freeze.py` | modified, 35+/7− | present, exactly |
| `corpus/tools/dependency-freeze-contract.json` | modified, 190+/3− | present, exactly |
| `corpus/tools/README.md` | modified, 56+/0− | present, exactly |
| r95 map, one-sentence repair only | 1+/1−, line 49 only | present, exactly |
| new r98 fixture (10 files) | new dir, 10 new files | present, exactly |
| new r98 knowledge note | new file `r98-clerk-scope-note.md` | present, exactly |
| dated addenda in r95/r96 scope notes | 14+/0− each, append-only | present, exactly |

No undeclared path exists in either direction: no declared artifact is missing,
and no changed path is undeclared. (The r98 note and the two addenda carry the
declared C3/C1-correction content; their prose correctness is the doc-parity and
claim seats' scope, not this census's.)

## 6. Preservation corroborations (cheap, in-scope)

- **r95 map repair is confined to one prose sentence.** `diff` vs
  `9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` → exactly
  one hunk, one line replaced (53 lines before, 53 after; 2 diff lines total:
  one `<`, one `>`), in the "Timeline normalization and scope" prose paragraph.
  No table row, pointer, anchor, span, or mode line is touched. (Receipt
  re-derivation for that fixture belongs to the r95-repair seats.)
- **r98 fixture preserves r97 bytes for the four untouched tables.**
  `contradictions.json`, `inspiration-note.md`, `relations.json`,
  `source-excerpt.md` are sha256-identical to
  `9a3d648:corpus/fixtures/r97-crossing-acknowledgment/…` (all four verified
  with `git show … | sha256sum` vs worktree).
- **r98 JSON tables are prefix-preserving extensions.** Parsed: entities 5→6,
  sources 6→7, timeline 6→7, relations 1→1, contradictions 0→0; in every case
  `r98[:len(r97)] == r97` is `True`. The appended rows are the declared
  `clerk-maren` (entity), `clerk-filing-note` (source), and `clerk-filing-open`
  (event, tick 14, actor `clerk-maren`, place `chalk-stair`,
  `depends_on: ["acknowledgment-aru-records"]`, source `clerk-filing-note`).
  Structural counts 6/1/7/7 match the C3 declaration; the r98 dir is `CLEAN` with
  0 violations.
- **W05 pin integrity.** `.ufo/waves/round-94/work/W05-baseline-corpus.sha256`
  (984 rows = 980 fixture rows + 4 tools rows) re-verified against the worktree:
  **983 ok, 1 mismatch, 0 missing** — `corpus/fixtures/README.md`, whose worktree
  sha `00e0074862b48eaa3ffcf50157ba5c70f030c1e775e299ebe23e29cf26b508b6` is
  **identical to its `9a3d648` bytes** (`git show 9a3d648:corpus/fixtures/README.md
  | sha256sum` → same), so the breakage is the inherited r94-era one, not an r98
  change. None of the 17 r98-changed corpus paths is pinned (`grep -c` per path →
  0; the pin has 0 `corpus/knowledge` rows and 0 `r98` rows; its 4 pinned tools
  rows are `boundary-doc-check`/`discriminate_check`/`support_check` class and are
  untouched). **r98 breaks zero W05 pins.**

## 7. Notes (not findings)

- **Out-of-lane observation (parent tree).** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt`
  (105 bytes, content: `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory`),
  untracked, mtime 2026-10-17 20:30:10 — i.e. **written during the r98 round, in
  the parent tree, outside the lane**. It is the r94-F01 stray-write class at the
  parent level and is not a lane corpus change (this seat's scope). Recorded for
  the adjacency/closure seats; no other parent-root file changed during the round
  (`MANIFEST.json` mtime 20:25:00 is pre-dispatch and `git status` in the parent
  shows only this one untracked file).
- `corpus/tools/__pycache__/` (now including `dependency_freeze.cpython-314.pyc`,
  mtime 20:31) is `gitignore`d (`.gitignore:2:__pycache__/`), pre-existing class,
  and not part of the delivered tree.
- **No nested git repo/gitlink in the wave tree** — `find .ufo/waves/round-98
  -name .git -type d` → empty, so the r97 V37 mirror-freeze gitlink class did not
  recur. Seat scratch is large but inert (`du -sh .ufo/waves/round-98` → 285M;
  `seats/V37-scratch/archive` 242M is an extracted `git archive`, not a clone).
  All seat scratch/report paths live under `.ufo/waves/round-98/` and are
  excluded from the delivered-tree accounting by construction.
- Transient `*-self-test-*/` directories materialized in the repo root while the
  corpus tools' self-tests run are `gitignore`d (`.gitignore` last line) and were
  absent at the frozen snapshot.
- No `git` mutation was performed by this seat (no add/commit/stash); `git
  archive` wrote only into the seat scratch.

## Bottom line

**PASS** — census **172 fixture dirs** (171→172, +1 `r98-clerk-filing`, +10 files,
0 removed; 38 clean / 134 negative / 421 VIOLATION lines, null control reproduces
r97's 171/37/134/421 exactly, receipts stable across both runs) and the
inherited-path diff vs `9a3d648` shows exactly the seven declared changes
(3 tools files, r95 map one-sentence repair, r98 fixture, r98 note, two note
addenda) with `LOG.md`/`SCORECARD.md` pre-round bookkeeping as the only other
rows, zero deletions/renames, zero broken W05 pins, a 45 s-stable 19/19-hash
snapshot — one out-of-lane parent-tree stray (`baseline-analyze.txt`) recorded as
a note for the adjacency seats, not a lane finding.
