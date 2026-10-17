# V34 — census-replica-2 (round 95)

Seat: V34 `census-replica-2`. Scope per seat spec: after producers finish, run an
**independent second census** with a **fresh script** comparing `corpus/fixtures`
against a `git archive` of `fb118c4`; expect **169** dirs; enumerate new paths;
require **0 unexpected inherited changes**; cross-check V15's numbers and explain
any disagreement.

Baseline: HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (r94 closure `fb118c4`),
all round writes present but uncommitted. All commands run from repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Writes: this report
plus my declared seat scratch `.ufo/waves/round-95/seats/V34-scratch/`
(`census_r95.py`, `census-baseline.json`, `census-snap2.json`, `census-final.json`,
`census-final2.json`, `census-corpus-final.json`). No commits, no pushes, no
network, no nested agents, no other file touched.

## 0. Method (fresh implementation, deliberately not V15's)

`.ufo/waves/round-95/seats/V34-scratch/census_r95.py` (written by this seat, ~130
lines, stdlib only): `git archive --format=tar <ref> <root>` → extract to a
`tempfile.TemporaryDirectory` → walk both trees → SHA-256 every file on both sides
→ classify `inherited/modified/deleted/new`; top-level dir lists via `os.listdir`,
all-dir lists via `os.walk`; expected-dir count and an `--allow-new` prefix set are
the pass conditions. V15 used `git ls-tree` + `git hash-object` (SHA-1, git-native);
this seat uses tar materialization + SHA-256 of file bytes. The two share no code,
so agreement is real corroboration.

**Method pre-validation on the untouched baseline** (before trusting the script for
the verdict — run at the start of the round, while producers were still writing):

```
$ python3 .ufo/waves/round-95/seats/V34-scratch/census_r95.py --ref fb118c4 --expected-dirs 168
{ "ref": "fb118c4", "work_head": "fb118c42038ed27a747eec704b9aab41bb4b2ebe",
  "baseline_top_dirs": 168, "work_top_dirs": 168, "baseline_files": 990, "work_files": 990,
  "modified_inherited": [], "deleted_inherited": [], "new_files": [], "verdict": "PASS" }
CENSUS PASS: dirs=168 files=990 modified=0 deleted=0 new=0
```

So the script independently reproduces the r94 closure numbers (168 dirs, 990
fixture files) with an empty diff — a null control for the post-producer run.

## 1. Poll-wait for producer artifacts

20 s cadence; watched `corpus/fixtures/r95-crossing-aftermath/` + `README.md` +
`claim-excerpt-map.md` + the five `P*.md` reports. Observed: fixture dir appeared
between tries 1–3 (empty); P3/P4 reports at ~16:21; P5 at ~16:24; P1 at ~16:26;
P2 (the last) at ~16:28. Two later polls (20 s × 12) confirmed all five producer
reports on disk before I froze my snapshot. Nothing in this seat's scope was ABSENT.

**Final snapshot: 2026-10-17T16:31:57–16:32:07-03:00**, taken after P1's last tool
write (16:26:27) and P2's last contract/README write (16:27:05); tool hashes at
census time (identical to V15's §5 and V45's final hashes):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

## 2. Census — 169 dirs, +10 files, 0 inherited changes (primary receipt)

```
$ python3 .ufo/waves/round-95/seats/V34-scratch/census_r95.py --ref fb118c4 \
    --expected-dirs 169 --allow-new r95-crossing-aftermath
{ "baseline_top_dirs": 168, "work_top_dirs": 169,
  "baseline_all_dirs": 168, "work_all_dirs": 169,
  "baseline_files": 990, "work_files": 1000, "inherited_files": 990,
  "modified_inherited": [], "deleted_inherited": [],
  "new_top_dirs": ["r95-crossing-aftermath"], "gone_top_dirs": [],
  "unexpected_new_files": [], "unexpected_new_dirs": [],
  "verdict": "PASS", "reasons": [] }
CENSUS PASS: dirs=169 files=1000 modified=0 deleted=0 new=10
```

New paths (all 10, exactly the declared C2 tree; `corpus/fixtures` has no nested
subdirectories — `all_dirs` == `top_dirs` on both sides, so the "+1 dir" is the
whole directory delta):

```
r95-crossing-aftermath/{README.md, claim-excerpt-map.md, contradictions.json,
entities.json, fictional-excerpts.md, inspiration-note.md, relations.json,
source-excerpt.md, sources.json, timeline.json}
```

Run repeated at 16:32:07 (`census-final2.json`): byte-identical result — 169/1000/
0/0/10. An earlier mid-round snapshot (16:2x, `census-snap2.json`) already showed
169/1000/0/0/10, so the fixture tree was stable across ≥3 snapshots.

**Second, independent method for the same claim** (git-native, no script):

```
$ git diff --name-status fb118c4 -- corpus/fixtures
(no output)
```

No tracked fixture path was added, deleted, modified or mode-changed.

## 3. Corpus-wide / repo-wide sweep (scope widening, for "0 unexpected changes")

`census_r95.py --root corpus` (filesystem SHA-256 over all 1780 inherited `corpus/`
paths):

```
modified: ['tools/README.md', 'tools/map-obligations-contract.json', 'tools/map_obligations.py']
deleted: []
new_files: ['fixtures/r95-crossing-aftermath/<10 files>', 'knowledge/r95-aftermath-scope-note.md',
            'tools/__pycache__/{boundary_doc_check,map_obligations,support_check}.cpython-314.pyc']
files baseline=1780 work=1794
```

Tracked+untracked view (excludes the ignored `.pyc` rows):

```
$ git diff --name-status fb118c4 -- . ':!.ufo'
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
$ git ls-files --others --exclude-standard | grep -v '^\.ufo/'
corpus/fixtures/r95-crossing-aftermath/… (10 files)
corpus/knowledge/r95-aftermath-scope-note.md
$ git check-ignore -v corpus/tools/__pycache__/map_obligations.cpython-314.pyc
.gitignore:2:__pycache__/	corpus/tools/__pycache__/map_obligations.cpython-314.pyc
```

Verdict: the inherited change set is exactly the declared producer-owned set
(`map_obligations.py`, `map-obligations-contract.json`, `README.md` — P1/P2) plus
the new fixture tree (P3/P4) and the new knowledge note (P5); `LOG.md` is the
additive r95 declaration (outside producer ownership, as V15 §6.4 also notes). The
3 `__pycache__/*.pyc` rows my filesystem walk lists are gitignored build artifacts
of the tools (not authored content, not under `corpus/fixtures`, never seen by a
git-based census) — classified, not a change.

## 4. Preservation of the new fixture (independent byte check)

```
$ sha256sum corpus/fixtures/r95-crossing-aftermath/* | sort -k2
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
```

Own comparison against `corpus/fixtures/r94-paired-crossing/`:

```
entities.json IDENTICAL   relations.json IDENTICAL   contradictions.json IDENTICAL
inspiration-note.md IDENTICAL   source-excerpt.md IDENTICAL
fictional-excerpts.md r94 bytes=1116 r95 bytes=1845 strict-prefix=True
```

Five declared byte copies are byte-identical; the three declared edits are
`sources.json` / `timeline.json` / `fictional-excerpts.md` (the last a strict
append). These hashes match V15 §5 and P3's report exactly.

## 5. W05 pin re-check (independent reproduction of V15's F-V15-3)

```
$ sha256sum -c .ufo/waves/round-94/work/W05-baseline-corpus.sha256
corpus/fixtures/README.md: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
# 983 OK / 1 FAILED / 0 missing, 984 rows total
$ sha256sum corpus/fixtures/README.md
01161b047f318c24e7c5e3ab0e763a07c6c90d97566dffc84682c46659651d91
$ git show fb118c4:corpus/fixtures/README.md | sha256sum
01161b047f318c24e7c5e3ab0e763a07c6c90d97566dffc84682c46659651d91
$ git log --oneline -3 -- corpus/fixtures/README.md
ac69044 lore r94: land admission conditions C-1..C-4,C-6 …
```

Pin row 1 is `a13d1af36aed…`; working tree equals the `fb118c4` blob, and the last
writer is the r94 commit `ac69044` → the single broken pin row is **pre-existing at
the r95 baseline**, not an r95 write. Independently reproduced: same row, same
classification.

Unpinned coverage, computed by set difference of the current fixture file list
against the pin (984 rows):

```
fixture files now: 1000  pin rows: 984  unpinned count: 20
unpinned by fixture dir: {'r94-paired-crossing': 10, 'r95-crossing-aftermath': 10}
```

So 980 pinned fixture rows + 20 unpinned (r94's and r95's trees) = 1000, matching
V15's arithmetic exactly.

## 6. Cross-check against V15 (`V15-preservation-census.md`) — full agreement

| Quantity | V15 | V34 (this seat) | Agree |
|---|---|---|---|
| top-level fixture dirs now / baseline | 169 / 168 | 169 / 168 | yes |
| fixture files now / baseline | 1000 / 990 | 1000 / 990 | yes |
| dir delta | +1 (`r95-crossing-aftermath`), 0 removed | same | yes |
| inherited changes in `corpus/fixtures` | 0 | 0 | yes |
| inherited changes in `corpus/` | 3 tool files | 3 tool files (same names) | yes |
| new paths outside `.ufo/` | 10 fixture files + 1 knowledge note | same | yes |
| repo-wide tracked change outside producer set | `LOG.md` (additive) | `LOG.md` (only other tracked change) | yes |
| 5 byte copies identical / 3 declared edits | yes | yes (own hashes) | yes |
| `fictional-excerpts.md` r94-preserved | lines 1–20 preserved, append 21–31 | r94 bytes = strict prefix (1116→1845) | yes |
| pin: rows / OK / FAILED | 984 / 983 / 1 (`corpus/fixtures/README.md`, pre-existing) | 984 / 983 / 1 (same, own run) | yes |
| unpinned fixture files | 20 = r94 (10) + r95 (10) | 20 = r94 (10) + r95 (10) | yes |
| tool hashes at snapshot | `d1c239cc…`, `8173bb97…`, `5d033c9d…` | identical | yes |

**Disagreements: none numerically.** Two presentational differences, both explained:

1. **`__pycache__` rows.** My raw filesystem walk over `corpus/` lists three
   `corpus/tools/__pycache__/*.cpython-314.pyc` as new paths; V15's git-native
   enumeration never sees them because `.gitignore:2` ignores `__pycache__/`
   (verified with `git check-ignore -v`). Not a corpus change; no bearing on either
   verdict. (V15's §6.2 also flags transient repo-root
   `map-obligations-self-test-<rand>/` dirs; I independently sighted one such dir
   (`map-obligations-self-test-40xls0_8/`) in `git status` at ~16:18 and it was gone
   on the next poll — same time-bounded artifact, corroborated.)
2. **Hash algorithm/plumbing.** V15 uses SHA-1 blob hashes via
   `git hash-object`; I use SHA-256 over file bytes on a materialized
   `git archive`. Same verdicts on every path, which is the point of a replica.

Independent corroboration of the same numbers also exists from other seats at the
same revision (V45 §fixture hashes, V20's pre/post check_bible census JSONs, P3's
before/after table) — no seat's count disagrees with 169/1000/0-inherited-changes.

## 7. Findings summary

| # | Finding | Class |
|---|---|---|
| F-V34-1 | Fresh-script census: 169 dirs / 1000 files, +10 files all under `r95-crossing-aftermath`, 0 modified, 0 deleted inherited, 0 unexpected new paths | PASS |
| F-V34-2 | Second method (`git diff --name-status fb118c4 -- corpus/fixtures`) empty → no tracked fixture change | PASS |
| F-V34-3 | Corpus-wide inherited change set == declared producer set; `LOG.md` the only other tracked change; nothing else anywhere | PASS |
| F-V34-4 | 5 byte copies byte-identical to r94; 3 declared edits as specified; `fictional-excerpts.md` strict r94 prefix | PASS |
| F-V34-5 | W05 pin: 1 broken row `corpus/fixtures/README.md`, pre-existing at baseline (last writer r94 `ac69044`), reproduced independently | finding (inherited; owner: closure / re-pin) |
| F-V34-6 | `corpus/tools/__pycache__/*.pyc` present as gitignored build residue; transient `map-obligations-self-test-*` dirs at repo root during concurrent runs (hygiene, not pollution at rest) | methodology note |
| F-V34-7 | V15's census numbers reproduced with an independent implementation; no disagreement to explain | PASS |

Bottom line: **PASS** — independent fresh-script census confirms 169 fixture dirs
(baseline 168) and 1000 files (baseline 990) with exactly the 10 declared new files
under `corpus/fixtures/r95-crossing-aftermath/`, zero modified/deleted inherited
paths under `corpus/fixtures/` and zero unexpected inherited changes anywhere in
`corpus/`; every V15 number was reproduced, the only difference being gitignored
`__pycache__` rows my filesystem walk sees and a git-native census does not, and
V15's single broken-pin finding (`corpus/fixtures/README.md`, pre-existing at
baseline) was independently reproduced.
