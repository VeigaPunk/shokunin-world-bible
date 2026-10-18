# V70 — census-3 (round 99)

**Seat:** V70 `census-3`. Third independent census, different tool from the python-census replicas: a shell loop over every `corpus/fixtures/*/` directory, plus a SHA-256 comparison of a deterministic 10% sample of inherited fixture files.

**Report path (only non-scratch file this seat writes):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V70-census-3.md`

**Scratch:** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V70-scratch/` (`census.sh`, `sha-sample.sh`, `poll.sh`, `poll.log`, `archive/` = `git archive 4265df5 corpus/fixtures`, `receipts-archive-4265df5.tsv`, `receipts-archive-rel.tsv`, `receipts-worktree-prelim.tsv`, `receipts-worktree-mid.tsv`, `receipts-worktree-final.tsv`, `inherited-files.txt`, `sample-10pct.txt`, `sha-sample.tsv`, `sha-sample-early.tsv`, `ls-tree.sorted`, `hash-object.sorted`). No commits, no pushes, no network, no nested agents. No corpus bytes written.

**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree `HEAD` at every check in this seat was `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`lore r99: record blocked dispatch attempt … zero increment`). `4265df5` is an ancestor of `HEAD`. `git diff --stat 4265df5 HEAD` is only `LOG.md` (+91) and `SCORECARD.md` (+32). Fixture bytes at `HEAD` therefore equal fixture bytes at `4265df5` for every tracked path. Wave additions are uncommitted.

**Claim under this seat:** census 172→173 (fixture directories). Declared companion shape 6/1/8 is inventoried below as a property of the new directory, not as a map-obligation verdict. This seat did not run `map_obligations` and does not claim the 21-row figure.

## 1. Method

Shell loop (`census.sh`), `LC_ALL=C`, `PYTHONDONTWRITEBYTECODE=1`, cwd = lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` unless noted. For each immediate child directory of `corpus/fixtures` (glob `corpus/fixtures/*/`, which matched `find -mindepth 1 -maxdepth 1 -type d`; zero dot-directories):

```sh
out=$(python3 corpus/fixtures/check_bible.py "${d%/}" 2>&1); rc=$?
n=$(printf '%s\n' "$out" | grep -c 'VIOLATION' || true)
hash=$(printf '%s\n' "$out" | sha256sum | awk '{print $1}')
```

Violation lines are the `VIOLATION` substring count (the r94–r98 convention). The summary line `N violation(s)` is lowercase and is not counted. Receipt hash is SHA-256 of combined stdout+stderr with command-substitution trailing-newline normalization (`printf '%s\n'`). Argv is repo-relative `corpus/fixtures/<name>`. That matters: an earlier archive pass that passed scratch-absolute paths embedded those paths in five missing-file diagnostics and produced false hash mismatches (see §4).

10% inherited sample (`sha-sample.sh`): `git ls-tree -r --name-only 4265df5 -- corpus/fixtures | LC_ALL=C sort`, keep 1-based lines with `NR % 10 == 0`. Compare `sha256sum <(git show 4265df5:$f)` to `sha256sum $f`. This is a sample, not a full-tree proof. A full `git diff --name-status 4265df5 -- corpus/fixtures` was run as additional corroboration and is labeled as such.

## 2. Poll-wait (20 s cadence, 40 tries; never verify a plan)

Watched producer reports `S1-*.md` … `S5-*.md`, `corpus/fixtures/r99-window-lapse/` file count, and the two S5 knowledge paths. Log: `V70-scratch/poll.log`.

| try | UTC | S1 | S2 | S3 | S4 | S5 | r99 files | knowledge notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-18T01:05:56Z | 0 | 0 | 1 | 1 | 0 | 10 | absent |
| 30 | 2026-10-18T01:15:36Z | 0 | 0 | 1 | 1 | 0 | 10 | absent |
| 31 | 2026-10-18T01:30:18Z | 0 | 0 | 1 | 1 | 0 | 10 | absent |
| 40 | 2026-10-18T01:33:18Z | 0 | 0 | 1 | 1 | 0 | 10 | absent |

`EXHAUSTED try=40 ts=2026-10-18T01:33:18Z`.

**Stall-escape (recorded, not fatal):** the first poll process (pid 1722687) was killed by the 600 s background cap after try 30, during the sleep before try 31. `ps -p 1722687` then reported the pid dead. Tries 31–40 were resumed in a second process and reached the 40-try cap. No all-reports poll was used, so the subtract-SELF convention was not exercised.

**Present at exhaustion (census inputs):** `S3-fixture-author.md` (mtime 22:01 -03) and `S4-fixture-docs.md` (mtime 22:03 -03). The new fixture had all ten files before try 1. S4's `README.md` / `claim-excerpt-map.md` mtimes are 22:02:39 / 22:03:19, before the first census (01:10:24Z = 22:10 -03). `check_bible` does not read those Markdown files.

**ABSENT at exhaustion, and still absent at the load-bearing snapshot 2026-10-18T01:40:45Z:** `S1-*.md`, `S2-*.md`, `S5-*.md`, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`. S1 had an in-flight worktree edit (`M corpus/tools/dependency_freeze.py`, `M corpus/tools/dependency-freeze-contract.json`) and a scratch mirror, but no report. Those paths are outside the census. `check_bible.py` was not among them.

The census artifact is not a plan: the directory is on disk and both seats that own its files had reported. The load-bearing reading is of that tree, not of the absent knowledge notes.

## 3. Baseline archive census

```sh
git archive 4265df5 corpus/fixtures | tar -x -C .../V70-scratch/archive
# integrity: git hash-object of each extracted file vs git ls-tree -r 4265df5
ARCHIVE_DIRS=172
ARCHIVE_FILES=1030
ARCHIVE_INTEGRITY_OK 1030 files
```

`diff -q ls-tree.sorted hash-object.sorted` was empty (1030/1030 blobs).

Repo-relative re-census, cwd = the extracted archive, same shell loop, archived `check_bible.py`:

```
ARCHIVE_REL_CENSUS dirs=172 clean=38 negative=134 violation_lines=421 non01=0
```

Saved `receipts-archive-rel.tsv` summarizes to `rows=172 exit0=38 exit1=134 other=0 viol=421`. That is the r98 closure tuple 172/38/134/421. Checker pin, worktree and `git show 4265df5:corpus/fixtures/check_bible.py`:

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

Same pin the r98 census seats recorded. `git diff --stat 4265df5 -- corpus/fixtures/check_bible.py` was empty.

## 4. Path-embedding control (not a finding)

First archive pass passed scratch-absolute argv. Five directories (`r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-{control,empty,whitespace}`) kept the same exit and violation count but differed in receipt hash, because the diagnostic embeds the path:

```
VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V70-scratch/archive/corpus/fixtures/r5-missing-file/contradictions.json'
```

Both exited 1. After the repo-relative re-run, inherited receipt equality against the worktree final TSV was `inherited_equal=172 changed=[]`. Those five hash gaps are a method artifact, not fixture drift.

## 5. Delivered-tree census

Directory accounting at the final snapshot:

```
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l    # 173
git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l      # 172
find corpus/fixtures -type f | wc -l                            # 1040
git ls-tree -r --name-only 4265df5 corpus/fixtures | wc -l      # 1030
find corpus/fixtures/r99-window-lapse -type f | wc -l           # 10
```

`diff` of sorted directory names, archive vs worktree, is one added line: `r99-window-lapse`. No removals.

Three shell-loop runs, identical receipts (`cmp` prelim==mid and mid==final):

| run | UTC | result |
|---|---|---|
| prelim | 2026-10-18T01:10:24Z | `CENSUS dirs=173 clean=39 negative=134 violation_lines=421 non01=0` |
| mid | 2026-10-18T01:20:32Z | same; `RECEIPTS_IDENTICAL` vs prelim |
| final (load-bearing) | 2026-10-18T01:35:33Z | same; `MID_EQ_FINAL` |

Final TSV summary: `rows=173 exit0=39 exit1=134 other=0 viol=421`.

Delta versus the repo-relative archive receipts: 172/172 inherited tuples equal (exit, violation count, output hash); one extra directory.

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
rc=0
```

Combined-stream / stdout SHA-256 of that run: `afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e` (stderr empty; matches the r98 clean combined-stream hash, because the CLEAN line is the same text). Stripped line without the trailing newline:

```
printf '%s' 'CLEAN: schema, citations, relations, timeline; 0 violations' | sha256sum
d9bdf82d2b0cddb2a60734ad10dc69beb75e085f5fb4b13a007c6ec43ac8606b
```

That is the r98 stripped-stdout receipt for a clean fixture. The new directory contributes 0 violation lines. Null control: the 172 inherited directories still sum to 38/134/421.

`find corpus/fixtures -name '__pycache__' -o -name '*.pyc'` printed nothing after the runs.

**Inventory of the new directory** (JSON array lengths, final snapshot; not a map-obligation count):

```
entities.json 6
relations.json 1
timeline.json 8
sources.json 8
contradictions.json 0
```

That is the declared 6/1/8 shape plus 8 sources. Twenty-one map rows were not measured here.

## 6. SHA-256 of the 10% inherited sample

```
INHERITED_FILES=1030 SAMPLE_10PCT=103
SAMPLE_OK=103 SAMPLE_MISMATCH=0 SAMPLE_MISSING=0
```

Selection check: 1030 / 10 = 103, and `grep -c '^MATCH'` on `sha-sample.tsv` is 103, `^MISMATCH` 0, `^MISSING` 0. Extensions in the sample: 89 json, 14 md. First path `corpus/fixtures/ally-reciprocal/sources.json`; last three are the timeline tables of `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`. The sample cannot include `r99-window-lapse` (not in `4265df5`).

Manual one-file replay:

```
FILE=corpus/fixtures/ally-reciprocal/sources.json
git show: ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1
worktree: ded882756d6cfaf4bb7f542e27c0030b0af10312a25b89301636cacedd4214d1
```

Early sample (01:10Z, before the final run) and the final sample are byte-identical (`SHA_SAMPLE_STABLE`).

**Additional full-tree corroboration, not a substitute for the sample:**

```
git diff --name-status 4265df5 -- corpus/fixtures
# empty, exit 0
git ls-files --others --exclude-standard -- corpus/fixtures
# exactly the 10 r99-window-lapse files
```

So the other 90% of inherited fixture paths are also unmodified on this snapshot. The 10% sample did not miss a change that `git diff` could see.

## 7. What this does not show

- `CLEAN` is structural/lexical (`schema, citations, relations, timeline`). It is not a prose, canon, or blame-absence proof.
- S1/S2/S5 reports and both r99 knowledge notes were **ABSENT** after 40 tries. C1 (freeze pinning) and C2 component 2 (blind-spot table) are outside this seat and were not verified. S1's unreported tool edits were present in the worktree and do not touch `check_bible.py` or `corpus/fixtures`.
- No other census-seat report existed under `.ufo/waves/round-99/seats/` at 01:40:45Z, so there is no cross-seat number to agree or disagree with. This census stands alone.
- Out of census scope, observed not authored: untracked `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md` (4208 bytes, mtime 2026-10-17 22:32:40 -03). Not a fixture path. Not opened.
- The snapshot is the post-S3/S4 fixture tree. A later producer write to `corpus/fixtures` after 01:40:45Z would be a new revision this seat did not re-read. Three runs from 01:10Z to 01:35Z were identical, and the directory count was still 173 at 01:40:45Z.

## Bottom line

**PASS** — shell-loop census: baseline archive `4265df5` = 172/38/134/421 (integrity 1030/1030) and delivered tree = **173/39/134/421**, zero non-0/1 exits; delta is exactly `r99-window-lapse` (exit 0, 0 violation lines, JSON lengths 6/1/8/8/0) with 172/172 inherited receipts unchanged; 10% inherited SHA sample 103/103 match, and `git diff --name-status 4265df5 -- corpus/fixtures` is empty. S1/S2/S5 reports and the r99 knowledge notes were ABSENT at poll exhaustion; they are not inputs to this census.
