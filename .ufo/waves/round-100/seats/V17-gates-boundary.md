# V17 — gates-boundary (round 100)

Seat scope: boundary default + self-test; delivered discriminator plus historical control; checker pin reproduction; no boundary-pinned byte change. Axes: calibration (bounded certification and real negative controls), operability (CLI replay), preservation/adjacency (byte identity), freshness (post-producer measurement). This is a seat verdict, not round-wide admission or independent certification of C1/C2/C3.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python commands used `python3`. Baseline: `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. Verified worktree HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, a descendant containing the r100 declaration; the wave changes were uncommitted. No nested agents, commits, pushes, or network.

Writes were limited to this exclusive report and declared scratch `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V17-scratch/`. Scratch contains `poll.py`, `poll.log`, `poll-status.json`, `replay.py`, `early/` and `final/` raw stdout/stderr/metadata and pin audits, two deliberate drift copies and their receipts, plus an empty `tmp/`. No corpus file was edited. `TMPDIR` pointed into the declared scratch for both boundary self-tests; their temporary trees were automatically removed. Dynamic imports disabled bytecode writes.

## 1. Producer readiness and bounded local correction

Actual poll commands:

```sh
python3 .ufo/waves/round-100/seats/V17-scratch/poll.py > .ufo/waves/round-100/seats/V17-scratch/poll.log 2>&1
python3 .ufo/waves/round-100/seats/V17-scratch/poll.py >> .ufo/waves/round-100/seats/V17-scratch/poll.log 2>&1
```

The first poll was deliberately stopped after attempt 1 to correct verifier-local schema assumptions: the ten-file fixture contains `contradictions.json`, not `world-rules.json`, and the freeze contract stores `pins`, not `fixtures`. Attempt 1 therefore falsely listed a missing `world-rules.json` and missing r99 pin; those were polling errors, not producer defects. The corrected poll used Read/Edit and resumed at attempt 2, preserving the 40-attempt cap. The interruption caused a bounded 46.152-second gap between attempts 1 and 2; subsequent attempts slept 20 seconds. This local stall/correction is recorded, not treated as a corpus failure or an ABSENT verdict.

Observed poll excerpts (`poll.log`; JSON lines shortened to the relevant recorded fields):

```text
try=1  time=2026-10-18T02:32:38.969935+00:00 missing_reports=[T1,T2,T3,T4]
POLL-RESUME after local schema correction; next_try=2
try=2  time=2026-10-18T02:33:25.121451+00:00 missing_artifacts=[r100-crossing-arc-synthesis.md,r100-provenance-semantics-boundary.md] missing_reports=[T1,T2,T3,T4]
try=8  time=2026-10-18T02:35:25.125571+00:00 missing_artifacts=[r100-crossing-arc-synthesis.md] missing_reports=[T3,T4]
try=19 time=2026-10-18T02:39:05.133343+00:00 missing_artifacts=[] missing_reports=[T4]
try=23 time=2026-10-18T02:40:25.136424+00:00 missing_artifacts=[] missing_reports=[] ready=true
POLL-READY try=23
```

Corrected readiness required all ten r100 fixture files, both new r100 knowledge records, the r99 blind-spot table, the r99 pin in `contract.pins`, and all four producer reports. Present and read before this report:

- `.ufo/waves/round-100/seats/T1-chain-seven.md`
- `.ufo/waves/round-100/seats/T2-fixture-author.md`
- `.ufo/waves/round-100/seats/T3-fixture-docs.md`
- `.ufo/waves/round-100/seats/T4-knowledge-author.md`

No all-reports/self-inclusive poll was used. No producer plan was accepted as a delivered artifact, no readiness cap was exhausted, and no required background task remains.

## 2. Post-delivery replay

Actual batched command, exit 0:

```sh
python3 .ufo/waves/round-100/seats/V17-scratch/replay.py final
```

The scratch harness ran the following four real CLI calls concurrently, with before/after pin audits. Final replay/audit window: `2026-10-18T02:40:28.931098+00:00` through `2026-10-18T02:40:30.193915+00:00`, after the ready poll. Complete per-command stdout, stderr and exact argv/exit timestamps are under `V17-scratch/final/`.

### Boundary default

```text
$ python3 corpus/tools/boundary_doc_check.py
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
[rc=0; stderr_bytes=0]
```

### Boundary self-test

```text
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
[rc=0; stderr_bytes=0]
```

Eight persisted cases passed: seven CLI cases plus the direct anchor-range control. `committed_default` internally checks `replay_cases=14/14`. The control's 220-line delivered checker is synthetic; the legacy 330-line checker is the real historical blob. Self-test capability evidence does not replace the separate live default certification.

### Delivered discriminator

```text
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
[rc=0; stderr_bytes=0]
```

### Historical regression control

```text
$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
[rc=2; stderr_bytes=0]
```

The valid control's result text plus exit 2 is an expected detected regression, not a gate execution failure. Exit 2 alone would be insufficient because argparse syntax failures also use 2. `checker_sha256`/`matches_pin=True` describe the delivered file in both modes; they do not claim that the historical source has the delivered hash. The distinct historical blob was independently hashed below.

Harness terminal output, verbatim:

```text
V17-SUMMARY {"checks": {"after_pins": true, "before_pins": true, "boundary-default": true, "boundary-self-test": true, "boundary_text": true, "control_text": true, "discriminate-control": true, "discriminate-held": true, "held_text": true, "self_test_text": true, "stable_during_run": true}, "pass": true, "path_count": 96, "phase": "final"}
```

## 3. Pin reproduction and no boundary-pinned byte change

`replay.py final` reads the persisted boundary contract, parses the discriminator's literal `PIN`/`BASELINE`, and SHA-256-hashes live bytes and `git show` blobs. It enumerates the pinned document's actual replay commands, then compares every scoped file with both `fe1ce46` and HEAD. Full path-by-path hashes and equalities are in `final/before-pins.json` and `final/after-pins.json`.

Observed final audit fields (excerpts of the harness's actual before/after JSON output):

```text
baseline=fe1ce466e9d7427948c0abe4ecfbf961880b72ff
head=b5fe472957ab1e4e9c90f5613acc14cd24a288ae
baseline_is_ancestor=true
path_count=96
bad_paths=[]
three_way_checker_match=true
legacy_match=true
control_is_distinct=true
scoped_git_status=""
scoped_diff_baseline=""
```

Reproduced hashes:

```text
checker   ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
document  7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e
legacy    88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81
control   e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
```

- Checker: boundary `checker.sha256` = discriminator `PIN` = worktree hash = blob at `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`.
- Document: contract pin = worktree hash = blob at that same pinned revision.
- Legacy checker: blob at `5eb9451baff217c19d5786405f9b2aa500b7c1b7` matches `legacy_baseline_sha256`.
- Regression control: blob at `e97613cc276f5fa9cac49ff1900798cf6863c020` is distinct from the delivered checker. This is not the boundary contract's legacy-anchor revision.

The 96-path preservation set comprises:

- Five core files: `corpus/tools/boundary_doc_check.py`, `corpus/tools/boundary-doc-contract.json`, `corpus/tools/discriminate_check.py`, `corpus/fixtures/check_bible.py`, `corpus/knowledge/holder-assessment-boundary.md`.
- All 79 files in the 14 replay fixture directories extracted from the pinned document.
- All 12 files in the two discriminator fixture directories, not only their READMEs.

Every path equals both r99 closure and HEAD; the contract itself was not retargeted. Its SHA-256 remains `e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871`. The audit also includes any additional files appearing inside those fixture directories, so an untracked addition would not silently escape its comparison/status checks.

The same four commands ran earlier with `python3 .ufo/waves/round-100/seats/V17-scratch/replay.py early` at `02:33:25–02:33:26Z`. An explicit Python byte comparison of `.stdout` and `.stderr` and equality comparison of the pin-audit records observed:

```text
EARLY-FINAL BYTE-IDENTICAL boundary-default
EARLY-FINAL BYTE-IDENTICAL boundary-self-test
EARLY-FINAL BYTE-IDENTICAL discriminate-held
EARLY-FINAL BYTE-IDENTICAL discriminate-control
PIN-PATHS 96 bad 0 same_baseline_and_HEAD=True stable_early_to_final=True
```

## 4. Live override controls — scratch only

Each target was first copied byte-identically into this seat's scratch. Read/Edit then appended one HTML comment to the document copy and appended `raise RuntimeError('V17 changed checker must not execute')` to the checker copy. The real live gate was run against each changed override in parallel; no live pinned input changed.

Actual commands and complete observed outputs:

```text
$ python3 corpus/tools/boundary_doc_check.py --doc .ufo/waves/round-100/seats/V17-scratch/document-drift.md
CHECK pinned inputs: FAIL
FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes
CERTIFICATION FAIL
[rc=1; stderr_bytes=0; expected_failure=True]
$ python3 corpus/tools/boundary_doc_check.py --checker .ufo/waves/round-100/seats/V17-scratch/checker-drift.py
CHECK pinned inputs: FAIL
FINDING checker_drift: delivered checker digest differs from the committed pin
CERTIFICATION FAIL
[rc=1; stderr_bytes=0; expected_failure=True]
LIVE-OVERRIDE-CONTROLS 2/2 PASS; modified checker not executed
```

Measured at `2026-10-18T02:37:25.108178+00:00` and `02:37:25.108301+00:00`; raw stdout/stderr/command metadata are in the corresponding `document-drift.*` and `checker-drift.*` scratch receipts. Both intentional failures demonstrate the earlier byte guard, not semantic or anchor-range validation. The final 96-path audit ran afterward and remained clean.

## Bounds and handoff

- Boundary certification covers frozen-document identity, receipt replay, explicit numeric anchor ranges, and limited structure only; it is not semantic/AST validation, testimony truth, chronology authentication, source authenticity, rights, permission, or canon.
- The discriminator's held result is specific to the two durable r91 fixtures and its pinned historical differential. It is not a general checker-correctness proof.
- This seat independently replayed only its assigned boundary/discriminator gates. Reading all producer reports establishes readiness, not independent verification of their C1/C2/C3 assertions.
- Preservation is measured for the 96 enumerated dependencies at the quoted delivered-tree times; later edits require a fresh replay. No round-wide tests/build claim is made.
- The only unexpected issue was the disclosed verifier-local first-poll schema error; it was corrected without resetting the cap or changing producer bytes. There were no unresolved gate errors or missing producer artifacts/reports at final verification.

PASS — after all four producer reports landed (poll 23), boundary default CERTIFIED rc=0 with receipts 3/3, cases 14/14 and anchors 2/2; self-test 8/8 rc=0; delivered discrimination HELD rc=0 and distinct historical control REGRESSION-DETECTED rc=2; checker pin ff9fd2aa…d1421 reproduced; all 96 boundary/discriminator paths match fe1ce46 and HEAD; both scratch-only byte-drift controls fail closed as expected.
