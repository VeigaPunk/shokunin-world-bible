# P4 — Round 87 SHONEN section (draft for the round report)

Seat: P4 (SHONEN-block writer). Measured tree: `lore-shokunin` HEAD
`2b48ca72033dfd1060b6f81c4cf27ad83deae57f`, clean at start
(`git status --short` → no output). No tracked file was written by this
seat; this file is the deliverable. Sibling-repo reads only.

Cross-check basis: `SHONEN.md` on the delivered tree is 10 lines / 718 bytes
with exactly **four** checklist boxes at `SHONEN.md:5,6,8,9`. The file is
unchanged this round:
`git diff --name-only 28706dc..2b48ca7 -- SHONEN.md` → empty output.
Every box below is reported `[~]` (lane assertion with a resolvable pointer)
or `[ ]` (untouched). **No `[x]` is claimed**: no named non-author verifier
has executed the lane's instructions cold, and the two `[ ]` boxes have no
satisfiable surface on this tree.

## SHONEN

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error
  patterns, checklists, cited sources* — **untouched**. No `SKILL.md` exists
  in the lane (`test -e SKILL.md` → `ABSENT SKILL.md`; `git ls-files |
  grep -Ei 'SKILL'` → `no matches`), so the box's subject does not exist to
  assert. Round 87's decision-table and checklist material landed in
  `corpus/knowledge/holder-assessment-boundary.md:66-103`, not in a
  SKILL.md. Sibling lanes do carry one (`chousa-shokunin/SKILL.md`,
  `kaidoku-shokunin/SKILL.md`, `kama-shokunin/SKILL.md`,
  `kotodama-shokunin/SKILL.md` → PRESENT), so the criterion is this lane's
  own file, not a fleet-level artifact.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and
  logged in LOG.md* — **lane assertion retained; not upgraded**. The round's
  end-to-end domain task was executed and is measured below, but its record
  lives only under `.ufo/waves/round-87/`: `git diff --name-only
  28706dc..2b48ca7 -- LOG.md` → empty output, so the "logged in LOG.md"
  clause is not satisfied for r87. The existing pointer stands (`LOG.md`,
  "Fleet round 1 — calibration declaration before batched dispatch";
  `reports/round-1/baseline-probes.json`). New supporting execution (not a
  LOG entry): commits `03c6746` (C1) and `e4708cb` (C3), the census and
  fixture replays in "Measurements" below, and independent verification of
  the delivered checker bytes by seat V1 (see the C1 chain note).
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral
  context* — **untouched; counter-evidence at `2b48ca7`, partially repaired
  in the working tree, still unresolved**. The lane's only instruction
  surface is `corpus/knowledge/holder-assessment-boundary.md`.
  - As committed at `2b48ca7` the doc contradicts delivered behavior: it
    self-labels `verified-at: STATIC PENDING PARENT RUNTIME` (`:14-20`), its
    parent-owned measured-results slot is empty (`:210-214`), its named
    recheck command points at an absent file (`:22-30`, `:146-157`; command
    receipt below), and its decision table says "exactly one notice per
    item, located at the FIRST ambiguous-holder record" (`:52-55`, `:73`)
    while the delivered checker emits a per-record disclosure (measured:
    4 `unassessed` lines per masked fixture).
  - Seat I2's refresh is present but **uncommitted** in the working tree
    (`git diff --stat corpus/knowledge/holder-assessment-boundary.md` →
    1 file changed, 25 insertions(+), 17 deletions(-)); it fixes the
    status header, the contract clauses 1-5, and the recheck paragraph.
    It leaves four residual blocks that still contradict the delivered
    checker: `:104` still says "at the first ambiguous-holder record only,
    the single … notice"; `:177-188` still presents
    `measure_holder_disclosure.py` as the "Agreed measurement entry point"
    though `:33-38` now says that file does not exist at `2b48ca7`;
    `:222-239` still lists "CONTRACT-SPECIFIED, PENDING PARENT RUNTIME" and
    "STATIC SOURCE READ (this seat)"; `:241-245` still reads "Nothing
    recorded by this seat … static-pending-runtime".
  - Even a fully consistent doc would not satisfy this box: no cold
    execution by an agent working only from the lane's written surface is
    recorded (I2 replayed the checker as the doc's rewriter, not as a blind
    executor), and the lane still has no `SKILL.md`/`AGENTS.md` entry
    surface. Flipping this box needs a named non-author cold-execution
    record; `[~]` would at minimum need the four residual blocks reconciled
    and landed.
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)*
  — **lane assertion retained; consistent with this round**. `PROVINCE.md`
  bytes are unchanged (`git diff --name-only 28706dc..2b48ca7 -- PROVINCE.md`
  → empty output); every path the round changed is inside the lane
  (`... | grep -vE '^(corpus/|\.ufo/)'` → `NONE outside corpus//.ufo/`;
  111 files changed, all under `corpus/` and `.ufo/`). The C3 fixture keeps
  attribution, rights, and AI-training permission as three separate open
  questions and reports the place contradiction without resolving it,
  matching `PROVINCE.md:7,9`; the C1 checker change is consistency
  verification, which `PROVINCE.md:3` owns.

**Round effect on the four boxes: all unchanged.** No box moved up or down;
box 3 gained counter-evidence (stale instruction surface, only partially
repaired by I2's uncommitted refresh) and box 2 gained supporting execution
that is not yet in `LOG.md`.

## Measurements (delivered tree, 2b48ca7; exact commands and observed output)

Full fixture census, `python3 /tmp/p4-census.py` (script replays
`corpus/fixtures/check_bible.py` over every direct `corpus/fixtures/*/`
directory):

```text
{"fixture_dirs": 138, "exit_counts": {"1": 108, "0": 30}, "total_violations": 272, "stderr_nonempty": 0}
```

Reconciles with the recorded baseline census (133 dirs, exits `{0:28,1:105}`,
259 violations, `.ufo/waves/round-87/B1.md:8-20`): +5 r87 fixture dirs
(4 C1 + `r87-myth-cluster`), +13 violation lines
(`r87-chain-unique-broken` 1; `r87-masked-break-to-ambiguous` 6;
`r87-masked-break-from-ambiguous` 6), +2 clean exits. 259+13=272 and
28+2=30, 105+3=108. Note: the C1 commit message says "census 133 -> 137
dirs" because it predates the C3 commit; the delivered tree measures 138.

The same script on the current **working tree** (after I1's uncommitted
probe fixtures landed) gives a different count, recorded here only so the
two numbers are not confused:

```text
{"fixture_dirs": 140, "exit_counts": {"1": 110, "0": 30}, "total_violations": 309, "stderr_nonempty": 0}
```

The +2 dirs are `corpus/fixtures/r87-probe-entry-shape/` (exit 1, 2
violations) and `corpus/fixtures/r87-probe-record-and-chain/` (exit 1, 35
violations); both are untracked. All box verdicts in this section are
measured against the committed tree at `2b48ca7`, per the round rule.

C3 fixture (box-4/coverage surface):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

C1 masked-break pair and unique controls (per-record disclosure):

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
6 violation(s); no canon changed
EXIT=1
```

(`r87-masked-break-from-ambiguous` is symmetric, `from_holder`, same 6 lines,
exit 1; `r87-chain-unique-valid` exit 0 CLEAN; `r87-chain-unique-broken`
exit 1 with the single definite break `entities[3].provenance[2]:
provenance chain break; expected from_holder 'harbor', got 'mira'`.)

Instruction-surface receipts for box 3:

```text
$ python3 corpus/fixtures/measure_holder_disclosure.py --revision 2b48ca7
python3: can't open file '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/measure_holder_disclosure.py': [Errno 2] No such file or directory
EXIT=2

$ for c in r87-masked-break-to-ambiguous r87-masked-break-from-ambiguous; do \
    python3 corpus/fixtures/check_bible.py corpus/fixtures/$c | grep -c 'unassessed'; done
4
4
```

The doc's "exactly one notice per item" claim (`:52-55`, `:73` at
`2b48ca7`) is contradicted by 4 `unassessed` lines per masked fixture
(1 first-ambiguity notice + 1 origin/cause line + 1 per later record).

Re-measured after I2's uncommitted refresh landed in the working tree
(checker bytes unchanged, so behavior is identical):

```text
$ git -C /home/vgpnk/Projects/shokunin/lore-shokunin diff --stat corpus/knowledge/holder-assessment-boundary.md
 corpus/knowledge/holder-assessment-boundary.md | 42 +++++++++++++++-----------
 1 file changed, 25 insertions(+), 17 deletions(-)

$ test -e corpus/fixtures/measure_holder_disclosure.py && echo PRESENT || echo ABSENT
ABSENT

$ python3 corpus/fixtures/measure_holder_disclosure.py --revision HEAD
python3: can't open file '.../corpus/fixtures/measure_holder_disclosure.py': [Errno 2] No such file or directory
EXIT=2

$ grep -n 'first ambiguous-holder record only' corpus/knowledge/holder-assessment-boundary.md
104:| Ambiguous holder, either field (ID matches ≥ 2 entity rows) | ... PLUS, at the first ambiguous-holder record only, the single `…continuity and tick-order comparisons unassessed…` notice. ... |
```

Residual stale blocks in the refreshed (uncommitted) doc: `:104`
(decision-table row), `:177-188` (measurement entry point presented as
usable), `:222-239` (status split still "PENDING PARENT RUNTIME"), and
`:241-245` (measured-results slot still "Nothing recorded by this seat").
The refresh is not committed, so the delivered tree at `2b48ca7` still
carries the pre-refresh text.

The doc's other documented command block (the five r85 probe invocations,
`:141-144`) does execute and matches its pinned triples — all five replayed by
this seat at 2b48ca7: `r85-control` exit 0 CLEAN; `r85-unique-break-control`
exit 1 (one break); `r85-masked-ambiguous` exit 1 (5 violations, notices at
`[1]` and `[2]`); `r85-isolated-ambiguous` exit 1 (4 violations, notice at
`[2]`); `r85-harbor-repro` exit 1 (7 violations incl. `timeline[0].place_id:
ambiguous place entity 'harbor'`). That is one working command block, not the
lane's instruction set, and it is this seat's replay, not a cold-agent
execution.

## C1 verification chain (for the parent's integration, not a box upgrade)

The delivered `corpus/fixtures/check_bible.py` is byte-identical to the
`X1-c1` candidate: applying `patches/X1-c1.patch`, `X2-c1-alt.patch`,
`X3-c1-min.patch`, `X4-c1-fsm.patch` to a clean `git archive 28706dc` copy in
`/tmp/p4-patchid` (all four `git apply` exit 0) and diffing each result
against the delivered file gives `IDENTICAL to delivered: X1-c1` and
differences of 32 / 19 / 68 changed lines for X2 / X3 / X4. Seat V1
independently applied the same `X1-c1.patch` in a fresh worktree and measured
133/133 identical returncode/stdout/stderr tuples (28 exit 0, 105 exit 1),
`preexisting_findings_preserved=True`, `all_stderr_empty=True`
(`.ufo/waves/round-87/V1.md`, `patches/V1-verify.json`). So a named non-author
verifier exists for the delivered checker delta — but that verifies the C1
delta, not the promotion checklist; `SHONEN.md:6` still fails its LOG.md
clause and no box is `[x]`.

## Limits and named gaps

- This seat wrote no tracked file and ran no experimental writes outside
  `/tmp` (`/tmp/p4-census.py`, `/tmp/p4-patchid/`, `/tmp/p4-baseline.py`).
- `SHONEN.md` itself was not edited; a box state change would need the
  parent's authority plus, for `[x]`, a named non-author verifier of the
  box's own condition.
- Open dependencies: I1's decision table had not landed at draft time
  (`.ufo/waves/round-87/followup/` held I3/JCOV4/K2/Q1/H2/H3/I2 artifacts),
  and `.ufo/reports/round-87/` does not exist. I2's
  `corpus/knowledge/holder-assessment-boundary.md` refresh landed
  **uncommitted** during this draft; its four residual stale blocks are
  listed under box 3 and should be reconciled before landing. The box-3
  counter-evidence on the committed tree is measured at `2b48ca7`; the
  post-refresh re-measurement is recorded above and must be repeated if I2
  edits again.
- Concurrent follow-up artifacts by other seats (`K2-adjacency.md`,
  `K2.md`, `Q1.md`, `I3.md`, `JCOV4.md`, `JCOV2.md`, `JCAL1.md`, `H2.md`,
  `H3.md`, `E2-*.json`, `I2.md`) were read for cross-reference only; none
  is cited as this seat's own measurement.
