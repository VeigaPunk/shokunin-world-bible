# F13 — preservation census (round-94 FOLLOW-UP)

Seat: F13, preservation-census verifier. Scope: replicate the corpus/fixtures
preservation census independently — directory count, inherited-byte equality vs
baseline `9c2eea3`, exact enumeration of new paths, byte-diff of any unexpected
inherited change. Verified revision: HEAD `65a9329` (WORK candidate `abbc3e0`,
baseline `9c2eea3`). All commands run from repo root with `python3`.

Hard-rule compliance: no commit, no push, no write outside
`.ufo/waves/round-94/followup/F13-preservation-census.md` and
`.ufo/waves/round-94/followup/F13-scratch/`. No corpus/ file was touched
(worktree verified clean vs HEAD below). No network, no nested agents.

## Scripts (own, independent)

- `.ufo/waves/round-94/followup/F13-scratch/census_bytes.py` — path→git-blob
  census `9c2eea3` vs HEAD vs worktree, plus directory counts.
- `.ufo/waves/round-94/followup/F13-scratch/census_tuples.py` — behavioral
  `(exit, stdout, stderr)` tuple per fixture dir; baseline tree extracted with
  `git archive 9c2eea3 -- corpus/fixtures/` into `F13-scratch/baseline/`.
- `.ufo/waves/round-94/followup/F13-scratch/crosscheck_work_artifacts.py` —
  cross-check against the WORK wave's own W04/W05 artifacts.

Raw outputs: `census-bytes.json`, `census-tuples.json` in the same scratch dir.

## 1. Directory census — 167 → 168, exactly one addition

```
$ python3 .ufo/waves/round-94/followup/F13-scratch/census_bytes.py
baseline 9c2eea3 tracked files: 980
HEAD 65a9329 tracked files: 990
top-level fixture dirs: baseline 167 -> HEAD 168 -> disk 168
dirs added: ['r94-paired-crossing']
dirs removed: []
```

Two further methods agree on the same counts:
`git ls-tree 9c2eea3 -- corpus/fixtures/` → `167 tree` + 2 blobs
(`README.md`, `check_bible.py`); at HEAD → `168 tree` + 2 blobs; on disk
`find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → `168`; the
`git archive` extraction enumerated 167 baseline dirs (`census_tuples.py`
reported `baseline dirs: 167  delivered dirs: 168`). No nested fixture dirs
(`find corpus/fixtures -mindepth 2 -type d` → 0).

## 2. Byte census — 0 inherited paths changed, 0 deleted

```
paths added (10): ... (all under corpus/fixtures/r94-paired-crossing/)
paths modified (0): []
paths deleted (0): []
disk files: 990; untracked=[]; missing=[]; dirty=[]
```

The 10 new paths with their HEAD blob hashes (`git ls-tree -r HEAD -- corpus/fixtures/r94-paired-crossing/`):

```
100644 blob da3d1effb87e29719e74d7a4f1d95a773009a10d  README.md
100644 blob 7edafa24aef9f789ccbe7ed7a9aebec5584c6321  claim-excerpt-map.md
100644 blob fe51488c7066f6687ef680d6bfaa4f7768ef205c  contradictions.json
100644 blob 1797bd87bb585909f5f5c2bb9934afe94efef0d0  entities.json
100644 blob c9cb17d552c01f8bbb6c5c15ee429dfcacc34eb5  fictional-excerpts.md
100644 blob e6b71d7e67ecff67f12606cf800576dab732c24b  inspiration-note.md
100644 blob 2804ae91240dbf34753bf955d4fab9ffeab0a8df  relations.json
100644 blob 9a1864013784ded68ea235c183901cda3f0046cb  source-excerpt.md
100644 blob 59d08da605c01443f2fe5163a06cee0712c99436  sources.json
100644 blob bd25265efbd21257b54c0a7893edcdba3e2c30a2  timeline.json
```

Every inherited path is blob-identical at `9c2eea3` and HEAD; the on-disk
worktree also matches HEAD for all 990 fixture files (0 dirty, 0 untracked,
0 missing under `corpus/fixtures/`). The whole corpus delta is additive:
`git diff --numstat 9c2eea3..HEAD -- corpus/` sums to 1025 added / 0 deleted
lines; fixtures alone 10 files / 247 added / 0 deleted.

## 3. Behavioral tuple census — 0 inherited tuples changed

Definition used (replicating the r89 CB1 census semantics): per fixture dir,
the tuple `(exit code, sha256(stdout), sha256(stderr))` of
`python3 check_bible.py <dir>`.

```
$ python3 .ufo/waves/round-94/followup/F13-scratch/census_tuples.py
baseline dirs: 167  delivered dirs: 168  inherited: 167
changed tuples among inherited: 0
control (same dir, both checker blobs) changed: 0
added dirs: ['r94-paired-crossing']
  r94-paired-crossing: exit=0 stdout_lines=1
removed dirs: []
```

Two controls make this robust:

- **Harness artifact found and neutralized, reported as observed.** The first
  run reported 5 changed tuples (`r5-missing-file`, `r62-missing`,
  `r67-claim-source-unavailable-{control,empty,whitespace}`). A diff of the
  actual stdout showed every difference was only the harness-specific absolute
  path inside the checker's cannot-load message, e.g.:
  `...No such file or directory: '.../F13-scratch/baseline/corpus/fixtures/r5-missing-file/contradictions.json'`
  vs `...'/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'`.
  All 5 dirs are negative fixtures whose message echoes the passed path; the
  violation text, counts and exits were identical. `census_tuples.py` now
  normalizes both fixture roots to `<FIXTURE_ROOT>` before hashing (comment in
  the script records why). After normalization: 0 changed tuples.
- **Same-dir checker control.** The baseline checker blob run against the
  *delivered* dirs vs the delivered checker against the same dirs: 0 changed
  tuples over all 168 dirs. Independently, the checker file is byte-identical
  at both revisions (`git rev-parse 9c2eea3:corpus/fixtures/check_bible.py` =
  `git rev-parse HEAD:...` = `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0`;
  `sha256sum corpus/fixtures/check_bible.py` →
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`), so no
  checker-behavior change could hide a fixture change.

The new fixture alone adds one exit-0 dir: delivered distribution 34×exit-0 /
134×exit-1 (baseline 33/134). Its delivered tuple:
`{"exit": 0, "violations": 0, "stdout_lines": 1, "stdout_sha256":
"afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e"}`
(same CLEAN stdout digest as other clean fixtures).

## 4. Cross-checks against WORK-wave artifacts

Independent corroboration, not authority — my census was computed from git and
the worktree, these artifacts were compared after the fact:

- `crosscheck_work_artifacts.py` (final output):
  ```
  W04 dirs: 167  my baseline dirs: 167  dir sets equal: True
  W04 exit/violation mismatches: 0
  baseline tracked fixture blobs (mine): 980
  W05 fixture rows: 980  mismatches vs recomputed: 0  missing-from-manifest: 0
  W05 rows mentioning r94-paired-crossing: 0
  ```
  W04's recorded baseline exit split `{1: 134, 0: 33}` equals my baseline
  replay; W04's `_meta.checker_sha256` `ff9fd2aa…` equals my measured checker
  sha256; W05 has 0 rows mentioning `r94-paired-crossing` (correct: it is the
  pre-change baseline).

## 5. Byte-diff of unexpected inherited changes

None exist. 0 inherited paths differ by blob at `9c2eea3` vs HEAD and 0 on
disk vs HEAD, so there is no unexpected inherited change to byte-diff. The only
inherited-content comparison in this seat is therefore the equality result
above; had any path shown up in `paths_modified`, it would have been diffed and
reported here.

## Adjacent observation (outside census scope, flagged for the judge)

During this seat's first `git status --short`, an untracked directory
`map-obligations-self-test-6tolvre9/` appeared at the repo root; on the next
check it was gone (`git status --short` then showed only
`?? .ufo/waves/round-94/followup/`). `corpus/tools/map_obligations.py:604`
creates its self-test scratch with
`tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`
and `ROOT = Path(__file__).resolve().parents[2]` (`:42`) = repo root, so a
running `--self-test` writes a transient directory into the live tree
(auto-removed on exit). This is consistent with a concurrent follow-up seat's
in-flight self-test, not a defect in the delivered fixture state, and it did
not affect this census (outside `corpus/fixtures/`; the worktree check ran
after it vanished, reporting 0 untracked). Left for the judge to weigh against
the "no live-tree writes" wording of the wave spec.

## Reproduction

```sh
python3 .ufo/waves/round-94/followup/F13-scratch/census_bytes.py
python3 .ufo/waves/round-94/followup/F13-scratch/census_tuples.py
python3 .ufo/waves/round-94/followup/F13-scratch/crosscheck_work_artifacts.py
```

## Bottom line

PASS — 168 fixture dirs (167 inherited + `r94-paired-crossing`), 0 inherited
paths modified or deleted (blob-level and worktree-level), 0 inherited
behavioral tuples changed, and the only additions are exactly the 10
`corpus/fixtures/r94-paired-crossing/` paths listed above.
