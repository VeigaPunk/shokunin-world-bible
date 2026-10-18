# V01 — c1-mismatch-pin (round 98, single-wave)

**Seat scope:** verify `SELF-TEST-MISMATCH` exits 2 (perturb a scratch
expectation → `RESULT ERROR` exit 2, quote; r97 exit-1 form from
`git show 9a3d648` as the before); the new self-test case is pinned and
load-bearing.

Repo root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo). Baseline r97 closure `9a3d648`. Writes
confined to `.ufo/waves/round-98/seats/V01-scratch/` and this report. Leaf
seat: no nested agents, no commits, no pushes, no network.

**Delivered revision under test** (S1 byte-ownership; matches S1's report
`S1-freeze-hygiene.md` lines 9–11 verbatim):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
```

No drift during verification: identical hashes before/after every probe batch
and at the final post-report check. The contract iterated while S1 was still
pinning the C2 chain (first landed revision `3a940a9f…`; the final
`153ebc5b…` adds the r97/r98 pins and a provenance note); the tool bytes were
stable at `03d04365…` throughout. All headline probes were re-run on the final
revision — `.ufo/waves/round-98/seats/V01-scratch/final-run.sh`, one
consistent record (below quotes are from it unless noted).

## Poll record

- 20:27:47 poll start: artifacts absent. 20:31:27: both files present (tool +
  contract changed vs `9a3d648`). First poll exited at 20:32:27 on a
  false-positive match (`S1-scratch` directory matched `^S1`).
- Corrected poll (`.md` only): `S1-freeze-hygiene.md` landed 20:35:41 (try 7).
  Artifacts were verified from 20:31:27 (hash-pinned) and re-verified on the
  final revision after the report; never a plan.

## Check 1 — before: the r97 exit-1 form

```
$ git show 9a3d648:corpus/tools/dependency_freeze.py | sed -n '543,545p'
    if failures:
        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
        return 1
```

Reproduced on the extracted baseline bytes (scratch mirror
`V01-scratch/mirror-baseline`; persisted `clean.exit` corrupted 0→1):

```
PERTURBED clean: exit 0 -> 1
EXIT=1
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
```

Consistent with r97 V09's P1 (same probe, exit 1) and r97 V37 NB-18 (freeze
tool `emit(1)` at `:544` vs sibling `map_obligations.py` exit 2).

## Check 2 — after: exit 2 on the delivered bytes

Delivered form (`corpus/tools/dependency_freeze.py:571-573`):

```
    if failures:
        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
        return 2
```

Primary probe (final-run §A): byte-copy mirror of the delivered tool+contract;
persisted expectation `clean.exit` 0→1 in the scratch contract; run
`--self-test`:

```
EXIT=2
CASE clean: exit=0 expected=1 findings=[] MISMATCH
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
```

The other 16 cases print `ok` in the same run — the new convention is the
only delta. Positive controls: unperturbed delivered mirror → `SELF-TEST
17/17` / `RESULT PASS` / exit 0; real tree → `python3
corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 17/17` /
`RESULT PASS` / exit 0, all 17 case lines end `ok`.

## Check 3 — the new case is pinned

- Case-set parity: tool `FROZEN_CASES` n=17, contract `self_test.expected`
  n=17, sets identical (`identical=True`); the only new key is
  `self_test_mismatch` with expectation `{"exit": 2, "finding_ids":
  ["SELF-TEST-MISMATCH"], "forbid_traceback": true}`.
- Fail-closed on a dropped pin, both directions:
  - removed from the contract →
    `FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['self_test_mismatch'] extra=[]` / `RESULT ERROR` / exit 2;
  - removed from `FROZEN_CASES` →
    `… missing=[] extra=['self_test_mismatch']` / `RESULT ERROR` / exit 2.
- The 16 inherited expectations are programmatically equal to the r97
  contract's (`inherited cases with changed expectation: []`; no dropped
  keys).
- The case construction (`dependency_freeze.py:515-527`) corrupts only the
  scratch mirror's contract copy; the delivered contract's `clean.exit`
  remains 0 (read back, `exit: 0`).

## Check 4 — the new case is load-bearing

- Neutralization (final-run §D): delivered bytes with the emit/return reverted
  to the r97 form (`emit(1)` + `return 1`) in a mirror:

```
EXIT=1
CASE self_test_mismatch: exit=1 expected=2 findings=['SELF-TEST-MISMATCH'] MISMATCH
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']
RESULT FAIL
```

The suite goes red on exactly the persisted case when the C1 fix regresses —
the pin is wired to the behavior, not decorative.
- Expectation flip (final-run §E): `self_test_mismatch.exit` 2→1 →
  `CASE self_test_mismatch: exit=2 expected=1 … MISMATCH` / exit 2 — the
  persisted value is actually compared.
- Non-vacuity: the case observes a real nested process exit (probe D changes
  it). The nested scenario was independently reproduced by hand — probe A is
  the same construction (corrupt a scratch `clean.exit`, run `--self-test` →
  exit 2 + `SELF-TEST-MISMATCH`) and matches the persisted expectation.

## Context and observations (not my claim)

- Sibling alignment target confirmed: `corpus/tools/map_obligations.py:877-879`
  prints `FINDING self_test_mismatch` / `RESULT ERROR` / `return 2`.
- Transient `dependency-freeze-self-test-*` dirs appear under the repo root
  during concurrent seat self-test runs and vanish within seconds (observed
  twice; none persisted); they are covered by `.gitignore:4`
  (`*-self-test-*/`). BR-05 residual unchanged, as S1 notes.
- `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (parent tree) exists;
  not mine (S3's report attributes it to an unattributed seat). Recorded, not
  touched.

## Bottom line

**PASS** — on the drift-checked delivered revision (tool `03d04365…`, contract
`153ebc5b…`, matching S1's declared hashes): a perturbed scratch expectation
yields `RESULT ERROR` exit 2 (r97 form `emit(1)`/`return 1` → exit 1 quoted as
the before); the new case `self_test_mismatch` is pinned in both
`FROZEN_CASES` and the contract (drop → `CONTRACT-INVALID` exit 2 either
direction) and load-bearing (r97-form neutralization reds exactly that case;
expectation flip reds it too); the 16 inherited cases are unchanged; real-tree
`--self-test` 17/17 `RESULT PASS` exit 0.
