# V12 — gates-boundary (round 101)

Seat: V12 gates-boundary · Round: r101 (28 seats, glm-5.3-flash-low) · Baseline: r100 closure `6f86bf2` (HEAD `ebec6bb` declaration) · Date: 2026-10-18

Axes: (A1) boundary default run clean · (A2) boundary self-test suite passes · (A3) HELD vs e97613c control discrimination · (A4) checker pin ff9fd2aa reproduced · (A5) no boundary-pinned byte changed.

All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with python3. No clarifying rounds; single parallel batch.

## A1 — boundary default run: PASS

Command: `python3 corpus/tools/boundary_doc_check.py`

Observed (exit 0):

```
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
[rc=0]
```

## A2 — boundary self-test: PASS

Command: `python3 corpus/tools/boundary_doc_check.py --self-test`

Observed (exit 0) — all 8 checks (anchor_range_control + 7 cases) pass, final `SELF-TEST PASS`:

```
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2 legacy_anchor=check_bible.py:212-224@5eb9451baff217c19d5786405f9b2aa500b7c1b7 baseline_lines=330
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS comment_parked_c9 exit=1 findings=['document_drift']
SELF-TEST PASS wrong_bare_anchor exit=1 findings=['document_drift']
SELF-TEST PASS checker_drift exit=1 findings=['checker_drift']
SELF-TEST PASS missing_document exit=1 findings=['document_missing']
SELF-TEST PASS missing_checker exit=1 findings=['checker_missing']
SELF-TEST PASS receipt_drift exit=1 findings=['receipt_drift']
SELF-TEST PASS
[rc=0]
```

Note: this is the boundary tool's own self-test (7+1), distinct from the dependency_freeze 18→19 count in C3 (U1's axis; not re-verified here).

## A3 — discrimination HELD + e97613c control: PASS

Command: `python3 corpus/tools/discriminate_check.py` (delivered)

```
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
[rc=0]
```

Command: `python3 corpus/tools/discriminate_check.py --checker e97613c` (control)

```
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
[rc=2]
```

The control behaves as designed: under baseline selection the delivered-semantics gate FAILs on both fixtures and the gate fires REGRESSION-DETECTED with exit 2 — a silent revert to `e97613c` would be caught. Delivered run: HELD, exit 0.

## A4 — checker pin ff9fd2aa reproduced: PASS

Command: `sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md`

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

Both match `corpus/tools/boundary-doc-contract.json` pins exactly (checker `ff9fd2aa…d1421`, document `7f815a93…c33e`). The discriminator's `matches_pin=True` independently confirms the same digest at runtime.

## A5 — no boundary-pinned byte changed: PASS

Boundary set: `corpus/fixtures` (incl. `check_bible.py`, r91 pair), `corpus/live/runs/round-85` (receipt replay inputs), `corpus/knowledge/holder-assessment-boundary.md`, `corpus/tools/boundary_doc_check.py`, `corpus/tools/boundary-doc-contract.json`, `corpus/tools/discriminate_check.py`.

Command: `git status --short -- <boundary set>` → empty (no uncommitted modifications vs HEAD).
Command: `git diff --stat 6f86bf2 -- <boundary set>` → empty output, `[diff-rc=0]` — byte-identical to the r100 closure baseline.

Also: the A1/A2 runs exercise the pinned bytes directly (digest check inside the tool: PASS), so worktree, HEAD, and `6f86bf2` all carry the pinned bytes.

## Per-axis verdicts

| Axis | Verdict |
|---|---|
| coverage (boundary gate intact, 14/14 receipts, 2/2 anchors) | improved/not harmed |
| calibration (self-test 8/8 incl. adversarial cases + anchor-range control) | not harmed |
| operability (discrimination HELD; control fires exit 2 as pinned) | not harmed |
| boundary pins (ff9fd2aa checker, 7f815a93 doc) | reproduced, zero drift vs 6f86bf2 |

One execution note (not a finding): the session cwd defaults to the parent `/home/vgpnk/Projects/shokunin`; the first batch of relative-path invocations failed with rc=2 (`No such file or directory`) and was rerun with the lane root as cwd — quoted outputs above are all from the lane root.

**Bottom line: PASS — boundary default run 14/14 receipts + self-test 8/8 exit 0; DISCRIMINATION HELD with e97613c control firing REGRESSION-DETECTED exit 2; checker pin ff9fd2aa… and doc pin 7f815a93… reproduced; boundary set byte-identical to r100 closure 6f86bf2.**
