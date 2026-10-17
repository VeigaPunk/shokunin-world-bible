# V23 — gates-boundary (round 97)

Seat: V23 gates-boundary. Lane: lore-shokunin. All commands run from
`/home/vgpnk/Projects/shokunin/lore-shokunin/`. No nested agents, no commits,
no pushes, no network. Only this report and `V23-scratch/` were written.

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

Receipt enumeration (instrumented via import of the tool, same run as above):
3 receipts / 14 cases / 0 replay failures. Cases are exactly
`r85-{control,unique-break-control,masked-ambiguous,isolated-ambiguous,harbor-repro}`
(doc fence line 346), `r88-{mixed-stop,nonholder-stop,shape-ambiguous-armed}` +
`r89-f2-{dangling-to,dangling-from,invalid-source-id}` (line 400), and
`r89-{c1-multi-cause-valid,fn2-unresolved-chain-break,fn2-control}` (line 456).

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
`forbid_traceback` on the six negatives, and the anchor-control field set).

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

## 4. Pin reproduction (three-way agreement)

```
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

- contract `checker.sha256` = discriminator `PIN` = delivered bytes =
  `ff9fd2aa…d1421` (equality checked programmatically: `all three equal: True`).
- contract `document.sha256` = delivered doc bytes = `7f815a93…c33e`.
- legacy baseline: `git show 5eb9451b:corpus/fixtures/check_bible.py | sha256sum`
  → `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` = contract
  `legacy_baseline_sha256`; revision object exists (`git cat-file -t` →
  `commit`).
- Pinned revisions resolve: `git cat-file -t 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`
  → `commit`, and its blobs hash to exactly the two pins above (checked with
  `git show 65838f86:… | sha256sum`).

Note (not a contradiction): the boundary contract's legacy baseline
(`5eb9451b…`, anchor-range control) and the discriminator's `BASELINE`
(`e97613c…`, r90 gate-pair regression control) are two different pins for two
different gates; both reproduced.

## 5. No pinned byte changed

Pinned-input set = doc + checker + contract + both gate scripts + the 14
replayed fixtures (19 paths). All byte-identical between baseline `f3e09f9`
and the checked revision:

```
$ for p in <19 paths>; do a=$(git rev-parse f3e09f9:$p); b=$(git rev-parse HEAD:$p); ... done
corpus/live/runs/round-85/probe-inputs/r85-control          base=26f0d0ddbea4 head=26f0d0ddbea4 same=YES
corpus/live/runs/round-85/probe-inputs/r85-unique-break-control base=eabb18bd4ec8 head=eabb18bd4ec8 same=YES
corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous base=ec3749400c97 head=ec3749400c97 same=YES
corpus/live/runs/round-85/probe-inputs/r85-isolated-ambiguous base=a87ba86c481a head=a87ba86c481a same=YES
corpus/live/runs/round-85/probe-inputs/r85-harbor-repro     base=e19e54278831 head=e19e54278831 same=YES
corpus/fixtures/r88-mixed-stop            base=23e80db2ef4a head=23e80db2ef4a same=YES
corpus/fixtures/r88-nonholder-stop        base=7ffa45025511 head=7ffa45025511 same=YES
corpus/fixtures/r88-shape-ambiguous-armed base=2708a20d579e head=2708a20d579e same=YES
corpus/fixtures/r89-f2-dangling-to        base=5df0204a1ca7 head=5df0204a1ca7 same=YES
corpus/fixtures/r89-f2-dangling-from      base=1cd8f212cfa9 head=1cd8f212cfa9 same=YES
corpus/fixtures/r89-f2-invalid-source-id  base=b2e724d3bbeb head=b2e724d3bbeb same=YES
corpus/fixtures/r89-c1-multi-cause-valid  base=804322e9712b head=804322e9712b same=YES
corpus/fixtures/r89-fn2-unresolved-chain-break base=c014ce1cdb06 head=c014ce1cdb06 same=YES
corpus/fixtures/r89-fn2-control           base=5c0bc2fc5897 head=5c0bc2fc5897 same=YES
corpus/fixtures/check_bible.py            base=20c56dbb90d9 head=20c56dbb90d9 same=YES
corpus/knowledge/holder-assessment-boundary.md base=625148b6f444 head=625148b6f444 same=YES
corpus/tools/boundary-doc-contract.json   base=9b73e150ceaf head=9b73e150ceaf same=YES
corpus/tools/boundary_doc_check.py        base=4daa9998023f head=4daa9998023f same=YES
corpus/tools/discriminate_check.py        base=aa601eee3ec2 head=aa601eee3ec2 same=YES
```

`git diff --stat f3e09f9 -- <the 19 paths>` is empty, and
`git status --porcelain -- <the 19 paths>` is empty on the worktree. The
contract's own bytes are also unchanged from baseline
(`git show f3e09f9:corpus/tools/boundary-doc-contract.json | sha256sum` =
`e89d2a76…9871` = `sha256sum corpus/tools/boundary-doc-contract.json`).

Live negative control on the delivered bytes (pin load-bearing, not
decorative): a copy of the pinned doc with one appended comment line
(`V23-scratch/doc-mutated.md`) run through the gate:

```
$ python3 corpus/tools/boundary_doc_check.py --doc .ufo/waves/round-97/seats/V23-scratch/doc-mutated.md
CHECK pinned inputs: FAIL
FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes
CERTIFICATION FAIL
[rc=1]
```

## 6. Final re-verification on the post-producer revision

Poll-wait satisfied: all six producer reports present at `2026-10-17 18:56:41
-03` (`R1-map-pinning.md`, `R2-contract-docs.md`, `R3-freeze-hardening.md`,
`R4-fixture-author.md`, `R5-fixture-docs.md`, `R6-knowledge-note.md`; each
bottom line PASS; R3 names one unresolved item outside this seat's scope — an
R2-owned README paragraph). Verified revision (worktree, no commit):

```
 M LOG.md
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-97/
?? corpus/fixtures/r97-crossing-acknowledgment/
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

Delivered hashes at verification time: `map_obligations.py` `86b52949…`,
`map-obligations-contract.json` `2142b991…`, `dependency_freeze.py`
`b06275f3…`, `dependency-freeze-contract.json` `27273be2…`, r96
`claim-excerpt-map.md` `e851f068…`, `tools/README.md` `6278e59b…`, r97 note
`5e3b4225…`; r97 fixture: map `49d4834e…`, entities `026af0bc…`, relations
`c279254b…`, contradictions `37517e5f…`, timeline `73063a86…`, sources
`438fb513…`, source-excerpt `b5edc2fd…`, inspiration-note `58f5390e…`,
fictional-excerpts `8ba491cb…`, README `d9387b7d…`.

Final gate runs on that revision (full outputs in §1–§3; identical):

```
$ python3 corpus/tools/boundary_doc_check.py            → [rc=0] CERTIFIED; receipts 3/3, cases 14/14, anchors 2/2
$ python3 corpus/tools/boundary_doc_check.py --self-test → [rc=0] 8/8 SELF-TEST PASS
$ python3 corpus/tools/discriminate_check.py             → [rc=0] RESULT: DISCRIMINATION HELD; matches_pin=True
$ python3 corpus/tools/discriminate_check.py --checker e97613c → [rc=2] REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

Pinned-input re-check on the final revision: `git diff --stat f3e09f9 --
<19 paths>` empty and `git status --porcelain -- <19 paths>` empty; the
contract still hashes `e89d2a76…9871` (baseline value). No boundary-pinned
path appears in the changed-file list above. Stability window: `stat -c %Y`
over the seven changed producer files before/after a 45 s sleep → identical
("STABLE: no producer file changed in 45s window"), boundary default still
`[rc=0] CERTIFIED` at `18:57:53 -03`.

## 7. Bounds and notes

- The gate certifies frozen-document drift, receipt replay, explicit anchor
  ranges, and limited structure only — not semantics/AST (tool's own scope
  line).
- This seat's gates read no producer-owned path: R1/R2/R3 (tools + their
  contracts), R4/R5 (r96/r97 fixtures), R6 (knowledge note) are all outside
  the 19-path pinned-input set; the r96 map repair and r97 fixture are
  structurally disjoint from the boundary receipts (r85/r88/r89 fixtures).
  Final §6 re-run confirms the revision did not move the pins anyway.

## Bottom line

PASS — on the frozen post-producer revision: boundary gate default rc=0
CERTIFIED (receipts 3/3, cases 14/14, anchors 2/2), `--self-test` 8/8 rc=0,
discriminator HELD rc=0 with the `e97613c` control rc=2 REGRESSION-DETECTED,
checker pin `ff9fd2aa…d1421` reproduced three ways (contract = discriminator
PIN = delivered bytes) and the doc pin `7f815a93…c33e` reproduced, all 19
boundary-pinned paths byte-identical to baseline `f3e09f9` (empty
`git diff`/`git status` on the pinned set), and a live mutated-doc control
fails the gate rc=1 `document_drift` — the pins are load-bearing.
