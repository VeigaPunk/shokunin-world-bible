# V22 — gates-boundary (round 99)

Seat: V22 gates-boundary. Lane: lore-shokunin. Every command below was run from
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. No nested agents,
no commits, no pushes, no network. Writes: this report and
`.ufo/waves/round-99/seats/V22-scratch/` only.

Axes: calibration (boundary default + self-test), depth (HELD vs a real
`e97613c` regression), coverage (checker + document + legacy, plus the gate's
receipt-fixture set), freshness (no boundary-pinned byte moved vs baseline
`4265df5`). A move was kept only if it improved one of those and harmed none.
None of the four moved the wrong way.

Standing declaration (LOG.md "Round 99 — declaration before dispatch"): baseline
`4265df5`. Worktree HEAD at verification was `337f0fa` (descendant; the only
committed delta is `LOG.md` / `SCORECARD.md`). The blocked-dispatch note in
LOG.md is the prior attempt; this re-dispatch is the one measured here.

## 1. Poll-wait

Cadence 20s, cap 40 tries. Expected producer reports (r98 names; S3 and S4
landed under exactly those names, so this was not a rename miss):
`S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S3-fixture-author.md`,
`S4-fixture-docs.md`, `S5-knowledge-notes.md`. Log:
`.ufo/waves/round-99/seats/V22-scratch/poll.log`.

- try 1, `2026-10-18T01:02:17Z`: present `S3-fixture-author.md`; missing S1, S2, S4, S5. `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md` absent.
- try 6, `2026-10-18T01:03:57Z`: `S4-fixture-docs.md` present.
- tries 7–15: still missing S1, S2, S5; both S5 knowledge files absent.
- Bounded stall (recorded, not fatal): the first poller was killed by the tool timeout after try 15 (`~01:06:57Z`). Resumed at try 16, `2026-10-18T01:15:40Z`. The try count was not reset.
- tries 16–40: `allSmd` stayed `[S3-fixture-author.md S4-fixture-docs.md]`. No other `S*.md` report name appeared under `seats/`.
- `POLL-EXHAUSTED try=40` at `2026-10-18T01:23:40Z`.

Rechecked after the battery, not only at try 40:

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-18T01:37:11Z
$ ls .ufo/waves/round-99/seats/S*.md
.ufo/waves/round-99/seats/S3-fixture-author.md
.ufo/waves/round-99/seats/S4-fixture-docs.md
```

ABSENT at poll exhaustion and at the final recheck: `S1-freeze-hygiene.md`,
`S2-tools-docs.md`, `S5-knowledge-notes.md`, and both S5 knowledge files.
Those planned S5 artifacts were not verified. Endgame stall-escape: this seat
then measured the boundary artifacts that do exist, on the tree as it stood.
That is not a certification that later producer writes cannot happen.

Producer-owned files that had landed by the battery were stable across a 45s
window ending `2026-10-18T01:31:50Z` (epoch mtimes identical before and after):
`dependency_freeze.py` `1792285653`, `dependency-freeze-contract.json`
`1792285726`, `README.md` `1792283525`, `SKILL.md` `1792283663`, and the five
boundary gate files. `README.md` and `SKILL.md` were not dirty vs HEAD
(`git status --porcelain` did not list them), so S2 had not edited them.
`dependency_freeze.py`'s mtime did move earlier in the poll window (seen
`1792285324` around 01:15Z, then `1792285653` by 01:31Z); the quoted battery
is after that later mtime, and the 45s window did not move again.

## 2. Boundary gate — default

Quoted from the post-stability run (`V22-scratch/final-default-1.out`, empty
stderr, rc file `[rc=0]`). A second run in the same minute was byte-identical
(`cmp` printed `IDENTICAL`; `final-default.diff` is 0 bytes; second rc=0).

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

Receipt fences, enumerated by importing `boundary_doc_check` against the
pinned document (same sha256 `7f815a93…c33e` as the final `sha256sum`):

```
receipt fence line=355 command line=346 cases=['r85-control', 'r85-unique-break-control', 'r85-masked-ambiguous', 'r85-isolated-ambiguous', 'r85-harbor-repro']
receipt fence line=406 command line=400 cases=['r88-mixed-stop', 'r88-nonholder-stop', 'r88-shape-ambiguous-armed', 'r89-f2-dangling-to', 'r89-f2-dangling-from', 'r89-f2-invalid-source-id']
receipt fence line=462 command line=456 cases=['r89-c1-multi-cause-valid', 'r89-fn2-unresolved-chain-break', 'r89-fn2-control']
```

3 receipts / 14 cases. That is the contract's `replay_cases: "14/14"`.

## 3. Boundary gate — self-test

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

Stderr empty. 7 cases + `anchor_range_control`. The tool fails a case unless
exit, finding ids, `forbid_traceback`, and (for `committed_default`)
`replay_cases == "14/14"` match `boundary-doc-contract.json`
`self_test.expected`. The PASS line does not echo `replay_cases`; the case
still printed `SELF-TEST PASS`, so that internal check held. The anchor
control's `delivered_line_count: 220` is a synthetic checker the self-test
builds (`b"control line\n" * 220`), not the delivered file's line count.
`baseline_lines=330` is the real legacy blob:

```
$ git show 5eb9451baff217c19d5786405f9b2aa500b7c1b7:corpus/fixtures/check_bible.py | wc -l
330
```

No `boundary-doc-self-test-*` directory was left under `/tmp` after the run.
The self-test reads committed blobs at `65838f86` / `5eb9451b`, not a plan.

## 4. Discriminator — held + control

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

Both stderrs empty. The control is a different blob, not a label:

```
$ git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

That is not `ff9fd2aa…`. `matches_pin=True` in both modes is the delivered
file's own pin (`discriminate_check.py` hashes `corpus/fixtures/check_bible.py`
either way). Under `e97613c`, both fixtures flip to `README_exact=False` and
`pinned_semantic_gate=FAIL`.

## 5. Pin reproduction

```
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
```

Same two digests at the early run (~01:01Z), the 01:31 battery, and this
`2026-10-18T01:37:11Z` recheck.

- Checker, three ways plus the pinned revision blob: contract
  `checker.sha256` = `discriminate_check.PIN` = worktree sha256 =
  `git show 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e:corpus/fixtures/check_bible.py | sha256sum`
  = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
  Programmatic compare at `2026-10-18T01:34:21Z`: `three-way True`.
- Document, two ways plus the same revision blob:
  `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`
  (`doc-two-way True`; `git show 65838f86:corpus/knowledge/holder-assessment-boundary.md | sha256sum` matched).
- Legacy: `git show 5eb9451baff217c19d5786405f9b2aa500b7c1b7:corpus/fixtures/check_bible.py | sha256sum`
  → `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`,
  equal to contract `legacy_baseline_sha256`.
- Contract file itself: sha256
  `e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871`,
  and its git blob matches `4265df5` and HEAD (in the 86-path set below).
  The pin targets were not retargeted.

```
$ git cat-file -t 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
commit
$ git cat-file -t 5eb9451baff217c19d5786405f9b2aa500b7c1b7
commit
$ git cat-file -t 4265df5e86e4121bde4125b649b89bb1676676a5
commit
$ git cat-file -t e97613cc276f5fa9cac49ff1900798cf6863c020
commit
```

The boundary contract's legacy pin (`5eb9451b`, anchor-range control) and the
discriminator's `BASELINE` (`e97613c`, r90 regression control) are two
different pins. Both reproduced. Neither is a substitute for the other.

Live negative control, scratch copy only (one appended comment line; the
pinned document was not edited):

```
$ python3 corpus/tools/boundary_doc_check.py --doc .ufo/waves/round-99/seats/V22-scratch/doc-mutated.md
CHECK pinned inputs: FAIL
FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes
CERTIFICATION FAIL
[rc=1]
```

The document pin is load-bearing. Stderr empty.

## 6. No boundary-pinned byte changed

Named pins (checker, document, legacy) first. Checker and document worktree
blobs equal `4265df5` and HEAD (`git hash-object` == `git rev-parse
4265df5:path` == `git rev-parse HEAD:path`). Legacy is not a worktree file;
the `5eb9451b` blob hash above is the contract pin, so the round did not
rewrite it.

Extended set, because the gate also depends on them: contract + both gate
scripts + the 14 receipt fixture dirs the document names (79 tracked files)
+ the two r91 discriminator READMEs. 86 paths. At `2026-10-18T01:34:21Z`,
after the battery and after the later `dependency_freeze.py` mtime:

```
checked 86 unique 86 bad 0
```

`bad` means worktree blob != `4265df5` blob or != HEAD blob. None differed.

```
$ git status --porcelain -- corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md corpus/tools/boundary_doc_check.py corpus/tools/boundary-doc-contract.json corpus/tools/discriminate_check.py
```

Empty (same for the 14 fixture dirs and both r91 READMEs; status exit 0).
`git diff --stat 4265df5 -- <those paths>` empty, diff exit 0. Empty status
also means no untracked stray inside those fixture dirs.

What the round did change, tracked, vs `4265df5`:

```
$ git diff --name-only 4265df5
LOG.md
SCORECARD.md
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py

$ git diff --stat 4265df5 HEAD
 LOG.md       | 91 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 SCORECARD.md | 32 +++++++++++++++++++++
 2 files changed, 123 insertions(+)
```

`LOG.md` and `SCORECARD.md` are committed in HEAD (`337f0fa`, which is a
descendant of `4265df5` via `111b9a3`). They are not worktree-dirty. The two
freeze files are worktree-dirty and are S1's owned paths, not boundary pins.
Untracked at the 01:31 status: `.ufo/waves/round-99/` and
`corpus/fixtures/r99-window-lapse/`. By 01:34 a further untracked file
existed, `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`,
not written by this seat and not a pin path. None of those paths are in the
86-path pin set.

Producer byte-ownership this round (freeze pair, tools README + SKILL freeze
row, r99 fixture, r99 knowledge notes) does not include
`corpus/fixtures/check_bible.py`, `corpus/knowledge/holder-assessment-boundary.md`,
the legacy blob, the boundary contract, or the receipt fixtures. The empty
pin diff is the check that the revision did not move them anyway.

## 7. Bounds

- The gate certifies frozen-document drift, receipt replay, explicit anchor
  ranges, and limited structure only. Its own scope line says it is not
  semantic or AST validation.
- S1, S2, and S5 reports were still absent at `2026-10-18T01:37:11Z`. This
  report does not treat the declaration's planned S5 table as verified.
  Stall-escape is recorded; it is not a pin failure.
- A producer still running after this seat's cap could still violate
  ownership later. As of the quoted commands, they had not: pin status empty,
  pin hashes equal to `4265df5` and HEAD.
- `delivered_line_count: 220` in the contract is the synthetic anchor-control
  checker, not a claim about `check_bible.py`'s length.

## Bottom line

PASS — post-poll tree at 2026-10-18T01:31:50Z through 01:37:11Z (stall-escape: S1/S2/S5 reports ABSENT after 40 tries, not a pin failure): boundary default rc=0 CERTIFIED (receipts 3/3, cases 14/14, anchors 2/2, two runs byte-identical), `--self-test` 8/8 rc=0, DISCRIMINATION HELD rc=0 with the `e97613c` control rc=2 REGRESSION-DETECTED on a distinct blob `e2bb9639…`, checker pin `ff9fd2aa…d1421` reproduced (contract = discriminator PIN = worktree = `65838f86` blob), document pin `7f815a93…c33e` and legacy pin `88c9b1d0…9b81` reproduced, 86 pin paths byte-identical to `4265df5` and HEAD, and a one-line mutated-doc control fails rc=1 `document_drift`.
