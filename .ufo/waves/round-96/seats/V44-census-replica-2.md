# V44 — census-replica-2 (round 96)

Seat: V44 `census-replica-2`. Scope per seat spec: after producers finish, run an
**independent second census** with a **fresh script** comparing `corpus/fixtures`
against a `git archive` of `dcb2d92`; expect **170** dirs; enumerate new paths;
require **0 unexpected inherited changes**; cross-check V24.

Baseline: r95 closure commit `dcb2d92` (working HEAD `60dba0c` = `dcb2d92` + the r95
SCORECARD closure commit; `LOG.md` carried the r96 declaration before any seat ran).
All commands run from repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with
`python3`. Writes: this report plus my declared scratch
`.ufo/waves/round-96/seats/V44-scratch/` (`census_r96.py`, `poll.sh`, `poll2.sh`,
`census-mid.json`, `census-interim.json`, `census-final.json`, `corpus-mid.json`,
`corpus-interim.json`, `corpus-final.json`, `freeze-manifest.sha256`). No commits, no
pushes, no network, no nested agents, no other file touched.

## 0. Method (fresh implementation, deliberately not V34's r95 script)

`.ufo/waves/round-96/seats/V44-scratch/census_r96.py` (written by this seat, stdlib
only): `git archive --format=tar dcb2d92 <root>` → extract to a scratch temp dir →
walk both trees → SHA-256 every file on both sides → classify
`inherited/modified/deleted/new`; directory sets both immediate-top and all-dirs via
`os.walk`; `--expected-dirs` and `--allow-new` are the pass conditions. V34 (r95)
materialized a tar and used SHA-256 too; V24's scratch shows `git ls-tree` +
`dirs-*.txt` and V56's `census_v56.py` is a third implementation — the shared verdicts
below are cross-implementation corroboration, not code reuse.

**Null control (baseline revision, before trusting the verdict):** `git archive
dcb2d92 corpus/fixtures` extracted twice → `diff -r` empty ("NULL-CONTROL:
archive==archive identical"), and the extraction counts **169 dirs / 1000 files**
agree with the git-native counts at the same revision
(`git ls-tree -d --name-only dcb2d92 corpus/fixtures/ | wc -l` → 169;
`git ls-tree -r --name-only dcb2d92 corpus/fixtures | wc -l` → 1000). So the walker
reproduces the known r95-closure fixture inventory exactly.

## 1. Poll-wait record (20 s cadence; producer artifacts only)

Watched the fixture tree + the six `Q*.md` producer reports. Timeline observed (file
mtimes at freeze): fixture dir absent 17:37, appeared 17:38 (8 files); Q4's report
sighted by 17:41 and final at 17:47:19; Q5's two files 17:43:09/17:43:17 with Q5
report 17:45:37; Q6 report 17:47:16; Q3 report 17:47:26; Q2's two files
17:50:17/17:51:26, Q2 report 17:52:12; Q1 report 17:52:17 (an earlier Q1 revision was
sighted at 17:49 — producers rewrote reports after first landing; corpus bytes are
what matter and are covered by the freeze manifest). **All six producer reports and
all ten declared fixture files were present before my frozen snapshot; nothing in
this seat's scope was ABSENT.**

**Freeze stability:** `sha256sum -c .ufo/waves/round-96/seats/V44-scratch/freeze-manifest.sha256`
→ **16/16 OK** at 2026-10-17T17:52:57-03:00 (10 fixture files + `map_obligations.py`,
`map-obligations-contract.json`, tools `README.md`, `dependency_freeze.py`,
`dependency-freeze-contract.json`, `r96-response-scope-note.md`).

## 2. Final fixtures census — 170 dirs, +10 files, 0 inherited changes (primary receipt)

```
$ python3 .ufo/waves/round-96/seats/V44-scratch/census_r96.py --ref dcb2d92 \
    --expected-dirs 170 --allow-new r96-crossing-response
{ "ref": "dcb2d92", "root": "corpus/fixtures",
  "baseline_top_dirs": 169, "work_top_dirs": 170,
  "baseline_all_dirs": 169, "work_all_dirs": 170,
  "baseline_files": 1000, "work_files": 1010, "inherited_files": 1000,
  "modified_inherited": [], "deleted_inherited": [],
  "new_top_dirs": ["r96-crossing-response"], "gone_top_dirs": [],
  "new_files_count": 10, "unexpected_new_files": [], "unexpected_new_dirs": [],
  "verdict": "PASS", "reasons": [] }
CENSUS PASS: dirs=170 files=1010 modified=0 deleted=0 new=10
```
(receipt trimmed in this quote only: the full `new_files` list is expanded below)

`corpus/fixtures` has no nested subdirectories, so `all_dirs == top_dirs` on both
sides and the +1 dir is the whole directory delta. The 10 new paths are exactly the
declared C2 tree:

```
r96-crossing-response/{README.md, claim-excerpt-map.md, contradictions.json,
entities.json, fictional-excerpts.md, inspiration-note.md, relations.json,
source-excerpt.md, sources.json, timeline.json}
```

Run repeated at 17:52:02 (`census-final.json`) after all six producer reports existed:
same 170/1010/0/0/10 result; an interim run at 17:44:33 (`census-interim.json`) after
Q5's files landed returned the identical receipt, so the directory inventory was
stable across ≥2 snapshots (individual file hashes were not yet final then — see
§7.1).

**Second, independent method for the same claim** (git-native, no script):

```
$ git diff --name-status dcb2d92 -- corpus/fixtures
(no output)
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
170
```

No tracked fixture path was added, deleted, modified or mode-changed; every new file
is untracked.

## 3. Corpus-wide / repo-wide sweep ("0 unexpected inherited changes")

`census_r96.py --root corpus` (filesystem SHA-256 over the whole `corpus/` tree):

```
all_dirs 209 → 211   (new: fixtures/r96-crossing-response, tools/__pycache__)
files   1791 → 1808  (+17)
modified: ['tools/README.md', 'tools/map-obligations-contract.json', 'tools/map_obligations.py']
deleted: []
new: 10 fixture files + knowledge/r96-response-scope-note.md +
     tools/dependency_freeze.py + tools/dependency-freeze-contract.json +
     tools/__pycache__/{boundary_doc_check,dependency_freeze,map_obligations,support_check}.cpython-314.pyc
```

Tracked+untracked view:

```
$ git diff --name-status dcb2d92 -- . ':!.ufo'
M	LOG.md
M	SCORECARD.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
$ git ls-files --others --exclude-standard | grep -v '^\.ufo/'
corpus/fixtures/r96-crossing-response/… (10 files)
corpus/knowledge/r96-response-scope-note.md
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py
```

Classification of every row, against the declared producer set:

- `corpus/tools/map_obligations.py` (Q1), `corpus/tools/map-obligations-contract.json`
  + `corpus/tools/README.md` (Q2) — the declared C1 modified set; nothing else
  tracked-and-modified anywhere.
- 10 fixture files (Q4/Q5), `corpus/knowledge/r96-response-scope-note.md` (Q6),
  `corpus/tools/dependency_freeze.py` + `dependency-freeze-contract.json` (Q3) —
  the declared new set; nothing else untracked outside `.ufo/`.
- `LOG.md`: 67 insertions / 0 deletions vs `dcb2d92` — purely additive, the
  pre-dispatch r96 declaration; `git diff --name-status 60dba0c -- LOG.md` shows the
  work tree is ahead of HEAD only by that declaration.
- `SCORECARD.md`: work tree == HEAD `60dba0c` (`git diff --name-status 60dba0c --
  SCORECARD.md` → no output), i.e. the change vs `dcb2d92` is the r95 closure commit
  `60dba0c`, not an r96 seat write.
- The 4 `tools/__pycache__/*.pyc` rows are gitignored build residue (`.gitignore:2
  __pycache__/`), never seen by a git-native census — classified, not a change.
- No stray `map-obligations-self-test-*` / `dependency-freeze-self-test-*` dirs at the
  repo root at freeze time (`ls -d …` → none).

Verdict: the inherited change set is exactly the declared producer-owned set; zero
unexpected changes anywhere in the repo outside `.ufo/` seat reports/scratch.

## 4. Preservation of inherited fixtures and the declared edits (own byte checks)

`modified_inherited: []` covers all 1000 inherited `corpus/fixtures` files — the r95
tree and every other fixture are byte-unchanged vs `dcb2d92`.

Own comparison `r96-crossing-response` against `r95-crossing-aftermath`:

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r95/$f r96/$f && echo BYTE-IDENTICAL $f; done
BYTE-IDENTICAL r95->r96: entities.json
BYTE-IDENTICAL r95->r96: relations.json
BYTE-IDENTICAL r95->r96: contradictions.json
BYTE-IDENTICAL r95->r96: inspiration-note.md
BYTE-IDENTICAL r95->r96: source-excerpt.md
fictional-excerpts strict prefix: True 1845 -> 2588
sources.json inherited rows parsed-equal: True 4 -> 5
timeline.json inherited rows parsed-equal: True 4 -> 5
```

The new event is exactly as declared (parsed from the delivered file):
`response-evin-salt-court`, tick 12, `entity_id: evin`, `place_id: salt-court`,
`depends_on: ["aftermath-missing-evin"]`, `source_id: evin-response-note`; the new
source is `evin-response-note` (sources 4→5). Counts: 5 entities / 1 relation /
5 events / 5 sources / 0 contradictions.

Producer declared hashes vs disk at freeze — all match:

| File | Declared by | sha256 (disk == declaration) |
|---|---|---|
| `map_obligations.py` | Q1 | `2b0ba815…c4a3ba8` |
| `map-obligations-contract.json` | Q2 | `97b76bb8…c936493b6` |
| tools `README.md` | Q2 | `965b29cd…5b20a91f24` |
| `dependency_freeze.py` | Q3 | `a3b57978…0457f0980` |
| `dependency-freeze-contract.json` | Q3 | `7d568cc4…468576975` |
| `sources.json` / `timeline.json` / `fictional-excerpts.md` | Q4 | `9f973f63…fabf32d` / `ea0225f9…208815b9` / `06b11bec…41cb2fe3` |
| fixture `README.md` / `claim-excerpt-map.md` | Q5 | `ff52ced4…3558c456` / `5093d72e…83045bfd8` |

Q6's note declares no hash in its report; it declares 61 lines and the delivered file
is 61 lines (`wc -l` → 61), sha256 `6db32ca2…ae157c6`.

## 5. W05 pin re-check (independent reproduction, for the V24 cross-check)

```
$ sha256sum -c .ufo/waves/round-94/work/W05-baseline-corpus.sha256
983 OK / 1 FAILED / 984 rows
corpus/fixtures/README.md: FAILED
$ sha256sum corpus/fixtures/README.md
f3733aad746f68fd2798ec1d9a72b50becf779375d272014e0e03fdbee11141c
$ git show dcb2d92:corpus/fixtures/README.md | sha256sum
f3733aad746f68fd2798ec1d9a72b50becf779375d272014e0e03fdbee11141c
```

The single broken pin row is `corpus/fixtures/README.md`, and the working tree equals
the `dcb2d92` blob (last writer `dcb2d92` itself) → **pre-existing at the r96
baseline**, not an r96 write. Pin composition: 980 fixture rows + 4 tool rows
(`boundary-doc-contract.json`, `boundary_doc_check.py`, `discriminate_check.py`,
`support_check.py`). Unpinned fixture files computed by set difference: **30 =
r94-paired-crossing (10) + r95-crossing-aftermath (10) + r96-crossing-response (10)**;
980 pinned fixture rows + 30 unpinned = 1010, matching the census exactly; no pinned
fixture row is missing.

## 6. Cross-check against V24 (`V24-preservation-census.md`, landed ~17:55) — full agreement

V24's report was absent at my frozen snapshot (17:52–17:54) and landed during this
seat's 13-minute poll (`V24_HIT try=9`); this section was updated after reading it.
**Every quantity V24 reports agrees with this seat:**

| Quantity | V24 | V44 (this seat) | Agree |
|---|---|---|---|
| fixture dirs now / baseline | 170 / 169 | 170 / 169 | yes |
| fixture files now / baseline | 1010 / 1000 | 1010 / 1000 | yes |
| dir delta | `166a167 > r96-crossing-response`, 0 removed | same | yes |
| inherited changes in `corpus/` | 3 tool files | 3 tool files (same names) | yes |
| repo-wide inherited change set | + `LOG.md`, + `SCORECARD.md` (r95 close commit) | same | yes |
| new paths outside `.ufo/` | 13 (10 fixture + note + 2 tools) | same | yes |
| 5 byte copies identical / 3 declared edits | yes (own SHA-256 of blobs) | yes (own `cmp`/prefix) | yes |
| `sources.json` / `timeline.json` prefix parsed-equal | yes (4→5) | yes (4→5) | yes |
| new event/source fields | evin/salt-court/depends_on `[aftermath-missing-evin]` | same | yes |
| W05 pin: rows / ok / changed | 984 / 983 / 1 (`corpus/fixtures/README.md`, pre-existing) | same, own run | yes |
| unpinned fixture files | 30 = r94 (10) + r95 (10) + r96 (10) | same | yes |
| snapshot hashes | 16 files; `snap-a.sha256` == `snap-b.sha256` (17:53→17:54) | 16/16 identical to my `freeze-manifest.sha256` | yes |
| `__pycache__` | 4 ignored `.pyc`; excluded from change sets | same classification | yes |

V24's own scratch artifacts, read before its report landed, already agreed:
`dirs-base.txt` = 169 lines, `dirs-now.txt` / `dirs-final.txt` = 170 lines with
`diff` = exactly `166a167 > r96-crossing-response`; `snap-a.sha256`/`snap-b.sha256`
byte-identical to each other and to my freeze manifest on all 16 shared paths
(16 equal, 0 differing, 0 one-sided); `copy_check.py` byte-compares the r96 fixture
against `dcb2d92` r95 blobs — the same object of comparison as my §4.

Other independent r96 censuses agree numerically with this seat:

- V56 `census_v56.py` (git-archive SHA-256): "169→170 confirmed; zero inherited
  modifications/deletions; r95 fixture byte-untouched" and its comparison table row
  "Census | 169→170, zero inherited changes | 169→170, modified=[] deleted=[]
  (git-archive SHA-256)".
- V55 quote 3: `find corpus/fixtures -maxdepth 1 -mindepth 1 -type d | wc -l → 170`.

**Disagreements: none numerically.** Two method differences, both explained:

1. **`__pycache__` rows.** My filesystem walks see the 4 gitignored
   `tools/__pycache__/*.pyc`; V24's git-native enumerations never see them (V24 §6.2
   reaches the same arithmetic from the other side: 1808 − 4 ignored = 1804 = 1791
   inherited + 13 new). Not a change in either direction.
2. **Symlink false positive.** V24's repo-wide `git hash-object` sweep flags the
   r94 artifact `.ufo/waves/round-94/work/W16-scratch/cluster/escape.md` (a symlink);
   my repo-wide view was git-native (`git diff` / `git ls-files --others`), so it
   never sees it. Same artifact r95's V15 recorded; not an r96 change.

## 7. Mid-round observations (explained, not discrepancies at freeze)

1. **Q4 intermediate caught.** My 17:39 snapshot hashed `sources.json`
   `10da97ee…` and `timeline.json` `50e3d2b6…`; the final files are `9f973f63…` /
   `ea0225f9…`. Q4's report discloses exactly this: a mid-seat rewrite at 17:39
   (joining comma moved to `  },\n  {` convention) before its receipts ran. The final
   bytes match Q4's declared hashes; my earlier reading caught the discarded
   intermediate, and I re-measured rather than trusting the stale snapshot.
2. **Q1 tool intermediate.** `map_obligations.py` read `db924c64…` at 17:44:33
   (mtime 17:44:20); the final revision is `2b0ba815…` (mtime 17:47:24), matching
   Q1's report. My census receipts at 17:52 use the final revision.
3. **Q6 note intermediate.** `r96-response-scope-note.md` read `9f1a920a…` at
   17:46:23; final `6db32ca2…` (mtime 17:47:02, 61 lines), written *before* Q6's
   report (17:47:16) — no post-report write.
4. All three are producer-declared or plainly time-ordered rewrites; none survives at
   the frozen revision, and none touches an inherited path.

## 8. Findings summary

| # | Finding | Class |
|---|---|---|
| F-V44-1 | Fresh-script census: **170 dirs / 1010 files**, +10 files all under `r96-crossing-response`, 0 modified, 0 deleted inherited, 0 unexpected new paths, no gone dirs | PASS |
| F-V44-2 | Second method (`git diff --name-status dcb2d92 -- corpus/fixtures`) empty; `find` count 170 | PASS |
| F-V44-3 | Corpus-wide inherited change set == declared producer set (3 modified tools Q1/Q2; new: 10 fixture + note + 2 tools); `LOG.md` additive 67/0 (pre-dispatch declaration); `SCORECARD.md` == HEAD `60dba0c` r95 closure; nothing else anywhere outside `.ufo/` | PASS |
| F-V44-4 | 5 byte copies byte-identical to r95; `fictional-excerpts.md` strict 1845→2588 prefix; sources/timeline inherited rows parsed-equal; new event/source exactly as declared; all producer declared hashes match disk | PASS |
| F-V44-5 | W05 pin: 1 broken row `corpus/fixtures/README.md`, pre-existing at baseline (equals `dcb2d92` blob); unpinned = 30 (r94+r95+r96 trees), 980+30=1010 consistent | finding (inherited; owner: closure / re-pin) |
| F-V44-6 | V24's census report landed during my poll and **agrees on every quantity** (169→170 dirs, 1000→1010 files, same single-dir delta, same change set, same pin finding, 16/16 identical snapshot hashes); V56/V55 censuses also agree; no numerical disagreement, only the explained `__pycache__`/symlink view differences | PASS |
| F-V44-7 | `tools/__pycache__/*.pyc` gitignored build residue; no stray self-test dirs at freeze | methodology note |

Bottom line: **PASS** — the independent fresh-script `git archive dcb2d92` census
confirms **170 fixture dirs (baseline 169) / 1010 files (baseline 1000)**, exactly the
10 declared new files under `corpus/fixtures/r96-crossing-response/`, **zero
modified/deleted inherited paths** under `corpus/fixtures` and zero unexpected changes
anywhere in `corpus/` (only the declared producer set plus the pre-dispatch `LOG.md`
declaration and the r95 closure `SCORECARD.md`); V24's report — landed during my poll —
agrees on every quantity (same single-dir delta, same change set, same pre-existing
W05 pin row, 16/16 identical snapshot hashes), as do V56's and V55's independent
censuses, with no numerical disagreement anywhere.
