# P4 — SHONEN block proposal (round 90)

Seat: P4 (round-90 follow-up wave, SHONEN-block writer; world-bible lane). Judged revision:
`ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (`lore r90: C1 hedged-shapes repair + raw-present
fixtures, C2 maps + support command, C3 decided sub-cases — work wave`); baseline
`e97613cc276f5fa9cac49ff1900798cf6863c020` (r89 closure). At seat start `git status --short`
was empty; by the terminal wait-check (06:57:40) `?? .ufo/waves/round-90/followup/H2-delta.json`
and `?? corpus/tools/__pycache__/` were present, and the phase-2 sibling wave's artifacts
(CB1/E1/H2–H5/JCAL1–5/JDEP1–4/JCOV1–5/Q1/Q2/V2/P3) landed during the seat. Every measurement
below is on the DELIVERED tree at `ca7f9ef`, never on a patch or a seat report's intent;
scratch was `/tmp/p4/r90/` only; no tracked file was written. Deliverables: this file and
`P4.md` (seat note).

## Work performed

- Pinned the revision (`git rev-parse HEAD` → `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`) and
  confirmed the delivered files used below are unmodified by the working tree (only untracked
  paths exist).
- **Two 60 s wait-checks on `.ufo/waves/round-90/followup/`** (seat-start protocol):
  check 1 `2026-10-17T06:55:40-03:00` and check 2 `06:56:40-03:00` found the committed
  `Q1-r90-debt.json`; the terminal check `06:57:40-03:00` found the new untracked
  `H2-delta.json` (landed between check 2 and terminal). Work then proceeded with what
  existed; the later sibling artifacts were read for cross-reference only, after my own
  measurements were captured.
- **Freeze-then-verify (r88-I1), the designated blocking check:** composed `X2-c1-nullonly`
  + `X3-c1-tickonly` onto the `e97613c` checker in a scratch directory and hash-compared
  against the delivered checker — **byte-identical, no mismatch** (§Measurements).
- Ran **my own 164-directory census** (`/tmp/p4/r90/census2.py`): baseline checker
  (`git show e97613c:corpus/fixtures/check_bible.py`) vs the delivered checker over every
  delivered fixture dir, comparing `(returncode, stdout, stderr)`, plus a git-tree dir delta.
- Ran the **C2 receipt** — `corpus/tools/support_check.py` — on both clusters (22/22 and
  10/10, exit 0 each), the R9 paraphrase demo, and a **negative span-tamper control** on a
  scratch copy of the r87 cluster (exit 1, `outside-span=7`), demonstrating the enforcement
  is real rather than documented-only.
- Replicated **C9's four semantic probe cases** (constructed from
  `r89-fn2-unresolved-chain-break`) under the **delivered** checker — C9's own receipts were
  for the X1 alternative, not for the delivered X2+X3 composition.
- Read the delivered instruction surface: `corpus/tools/README.md`, both
  `claim-excerpt-map.md` files and the excerpt mode lines, the R8/R9/R10 decided appendices
  (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:28-63`), the boundary doc's
  fixture-coverage passages, `corpus/fixtures/README.md`, and the two cluster READMEs.
- Established the revision state of `SHONEN.md` (10 lines; four boxes at `:5,:6,:8,:9`),
  `PROVINCE.md`, `l0-questions.md`, and the round-record state (`LOG.md`,
  `SCORECARD.md`), and enumerated each box's subject on the delivered tree.
- Cross-reference reads after own measurement, not substitutes for it: `H2-delta.json`
  (independent census: `dirs_total 164`, `old160_base_vs_deliv_changed_tuples 0`,
  `old160_exit_flips 0`, `freeze_then_verify_match true`), `JCAL1.md` (independent
  freeze-then-verify to the same `ff9fd2aa…` hash), `H3-r90-mutations.json`
  (`stdout_changed_vs_r89: ["fn2-tick-qualification-superset"]` — matches my one-probe
  difference finding below).
- Drafted the SHONEN block for the round-90 report (§Findings). `SHONEN.md` itself is a
  tracked file outside this seat's write scope — the block is a proposal only.

## Before → after measurements

All commands run from the lane root unless noted; "before" = `e97613c`, "after" = `ca7f9ef`.

### Revision / file state

```sh
$ git rev-parse HEAD
ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13
$ git diff --stat e97613c ca7f9ef -- SHONEN.md PROVINCE.md l0-questions.md
(empty)
$ git diff --shortstat e97613c ca7f9ef
 95 files changed, 12619 insertions(+), 11 deletions(-)
$ git diff --name-only e97613c ca7f9ef | grep -v '^corpus/' | grep -v '^\.ufo/'
(no output)
$ test -e SKILL.md && echo SKILL-PRESENT || echo SKILL-ABSENT
SKILL-ABSENT
$ git ls-files | grep -Ei 'skill'
(no matches)
```

`SHONEN.md` unchanged this round: 10 lines, four boxes with glyphs `[ ]` at `:5`, `[~]` at
`:6`, `[ ]` at `:8`, `[~]` at `:9`. `l0-questions.md` unchanged (5 lines). Box 1's subject
(`SKILL.md`) does not exist on the delivered tree.

### Freeze-then-verify (r88-I1) — the blocking check: PASS, no mismatch

```sh
$ mkdir -p /tmp/p4/r90/compose/corpus/fixtures && cd /tmp/p4/r90/compose
$ git -C <repo> show e97613c:corpus/fixtures/check_bible.py > corpus/fixtures/check_bible.py
$ sha256sum corpus/fixtures/check_bible.py
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  corpus/fixtures/check_bible.py
$ git apply <repo>/.ufo/waves/round-90/patches/X2-c1-nullonly.patch    # rc=0
$ git apply <repo>/.ufo/waves/round-90/patches/X3-c1-tickonly.patch    # rc=0
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ sha256sum <repo>/corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  <repo>/corpus/fixtures/check_bible.py
$ cmp corpus/fixtures/check_bible.py <repo>/corpus/fixtures/check_bible.py && echo BYTE-IDENTICAL
BYTE-IDENTICAL
```

Method: `git apply` (strict context, no fuzz) in a scratch directory outside the repository —
an independent route to JCAL1's `patch`-based replay; both reach the same delivered hash.
**No mismatch: the composition claim in the work commit is verified.**

### Census — my own, 164 dirs, before vs after (`/tmp/p4/r90/census2.py`)

```sh
$ python3 /tmp/p4/r90/census2.py
dirs: 164
exits base: {1: 132, 0: 32} deliv: {1: 132, 0: 32}
changed tuples: 0
exit flips: []
stderr diffs: []
violation lines base: 417 deliv: 417
tree dirs base: 162 deliv: 166
new dirs: ['r90-c1-rawpresent-from', 'r90-c1-rawpresent-source', 'r90-c1-rawpresent-to', 'r90-c1-three-causes']
removed dirs: []
```

Reading: the delivered census delta is exactly **0 changed tuples + 4 new dirs of 164, 0 exit
changes, 0 stderr changes**, with 417 violation lines at both revisions. `tree dirs` counts
git-tree directories holding any file directly (166 delivered; the canonical-JSON census set
is 164); both new-dir reports agree. The four new dirs are behavior-pinning fixtures: their
stdout is identical under the baseline and delivered checkers (hence "0 changed"), and each
carries a README declaring that after-state.

### C2 receipt — the delivered support command (exit + N/N)

```sh
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
… 22 PASS lines … SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS                                          # EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
… 10 PASS lines … SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS                                          # EXIT=0
```

The receipt is reproducible from the tree alone: both clusters carry in-corpus maps
(`corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md`, 22 mapped rows incl. the 8 hymn
clauses; `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md`, 10 rows), each with an
R9 excerpt-declaration table and a per-row mode. The previously-unlabelled excerpts now carry
`**Delivery mode (R9):** verbatim` (five r87 files, including the four r89 excerpts;
`r88-m3-maya-cluster/fictional-excerpts.md`). The r89 named debts D1 (no in-corpus map) and
D2 (no R9 mode on the four excerpts) are discharged on the delivered tree.

R9/span enforcement controls (delivered tool, exact output):

```sh
$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
RESULT PASS                                          # EXIT=0
$ cp -r corpus/fixtures/r87-myth-cluster /tmp/p4/r90/tamper   # row E1 locator 7 → 2
$ python3 corpus/tools/support_check.py /tmp/p4/r90/tamper | grep -E '^FAIL|E1:|SOURCE-SUPPORT'
FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.; span=2; outside-span=7
SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
FAIL: E1: anchor hit outside declared line span 2 (hit lines: 7)
# EXIT=1
```

So a paraphrase with a matching anchor contributes 0 source support (R9), and an anchor hit
outside the declared span fails the run (M5's span enforcement) — both measured, not quoted.

### C1 hedged-shape probes under the DELIVERED checker (C9 matrix)

Built from `r89-fn2-unresolved-chain-break` with C9's four-case constructor, run with
`python3 corpus/fixtures/check_bible.py <probe>` (delivered checker sha256 recorded in-run:
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`):

```text
=== chain-unresolved (2 violations, exit 1)
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible
provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not
uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
=== tick-relevant-unresolved (2 violations, exit 1)
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
=== null-from-chain (2 violations, exit 1)
VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got None
=== unrelated-duplicate-tick (2 violations, exit 1)
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
```

(Each probe also carries the unrelated `entities[1].first_appearance` violation from the base
fixture; the target findings are the second lines shown.) Reading: genuinely unresolved
**non-null** holder chain stays qualified; **null** chain is definite; tick findings — both
under unrelated identity uncertainty and under an unresolved compared holder — are definite
integer comparisons. This is exactly the C9-written core ("null chains and tick findings
definite; genuinely unresolved non-null holder breaks qualified"). Note the one probe where
the delivered composition intentionally differs from C9's X1 replay: under X1,
`tick-relevant-unresolved` was qualified (C9.md output, `candidate_checker_sha256=12866e734b…`);
under the delivered X2+X3 it is definite — the ruling C9 recommended. `C9-rerun-probes.sh`
therefore still exercises X1, not the delivery; `H3-r90-mutations.json` records the same
one-case stdout change vs r89.

### Four new durable fixtures (delivered outputs = declared after-states)

```text
r90-c1-rawpresent-from    5 violations, rc=1: … "first stop: holder reference from_holder
'r90-c1-rawpresent-from-ghost' present in raw entities but absent from the resolved index at
entities[0].provenance[0]"
r90-c1-rawpresent-to      5 violations, rc=1 (symmetric, to_holder)
r90-c1-rawpresent-source  4 violations, rc=1: … "first stop: source reference
'r90-c1-rawpresent-source-ghostsrc' present in raw sources but absent from the resolved index"
r90-c1-three-causes       4 violations, rc=1: "first stop: malformed record (invalid tick);
holder reference to_holder '…absent-holder' absent from raw entities and absent from the resolved
index; source reference '…absent-source' absent from raw sources and absent from the resolved index"
```

Each output matches the fixture's own README declared after-state; base-vs-delivered stdout is
identical (census §above), so these pin the r89 FN-1 raw-present wordings and the ≥3-cause
valid-key summary durably.

FN-2 pair on the delivered tree:

```text
r89-fn2-unresolved-chain-break  2 violations, rc=1 — qualified "possible provenance chain break,
not a definite identity mismatch" (holder not uniquely resolvable)
r89-fn2-control                 1 violation,  rc=1 — definite "provenance chain break; expected
from_holder 'f3-dup', got 'mira'"
```

### Round-record state (box 2's LOG clause)

```sh
$ grep -n '^## ' LOG.md | tail -5
1908:## Round 88 — 2026-10-17 (…work commit `2ea9ef1`)
$ grep -n 'Round 89' LOG.md
2180:  no Round 89 section; `r87-probe-source-prefix/README.md` cites stale line refs. Per the
$ sed -n '2089,2090p' LOG.md
FN-1/FN-2 wording; r87 support completion; R8–R10 governance; luna-max work wave; work
commit `1b09f3f`)
$ grep -n "round's LOG record" LOG.md
2236:- **Round record.** `LOG.md` and `SCORECARD.md` are unchanged at `1b09f3f`; this entry is
$ grep -n "Round 90" SCORECARD.md LOG.md
(no matches)
```

Reading: the r89 closure appended its record as unheaded text (`:2089-2253`, self-labelled at
`:2236`); there is no `## Round 89` or `## Round 90` heading anywhere, and `LOG.md`'s last
round heading is `:1908`. `SCORECARD.md` has `## Round 89` at `:174` but no Round 90 section.
W2's r90 LOG/SCORECARD entries are proposals only
(`patches/W2-log-r90.proposal.md`, `patches/W2-scorecard-r90.proposal.md`).

## Findings & named debt

Per-box verdicts on the delivered tree at `ca7f9ef` (glyph in the delivered `SHONEN.md` in
parentheses; this seat judges the delivered glyph, as P4 did in r89). This seat makes no axis
verdict — that is the axis judges' remit; the measurements above are the C1/C2/C3 delivery
receipts the block cites.

- **Box 1 — `SHONEN.md:5` `[ ]` "SKILL.md contains real decision tables, error patterns,
  checklists, cited sources" — unchanged.** No `SKILL.md` exists (`test -e SKILL.md` →
  ABSENT; `git ls-files | grep -Ei 'skill'` → no matches), so the box's subject does not exist
  to assert. The substance grew this round — the R8/R9/R10 appendices are now *decided*
  (`r88-sourced-inspiration-decision-table.md:28-63`), the support tool ships with a checklist
  README (`corpus/tools/README.md`), and the claim maps carry per-row modes — but none of it
  is in a `SKILL.md`.
- **Box 2 — `SHONEN.md:6` `[~]` "At least one end-to-end domain task executed and logged in
  LOG.md" — lane assertion retained; evidence improved.** LOG records now: r87 (`LOG.md:1699`),
  r88 (`LOG.md:1908`), and the r89 record (`:2089-2253`, unheaded). Round 90 adds a third
  end-to-end set with delivered receipts: the 164-dir census (0 changed, 0 exit/stderr
  changes, 417 lines), the X2+X3 freeze-then-verify match, the four durable fixtures and the
  FN-2 pair, the 22/22 + 10/10 support receipt with two enforcement controls, and the decided
  R8/R9/R10 appendices. r90's own LOG entry is unlanded (proposal only). The box's evidence
  pointer is stale (cites only LOG.md round-1 and `reports/round-1/baseline-probes.json`);
  recommend adding `LOG.md:1699`, `LOG.md:1908`, `LOG.md:2089`. No external promotion
  verification → no `[x]`.
- **Box 3 — `SHONEN.md:8` `[ ]` "Instructions executable by an agent without oral context" —
  improved; proposal: `[ ]` → `[~]`.** Positive evidence, measured on the delivered tree:
  - one committed, documented, reproducible command whose exit code + N/N print is the
    receipt (`corpus/tools/support_check.py` + `corpus/tools/README.md`): r87 `22/22`,
    r88-m3 `10/10`, both exit 0;
  - the r89-executability blockers are discharged: the r87 application's evidence is now
    in-corpus (`claim-excerpt-map.md`), not wave scratch, and the four r89 excerpts carry R9
    delivery-mode labels;
  - enforcement is demonstrated, not declared: paraphrase → `0/0` source support
    (`RETELLING-SUPPORT-ONLY 1`), and a declared-span/actual-hit mismatch fails the run
    (`FAIL E1 … outside-span=7`, exit 1);
  - the C1 wording core is reproducibly receipted on the delivered checker (four C9 probes),
    and C3's governance rows are written with owners and review clauses
    (`r88-sourced-inspiration-decision-table.md:28-63`, including the R2 two-part gate and
    the "comparison keys, not identity" ruling).
  Bounds (why `[~]`, not `[x]`):
  - **B1 (stale coverage prose, new):** `corpus/knowledge/holder-assessment-boundary.md:472-477`
    and `:589-592` still call the raw-present wordings and the three-cause valid-key record
    "verified by CB1's round-89 scratch probes only … have no durable fixture in the tree yet"
    / "OBSERVED only in scratch probes at `1b09f3f` (no durable fixture)". At `ca7f9ef` the
    four `r90-c1-*` fixtures pin exactly those cases. The four FN-2 sub-branches named there
    (observed-side, tick, first-record; expected-side now pinned by the fn2 pair) remain
    scratch-only, as stated. This is incompleteness, not a behavioral contradiction — no
    delivered instruction now describes retired behavior.
  - **B2:** `corpus/fixtures/README.md` has no Round 90 section (the four new dirs are
    unreferenced); `r87-myth-cluster/README.md` (and r88's) still omit the claim maps and the
    support command (Q89-016 carried), and the r87 README omits the four delivered excerpts.
  - **B3:** `corpus/tools/__pycache__/` is untracked and `.gitignore` (`.ufo/interactive-sessions/`
    only) does not cover `__pycache__/` — file/inode hygiene, r89-named class recurring.
  - No named non-author cold-execution record of the lane's instructions exists; dispatched
    reviewers judged claims, not executability. L1 decides whether this command-based
    surfaces reach `[~]` on the block's evidence alone.
- **Box 4 — `SHONEN.md:9` `[~]` "No cross-domain bleed (PROVINCE.md still accurate)" — lane
  assertion retained; evidence strengthened.** `PROVINCE.md` byte-unchanged (empty diff
  `e97613c..ca7f9ef` for `SHONEN.md PROVINCE.md l0-questions.md`; `PROVINCE.md` still 11
  lines), `l0-questions.md` untouched (5 lines), and all 95 changed paths are under `corpus/`
  or `.ufo/` (grep filter → no output). The new surfaces keep the province's separations: the
  tool README states the check is "a reproducible lexical preflight, not a judgment" about
  fidelity, permission, or canon; the R8/R9/R10 rows keep attribution / rights / AI-training
  as three separate questions and assert no rights conclusion. No game-dev or kotodama surface
  is touched.

**Blocking-check result:** the designated freeze-then-verify check (delivered checker must
hash-match X2+X3 composed on `e97613c`) **passes with no mismatch** — no blocking finding.

**Additional finding — the committed Q1 ledger is a pre-integration artifact.**
`.ufo/waves/round-90/followup/Q1-r90-debt.json` as committed at `ca7f9ef` records
`observed_head=e97613c`, `sentinel_SE1_present=false`, and the interpretation "No immutable
delivered round-90 tree was available in this checkout"; its 28 `closure_verdict` rows
therefore describe the baseline, not the delivered tree (e.g. Q89-001 "null guard exists only
in an unintegrated patch" is false at `ca7f9ef`). The live phase-2 Q1 seat has already
modified that file (`git status` → ` M .ufo/waves/round-90/followup/Q1-r90-debt.json`). The
round record must not copy those baseline verdicts as delivered-tree verdicts.

**Finding — C9's harness vs the delivery.** `C9-rerun-probes.sh` replays X1 (pinned
`candidate_checker_sha256=12866e734b…`), whose `tick-relevant-unresolved` output is qualified;
the delivered X2+X3 checker makes the same probe definite, which is the ruling C9 recommended.
The harness is a valid receipt for X1's behavior and for the ruling's rationale, but it is not
a delivery receipt for the tick case; the delivered receipts are the C9-matrix probes above.

### Proposed SHONEN block for the round-90 report (proposal only — do not edit `SHONEN.md`)

> `SHONEN.md` is unchanged this round (`git diff --stat e97613c ca7f9ef -- SHONEN.md` →
> empty); four boxes at `SHONEN.md:5,6,8,9`. No `[x]` is claimed — no named non-author
> verifier has been asked to execute the lane's instructions cold. Drafted by follow-up seat
> `P4` (`followup/P4-shonen.md`).

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists,
  cited sources* — **unchanged**. No `SKILL.md` exists in the lane (`test -e SKILL.md` →
  ABSENT). Round 90's decision-table material (R8/R9/R10 decided appendices, the support
  command's README checklist, the claim maps) does not live in a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* —
  **lane assertion retained; evidence improved.** Three LOG records now carry end-to-end work
  (`LOG.md:1699` r87, `LOG.md:1908` r88, `LOG.md:2089` r89 record); round 90 adds the
  164-dir census (0 changed, 0 exit/stderr changes, 417 violation lines both revisions), the
  X2+X3 freeze-then-verify byte-match, four new durable fixtures + the FN-2 pair, the
  `22/22` + `10/10` support receipt with enforcement controls, and the decided R8/R9/R10
  appendices. r90's own LOG entry is a proposal only. Pointers: `LOG.md:1699`, `LOG.md:1908`,
  `LOG.md:2089`, `reports/round-1/baseline-probes.json`.
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* —
  **improved; proposal `[ ]` → `[~]`**. A committed reproducible command
  (`python3 corpus/tools/support_check.py <cluster>`, documented in
  `corpus/tools/README.md`) returns exit 0 with `SOURCE-SUPPORT 22/22` (r87) and `10/10`
  (r88-m3) on the delivered tree; the r87 evidence is in-corpus (claim map + mode labels);
  enforcement is demonstrated (paraphrase contributes 0 source support; out-of-span hit →
  exit 1). Bounds, so not `[x]`: `holder-assessment-boundary.md:472-477`/`:589-592` still
  call the now-fixtured raw-present and three-cause cases scratch-only;
  `corpus/fixtures/README.md` has no Round 90 section; the cluster READMEs omit the maps and
  the command; no named non-author cold-execution record exists.
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — lane
  assertion retained; evidence strengthened. `PROVINCE.md` bytes unchanged
  (`PROVINCE.md:3-11` resolves; 11 lines); all 95 changed paths under `corpus/` or
  `.ufo/`; `l0-questions.md` untouched; the new surfaces keep attribution / rights /
  AI-training separate and state no rights or canon conclusion.

## Handoff

- **Deliverables:** `.ufo/waves/round-90/followup/P4-shonen.md` (this file) and
  `.ufo/waves/round-90/followup/P4.md` (seat note). No tracked file was written outside the
  seat's allowed paths; no commit, no push, no sibling-repo write, no `SHONEN.md` edit.
- **Judged revision:** `ca7f9ef` (baseline `e97613c`); the freeze-then-verify check passes
  (composed X2+X3 sha256 = delivered sha256 = `ff9fd2aa…`). Scratch `/tmp/p4/r90/` is
  probe-only and not a deliverable.
- **Headline for L1:** all four boxes keep `[~]`/`[ ]` in the delivered file; the block's
  proposal moves box 3 `[ ]` → `[~]` on delivered evidence (reproducible support command
  22/22 + 10/10, in-corpus maps, R9 mode labels, demonstrated enforcement), with the bounds
  above; box 2's and box 4's assertions are retained with improved evidence; box 1 remains
  `[ ]` (no `SKILL.md`). No `[x]` is claimed.
- **Named debt handed forward (all outside this seat's write scope):** (1) refresh
  `holder-assessment-boundary.md:472-477`/`:589-592` to cite the four `r90-c1-*` fixtures
  (observed-side/tick/first-record FN-2 sub-branches remain scratch-only); (2) add a Round 90
  section to `corpus/fixtures/README.md`; (3) extend the cluster READMEs with the claim maps
  and support command (Q89-016 carried); (4) add `__pycache__/` to `.gitignore`; (5) do not
  copy the committed `Q1-r90-debt.json` baseline verdicts into the round record — re-read them
  at `ca7f9ef` (the live phase-2 Q1 re-audit is already modifying that file).
- **Process notes:** the two 60 s wait-checks met the seat protocol (first artifact
  `Q1-r90-debt.json` was already present; `H2-delta.json` landed at the terminal check); the
  wider phase-2 sibling wave landed during this seat and was read for corroboration only
  (`H2-delta.json`, `JCAL1.md`, `H3-r90-mutations.json`), never as a substitute for the
  measurements above. At seat end the working tree holds the sibling artifacts untracked (and
  `Q1-r90-debt.json` modified) — outside this seat's write scope.
