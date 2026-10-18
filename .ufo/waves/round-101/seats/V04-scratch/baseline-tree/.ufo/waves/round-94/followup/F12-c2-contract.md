# F12 — c2-contract (FOLLOW-UP verification seat)

**Role:** audit `corpus/tools/map-obligations-contract.json` (C2 calibration) — persisted-independence of the expectations, absence of a baseline-regeneration path, no network / no live-tree writes / stdlib-only dependencies, and `--self-test` exit-code agreement with the contract on every case.

**Artifacts under audit (sha256, read-only):**

```
cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790  corpus/tools/map_obligations.py
349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50  corpus/tools/map-obligations-contract.json
```

**Scope note:** I wrote no product file. All verification fixtures were built either in `/tmp` or in throwaway temp roots, then deleted (see §6). My only repo write is this report. One incidental untracked, gitignored side effect is disclosed in §6.

---

## 1. Claim: "expectations were persisted independently of the self-test run"

**The named check does not separate the two files.** Both landed in the *same* commit, and neither exists in the parent baseline:

```
$ git log --oneline -3
65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch
b8b50c8 Merge origin/main preserving wiki update and lore training history
abbc3e0 lore r94: checkpoint Luna WORK candidate pending DeepSeek review

$ git log -1 --format='%H %ad %s' -- corpus/tools/map-obligations-contract.json
abbc3e0186c89016d5cbe68b37a2c027bf11d548 Sat Oct 17 15:19:01 2026 -0300 lore r94: checkpoint Luna WORK candidate pending DeepSeek review

$ git log -1 --format='%H %ad %s' -- corpus/tools/map_obligations.py
abbc3e0186c89016d5cbe68b37a2c027bf11d548 Sat Oct 17 15:19:01 2026 -0300 lore r94: checkpoint Luna WORK candidate pending DeepSeek review

$ git show --name-status --format='' abbc3e0 -- corpus/tools/
A	corpus/tools/map-obligations-contract.json
A	corpus/tools/map_obligations.py

$ git cat-file -e 9c2eea3:corpus/tools/map_obligations.py
fatal: path 'corpus/tools/map_obligations.py' exists on disk, but not in '9c2eea3'
$ git cat-file -e 9c2eea3:corpus/tools/map-obligations-contract.json
fatal: path 'corpus/tools/map-obligations-contract.json' exists on disk, but not in '9c2eea3'
```

So `git log -1` is **not** evidence of independence — the tool and its expectations were committed together as one artifact pair. Independence instead rests on the following four observations.

**(a) The tool contains no writer for the contract.** The only references to the contract path are reads and validation failures:

```
$ grep -n 'contract' corpus/tools/map_obligations.py
562:        fail("self_test_contract", f"unknown self-test case {case_name!r}")
575:    contract_path = Path(__file__).resolve().with_name("map-obligations-contract.json")
576:    if contract_path.is_symlink():
577:        fail("self_test_contract", "self-test contract must not be a symlink")
579:        contract = json.loads(contract_path.read_text(encoding="utf-8"))
581:        fail("self_test_contract", f"cannot load self-test contract: {error}")
582:    cases = contract.get("self_test", {}).get("cases") if isinstance(contract, dict) else None
584:        fail("self_test_contract", "contract self_test.cases must be an array")
591:        fail("self_test_contract", "contract contains an invalid self-test expectation")
593:        fail("self_test_contract", "contract repeats a self-test case ID")
596:        fail("self_test_contract", "contract self-test cases do not match the implemented cases")
```

There is no `json.dump(` anywhere in the file (the write helpers use `json.dumps` only, into throwaway fixtures — §3), and no code path constructs or refreshes the contract.

**(b) A missing contract is an error, not a regeneration trigger.** Copied the tool alone into an empty `/tmp` directory and ran `--self-test`:

```
FINDING self_test_contract: cannot load self-test contract: [Errno 2] No such file or directory: '/tmp/f12-nobaseline-6M65/map-obligations-contract.json'
RESULT ERROR
NO_BASELINE_EXIT=2
--- files after run (contract auto-created?) ---
-rw-r--r-- 1 vgpnk vgpnk 28264 Oct 17 15:42 map_obligations.py
```

No contract was created; the run failed closed.

**(c) The contract is authoritative input, falsifiable by mutation** (run against a byte-identical copy of tool+contract in a temp root — `COPY_BYTE_IDENTICAL True`):

```
MUTATED_EXIT_WRONG_EXPECTATION exit= 2 findings= ['FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations'] last= RESULT ERROR
MUTATED_MISSING_CASE exit= 2 findings= ['FINDING self_test_contract: contract self-test cases do not match the implemented cases'] last= RESULT ERROR
```

If the contract were a rubber stamp regenerated from a run, tampering with it could not flip the verdict.

**(d) The contract carries authored metadata no self-test run emits** — `schema_version`, `scope`, `raw_files`, `map_grammar` (section/pointer/source-id column/allowed pointer files), and `exit_codes` (`map-obligations-contract.json:1-23`) — alongside the case table. It is a written contract, not a captured log.

**Corroborating ordering (weak):** contract mtime precedes the tool's last write, consistent with expectations authored before the implementation was finalised.

```
$ stat -c '%n %y' corpus/tools/map-obligations-contract.json corpus/tools/map_obligations.py
corpus/tools/map-obligations-contract.json 2026-10-17 15:01:17.696961714 -0300
corpus/tools/map_obligations.py 2026-10-17 15:04:57.394786234 -0300
```

**Limit of this finding:** "persisted independently of the self-test run" is confirmed in the operationally checkable sense — the expectations are a separate committed input that the tool reads, never writes, and cannot silently refresh. Whether a human/agent consulted a trial run's output while authoring the case table is not observable from the artifacts and is not claimed here. What is excluded is the failure mode that matters: **there is no regeneration path.**

## 2. Claim: "no baseline regeneration path exists in the tool"

Confirmed by §1(a), §1(b), and by the complete CLI surface — four options, none of which writes:

```
$ python3 corpus/tools/map_obligations.py --help
usage: map_obligations.py [-h] [--map MAP] [--frozen FROZEN] [--self-test]
                          [cluster]

options:
  -h, --help            show this help message and exit
  --map MAP             map path within the cluster
  --frozen FROZEN       verify input SHA-256 pins and replay expected.json from this directory
  --self-test           exercise isolated CLI cases
```

The contract path is resolved relative to the script itself (`Path(__file__).resolve().with_name(...)`, line 575) and symlinks are rejected (line 576-577), so there is no environment- or argument-driven way to redirect or rewrite it.

## 3. Claim: "no network, no live-tree writes, no dependencies beyond stdlib"

**Imports — stdlib only.** AST scan of every `import` / `from ... import` in the file:

```
IMPORTS ['argparse', 'collections', 'hashlib', 'json', 'os', 'pathlib', 're', 'subprocess', 'sys', 'tempfile']
NON_STDLIB_IMPORTS none
```

No `socket`, `urllib`, `http`, `requests`, `ssl`, `ftplib`, `smtplib`, `asyncio`, or `xmlrpc` appears anywhere in the file. Runtime confirmation with site-packages disabled:

```
$ python3 -S corpus/tools/map_obligations.py --self-test | tail -3
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
S_EXIT=0
```

**Subprocess use is local self-invocation only.** `subprocess.run` appears once (line 615), launching `[sys.executable, <this file>, ...]` for the isolated self-test cases; no `shell=True` in the file (`grep -n 'shell=True'` → no matches), no external command, no network client.

**Writes are confined to disposable fixture directories, and only on `--self-test`.** Every `write_text` / `write_bytes` / `mkdir` / `unlink` call sits inside `write_test_fixture` (lines 457-484), `prepare_test_frozen` (487-515) and `prepare_test_case` (518-563); the call graph confirms those are reachable only from `run_self_test` (line 608), never from `run_cluster` (324) or `run_frozen` (413):

```
$ grep -nE 'write_test_fixture|prepare_test_frozen|prepare_test_case|run_self_test|run_frozen|run_cluster|subprocess\.run' corpus/tools/map_obligations.py
324:def run_cluster(cluster_value, map_value=None):
413:def run_frozen(value):
457:def write_test_fixture(cluster, rows, pointer_overrides=None):
487:def prepare_test_frozen(case_name, snapshot):
496:    write_test_fixture(snapshot, rows)
518:def prepare_test_case(case_name, cluster):
520:        prepare_test_frozen(case_name, cluster)
524:    write_test_fixture(cluster, rows)
563:    write_test_fixture(cluster, rows, pointer_overrides)
600:def run_self_test():
608:                prepare_test_case(case_name, cluster)
615:                    result = subprocess.run(
674:        return run_self_test()
679:            return run_frozen(args.frozen)
685:        return run_cluster(args.cluster, args.map)
```

**Exact nuance, stated precisely:** the self-test's scratch root is `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` (line 604) where `ROOT` is the repository root (`Path(__file__).resolve().parents[2]`, line 42; observed `ROOT_EQ_REPO True`). So `--self-test` does create a directory *inside the live tree*, but it is a fresh untracked temp directory, removed by the context manager, and nothing under `corpus/` is touched. The `--frozen` and cluster-comparison paths write nothing at all. This is a documented-in-code design consequence of the frozen-snapshot containment check (`resolve_frozen` requires the snapshot to live under `ROOT`, lines 347-350) and it fails if the repo root is read-only; it is not a claim violation, but it is the one place the phrase "no live-tree writes" needs the qualifier "no writes to live *content*".

**Observed cleanliness after every run performed in this seat:**

```
$ git status --porcelain
?? .ufo/waves/round-94/followup/
(end)
$ ls -d map-obligations-self-test-* 2>/dev/null
none_found_exit=2
```

No leftover scratch directories, no modified or new tracked path.

## 4. Claim: "`--self-test` exit codes match the contract file on every case"

**4a — the tool's own self-test, real tool, real repo:**

```
$ python3 corpus/tools/map_obligations.py --self-test
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
RESULT PASS
SELF_TEST_EXIT=0
```

**4b — independent replay, because the above is the tool grading itself.** I rebuilt every case from my own fixtures (different shape from the tool's internal fixture: 2 entities with 1+2 claims, 2 relations, 1 timeline → **7** raw obligations, not the tool's 4), and compared the CLI's real process exit code and FINDING IDs against the contract JSON parsed directly. All 15 non-frozen cases were run against the **real** `corpus/tools/map_obligations.py` with cluster fixtures under `/tmp`. *(Output-fidelity note: the harness printed `MATCH <case> observed_exit=N observed_findings=[...] contract_exit=N contract_findings=[...] results=['RESULT ...'] stderr=''`; the block below collapses the duplicated observed/contract fields into one line per case. Every number and ID shown is verbatim; the `RESULT ...` line and empty stderr were verified on all 15.)*

```
MATCH complete exit=0 findings=none                          (contract 0 / [])
MATCH missing exit=1 findings=['missing_obligation']         (contract 1 / ['missing_obligation'])
MATCH duplicate exit=1 findings=['duplicate_mapping']        (contract 1 / ['duplicate_mapping'])
MATCH phantom exit=1 findings=['phantom_obligation']         (contract 1 / ['phantom_obligation'])
MATCH source_id_mismatch exit=1 findings=['source_id_mismatch'] (contract 1 / ['source_id_mismatch'])
MATCH malformed_json exit=2 findings=['malformed_json']      (contract 2 / ['malformed_json'])
MATCH co_mapped_grammar exit=2 findings=['unsupported_map']  (contract 2 / ['unsupported_map'])
MATCH legacy_grammar exit=2 findings=['unsupported_map']     (contract 2 / ['unsupported_map'])
MATCH invalid_pointer exit=2 findings=['invalid_pointer']    (contract 2 / ['invalid_pointer'])
MATCH empty_segment exit=2 findings=['invalid_pointer']      (contract 2 / ['invalid_pointer'])
MATCH noncanonical_index exit=2 findings=['invalid_pointer'] (contract 2 / ['invalid_pointer'])
MATCH noncanonical_claim_index exit=2 findings=['invalid_pointer'] (contract 2 / ['invalid_pointer'])
MATCH foreign_path exit=2 findings=['foreign_path']          (contract 2 / ['foreign_path'])
MATCH traversal_path exit=2 findings=['unsafe_path']         (contract 2 / ['unsafe_path'])
MATCH symlink_path exit=2 findings=['unsafe_path']           (contract 2 / ['unsafe_path'])
```

Each case also produced exactly one `RESULT` line with the contract-implied word (`RESULT PASS` / `FAIL` / `ERROR`) and empty stderr. The 5 frozen cases require the snapshot to be inside `ROOT`, so they were replayed against a **byte-identical copy** of tool+contract in a temp root (`COPY_BYTE_IDENTICAL True`), with snapshots and `expected.json` I wrote myself (same output-collapsing convention as above; the harness additionally checked `last_line='RESULT ...'` and `stderr=''` per case):

```
MATCH frozen_complete exit=0 findings=none                        (contract 0 / [])
MATCH frozen_tampered exit=2 findings=['snapshot_tampered']       (contract 2 / ['snapshot_tampered'])
MATCH frozen_missing_digests exit=2 findings=['unpinned']         (contract 2 / ['unpinned'])
MATCH frozen_expected_failure exit=1 findings=['missing_obligation'] (contract 1 / ['missing_obligation'])
MATCH frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch'] (contract 2 / ['frozen_verdict_mismatch'])
ALL_CASES_MATCH_CONTRACT True
```

**4c — structural agreement between contract and implementation:**

```
CONTRACT_CASE_COUNT 20
TOOL_CASE_COUNT 20
CASE_ID_SET_EQUAL True
CASE_ORDER_EQUAL True
EXIT_CODES_IN_CONTRACT {'0': 'PASS', '1': 'FAIL', '2': 'ERROR'}  TOOL_RESULTS {0: 'PASS', 1: 'FAIL', 2: 'ERROR'}
```

The contract's 20 case IDs and their order match the implementation's `SELF_TEST_CASES` tuple exactly (`map_obligations.py:19-40`), and the contract's `exit_codes` triple matches `RESULTS` (line 41). The tool also enforces this itself (line 595-596), so a future divergence cannot pass silently.

**4d — bonus, the real committed frozen snapshot replays clean and is not modified by the run:**

```
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
FROZEN_EXIT=0
```

Independently recomputing the four SHA-256 pins against the on-disk bytes gives `pin_match=True` for `entities.json`, `relations.json`, `timeline.json`, and `claim-excerpt-map.md` — the snapshot is genuinely pinned and the run left it untouched.

## 5. What would falsify this audit (and did not)

- A writer for the contract anywhere in the tool → none (`grep -n 'contract'`, no `json.dump`).
- Silent baseline regeneration on a missing contract → refuted: exit 2, `self_test_contract`.
- A contract that cannot fail the tool → refuted: mutated expectation ⇒ exit 2 `self_test_mismatch`; mutated case set ⇒ exit 2 `self_test_contract`.
- Any case whose real exit code differs from the contract → none in 20/20, under both the tool's own harness and my independent fixtures.
- Network or third-party imports → none (AST scan + `python3 -S` pass).
- Live-tree writes → none to tracked content; `git status --porcelain` unchanged across all runs; no leftover scratch dirs.

## 6. Disclosure: my own footprint

- Verification fixtures, the tool+contract copy, and the missing-contract probe were created under `/tmp` (`/tmp/f12-audit-*`, `/tmp/f12-nobaseline-*`) and all were deleted (`ls -d /tmp/f12-*` → nothing).
- Loading the module for introspection caused Python to write `corpus/tools/__pycache__/map_obligations.cpython-314.pyc` (15:42:10). That directory is gitignored (`.gitignore:2: __pycache__/`, confirmed by `git check-ignore -v`) and untracked, so no tracked state changed; I left the directory in place because another seat's `support_check.cpython-314.pyc` (15:41:07) shows concurrent use, and the file is regenerable. No `corpus/` content, no fixture, no other seat's report was read-modified or written.
- Only file written by this seat: `.ufo/waves/round-94/followup/F12-c2-contract.md`.

## 7. Findings not claimed

This audit covers only the contract's persistence, the absence of regeneration, the tool's I/O and dependency envelope, and self-test/contract exit-code agreement. It makes **no** claim about the tool's correctness on live r93/r94 maps, map-grammar coverage beyond the canonical form, textual entailment, R9 mode/fidelity, chronology, rights, or canon — those are outside this seat and are explicitly disclaimed by the tool's own scope string (`map-obligations-contract.json:3`).

---

**Bottom line: PASS** — the contract is a committed, read-only input that the tool can never regenerate (missing ⇒ exit 2 `self_test_contract`; tampered ⇒ exit 2 `self_test_mismatch`), the tool is stdlib-only with no network and no writes to live content (scratch confined to a removed temp dir under `ROOT`), and all 20 `--self-test` cases reproduce the contract's exit codes and FINDING IDs both under the tool's own harness and under my independent replay — with the sole caveat that `git log -1` shows both files added in the same commit `abbc3e0`, so commit separation is not, and does not need to be, the evidence for independence.
