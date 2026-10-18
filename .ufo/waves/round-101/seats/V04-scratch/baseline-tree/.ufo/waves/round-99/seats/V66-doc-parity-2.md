# V66 — doc-parity-2 (round 99)

Seat: **V66 doc-parity-2** — second inventory. Scope: every lane README, registry, and index surface versus delivered bytes, then a merged list for L1. First inventory on disk: `V25-doc-parity.md`. Axes: completeness (broader surface set than V25's five closure docs), fidelity (quoted commands, not plans), agreement with V25 where both measured the same bytes, non-harm (read-only outside this report and `.ufo/waves/round-99/seats/V66-scratch/`).

Baseline named in the r99 declaration: `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at measurement: `337f0fa` (`lore r99: record blocked dispatch attempt`). `git diff --name-status 4265df5 HEAD` is only `LOG.md` and `SCORECARD.md`. Those two match HEAD (`git diff --stat HEAD` on them was empty). Uncommitted corpus writes at 22:48:10 were only `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, and the untracked `corpus/fixtures/r99-window-lapse/` tree.

## 1. What this inventory covers

77 surfaces, listed in `.ufo/waves/round-99/seats/V66-scratch/surfaces.txt` (script `inventory.py`, run after S4's README and map had landed):

- Root indexes: `README.md`, `PROVINCE.md`, `SCORECARD.md`, `SHONEN.md`, `LOG.md`, `l0-questions.md`, `SKILL.md`.
- Corpus indexes: `corpus/README.md`, `corpus/fixtures/README.md`, `corpus/tools/README.md`.
- Every `corpus/**/README.md` outside `.ufo/` and `v05-self-test-scratch/` (40 fixture READMEs plus the three corpus indexes above).
- Every `corpus/knowledge/*.md` (16 files; the two declared r99 notes were absent).
- Pin registries: `dependency-freeze-contract.json`, `map-obligations-contract.json`, `boundary-doc-contract.json`.
- Continuation-chain claim-excerpt maps, r88 through r99.
- The freeze tool's own module docstring, re-read on the final hash (section 4). `r10-registry-witness/` has no `README.md` (glob returned no match). `reports/` was not treated as a live index of this round.

V25 inventoried the five closure-pass documents. This seat re-measured those five and added the rest. Where both seats measured the same file, the hashes agree (section 6).

## 2. Surfaces that match their own delivered bytes

Byte-identical to `4265df5` (no unowned drift), and carrying no r99 claim that the delivered tree falsifies:

- `PROVINCE.md`, `SHONEN.md`, `l0-questions.md`.
- All 39 pre-r99 fixture READMEs, including the chain READMEs `r88-m3-maya-cluster` through `r98-clerk-filing`. They describe their own fixtures. None claims to be the terminal beat of the arc. No action.
- Knowledge decision tables, `reference-ledger.md`, `seed.md`, and the r95–r98 scope notes. The r98 note's freeze pins (`dependency_freeze.py` `03d04365…`, contract `153ebc5b…`, `r98-clerk-scope-note.md:77-83`) are the r98-closure pins. They still match `git show 4265df5` for those two files. Do not rewrite them as if they were a claim about the r99 working tree. The note already says to re-derive before citing.
- `map-obligations-contract.json` and `boundary-doc-contract.json`.
- Chain claim-excerpt maps r88 through r98.

Delivered r99 index surfaces that match the delivered tables (S4 hashes, re-measured 22:45:21):

```
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
```

Those are the hashes S4's report names. README:3 states 6/1/8 and 8 sources. README:11 states the lapse bound (window closed per the original minute; agreement unfulfilled; no claim lodged; matter stays open; no resolution, no blame, no reconciliation). README:21 states 21 obligations, 20 inherited plus `timeline.json#/7`. README:26-28 are the three replay commands against `corpus/fixtures/r99-window-lapse`. The map's expected inventory is 21 JSON facts, 2 editorial rows, 23 total, 19 distinct anchors. Parsed counts at 22:46:49: entities 6, relations 1, events 8, sources 8, contradictions 0. Last event `clerk-lapse-recorded` tick 15, actor `clerk-maren`, place `chalk-stair`, `depends_on ['clerk-filing-open']`, source `clerk-lapse-note`.

Gates on those bytes (22:04:00, lane root; fixture hashes above unchanged at 22:45):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
# CLEAN: schema, citations, relations, timeline; 0 violations
# EXIT:0
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
# OBLIGATIONS raw=21 mapped=21
# INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
# RESULT PASS
# EXIT:0
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
# SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
# RESULT PASS
# EXIT:0
# PASS J21 cited line 70: Tick 15: The crossing-window named in the original minute has closed.
```

Independent census (`.ufo/waves/round-99/seats/V66-scratch/census_v66.py`, repo-relative `check_bible.py` per direct fixture directory, same counting rule as the r98 V22 census):

```sh
python3 .ufo/waves/round-99/seats/V66-scratch/census_v66.py
# {"clean": 39, "dirs": 173, "has_r99": true, "negative": 134, "non01": [], "r99_exit": 0, "violation_lines": 421}
```

V25's census was the same 173/39/134/421 with `r99` exit 0. Agreed.

## 3. Delivered freeze bytes the index docs must match

Final hashes, 22:46:49 and again 22:48:10:

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

The tool hash changed during the poll (try 31 `6f81f8be1974`, try 32 `fb9bb9ff608c`, then stable through try 40 and the 22:48 snapshot). V25 measured the earlier hash `6f81f8be19742372…` and the same contract hash. Contract did not move. Chain digests on the final tool match the digests this seat recorded on `6f81f8be` and the digests V25 recorded. Self-test was re-run on the final hash, not copied from the earlier hash.

Contract, read on `8c2561b0…`: `schema_version` 2, `payload_schema_version` 2, `pinned_files` the five JSON tables plus `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. Six pins, each with 10 file digests and `payload_schema_version` 2. Pin `revision` on all six is `337f0fa52b02626b7687eedbb2d99fab30446fe4`, not `4265df5`. `self_test.expected` has 18 names, including `markdown_tamper`. `r99-window-lapse` is not a pin. Scope text says each pin covers all ten declared files. Precedence text says `DIGEST-MISMATCH` names each changed pinned file, including the five Markdown files. Provenance's earlier "exactly the four declared chain fixtures" sentence is historical; later sentences in the same note record the six-pin chain and the r99 ten-file upgrade. Do not edit the historical sentences into a current claim.

```sh
python3 corpus/tools/dependency_freeze.py --self-test
# CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
# SELF-TEST 18/18
# RESULT PASS
# SELFTEST_EXIT:0
# (22:46:49, tool sha256 fb9bb9ff608c3333…)
```

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
# FREEZE events 2/2; dependency-edges 0/0; relations 0/0
# DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
# FREEZE events 3/3; dependency-edges 2/2; relations 1/1
# DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
# FREEZE events 4/4; dependency-edges 3/3; relations 1/1
# DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
# FREEZE events 5/5; dependency-edges 4/4; relations 1/1
# DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
# FREEZE events 6/6; dependency-edges 5/5; relations 1/1
# DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
# FREEZE events 7/7; dependency-edges 6/6; relations 1/1
# DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
# RESULT PASS  EXIT:0
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
# FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' ...
#   (pinned: the six names above)
# RESULT ERROR
# EXIT:2
```

The declaration re-freezes the existing chain 6/6. It does not add r99 as a seventh pin. A closure sentence that says the chain is seven, or that r99 is pinned, would be false on these bytes.

The final tool docstring already states the r99 bound (`dependency_freeze.py:25-30`): ten declared files, not the five JSON tables alone; a Markdown edit exits 2 `DIGEST-MISMATCH` naming the file; `markdown_tamper` is the 17→18 case. That surface matches. `SKILL.md` and `corpus/tools/README.md` do not. L1 should update those two docs. It should not treat the tool as undocumented.

C9 pair, reproduced on the delivered checker (same pin the r98 watch row already records):

```sh
sha256sum corpus/fixtures/check_bible.py
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
python3 corpus/tools/discriminate_check.py
# RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
# EXIT:0
python3 corpus/tools/discriminate_check.py --checker e97613c
# REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
# EXIT:2
```

V25 recorded the same pair. Agreed. The r99 watch row is still unwritten.

## 4. Merged stale list for L1

Union of V25's ten items and this seat's broader scan. No item below is contradicted by V25. Items 11–14 are this seat's additions. Historical sentences inside earlier round sections stay; the new text supersedes them.

1. `corpus/fixtures/README.md:1263` — census still **172 / 38 / 134 / 421**. Needs a Round-99 section and a re-declaration **173 / 39 / 134 / 421 / zero non-0/1**. Measured in section 2. No `## Round 99` heading; the file ends at the Round-98 section (`:1244`).
2. `corpus/fixtures/README.md:1259` — "17 cases"; "five JSON tables only"; "BR-01's prose half remains open." The six-fixture list in that sentence is still true. Do not extend it to r99. Replacement bound: self-test 18/18; ten-file payload, `payload_schema_version` 2; prose half edit-detectable, not semantics-provable.
3. `corpus/README.md:25` — navigation list ends at the r98 bullet. No `r99-window-lapse` bullet. Expected fifth-beat bullet: window closed per the original minute, agreement unfulfilled, no claim lodged, matter stays open; 6/1/8, 8 sources, 21 obligations; navigate the map and `fictional-excerpts.md`. No resolution, blame, or reconciliation.
4. `corpus/README.md:40` — "(rounds 96–98)", "17-case persisted self-test", "the pin payload covers the five JSON tables only." The chain arrow through r98 is still the delivered pin set. Do not append r99 to that arrow.
5. `corpus/README.md:33` — C9 bullet still says "including the r93 re-check entry." The log holds rows through r98, and an r99 row is due. After that append, the phrase should cover the r93–r99 entries (or equivalent).
6. `SKILL.md:98` — "17 cases." S2 owns this row. File still `4265df5` hash `22ffaa82…` at 22:48:10. No S2 report. Expected: 18 cases, including `markdown_tamper` (exit 2, finding `DIGEST-MISMATCH`, names `fictional-excerpts.md`).
7. `SKILL.md:99` — "content SHA-256 over the five JSON tables." "exactly the six chain fixtures" is still true. If the row quotes a pin revision, the delivered value is `337f0fa…`, not `4265df5`.
8. `SKILL.md:100` — "the pin payload covers the JSON tables only — fixture Markdown (maps, excerpts) is not pinned; BR-01's markdown/prose half remains open." Stale. Path-binding, scope guard, and path-less migration sentences in this row were not re-probed here and are not contradicted by the declaration.
9. `corpus/knowledge/r91-c9-watch.md` — no r99 row. `:319` already says "Next re-check: r99." Expected row, content pre-verified in section 3: checker pin `ff9fd2aa…d1421`; DISCRIMINATION HELD; control REGRESSION-DETECTED; ruling retained; next re-check r100. No producer owns this file.
10. `corpus/tools/README.md` — S2-owned, still `4265df5` hash `294dd56f…`, no Round-99 addendum, no S2 report. Stale current-tense sentences: `:236` and `:276` "17 cases"; `:238` "five JSON tables only" and "BR-01's markdown/prose half remains open"; `:279` documents `SELF-TEST 17/17`. The six-fixture statements at `:236`–`:237` are still true. The r98 gitignore supersession at `:286`–`:288` was not re-opened.
11. `SKILL.md:96` is **not** stale. Frozen chain of six through `r98-clerk-filing` matches the contract. V25 said the same. Do not add `r99-window-lapse` unless a later pin appears. None had at 22:48:10.
12. `dependency_freeze.py:25-30` already matches the delivered contract (ten files, 18 cases, `DIGEST-MISMATCH` names the file). This landed on the final hash `fb9bb9ff…`, after V25's measurement of `6f81f8be…`. Not a closure-doc gap. Do not describe the tool source as still saying five JSON tables.
13. `corpus/knowledge/r98-clerk-scope-note.md:77-83` names the r98-closure tool pins. Those hashes still match `4265df5`. Not an r99 defect. Do not "update" them to `fb9bb9ff…` / `8c2561b0…` inside an r98 historical note.
14. Root `README.md:16` claims `lessons/` and `QUALITY.md`. Neither path exists (`corpus/lessons`, `QUALITY.md`, `corpus/QUALITY.md` all absent). The file is byte-identical to `4265df5`. Carried pre-existing mismatch, not an r99 closure item. `LOG.md:1670` already records that absence as history.

Not a defect to rewrite: `LOG.md` Round 99 blocked-dispatch section (`:3267`–`:3289`) says that attempt touched no corpus bytes and landed no reports. That is the committed record of the failed dispatch (`337f0fa`), and it matches HEAD. It is not a description of this re-dispatch. Append a re-dispatch note at closure; do not edit those sentences into the current tree. `SCORECARD.md` has no r99 admitted section. `:558`–`:561` is still a plan ("planned (r99)"), not a false claim about delivered bytes. L1 writes the admitted section at closure. Drift of both files versus `4265df5` is the two commits already on HEAD, not a seat edit.

## 5. ABSENT — not verified

After 40 poll tries (22:15:55 through 22:25:35, then 22:38:01 through 22:41:01; the first loop was killed by a 600s background timeout at try 30, recorded, not fatal; tries 31–40 were run in a second loop) plus a 22:48:10 snapshot:

- No `S1-*.md`, `S2-*.md`, or `S5-*.md`.
- No `corpus/knowledge/r99-gate-blind-spot-table.md`.
- No `corpus/knowledge/r99-lapse-scope-note.md`.

S1's tool and contract are on disk without a report. S2's two owned docs did not change. S5's two files did not appear. This inventory does not confirm C2 component 2, and it does not verify any planned S2 or S5 prose. V25 recorded the same absence at 22:36:25. Agreed, and still true at 22:48:10.

Producer reports that were on disk: `S3-fixture-author.md`, `S4-fixture-docs.md`. S3 says the README and map were still r98 copies at its write time. That was true then and is stale for the delivered tree (S4 rewrote both; section 2 gates ran on those bytes). S4's hashes match the 22:45 measurement.

Endgame: this seat did not poll every verifier report. Any such count must subtract SELF. This report is the SELF file.

## 6. Agreement with V25

Agreed, same numbers: closure docs `SKILL.md`, `corpus/README.md`, `corpus/fixtures/README.md`, `corpus/tools/README.md`, and `corpus/knowledge/r91-c9-watch.md` still the `4265df5` hashes; census 173/39/134/421; r99 fixture 6/1/8, 21/21, CLEAN; freeze self-test 18/18; chain 6/6; r99 `UNPINNED-FIXTURE` exit 2; C9 pair green; do not call the chain seven; S5 files and S1/S2/S5 reports absent.

Delta, not a contradiction: the tool was rewritten from `6f81f8be…` to `fb9bb9ff…` at poll try 32 (22:38:21), after V25's 22:36 recheck. Contract hash unchanged. Chain digests unchanged. Self-test re-run on the new hash is still 18/18. The new docstring (`:25-30`) states the ten-file / 18-case bound, which V25's earlier hash was not quoted as stating. The stale-doc list in section 4 is unchanged by that rewrite.

## 7. Bottom line

**PASS (second inventory, merged with V25)** — 77 README/registry/index surfaces checked against delivered bytes; the four unowned closure docs and S2's two owned docs are still the r98 text; census measured 173/39/134/421; r99 README and map match the delivered 6/1/8 and 21-obligation tables; freeze on the final hash `fb9bb9ff…` / contract `8c2561b0…` is 18/18 and chain 6/6, with r99 `UNPINNED-FIXTURE` exit 2; fourteen merged items for L1, of which 11–14 say what not to rewrite. **ABSENT, not verified:** S1/S2/S5 reports and both S5 knowledge files after 40 polls plus a 22:48:10 snapshot — the blind-spot table was not checked.
