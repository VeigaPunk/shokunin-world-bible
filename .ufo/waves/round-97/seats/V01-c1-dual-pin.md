# V01 — c1-dual-pin (round 97, single-wave swarm)

Seat: V01, verifier for **C1/calibration — `dual_pointer` persisted pin**. Lane:
`/home/vgpnk/Projects/shokunin/lore-shokunin` (all commands run there unless
noted; baseline r96 closure `f3e09f9`). Poll target: R1 (`corpus/tools/map_obligations.py`)
+ R2 (`corpus/tools/map-obligations-contract.json`). No commits, no pushes, no
network, no nested agents. Scratch:
`.ufo/waves/round-97/seats/V01-scratch/` (poll.sh, battery.sh, pertA/A0/B/C/D/E,
cluster, r96/r96b).

## 0. Poll result

`poll.sh` (20 s cadence): `try=10 … R1report=0 R2report=2` → `try=11 … R1report=1`
→ `POLL-LANDED` (18:48:51). Landed reports: `R1-map-pinning.md` (13291 B),
`R2-contract-docs.md` (7433 B). Verified revision, digests re-checked before and
after every probe (unchanged):

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

Both digests match those quoted by R1 (`86b52949…`, `2142b991…`) and R2
(`2142b991…`). `stat`: tool 18:45:37, contract 18:46:12 (pre-report, stable
across my whole session).

## 1. Contract: 25 cases incl. `dual_pointer`

```
$ python3 - <<'PY'
import json
d=json.load(open('corpus/tools/map-obligations-contract.json'))
c=d['self_test']['cases']; print("cases:",len(c)); print("ids:",",".join(x['id'] for x in c))
print("dual_pointer entry:",json.dumps([x for x in c if x['id']=='dual_pointer']))
PY
cases: 25
ids: complete,missing,duplicate,phantom,source_id_mismatch,schema_drift,inventory_mismatch,malformed_json,co_mapped_grammar,legacy_grammar,invalid_pointer,empty_segment,noncanonical_index,noncanonical_claim_index,foreign_path,traversal_path,symlink_path,frozen_complete,frozen_tampered,frozen_missing_digests,frozen_expected_failure,frozen_verdict_mismatch,map_missing,invalid_arguments,dual_pointer
dual_pointer entry: [{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}]
```

Delta vs the r96-committed contract (`git show f3e09f9:…`), programmatic:

```
r96 cases: 24 r97 cases: 25
added: ['dual_pointer'] removed: []
changed expectations: NONE
non-self_test sections identical: True
```

`python3 -m json.tool corpus/tools/map-obligations-contract.json` → valid.
Tool side: `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch", "dual_pointer")`
(line 76) → `SELF_TEST_CASES` = 25 implemented cases (line 77);
`prepare_test_case` branch lines 732–734 builds the legacy-dialect fixture
(`legacy_test_rows()` + `DUAL_POINTER_CELL`, lines 639–649).

## 2. `--self-test` on the delivered revision: 25/25 PASS

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS complete exit=0 findings=none
… (24 PASS lines) …
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
exit=0
```

(Full 26-line output captured in `V01-scratch/r97-self.out`; the delivered run
above is verbatim.)

**Independent non-regression diff** (not relying on R1's claim): r96 tool+contract
extracted from `f3e09f9` into scratch and replayed:

```
$ diff <(grep '^SELF-TEST' r96-self.out) <(grep '^SELF-TEST' r97-self.out)
1c1
< SELF-TEST CASES 24/24 pinned
---
> SELF-TEST CASES 25/25 pinned
25a26
> SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
```

r96 run: `SELF-TEST CASES 24/24 pinned` … `RESULT PASS`, exit 0. So the only
difference across the whole self-test surface is the header and the one added
`dual_pointer` PASS line — the 24 inherited cases are outcome-identical.

## 3. The pin is load-bearing (perturbations in scratch)

### 3a. Direct real-input probe (delivered tool)

Hand-built legacy dual-pointer cluster (same shape as `prepare_test_case`'s
fixture; `.ufo/waves/round-97/seats/V01-scratch/cluster`):

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-97/seats/V01-scratch/cluster
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
exit=1
```

Exactly the pinned expectation (exit 1, `['dual_pointer']`).

### 3b. Perturbation A — neutralize the emission (scratch tool copy)

Patch applied to `V01-scratch/pertA/corpus/tools/map_obligations.py` (anchor count
asserted = 1): `if mention is not None:` → `if False:  # V01 perturbation: neutralize dual_pointer emission`
(line 369 of the delivered file).

Same cluster, perturbed tool — the capability really is gone:

```
OBLIGATIONS raw=4 mapped=4
RESULT PASS
exit=0
```

Perturbed `--self-test` (raw log `V01-scratch/A.out`):

```
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=0 findings=none
OBLIGATIONS raw=4 mapped=4
RESULT PASS
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

**Control A0** — the same scratch copy *unperturbed* (tool + contract, nothing
else changed): `SELF-TEST CASES 25/25 pinned` … `SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']` …
`RESULT PASS`, exit 0. So the failure in A is attributable to the perturbation,
not to the scratch relocation.

### 3c. Perturbation B — scratch contract drops the `dual_pointer` case

```
cases 25 -> 24 (dropped dual_pointer)
$ python3 corpus/tools/map_obligations.py --self-test
FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer
RESULT ERROR
exit=2
```

### 3d. Perturbation C — expectation flip (exit 1 → 0, findings → [])

```
SELF-TEST FAIL dual_pointer exit=1 findings=['dual_pointer']
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

So both halves of the pin (the expected exit/finding list **and** the emission)
are load-bearing.

### 3e. Loader tightening — ANY missing pinned case now fails

- Perturbation E (delivered tool, contract minus a **core** case `complete`):
  `FINDING self_test_contract: contract drops implemented self-test cases: complete`,
  `RESULT ERROR`, exit 2.
- Pre-state reproduction (r96 tool + r96 contract minus r96-added pin
  `schema_drift`, unmodified bytes from `f3e09f9`):
  `SELF-TEST CASES 23/24 pinned` … `RESULT PASS`, **exit 0** — the documented
  r96 tolerance, independently reproduced.
- Pre-fix blindness to the new pin (r96 tool + delivered contract minus
  `dual_pointer`): `SELF-TEST CASES 24/24 pinned` … `RESULT PASS`, exit 0.

This closes C1(b): the delivered loader (line 820, `set(SELF_TEST_CASES) - set(expected)`)
fails on any dropped pinned case; the r96 revision passed a 23-case contract.

## 4. Discrepancies observed (evidence hygiene; non-blocking)

1. R1 report table row `neutralized-live25` (`R1-map-pinning.md:56`) quotes
   `SELF-TEST FAIL dual_pointer exit=1 findings=[]`. My independent reproduction
   of the same patch is `SELF-TEST FAIL dual_pointer exit=0 findings=none`
   (perturbation A). The tool prints `none` for an empty finding list and an
   exit-1 result cannot carry zero findings, so `exit=1 findings=[]` is not a
   producible output. R1's headline claim (case fails → `RESULT ERROR`, exit 2)
   is confirmed; the child-exit detail in that table row is a transcription slip.
   R1's raw log (`scratch-R1/probes.txt:39-`) elides the line with `…`, so their
   exact observed child exit cannot be re-read from their artifacts; my value is
   direct.
2. `scratch-R1/probes.txt` section header
   `=== baseline-drop-schema — 24 cases: schema_drift dropped, r96 tool — exit=2 ===`
   actually contains `FINDING self_test_contract: contract pins unimplemented self-test cases: dual_pointer`
   — i.e. that section ran the **r96 tool against the live 25-case contract**, not
   the described variant. Labeling mismatch in R1's scratch log; it does not
   affect my findings (I reproduced the r96 baseline row myself in §3e).

Neither discrepancy touches the delivered artifacts, whose bytes are stable and
whose behavior I verified directly.

## 5. Non-claims / scope

- Verified: the `dual_pointer` pin, its load-bearing property, the loader
  tightening, and inherited-case outcome stability. I did **not** verify the
  r87–r97 fixture battery, the frozen-r93 replay, or r87/r89 fail-closed runs
  (other seats), nor any C2 (`dependency_freeze`) or C3 (r97 fixture) claim.
- No stray writes: everything I wrote is under
  `.ufo/waves/round-97/seats/V01-scratch/` and this report; `git status` shows
  no change to `corpus/tools/` attributable to V01 (digests unchanged across the
  session).

## Bottom line

**PASS** — delivered `map_obligations.py` `86b52949…` + contract `2142b991…`: 25 cases with the `dual_pointer` pin, `--self-test` 25/25 `RESULT PASS` exit 0, and the pin proven load-bearing three ways (emission neutralization → case FAIL / exit 2; contract drop → `self_test_contract` / exit 2; expectation flip → case FAIL / exit 2), with the r96 23/24-exit-0 hole independently reproduced as the closed pre-state.
