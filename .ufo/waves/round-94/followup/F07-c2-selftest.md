# F07 — c2-selftest (verification seat, r94 FOLLOW-UP wave)

**Seat:** F07 · **Role:** c2-selftest — independent verification of the C2 calibration tool `corpus/tools/map_obligations.py` and its persisted contract `corpus/tools/map-obligations-contract.json`.

**Claim under test:** `--self-test` exits 0 with 20/20 real-CLI cases; the persisted expected exits/FINDING IDs match what the self-test prints, without regenerating anything; the self-test writes nothing to the live tree.

**Bottom line: PASS** — all three sub-claims hold under direct observation; two concurrency caveats noted at the end (neither is a defect in the tool).

---

## 1. Self-test runs clean: exit 0, 20/20 cases

```
$ python3 corpus/tools/map_obligations.py --self-test; echo "EXIT=$?"
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
EXIT=0
```

Repeated 3× sequentially (`/tmp/F07-run{1,2,3}.out`), each run: `exit=0`, `passes=20`, `fails=0`, last line `RESULT PASS`. Observed `stderr` was empty and no `Traceback` appeared.

The cases are **real CLI invocations**, not in-process calls — `map_obligations.py:615` runs `subprocess.run([sys.executable, str(Path(__file__).resolve())], cwd=ROOT, ...)` once per case inside the loop at `map_obligations.py:606`. `SELF_TEST_CASES` (`map_obligations.py:19`) holds exactly 20 ids, matching the 20 printed lines.

## 2. Persisted contract matches printed exits/FINDING IDs — independently parsed

Contract read directly: `corpus/tools/map-obligations-contract.json` (48 lines) declares `self_test.cases` with 20 entries, each carrying `id`/`exit`/`finding_ids` (lines 26–45), plus `exit_codes` 0=PASS / 1=FAIL / 2=ERROR (lines 19–23).

I parsed the contract and the tool's stdout **separately** and compared them rather than trusting the tool's own verdict:

```
contract cases: 20 | printed SELF-TEST lines: 20
case-id sets equal: True
exit/finding mismatches: NONE
all lines verdict PASS: True
RESULT line: ['RESULT PASS']
stderr empty: True
process exit: 0
```

Zero mismatches on exit codes and FINDING-ID lists across all 20 cases. The tool also enforces this both ways itself: it refuses to run if the contract's case set differs from the implemented cases (`map_obligations.py:595`, `"contract self-test cases do not match the implemented cases"`), and per case requires `returncode == expectation["exit"]`, exact finding-id list equality, exactly one `RESULT` line, empty stderr, and no `Traceback` (`map_obligations.py:628–635`).

## 3. Nothing was regenerated

The contract was **not** rewritten by any run — it is byte-identical to the version committed at the round checkpoint:

```
$ sha256sum corpus/tools/map-obligations-contract.json
349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50  corpus/tools/map-obligations-contract.json

$ git show abbc3e0:corpus/tools/map-obligations-contract.json | sha256sum
349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50  -

$ git diff --stat HEAD -- corpus/tools/map-obligations-contract.json
(empty)
```

Its mtime is `2026-10-17 15:01:17 -0300`, which predates every run I performed (15:38–15:41). `git log` for the file shows a single commit, `abbc3e0`. So the expectations are persisted, pre-existing data, and the self-test reads them (via `load_test_expectations`, `map_obligations.py:574–597`) rather than deriving them from live output.

## 4. The self-test writes nothing to the live tree

Tight before/after windows (hash → run → hash inside one shell call), 3 sequential runs:

```
BEFORE corpus=24f2b0ab07c7e7af10f3c3ce56061cda02901824aeb4a4531dbc84dca55d1526  whole=4c03086bf1dd9a29d2afcf94ecbe4dd69745fc211d13c2e5a6c2a0e19c068bc7
run1 exit=0 last=RESULT PASS passes=20 fails=0   stray-after-2s: 0 dirs
run2 exit=0 last=RESULT PASS passes=20 fails=0   stray-after-2s: 0 dirs
run3 exit=0 last=RESULT PASS passes=20 fails=0   stray-after-2s: 0 dirs
AFTER  corpus=24f2b0ab07c7e7af10f3c3ce56061cda02901824aeb4a4531dbc84dca55d1526  whole=4c03086bf1dd9a29d2afcf94ecbe4dd69745fc211d13c2e5a6c2a0e19c068bc7
```

Both `corpus/` and whole-tree hashes are bit-identical across the runs. Supporting checks:

- `git status --porcelain` after all runs: only `?? .ufo/waves/round-94/followup/` (the follow-up wave's own report directory) — no tracked content changed anywhere in the repo.
- No leftover temp directories: `ls -d map-obligations-self-test-*` → `NONE` after each run's 2-second settle.
- File-list diff of `corpus/` before vs after the first run: identical (1781 entries).

The self-test does write transiently *inside* the repo, which is worth recording: `map_obligations.py:604` uses `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` with `ROOT = Path(__file__).resolve().parents[2]` (`map_obligations.py:42`) — i.e. the repository root. Fixtures are built there and removed by the context manager on exit; three consecutive runs left zero residue. So "writes nothing to the live tree" holds in the sense of **no persistent mutation**, with the honest caveat that per-case fixtures exist under the repo root for the duration of a run.

## 5. Caveats observed (environment concurrency, not tool defects)

- **My own probe caused one stray artifact, now removed.** To enumerate `SELF_TEST_CASES` I ran `python3 -c "import map_obligations"`, which made CPython write `corpus/tools/__pycache__/map_obligations.cpython-314.pyc` (45131 bytes, 15:39). That file was created by my probe, not by `--self-test` (running a script as `__main__` is not byte-cached), and it is gitignored (`git check-ignore` → `.gitignore:2:__pycache__/`). I deleted it to restore the as-found state. The same path reappeared at `15:42:10` (after my deletion, my last import being 15:39) — i.e. from another seat importing the module, which is itself confirmation that this artifact class tracks concurrent seat activity rather than the self-test. It remains gitignored and untracked; I did not remove another seat's artifact.
- **Other concurrent seats perturb naive whole-tree hashing.** A `corpus/tools/__pycache__/support_check.cpython-314.pyc` (15:41) and an in-flight `map-obligations-self-test-9f7uvbhs/` directory appeared during my session from other seats running their own tools. The stray dir disappeared within ~1s of polling and no Python processes were running afterwards, confirming it was a concurrent seat's in-flight temp dir rather than a leak from my runs. Because of this I excluded `__pycache__` and `map-obligations-self-test-*` from the stability hashes above; the `corpus/`-scope hash and `git status` are the decisive, concurrency-immune evidence.

**Bottom line: PASS** — `--self-test` exits 0 with 20/20 real-CLI cases (verified over 4 total runs), my independent parse of the printed exits/FINDING IDs matches all 20 persisted contract expectations with zero mismatches, the contract is byte-identical to its `abbc3e0` committed state and was never regenerated, and repeated runs left `corpus/` and the whole tree hash-identical with no leftover temp dirs.
