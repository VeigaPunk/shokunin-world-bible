# V75 integration-2 — round 99 (independent L1 checklist)

- Seat: V75 integration-2 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Wave tree uncommitted. HEAD throughout `337f0fa52b02626b7687eedbb2d99fab30446fe4` (blocked-dispatch record only; `git log --oneline 4265df5..HEAD` is `337f0fa` then `111b9a3`, both pre-wave).
- Writes: this report, and `.ufo/waves/round-99/seats/V75-scratch/` only. No commits, no pushes, no network, no nested agents, no other lane file written.
- Scope: independent L1 pre-closure checklist for C1 and C2 (both components). Every receipt below was measured by this seat on the delivered bytes. Producer reports were read afterwards for cross-check only. Comparison target V38's report never landed.

Axes named: calibration (C1), depth (C2, both components), coverage (chain re-freeze, witnessed), operability / freshness / adjacency (witnessed, not owned claims).

## 0. Poll-wait record

Cadence 20 s. Never scored a plan. First poller (`.ufo/waves/round-99/seats/V75-scratch/poll.sh`) was killed by a 300 s host timeout after 15 tries (22:02:26–22:07:06); restarted; that second run exhausted try 40 at `2026-10-17T22:29:22-0300` (`POLL-TIMEOUT`). At timeout: knowledge files absent; reports present only `S3-fixture-author.md` and `S4-fixture-docs.md`. Missing: `REPORT:S1 REPORT:S2 REPORT:S5 REPORT:V38`.

Stall-escape (recorded, not fatal): 8 further tries, `stall-escape.log`, `22:49:50`–`22:52:30` `STALL-EXHAUSTED`. By try 1 of that escape `S1-full-file-pins.md` had landed. Knowledge files and V38 were still absent at exhaustion.

Late landings, measured rather than left ABSENT: `corpus/knowledge/r99-*.md` were on disk at the next manual check; `S2-tools-docs.md` and `S5-knowledge-author.md` were present by `23:10`. `V38-integration-checklist.md` was absent at the first write of this report (`23:12`) and present on the immediate re-check. Compared in §7. `V38-scratch/census.txt` (`173/39/134/421`) was not used as the report.

## 1. Revision pinned for the measurements

Re-hashed at write (`sha256sum`):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
```

The tool's only edit after the first self-test (`6f81f8be…`, 22:07) is one detail-string change at 22:38:11 (`fixture bytes changed outside the frozen inventory` → `pinned-file bytes changed outside the semantic inventory`). Exit codes and finding IDs are unaffected. Self-test, row replays, and the newline probe quoted below were re-run on `fb9bb9ff…`. Chain PASS receipts do not print that string; pin digests were recomputed independently and match the contract.

Baseline tool at `4265df5` is `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`. Baseline contract is `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.

Mid-flight observation (not a verdict): before the re-freeze, the new tool against the r98 contract printed `FINDING CONTRACT-INVALID: pin … payload_schema_version None != 2` and the chain exited 2. That state was not scored.

## 2. C1 — calibration (full-file freeze pinning): VERIFIED, with one literal bound

**(a) Payload is all ten files, schema versioned.** Contract root `schema_version` 2 / `payload_schema_version` 2. `pinned_files` equals `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. Each of the six pins has `payload_schema_version` 2, exactly those ten file digests, and `revision` `337f0fa52b02…`. Independently recomputed per-file sha256 and content digest (sorted JSON of name→sha256, `separators=(",", ":")`) match every pin (`files_match=True`, `digest_match=True`).

**(b) Semantic inventory unchanged vs `4265df5`.** For all six pins, `events`, `relations`, `counts`, and the five JSON file digests are identical to the baseline contract. Only the content digest and the five Markdown digests were added. Old→new content digests: r88 `15ef230e…`→`acf677a7085b…`; r94 `2527beb9…`→`048b8ff39e4a…`; r95 `d541ae64…`→`97cffd7bfe6e…`; r96 `d422a9b3…`→`43911900923c…`; r97 `3c922d20…`→`a28b9ea0d65e…`; r98 `59a0f4fa…`→`5ecf84e19121…`.

**(c) Chain 6/6 clean on the delivered contract.** Each `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` printed `RESULT PASS` exit 0:

```
FREEZE r88-m3-maya-cluster:         events 2/2; dependency-edges 0/0; relations 0/0   DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
FREEZE r94-paired-crossing:         events 3/3; dependency-edges 2/2; relations 1/1   DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
FREEZE r95-crossing-aftermath:      events 4/4; dependency-edges 3/3; relations 1/1   DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
FREEZE r96-crossing-response:       events 5/5; dependency-edges 4/4; relations 1/1   DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1   DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
FREEZE r98-clerk-filing:            events 7/7; dependency-edges 6/6; relations 1/1   DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
```

`r99-window-lapse` is not pinned. `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse` → `FINDING UNPINNED-FIXTURE` / `RESULT ERROR` exit 2. That matches the declaration (re-freeze the existing six, not a seventh). S1's report states the same choice. Not a coverage miss.

**(d) Self-test 17→18.** On `fb9bb9ff…`: 18 `CASE … ok` lines, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`, then `SELF-TEST 18/18` / `RESULT PASS` exit 0. Inherited expectation objects vs `4265df5`: `changed=[] added=['markdown_tamper'] dropped=[]`. `markdown_tamper` persisted as exit 2, finding `DIGEST-MISMATCH`, `names_file: fictional-excerpts.md`.

**(e) Before/after, scratch mirrors only (live contract not written).** Non-anchor excerpt replacement `the inherited wording is unchanged` → `the inherited wording is retained` on an r98 copy:

```
# baseline tool 4265df5
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
exit 0
# delivered tool
FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md (sha256 29e384bf… -> ebb0d805…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit 2
```

Same copy, live tools: `check_bible` CLEAN exit 0; `map_obligations` `raw=20 mapped=20` PASS exit 0; `support_check` `SOURCE-SUPPORT 20/20` PASS exit 0. README dependency-wording replacement of the first `depends on` → `is ordered after`: baseline freeze exit 0; delivered freeze exit 2 naming `README.md`; the same three gates stay exit 0. So a prose edit invisible to every other gate, and invisible to the r98 freeze, is named `DIGEST-MISMATCH` after.

The table's coherent edit (excerpt and J14 anchor both `depends on both ninth-bell entries` → `follows both ninth-bell entries`) reproduced: baseline `DIGEST 59a0f4fa…` `RESULT PASS` exit 0; delivered `content digest 1f73326f38eb20f75d6c2541df5ec67ae20e157e5b4c1053dc10464ae88d67f2` exit 2 naming both files; bible/support/map stay green. Narrative-only map edit after-hash `85b16b4f7c952fbfa80649edca86cb1a89220653f49c52f51ff8b1017b8352d0` matches the table; freeze exit 2; lexical gates exit 0.

**Bound, measured.** Removing the J14 anchor sentence from the excerpt alone is not invisible: `support_check` exit 1 `FAIL: J14: source-support anchor missing`. The invisible class is the coherent or non-anchor edit, which is what C1 closes. BR-01's prose half is edit-detectable, not semantics-provable.

**(f) Per-file byte edit exits 2 and names the file.** Appending a newline to each of the ten pinned files, each in its own r98 mirror, exited 2 `DIGEST-MISMATCH` naming that file (nine files probed on `6f81f8be…`; `fictional-excerpts.md` repeated on `fb9bb9ff…`):

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 3e992626a155faba83490f4810d2aa0b13bd1e51e2153e98e1e7af86c925beab != pin 5ecf84e19121…; changed: fictional-excerpts.md (sha256 29e384bf… -> a6bff890…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit 2
```

**(g) Literal "any edit → exit 2" is false for semantic inventory edits.** Dropping `clerk-filing-open.depends_on` to `[]` on a path-bound r98 mirror:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
exit 1
```

No `DIGEST-MISMATCH` line. Semantic findings decide first. That matches the tool and S1's report. It does not match the literal sentence in the declaration, in `SKILL.md:100` ("any pinned-file edit exits 2 `DIGEST-MISMATCH` naming the file"), or in `corpus/tools/README.md:310` ("Any edit to any of the ten pinned files exits 2"). L1 must not promote that sentence as literal. The prose-detectability claim still holds.

**(h) Guard still present.** Mirror `--freeze` of a directory outside `corpus/fixtures/**` → `FINDING SCOPE-REFUSED` / `RESULT ERROR` exit 2. This seat did not re-run `--freeze` against the live contract.

Cross-check: S1's declared digests and the 18/18 self-test match. S2's declared hashes for tool, contract, README (`837a7f5d…`), and SKILL (`e0bcb61a…`) match the bytes at write.

## 3. C2 component 1 — `r99-window-lapse`: VERIFIED

Counts on the delivered JSON: **6 entities / 1 relation / 8 events / 8 sources / 0 contradictions** (6/1/8, sources 7→8).

New records, parsed:

- `sources.json` last item `clerk-lapse-note`, title "Maren's Chalk Stair Lapse Note". Prefix `sources[:-1]` parsed-equal to `4265df5:corpus/fixtures/r98-clerk-filing/sources.json`.
- `timeline.json` last item `clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. Description records the window closed, the agreement unfulfilled, no claim lodged, matter a historical open entry. Prefix parsed-equal to r98. No new entity, claim, or relation.
- `fictional-excerpts.md` byte-prefix of r98 (`True`, 4187 → 5114, 64 → 76 lines). Appended section includes `I record no resolution, assign no blame, and reconcile nothing.`
- Byte-identical to r98: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md`.

Map: `**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.` J01–J20 identical to r98 modulo the namespace string `r98-clerk-filing:` → `r99-window-lapse:` (`J_inherited_changed 0`). S01/S02 identical modulo that same swap. New row only J21: `timeline.json#/7`, source `clerk-lapse-note`, span 66-76, anchor `Tick 15: The crossing-window named in the original minute has closed.`

Receipts (lane root, exit 0):

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

Census, every fixture directory carrying `entities.json`, `check_bible.py`: **CENSUS dirs=173 clean=39 negative=134 other=0 violation_lines=421**. `ls -d corpus/fixtures/*/ | wc -l` = 173. Declared 172→173. r98 closure text is 172/38/134/421; the increment is one clean directory. Inherited negative/violation totals unchanged.

Prose bound: resolution / blame / reconciliation in the new README, map, and excerpt occur as denials (`asserts no resolution, no blame, and no reconciliation`; `closes no one`; `I record no resolution, assign no blame, and reconcile nothing.`). "The agreement was unfulfilled" and "No claim was lodged" are the note's statements about this crossing, not a breach finding. No positive resolution, blame, or reconciliation assertion found in the new text. No canon-truth claim made here.

Scope-note line spots that I re-checked: `sources.json:45` id, `:46` title, `:48` reliability_note; `entities.json:63` `clerk-maren`, `:66` `first_appearance: clerk-filing-note`, `:69` filing-note statement; `timeline.json:77` id, `:84` description; `fictional-excerpts.md:70` and `:74`; `claim-excerpt-map.md:5` inventory and `:42` J21; `README.md:11` contains "closes no one". Note hash `96de708f…` matches S5's report.

## 4. C2 component 2 — blind-spot table: VERIFIED by independent replay

Table hash `4670c0b7…` matches S5's report. Replay script `.ufo/waves/round-99/seats/V75-scratch/replay_rows.py`; log `row-replay.txt`. Mutations were rebuilt in `V75-scratch/row-replay/`, not re-executed from S5's trees. Tool `fb9bb9ff…`, contract `8c2561b0…`.

| Row | Replayed result |
|---|---|
| 1 emptied `depends_on` | freeze exit 1 `REDUCTION-DETECTED` `clerk-filing-open lost depends_on ['acknowledgment-aru-records']`; r98 mirror and r99 twin `check_bible` CLEAN 0; r99 twin support 21/21 PASS, map 21/21 PASS |
| 1b drop `evin-ninth-bell` | freeze exit 1 `paired-crossing-decision lost depends_on ['evin-ninth-bell']`; bible CLEAN 0 |
| 2 wrong-but-earlier | freeze exit 1 `ADDITION-DETECTED` `response-evin-salt-court` and `REDUCTION-DETECTED` `acknowledgment-aru-records`; bible CLEAN 0; r99 twin bible/support/map exit 0 |
| 3 deleted terminal, map kept | r99 bible CLEAN 0, support PASS 0, map exit 1 `phantom_obligation: timeline.json#/7 is not a raw source-attributed obligation`; r98 freeze exit 1 `clerk-filing-open is missing`; bible CLEAN 0 |
| 4 span-break J05 17→20 | support exit 1 `outside-span=17` / `anchor hit outside declared line span 20`; bible CLEAN 0; map PASS 0; r98 freeze exit 2 digest `09858d77de0ecc37…` naming `claim-excerpt-map.md` (matches the table's digest) |
| 5 source-id rebound | r99 map exit 1 `source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'`; support 21/21 PASS; bible CLEAN 0; r98 map exit 1 `timeline.json#/6 does not bind to 'aru-acknowledgment-note'`; freeze exit 2 naming `timeline.json` (digest only; my `json.dumps` bytes differ from S5's quoted sha, the finding class does not) |
| 6 prose | baseline coherent edit `DIGEST 59a0f4fa…` exit 0; delivered same edit digest `1f73326f…` exit 2 naming both files; lexical gates green. Narrative map sha `85b16b4f…` matches the table. Excerpt-only: support exit 1 `J14: source-support anchor missing` |
| 7 consistent regen | r99 (drop event + J21 + restate 21/2/23/19 → 20/2/22/18): bible CLEAN 0, support PASS 0, map `raw=20 mapped=20` PASS 0. r98 twin: map `raw=19 mapped=19` PASS 0, support 19/19 PASS 0, bible CLEAN 0, freeze exit 1 `clerk-filing-open is missing` |
| 8 checker pin | `check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` equals `boundary-doc-contract.json` `checker.sha256`. `boundary_doc_check` `CERTIFIED` exit 0. One-comment scratch copy: `FINDING checker_drift` / `CERTIFICATION FAIL` exit 1 |
| 9 catches | all exit 1 on r99 copies: unknown event `no-such-event-id`; dangling entity `no-such-entity`; unknown source `no-such-source`; missing key `required nonempty list`; self dependency plus timeline inversion; repeated dependency `clerk-filing-open`; tick-14 inversion; deleted predecessor `unknown event 'clerk-filing-open'` |

No row's catch/miss claim failed. Span-break is not support_check-silent; the table says so, and the replay agrees. The declaration's "F15 support_check-silent mutants" is the source-id class (row 5), not the span-break class.

## 5. Integration surface

`git status --porcelain --untracked-files=all -- . ':!.ufo'` at write shows only declared ownership: `SKILL.md`, `corpus/tools/README.md`, `dependency_freeze.py`, `dependency-freeze-contract.json`, untracked `corpus/fixtures/r99-window-lapse/` (10 files), untracked `corpus/knowledge/r99-gate-blind-spot-table.md` and `r99-lapse-scope-note.md`. `LOG.md` and `SCORECARD.md` are unmodified (`git diff --stat` empty). No seat commit. `git rev-parse HEAD` still `337f0fa`.

Regression, this seat: `map_obligations.py --self-test` `RESULT PASS` exit 0 (includes `schema_drift`, `inventory_mismatch`, `dual_pointer`). `boundary_doc_check` `CERTIFIED` exit 0; `--self-test` PASS exit 0. `discriminate_check.py` `DISCRIMINATION HELD` exit 0, `checker_sha256=ff9fd2aa… matches_pin=True`. The `e97613c` control was not re-run here. Scope-note tool pins match: `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`, `map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`.

`v05-self-test-scratch/` at the lane root is mtime `2026-10-17 20:36` (before this wave). Not attributed to r99. No `dependency-freeze-self-test-*` left at the lane root after the self-test. Parent-tree sweep was not exhaustive; no `r99-window-lapse` directory was seen at the parent top level.

Axis witness, not a scalar:

- calibration improved (bounded — prose edits detectable; semantic edits still exit 1; not semantics-provable).
- depth improved (bounded — lapse record closes no one; blind-spot table replayed).
- coverage not harmed (chain 6/6 re-frozen, semantic inventories unchanged; r99 unpinned as declared).
- operability improved on the owned freeze row (18 cases, ten-file pin) and harmed nowhere measured; the "any edit exits 2" sentence is inaccurate (see §2g and the worklist).
- freshness not harmed. New dated knowledge records exist. The r99 C9 re-check row is not filed (unowned).
- adjacency not harmed. Tracked dirt is the declared producer set.

## 6. Closure worklist (unowned paths; none of these is a C1/C2 code defect)

1. `corpus/fixtures/README.md:1259` still says the pin covers the five JSON tables, the prose half remains open, and the self-test is 17 cases. `:1263` still declares census 172/38/134/421. No Round-99 section. Measured census is 173/39/134/421.
2. `corpus/README.md:40` still says rounds 96–98, 17-case self-test, and "the pin payload covers the five JSON tables only."
3. `corpus/knowledge/r91-c9-watch.md:319` ends "Next re-check: r99". The r99 row is not filed. This seat's `discriminate_check` held on `ff9fd2aa…`; the `e97613c` control was not re-run here.
4. `SCORECARD.md:544` (r98 coverage bound) still says "pin payload covers the five JSON tables only; BR-01 prose half open." No Round-99 admitted section. `LOG.md` has the r99 declaration and the blocked-dispatch record, no closure entry. Both unmodified by the wave. Confirmed after reading V38's worklist item.
5. Delivered-doc bound, already written by S2: `SKILL.md:100` and `corpus/tools/README.md:310` say any pinned-file edit exits 2 `DIGEST-MISMATCH`. Semantic inventory edits exit 1 and do not emit that finding (§2g). Do not close that sentence as literal without the precedence clause. S1's report already states the precedence. V38 records the same exit-1 fact and does not list this sentence as a worklist item. Measurement agrees; emphasis differs. Not a claim contradiction.

## 7. Comparison with V38

V38's report `V38-integration-checklist.md` was absent through the stall-escape and through this seat's first write (`23:12`). It was on disk at the immediate re-check. Compared against that file, not against `V38-scratch/`.

Same pinned revision: tool `fb9bb9ff…`, contract `8c2561b0…`, README `837a7f5d…`, SKILL `e0bcb61a…`, table `4670c0b7…`, scope note `96de708f…`, and the ten r99 fixture hashes V38 lists match the hashes this seat measured (map `d2fe20e5…`, README `b9320941…`, excerpts `fefebaf9…`, sources `8c215b38…`, timeline `2cdb9fda…`).

Agreement, both measured independently:

- C1 VERIFIED. Chain digests identical (r88 `acf677a7…` through r98 `5ecf84e1…`). Self-test 18/18, `markdown_tamper` exit 2. JSON digests and event inventories unchanged vs `4265df5`. `r99-window-lapse` `UNPINNED-FIXTURE` exit 2. Semantic edge-drop of `clerk-filing-open.depends_on` exits 1 `REDUCTION-DETECTED`, not `DIGEST-MISMATCH`.
- C2 component 1 VERIFIED. 6/1/8, J01–J20 identical modulo namespace, J21 only new JSON row, bible CLEAN, map 21/21, support 21/21, census `173/39/134/421`.
- C2 component 2 VERIFIED. Both seats replayed rows 1–9 and match the table's catch/miss exits, including freeze digest `09858d77…` (span-break), coherent-prose digest `1f73326f…`, and narrative map sha `85b16b4f…`. Both read the declaration's "support_check-silent" phrase as narrowed by the table: span-break is caught; the silent class is the source-id rebound.
- Ownership set matches. No seat commit. Closure items 1–4 above are the same unowned surfaces V38 lists. Neither seat treats an unpinned r99 as a C1 miss.

Differences, none a claim contradiction:

- Row 5 timeline after-hash. V38 reproduced the table's `eb24e084… -> 17e9230e…`. This seat's `json.dumps` rewrite of the same `source_id` change produced a different sha and the same finding class (exit 2 naming `timeline.json`). Serialization, not a different gate result.
- `e97613c` control. V38 reports `discriminate_check --checker e97613c` → `REGRESSION-DETECTED` exit 2. This seat did not run that control. No disagreement with the delivered-checker `DISCRIMINATION HELD` both seats observed.
- Doc sentence. This seat flags `SKILL.md:100` and `README.md:310` ("any pinned-file edit exits 2") as not literal, because semantic edits exit 1. V38 records that exit-1 fact in §2(b) and still says the S2 docs match delivered behavior. The bytes and the exit codes agree.

## Bottom line

**PASS** — C1 and both C2 components verify on the delivered revision (`dependency_freeze.py fb9bb9ff…`, contract `8c2561b0…`, table `4670c0b7…`, lapse fixture 6/1/8 and 21/21); no axis harmed; the literal "any edit exits 2" sentence is a recorded bound, not a code miss; V38's checklist agrees on the claim verdicts and on the pinned hashes (compared after it landed; row-5 sha and the `e97613c` control are the only non-contradictory differences).
