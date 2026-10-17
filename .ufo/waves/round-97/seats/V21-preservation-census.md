# V21 — preservation census (round 97)

**Seat:** V21 `preservation-census`. Scope per seat spec: after all producers,
enumerate `corpus/fixtures` (expect **171**); diff **every** inherited path
against `f3e09f9`; expected changes ONLY `map_obligations.py`,
`map-obligations-contract.json`, `tools/README.md`, `dependency_freeze.py`,
`dependency-freeze-contract.json`, the r96 `claim-excerpt-map.md` (cosmetic),
plus the new r97 fixture and knowledge note; **any other inherited change is a
finding**.

**Report path (only file this seat writes):** this file. Scratch (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V21-scratch/`):
`census.py`, `census.sh`, `census_pre_receipts.json`, `census_final_receipts.json`,
`baseline_f3e09f9_manifest.txt`, `current_delta.txt`, `changed_paths.txt`,
`snap-a.sha256`, `snap-b.sha256`, `dirs-base.txt`, `dirs-now.txt`,
`files-base.txt`, `files-now.txt`, `archive/` (extracted `f3e09f9` corpus tree).
No commit, no push, no network, no nested agents. All commands run from the lane
repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

**Baseline:** r96 closure `f3e09f9`. `git rev-parse HEAD` →
`2393934237ea076366f3db6dceeff033edb52ab1`; `git diff --stat f3e09f9 HEAD` →
`SCORECARD.md | 31 +` only (the r96 SCORECARD closure commit), so that one extra
inherited row is baseline-attributable, not an r97 write. `LOG.md` carried the
round-97 declaration (`+61` lines, append-only) before any seat ran.

**Host note:** `/tmp` inodes are exhausted on this host (`df -i /tmp` →
`1048576 1048576 0 100%`); an early scratch write to `/tmp` failed with
`No space left on device`, so all scratch is repo-local under the seat dir
(matches the r96 closure host note).

## 1. Poll-wait record (20 s cadence)

Watched `corpus/fixtures` + the six `R*.md` producer reports from 18:44:05.
First sighting times (final mtimes): R2 18:49:31, R4 18:50:14, R5 18:51:25,
R1 18:52:25, R6 18:53:37, R3 18:56:23 — all six present by 18:56:40 (~12.5 min
after first check, well inside the 40-try budget). At the first poll the fixture
dir already existed; the frozen snapshot below is taken after all six reports
and all declared artifacts existed. **Nothing in this seat's scope was ABSENT.**

## 2. Snapshot stability (pre-condition for the verdict)

```sh
{ git diff --name-only f3e09f9; git ls-files --others --exclude-standard \
    | grep -v 'round-97/seats'; } | sort -u > .../changed_paths.txt   # → 19 paths
xargs -a changed_paths.txt sha256sum > snap-a.sha256   # 18:58
sleep 45; xargs -a changed_paths.txt sha256sum > snap-b.sha256
diff -q snap-a.sha256 snap-b.sha256
```

Observed: `SNAPSHOT STABLE (19/19 identical over 45s)`; recomputed changed set
still 19. The snapshot is post-producer-write and stable, so the verdict below
is taken on a quiescent tree.

## 3. Census — 171 dirs, delta exactly +1

```sh
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l      # → 171
find corpus/fixtures -type f | wc -l                              # → 1020
git ls-tree -d --name-only f3e09f9:corpus/fixtures | wc -l        # → 170
git ls-tree -r f3e09f9 --name-only corpus/fixtures | wc -l        # → 1010
diff dirs-base.txt dirs-now.txt                                   # 167a168 > r97-crossing-acknowledgment
diff files-base.txt files-now.txt                                 # +10 files, all in the r97 dir, 0 removed
```

**170 → 171 dirs, 1010 → 1020 files, zero removed directories, zero removed
files.**

Independent `check_bible` census (fresh script `census.py`, repo-relative argv,
same counting convention as the r94–r96 census — violation lines = lines
containing `VIOLATION`):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 .../V21-scratch/census.py final
{"fixture_dirs": 171, "clean_exit0": 37, "negative_exit1": 134,
 "violation_lines": 421, "non_0_1_exits": []}
```

**171 dirs / 37 clean / 134 negative / 421 VIOLATION lines / zero non-0/1
exits**, i.e. **+1 dir, +1 clean**, negative count and violation-line count
unchanged. Receipts for all 171 dirs (exit + stdout sha256) are in
`census_final_receipts.json`; the r97 dir's own entry is
`{"exit": 0, "stdout_sha256": "d9bdf82d…"}` and its direct run prints
`CLEAN: schema, citations, relations, timeline; 0 violations` (rc=0).

**Null control:** the same counter over the 170 inherited dirs only (r97 dir
excluded) reproduces the r96 closure census exactly —
`dirs 170 clean 36 neg 134 VIOLATION-lines 421`. So the counter is calibrated
against a known figure and the new dir contributes 0 violation lines.

## 4. Inherited-path diff vs `f3e09f9` — two independent methods

**Method A (git-native).**

```sh
git diff --name-status f3e09f9
M  LOG.md
M  SCORECARD.md
M  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
M  corpus/tools/README.md
M  corpus/tools/dependency-freeze-contract.json
M  corpus/tools/dependency_freeze.py
M  corpus/tools/map-obligations-contract.json
M  corpus/tools/map_obligations.py

git diff --name-status --diff-filter=DR f3e09f9 | wc -l   # → 0
git ls-files --others --exclude-standard | grep -v 'round-97/seats'
  # → exactly 11 new paths: the 10 r97 fixture files + r97-acknowledgment-scope-note.md
```

**Method B (fresh implementation, archive + `diff -r`).**

```sh
git archive f3e09f9 corpus | tar -x -C .../V21-scratch/archive
diff -rq .../V21-scratch/archive/corpus corpus
Files .../r96-crossing-response/claim-excerpt-map.md and corpus/... differ
Files .../tools/dependency-freeze-contract.json and corpus/... differ
Files .../tools/dependency_freeze.py and corpus/... differ
Files .../tools/map-obligations-contract.json and corpus/... differ
Files .../tools/map_obligations.py and corpus/... differ
Files .../tools/README.md and corpus/... differ
Only in corpus/fixtures: r97-crossing-acknowledgment
Only in corpus/knowledge: r97-acknowledgment-scope-note.md
Only in corpus/tools: __pycache__          # gitignored, see §6
```

Both methods agree: **6 modified inherited files (exactly the declared set), 2
new paths (r97 fixture dir + knowledge note), 0 deletions, 0 renames.** File
arithmetic: archive 1804 files vs worktree 1815 (`find corpus -type f` excluding
`__pycache__`) = +11 = the 10 fixture files + the knowledge note.

**Classification of the two extra inherited rows:** `SCORECARD.md` (+31 lines)
is from the pre-round r96 closure commit `2393934`, i.e. baseline-attributable;
`LOG.md` (+61 lines) is the append-only round-97 declaration written before
dispatch. Neither is a producer write and neither touches corpus bytes — same
treatment as V24's r96 handling of the analogous pair. **No undeclared inherited
change exists: no finding of the r94-F01 stray-write class.**

## 5. Preservation corroborations (cheap, in-scope)

- **r96 map repair is confined to the declared cosmetic edit.** `diff` vs
  `f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` → 4
  changed lines total (1 delimiter row `|---|---|---|---|---|---:|---|---|` →
  `|---|---|---|---|---:|---|---|`, i.e. 8 cells → 7, matching the 7-column header;
  plus 1 prose sentence where "The new relation encodes…" becomes "The new
  tick-12 event encodes…"). All table **data rows, pointers, anchors, spans and
  modes are byte-unchanged** (no other diff hunk).
- **r97 fixture preserves r96 bytes.** `entities.json`, `relations.json`,
  `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` are
  byte-identical (`diff -q`) to the *post-repair* r96 files. `sources.json` and
  `timeline.json` are prefix-preserving extensions: parsed r96 lists are exact
  prefixes of the r97 lists (5 → 6 each), the appended event being
  `acknowledgment-aru-records` (tick 13, actor `aru`, place `chalk-stair`,
  `depends_on: ["response-evin-salt-court"]`). Parsed equality also holds for
  the three unchanged tables. Structural counts: entities 5, relations 1,
  timeline 6, sources 6, contradictions 0 — matching the declared 5/1/6 and
  "sources 5→6".
- **W05 pin integrity.** `.ufo/waves/round-94/work/W05-baseline-corpus.sha256`
  (984 rows = 980 fixture rows + 4 tools rows) re-verified against the worktree:
  **1 mismatch, 0 missing** — `corpus/fixtures/README.md`, whose worktree sha
  `20c639e74c6225fc66e4b97a4c28c57d76684d47f0cc806cd176a725f87d4c35` is
  **identical to its `f3e09f9` bytes** (`git diff --name-only f3e09f9 -- corpus/fixtures/README.md` → 0 rows), so the breakage is the inherited
  r94–r96-documented one, not an r97 change. None of the 6 r97-modified
  inherited files is pinned (`grep -c` per path → 0); the 4 pinned tools rows
  are `boundary-doc-check`/`discriminate_check`/`support_check` class and are
  untouched. **r97 breaks zero W05 pins.**

## 6. Notes (not findings)

- `corpus/tools/__pycache__/` appears in the archive diff as worktree-only; it
  is `gitignore`d (`.gitignore:2:__pycache__/`), pre-existing
  (`boundary_doc_check.cpython-314.pyc`, 14:04), and not part of the delivered
  tree. Ignored class, no action.
- Transient: a `map-obligations-self-test-*/` directory is materialized **in the
  repo root** while `map_obligations.py --self-test` runs
  (`tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`
  — present at baseline `f3e09f9:corpus/tools/map_obligations.py:809`, so not an
  r97 regression). One 18:48 untracked snapshot caught it mid-run with 108 files;
  it was removed by the tool and is **absent** at the frozen snapshot
  (`ls` → `No such file or directory`; final untracked non-seat list = the 11
  declared new paths only). Recorded so no future census reads it as a stray.
- No `git` mutation was performed by this seat (no add/commit/stash); `git
  archive` writes only into the seat scratch.

## Bottom line

**PASS** — census 171 fixture dirs (170→171, +1 `r97-crossing-acknowledgment`,
+10 files, 0 removed; 37 clean / 134 negative / 421 VIOLATION lines, null
control reproduces r96's 170/36/134/421 exactly) and the inherited-path diff vs
`f3e09f9` shows exactly the six declared modified files plus the eleven declared
new paths (10 fixture files + knowledge note), with `LOG.md`/`SCORECARD.md`
pre-round bookkeeping as the only other rows, zero deletions/renames, zero
broken W05 pins, and a 45 s-stable 19/19-hash snapshot.
