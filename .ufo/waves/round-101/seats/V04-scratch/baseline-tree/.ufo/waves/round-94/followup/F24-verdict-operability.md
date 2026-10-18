# F24 — verdict-operability (r94 FOLLOW-UP, independent per-axis verdict)

**Seat:** F24 — verdict-operability.
**Role:** independent per-axis verdict for OPERABILITY of the r94 WORK candidate: new gate default/self-test runnable, documented commands replay, exit-code contract honored.
**Bounds:** phase-structure validation only. No admission, no capability row, no whole-claim/source-support verdict. Operability of the delivered artifacts only; nothing here is entailment, fidelity, chronology, rights, permission or canon evidence (that limit is the tool's own declared scope, `corpus/tools/map-obligations-contract.json` `"scope"`).
**Verified revision:** checkpoint `abbc3e0` (HEAD at check time `65a9329`), Python 3.14.7, all commands run from the repo root.
**Scratch:** none written in the repo. All mutation controls ran in `/tmp/f24-scratch` (removed at the end; every command below is replayable from this report). No `corpus/`, report, registry or fixture byte was modified by this seat; no commit was made.

## 0. What I ran the verdict against (revision identity)

Working-tree bytes are the committed checkpoint bytes, so the results below describe `abbc3e0`, not an uncommitted edit:

```
$ git hash-object corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
5801192b60f2905356ec6802f757d36dd58d2f25
e26574ad36706594f732f8819f66dc706e537141
$ git rev-parse abbc3e0:corpus/tools/map_obligations.py abbc3e0:corpus/tools/map-obligations-contract.json
5801192b60f2905356ec6802f757d36dd58d2f25
e26574ad36706594f732f8819f66dc706e537141
$ git diff --stat abbc3e0 HEAD -- corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
(empty — unchanged since checkpoint)
```

Content digests for pinning: tool `sha256=cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790`, contract `sha256=349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50`, r94 map `sha256=ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47`.

`git status --short` before and after every run below showed only `?? .ufo/waves/round-94/followup/` (this follow-up directory itself) — no product path was dirty at any point.

## 1. Default invocation is runnable (both documented fixtures)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
RESULT PASS            EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS            EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing --map claim-excerpt-map.md
OBLIGATIONS raw=14 mapped=14
RESULT PASS            EXIT=0
```

Default map resolution is bounded and fail-closed (`MAP_CANDIDATES`, `corpus/tools/map_obligations.py:16`; `resolve_map` requires exactly one conventional map). Negative controls in `/tmp` copies:

```
no map file present  -> FINDING map_missing: expected exactly one conventional claim-to-excerpt map      EXIT=2
both candidate names -> FINDING unsupported_map: expected exactly one conventional claim-to-excerpt map  EXIT=2
```

Both r93 and r94 resolve cleanly under the default form, which is the form the LOG/SCORECARD commands use.

## 2. `--self-test` is runnable, real-CLI, and expectation-driven

```
$ python3 -B corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS            EXIT=0
```

- Re-run produced byte-identical output (`identical=yes`), exit 0 both times.
- 20 cases, all through the **real CLI**: `run_self_test` builds each case in a temp directory and invokes `subprocess.run([sys.executable, <tool path>, ...])` (`corpus/tools/map_obligations.py:604`, `:615`), not in-process helper calls.
- Expectations are **persisted and consumed, not regenerated**: `load_test_expectations` reads `map-obligations-contract.json` (`:574–575`); the contract's 20 case IDs equal the implemented 20 (`contract_cases= 20`, `implemented_cases= 20`, `sets_equal= True`, `order_equal= True`).
- Positive control that the self-test can fail (isolated `/tmp` copy of tool + contract, one expected exit flipped 0→1 for `complete`):

```
SELF-TEST FAIL complete exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR            EXIT=2
```

- Fail-closed on a missing contract (isolated copy, contract moved away): `FINDING self_test_contract: cannot load self-test contract: [Errno 2] No such file or directory: ...` / `RESULT ERROR` / `EXIT=2`. Restoring the pristine contract (digest `349a1956…`) returned `RESULT PASS`, `EXIT=0`.

## 3. Documented commands replay (round records)

Documented set: `LOG.md:2669` and `SCORECARD.md:374`, against the wave-spec CLI contract at `.ufo/waves/round-94/wave-spec.md:27`.

| Documented command | Observed | Exit |
|---|---|---|
| `python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` | `OBLIGATIONS raw=12 mapped=12` / `RESULT PASS` | 0 |
| `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` | `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` | 0 |
| `python3 -B corpus/tools/map_obligations.py --self-test` | 20/20 `SELF-TEST PASS`, `RESULT PASS` | 0 |
| `python3 -B corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` | 0 |
| `python3 .ufo/waves/round-94/work/W02-unmapped-demo.py` | `support_check exit=0 terminal=['RESULT PASS']` / `map_obligations exit=1 findings=['FINDING missing_obligation: entities.json#/0/claims/1 has no map row'] terminal=['RESULT FAIL']` / `counterexample=PASS` | 0 |
| `python3 .ufo/waves/round-94/work/W02-frozen-demo.py` | `frozen_baseline exit=0 terminal=['RESULT PASS']` / `mutated_copy exit=2 finding=['FINDING snapshot_tampered: missing, unsafe, or digest-mismatched inputs: entities.json'] terminal=['RESULT ERROR']` / `mutation_to_tamper=PASS` | 0 |

Frozen pins independently recomputed (not taken from the tool's own output) — `sha256sum` of the snapshot inputs equals `expected.json` field-for-field:

```
19f75678…d2d1d entities.json    32b79cd4…e46d relations.json
69da079e…17e2 timeline.json     17f0e812…f7d6 claim-excerpt-map.md
```

The LOG/SCORECARD claim "20 real-CLI isolated controls", "12/12", "14/14", "four digests verified, expected PASS/0/[] matched" all match what I observed. The historical exit-2 event the round records (first r94 invocation → `unsupported_map` from header labels, repaired by W01; `LOG.md:2669`) is consistent with my replay: the delivered map passes, and the grammar path really does return 2 (my own legacy-grammar control below).

## 4. Exit-code contract honored

Spec: `0` clean / `1` failed comparison / `2` could-not-evaluate, one terminal RESULT line, stable FINDING IDs (`.ufo/waves/round-94/wave-spec.md:27`). Implementation mapping `RESULTS = {0: "PASS", 1: "FAIL", 2: "ERROR"}` (`corpus/tools/map_obligations.py:41`) agrees with the contract file's `exit_codes`.

Sweep of 14 invocations (exit / RESULT-line count / FINDING-line count / traceback count / stderr bytes):

```
r93 default                  exit=0 RESULT_lines=1 FINDING_lines=0 traceback=0 stderr_bytes=0
r94 default                  exit=0 RESULT_lines=1 FINDING_lines=0 traceback=0 stderr_bytes=0
r94 --map explicit           exit=0 RESULT_lines=1 FINDING_lines=0 traceback=0 stderr_bytes=0
no-arg                       exit=2 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
missing cluster              exit=2 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
self-test                    exit=0 RESULT_lines=1 FINDING_lines=0 traceback=0 stderr_bytes=0
frozen                       exit=0 RESULT_lines=1 FINDING_lines=0 traceback=0 stderr_bytes=0
live fail missing            exit=1 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
live fail dup                exit=1 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
live fail sid                exit=1 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
live fail phantom            exit=1 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
live err malformed           exit=2 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
live err legacy              exit=2 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
misuse self-test+cluster     exit=2 RESULT_lines=1 FINDING_lines=1 traceback=0 stderr_bytes=0
```

The four live `1` cases and three live `2` cases were produced by mutating **copies** of the r94 fixture in `/tmp` (live fixtures untouched):

```
missing raw claim added      -> OBLIGATIONS raw=15 mapped=14 / FINDING missing_obligation: entities.json#/0/claims/1 has no map row      EXIT=1
duplicated map row           -> OBLIGATIONS raw=14 mapped=15 / FINDING duplicate_mapping: entities.json#/0/first_appearance appears 2 times EXIT=1
source-ID cell rewritten     -> OBLIGATIONS raw=14 mapped=14 / FINDING source_id_mismatch: entities.json#/0/first_appearance does not bind to 'paired-clock' EXIT=1
non-obligation pointer row   -> OBLIGATIONS raw=14 mapped=15 / FINDING phantom_obligation: entities.json#/0/name is not a raw source-attributed obligation EXIT=1
entities.json truncated to `{` -> FINDING malformed_json: cannot parse entities.json: Expecting property name enclosed in double quotes: line 1 column 2 (char 1) EXIT=2
pointer rewritten to legacy `entities[0].claims[0]` -> FINDING unsupported_map: co-mapped or unsupported pointer grammar EXIT=2
```

Additional exit-2 boundaries: `--self-test` combined with a cluster, `--frozen` combined with a cluster, and a frozen snapshot outside the repository (`FINDING unsafe_path: frozen snapshot must be inside the owning repository`) all return 2. `--help` returns 0. So the wave-spec's "unsupported grammar / malformed JSON / invalid paths must be could-not-evaluate, never an empty successful inventory" is honored in live runs, not only in self-test cases.

## 5. No live-tree writes

- Corpus byte manifest (every non-`__pycache__` file under `corpus/`, `sha256` of sorted per-file digests) identical across the three documented runs: `84970936fcd6d6bf95d6bd800688e64fdb3f4812e88a2c03f42c68cb32d9897a` before and after.
- WORK directory listing hash identical before/after the two demo scripts (their temp dirs self-clean): `772b78d3258639ae6448a867a759ea1b` both times.
- Repo root after all runs: `find . -maxdepth 1 -name 'map-obligations-self-test-*' | wc -l` → `0`; `git status --short` → only `?? .ufo/waves/round-94/followup/`.

## 6. Bounds, disclosed construction errors, residual observations

1. **Two of my own mutation controls were mis-built; the tool was right, not wrong.** (a) My first "source-ID mismatch" edit replaced the row's *anchor* cell, not the source-ID cell — the tool correctly still returned `RESULT PASS` (it parses only the pointer and source-ID columns of the `## JSON facts` table). (b) My first replacement also landed outside the parsed section (r94 map headings: `## R9 excerpt declarations` line 7, `## JSON facts` line 16, `## Editorial rows` line 37), so it was correctly ignored. The corrected in-section column-3 edit produced the exit-1 `source_id_mismatch` shown above; moving a fact row into the editorial section produced exit 1 `missing_obligation` (`raw=14 mapped=13`). Both errors are recorded here rather than smoothed over.
2. **Self-test scratch lives under the repo root.** `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` (`map_obligations.py:604`). Normal exit removes it (verified in the live repo and in an isolated `/tmp` copy of the tool: `leftover_after_normal=0`). A `kill -9` mid-run leaves one untracked directory: isolated-copy experiment `kill_exit=137`, `leftover_after_kill=1`, path `map-obligations-self-test-g6nbxjr7` (I removed it in `/tmp`). At the repo root I observed one such directory transiently (`./map-obligations-self-test-upaladkg` at 2026-10-17T18:41:0xZ, gone by 18:41:4xZ) — consistent with a concurrent follow-up seat's in-flight run; I do not attribute it to a tool defect and my own completed runs left zero. The name is **not** gitignored (`.gitignore` = `.ufo/interactive-sessions/`, `__pycache__/`), so a killed run can leave an untracked path in the repo root. Minor, non-blocking, named here as a residual.
3. **Documentation surface is the round records only, for now.** `grep -rn "map_obligations" corpus/README.md corpus/tools/README.md` → exit 1, no match; the tool index at `corpus/README.md:33` still lists only `support_check.py`, `discriminate_check.py` and the boundary-document checker. The commands are documented in `LOG.md:2669` and `SCORECARD.md:374`, and SCORECARD's `planned:` block already carries "integrate W25's minimal docs/registry proposals" as pending FOLLOW-UP work. So "documented commands replay" holds against the round's own records; the README/registry entry is a declared-pending item, not a delivered claim.
4. **Environment/surface:** Python 3.14.7; imports are stdlib only (`argparse, hashlib, json, os, re, subprocess, sys, tempfile, collections.Counter, pathlib` — `map_obligations.py:4–13`), no socket/urllib/HTTP import, no third-party dependency, no network call in any path I exercised. The tool also runs from a non-repo cwd with absolute paths (`cd /tmp && python3 <abs tool> <abs cluster>` → `RESULT PASS`, exit 0).
5. **What this verdict is not:** exit 0 says the raw obligations are mapped one-to-one with matching source IDs. It says nothing about textual entailment, R9 mode/fidelity, source authentication, chronology truth, rights, permission or canon — and nothing about C1's claims, which are other seats' axes. No admission or capability row is asserted by this seat.

**Bottom line: PASS** — at checkpoint `abbc3e0` the new r94 gate's default run and `--self-test` are runnable, every command documented in `LOG.md:2669`/`SCORECARD.md:374` replays with the recorded result, and the 0/1/2 exit-code contract is honored live in all three branches (one terminal RESULT line, stable FINDING IDs, empty stderr), with the only residuals being a repo-root self-test scratch directory that survives `kill -9` and the still-pending README/registry entry.
