# F36 — scope-creep verification (round 94 FOLLOW-UP)

**Seat:** F36
**Role:** scope-creep / blast-radius verification of the r94 WORK candidate
**Scope checked:** `git diff 9c2eea3..abbc3e0` (parent baseline → checkpoint commit)
**Verdict mechanism:** blob-level comparison, not path-name inspection

---

## 1. Baseline / checkpoint identity

```
$ git log --oneline -5
65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch
b8b50c8 Merge origin/main preserving wiki update and lore training history
abbc3e0 lore r94: checkpoint Luna WORK candidate pending DeepSeek review
9c2eea3 lore r93: close verified claims and correct historical admission records
7a3a795 lore r93: replace HEAD-bound R10 receipt with content-pinned replay

$ git rev-parse abbc3e0^
9c2eea3b58a090f8820c7a723d2f6a22b46ae52b
```

`abbc3e0^ == 9c2eea3`, so the seat-specified range is exactly the single WORK checkpoint commit — no intermediate commits are being hidden inside the range.

Total range size:

```
$ git diff --stat 9c2eea3..abbc3e0 | tail -1
 154 files changed, 7554 insertions(+)
```

Zero deletions in the whole range. Working tree is clean against HEAD (`git status --porcelain` → empty output), so the committed diff is the complete change set; no uncommitted author work is floating outside the checkpoint.

---

## 2. Modified / deleted / renamed paths — the core question

```
$ git diff --name-status --diff-filter=MDR 9c2eea3..abbc3e0 -- corpus/
(no output)

$ git diff --name-status --diff-filter=MDR 9c2eea3..abbc3e0
M	LOG.md
M	SCORECARD.md
```

**Under `corpus/` there is not a single modified, deleted, or renamed path.** Repo-wide, the only two non-additive paths are `LOG.md` and `SCORECARD.md` (assessed in §5).

---

## 3. Blob-level corpus comparison (strongest check)

Path-name diffs can miss in-place content edits. I therefore compared every corpus blob hash:

```
$ git ls-tree -r 9c2eea3 -- corpus/ | awk '{print $3" "$4}' | sort -k2 > base
$ git ls-tree -r abbc3e0 -- corpus/ | awk '{print $3" "$4}' | sort -k2 > head
$ diff base head
base paths: 1767  head paths: 1780
964a965,974
> 7edafa24aef9f789ccbe7ed7a9aebec5584c6321 corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md
> fe51488c7066f6687ef680d6bfaa4f7768ef205c corpus/fixtures/r94-paired-crossing/contradictions.json
> 1797bd87bb585909f5f5c2bb9934afe94efef0d0 corpus/fixtures/r94-paired-crossing/entities.json
> c9cb17d552c01f8bbb6c5c15ee429dfcacc34eb5 corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
> e6b71d7e67ecff67f12606cf800576dab732c24b corpus/fixtures/r94-paired-crossing/inspiration-note.md
> da3d1effb87e29719e74d7a4f1d95a773009a10d corpus/fixtures/r94-paired-crossing/README.md
> 2804ae91240dbf34753bf955d4fab9ffeab0a8df corpus/fixtures/r94-paired-crossing/relations.json
> 9a1864013784ded68ea235c183901cda3f0046cb corpus/fixtures/r94-paired-crossing/source-excerpt.md
> 59d08da605c01443f2fe5163a06cee0712c99436 corpus/fixtures/r94-paired-crossing/sources.json
> bd25265efbd21257b54c0a7893edcdba3e2c30a2 corpus/fixtures/r94-paired-crossing/timeline.json
990a1001
> bc70506647199bae58e8ea9450bac0977d74eb9b corpus/knowledge/r94-cross-myth-design-comparison.md
1765a1777,1778
> e26574ad36706594f732f8819f66dc706e537141 corpus/tools/map-obligations-contract.json
> 5801192b60f2905356ec6802f757d36dd58d2f25 corpus/tools/map_obligations.py
```

Every line of the diff is a `>` (addition). There is no `<` line and no paired add/remove, i.e. **all 1767 pre-existing corpus blobs are byte-identical between baseline and checkpoint.** The 13 additions are exactly the declared r94 set:

| bucket | count | paths |
|---|---|---|
| new r94 fixture | 10 | `corpus/fixtures/r94-paired-crossing/{README.md, claim-excerpt-map.md, contradictions.json, entities.json, fictional-excerpts.md, inspiration-note.md, relations.json, source-excerpt.md, sources.json, timeline.json}` |
| new r94 tool | 1 | `corpus/tools/map_obligations.py` |
| new r94 tool contract | 1 | `corpus/tools/map-obligations-contract.json` |
| new r94 knowledge | 1 | `corpus/knowledge/r94-cross-myth-design-comparison.md` |

Counted independently:

```
$ git diff --name-status --diff-filter=A 9c2eea3..abbc3e0 -- corpus/ | wc -l
13
$ git diff --name-only --diff-filter=A 9c2eea3..abbc3e0 -- corpus/fixtures/r94-paired-crossing/ | wc -l
10
```

---

## 4. Named protected files and prior artifacts

Explicit blob-hash comparison of every file the seat named as protected:

```
$ for f in corpus/fixtures/check_bible.py corpus/live/rejected-r4/check_bible.py \
           corpus/tools/support_check.py corpus/tools/boundary_doc_check.py \
           corpus/tools/discriminate_check.py; do compare blobs at both revs; done
SAME  corpus/fixtures/check_bible.py            20c56dbb90d9
SAME  corpus/live/rejected-r4/check_bible.py    072402681f7c
SAME  corpus/tools/support_check.py             a69ae9d27ad1
SAME  corpus/tools/boundary_doc_check.py        4daa9998023f
SAME  corpus/tools/discriminate_check.py        aa601eee3ec2
```

Note: `check_bible.py` does **not** live at `corpus/tools/check_bible.py` (that path resolves in neither revision); the two tracked copies are `corpus/fixtures/check_bible.py` and `corpus/live/rejected-r4/check_bible.py`. Both are unchanged.

- **No prior knowledge doc modified.** `git diff --name-status 9c2eea3..abbc3e0 -- corpus/knowledge/` returns only `A corpus/knowledge/r94-cross-myth-design-comparison.md`. The 12 pre-existing knowledge files (incl. `r93-r8-worked-example.md`, `r91-c9-watch.md`, `reference-ledger.md`) are untouched.
- **r88 fixture untouched.** `git diff --name-status 9c2eea3..abbc3e0 -- corpus/fixtures/r88-m3-maya-cluster/` → empty. So C1's "explicit continuation of r88" claim is achieved without rewriting the r88 snapshot — the new fixture is an additional directory, and `corpus/fixtures/r94-paired-crossing` does not exist at `9c2eea3` (`git cat-file -e` → NO).
- **No other fixture directory touched.** `git diff --name-only 9c2eea3..abbc3e0 -- corpus/fixtures/ | grep -v '^corpus/fixtures/r94-paired-crossing/'` → empty output. Baseline and checkpoint `git ls-tree --name-only corpus/fixtures/` listings are identical apart from the appended `r94-paired-crossing` entry:

```
$ git ls-tree -d --name-only 9c2eea3 corpus/fixtures/ | wc -l   # 167
$ git ls-tree -d --name-only abbc3e0 corpus/fixtures/ | wc -l   # 168
$ git ls-tree    --name-only 9c2eea3 corpus/fixtures/ | wc -l   # 169 (incl. README.md, check_bible.py)
$ git ls-tree    --name-only abbc3e0 corpus/fixtures/ | wc -l   # 170
```

The +1 is entirely `r94-paired-crossing`; no directory was renamed, merged, or removed.

---

## 5. Root-file modifications (`LOG.md`, `SCORECARD.md`) — in or out of scope?

These are the only two modified paths, and they are outside both buckets the seat named. They are, however, the lane's own append-only records, which `wave-spec.md` explicitly permits:

- `wave-spec.md:31` — "No existing fixture, checker, gate, knowledge record or past wave is modified by authors. Documentation/registry additions are appended after the actual tools/files exist and their commands run."
- `wave-spec.md:33` — "Corpus corrections and LOG are append-only."

Both edits are provably pure appends:

```
$ git diff --numstat 9c2eea3..abbc3e0 -- LOG.md SCORECARD.md
11	0	LOG.md
16	0	SCORECARD.md

$ git diff --unified=0 ... | grep -c '^-[^-]'
0

$ git diff --unified=0 ... | grep -E '^@@'
@@ -2662,0 +2663,11 @@ ...
@@ -367,0 +368,16 @@ ...
```

Zero removed lines; both hunks start at the pre-existing EOF (old range length 0, new range appended). Content is a new "Round 94 — luna round 8 of 12, WORK checkpoint" section in each. This is documentation of the candidate, not a mutation of prior records, and it is not a claim of round closure (LOG explicitly states "Round 94 is not closed, rejected, or admitted").

Related negative checks:

```
$ git diff --name-only 9c2eea3..abbc3e0 -- .ufo ':!.ufo/waves/round-94' PROVINCE.md SHONEN.md MANIFEST.md registry/ corpus/README.md
(no output)
$ git diff --name-only 9c2eea3..abbc3e0 -- '.ufo/waves/round-9[0-3]' '.ufo/waves/round-8*'
(no output)
```

No other lane state file, no registry, no MANIFEST, no `PROVINCE.md`/`SHONEN.md`, no `corpus/README.md`, and no earlier round wave directory was touched.

---

## 6. Full path bucket census

Classification of all 154 changed paths:

| bucket | count |
|---|---|
| A: new r94 fixture (`corpus/fixtures/r94-paired-crossing/`) | 10 |
| B: new r94 tool + contract (`corpus/tools/`) | 2 |
| C: new r94 knowledge (`corpus/knowledge/r94-*`) | 1 |
| D: `.ufo/waves/round-94/` bookkeeping | 139 |
| E: root append-only lane records (`LOG.md`, `SCORECARD.md`) | 2 |
| **unbucketed** | **0** |
| **total** | **154** |

The unbucketed count is zero, and 10+2+1+139+2 = 154 matches `git diff --stat`'s "154 files changed". Nothing in the range falls outside the declared r94 surface.

Bookkeeping shape check — every entry under `.ufo/waves/round-94/work/` is seat-prefixed, and the round directory contains only expected members:

```
$ ls -A .ufo/waves/round-94/work/ | grep -vE '^W[0-9]{2}'
(no output)
$ ls -A .ufo/waves/round-94/
followup  frozen  wave-spec.json  wave-spec.md  work  work-receipt.json  work-results.xml
```

The nested `W13-source-controls/`, `W15-fixture/`, `W16-scratch/` directories all match the leaf ownership rule in `wave-spec.md:32` ("Each leaf owns only its assigned new files plus `.ufo/waves/round-94/work/<ID>*` artifacts").

The follow-up declaration commit is likewise self-contained:

```
$ git show --stat --oneline 65a9329
65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch
 LOG.md | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)
```

---

## 7. Working-tree residues found (not part of the committed diff)

`git status --porcelain` is clean, so these do not enter the checkpoint — but two non-committed artifacts exist on disk and are reported exactly as observed.

**(a) Transient `--self-test` scratch directory at repo root.** Observed present, then gone:

```
$ git status --porcelain --ignored
?? .ufo/waves/round-94/followup/
?? map-obligations-self-test-km8dsns6/
!! .ufo/interactive-sessions/
!! corpus/tools/__pycache__/

# later, same session:
$ ls -la map-obligations-self-test-km8dsns6/
ls: cannot access 'map-obligations-self-test-km8dsns6/': No such file or directory
```

Source of that name, from the new tool:

- `corpus/tools/map_obligations.py:42` — `ROOT = Path(__file__).resolve().parents[2]`
- `corpus/tools/map_obligations.py:604` — `with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT) as temporary:`

So `--self-test` creates an isolated directory **in the repository root** and removes it on exit via `TemporaryDirectory`. The directory I saw was mid-run scratch from a concurrently executing self-test (another seat), not leaked state. Assessment: by-design and self-cleaning, but it does mean any observer doing a `git status` during a self-test run sees an untracked root directory, and a hard kill (SIGKILL / power loss) would leave one behind. Bounded, non-blocking, worth naming.

**(b) Ignored bytecode under `corpus/`.**

```
$ git status --porcelain --ignored corpus/
!! corpus/tools/__pycache__/
$ find corpus/tools/__pycache__ -printf '%T+ %p\n'
2026-10-17+15:39:32.7997163780 corpus/tools/__pycache__
2026-10-17+14:04:33.4073611860 corpus/tools/__pycache__/boundary_doc_check.cpython-314.pyc
2026-10-17+15:39:32.7997163780 corpus/tools/__pycache__/map_obligations.cpython-314.pyc
```

`__pycache__/` is gitignored (`.gitignore` contains `__pycache__/`), so this is untracked interpreter output from *running* the new tool, not a corpus edit — the corpus blob comparison in §3 is unaffected. Note `map_obligations.cpython-314.pyc` is fresh (same minute as the last observed self-test activity), and `corpus/tools/` had no prior `__pycache__` from `boundary_doc_check.py` until 14:04. Both are build byproducts, not authored files.

**Negative write check on the new tool.** The new CLI does not write into the live tree:

```
$ grep -n "open(.*['\"]w|\.write(|os.replace|shutil\." corpus/tools/map_obligations.py
(no output)
```

No write-mode file opens, no `os.replace`, no `shutil` mutation calls — consistent with the C2 contract's "no live-tree writes" clause (`wave-spec.md:27`). The only filesystem write path is the isolated `TemporaryDirectory` in §7(a).

**mtime noise, explicitly discounted.** Many corpus files carry recent mtimes (e.g. `corpus/fixtures/r88-m3-maya-cluster/entities.json` → `2026-10-17 03:08:53`, `corpus/tools/support_check.py` → `2026-10-17 10:00:58`), which could look like tampering. Content comparison shows otherwise:

```
$ git diff --quiet 9c2eea3 -- <path> && echo IDENTICAL
IDENTICAL  corpus/fixtures/ally-one-way/entities.json
IDENTICAL  corpus/fixtures/r88-m3-maya-cluster/entities.json
IDENTICAL  corpus/tools/support_check.py
```

mtime differences here are checkout/sync artifacts of the merge commit `b8b50c8`, not content changes. Content hashes, not timestamps, are the evidence.

---

## Appendix — full path census (all 154 changed paths, bucketed)

Generated by classifying `git diff --name-only 9c2eea3..abbc3e0`. Bucket letters match §6. `X` (unbucketed) does not appear, which is the zero-unbucketed result stated in §6.

### Bucket A — new r94 fixture (10)

- `corpus/fixtures/r94-paired-crossing/README.md`
- `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md`
- `corpus/fixtures/r94-paired-crossing/contradictions.json`
- `corpus/fixtures/r94-paired-crossing/entities.json`
- `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md`
- `corpus/fixtures/r94-paired-crossing/inspiration-note.md`
- `corpus/fixtures/r94-paired-crossing/relations.json`
- `corpus/fixtures/r94-paired-crossing/source-excerpt.md`
- `corpus/fixtures/r94-paired-crossing/sources.json`
- `corpus/fixtures/r94-paired-crossing/timeline.json`

### Bucket B — new r94 tool + contract (2)

- `corpus/tools/map_obligations.py`
- `corpus/tools/map-obligations-contract.json`

### Bucket C — new r94 knowledge (1)

- `corpus/knowledge/r94-cross-myth-design-comparison.md`

### Bucket D — `.ufo/waves/round-94/` bookkeeping (139)

Round-level records:

- `.ufo/waves/round-94/wave-spec.md`
- `.ufo/waves/round-94/wave-spec.json`
- `.ufo/waves/round-94/work-receipt.json`
- `.ufo/waves/round-94/work-results.xml`

Frozen replay inputs:

- `.ufo/waves/round-94/frozen/map-obligations-r93/claim-excerpt-map.md`
- `.ufo/waves/round-94/frozen/map-obligations-r93/entities.json`
- `.ufo/waves/round-94/frozen/map-obligations-r93/relations.json`
- `.ufo/waves/round-94/frozen/map-obligations-r93/timeline.json`
- `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json`

Seat reports and artifacts:

- `.ufo/waves/round-94/work/W01.md`
- `.ufo/waves/round-94/work/W01-preservation.py`
- `.ufo/waves/round-94/work/W02.md`
- `.ufo/waves/round-94/work/W02-frozen-demo.py`
- `.ufo/waves/round-94/work/W02-unmapped-demo.py`
- `.ufo/waves/round-94/work/W03.md`
- `.ufo/waves/round-94/work/W04.md`
- `.ufo/waves/round-94/work/W04-baseline.json`
- `.ufo/waves/round-94/work/W05.md`
- `.ufo/waves/round-94/work/W05-build-baseline.py`
- `.ufo/waves/round-94/work/W05-baseline-corpus.sha256`
- `.ufo/waves/round-94/work/W06.md`
- `.ufo/waves/round-94/work/W07.md`
- `.ufo/waves/round-94/work/W07-gutenberg-check.py`
- `.ufo/waves/round-94/work/W08.md`
- `.ufo/waves/round-94/work/W09.md`
- `.ufo/waves/round-94/work/W09-replay.py`
- `.ufo/waves/round-94/work/W09-replay.out`
- `.ufo/waves/round-94/work/W10.md`
- `.ufo/waves/round-94/work/W11.md`
- `.ufo/waves/round-94/work/W12.md`
- `.ufo/waves/round-94/work/W13.md`
- `.ufo/waves/round-94/work/W13-inventory.py`
- `.ufo/waves/round-94/work/W13-source-controls.py`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/contradictions.json`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/control-excerpt.md`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/entities.json`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/relations.json`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/sources.json`
- `.ufo/waves/round-94/work/W13-source-controls/claim-valid-other/timeline.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/contradictions.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/control-excerpt.md`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/entities.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/relations.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/sources.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-unknown-id/timeline.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/contradictions.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/control-excerpt.md`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/entities.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/relations.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/sources.json`
- `.ufo/waves/round-94/work/W13-source-controls/first-appearance-valid-other/timeline.json`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/contradictions.json`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/control-excerpt.md`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/entities.json`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/relations.json`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/sources.json`
- `.ufo/waves/round-94/work/W13-source-controls/relation-valid-other/timeline.json`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/contradictions.json`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/control-excerpt.md`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/entities.json`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/relations.json`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/sources.json`
- `.ufo/waves/round-94/work/W13-source-controls/timeline-valid-other/timeline.json`
- `.ufo/waves/round-94/work/W14.md`
- `.ufo/waves/round-94/work/W14-replay.py`
- `.ufo/waves/round-94/work/W15.md`
- `.ufo/waves/round-94/work/W15-replay.py`
- `.ufo/waves/round-94/work/W15-replay.txt`
- `.ufo/waves/round-94/work/W15-fixture/.w15-owned`
- `.ufo/waves/round-94/work/W15-fixture/README.md`
- `.ufo/waves/round-94/work/W15-fixture/archive-record-excerpt.md`
- `.ufo/waves/round-94/work/W15-fixture/claim-excerpt-map.md`
- `.ufo/waves/round-94/work/W15-fixture/contradictions.json`
- `.ufo/waves/round-94/work/W15-fixture/entities.json`
- `.ufo/waves/round-94/work/W15-fixture/inspiration-note.md`
- `.ufo/waves/round-94/work/W15-fixture/kojiki-chamberlain-excerpt.md`
- `.ufo/waves/round-94/work/W15-fixture/relations.json`
- `.ufo/waves/round-94/work/W15-fixture/sources.json`
- `.ufo/waves/round-94/work/W15-fixture/symbolism-clause-map.md`
- `.ufo/waves/round-94/work/W15-fixture/timeline.json`
- `.ufo/waves/round-94/work/W16.md`
- `.ufo/waves/round-94/work/W16-scratch/cluster/escape.md`
- `.ufo/waves/round-94/work/W16-scratch/cluster/inside.md`
- `.ufo/waves/round-94/work/W16-scratch/map-absolute.md`
- `.ufo/waves/round-94/work/W16-scratch/map-local.md`
- `.ufo/waves/round-94/work/W16-scratch/map-symlink.md`
- `.ufo/waves/round-94/work/W16-scratch/map-traversal.md`
- `.ufo/waves/round-94/work/W16-scratch/outside.md`
- `.ufo/waves/round-94/work/W17.md`
- `.ufo/waves/round-94/work/W18.md`
- `.ufo/waves/round-94/work/W19.md`
- `.ufo/waves/round-94/work/W19-inventory.py`
- `.ufo/waves/round-94/work/W19-obligations.json`
- `.ufo/waves/round-94/work/W21.md`
- `.ufo/waves/round-94/work/W21-F14-postrepair-check.exit`
- `.ufo/waves/round-94/work/W21-F14-postrepair-check.out`
- `.ufo/waves/round-94/work/W21-F29-shonen-format-check.exit`
- `.ufo/waves/round-94/work/W21-F29-shonen-format-check.out`
- `.ufo/waves/round-94/work/W21-boundary-default.exit`
- `.ufo/waves/round-94/work/W21-boundary-default.out`
- `.ufo/waves/round-94/work/W21-boundary-self-test.exit`
- `.ufo/waves/round-94/work/W21-boundary-self-test.out`
- `.ufo/waves/round-94/work/W21-c9-checker-hash.exit`
- `.ufo/waves/round-94/work/W21-c9-checker-hash.out`
- `.ufo/waves/round-94/work/W21-c9-gate-census.exit`
- `.ufo/waves/round-94/work/W21-c9-gate-census.out`
- `.ufo/waves/round-94/work/W21-c9-gate3-source-scope.exit`
- `.ufo/waves/round-94/work/W21-c9-gate3-source-scope.out`
- `.ufo/waves/round-94/work/W21-c9-null-chain.exit`
- `.ufo/waves/round-94/work/W21-c9-null-chain.out`
- `.ufo/waves/round-94/work/W21-c9-tick-unresolved.exit`
- `.ufo/waves/round-94/work/W21-c9-tick-unresolved.out`
- `.ufo/waves/round-94/work/W21-discriminate-delivered.exit`
- `.ufo/waves/round-94/work/W21-discriminate-delivered.out`
- `.ufo/waves/round-94/work/W21-discriminate-e97613c.exit`
- `.ufo/waves/round-94/work/W21-discriminate-e97613c.out`
- `.ufo/waves/round-94/work/W21-discriminate-e97613c-short.exit`
- `.ufo/waves/round-94/work/W21-discriminate-e97613c-short.out`
- `.ufo/waves/round-94/work/W21-discriminate-isolated-default.exit`
- `.ufo/waves/round-94/work/W21-discriminate-isolated-default.out`
- `.ufo/waves/round-94/work/W22.md`
- `.ufo/waves/round-94/work/W22-replay.py`
- `.ufo/waves/round-94/work/W22-evidence.json`
- `.ufo/waves/round-94/work/W23.md`
- `.ufo/waves/round-94/work/W24.md`
- `.ufo/waves/round-94/work/W25.md`
- `.ufo/waves/round-94/work/W26.md`
- `.ufo/waves/round-94/work/W27.md`
- `.ufo/waves/round-94/work/W27-roster-validation.json`
- `.ufo/waves/round-94/work/W28.md`
- `.ufo/waves/round-94/work/W29.md`
- `.ufo/waves/round-94/work/W30.md`
- `.ufo/waves/round-94/work/W31.md`
- `.ufo/waves/round-94/work/W32.md`

### Bucket E — root append-only lane records (2)

- `LOG.md`
- `SCORECARD.md`

### Bucket X — unbucketed (0)

None.

---

## 8. Bottom line

**PASS** — `9c2eea3..abbc3e0` adds exactly the declared r94 surface (13 corpus additions: 10 new `r94-paired-crossing` fixture files, `map_obligations.py`, `map-obligations-contract.json`, `knowledge/r94-cross-myth-design-comparison.md`; 139 `.ufo/waves/round-94/` bookkeeping files) plus two provably append-only lane records (`LOG.md` +11/-0, `SCORECARD.md` +16/-0), with all 1767 pre-existing corpus blobs byte-identical, all five named protected checker files unchanged, and no modification to r88, r93, any prior knowledge doc, or any earlier round's wave directory; the only out-of-bucket artifacts are two untracked, non-committed byproducts — a self-cleaning `map-obligations-self-test-*` scratch dir created in the repo root by `--self-test` and gitignored `corpus/tools/__pycache__/` bytecode.
