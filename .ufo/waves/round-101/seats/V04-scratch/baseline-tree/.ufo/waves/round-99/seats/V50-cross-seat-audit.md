# V50 — cross-seat-audit (round 99)

**Seat:** V50 cross-seat-audit (verifier, single-wave round-99 swarm, lore-shokunin lane).
**Scope (verbatim):** *Re-run 8 load-bearing quoted outputs from other seats (2 tamper, 2 table rows, 2 chain, 1 census, 1 support); REPRODUCED/MISMATCHED.*
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. Session cwd is the parent repo. Every write used an absolute path under the lane. Commands from the lane root with `python3`.
**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD during the round: `337f0fa`.
**Writes of this seat:** this report and `.ufo/waves/round-99/seats/V50-scratch/**` only. No commits, no pushes, no network, no nested agents, no `--freeze` on the live tree. Tamper and table-row probes ran in scratch mirrors.

**STATUS: FINAL — chain, census, support, and both table rows reproduced; the two pre-edit tamper lines are exact on tool `6f81f8be` and suffix-MISMATCHED on live tool `fb9bb9ff`.**

## 0. Revision binding

Two freeze-tool revisions matter. Verifier quotes from V94 / V108 / V115 were taken against `6f81f8be…`. S1 then changed one detail string. The live tool at every re-run below is the later bytes.

```
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  dependency_freeze.py  (V94 mirror; 29104 bytes; the tool those tamper seats quoted)
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  dependency_freeze.py  (live, mtime 22:38:11, 29110 bytes; unchanged through 22:53 and the later row replay)
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  dependency-freeze-contract.json (25987 bytes, mtime 22:08:46; unchanged by every verify)
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

The only live-vs-quoted tool diff is the `DIGEST-MISMATCH` tail clause (`dependency_freeze.py` around the digest emit):

```
- "fixture bytes changed outside the frozen inventory"
+ "pinned-file bytes changed outside the semantic inventory"
```

S1's report (`S1-full-file-pins.md`, mtime 22:48:57) says the self-test was re-run after that edit and still printed `SELF-TEST 18/18`. That matches what I observed.

## 1. Poll-wait record

Protocol: artifacts and producer reports, 20 s cadence, 40 tries, then ABSENT. Never verified a plan. Poller: `.ufo/waves/round-99/seats/V50-scratch/poll.sh`. An earlier 300 s poller was killed and restarted so the 40-try loop could finish; that restart is recorded, not a second budget.

```
try 1  22:04:15 reports=4 producers=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
try 40 22:17:15 reports=14 producers=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
TIMEOUT after 40
```

S3 report was already present at the first look (22:01:40). S4 landed at 22:03:54. Placeholder hazard, recorded by S3/S4/V13 and not treated as delivery: at 22:01 the r99 directory existed with r98-sized README and map.

Bounded stall-escape (8 extra tries, logged in `V50-scratch/stall-escape.log`, not a new 40): exhausted ~22:20. Still no S1/S2/S5 and no knowledge files.

Post-cap arrivals, recorded, not a fresh poll budget:

- 22:48:57 `S1-full-file-pins.md` appeared. Read. Delete-file quote and `--self-test` re-run against the live tool.
- 22:57:50 both knowledge files appeared (`r99-gate-blind-spot-table.md` 20526 bytes, `r99-lapse-scope-note.md` 14990 bytes). `S5*.md` was still absent at the row replay (~23:05) and at this write. S2's report was still absent. `corpus/tools/README.md` and `SKILL.md` mtimes stayed 21:32 / 21:34 (pre-wave).

ENDGAME: this seat did not run an all-reports poll of the other 127 seats, so SELF subtraction did not apply. The producer poll did not count V50.

## 2. Audit items

### T1 — V94 pair A, two-file tamper names both files — **REPRODUCED on the quoted tool; live-tool suffix MISMATCHED**

Quoted by **V94** (`V94-c1-two-mutation.md`, pair A). Mutation recovered from V94's scratch mirror versus the live r98 files: `entities.json` gains one trailing newline; `fictional-excerpts.md` gains `\n<!-- v94-json-then-md -->\n`. V94's quoted line:

```
FINDING DIGEST-MISMATCH: content digest 9d89ba3f8e19d34394575a782b8a69c38e7a4ee94b823c0cd8912bafe05416ad != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> 457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3), fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> c62880b9beab277b88dfa2321eef5fd4663b256b8189e9a1568d3cd824842c3c); fixture bytes changed outside the frozen inventory
RESULT ERROR
exit: 2
```

My re-run, scratch mirror, tool bytes copied from V94's mirror (`6f81f8be…`), contract copied from the live contract, r98 copied from the live fixture, same two appends, then verify. Full log: `V50-scratch/rerun-final.txt`.

```
$ python3 <V50-scratch/replay/v94a-quoted-tool-6f81f8be>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 9d89ba3f8e19d34394575a782b8a69c38e7a4ee94b823c0cd8912bafe05416ad != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> 457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3), fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> c62880b9beab277b88dfa2321eef5fd4663b256b8189e9a1568d3cd824842c3c); fixture bytes changed outside the frozen inventory
RESULT ERROR
rc=2
EXACT_MATCH True
```

Same mutation against the live tool (`fb9bb9ff…`): exit 2, same digest, same two file names and sha256s, tail clause `pinned-file bytes changed outside the semantic inventory`. `EXACT_MATCH False`. `CORE_MATCH True` (everything before that clause).

Pair B (r95 README comment + timeline trailing newline) was the same shape: exact on `6f81f8be…`, suffix-only mismatch on the live tool. Not a second scored item.

### T2 — V108 markdown-only append names only that file — **REPRODUCED on the quoted tool; live-tool suffix MISMATCHED**

Quoted by **V108** (`V108-c1-tamper-restore.md`). Append `\nV108-TAMPER fictional-excerpts\n` to a scratch copy of r98 `fictional-excerpts.md`.

```
FINDING DIGEST-MISMATCH: content digest ef0a7f1a39a306dc06eb74f2a8722865c3fee18371ccf9d6b4585d3bf28a13ea != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> 9660d381e09b40c14f7eb3e67ee653bad06ec1a8d9e832c681188a83da457d1c); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT 2
```

My re-run on the quoted tool: that line, `rc=2`, `EXACT_MATCH True`. Live tool: same digest and the single filename, tail clause swapped, `EXACT_MATCH False`, `CORE_MATCH True`.

S1's later quote, which already uses the new clause, does reproduce on the live tool. Scratch mirror, r94 copy, `fictional-excerpts.md` deleted, live tool+contract:

```
$ python3 <V50-scratch/replay-s1>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest dec0a20280e2da7fae055459bd7edaba6567acd2cfd980f7d9193cf700c5205f != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
rc=2
EXACT True
```

That is S1's delete quote, not a third scored tamper. It shows the mismatch in T1/T2 is the documented wording edit, not a different finding.

S1's persisted case, re-run on the live tool after that edit:

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
selftest_rc=0
```

No `dependency-freeze-self-test-*` directory left under the lane root.

### R1 — emptied `depends_on` — **REPRODUCED**

Quoted by **V78** (`V78-cross-gates-2.md`, edge-reduction), **V69** (`V69-crosscheck-coverage-2.md`), and the table file row 1. V78:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
EXIT=1
```

The table also says `check_bible` on that copy is `CLEAN` exit 0.

My re-run: scratch mirror of the live tool+contract and r98; `clerk-filing-open.depends_on` set to `[]`; verify inside the mirror (path binding). Log not separately saved beyond this quote; the process printed:

```
$ python3 <V50-scratch/replay-rows/row1-empty>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
rc=1
ROW1_EXACT True
$ python3 corpus/fixtures/check_bible.py <mirror>/corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
rc=0
```

### R2 — wrong-but-earlier edge — **REPRODUCED**

Quoted by the delivered table (`corpus/knowledge/r99-gate-blind-spot-table.md` lines 76–81, mtime 22:57:50), not by an `S5*.md` (none existed at the replay) and not by any `seats/V*.md` that contained the exact `gained depends_on ['response-evin-salt-court']` line when searched. The table quote:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING ADDITION-DETECTED: event clerk-filing-open gained depends_on ['response-evin-salt-court']
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
exit=1
```

Table also says `check_bible` on that copy is `CLEAN` exit 0.

My re-run, fresh scratch mirror, `depends_on` set to `["response-evin-salt-court"]`:

```
$ python3 <V50-scratch/replay-rows/row2-earlier>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING ADDITION-DETECTED: event clerk-filing-open gained depends_on ['response-evin-salt-court']
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
rc=1
ROW2_EXACT True
$ python3 corpus/fixtures/check_bible.py <mirror>/corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
rc=0
```

At the replay (~23:05) `find … -name 'S5*.md'` returned empty, so this was an artifact replay, not a producer-report replay. `S5-knowledge-author.md` landed at 23:11:27, after the replay. Its summary matches the same finding pair (`ADDITION-DETECTED` + `REDUCTION-DETECTED` exit 1) and the emptied-`depends_on` row (`clerk-filing-open lost depends_on ['acknowledgment-aru-records']`, exit 1). I did not re-run after that landing; the scratch outputs above are the re-run.

### C1 — six-fixture chain verify — **REPRODUCED**

Quoted by **V115** (`V115-c1-verify-vs-freeze.md`) and, with the same digests, by **S1** and **V108**. V115's six:

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

My re-run at 22:53, live tool, each `rc=0`, `MATCH_V115 True`, `CHAIN_ALL_MATCH True`. Contract sha256 before and after the six verifies: both `8c2561b0…`. Verify did not rewrite the pin. I did not pass the live contract to `--freeze`.

### C2 — r99 is unpinned — **REPRODUCED**

Quoted by **V108** (`FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse'`) and by **S1** ("`r99-window-lapse` was not pinned").

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
rc=2
MATCH_V108_UNPINNED True
```

This does not contradict C1's 6/6. The declaration's chain is the existing six. r99 is not a seventh pin.

### N1 — census 172→173 — **REPRODUCED**

Quoted by **V29** (`V29-verdict-depth.md`):

```
{"dirs": 173, "clean": 39, "negative": 134, "violation_lines": 421, "odd": []}
```

and baseline `git ls-tree -d --name-only 4265df5 corpus/fixtures/` → 172. r98 closure text in `corpus/fixtures/README.md` is 172 / 38 / 134 / 421.

My sweep (same definition as the r98 census script: fixture dirs, `check_bible`, violation lines = lines containing `VIOLATION`), 22:53:

```
$ python3 <census over corpus/fixtures/*/ via check_bible.py>
{"dirs": 173, "clean": 39, "negative": 134, "violation_lines": 421, "odd": []}
MATCH_V29 True
```

Corrected baseline (a first call without the trailing slash listed the tree entry itself and printed 1; that was my command bug, not V29's number):

```
$ git ls-tree -d --name-only 4265df5 corpus/fixtures/ | wc -l
172
```

`r99-window-lapse` is in the worktree and not in the baseline tree. The +1 clean directory is that fixture (exit 0, already reproduced under support). Negative 134 and violation lines 421 are unchanged from the r98 closure figures.

### S1-support — `support_check` 21/21 — **REPRODUCED**

Quoted by **S4** (`S4-fixture-docs.md` section C) and **V12** (`V12-c2-support-map.md`). S4's summary:

```
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; … VALIDATED-ROWS 23/23
RESULT PASS
support_exit=0
```

My re-run at 22:04:26 (`V50-scratch/rerun-s4.txt`) and again at 22:53, same map/README hashes as S4 declared (`d2fe20e5…` / `b9320941…`):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
rc=0
```

Companion map quote from S4, same bytes, also matched at 22:04:26: `OBLIGATIONS raw=21 mapped=21` / `RESULT PASS` / `map_exit=0`. Not a scored slot. Inherited J01–J20, namespace swapped back to r98, `changed_inherited 0` (`V50-scratch/inherited-rows.txt`).

## 3. What this does not close

- S2's report never landed. README and SKILL.md were not in the eight slots. V94 already noted they still describe the five-JSON pin. Not re-scored here.
- `S5-knowledge-author.md` was absent at the row replay and present at 23:11:27, after it. Its row summaries agree with R1 and R2. The lapse scope note was not read for a scored quote.
- The two tamper quotes that still say `frozen inventory` do not match current stdout. The finding id, exit, filenames, and hashes do. S1's post-edit quotes match the live tool.
- No claim that prose-edit detection is semantic proof. S1's own report already bounds that.

INCONCLUSIVE — 2 tamper quotes exact on tool `6f81f8be` and suffix-MISMATCHED on live `fb9bb9ff`; 2 table rows reproduced (row 2 without an S5 report); chain 6/6 and r99 UNPINNED reproduced; census 173/39/134/421 and support 21/21 reproduced.
