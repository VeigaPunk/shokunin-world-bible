# V40 — census-replica-2 (round 99)

**Seat:** V40 `census-replica-2`. Scope: independent second census against the git archive of `4265df5` (expect 173 dirs on the delivered tree), cross-check V20.

**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). `git rev-parse HEAD` → `337f0fa52b02626b7687eedbb2d99fab30446fe4`. `git log --oneline 4265df5..HEAD`:

```
337f0fa lore r99: record blocked dispatch attempt (xai-oauth credential pool missing) — zero increment
111b9a3 lore r98: close round — SCORECARD admitted section
```

Those two commits touch `LOG.md` and `SCORECARD.md` only (baseline-attributable, not fixture bytes).

**Only files this seat writes:** this report plus scratch `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V40-scratch/` (`census_v40.py`, `receipts-4265df5.json`, `receipts-tree-r99-prelim.json`, `receipts-tree-r99-final1.json`, `receipts-tree-r99-final2.json`, `archive/` = extracted `git archive 4265df5` (307M — closer may drop it; r98 V37 precedent), `ls-tree.sorted`, `hash-object.sorted`, `dirs-base.txt`, `dirs-now.txt`, `files-base.txt`, `files-now.txt`, `r99-sha256.txt`, `poll.log`). No commits, no pushes, no network, no nested agents. All commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

## 1. Method (independent implementation)

Own script `census_v40.py` (written for this seat; not a copy of V17/V37 or of V20-scratch). For each directory directly under `<root>/corpus/fixtures/` (dot-dirs excluded), runs `python3 corpus/fixtures/check_bible.py corpus/fixtures/<d>` with cwd = root and a repo-relative argv, `PYTHONDONTWRITEBYTECODE=1`. Records exit code and sha256 of the combined stdout+stderr bytes exactly as captured (no stripping). Counts violation lines under two conventions (`line.startswith("- ")` and `"VIOLATION" in line`).

Both roots used the same checker bytes:

```
sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

Archive copy and `git show 4265df5:corpus/fixtures/check_bible.py | sha256sum` printed the same digest. `git hash-object corpus/fixtures/check_bible.py` = `git rev-parse 4265df5:corpus/fixtures/check_bible.py` = `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0`.

Archive extraction and fidelity:

```
$ git archive 4265df5 | tar -x -C .ufo/waves/round-99/seats/V40-scratch/archive
EXTRACT_OK
$ ls -d .../archive/corpus/fixtures/*/ | wc -l          # 172
$ find .../archive/corpus/fixtures -type f | wc -l     # 1030
$ git ls-tree -r 4265df5 -- corpus/fixtures | awk '{print $3" "$4}' | sort -k2 > ls-tree.sorted
LS_TREE_ROWS 1030
$ (cd archive && find corpus/fixtures -type f | sort | while read f; do
     printf '%s %s\n' "$(git hash-object "$f")" "$f"; done | sort -k2 > ../hash-object.sorted)
HASH_ROWS 1030
$ diff -q ls-tree.sorted hash-object.sorted            # exit 0
ARCHIVE_INTEGRITY_OK 1030/1030
```

## 2. Poll record (20 s cadence, 40 tries; never verify a plan)

Pre-loop sighting 22:01:27-03:00: fixture dir present (10 files; `sources.json` / `timeline.json` / `fictional-excerpts.md` mtime 22:01:13, the other seven still the 21:36 copy stamps), no `corpus/knowledge/r99*`, no `S*.md`, no `V20*.md`.

Numbered tries in `V40-scratch/poll.log` (`grep -c '^TRY ' poll.log` → 40). First and last:

| try | time (-03:00) | S reports | r99 knowledge | V20 report |
|---|---|---|---|---|
| 0 | 22:02:39 | S3 only | 0 | absent |
| 4 | 22:04:12 | S3, S4 | 0 | absent |
| 39 | 22:33:57 | S3, S4 | 0 | absent |

Tries 5–39 did not add a producer report, a knowledge file, or a V20 report. Recheck after the budget, 22:35:37 and again 22:38:24: still only `S3-fixture-author.md` (22:01:40, 5069 bytes) and `S4-fixture-docs.md` (22:03:54, 9303 bytes). `S1*.md`, `S2*.md`, `S5*.md`, and `corpus/knowledge/r99*` were **ABSENT**. `V20-preservation-census.md` was also absent at 22:38:24; it landed at 22:42:32 and is cross-checked in §4. That landing does not reopen the poll.

No stall-escape was used by this seat (the 40 tries ran in-process). No all-reports poll was issued, so the subtract-SELF convention was not exercised; recorded, not fatal. V20-scratch exists and its `poll.log` ends `EXHAUSTED ts=2026-10-17T22:28:51-0300` with the same S1/S2/S5 and notes absence; that is their log, not a seat report, and it was not used as a census source.

Fixture-owning producer reports (S3, S4) were on disk before every load-bearing tree run (final1 22:29:25, final2 22:35:37). S1's tool files were still moving during the early tries (`dependency_freeze.py` mtime 22:07:33, contract 22:08:46) and then stopped; `corpus/tools/README.md` and `SKILL.md` mtimes stayed at 21:32 / 21:34 (pre-wave). Those files are not `check_bible` inputs.

## 3. Census results

**Archive `4265df5`** (root = extracted archive), 22:02:34–22:02:39:

```json
{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134,
 "violation_lines_dash": 0, "violation_lines_word": 421, "non01": []}
```

Reproduces the r98 closure census 172/38/134/421 with zero non-0-1 exits. Smoke of the archive's own `r98-clerk-filing`: `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0.

**Delivered tree**, three runs, identical receipts (`prelim==final1: True`, `final1==final2: True`):

- prelim 22:05:07 (after S3+S4 reports; S1 tools not yet quiescent)
- final1 22:29:25 (after S1 tool mtimes had stopped at 22:08:46; S1/S2/S5 reports still absent)
- final2 22:35:37 (after poll budget)

```json
{"fixture_dirs": 173, "clean_exit0": 39, "negative_exit1": 134,
 "violation_lines_dash": 0, "violation_lines_word": 421, "non01": []}
```

**173 dirs / 39 clean / 134 negative / 421 violation lines / zero non-0-1 exits** — the declared 172→173 with +1 clean. Negative count and violation-line count unchanged.

Directory and file arithmetic (final2 window):

```
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l     # 173
$ git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l       # 172
$ find corpus/fixtures -type f ! -path '*/__pycache__/*' | wc -l   # 1040
$ git ls-tree -r --name-only 4265df5 corpus/fixtures | wc -l       # 1030
$ diff dirs-base.txt dirs-now.txt
# one added line: r99-window-lapse
$ diff files-base.txt files-now.txt
# ten added lines, all under corpus/fixtures/r99-window-lapse/, no '<' lines
```

**Delta vs archive** (per-dir receipt = exit + combined-output sha256), final2 vs archive receipts:

```
new dirs: ['corpus/fixtures/r99-window-lapse']
removed dirs: []
inherited count: 172 | changed tuples: 0
r99 receipt: {"exit": 0, "sha256": "afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e",
              "dash_lines": 0, "violation_word_lines": 0}
```

Direct re-run:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0
stdout b'CLEAN: schema, citations, relations, timeline; 0 violations\n'
stderr b''
combined sha256 afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e
stripped-stdout sha256 d9bdf82d2b0cddb2a60734ad10dc69beb75e085f5fb4b13a007c6ec43ac8606b
```

All 39 exit-0 dirs share that one combined sha256. The CLEAN line is identical and stderr is empty, so the receipt does not uniquely identify `r99-window-lapse`; uniqueness is the directory delta, not the hash.

Convention note: only the `"VIOLATION"`-substring convention yields 421; the `"- "`-prefix convention yields 0 on every dir. Same split as the r94–r98 census. This replica uses the substring count.

**Inherited fixture bytes vs the archive** (sha256 of every archive `corpus/fixtures` file against the worktree, run ~22:19, after S1's last tool write): `compared=1030 missing=0 mismatched=0`. Corroborated at 22:35:37 by `git diff --name-status 4265df5`, which lists no `corpus/fixtures` path:

```
M	LOG.md
M	SCORECARD.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py
```

`git ls-files --others --exclude-standard | grep -v '^\.ufo/'` lists exactly the ten `corpus/fixtures/r99-window-lapse/` files. No extra fixture dir, no deleted fixture file.

**New-dir inventory** (JSON array lengths, not a semantic reading): entities 6, relations 1, sources 8, timeline 8, contradictions 0. That is the declared 6/1/8 table shape. `check_bible` CLEAN is structural only.

**Byte compare of the ten new files vs archive `r98-clerk-filing`** (final2, 22:35):

```
DIFFERS  README.md               b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
DIFFERS  claim-excerpt-map.md    d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d
SAME     contradictions.json     37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
SAME     entities.json           db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
DIFFERS  fictional-excerpts.md   fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d
SAME     inspiration-note.md     58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
SAME     relations.json          c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
SAME     source-excerpt.md       b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
DIFFERS  sources.json            8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15
DIFFERS  timeline.json           2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069
```

Five differ, five match. S4's report declares map `d2fe20e5…` and README `b9320941…`; both match these hashes exactly. S3's report does not publish sha256s. An earlier compare at 22:02 (before S4's rewrites; README mtime later 22:03:19, map mtime 22:02:39) had README and claim-excerpt-map still SAME as r98, which matches S3's statement that those two were left as byte copies for S4. The final2 table above is the delivered state.

Fixture mtimes were unchanged from try 6 (22:04:52) through final2 (22:35:37).

## 4. Cross-check V20

Absent through the poll budget and the 22:38:24 recheck. The report then landed: `V20-preservation-census.md`, mtime 22:42:32-03:00, 7979 bytes. Read in full at 22:44 (141 lines, ends with their ABSENT line). Scratch was not used as their verdict; the cross-check is against that file only. No census number in §§1–3 was taken from them.

V20's own bottom line is that the preservation census was **not taken** (S1/S2/S5 and both knowledge notes absent at their try 40, 22:28:51). They say the full `census.py` (all dirs, including r99) was not run, and they publish no 173/39 figure. Overlap with this seat, compared, not copied:

| figure | V40 (this seat) | V20 report |
|---|---|---|
| fixture dirs | 173 (checker + find) | 173 on every poll try (`find`; not a checker census) |
| inherited / archive checker | archive 172/38/134/421; tree inherited tuples unchanged (172 compared, 0 changed) | null-control excluding r99: `{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}` |
| full-tree checker | 173/39/134/421, zero non-0-1 | not run (their §4) |
| `git diff --name-status 4265df5` | LOG, SCORECARD, freeze py, freeze contract | same four paths |
| HEAD | `337f0fa52b02626b7687eedbb2d99fab30446fe4` | same |
| SKILL.md / tools README vs archive | `cmp` at 22:44: `SKILL_IDENTICAL`, `TOOLS_README_IDENTICAL` | `SKILL_IDENTICAL`, `TOOLS_README_IDENTICAL` |

No contradiction on any figure both seats published. The +1 clean (38→39) is this seat's measurement; V20 did not replicate it. Their poll `dirs=173` agrees with the directory half of the claim only.

## 5. Bounds

- `check_bible` is structural/lexical. CLEAN means schema, citations, relations, and timeline checks pass. It does not prove the lapse prose, the 21 map obligations, or C1 freeze behavior. Those are other seats.
- S1, S2, and S5 reports, and both r99 knowledge files, were ABSENT at poll exhaustion and still absent when V20's report was read. They are outside the fixture census inputs. S1 did modify the two freeze-tool files (visible in `git diff`); that does not move a `check_bible` receipt, and the three tree runs agree.
- The load-bearing reading is final1/final2 (identical), both after fixture mtimes had been stable since 22:03:19 and after S3/S4 reports had landed. The prelim run matched them but was taken while S1's tools were still being written; it is corroboration, not the sole reading.
- The archive census uses the archive's `4265df5` `check_bible.py`; the tree census uses the worktree copy. Content-identical (`ff9fd2aa…`).
- Scratch `archive/` is 307M. Disclosed so a closer can drop it; not deleted here, so the integrity check stays reproducible until closure.
- V20 refused a full-tree checker census on protocol grounds. Agreement is on the overlapping figures only. That is a bound on the cross-check, not a contradiction.

## Bottom line

**PASS** — independent census (own script, both roots): archive `4265df5` = 172/38/134/421 and delivered tree = **173/39/134/421**, zero non-0-1 exits, delta exactly +1 dir (`r99-window-lapse`, exit 0) / 0 removed / 0 changed inherited tuples, archive integrity 1030/1030, three identical tree runs. V20's report (landed 22:42:32, after this seat's 40-try budget) agrees on dir count 173, on the inherited 172/38/134/421 null-control, and on the `4265df5` diff set, and contradicts nothing; they did not run the full-tree checker census, so the +1 clean is not co-signed.
