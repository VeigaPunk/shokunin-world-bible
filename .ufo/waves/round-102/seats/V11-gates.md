# V11 — gates-final (round 102)

Seat: V11, verifier. Date: 2026-10-18. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Measured revision: HEAD `8fa2e87b40b74f8f78864b7044ed0345712af605` (r102 declaration);
`git status --short corpus/ SKILL.md LOG.md` → empty (clean), and
`git diff 542021a HEAD --stat -- corpus/` → empty — corpus bytes identical to the r101
closure baseline `542021a`. The battery therefore ran on the delivered revision. No commits, no pushes, no network. Self-test scratch dirs created at repo root are gitignored (`*-self-test-*/`) per contract.

## Battery results — all commands run from lane root

### 1. Freeze self-test — 19/19 PASS

```
$ python3 corpus/tools/dependency_freeze.py --self-test
... (19 CASE lines, each ending `ok`) ...
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
EXIT=0
```

19 cases including the r101 `repointed_edge` case (wrong-but-earlier edge → ADDITION+REDUCTION, exit 1). Matches the SKILL.md registry wording ("19 cases … r101 added `repointed_edge`").

### 2. Chain 8/8 — all RESULT PASS, exit 0

`$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/<fixture>` for each:

| fixture | output line | DIGEST | EXIT |
|---|---|---|---|
| r88-m3-maya-cluster | events 2/2; dependency-edges 0/0; relations 0/0 | acf677a7…96aae | 0 |
| r94-paired-crossing | events 3/3; dependency-edges 2/2; relations 1/1 | 048b8ff3…53ef | 0 |
| r95-crossing-aftermath | events 4/4; dependency-edges 3/3; relations 1/1 | 97cffd7b…0c710 | 0 |
| r96-crossing-response | events 5/5; dependency-edges 4/4; relations 1/1 | 43911900…aa7c | 0 |
| r97-crossing-acknowledgment | events 6/6; dependency-edges 5/5; relations 1/1 | a28b9ea0…1d54 | 0 |
| r98-clerk-filing | events 7/7; dependency-edges 6/6; relations 1/1 | 5ecf84e1…95f0 | 0 |
| r99-window-lapse | events 8/8; dependency-edges 7/7; relations 1/1 | 7fe7e3b0…e470e | 0 |
| r100-docket-review | events 9/9; dependency-edges 8/8; relations 1/1 | 77debadf…325c19 | 0 |

Every fixture: `RESULT PASS`, `EXIT=0`. Eight of eight chain fixtures clean — matches the r101 supersession wording ("exactly the eight chain fixtures … verifying 8/8 clean").

### 3. Map self-test — 25/25 PASS

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
... (25 SELF-TEST PASS lines) ...
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
EXIT=0
```

25/25 including the r95/r96/r97 additions (`schema_drift`, `inventory_mismatch`, `dual_pointer`) and the frozen-snapshot cases (`frozen_tampered` → `snapshot_tampered`, `frozen_verdict_mismatch`).

### 4. Boundary gate — default CERTIFIED + self-test PASS

Default (live document):
```
$ python3 corpus/tools/boundary_doc_check.py
CHECK pinned inputs: PASS
CHECK receipt replay: PASS
CHECK explicit anchor ranges: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
EXIT=0
```

Self-test (capability evidence, isolated temp tree):
```
$ python3 corpus/tools/boundary_doc_check.py --self-test
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2 legacy_anchor=check_bible.py:212-224@5eb9451baff217c19d5786405f9b2aa500b7c1b7 baseline_lines=330
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS comment_parked_c9 exit=1 findings=['document_drift']
SELF-TEST PASS wrong_bare_anchor exit=1 findings=['document_drift']
SELF-TEST PASS checker_drift exit=1 findings=['checker_drift']
SELF-TEST PASS missing_document exit=1 findings=['document_missing']
SELF-TEST PASS missing_checker exit=1 findings=['checker_missing']
SELF-TEST PASS receipt_drift exit=1 findings=['receipt_drift']
SELF-TEST PASS
EXIT=0
```

Both run, as the SKILL.md contract requires (self-test is capability evidence, default is the live certification).

### 5. Discriminate — HELD + e97613c negative control REGRESSION-DETECTED

Delivered checker:
```
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT=0
```

Negative control (expected to fail-closed):
```
$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c ... r91-c1-null-chain ... pinned_semantic_gate=FAIL
... r91-c1-tick-unresolved ... pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT=2
```

Exactly the contract verdicts: valid entry `0 → clean` with `DISCRIMINATION HELD`; negative control `2 → failed` with `REGRESSION-DETECTED`. The expected negative-control failure is not a delivered-run pass (SKILL.md error-signature note respected).

### 6. Checker pin ff9fd2aa — reproduced three ways

- Delivered bytes, independent of the gate: `sha256sum corpus/fixtures/check_bible.py` →
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py`
- Contract pin: `corpus/tools/boundary-doc-contract.json` `/checker/path = corpus/fixtures/check_bible.py`, `/checker/sha256 = ff9fd2aa…d1421`, `/checker/revision = 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`.
- Gate constant: `corpus/tools/discriminate_check.py:12` `PIN = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"`; `:13` `BASELINE = "e97613cc276f5fa9cac49ff1900798cf6863c020"` (the `e97613c` control).
- And `matches_pin=True` reported by the discriminator run itself (item 5). Matches the r101 closure record "checker pin `ff9fd2aa…` reproduced".

### 7. `--frozen` r93 replay — matched

```
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT=0
```

Snapshot digests verified, verdict matched the pinned expectation (`PASS/0`).

## Witness note (non-blocking, outside my byte-ownership)

At run time the producer artifacts `corpus/knowledge/r102-push-synthesis-r95-r102.md`, `r102-debt-ledger.json`, `r102-freshness-sweep.md` were not yet present in `corpus/knowledge/` (grep for `r102` in that directory: no matches). V11's battery is self-contained — it re-measures the six registry gates on the delivered tree and does not depend on producer bytes — so no poll-wait was required and this is recorded as a witness observation, not a verification gap. Sibling seat reports already present at write time: V13-doc.md.

## Per-axis verdicts

- Gate battery (all seven items): improved-not-harmed — every gate green on the delivered revision, including both r101 additions (`repointed_edge` self-test case; 8/8 chain) re-observed live.
- Evidence fidelity: every claim above quotes the observed stdout/exit; the pin is reproduced independently of the gates (sha256sum) and of the gate constants (contract JSON).
- No axis harmed: read-only battery; only gitignored self-test scratch and this seat report written; no commits, no pushes, no network, no producer files touched.

**Bottom line: PASS — all seven gate items green on delivered revision 8fa2e87 (corpus == 542021a): freeze self-test 19/19, chain 8/8, map self-test 25/25, boundary default CERTIFIED + self-test PASS, discriminate HELD with e97613c control REGRESSION-DETECTED (exit 2), checker pin ff9fd2aa…d1421 reproduced three independent ways, --frozen r93 replay matched.**
