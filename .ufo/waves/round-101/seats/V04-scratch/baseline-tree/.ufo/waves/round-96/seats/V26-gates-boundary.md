# V26 — gates-boundary (round 96)

**Seat:** V26 `gates-boundary`. Scope: the two repo-level boundary gates and the
C9 checker pin, as delivered at round 96 — (1) `boundary_doc_check.py` default
run PASS, (2) `boundary_doc_check.py --self-test` PASS, (3)
`discriminate_check.py` default → `DISCRIMINATION HELD` exit 0, (4)
`discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED` exit 2
(expected control), (5) checker pin `ff9fd2aa…` reproduced, (6) no pinned byte
changed this round.

**Report path (only file written by this seat):** this file. Scratch:
`.ufo/waves/round-96/seats/V26-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V26-scratch/`).
No commit, no push, no network, no nested agents.

**Baseline:** r95 closure `dcb2d92`. `git rev-parse HEAD` at report time →
`60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 close — SCORECARD admitted
section; `dcb2d92..HEAD` touches `SCORECARD.md` only). Python 3.14.7. All
commands run from the lane repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`.

**Note on target availability:** all five verification targets are
pre-existing artifacts from earlier rounds (nothing is owned by an r96
producer), so no poll-wait was required; every run below was executed against
the live tree and re-executed after the one mid-check corpus landing (§6).

## 0. Pinned bytes at report time (final re-check 2026-10-17T17:41:00-0300)

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871  corpus/tools/boundary-doc-contract.json
6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef  corpus/tools/discriminate_check.py
```

The first hash is the C9/contract pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`;
the second is the boundary contract's `document.sha256`; the fourth is the
discriminator itself (not pinned by any contract, recorded for the round).

## 1. `boundary_doc_check.py` default — exit 0, all four CHECKs PASS

```
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
$ echo $?
0
```

stderr bytes: 0 (captured to `V26-scratch/bd.out` / `bd.err`). The receipt
replay is a live re-execution: `replay_receipts()` in
`corpus/tools/boundary_doc_check.py:249` runs `python3 corpus/fixtures/check_bible.py <path>`
for every checker command block in the frozen document and byte-compares
stdout, return code, and empty stderr — 3 blocks, 14 fixture cases, all
matched.

## 2. `boundary_doc_check.py --self-test` — exit 0, 8/8 cases PASS

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
$ echo $?
0
```

stderr bytes: 0; `grep -c 'SELF-TEST PASS'` = 9 lines (8 case lines + the
final summary line). The 8 case names are exactly the
`self_test.expected` keys in `corpus/tools/boundary-doc-contract.json`
(committed_default, comment_parked_c9, wrong_bare_anchor, checker_drift,
missing_document, missing_checker, receipt_drift, anchor_range_control) — no
persisted expectation is unexercised and no exercised case is undeclared.
`committed_default` additionally asserts `replay_cases=14/14` per the contract.

## 3. Discriminator pair — HELD exit 0 / control exit 2

```
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
$ echo $?
0
```

```
$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
$ echo $?
2
```

stderr bytes: 0 for both modes. Both runs reproduce the row-4 reading recorded
in `corpus/knowledge/r91-c9-watch.md:271` (r95 row: DISCRIMINATION HELD /
`e97613c` control REGRESSION-DETECTED, "Next re-check: r96") — this is that
re-check, and the reading holds at r96. The control feeds the historical
checker source via `git show e97613c:corpus/fixtures/check_bible.py`
(`BASELINE` = `e97613cc276f5fa9cac49ff1900798cf6863c020`, verified to be a
commit object in this repo), so the control exercises real historical bytes,
not a paraphrase; `baseline_README_exact=True` on both fixtures confirms the
fixtures' pinned `e97613c` expectation blocks still describe those bytes
exactly. In both modes the delivered checker's own hash is printed as
`ff9fd2aa…` `matches_pin=True`.

## 4. Checker pin `ff9fd2aa…` reproduced — three independent methods

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py

$ python3 -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('corpus/fixtures/check_bible.py').read_bytes()).hexdigest())"
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421

$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"; \
  echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"; \
  echo "dcb2d92 blob: $(git rev-parse dcb2d92:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
dcb2d92 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
```

The hash equals the pin in `corpus/tools/discriminate_check.py:12`, in
`corpus/tools/boundary-doc-contract.json` `checker.sha256`, and in
`corpus/knowledge/r91-c9-watch.md:6`. The blob identity
`20c56dbb…` is the same object at baseline `dcb2d92`, at `HEAD`, and in the
working tree, so the pinned bytes are byte-identical across all three views.

## 5. No pinned byte changed this round

```
$ git status --porcelain -- corpus/
?? corpus/fixtures/r96-crossing-response/

$ git diff --stat HEAD -- corpus/fixtures/check_bible.py \
  corpus/knowledge/holder-assessment-boundary.md corpus/tools/boundary-doc-contract.json \
  corpus/tools/discriminate_check.py corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved
(empty output; rc=0)

$ git diff --stat dcb2d92..HEAD -- corpus/fixtures/check_bible.py \
  corpus/knowledge/holder-assessment-boundary.md corpus/tools/boundary-doc-contract.json \
  corpus/tools/discriminate_check.py corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved
(empty output; rc=0)
```

Tracked corpus content is unchanged versus `HEAD`, and `dcb2d92..HEAD` is
`SCORECARD.md` only (32 insertions, from the r95 closure commit `60dba0c`).
The single untracked corpus entry is the C2 producer's new fixture directory
(not a pinned artifact, and not read by either gate: the boundary receipt
replay names explicit fixture paths, and the discriminator reads only
`r91-c1-null-chain` / `r91-c1-tick-unresolved`).

Ownership-disjointness, stated explicitly: the round's producer-owned paths
(`map_obligations.py`, `map-obligations-contract.json`, `tools/README.md`,
`dependency_freeze.py`, `dependency-freeze-contract.json`,
`fixtures/r96-crossing-response/`, `knowledge/r96-response-scope-note.md`) do
not intersect the pinned set read by either gate
(`check_bible.py`, `holder-assessment-boundary.md`, `boundary-doc-contract.json`,
`discriminate_check.py`, and the two r91 fixture directories). At report time
`corpus/tools/map_obligations.py` and its contract still carry their r95
revision (mtimes 16:26/16:27, pre-round) — i.e. no r96 producer has yet
rewritten a tracked file at all.

## 6. Mid-check landing re-verification, and one environment anomaly

Between my first pass (17:37–17:39) and the final pass (17:41) the C2 producer
landed `corpus/fixtures/r96-crossing-response/` (8 files: contradictions,
entities, relations, sources, timeline, inspiration-note, source-excerpt,
fictional-excerpts — no README/claim-excerpt-map yet, those are Q5's). Both
gates were re-run after that landing and their stdout is **byte-identical** to
the pre-landing runs (`diff -q` clean on both captures), exit codes unchanged
(0 / 0). Nothing in the new directory perturbs either gate.

Environment anomaly (reported because it silently fails scratch writes):
`/tmp` is inode-exhausted on this host.

```
$ df -i /tmp | tail -2
Filesystem      Inodes   IUsed IFree IUse% Mounted on
tmpfs          1048576 1048576     0  100% /tmp

$ python3 corpus/tools/boundary_doc_check.py > /tmp/v26_bd.out
/bin/bash: line 1: /tmp/v26_bd.out: No space left on device
```

`df -h` shows 8.5G free, so the failure is inode exhaustion, not bytes; a
redirected command still "runs" but the capture file is never created and the
shell reports exit 1. All my captures were therefore written to
`V26-scratch/` under the lane repo (782G free). Any r96 seat that redirects
output to `/tmp` may be reading an artifact of this, not of the tools.

## Bounds

- This seat verifies the two repo-level gates and the checker pin only. It
  makes no statement about C1/C2/C3 claim content, the new fixture's substance,
  the census, or the discriminator's ability to catch anything other than the
  two pinned r91 fixture classes.
- "No pinned byte changed this round" is a point-in-time confirmation
  (17:41:00-0300) plus the ownership-disjointness argument above; a later
  producer write outside its declared byte-ownership would not be caught by
  this report. The gate commands are cheap (0.4 s / 1.1 s / 0.1 s each) and can
  be re-run at closure as the final check.
- The boundary gate's `CERTIFIED` string is itself bounded by the tool's own
  scope line (frozen-document drift + receipts + anchors + structure; no
  semantic/AST validation) — quoted here with that scope, not as a general
  correctness claim.
- `/tmp` inode exhaustion is an environment observation on this host at this
  time; I did not investigate its cause or clean it (destructive, out of
  scope, other seats may be using it).

**Bottom line: PASS** — `boundary_doc_check.py` default exit 0 (4/4 CHECKs, receipts 3/3, cases 14/14) and `--self-test` exit 0 (8/8 persisted cases); `discriminate_check.py` exit 0 `DISCRIMINATION HELD` with the `e97613c` control exit 2 `REGRESSION-DETECTED`; checker pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` reproduced by three methods and blob-identical at `dcb2d92`/`HEAD`/worktree; no pinned byte changed this round.
