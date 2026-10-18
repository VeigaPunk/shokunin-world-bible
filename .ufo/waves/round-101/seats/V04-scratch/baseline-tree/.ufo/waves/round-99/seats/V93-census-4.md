# V93 — census-4 (round 99)

**Seat:** V93 `census-4`. Fourth census: python hashlib full inherited sweep against `4265df5`, numbers expected to match V20's published census. **They do not, because V20 published no report.**

**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree `HEAD` at every check: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (r99 blocked-dispatch note; `4265df5..HEAD` is only `LOG.md` and `SCORECARD.md`).

**Writes:** this report, and scratch `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V93-scratch/` (`poll.log`, `sweep.py`, `archive/` = `git archive 4265df5 corpus`, `hash-sweep-cap.json`, `hash-sweep-early.json`, `census_early_receipts.json`, `census_archive_receipts.json`, `inherited-sweep-early.json`). No commit, no push, no network, no nested agents. Commands from the lane root with `python3`.

**Axes:** producer-completeness, V20-identity, inherited-byte observation. A move is kept only if it does not score an unfinished delivery as the plan.

## 1. Poll-wait (20 s, 40 tries) — ABSENT

Watched `corpus/fixtures/r99-window-lapse/` (≥10 files), `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and `S1`–`S5` reports under `.ufo/waves/round-99/seats/`. Not an all-reports poll, so the SELF subtraction was never exercised.

The first poll process was killed by a 300 s tool timeout after try 15 (`t=15 ts=2026-10-17T22:07:00-0300`). Resumed at try 16 (`22:11:39-0300`) and ran through try 40. That gap is a recorded stall, not an extension past 40 tries.

Last line and exhaustion, quoted from `V93-scratch/poll.log`:

```
t=40 ts=2026-10-17T22:19:39-0300 fixture_files=10 notes=0,0 allrep=0 reports: S1:0 S2:0 S3:1 S4:1 S5:0
EXHAUSTED ts=2026-10-17T22:19:59-0300
```

Present at exhaustion and still present at the 22:36:30 re-check: the r99 fixture directory (10 files) and `S3-fixture-author.md`, `S4-fixture-docs.md`.

Absent at exhaustion and still absent at 22:36:30:

- `S1-*.md`, `S2-*.md`, `S5-*.md`
- `corpus/knowledge/r99-gate-blind-spot-table.md`
- `corpus/knowledge/r99-lapse-scope-note.md`
- `V20-*.md` (no published census to match)

V20's own poll log ends the same way (`V20-scratch/poll.log`):

```
t=40 ts=2026-10-17T22:28:51-0300 dirs=173 fixture_files=10 notes=0,0 reports: S1:0 S2:0 S3:1 S4:1 S5:0
EXHAUSTED ts=2026-10-17T22:28:51-0300
```

**Did not verify the plan.** C1 and C2 are not scored. The measurements below are the tree at the cap, not a delivered-revision verdict.

## 2. Cap-time hash sweep (observation, not a verdict)

`sweep.py` hashes every `git ls-tree -r 4265df5 -- corpus` blob with python `hashlib.sha256` against the extracted archive. It does not use `git hash-object`.

```
python3 .ufo/waves/round-99/seats/V93-scratch/sweep.py \
  .ufo/waves/round-99/seats/V93-scratch/archive \
  .ufo/waves/round-99/seats/V93-scratch/hash-sweep-cap.json
```

Observed (22:29:52-0300):

```
baseline_corpus_blobs 1826
identical 1824
mismatch_count 2
missing_count 0
mismatch_paths:
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/dependency_freeze.py
```

Mismatch bytes:

| path | worktree sha256 | archive sha256 | sizes (wt/ar) |
|---|---|---|---|
| `corpus/tools/dependency-freeze-contract.json` | `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` | `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` | 25987 / 19291 |
| `corpus/tools/dependency_freeze.py` | `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` | `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` | 29104 / 26644 |

Those two paths are S1's declared ownership. S1's report was absent, so this seat does not treat the dirty bytes as a completed C1 delivery. No other corpus blob differs. Missing: 0. Deletions/renames vs `4265df5`: 0 (`git diff --name-status --diff-filter=DR 4265df5 | wc -l` → `0`).

Extras against the same archive:

- `SKILL.md` identical (`22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5`, 16802 bytes). S2 has not written.
- `corpus/tools/README.md` identical to the archive (`294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207`, 32577 bytes; compared in the 22:07 pass, and it is not in the cap mismatch list).
- `LOG.md` and `SCORECARD.md` differ from `4265df5` and match `HEAD`. `git diff --name-only HEAD -- . ':!.ufo'` at the cap was only the two tool files. The `4265df5..HEAD` name-status is `M LOG.md` and `M SCORECARD.md` only (commits `111b9a3`, `337f0fa`), not a wave write.

Untracked outside `.ufo/` (`git ls-files --others --exclude-standard | grep -v '^\.ufo/'`): exactly the 10 `corpus/fixtures/r99-window-lapse/` files. No knowledge notes.

Fixture counts:

```
now dirs 173
now files 1040
base dirs 172    # git ls-tree -d --name-only 4265df5:corpus/fixtures
base files 1030  # git ls-tree -r --name-only 4265df5 corpus/fixtures
```

Archive extract itself: 1826 corpus files, 172 fixture dirs. `check_bible.py` sha256 worktree = archive = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.

An earlier sweep (22:03, before the contract was dirty) was 1825 identical / 1 mismatch (`dependency_freeze.py` only). The second mismatch appeared when the contract file changed (mtime 22:08:46). No inherited fixture path entered the mismatch set.

## 3. Checker census (observation, not a verdict)

Archive null control, same checker, cwd = extracted `4265df5` tree (22:04:10):

```
{"root": "archive-4265df5", "fixture_dirs": 172, "clean_exit0": 38,
 "negative_exit1": 134, "violation_lines": 421, "non_0_1": []}
```

That reproduces the r98 closure sentence in `corpus/fixtures/README.md` (172 / 38 / 134 / 421). Worktree inherited receipts from the 22:02 run matched those 172 archive receipts exactly (`inherited_receipts_identical: 172, differ: 0`).

Worktree at 22:36:30, after the poll cap, repo-relative `check_bible` (violation line = a line containing `VIOLATION`):

```
{"fixture_dirs": 173, "clean_exit0": 39, "negative_exit1": 134,
 "violation_lines": 421, "non_0_1_exits": []}
```

Same tuple as the 22:02 run. The added directory is `r99-window-lapse` (exit 0). This is an observation of an incomplete tree: S4 had rewritten the fixture README and map, S3/S4 reports were present, and S1/S2/S5 plus both knowledge notes were not. It is not a confirmation that census 172→173 is the closed round figure.

## 4. V20 identity — not established

No `V20-*.md` existed at 22:19:59, at 22:28:51 (V20's own exhaustion), or at 22:36:30. There is no published V20 number set to compare.

V20 scratch `census_inherited_receipts.json` (mtime 22:05:33, unpublished, mid-poll) has 172 receipts with exit counts `{0: 38, 1: 134}`. That file has no violation-line total and is not a report. It is not used as V20's number. Identity with V20 is **not established**.

## 5. What this seat did not do

- Did not score C1 (full-file freeze pin, 17→18, chain 6/6) or C2 (6/1/8, 21 obligations, blind-spot table). Those artifacts or reports were absent.
- Did not treat S1's dirty tool/contract bytes as a finished delivery.
- Did not extend the poll past 40 tries.
- Parent-tree `git status --porcelain` at 22:07:51 was empty. Not rechecked at the cap; not a census finding.

## Bottom line

**ABSENT** — after 40 tries (exhausted 22:19:59-0300; re-checked 22:36:30) S1, S2, and S5 reports and both r99 knowledge notes were missing, and V20 published no census, so identical-numbers was not checked and the plan was not verified.
