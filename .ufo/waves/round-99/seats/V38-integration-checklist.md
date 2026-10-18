# V38 integration-checklist — round 99 (L1 pre-closure checklist)

- Seat: V38 integration-checklist (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Declared baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the round `337f0fa52b02626b7687eedbb2d99fab30446fe4` (blocked-dispatch LOG note; `git diff --stat 4265df5..HEAD` is only `LOG.md` and `SCORECARD.md`). Wave tree uncommitted. No commits, no pushes, no network, no nested agents by this seat.
- Writes: this report, and `.ufo/waves/round-99/seats/V38-scratch/**` only. No lane corpus file written.
- Scope: L1 pre-closure checklist for C1 and both C2 components. Every receipt below was measured by me on the pinned revision, not copied from a producer report. Producer reports were read afterwards for cross-check only.
- Axes named: calibration (C1 full-file pin), depth (C2 lapse fixture + blind-spot table). Coverage, operability, freshness, and adjacency witnessed as not harmed.

## 0. Revision pinned for the measurements

Stable across the self-test re-run, the row replay, and the 02:10:53Z snapshot (tool hash unchanged from the post-window remeasure through S5 handoff):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r99-window-lapse/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r99-window-lapse/entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r99-window-lapse/inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r99-window-lapse/source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
```

The r99 fixture hashes were unchanged from the first content landing (try 1, 01:03:54Z) through 02:10:53Z. Tool hash moved during S1's write (`03d04365` baseline → intermediate `6f81f8be` at poll try 40 → delivered `fb9bb9ff`). All C1 receipts below were re-run on `fb9bb9ff` + contract `8c2561b0`. I did not run `--freeze` (it rewrites S1's contract).

Baseline receipts, measured on `git show 4265df5:` tool+contract in a private mirror, before treating the wave as delivered: `--self-test` **17/17** `RESULT PASS` exit 0; chain r88/r94/r95/r96/r97/r98 exit 0 with the r98 JSON-only digests (`15ef230e…`, `2527beb9…`, `d541ae64…`, `d422a9b3…`, `3c922d20…`, `59a0f4fa…`).

## 1. Poll-wait record (20 s cadence; never verified a plan)

- 01:01:26Z first inspection: tool and contract still the `4265df5` hashes; `corpus/fixtures/r99-window-lapse/` present as a partial copy; no producer reports; no `corpus/knowledge/r99*`.
- Tries 1–15 (poller killed by the 300 s tool cap, not by absence) plus continuation tries 16–40, log `.ufo/waves/round-99/seats/V38-scratch/poll.log`. Try 40 at 01:35:06Z: `EXHAUSTED 40`. Expected names `S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S5-knowledge-notes.md` absent. S3 and S4 reports present and size-stable. Contract already schema 2, six pins, 10 files each, 18 self-test cases. Knowledge files still absent. Tool hash at try 40 was `6f81f8be…`, not the later delivered hash.
- Honest poll defect: I polled the r98 filename `S1-freeze-hygiene.md`. The delivered report is `S1-full-file-pins.md` (mtime 22:48 local / 01:48Z), after try 40. The poller would have printed `EXTRA-REPORT` for any `S[1-5]-*.md` not in the expected set; none was present at try 40.
- Stall-escape, recorded, not fatal (8×20 s, `.ufo/waves/round-99/seats/V38-scratch/stall-escape.log`): S2 docs mutated during the stability sleep; S5 scratch appeared; knowledge files landed at escape 6 (22:57, sizes 20526 and 14990) and stayed size-stable through escape 8. Escape exited 2 because S2/S5 *reports* were still absent. By write time all five reports exist: `S1-full-file-pins.md`, `S2-tools-docs.md` (23:10), `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-author.md`. No all-reports poll waited on SELF.

## 2. C1 — calibration (full-file pin): **VERIFIED**

**(a) Before: prose edit invisible.** Private mirror of `4265df5` tool (`03d04365…`) + contract (`153ebc5b…`) and a path-bound copy of `r98-clerk-filing`. Dropped the first line containing `depends`:

```
DROPPED "> Their tick-10 decision depends on both ninth-bell entries: …"
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
EXIT 0
```

Same digest as the unmodified control. Command: `python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing`.

The table's coherent replacement (`depends on both ninth-bell entries` → `follows both ninth-bell entries` in excerpt and map) on that same baseline tool also exits 0 with digest `59a0f4fa…` (replay row 6). I did not re-run S2's exact r95 "first depends on" scratch; the r98 before/after is the claim's before.

**(b) After: any pinned-file edit exits 2 and names the file.** Delivered tool+contract copied into `.ufo/waves/round-99/seats/V38-scratch/tamper-mirror`. Control: `RESULT PASS` exit 0, digest `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0`. Same prose-line drop:

```
FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md (sha256 29e384bf… -> ec243ed1…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT 2
```

A trailing newline appended to each of the ten pinned files, restored between probes, each exit 2 `DIGEST-MISMATCH` naming that file and no other: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

Semantic findings still decide first. Dropping `clerk-filing-open.depends_on` on the same mirror:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
EXIT 1
```

**(c) Self-test 17→18.** On the delivered tree:

```
python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

exit 0. Contract expectation `markdown_tamper` is `{exit: 2, finding_ids: [DIGEST-MISMATCH], names_file: fictional-excerpts.md}`. Inherited expectation objects versus the `4265df5` contract: added `['markdown_tamper']`, dropped `[]`, changed `[]`.

**(d) Chain re-frozen 6/6.** `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>`:

```
FREEZE r88-m3-maya-cluster:         events 2/2; dependency-edges 0/0; relations 0/0   DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae   EXIT 0
FREEZE r94-paired-crossing:         events 3/3; dependency-edges 2/2; relations 1/1   DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef   EXIT 0
FREEZE r95-crossing-aftermath:      events 4/4; dependency-edges 3/3; relations 1/1   DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710   EXIT 0
FREEZE r96-crossing-response:       events 5/5; dependency-edges 4/4; relations 1/1   DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c   EXIT 0
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1   DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54   EXIT 0
FREEZE r98-clerk-filing:            events 7/7; dependency-edges 6/6; relations 1/1   DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0   EXIT 0
```

Each pin has `payload_schema_version` 2, `pinned_files` equal to the ten declared names, and per-file sha256 matching the live bytes (`ALL_PIN_DIGESTS_MATCH True`). Versus `4265df5` pins: the five JSON file digests and the `events` object are unchanged on all six; the five Markdown digests are the addition; content digests moved. Pin `revision` and contract `revision` are `337f0fa52b02626b7687eedbb2d99fab30446fe4`, which is what `freeze()` writes from `git rev-parse HEAD`. S1's report quotes the same six digests from `--freeze`. I did not observe that process.

`r99-window-lapse` is not in the pin set (declared: chain stays six):

```
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' …
RESULT ERROR
EXIT 2
```

**(e) Precedence text.** Delivered `precedence` names exit-1 findings (`REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`), the exit-2 order including `DIGEST-MISMATCH` naming each changed pinned file (including the five Markdown files), `CONTRACT-INVALID` for `payload_schema_version` other than 2, and the `--freeze` `SCOPE-REFUSED` / path-less migration sentence. Those IDs match what the tool emits.

**(f) S2 owned docs match the delivered behavior.** `SKILL.md` freeze row (lines 96–100) says 18 cases, `markdown_tamper`, schema 2, ten files, six-fixture chain, prose half edit-detectable not semantics-provable. `corpus/tools/README.md` Round-99 addendum (line 290) records the same, including the six digests above and `SELF-TEST 18/18`. S2 report hash `837a7f5d…` matches the file I re-read. `git diff --stat` in S2's report (`SKILL.md` 6 lines, README +73) is consistent with an append plus the freeze-row replacement; I did not re-diff every historical paragraph.

## 3. C2 component 1 — lapse fixture: **VERIFIED**

Counts on the delivered JSON: **6 entities / 1 relation / 8 events / 8 sources**. New records: source `clerk-lapse-note`; event `clerk-lapse-recorded` tick 15, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`, `source_id: clerk-lapse-note`. Description records that the crossing-window named in the original minute has closed, the agreement was unfulfilled, no claim was lodged, and the matter stands as a historical open entry.

Inheritance, script `.ufo/waves/round-99/seats/V38-scratch/inherit.py`: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical to `r98-clerk-filing`. `timeline.json` and `sources.json` prefix-identical (7→8). `fictional-excerpts.md` is a byte-prefix of the r98 file plus 927 bytes. The appended section (lines 66–76) is negations, not a resolution: "I record no resolution, assign no blame, and reconcile nothing." No new entity, claim, or relation.

Map: `**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.` J01–J20 identical to r98 modulo `r98-clerk-filing:` → `r99-window-lapse:`. Both editorial rows identical modulo that namespace. New row J21 is `timeline.json#/7` / `clerk-lapse-note` / lines 66–76.

Receipts (all exit 0):

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations

python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS

python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
```

Census (repo-relative `check_bible` over every fixture directory that contains `entities.json`; violation lines = lines containing `VIOLATION`):

```
CENSUS entities.json dirs=173 clean=39 negative=134 other=0 violation_lines=421 all_dirs=173
```

Baseline directory count: `git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l` → **172**. The only new fixture directory in `git status` is `r99-window-lapse`, and it is CLEAN, so the declared 172→173 holds with inherited negative/violation tuples unchanged (134, 421). Clean 38→39 is the one new clean directory.

S3 and S4 reports agree on these hashes and on 20 inherited map rows modulo namespace. No contradiction.

## 4. C2 component 2 — blind-spot table: **VERIFIED** (independently replayed)

Table `4670c0b7…` (20526 bytes, mtime 22:57:50, unchanged through write). Scope note `96de708f8e…` present; I did not line-audit all 14990 bytes. S5's report quotes both hashes. I replayed every table row on fresh scratch copies (`.ufo/waves/round-99/seats/V38-scratch/replay_rows.py`, log `replay.txt`) against tool `fb9bb9ff…` and contract `8c2561b0…`. Live fixtures were not mutated. Outcomes match the table, including several byte-identical digest quotes.

| Row | What I observed |
|---|---|
| 1 emptied `depends_on` | r99 twin: `check_bible` CLEAN 0, `support_check` PASS 0, `map_obligations` raw=21 mapped=21 PASS 0. Pinned r98: `REDUCTION-DETECTED` `clerk-filing-open lost depends_on ['acknowledgment-aru-records']` exit 1; bible CLEAN 0 |
| 1b drop one predecessor | `REDUCTION-DETECTED` `paired-crossing-decision lost depends_on ['evin-ninth-bell']` exit 1; bible CLEAN 0 |
| 2 wrong-but-earlier | r99 twin green on all three lexical gates. Pinned r98: `ADDITION-DETECTED` + `REDUCTION-DETECTED` exit 1; bible CLEAN 0 |
| 3 deleted terminal, map kept | r99: bible CLEAN 0, support PASS 0, map `phantom_obligation: timeline.json#/7` exit 1. Pinned r98: `REDUCTION-DETECTED: event clerk-filing-open is missing` exit 1; bible CLEAN 0 |
| 4 span-break J05 17→20 | support `FAIL J05 … span=20; outside-span=17` exit 1; bible CLEAN 0; map PASS 0. Freeze digest `09858d77…` names `claim-excerpt-map.md` (`c1099d0e… -> f5d2c136…`) exit 2 — same digests the table quotes. Span-break is not support_check-silent; the table says so |
| 5 source-id rebound | r99: bible CLEAN 0, support 21/21 PASS 0, map `source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'` exit 1. Pinned r98: map `timeline.json#/6 does not bind to 'aru-acknowledgment-note'` exit 1; freeze names `timeline.json` (`eb24e084… -> 17e9230e…`) exit 2 — same file digest the table quotes |
| 6 prose wording | Baseline tool: coherent replacement `RESULT PASS` exit 0 digest `59a0f4fa…`. Delivered: `DIGEST-MISMATCH` digest `1f73326f…` naming `claim-excerpt-map.md` (`fc4633b9…`) and `fictional-excerpts.md` (`dbcd5f11…`) exit 2; lexical gates stay green (map raw=20). Narrative-only map edit: lexical gates green; freeze names `claim-excerpt-map.md` (`85b16b4f…`) exit 2. Excerpt-only: `support_check` `FAIL J14: source-support anchor missing` exit 1. Edit-detectable, not semantics-provable |
| 7 consistent regeneration | r99 (drop event, drop J21, restate inventory 21/2/23/19 → 20/2/22/18): bible CLEAN 0, support 20/20 PASS 0, map raw=20 mapped=20 PASS 0. Pinned r98 twin: map raw=19 mapped=19 PASS 0, support 19/19 PASS 0, bible CLEAN 0, freeze `REDUCTION-DETECTED` exit 1 |
| 8 checker byte-frozen | live `check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED` exit 0. One-comment scratch copy: `FINDING checker_drift` / `CERTIFICATION FAIL` exit 1 |
| 9 classes the checker does catch | all exit 1 on r99 scratch copies: unknown event, dangling entity, unknown source, missing `depends_on` key (`required nonempty list`), self dependency plus inversion, repeated dependency, tick-14 inversion, deleted predecessor `unknown event 'clerk-filing-open'` |

The declaration's phrase "F15 support_check-silent mutants" is narrowed by the table, correctly: span-break is caught by `support_check`; the silent class is the source-id rebound (row 5). That is a measured correction, not a miss.

`r99-window-lapse` remains unpinned, so freeze catches rows 1–3 and 7 only on the six pinned fixtures. The table states that bound. I agree.

## 5. Integration surface

- **Change set = declared ownership.** `git status --porcelain --untracked-files=all` excluding `.ufo/` shows only: `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, untracked `corpus/fixtures/r99-window-lapse/` (10 files), untracked `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`. No other corpus path. `map_obligations.py`, `support_check.py`, `boundary_doc_check.py`, `check_bible.py` not in the status.
- **No seat commit.** `git log --oneline 4265df5..HEAD` is `111b9a3` (r98 SCORECARD closure, already in history before this wave's working tree) and `337f0fa` (the blocked-dispatch note, pre-wave). No new commit during the measurements.
- **Regression surface green** on the delivered tree: `map_obligations --self-test` `SELF-TEST CASES 25/25 pinned` exit 0; `map_obligations --frozen .ufo/waves/round-94/frozen/map-obligations-r93` exit 0; `map_obligations` on r98 `raw=20 mapped=20` PASS; `boundary_doc_check` CERTIFIED exit 0 and `--self-test` PASS; `discriminate_check` `RESULT: DISCRIMINATION HELD` exit 0; `discriminate_check --checker e97613c` `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` exit 2. Checker pin `ff9fd2aa…` unchanged.
- **No new parent stray.** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` is absent. `v05-self-test-scratch/` at the lane root is gitignored, mtime 20:36 (before this wave's 22:00 start); pre-existing, not an r99 producer write. No `dependency-freeze-self-test-*` left at the lane root after the self-test.
- Producer cross-check: S1 digests match my chain. S3/S4 fixture hashes and 20-row namespace claim match. S2 doc hashes match. S5 table hash matches, and my replay matches its quoted exits. No contradiction that changes a claim.

## 6. Closure worklist (unowned paths; L1 action before commit — none of these is a C1/C2 defect)

1. `corpus/README.md:40` still says rounds 96–98, "17-case persisted self-test", "the pin payload covers the five JSON tables only."
2. `corpus/fixtures/README.md:1259` and `:1263` — no Round-99 section; still "17 cases", "five JSON tables only", "BR-01's prose half remains open", census **172/38/134/421**. Measured now **173/39/134/421**.
3. `corpus/knowledge/r91-c9-watch.md:319` — r98 row ends "Next re-check: r99". No r99 row. I re-ran the pair (`DISCRIMINATION HELD` exit 0; `e97613c` control exit 2) but did not append the watch row (unowned).
4. `SCORECARD.md:544` — r98 coverage bound still says "pin payload covers the five JSON tables only; BR-01 prose half open." No Round-99 admitted section. `LOG.md` has the r99 declaration and the blocked-dispatch note only; no closure entry.
5. `r99-window-lapse` is intentionally unpinned. Do not treat a later `--freeze` of it as required by this round's C1. Do not re-run `--freeze` against the delivered contract to "re-check"; it rewrites the pin.

## Bottom line

**PASS** — C1 (prose edit invisible on `4265df5` tool digest `59a0f4fa…` exit 0, same edit and a newline on each of the ten files `DIGEST-MISMATCH` exit 2 naming the file, self-test 18/18 with `markdown_tamper`, chain 6/6 on schema-2 ten-file pins, five JSON digests and event inventories unchanged, semantic reduction still exit 1) and both C2 components (fixture 6/1/8, 21/21 map, CLEAN, census 172→173 with 134/421 unchanged; blind-spot rows 1–9 independently replayed, including the table's quoted digests `09858d77…`, `17e9230e…`, `1f73326f…`, `85b16b4f…`) verify on tool `fb9bb9ff…` + contract `8c2561b0…`; no axis harmed; owned change set matches the declaration; five closure-doc items remain on unowned paths.
