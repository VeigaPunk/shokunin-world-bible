# V02 — c1-loader-tight (round 97)

- **Seat:** V02 `c1-loader-tight` (verifier). Report path (only file this seat writes besides scratch): `.ufo/waves/round-97/seats/V02-c1-loader-tight.md` (absolute `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V02-c1-loader-tight.md`).
- **Lane:** lore-shokunin · **Wave:** round-97 single wave (64 seats: 6 producers + 58 verifiers). **Baseline:** r96 closure `f3e09f9` (HEAD `2393934`).
- **Scope (per seat brief):** C1 loader tightening. Subset-tolerance closure — scratch contract copies missing each of 4 cases (one core, `dual_pointer`, `inventory_mismatch`, `map_missing`) must make `--self-test` FAIL closed in every variant; the delivered 25-case contract must pass 25/25. Supplementary: `schema_drift`/`phantom` drops, 23-case double drop, neutralized-emission load-bearing probe, before-state reproduction on the r96 baseline.
- **Scratch (only writes):** `.ufo/waves/round-97/seats/V02-scratch/` (poll log, frozen r96-baseline copies, `crosscheck.py`, `neutralize.py`, `run.sh`, `probe.sh`, variant trees, captures). No commits, no pushes, no network, no nested agents; all commands from the lane repo root with `python3`. Producer byte-ownership untouched (delivered files read-only for this seat; every mutation on scratch copies).

## 0. Poll-wait record — READY at try 15, no ABSENT

Poll `.ufo/waves/round-97/seats/V02-scratch/poll.sh` (20 s cadence, 40 tries; predicate: R1-*.md + R2-*.md regular files, contract 25 cases incl. `dual_pointer`, tool carries a `case_name == "dual_pointer"` prepare branch):

```
18:45:31 try=5 r1=no r2=no contract=[24 False] dqbranch=1
18:46:31 try=8 r1=no r2=no contract=[25 True] dqbranch=1
18:48:31 try=14 r1=no r2=.ufo/waves/round-97/seats/R2-contract-docs.md contract=[25 True] dqbranch=1
18:48:52 try=15 r1=.ufo/waves/round-97/seats/R1-map-pinning.md r2=.ufo/waves/round-97/seats/R2-contract-docs.md contract=[25 True] dqbranch=1
READY try=15 ...
```

Delivered revision pinned by this seat (hashes taken at READY and re-verified after every probe below — unchanged throughout):

| Artifact | sha256 | bytes | mtime |
|---|---|---|---|
| `corpus/tools/map_obligations.py` (R1) | `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` | 38693 | 18:45:37 |
| `corpus/tools/map-obligations-contract.json` (R2) | `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` | 3189 | 18:46:12 |
| `corpus/tools/README.md` (R2) | `6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992` | 24293 | 18:47:13 |

Both producer reports declare the same hashes (R1 §Delivered revision line; R2 §Delivered revision lines 16–18), so there is no revision drift between producer receipts and my runs. The r96-baseline tool copy frozen before R1 landed re-hashes as `2b0ba815…` (r96 pin) and the r96 contract copy as `97b76bb8…` (r96 pin) — the before-state below is on exact r96 bytes.

## 1. Delivered revision — `--self-test` 25/25 PASS, exit 0

Harness `.ufo/waves/round-97/seats/V02-scratch/run.sh` (hash manifest → run → cross-check → manifest):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
exit=0
```

Counts and guards: `pass_lines=25 fail_lines=0 result_lines=1 total_lines=27`, `stderr_bytes=0`; second run byte-identical (`STDOUT_IDENTICAL` / `STDERR_IDENTICAL`). Independent parser (`.ufo/waves/round-97/seats/V02-scratch/crosscheck.py`, own regex over captured stdout, no contract-writing code):

```
contract_cases=25 printed_cases=25 pinned_line=(25, 25)
id_sets_equal=True
MISMATCHES: NONE
RESULT line: ['RESULT PASS']
crosscheck_exit=0
```

Hash/state guard around the runs: `PINS_IDENTICAL`, `GIT_STATUS_IDENTICAL`, self-test residue at repo root `residue_before=0 residue_after=0`.

## 2. Delivered contract 24 → 25 — inherited entries value-identical

Diff of the frozen r96 contract vs the delivered one (scripted comparison, not eyeballed):

```
old n=24 new n=25
inherited id set equal: True
value-changed inherited entries: NONE
added: ['dual_pointer']
old order is subsequence of new order: True
new tail: ['map_missing', 'invalid_arguments', 'dual_pointer']
dual_pointer entry: {'id': 'dual_pointer', 'exit': 1, 'finding_ids': ['dual_pointer']}
top-level keys unchanged
```

The 25th case is appended at the tail; every r96 entry is byte-equal in value. The delivered tool implements it: `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch", "dual_pointer")` (`map_obligations.py:76`).

## 3. Subset-tolerance closure — BEFORE (r96 baseline, frozen copies)

Frozen r96 tool `2b0ba815…` + r96 contract `97b76bb8…` copied to scratch; one case dropped per variant (same mechanics as §4). Reproduced the carried fail-open class:

```
--- r96 variant drop_complete (core) ---        exit=2
FINDING self_test_contract: contract drops implemented self-test cases: complete
RESULT ERROR

--- r96 variant drop_map_missing (core) ---     exit=2
FINDING self_test_contract: contract drops implemented self-test cases: map_missing
RESULT ERROR

--- r96 variant drop_schema_drift (added) ---   exit=0   <- fail open
SELF-TEST CASES 23/24 pinned
... SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS

--- r96 variant drop_inventory_mismatch ---     exit=0   <- fail open
SELF-TEST CASES 23/24 pinned
... SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
RESULT PASS
```

(`dual_pointer` was unpinned at r96, so it cannot be dropped from the r96 contract.) This is the exact r96 tolerance the round closes: core drops failed closed, added-pin drops stayed green.

## 4. Subset-tolerance closure — AFTER (delivered revision): every variant fails closed

Harness `.ufo/waves/round-97/seats/V02-scratch/probe.sh` — for each variant a **byte-identical copy of the delivered tool** sits beside a scratch contract copy with one case removed; only the contract differs (`tool_copy_identical=yes` per variant, `stderr_bytes=0` per variant). Required 4 (one core + three named) plus two supplementary single-drops and one double-drop:

```
=== VARIANT drop_complete ===            exit=2
FINDING self_test_contract: contract drops implemented self-test cases: complete
RESULT ERROR
=== VARIANT drop_dual_pointer ===        exit=2
FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer
RESULT ERROR
=== VARIANT drop_inventory_mismatch ===  exit=2
FINDING self_test_contract: contract drops implemented self-test cases: inventory_mismatch
RESULT ERROR
=== VARIANT drop_map_missing ===         exit=2
FINDING self_test_contract: contract drops implemented self-test cases: map_missing
RESULT ERROR
=== VARIANT drop_schema_drift ===        exit=2
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR
=== VARIANT drop_phantom ===             exit=2
FINDING self_test_contract: contract drops implemented self-test cases: phantom
RESULT ERROR
=== VARIANT drop_two (23-case: schema_drift + dual_pointer) ===  exit=2
FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer, schema_drift
RESULT ERROR
```

Loader source of the closure (`map_obligations.py:820`): `missing = sorted(set(SELF_TEST_CASES) - set(expected))` (r96 line used `set(CORE_SELF_TEST_CASES)`); `SELF_TEST_CASES` = the 25 implemented cases. Every drop fails closed before any case is exercised, naming the dropped case(s), `RESULT ERROR` exit 2. Before→after flip proven for all four required variants (§3 vs §4) and for both r96-added pins that previously stayed green.

## 5. Load-bearing — neutralized `dual_pointer` emission fails the self-test

Scratch copy of the delivered tool, one string substitution at the emission site only (`.ufo/waves/round-97/seats/V02-scratch/neutralize.py`: `gating.append(( "dual_pointer", …` → `gating.append(("dual_pointer_off", …`), delivered contract unchanged (copy byte-identical):

```
$ diff corpus/tools/map_obligations.py variants/neutralize_dual/corpus/tools/map_obligations.py
370,371c370
<                 gating.append((
<                     "dual_pointer",
---
>                 gating.append(("dual_pointer_off",
```

```
$ python3 variants/neutralize_dual/corpus/tools/map_obligations.py --self-test
... 24 × SELF-TEST PASS ...
SELF-TEST FAIL dual_pointer exit=1 findings=['dual_pointer_off']
FINDING dual_pointer_off: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

Removing the behavior turns exactly the pinned case red (24 PASS + 1 FAIL, then `self_test_mismatch`, exit 2) — the persisted pin has teeth.

## 6. Hygiene and final hash guard

- Final re-hash after all probes: tool `86b52949…`, contract `2142b991…`, README `6278e59b…` — identical to the READY pins; `PINS_IDENTICAL` in both harnesses.
- `git status --porcelain` tracked modifications are only producer-owned round files (`corpus/tools/map_obligations.py`, `map-obligations-contract.json`, `README.md`, `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` [R4 repair], `LOG.md` [round declaration]); untracked additions are `.ufo/waves/round-97/` and `corpus/fixtures/r97-crossing-acknowledgment/`. No strays from this seat outside its scratch and report.
- No `map-obligations-self-test-*` residue at the repo root before/after (0/0).
- Non-claims: I verified C1 tool+contract behavior only. The r97 fixture/C2/C3 claims, README prose quality, and R4's repair are other seats' scope; R1's r87–r97 battery and frozen replay were not re-run here (not needed for this seat's claims).

## 7. Observations for the closure pass (not C1 failures)

1. **Doc debt (verified by grep, outside producer byte-ownership):** `SKILL.md:87` still says "24 cases" and records both r96 residuals as open ("`dual_pointer` … not pinned by a persisted case; the two r96-added pins are droppable under the subset-tolerant loader (23/24 still passes) — both r97 debt"); `corpus/README.md:37` still says "24 persisted cases". Both statements are now stale — this seat's §1/§4/§5 show both residuals closed. R2's report flagged the same two files (its §Observations 1). Closure doc pass should update them.
2. R1's report §4.3 recorded the r97 fixture as `raw=17 mapped=16` / `missing_obligation` mid-flight before R5's map landed — observed state at that time, not a regression; not re-verified here.

Bottom line: **PASS** — on the delivered revision (tool `86b52949…`, contract `2142b991…`, both matching producer receipts) `--self-test` is `25/25 pinned` / 25 PASS / `RESULT PASS` exit 0 with clean independent cross-check and byte-identical repeat; scratch contracts dropping each of `complete`, `dual_pointer`, `inventory_mismatch`, `map_missing` (plus `schema_drift`, `phantom`, and a 23-case double drop) all fail closed exit 2 naming the dropped case(s), while the same drops on frozen r96 copies stayed green for the two added pins (the closed tolerance); and neutralizing the `dual_pointer` emission flips exactly that case to FAIL → `self_test_mismatch` exit 2, proving the pin load-bearing.
