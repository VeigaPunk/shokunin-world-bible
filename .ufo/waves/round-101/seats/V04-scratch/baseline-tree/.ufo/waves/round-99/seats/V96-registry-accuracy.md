# V96 — registry-accuracy (round 99)

Seat: V96 registry-accuracy. Leaf verifier. No commits, no pushes, no network, no nested agents. Exclusive writes: this report and `.ufo/waves/round-99/seats/V96-scratch/`.

Task: verify every SKILL.md gate-registry row's commands and exits against delivered behavior by running each entry command from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`.

Working-tree HEAD: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (r99 blocked-dispatch note). Declared baseline `4265df5e86e4121bde4125b649b89bb1676676a5`. At 22:29 `git diff --stat HEAD -- SKILL.md` was empty. That is not the final tree: the freeze row changed at 22:51:39. The verdict is the late-landing section, not the 22:29 reading.

## Poll

Producer reports required for the freeze row: S1 (`dependency_freeze.py` + contract) and S2 (SKILL.md freeze row + tools README). Cadence 20s, max 40. Script: `.ufo/waves/round-99/seats/V96-scratch/poll.sh`. Log: `poll.log`.

```
try=1 ts=2026-10-17T22:08:40-03:00 s1=0 s2=0 reports=[S3-fixture-author.md S4-fixture-docs.md ]
try=40 ts=2026-10-17T22:21:40-03:00 s1=0 s2=0 reports=[S3-fixture-author.md S4-fixture-docs.md ]
EXHAUSTED try=40 s1=0 s2=0
```

Final recheck `2026-10-17T22:29:34-03:00`: still only `S3-fixture-author.md` and `S4-fixture-docs.md`. `S2-scratch/` empty. `S1-scratch/before/mirror/` exists; no `S1*.md` report. This verdict is on files present, not on a planned row rewrite. S3/S4 do not own the registry.

Hashes at 22:29:34, unchanged from the 22:14 passing freeze run (contract mtime 22:08:46, tool mtime 22:07:33):

```
22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5  SKILL.md
294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207  corpus/tools/README.md
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

`git diff --stat HEAD` at 22:29:34:

```
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  65 ++++++++++-
 2 files changed, 206 insertions(+), 22 deletions(-)
```

SKILL.md and `corpus/tools/README.md` are not in that diff.

## Row count

Seat brief said six registry rows. Delivered `SKILL.md` Gate registry (`## Gate registry` at line 44) has five `###` headings and five `- **name:**` / entry / self-test / code-map fields:

1. `boundary_doc_check` (line 50)
2. `discriminate_check` (line 61)
3. `support_check` (line 72)
4. `map_obligations` (line 83)
5. `dependency_freeze` (line 94)

No sixth `###` row appeared during the poll. `corpus/tools/*.py` is those five scripts. `check_bible.py` is cited in the error-signature section and is not a registry row; that was already true at `4265df5`. All five present rows were run. There was no sixth row to run.

## 1. boundary_doc_check — entry and self-test match

Row: entry `python3 corpus/tools/boundary_doc_check.py`; `0 → clean`; `1 → failed`; other → `could-not-evaluate`; self-test `python3 corpus/tools/boundary_doc_check.py --self-test`.

```
python3 corpus/tools/boundary_doc_check.py
# 2026-10-17T22:05:03-03:00  EXIT:0
CHECK pinned inputs: PASS
CHECK receipt replay: PASS
CHECK explicit anchor ranges: PASS
CHECK document structure: PASS
scope=frozen-document drift + receipts + explicit-anchor range + structure; not semantic or AST validation
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
```

Exit 0 with `CERTIFIED` matches `0 → clean`. stderr empty.

```
python3 corpus/tools/boundary_doc_check.py --self-test
# 2026-10-17T22:05:03-03:00  EXIT:0  stderr empty
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2 legacy_anchor=check_bible.py:212-224@5eb9451baff217c19d5786405f9b2aa500b7c1b7 baseline_lines=330
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS comment_parked_c9 exit=1 findings=['document_drift']
SELF-TEST PASS wrong_bare_anchor exit=1 findings=['document_drift']
SELF-TEST PASS checker_drift exit=1 findings=['checker_drift']
SELF-TEST PASS missing_document exit=1 findings=['document_missing']
SELF-TEST PASS missing_checker exit=1 findings=['checker_missing']
SELF-TEST PASS receipt_drift exit=1 findings=['receipt_drift']
SELF-TEST PASS
```

Those eight case names are exactly `corpus/tools/boundary-doc-contract.json` `self_test.expected` keys. Self-test command exists, spelling is `--self-test`, exit 0. Matches the row. The row does not claim a numeric case count.

Noted, not an entry-command miss: `python3 corpus/tools/boundary_doc_check.py --selftest` at 22:13:03 exited 1 (stderr: `unrecognized arguments: --selftest`, stdout empty). `boundary_doc_check.py:760-763` remaps any nonzero argparse `SystemExit` to 1. The row maps 1 to `failed` and does not carve usage out the way the discriminate row does, so a flag typo is classed as failed rather than `could-not-evaluate`. The written map matches the number the tool returns. It does not contradict the entry command.

## 2. discriminate_check — both entry commands match

Row: `python3 corpus/tools/discriminate_check.py` is `0 → clean`; negative control `python3 corpus/tools/discriminate_check.py --checker e97613c` is `2 → failed` only with `REGRESSION-DETECTED`. Argparse exit 2 without that text is `could-not-evaluate`. Self-test unavailable; `--selftest` absent.

```
python3 corpus/tools/discriminate_check.py
# 2026-10-17T22:05:04-03:00  EXIT:0  stderr empty
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
```

```
python3 corpus/tools/discriminate_check.py --checker e97613c
# 2026-10-17T22:05:04-03:00  EXIT:2  stderr empty
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
```

Exit 0 + `DISCRIMINATION HELD` matches clean. Exit 2 + `REGRESSION-DETECTED` matches the negative-control failed class.

```
python3 corpus/tools/discriminate_check.py --checker not-a-rev
# 2026-10-17T22:13:03-03:00  EXIT:2  stdout empty
# stderr: argument --checker: invalid choice: 'not-a-rev' (choose from 'delivered', 'e97613c')
```

Exit 2 without `REGRESSION-DETECTED` matches the row's argparse carve-out (`could-not-evaluate`).

```
python3 corpus/tools/discriminate_check.py --self-test
# EXIT:2  stdout empty  stderr: unrecognized arguments: --self-test
python3 corpus/tools/discriminate_check.py --selftest
# EXIT:2  stdout empty  stderr: unrecognized arguments: --selftest
```

`--help` lists only `-h`, `--checker {delivered,e97613c}`, `--repo-root`. Self-test unavailable, as the row says.

## 3. support_check — entry instantiations match

Row: `python3 corpus/tools/support_check.py <cluster-directory>`; `0 → clean` (including warnings); `1 → failed`; `2 → could-not-evaluate`. Self-test unavailable; `--selftest` spelling absent. Pinned-value examples named in the row: `r89-inspiration-paraphrase`, `r87-myth-cluster`. Also ran `r88-m3-maya-cluster` and `r98-clerk-filing`.

```
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
# 2026-10-17T22:07:33-03:00  EXIT:0
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS

python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
# 2026-10-17T22:07:33-03:00  EXIT:0
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS

python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
# 2026-10-17T22:07:33-03:00  EXIT:0
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS

python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
# 2026-10-17T22:05:04-03:00  EXIT:0
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
```

All four exit 0 with `RESULT PASS`, matching `0 → clean`. stderr empty. r89 is retelling-only and still exit 0, which the row allows.

```
python3 corpus/tools/support_check.py
# 2026-10-17T22:13:03-03:00  EXIT:2
# stdout: RESULT ERROR
# stderr: the following arguments are required: cluster

python3 corpus/tools/support_check.py --selftest corpus/fixtures/r87-myth-cluster
# EXIT:2
# stdout: RESULT ERROR
# stderr: unrecognized arguments: --selftest

python3 corpus/tools/support_check.py --self-test corpus/fixtures/r87-myth-cluster
# EXIT:2
# stdout: RESULT ERROR
# stderr: unrecognized arguments: --self-test
```

Exit 2 + `RESULT ERROR` matches `2 → could-not-evaluate`. Both self-test spellings are unrecognized when a cluster is supplied. `--help` has no self-test flag. Matches the row. (`--self-test` with no cluster prints only the missing-cluster error, because argparse reports the required positional before unrecognized optionals; the with-cluster run is the one that shows the flag is absent.)

## 4. map_obligations — entry, frozen demo, and 25-case self-test match

Row: `python3 corpus/tools/map_obligations.py <cluster-directory>`; optional demo `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93`; `0 → clean`; `1 → failed`; `2 → could-not-evaluate`. Self-test `python3 corpus/tools/map_obligations.py --self-test`; 25 cases. `--selftest` spelling absent.

```
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
# 2026-10-17T22:05:04-03:00  EXIT:0  stderr empty
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS

python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
# 2026-10-17T22:05:04-03:00  EXIT:0  stderr empty
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS

python3 corpus/tools/map_obligations.py --self-test
# 2026-10-17T22:05:04-03:00  EXIT:0  stderr empty
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS complete exit=0 findings=none
... 23 more SELF-TEST PASS lines ...
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
```

`grep -c '^SELF-TEST PASS '` on that stdout is 25. Exit 0 and `25/25` match the row's 25-case self-test. Entry and frozen demo exit 0 `RESULT PASS`, matching `0 → clean`.

```
python3 corpus/tools/map_obligations.py
# 2026-10-17T22:13:03-03:00  EXIT:2
FINDING invalid_arguments: cluster directory is required
RESULT ERROR

python3 corpus/tools/map_obligations.py --selftest
# 2026-10-17T22:13:03-03:00  EXIT:2
FINDING invalid_arguments: unrecognized arguments: --selftest
RESULT ERROR
```

Exit 2 matches `could-not-evaluate`. `--selftest` is absent, as the row says.

## 5. dependency_freeze — entry exits match; row text does not

Row still on disk (SKILL.md:96-100, hash `22ffaa82…`, identical to HEAD and to `4265df5`):

- entry: `python3 corpus/tools/dependency_freeze.py <fixture-dir>` for the six named chain fixtures
- `0 → clean`; `1 → failed` (`REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE`); `2 → could-not-evaluate`
- self-test: `python3 corpus/tools/dependency_freeze.py --self-test`; **17 cases** (r97 `SCOPE-REFUSED`, `PATH-MISMATCH`; r98 `self_test_mismatch`)
- pinned-values path: `corpus/tools/dependency-freeze-contract.json` — content SHA-256 over the **five JSON tables**
- scope: "the pin payload covers the JSON tables only — fixture Markdown (maps, excerpts) is not pinned; BR-01's markdown/prose half remains open"

### Mid-write, not the verdict

At 22:05:05, before the contract pins carried `payload_schema_version` 2, the same entry command failed closed:

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
# EXIT:2
FINDING CONTRACT-INVALID: pin r98-clerk-filing payload_schema_version None != 2 (full-file pin of 10 files)
RESULT ERROR

python3 corpus/tools/dependency_freeze.py --self-test
# EXIT:2
SELF-TEST 4/18
FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'clean', 'digest_tamper', 'event_endpoint_change', 'event_removed', 'malformed_json', 'markdown_tamper', 'missing_fixture', 'missing_timeline', 'path_mismatch', 'reduction_edge_drop', 'relation_added', 'relation_endpoint_flip', 'relation_removed']
RESULT ERROR
```

That 4/18 tally already named an 18th case, `markdown_tamper`, which the standing row does not. Poll try 12+ then showed `schema_top=2 pin_vers=2 pins=6 cases=18 case_has_md=True`. Contract hash settled at `8c2561b0…` (mtime 22:08:46) and was the same hash at 22:29:34. The runs below are on that stable tree. `--freeze` was not run (S1-owned write).

### Stable entry commands — exits match `0 → clean`

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
# 2026-10-17T22:14:28-03:00  EXIT:0
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
# EXIT:0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
# EXIT:0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
# EXIT:0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
# EXIT:0
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS

python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
# EXIT:0
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

Six of six chain entry commands exit 0 `RESULT PASS`. That matches `0 → clean`. stderr empty. The six names in the row are the six pins.

Usage probes on the same tree match `2 → could-not-evaluate`:

```
python3 corpus/tools/dependency_freeze.py
# EXIT:2
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR

python3 corpus/tools/dependency_freeze.py --selftest
# EXIT:2
FINDING INVALID-ARGUMENTS: unrecognized arguments: --selftest
RESULT ERROR
```

`--help` exposes `--self-test`, not `--selftest`.

### Self-test command — exit 0, but the row's "17 cases" is false

```
python3 corpus/tools/dependency_freeze.py --self-test
# 2026-10-17T22:14:29-03:00  EXIT:0  stderr empty
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

The exit code 0 is a passing self-test. The row's case count is not. Observed 18 cases, including `markdown_tamper`. The row says 17. The code→class map still matches the case exits: exit 1 only with `REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE`; exit 2 for the could-not-evaluate findings, including `DIGEST-MISMATCH`.

### Pin scope in the row contradicts the contract the row cites

At 22:14:28, `corpus/tools/dependency-freeze-contract.json` (the row's pinned-values path) had `schema_version` 2, 18 `self_test.expected` names including `markdown_tamper`, and six pins each with `payload_schema_version` 2 and these ten files:

`README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`

`markdown_tamper` expected value observed in that file: `{'exit': 2, 'finding_ids': ['DIGEST-MISMATCH'], 'names_file': 'fictional-excerpts.md', 'forbid_traceback': True}`. The self-test case passed, so the delivered command treats a Markdown edit as exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`.

At 22:29 the standing row still said the pin covers the five JSON tables only and that fixture Markdown is not pinned, with BR-01's prose half open. That sentence was false against the contract and the 22:14 self-test. S2's report was absent through 40 polls and at the 22:29 recheck. That reading is chronology. It is superseded by the late landing below.

## Late landing (supersedes the 22:29 row text)

After this report was first written, the freeze row changed. Recheck `2026-10-17T22:53:15-03:00`:

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
```

Tool mtime 22:38:11 (hash no longer `6f81f8be…`). Contract hash unchanged from the 22:14 pin read. SKILL.md mtime 22:51:39, same timestamp as `corpus/tools/README.md`. `git diff HEAD -- SKILL.md` is three lines in the freeze row only (17→18 cases, five JSON tables→ten declared files, BR-01 prose half now "any prose edit is detectable"). The other four registry rows are not in that diff. Stability recheck `2026-10-17T23:01:18-03:00`: those three hashes and the 22:51:39 SKILL mtime unchanged. `S2*.md` still absent. `S1-full-file-pins.md` had landed at 22:48 (after poll exhaustion); it says S1 did not write SKILL.md. The row bytes are what was verified, not S2's missing report.

Delivered freeze row (SKILL.md:98-100), quoted from the file at 22:53:

- self-test: `python3 corpus/tools/dependency_freeze.py --self-test`; 18 cases, r99 added `markdown_tamper`
- pinned-values: `schema_version` 2 / `payload_schema_version` 2; SHA-256 over all ten declared files (five JSON tables + `README.md` + `claim-excerpt-map.md` + `fictional-excerpts.md` + `inspiration-note.md` + `source-excerpt.md`); exactly the six chain fixtures
- scope: full-file digests over those ten files; any pinned-file edit exits 2 `DIGEST-MISMATCH` naming the file; BR-01's prose half is edit-detectable, not semantics-provable; files outside the ten (r88 `symbolism-clause-map.md`) are not pinned

Re-ran the entry commands and self-test after that tool hash, cwd lane root, `2026-10-17T22:53:15-03:00`. Stdout digests matched the 22:14 run. stderr empty.

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
# EXIT:0  RESULT PASS  DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
# EXIT:0  RESULT PASS  DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
# EXIT:0  RESULT PASS  DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
# EXIT:0  RESULT PASS  DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
# EXIT:0  RESULT PASS  DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
# EXIT:0  RESULT PASS  DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
python3 corpus/tools/dependency_freeze.py --self-test
# EXIT:0
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

Those exits match the updated row: chain entry `0 → clean`; self-test 18 cases including `markdown_tamper` at exit 2 `DIGEST-MISMATCH`. The contract hash is the one whose pins list exactly those ten files and omit `symbolism-clause-map.md`. `--freeze` was not re-executed here; the row's "re-frozen through guarded `--freeze`" is S1's write, and the verify digests match the digests S1 quotes.

The other four rows were not edited. Their 22:05–22:13 entry-command exits still stand against the unchanged tools.

## What was not graded

- No `--freeze` write.
- `r99-window-lapse` is not in the registry entry command or in the six pins.
- S5 knowledge files are not registry rows.
- S2's report file was still absent at 23:01. The freeze-row bytes were present and stable.

Full stdout/stderr is under `.ufo/waves/round-99/seats/V96-scratch/runs/` (`late-*` is the 22:53 re-run).

PASS: five SKILL.md registry rows, not six; after the 22:51 freeze-row update, each row's entry command and declared exit match a run on the delivered tree (freeze chain 6/6 exit 0 and SELF-TEST 18/18 re-run at 22:53). S2 report file still absent at 23:01; the row bytes were verified.
