# V73 — shonen-2 (round-99 verification seat, lore-shokunin)

**Seat:** independent SHONEN form check + SKILL.md registry accuracy audit against delivered tool behavior.
**Leaf:** no nested agents, no commits, no network. Writes: this report and `.ufo/waves/round-99/seats/V73-scratch/` only.
**Lane root:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. All commands below were run there unless noted.
**Revision:** working-tree HEAD `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa lore r99: record blocked dispatch attempt … — zero increment`). Round baseline `4265df5e86e4121bde4125b649b89bb1676676a5`. Scores unmeasured. Wave tree uncommitted.

**Axes used:** form fidelity (SHONEN.md vs the canonical seed); registry accuracy (every named SKILL.md gate row vs a command I ran); evidence completeness (quoted command + observed output); non-harm (no live-fixture or SKILL.md edits).

## Poll

Protocol: artifacts and producer reports, 20s cadence, max 40 tries, ABSENT rather than a plan. Tries 0 and 1 were manual; a scratch poller then logged tries 2–40. `poll.log` line 492 is `EXHAUSTED` at `2026-10-17T22:30:59-0300`.

At exhaustion (try 40, `2026-10-17T22:30:59-0300`):

- Present: `S3-fixture-author.md`, `S4-fixture-docs.md`.
- ABSENT: `S1*.md`, `S2*.md`, `S5*.md`.
- `SKILL.md` identical to `4265df5`. SHA-256 `22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5`. mtime `2026-10-17 21:34:23`. Five `**name:**` rows, not six.

Late landing, after that exhaustion and after the first draft of this report. Re-checked before the correction below. Not a 41st poll; the bytes changed under the draft.

- `S1-full-file-pins.md` present (mtime 22:48). I did not adopt its narrative. S2 and S5 reports still ABSENT.
- `SKILL.md` no longer identical to `4265df5`. `git diff --stat 4265df5 -- SKILL.md` → `1 file changed, 3 insertions(+), 3 deletions(-)`, freeze-row lines only. SHA-256 `e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443`. mtime `2026-10-17 22:51:39`. Still five `**name:**` rows.
- `corpus/tools/README.md` mtime also moved to 22:51:39 (38397 bytes). S2-owned. Not audited here.
- Freeze bytes were on disk and I executed them. They are not a plan. S1's report is still ABSENT, so I do not credit any S1 narrative — only the commands below.
  - Commands in §3.5 (self-test, chain, first scratch tamper) ran against `dependency_freeze.py` as copied into `V73-scratch/mirror/` : 29104 bytes, SHA-256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`, poll mtime 22:07:33.
  - After the poll, and after that copy, the live file's mtime moved to 22:38:11 and the size to 29110. SHA-256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`. One line differs (658 lines both): the `DIGEST-MISMATCH` detail clause changed from `fixture bytes changed outside the frozen inventory` to `pinned-file bytes changed outside the semantic inventory`. Re-run on that later file is in §3.5. S1 report still absent.
  - `corpus/tools/dependency-freeze-contract.json` SHA-256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes, mtime 22:08:46). Unchanged across the tool's 6-byte wording edit.

`git status --short -- corpus/fixtures/r98-clerk-filing SKILL.md SHONEN.md` was empty at the first draft. Scratch tampers did not touch those paths. `SKILL.md` then changed, as recorded above; `SHONEN.md` and `r98-clerk-filing` were not part of that diff.

## 1. SHONEN form — PASS

`SHONEN.md` is 12 lines, four `[~]`, zero `[x]`, zero `[ ]`. Digest `03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1`, the same digest recorded by the r94–r98 form seats. `git diff HEAD -- SHONEN.md | wc -l` → `0`. `git diff 4265df5 -- SHONEN.md | wc -l` → `0`.

Mechanical checker (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`), run from the lane root:

```
PASS title matches seed modulo <name>
PASS seed frame (blank + manifest line)
PASS four boxes, seed order and text
PASS marks confined to box character
PASS no [x] promotion claim present
PASS at most one evidence line per box
PASS both [~] boxes carry their required pointer
PASS box2 evidence names the LOG.md entry
PASS box2 evidence names reports/round-1/baseline-probes.json
PASS box4 evidence cites PROVINCE.md:3-11 within range
SHA256 SHONEN.md 03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1
SHA256 SKILL.md 22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5
SHA256 PROVINCE.md 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
EXIT:0
```

Mark census, independent of the checker:

```
grep -c '^- \[~\]' SHONEN.md  → 4
grep -c '^- \[x\]' SHONEN.md  → 0 (grep exit 1)
grep -c '^- \[ \]' SHONEN.md  → 0 (grep exit 1)
grep -c '^- \[' SHONEN.md     → 4
grep -n '\[x\]' SHONEN.md     → no match (grep exit 1)
```

Independent seed diff against `PROTOCOL.md:425-432` (4-space indent stripped, `<name>` → `lore-shokunin`): substituted frame match True (lines 1–4); box texts match True; seed marks are all `[ ]`. Four evidence lines, one per box, no other prose.

Evidence pointers, 13/13 files present: `SKILL.md`, `LOG.md`, `PROVINCE.md`, `reports/round-1/baseline-probes.json`, `.ufo/waves/round-93/recovery/R08-skill-check.py`, `.ufo/waves/round-93/deepseek/{F21,F29,F01,F25-replay.py,F31,F14-postrepair-check.py,F03,F24}.md`. `LOG.md` contains `Fleet round 1 — calibration declaration before batched dispatch` once. `PROVINCE.md` has 11 lines, so `:3-11` is in range (line 3 owns fictional-world records; line 11 is the write-scope sentence).

```
git cat-file -t 8e5a68d                         → commit
git merge-base --is-ancestor 8e5a68d HEAD       → exit 0
git log --oneline -1 8e5a68d                    → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

Negative controls: checker copied to `V73-scratch/negctl/a/b/c/d/check.py` (`parents[4]` = the sandbox, not the lane). Sandbox baseline exits 1 with `FAIL title matches seed modulo <name>` because the directory is named `negctl`. That title fail is a sandbox artifact, not a live-file defect. Three tampers, each on the sandbox copy only:

- `[~]` → `[x]` on box 1: EXIT=1, `FAIL no [x] promotion claim present`
- box 2 evidence line removed: EXIT=1, `FAIL both [~] boxes carry their required pointer` (also the two box-2 pointer checks)
- fifth box appended: EXIT=1, `FAIL four boxes, seed order and text`

`PROTOCOL.md:63-68`: `[x]` requires a reviewer who did not author the round's changes; a subagent the lane dispatched is still the lane. This seat does not convert any box to `[x]`. `PROTOCOL.md:417` is the form that was diffed.

**SHONEN verdict:** PASS. Four `[~]`, zero `[x]`, canonical against the checker and an independent seed diff, pointers live, cited commit an ancestor, checker discriminates on three tamper classes.

## 2. Registry count — five rows, not six

The seat brief says "all six rows". The registry home (`SKILL.md:44-100`, "Rows follow the fleet schema in `../PROTOCOL.md:360-406`") contains five `**name:**` rows:

1. `boundary_doc_check`
2. `discriminate_check`
3. `support_check`
4. `map_obligations`
5. `dependency_freeze`

`rg -c '^- \*\*name:\*\*' SKILL.md` → `5`. `corpus/tools/*.py` is those same five files. `check_bible.py` lives under `corpus/fixtures/` and is cited in the error-signature section; it is not a registry row. That omission predates this round (SKILL.md is byte-identical to `4265df5`). I audited every named row. There is no sixth row to compare. I do not treat the brief's "six" as a new lane defect.

Fleet row fields (`PROTOCOL.md:386-388`) are eight, not six: name, gate|probe, entry command, verdict map, self-test command, pinned-value path, scope, owner. Each of the five rows has those eight labels (`scope`, not the literal words "write scope").

`git diff --stat 4265df5 --` the four non-freeze tools, their contracts, and `SKILL.md` was empty. Those four rows were not rewritten this round. The freeze tool and contract were.

## 3. Row audits vs commands I ran

### 3.1 `boundary_doc_check` — matches, with one usage-exit bound

Entry command, lane root:

```
python3 corpus/tools/boundary_doc_check.py
EXIT:0
CHECK pinned inputs: PASS
CHECK receipt replay: PASS
CHECK explicit anchor ranges: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
```

Missing document (row: `1 → failed`):

```
python3 corpus/tools/boundary_doc_check.py --doc /tmp/does-not-exist-v73.md
CHECK pinned inputs: FAIL
FINDING document_missing: document not found: /tmp/does-not-exist-v73.md
CERTIFICATION FAIL
EXIT:1
```

Self-test (row: `--self-test`, capability not live certification). Contract `self_test.expected` has 8 names; the run printed 8 case lines plus the summary:

```
python3 corpus/tools/boundary_doc_check.py --self-test
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] ...
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS comment_parked_c9 exit=1 findings=['document_drift']
SELF-TEST PASS wrong_bare_anchor exit=1 findings=['document_drift']
SELF-TEST PASS checker_drift exit=1 findings=['checker_drift']
SELF-TEST PASS missing_document exit=1 findings=['document_missing']
SELF-TEST PASS missing_checker exit=1 findings=['checker_missing']
SELF-TEST PASS receipt_drift exit=1 findings=['receipt_drift']
SELF-TEST PASS
EXIT:0
```

Pinned-values path `corpus/tools/boundary-doc-contract.json` exists. `--help` exposes `--self-test` and not `--selftest`.

Bound, not a row falsehood: `boundary_doc_check.py` turns argparse `SystemExit` into exit 1 (`except SystemExit as error: return 0 if error.code == 0 else 1`). Observed:

```
python3 corpus/tools/boundary_doc_check.py --selftest
unrecognized arguments: --selftest
EXIT:1
```

The row maps `1 → failed` and does not carve usage errors out (unlike `discriminate_check`). The map matches the tool. A typo flag is therefore classed `failed`, not `could-not-evaluate`.

### 3.2 `discriminate_check` — matches

```
python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: ... pinned_semantic_gate=PASS
r91-c1-tick-unresolved: ... pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT:0
```

That hash is `PIN` at `corpus/tools/discriminate_check.py:12`. `BASELINE` at line 13 is `e97613cc276f5fa9cac49ff1900798cf6863c020`. Negative control:

```
python3 corpus/tools/discriminate_check.py --checker e97613c
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT:2
```

Usage without that text (row: argparse exit 2 is `could-not-evaluate`, not a regression verdict):

```
python3 corpus/tools/discriminate_check.py --checker nope
error: argument --checker: invalid choice: 'nope'
EXIT:2

python3 corpus/tools/discriminate_check.py --self-test
error: unrecognized arguments: --self-test
EXIT:2

python3 corpus/tools/discriminate_check.py --selftest
error: unrecognized arguments: --selftest
EXIT:2
```

`--help` has no self-test flag. Row's "unavailable; `--selftest` spelling absent" matches. Scope claim (read-only pair of r91 fixtures, not a bible verdict) was not contradicted by the output.

### 3.3 `support_check` — matches on the exits I ran

```
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
RESULT PASS
EXIT:0
```

Exit 1 (`failed`), scratch copy only (`V73-scratch/support-fail/`, one anchor string suffixed so it cannot hit). Live `r98-clerk-filing` was not edited (`git status --short` empty afterwards):

```
FAIL J06: source-support; mode=verbatim; anchor=not-found
FAIL: J06: source-support anchor missing
RESULT FAIL
EXIT:1
```

Exit 2 (`could-not-evaluate`):

```
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing --self-test
error: unrecognized arguments: --self-test
RESULT ERROR
EXIT:2

python3 corpus/tools/support_check.py --selftest corpus/fixtures/r98-clerk-filing
error: unrecognized arguments: --selftest
RESULT ERROR
EXIT:2
```

`--self-test` with no cluster prints `RESULT ERROR` and `the following arguments are required: cluster`, exit 2 — argparse reports the missing positional before the unknown flag. With a cluster, both spellings are unrecognized. No self-test mode. No `support-check-contract.json` beside the three contracts in `corpus/tools/`. The row's "no independent digest/frozen snapshot" is consistent with that; I did not read every line of `support_check.py` to prove it never hashes.

Not replayed this seat: `0 → clean (including warnings)`. Source `support_check.py` prints `RESULT PASS WITH WARNINGS` and returns 0 when warnings exist and failures do not. I did not produce a warnings-only run. Do not treat that clause as re-executed.

### 3.4 `map_obligations` — matches

```
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
EXIT:0

python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS complete exit=0 findings=none
... 25 SELF-TEST PASS lines, including schema_drift, inventory_mismatch, dual_pointer ...
RESULT PASS
EXIT:0

python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT:0

python3 corpus/tools/map_obligations.py --selftest
FINDING invalid_arguments: unrecognized arguments: --selftest
RESULT ERROR
EXIT:2
```

Contract `self_test.cases` is a list of 25 names, the same 25 the run printed. Wrong spelling `--selftest` is absent; `--self-test` is the real flag. Exit 1 finding IDs in the self-test include `missing_obligation`, `duplicate_mapping`, `phantom_obligation`, `source_id_mismatch`, `schema_drift`, `inventory_mismatch`, `dual_pointer`. Exit 2 includes `unsupported_map`, `invalid_pointer`, `snapshot_tampered`, `unpinned`, `frozen_verdict_mismatch`, `invalid_arguments`. That matches the row's `0 → clean`, `1 → failed`, `2 → could-not-evaluate`.

I did not re-prove the r87/r89 `unsupported_map` live exits this seat. The self-test cases `co_mapped_grammar` and `legacy_grammar` printed `exit=2 findings=['unsupported_map']`.

### 3.5 `dependency_freeze` — matches after the late row edit

At poll exhaustion the row was still the `4265df5` text: 17 cases, digests over the five JSON tables, "BR-01's markdown/prose half remains open". That text did not match the tool I had already run. I am not leaving that as the verdict. The row on disk at correction (`SKILL.md:98-100`, SHA-256 `e0bcb61a…`) says 18 cases including `markdown_tamper`, `schema_version` 2 / `payload_schema_version` 2, SHA-256 over all ten declared files, and "any prose edit is detectable, not dependency semantics provable". Those claims match the commands below. S2's report is still ABSENT; the bytes are what I audited.

What I ran on the on-disk tool and contract:

```
python3 corpus/tools/dependency_freeze.py --self-test
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
EXIT:0
```

Contract, parsed at report write: `schema_version` 2, `payload_schema_version` 2, `self_test.expected` length 18, six pins, `pinned_files` the ten names (five JSON + `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`). Each pin's `files` object has those ten keys and `payload_schema_version` 2. Contract scope text says full-file digests of all ten declared files.

Chain named in the row, each `RESULT PASS` exit 0:

```
r88-m3-maya-cluster          DIGEST acf677a7085be3f6… EXIT:0
r94-paired-crossing          DIGEST 048b8ff39e4a5232… EXIT:0
r95-crossing-aftermath       DIGEST 97cffd7bfe6e0c92… EXIT:0
r96-crossing-response        DIGEST 43911900923c110b… EXIT:0
r97-crossing-acknowledgment  DIGEST a28b9ea0d65ec355… EXIT:0
r98-clerk-filing             DIGEST 5ecf84e19121ea12… EXIT:0
```

Independent naming probe, scratch mirror only (`V73-scratch/mirror/`, copy of the 29104-byte tool, the contract, and `r98-clerk-filing`). Clean mirror first printed the same digest `5ecf84e19121ea12…` and `RESULT PASS` exit 0. Then:

```
README.md tamper:
FINDING DIGEST-MISMATCH: content digest 7f5725068f6f9580… != pin 5ecf84e19121ea12…; changed: README.md (sha256 32efc78f70e6de4f… -> 0d0a47be5bccc596…); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT:2

fictional-excerpts.md tamper (README restored from the live file first):
FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80… -> 2e6fa033b4ef9a1d…)
RESULT ERROR
EXIT:2
```

Post-poll re-run, after the live tool became 29110 bytes (`fb9bb9ff…`). Self-test again printed `SELF-TEST 18/18` / `RESULT PASS` / exit 0, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`. `r98-clerk-filing` again printed digest `5ecf84e19121ea12…` / `RESULT PASS` / exit 0. A new scratch copy (`V73-scratch/mirror2/`) with a README append:

```
FINDING DIGEST-MISMATCH: content digest 6261b323e5d5b188… != pin 5ecf84e19121ea12…; changed: README.md (sha256 32efc78f70e6de4f… -> d4848ab8719f8cc4…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT:2
```

The wording clause changed. The exit, the finding id, and the named file did not.

`r99-window-lapse` is not in the row's chain and is not pinned:

```
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' … (pinned: [the six names above])
RESULT ERROR
EXIT:2
```

Against the corrected row: entry command and the six-fixture list match (6/6 exit 0). `0 → clean`. `1 → failed` only with `REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE` in the self-test. `2 → could-not-evaluate` for `DIGEST-MISMATCH` and the other exit-2 ids. Case count 18, including `markdown_tamper`, matches `SELF-TEST 18/18`. Contract parse at correction: `schema_version` 2, `payload_schema_version` 2, 18 expected cases, six pins, each with `payload_schema_version` 2 and the ten declared file keys. `symbolism-clause-map.md` exists under `r88-m3-maya-cluster` (1094 bytes) and is not a pin key.

Unpinned-file probe, scratch only (`V73-scratch/mirror3/`, copy of the 29110-byte tool, the contract, and `r88-m3-maya-cluster`). Clean copy: digest `acf677a7085be3f6…`, `RESULT PASS`, exit 0. After appending a line to `symbolism-clause-map.md` only: same digest, `RESULT PASS`, exit 0. That matches "files outside the declared ten are not pinned". A pinned Markdown append does not: it exits 2 `DIGEST-MISMATCH` and names the file. The finding id is a digest id, not a semantic verdict. I did not run a separate "does the remaining sentence still state the dependency" reading; the tool did not emit one.

Not replayed by this seat: `--freeze` itself (it writes the contract). The row's "re-frozen at r99 through the guarded `--freeze`" is a procedure sentence. The pins verify, and each pin `revision` is `337f0fa52b02626b7687eedbb2d99fab30446fe4` (current HEAD, the blocked-dispatch commit, not a new r99 commit). I do not treat S1's report as proof of the procedure.

## 4. Not done

- S2 and S5 reports: still ABSENT at correction. S1's report exists; I did not grade its narrative.
- No sixth registry row exists; none was invented. `check_bible.py` remains unregistered, as at `4265df5`.
- `support_check` warnings-only exit 0 was not re-executed.
- I did not run `dependency_freeze.py --freeze`.
- `corpus/tools/README.md` changed at 22:51:39. Not audited.
- This seat did not score C1 or C2 and did not promote any SHONEN box.

PASS — SHONEN form holds (four `[~]`, zero `[x]`, checker exit 0); all five named registry rows match commands I ran, including the late freeze-row edit (18 cases, ten-file pins, Markdown tamper exit 2 `DIGEST-MISMATCH` naming the file; unpinned `symbolism-clause-map.md` stays exit 0). No sixth row. S2 report still ABSENT; `--freeze` not replayed by this seat.
