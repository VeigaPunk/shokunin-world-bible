# V37 — census-replica-2 (round 98)

**Seat:** V37 `census-replica-2`. Scope per seat spec: independent second census
against the git archive of `9a3d648` (expect 172 dirs), cross-check V17.

**Baseline:** r97 closure `9a3d648`. `git rev-parse HEAD` →
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (r97 closure SCORECARD commit; the
only delta `9a3d648..HEAD` is `SCORECARD.md`, baseline-attributable).

**Only files this seat writes:** this report plus scratch
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V37-scratch/`
(`census_v37.py`, `receipts-9a3d648.json`, `receipts-tree-r98-prelim.json`,
`receipts-tree-r98-final1/2/3.json`, `archive/` = extracted `git archive 9a3d648`,
`ls-tree.sorted`, `hash-object.sorted`, `integrity.diff`). No commits, no pushes,
no network, no nested agents. One transient `/tmp/v37-ls-tree.txt` was created by
a buggy first integrity attempt and deleted in the same command (`ls` confirms
gone); disclosed for hygiene.

## 1. Method (independent implementation)

Own script `census_v37.py` (not a copy of any other seat's): for each directory
directly under `corpus/fixtures/` (excluding dot-dirs; there are 0), runs
`python3 corpus/fixtures/check_bible.py corpus/fixtures/<d>` with cwd = root and
repo-relative argv (r92 convention), `PYTHONDONTWRITEBYTECODE=1`; records exit
code + sha256 of combined stdout+stderr; counts clean(0) / negative(1) /
non-0-1; counts violation lines under two conventions (`line.startswith("- ")`
and `"VIOLATION" in line`).

Both roots were run with the same checker revision: tree `check_bible.py`
sha256 = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
= `git show 9a3d648:corpus/fixtures/check_bible.py | sha256sum` (identical).

Archive extraction and fidelity:

```sh
$ git archive 9a3d648 | tar -x -C .ufo/waves/round-98/seats/V37-scratch/archive
$ ls -d .../V37-scratch/archive/corpus/fixtures/*/ | wc -l   # 171
# integrity: every archive file must equal its git blob
$ git ls-tree -r 9a3d648 -- corpus/fixtures | awk '{print $3" "$4}' | sort -k2 > ls-tree.sorted   # 1020 rows
$ (cd archive && find corpus/fixtures -type f | sort | while read f; do printf '%s %s\n' \
     "$(git hash-object "$f")" "$f"; done | sort -k2 > ../hash-object.sorted)               # 1020 rows
$ diff ls-tree.sorted hash-object.sorted   # exit 0 — ARCHIVE_INTEGRITY_OK, 1020/1020 files match
```

## 2. Poll record (20 s cadence; artifacts + producer reports)

- 23:28:39Z first check: `corpus/fixtures/r98-clerk-filing/` present with all 10
  files (S3's byte copies, mtimes 23:28:24–23:28:55Z) — but `claim-excerpt-map.md`
  and `README.md` were still r97 placeholders at that instant (S4's rewrites
  carry mtimes 23:30:21Z / 23:30:41Z). Existence-only polling is satisfiable by
  placeholders; my census does not depend on either file (check_bible reads the
  JSON tables), and both were rewritten before my load-bearing runs.
- Producer reports first sighted: S3 23:31:02Z, S4 23:32:22Z, S5 23:33:42Z;
  S1/S2 present by 23:37:38Z (V17's poll record: all five by 20:35:33 local).
- V17 (`V17-preservation-census.md`) first sighted at 23:37:38Z (my second
  loop, try 10) — well inside the 40-try budget. No stall escape needed; no
  all-reports poll was used (two single-seat waits, SELF subtraction never
  exercised). Nothing in scope was ABSENT.

## 3. Census results

**Archive `9a3d648`** (root = extracted archive):

```json
{"root": ".../V37-scratch/archive", "fixture_dirs": 171, "clean_exit0": 37,
 "negative_exit1": 134, "violation_lines_dash": 0, "violation_lines_word": 421, "non01": []}
```

Reproduces the r97 closure census 171/37/134/421 with zero non-0-1 exits.

**Delivered tree** (three runs: final1 23:34Z, final2 23:38Z, final3 23:39Z, all
after the five producer reports landed; identical receipts in all three —
`final1==final2: True`, `final2==final3: True`):

```json
{"root": "/home/vgpnk/Projects/shokunin/lore-shokunin", "fixture_dirs": 172,
 "clean_exit0": 38, "negative_exit1": 134, "violation_lines_dash": 0,
 "violation_lines_word": 421, "non01": []}
```

**172 dirs / 38 clean / 134 negative / 421 violation lines / zero non-0-1
exits** — the declared 171→172 with +1 clean, negative count and violation
lines unchanged.

**Delta vs archive** (per-dir receipt = exit + output sha256):

```
new dirs: ['corpus/fixtures/r98-clerk-filing']
removed dirs: []
inherited count: 171 | changed tuples: 0
r98-clerk-filing receipt: {"dash_lines": 0, "exit": 0,
  "sha256": "afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e",
  "violation_word_lines": 0}
```

Exactly one new dir, zero removals, and all 171 inherited directories
byte-identical in (exit, output-hash). The new dir exits 0 with output
`CLEAN: schema, citations, relations, timeline; 0 violations` (stderr empty).

Convention note: only the `"VIOLATION"`-substring convention yields the declared
421; the `"- "`-prefix convention yields 0 on every dir. The r94–r97 "violation
lines" figure is therefore the VIOLATION-substring count, and my replica uses it.

**Copy fidelity of the new dir** (vs `9a3d648:corpus/fixtures/r97-crossing-acknowledgment/<f>`,
sha256 of blob vs worktree file):

```
contradictions.json  SAME    inspiration-note.md  SAME
relations.json       SAME    source-excerpt.md    SAME
README.md            DIFFERS claim-excerpt-map.md DIFFERS
entities.json        DIFFERS sources.json         DIFFERS
timeline.json        DIFFERS fictional-excerpts.md DIFFERS
```

The four untouched tables are byte-identical to r97; the six declared
rewrites/extensions differ. My hashes match the producers' declared hashes
exactly: S3 — entities `db2d8e5d3866009b…`, sources `32ee15b1f3d72d94…`,
timeline `eb24e0848e597efa…`, fictional-excerpts `29e384bf2eb2ab80…`; S4 — map
`c1099d0ee9eece24…`, README `32efc78f70e6de4f…`. `entities.json`/`timeline.json`
re-hashed at final3 are unchanged from 23:34Z (no late writes).

## 4. Cross-check V17 (census-replica-1)

| figure | V37 (this seat) | V17 |
|---|---|---|
| fixture dirs | 172 | 172 |
| clean exit 0 | 38 | 38 |
| negative exit 1 | 134 | 134 |
| violation lines | 421 | 421 |
| non-0/1 exits | none | none |
| null control (inherited 171) | 171/37/134/421 (archive census) | 171/37/134/421 |
| r98 dir receipt | stripped stdout sha256 `d9bdf82d…` (recomputed) | `d9bdf82d…` |

The r98 dir receipt reconciles across hash conventions: my combined-stream
sha256 is `afe570fcebf45fe3…`; V17's stripped-stdout receipt `d9bdf82d2b0cddb2…`
is reproduced bit-exactly by my run of the same command
(`sha256("CLEAN: schema, citations, relations, timeline; 0 violations")` =
`d9bdf82d…`). Agreement is exact on every number; no divergence found.

## 5. Bounds

- `check_bible` is structural/lexical; the census counts directories and checker
  output, not semantic quality. `CLEAN` means the schema/citation/relation/
  timeline checks pass, nothing more.
- The load-bearing reading is taken on the post-producer frozen revision
  (final1/2/3 identical over ~5 min; V17's independent 45 s snapshot stability
  and mid-write/final receipt stability corroborate). The prelim reading
  (23:29Z, while S4's map/README were placeholders) happened to be identical but
  is not load-bearing.
- The archive census uses the archive's own 9a3d648 `check_bible.py`; the tree
  census uses the tree copy, verified content-identical (`ff9fd2aa…`).
- Out-of-lane observation (not this seat's finding): parent-tree stray
  `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 bytes, mtime
  2026-10-17 20:30, content `python3: can't open file
  '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or
  directory`) corroborated by direct `ls`/`cat` — r94-F01 stray-write class at
  the parent level, outside the lane; recorded for adjacency/closure seats.

## Bottom line

**PASS** — independent census (own script, both roots): archive `9a3d648` =
171/37/134/421 and delivered tree = **172/38/134/421**, zero non-0-1 exits, with
delta exactly +1 dir (`r98-clerk-filing`, exit 0 clean) / 0 removed / 0 changed
inherited tuples (171 compared on exit+output-hash), archive integrity 1020/1020
blobs, three stable tree runs, and exact agreement with V17 including
bit-exact receipt reconciliation under both hash conventions.
