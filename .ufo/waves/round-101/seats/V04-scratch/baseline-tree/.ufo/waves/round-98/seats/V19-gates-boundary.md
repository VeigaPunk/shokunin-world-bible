# V19 — gates-boundary (round 98)

Seat: V19 gates-boundary. Lane: lore-shokunin. All commands run from
`/home/vgpnk/Projects/shokunin/lore-shokunin/`. No nested agents, no commits,
no pushes, no network. Only this report and `V19-scratch/` were written.

Seat scope: (a) `boundary_doc_check.py` default + `--self-test`;
(b) `discriminate_check.py` DISCRIMINATION HELD + `e97613c` control;
(c) checker pin `ff9fd2aa…` reproduced; (d) no pinned byte changed
(boundary contract pins).

## 1. Boundary gate — default run

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
[rc=0]
```

Receipt enumeration (instrumented via import of the tool, same revision as the
run above):

```
receipt fence line=355 command line=346 cases=[r85-control, r85-unique-break-control, r85-masked-ambiguous, r85-isolated-ambiguous, r85-harbor-repro]
receipt fence line=406 command line=400 cases=[r88-mixed-stop, r88-nonholder-stop, r88-shape-ambiguous-armed, r89-f2-dangling-to, r89-f2-dangling-from, r89-f2-invalid-source-id]
receipt fence line=462 command line=456 cases=[r89-c1-multi-cause-valid, r89-fn2-unresolved-chain-break, r89-fn2-control]
```

3 receipts / 14 cases / 0 replay failures; fence errors `[]`. Two consecutive
default runs are byte-identical (`diff` empty, both rc=0) — deterministic.

## 2. Boundary gate — self-test

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
[rc=0]
```

7 cases + `anchor_range_control`, all matching `boundary-doc-contract.json`
`self_test.expected` (including `replay_cases: "14/14"` on `committed_default`,
`forbid_traceback` on the six negatives, and the full anchor-control field
set). Self-test scratch is its own `TemporaryDirectory`; nothing left in the
repo tree by this seat.

## 3. Discriminator — held + control

```
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
[rc=0]

$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
[rc=2]
```

The control is real, not nominal: the checker blob at
`e97613cc276f5fa9cac49ff1900798cf6863c020` hashes to
`e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
(distinct bytes), and both fixtures flip to `README_exact=False` /
`pinned_semantic_gate=FAIL` under it. `matches_pin=True` in both modes refers
to the delivered checker's own pin.

## 4. Pin reproduction

```
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

- checker pin three-way agreement (checked programmatically:
  contract `checker.sha256` = `discriminate_check.PIN` = delivered bytes =
  `ff9fd2aa…d1421`; `all three equal: True`).
- document pin two-way equal (`7f815a93…c33e`).
- contract bytes `e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871`
  = the r97-closure baseline value.
- legacy baseline: `git show 5eb9451b:corpus/fixtures/check_bible.py | sha256sum`
  → `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` = contract
  `legacy_baseline_sha256`; both revisions resolve (`git cat-file -t` →
  `commit` for `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` and `5eb9451b…`), and
  blobs at `65838f86` hash exactly to the two pins above.

Note (not a contradiction): the boundary contract's legacy baseline
(`5eb9451b…`, anchor-range control) and the discriminator's `BASELINE`
(`e97613c…`, r90 gate-pair regression control) are two different pins for two
different gates; both reproduced.

## 5. No pinned byte changed

Pinned-input set = doc + checker + contract + both gate scripts + the 14
replayed fixture dirs + the two r91 discriminator READMEs (expectation
sources) = 21 paths / 68 tracked files. All byte-identical between baseline
`9a3d648` and the checked worktree:

```
$ python3 <hash-object vs ls-tree check over the 21 paths>
tracked files checked: 68
worktree == 9a3d648 blobs for all pinned paths: True
worktree == HEAD blobs for all pinned paths: True
changed: []

$ git diff --stat 9a3d648 -- <the 21 paths>    → empty, diff-exit=0
$ git status --porcelain -- <the 21 paths>     → empty, status-exit=0 (0 lines)
```

`git status --porcelain` empty also proves no untracked stray landed inside
the 14 pinned fixture directories. Worktree HEAD is `dd4df1b` (r97 close
commit); the pinned set is identical to both `9a3d648` and HEAD.

Live negative control on the delivered bytes (pin load-bearing, not
decorative): a copy of the pinned doc with one appended comment line
(`V19-scratch/doc-mutated.md`) run through the gate:

```
$ python3 corpus/tools/boundary_doc_check.py --doc .ufo/waves/round-98/seats/V19-scratch/doc-mutated.md
CHECK pinned inputs: FAIL
FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes
CERTIFICATION FAIL
[rc=1]
```

## 6. Poll-wait and final re-verification on the settled revision

Poll-wait protocol (20 s cadence): all five producer reports present at try 20
/ t=400 s — `ALL-REPORTS-PRESENT`. Landing timeline: S3/S5-addenda artifacts
early; S1 artifacts at try 7; S5 note (`r98-clerk-scope-note.md`) at try 11;
S2 (`tools/README.md`) at try 15; S1 report (`S1-freeze-hygiene.md`) at try
20. Reports at end: `S1-freeze-hygiene.md`, `S2-tools-docs.md`,
`S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md` (plus
landed verifier reports). No ABSENT item in this seat's dependency set.

Stability window: `stat -c %Y` over the 18 producer-touched files before/after
a 45 s sleep → identical ("STABLE: no producer file changed in 45s window",
checked at 2026-10-17T23:36:41Z). Final battery re-run on that settled
revision (full outputs in §1–§3; identical):

```
$ python3 corpus/tools/boundary_doc_check.py            → [rc=0] CERTIFIED; receipts 3/3, cases 14/14, anchors 2/2
$ python3 corpus/tools/boundary_doc_check.py --self-test → [rc=0] 8/8 SELF-TEST PASS
$ python3 corpus/tools/discriminate_check.py             → [rc=0] RESULT: DISCRIMINATION HELD; matches_pin=True
$ python3 corpus/tools/discriminate_check.py --checker e97613c → [rc=2] REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

Pinned-input re-check on the final revision: §5 checks above were run on this
same settled revision (68/68 identical to `9a3d648` and HEAD; diff and status
empty). No boundary-pinned path appears in the changed-file list.

Settled revision snapshot (`git status --short`, 20:37:15 -03):

```
 M LOG.md
 M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
 M corpus/knowledge/r95-aftermath-scope-note.md
 M corpus/knowledge/r96-response-scope-note.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-98/
?? corpus/fixtures/r98-clerk-filing/
?? corpus/knowledge/r98-clerk-scope-note.md
```

Delivered hashes at verification time (sha256): `dependency_freeze.py`
`03d04365…`, `dependency-freeze-contract.json` `153ebc5b…`, `tools/README.md`
`1d299c16…`, r95 map `80440d61…`, r95 note `8e9e1774…`, r96 note `a9b51f8c…`,
r98 note `1162262c…`; r98 fixture: README `32efc78f…`, map `c1099d0e…`,
entities `db2d8e5d…`, relations `c279254b…`, contradictions `37517e5f…`,
timeline `eb24e084…`, sources `32ee15b1…`, source-excerpt `b5edc2fd…`,
inspiration-note `58f5390e…`, fictional-excerpts `29e384bf…`.

## 7. Bounds and notes

- The gate certifies frozen-document drift, receipt replay, explicit anchor
  ranges, and limited structure only — not semantics/AST (tool's own scope
  line).
- Producer byte-ownership this round (tools freeze pair, tools README, r95
  map repair, r98 fixture, r98/r95/r96 knowledge notes) is disjoint from the
  21-path pinned set; §5's empty diff/status confirms the revision did not
  move the pins anyway.
- Baseline nuance: the round declaration names baseline `9a3d648`; worktree
  HEAD is `dd4df1b` (r97 close — SCORECARD admitted section), which touches
  only `LOG.md`/`SCORECARD.md` outside the pinned set. Pinned bytes were
  compared against both and are identical to both.
- C9 watch: the r97 row (`r91-c9-watch.md`) records "Next re-check: r98".
  This report supplies the r98 re-check evidence (checker pin fresh,
  DISCRIMINATION HELD, `e97613c` control REGRESSION-DETECTED); appending the
  watch row is closure work outside this seat's byte ownership.
- S3's report notes a parent-repo stray it did not write (its item D5) —
  outside this lane's tree; not re-examined here, and it does not touch any
  pinned path in this lane.

## Bottom line

PASS — on the settled post-producer revision: boundary gate default rc=0
CERTIFIED (receipts 3/3, cases 14/14, anchors 2/2, deterministic), `--self-test`
8/8 rc=0, discriminator HELD rc=0 with the `e97613c` control rc=2
REGRESSION-DETECTED, checker pin `ff9fd2aa…d1421` reproduced three ways
(contract = discriminator PIN = delivered bytes) and the doc pin
`7f815a93…c33e` reproduced, all 68 pinned files across 21 paths byte-identical
to baseline `9a3d648` and HEAD (empty diff/status), and a live mutated-doc
control fails the gate rc=1 `document_drift` — the pins are load-bearing.
