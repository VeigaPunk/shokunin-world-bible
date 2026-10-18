# V17 — gates-boundary (round 95)

- Seat: V17 gates-boundary. Round 95, single wave, baseline r94 closure `fb118c4`.
- Repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from repo root with `python3`.
- Observed tree: `HEAD = fb118c42038ed27a747eec704b9aab41bb4b2ebe` (= baseline). Window: 2026-10-17 16:17–16:28 local.
- Scope under test: boundary gate certification, discrimination gate behavior, and pinned-byte integrity across the r95 round.

## 1. Primary commands and observed outputs

### 1.1 `python3 corpus/tools/boundary_doc_check.py`

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
EXIT=0
```

Run twice; stdout byte-identical both times (exit 0/0) → deterministic.

### 1.2 `python3 corpus/tools/boundary_doc_check.py --self-test`

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
EXIT=0
```

8/8 cases PASS; the control case confirms the legacy anchor is resolved against baseline revision `5eb9451b` (330 lines).

### 1.3 `python3 corpus/tools/discriminate_check.py`

```
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT=0
```

### 1.4 `python3 corpus/tools/discriminate_check.py --checker e97613c`

```
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT=2
```

`e97613c` = r89 closure commit (`lore r89: closure — verdicts ruled…`); its `check_bible.py` blob sha256 is `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556` (differs from delivered `ff9fd2aa…`). Note the tool prints `checker_sha256` of the *delivered* working-tree checker in both modes (`matches_pin=True`), not of the e97613c blob — read the mode field, not the hash, when interpreting the control run.

### 1.5 Checker pin hash

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Matches the seat's required value exactly.

## 2. Pin integrity — r95 changed no pinned byte

Boundary contract `corpus/tools/boundary-doc-contract.json` pins three byte classes. Observed at end of window:

| Pin class | Pin | Observed | Verdict |
|---|---|---|---|
| document `corpus/knowledge/holder-assessment-boundary.md` | sha256 `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e` @ rev `65838f86…` | working tree `7f815a93…`; `git cat-file blob 65838f86…` also `7f815a93…` | MATCH |
| delivered checker `corpus/fixtures/check_bible.py` | sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` @ rev `65838f86…` | working tree `ff9fd2aa…`; blob @ `65838f86…` also `ff9fd2aa…` | MATCH |
| legacy checker @ `5eb9451baff217c19d5786405f9b2aa500b7c1b7` | sha256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` | `git cat-file blob 5eb9451b…:corpus/fixtures/check_bible.py \| sha256sum` → `88c9b1d0…`; blob id `46472f33…` | MATCH |

Both pinned revisions are ancestors of HEAD (`git merge-base --is-ancestor … HEAD` → YES).

Round-drift check against baseline:

```
$ git diff --stat fb118c4 -- corpus/knowledge/holder-assessment-boundary.md corpus/fixtures/check_bible.py
(empty; rc=0)
$ git status --porcelain -- corpus/knowledge/holder-assessment-boundary.md corpus/fixtures/check_bible.py
(empty)
```

600 s integrity watcher (scratch script, `scratch/V17/watch.log`): sampled the document hash, checker hash, `git status` digest, fixture/knowledge-note presence, and the three tool-surface hashes every 20 s for the full round window. Result: **13 distinct change points, every one with `doc_pin_ok=1 chk_pin_ok=1`; zero `_pin_ok=0` samples**. The window includes the concurrent producer writes: P1's `map_obligations.py` changed 9 times (`cc1df4dc…` → `28d308be…` → `85c237c3…` → `ca05159e…` → `52d838b0…` → `8eb5051d…` → `3f87fe8b…` → `9224a684…` → `d1c239cc…`), P2's `map-obligations-contract.json` landed at t=600 s (`349a1956714c…` → `0a6438ab07d9…`), P3/P4 fixture files and P5's `r95-aftermath-scope-note.md` appeared (`fx=no→yes` t≈60 s, `kn=no→yes` t≈360 s). Pinned hashes were constant at every sample. The full gate battery was re-run once more immediately after the window closed (after P2's contract landed): all four commands returned the same exit codes/outputs as §1.

Caveat (explicit): the watcher covers t≈0–600 s of the round; writes after the window are not observed by it. At handoff the round was still in flight (P1 still iterating `map_obligations.py`; its hash changed twice in the last 20 s of the window). No declared producer ownership includes any pinned path.

## 3. Adversarial controls (own scratch copies, `.ufo/waves/round-95/seats/scratch/V17/`)

- 1-byte flip in a copy of the document (`sha256 e94733fa…` vs pin `7f815a93…`), run with `--doc <copy>`:
  `CHECK pinned inputs: FAIL` / `FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes` / `CERTIFICATION FAIL`, `EXIT=1`.
- Appended line to a copy of the checker, run with `--checker <copy>`:
  `CHECK pinned inputs: FAIL` / `FINDING checker_drift: delivered checker digest differs from the committed pin` / `EXIT=1`.

Both gates fail closed on tampered inputs, so the exit-0 receipts above are meaningful rather than vacuous.

## 4. Cross-checks and observations

- Receipt counts independently reproduced: the document contains exactly 3 fenced blocks carrying receipt markers (`VIOLATION:`/`CLEAN:`/` violation(s); no canon changed`) with 5+6+3 = 14 `[rc=…]` wrappers, matching `replay_receipts=3/3 replay_cases=14/14`.
- Anchors counted by the gate are exactly the 2 full `check_bible.py:NNN` citations: doc line 78 `check_bible.py:212-224` (legacy revision anchor) and doc line 111 `check_bible.py:184` (delivered); both resolve → `anchors=2/2`. The bare `:277`/`:290` citations on line 111 are not counted by the gate's `ANCHOR` regex (`boundary_doc_check.py:35`).
- Reading trap for other seats: the contract's `self_test.expected.anchor_range_control.delivered_line_count=220` is a *synthetic* control input (`boundary_doc_check.py:555` builds `b"control line\n" * 220`), not the real delivered checker, which is 428 lines. The delivered anchor `:184` and legacy `:212-224` both resolve in their real files.
- Transient artifact observed and gone again: `map-obligations-self-test-pevhytt0/` appeared at repo root during a concurrent `map_obligations.py --self-test` run. Source: `map_obligations.py:618` uses `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`; it is cleaned up on exit. Observation only; no pinned byte involved.
- Gate-script hashes at the observed revision (for receipt reproducibility): `boundary_doc_check.py` `ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053`, `discriminate_check.py` `6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef`, `boundary-doc-contract.json` `e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871` (unmodified in `git status`).
- No failures or contradictions found in this seat's scope.

Bottom line: PASS — boundary gate CERTIFIED exit 0 (self-test 8/8), discrimination HELD exit 0 vs REGRESSION-DETECTED exit 2 on e97613c, `check_bible.py` sha256 `ff9fd2aa…d1421`, and all three pinned byte classes unchanged across the r95 round window (600 s watcher: 13 change points, 0 pin violations; `git diff fb118c4` on pinned paths empty).
