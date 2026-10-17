# P4 — SHONEN block proposal (round 91)

Seat: P4 (round-91 follow-up wave, SHONEN-block writer; world-bible lane). Judged revision:
`c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (`lore r91: C3 R8/R10 r91 edge decisions …`,
follow-up to work commit `6332115`); baseline `a7c6a1773d5994246a76e4eff30d645f161920e0`
(r90 closure). Lineage ancestors used for comparisons: `e97613c` (r89 closure, pre-repair
checker) and `ca7f9ef` (r90 work commit, 630-line pre-reconstruction boundary contract). At
seat start `git status --short` was empty; the seat created
`.ufo/waves/round-91/followup/` (it did not exist) and wrote only this file and `P4.md`. Every
measurement below is on the DELIVERED tree at `c2ab3d0`, never on a patch or a seat report's
intent. Scratch: `/tmp/p4` only (one 11-file cluster copy for inventory controls), swept at
seat end; the baseline checker and the e97613c checker were fed through `python3 -` via
`git show` without any scratch file. No commit, no push, no sibling-repo write, no
`SHONEN.md` edit, no axis verdict (axis judging is the judges' remit; this seat supplies the
delivery receipts the block cites).

## Work performed

- Pinned the revision and file state (HEAD, clean status, 77-file diff split, protected-file
  bytes, `SKILL.md` absence, line counts; §Revision state).
- Ran the two 60 s wait-checks on `.ufo/waves/round-91/followup/` (one background call,
  timestamps below): check 1 empty; check 2 found `H4-census.json`, `H4-lineage.json`,
  `H4-probes.json`; terminal found those plus `H4-c1-discrimination.json`, `JCAL5-delta.json`.
  Work proceeded with what existed; the wider sibling wave was read only after my own
  measurements, for corroboration only.
- Ran **my own 166-directory census** (baseline `a7c6a17` checker vs the delivered checker
  over every delivered fixture dir, comparing `(returncode, stdout, stderr)`, plus a git-tree
  dir delta) — the C1 census receipt reproduced independently (§Census).
- Ran the **two discriminating fixtures under both checkers**: delivered checker from the
  tree; `e97613c` checker via `git show e97613c:corpus/fixtures/check_bible.py | python3 -
  <dir>` — outputs differ exactly on the repaired lines and match both fixture READMEs
  (§Discriminating fixtures).
- Verified the **C9 watch pin**: `sha256sum corpus/fixtures/check_bible.py` equals the
  artifact's pinned hash; read the ruling, the reproducible boundary probe, and the four-gate
  falsification trigger (§C9 watch).
- Ran the **C2 receipt** — `corpus/tools/support_check.py` — on the r87 and r88-m3 clusters
  (exit 0 with `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8` and `10/10` respectively, the
  expected unreferenced-declaration WARN on r88-m3), plus **two negative inventory controls**
  on a `/tmp` copy (exit 2 with the documented `FAIL:` diagnostics) (§C2 receipt).
- Read the delivered **C3 additions** (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:37-108`),
  ran the R9 section's own verification command (11/11, exit 0), and checked each addendum
  against the C3 claim's "owner, trigger, worked example" wording (§C3).
- Audited the **boundary-document reconstruction** (`corpus/knowledge/holder-assessment-boundary.md`,
  delivered sha256 `c0c59daf…`) against `ca7f9ef` (630 lines) and the mis-landed r90
  instruction sheet (`a7c6a17:…`, 316 lines): diffstat, heading inventory, distinctive-phrase
  counts, decision-table duplicate rows, named-skip accounting (§Boundary-document audit).
- Established the **documentation and round-record state**: `corpus/fixtures/README.md`
  round sections, cluster READMEs, `.gitignore`, `LOG.md` headings and 2411-line tail,
  `SCORECARD.md` headings, and the proposal-only W2 artifacts (§Documentation surface).
- Drafted the SHONEN block for the round-91 report (§Findings) — `SHONEN.md` itself is a
  tracked file outside this seat's write scope; the block is a proposal only.

## Before → after measurements

All commands run from the lane root. "Before" = `a7c6a17` unless stated.

### Revision and file state

```sh
$ git rev-parse HEAD
c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
$ git status --short
(empty at seat start)
$ git diff --stat a7c6a17 c2ab3d0
 77 files changed, 11154 insertions(+), 227 deletions(-)
$ git diff --stat a7c6a17 c2ab3d0 -- SHONEN.md PROVINCE.md l0-questions.md
(empty)
$ git diff --name-only a7c6a17 c2ab3d0 | awk -F/ '{print $1}' | sort | uniq -c
     20 corpus
     57 .ufo
$ git diff --name-only a7c6a17 c2ab3d0 | grep -v '^corpus/' | grep -v '^\.ufo/'
(no output)
$ test -e SKILL.md && echo SKILL-PRESENT || echo SKILL-ABSENT
SKILL-ABSENT
$ git ls-files | grep -Ei 'skill'
(no output)
$ wc -l SHONEN.md PROVINCE.md l0-questions.md
  10 SHONEN.md
  11 PROVINCE.md
   5 l0-questions.md
```

`SHONEN.md` glyphs on the delivered tree: `:5 [ ]`, `:6 [~]`, `:8 [ ]`, `:9 [~]`; evidence
lines `:7` and `:10` still cite only round-1 pointers. `SHONEN.md` is byte-unchanged this
round (empty protected-file diff above).

### Own 166-directory census — `a7c6a17` checker vs delivered checker

```sh
$ python3 - <<'PY'   # baseline checker via git show; delivered checker from the tree
dirs_total 166
old_dirs_base 164
exits base {1: 134, 0: 32} deliv {1: 134, 0: 32}
changed_tuples 0 []
exit_flips []
stderr_diffs []
violation_lines base 421 deliv 421
new_dirs ['r91-c1-null-chain', 'r91-c1-tick-unresolved']
removed_dirs []
PY
```

Reading: **0 changed tuples + 2 new dirs of 166, 0 exit changes, 0 stderr changes**, 421
violation lines at both revisions, no removed dir. The delivered checker is byte-frozen:
`sha256sum corpus/fixtures/check_bible.py` and
`git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum` both print
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.

### Discriminating fixtures — delivered vs `e97613c` on the repaired lines

```sh
$ git show e97613c:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-null-chain
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible
provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got
None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only
0 is in the resolved index)
1 violation(s); no canon changed                              # EXIT=1
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed                              # EXIT=1
```

```sh
$ git show e97613c:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-tick-unresolved
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder
identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable
(2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must
be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible
provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not
uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed                              # EXIT=1
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible
provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not
uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed                              # EXIT=1
```

Both outputs equal the after-state blocks in the fixture READMEs; the null-chain line and the
tick line are the exact repaired lines; the tick fixture's chain-break line is byte-identical
across revisions. The two fixtures therefore fail a silent revert of either gate, as claimed.

### C9 watch (`corpus/knowledge/r91-c9-watch.md`)

- Pins "Delivered checker … at r90 closure `a7c6a17…`" and SHA-256 `ff9fd2aa…` — matches the
  delivered hash above.
- Carries the C9 ruling (tick inversion is a definite integer finding; holder-identity
  uncertainty does not qualify it), the reproducible boundary probe naming both fixtures, and
  a four-gate falsification trigger ("Reopen the ruling only when a demonstrated case shows
  that the integer tick finding itself needs holder-identity context").
- Owned by S1 for round 91, handed to the next C1 calibration owner at closure.

### C2 receipt — hardened support command, plus inventory controls

```sh
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
… 22 PASS lines …
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                    # EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… 10 PASS lines …
WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
RESULT PASS WITH WARNINGS                                      # EXIT=0
```

Negative controls (on `/tmp/p4/r91/tamper`, a copy of `r88-m3-maya-cluster`):

```sh
# declared 11 JSON facts vs 10 parsed rows
FAIL: expected JSON facts and editorial rows must sum to total mapped rows   # stderr; EXIT=2
# Expected-inventory line deleted
FAIL: map must contain exactly one expected inventory declaration            # stderr; EXIT=2
```

So the inventory assertion fires (a count edit or a dropped declaration cannot PASS
silently), and both observed diagnostics match the two M2 contract deviations now documented
in `corpus/tools/README.md` under "Named debt — S2 terminal-status contract" (missing
inventory exits 2; no `RESULT FAIL` terminal summary).

### C3 additions on the delivered tree (`r88-sourced-inspiration-decision-table.md`)

- R8 `:40-47`: failed-gate disposition + withhold-scope precedence ("the element is NOT proven
  influenced … the `R2` claim is not available … Withhold-scope precedence (decided r91):
  detail-level withholding wins over element-level when they conflict"). Owner is inherited
  from the R8 appendix ("**Owner:** the lore lane"); no explicit trigger or worked-example
  label for this addendum.
- R9 `:49-92`: "reprint boundary clarified r91" with explicit `**Owner:**` (`:51-53`),
  `**Trigger:**` (`:55`), `**Decision:**`, `**Worked example:**` (`:78`), and a
  `**Verification command**` (`:87-92`) that I ran — `R9 reprint decision completeness:
  11/11`, exit 0. The command reads `.ufo/waves/round-91/patches/D2-edges.patch` (a wave
  artifact, committed today) rather than a durable corpus file.
- R10 `:105-108`: "Namespace scoping (decided r91): `source_id` values are cluster-local
  identifiers … comparison keys are `(cluster-relative path, source_id)` pairs … A collision
  alone never enters the register." No explicit owner/trigger/worked-example labels for this
  addendum (owner inherited from the R10 appendix).

### Boundary-document audit — the r91 reconstruction vs `ca7f9ef`

```sh
$ git diff --stat ca7f9ef c2ab3d0 -- corpus/knowledge/holder-assessment-boundary.md
 1 file changed, 91 insertions(+), 172 deletions(-)     # 630 lines → 549 lines
$ sha256sum corpus/knowledge/holder-assessment-boundary.md
c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9
```

Heading inventory (delivered vs `ca7f9ef`): the delivered doc has one duplicated H1 (`:1`,
`:8`) and six H2 sections; `ca7f9ef` had one H1 and nine H2 sections. Absent after
reconstruction: `## The contract (round-1 baseline paragraph, kept)` (`ca7f9ef:62`),
`## Commands (self-contained, run from the lane root)` (`ca7f9ef:319`), `## Status split`
(`ca7f9ef:578`). Four "Commands" cross-references remain in the delivered text.

Distinctive r89 limit-bullet phrases — presence count delivered / `ca7f9ef`:

```text
0 / 1  Emission order is asymmetric          0 / 1  Three states, not two
0 / 1  Ambiguous SOURCE is not a stop cause  0 / 1  No truth claims
0 / 1  Measurement ceiling                   0 / 1  One form, one boundary
0 / 1  Causes are collected, not selected    0 / 1  Everything else continues
0 / 1  A duplicated item id arms             0 / 1  Chain eligibility is no longer
```

`grep -n 'skip\|debt'` on the delivered doc → exactly one hit, `:6`, which names a single
skipped item: "Skipped as named debt: D1 — Decision-table row 2 code refs." The r91 campaign
wording "2 items named as skipped debt" is therefore not supported by the delivered file.

Other delivered-tree defects measured:

- **Falsified duplicate row.** The Decision table carries two rows with the same state key
  ("A referenced holder ID is **not uniquely resolvable**…"): `:179` (r89 text — promises the
  hedged tick form `… holder identity is not uniquely resolvable: {details}; provenance tick …`,
  refs `:327-333`, `:334-344`, `:345-350`) and `:184` (r90 text — "Tick findings are NOT
  qualified", refs `:330-335`, `:339-341`, `:323-326`). The delivered checker emits only the
  `:184` form (probe `r91-c1-tick-unresolved` above), so `:179` documents retired behavior.
- **Structural splices.** Truncated scope bullet `:227-229` ("… at the first stop and ALL
  later") running into the orphaned code-block lead-in `:243` ("are pinned in
  `reports/round-1/current-baseline.json`):"). Spliced revision prose `:37-40`
  ("… at `ca7f9ef` (`…/round-90/followup/CB1.md`)\ndelivered checker at `1b09f3f`\n
  (`…/round-89/followup/CB1.md`); …"). Two `verified-at:` openers (`:46`, `:51`). Stale r89
  banner `:9-16` under the new r91 reconstruction comment `:3-6`.
- **Stale revision labels.** `1b09f3f` occurs 15× in the delivered doc (20× at `ca7f9ef`);
  the `## First-stop causes (delivered 1b09f3f)` heading (`:139`) still names the r89 revision.
- **The r90 sheet's in-place edits that did not land:** row-2 code refs (`:185` area, still
  `:343-344`, `:349-350`, `:333` — the one *named* skip), the new D2 limits bullet, the D6/D7
  cause-section anchor remap, and the D9/D13 relabels. Only 1 of these is named in the doc
  header.

Same-wave corroboration (read after my own measurements): `followup/CB1.md` ("the
reconstruction lost three sections"; "12 of 13 r89 limit bullets lost, Commands body grafted
inside"; D4/D6/D7/D9/D13 unapplied) and `followup/H5.md` (A4 "not improved — 1 of the brief's
2 skipped items is honestly named; the other is absent"; F1/F4/F5/F6/F7; it also reports 9 of
the claimed 10 sections verifiably present, ≥4 unapplied). `followup/H4.md` independently
reproduces the census (0 changed + 2 new of 166) and the discrimination of the two new dirs;
`followup/JDEP4-check.md` reports the e97613c-fed run as `REGRESSION-DETECTED`, exit 2;
`followup/JDEP3.md` reads the R10 namespace text at `:105-108` and finds the register
correctly absent.

### Documentation surface and round-record state

```sh
$ grep -n "^## Round" corpus/fixtures/README.md | tail -3
1012:## Round 89: cause branches + support completion
1016:## Round 90: hedged-shapes repair + support machinery
$ grep -n "r91-c1\|Round 91" corpus/fixtures/README.md
(no output)
$ grep -n "holder-assessment-boundary" corpus/fixtures/README.md
1006:… see `corpus/knowledge/holder-assessment-boundary.md` for the current contract.
1014:… First-stop cause contract: `corpus/knowledge/holder-assessment-boundary.md` (r89 refresh).
```

So the two new r91 fixtures are unindexed in `corpus/fixtures/README.md`, and `:1014` still
labels the contract "(r89 refresh)". The cluster READMEs (`r87-myth-cluster/README.md`,
`r88-m3-maya-cluster/README.md`) mention neither `support_check` nor `claim-excerpt-map`
(Q89-016 carried). `.gitignore` now carries `__pycache__/` (r90 B3 discharged); no
`corpus/tools/__pycache__/` exists. `LOG.md` (2411 lines) has headings at `:1699` (r87),
`:1908` (r88), `:2256` (r90, running to EOF); the r89 record is unheaded (`:2089-2253`); there
is no r91 record. `SCORECARD.md` ends at `## Round 90 — luna round 4 of 12` (`:220`); both
files are byte-unchanged in the r91 delta. The r91 LOG/SCORECARD/report entries exist as
proposals only (`.ufo/waves/round-91/patches/W2-log-r91.proposal.md`,
`W2-scorecard-r91.proposal.md`, `W2-report-r91.skeleton.md`).

## Findings & named debt

Per-box verdicts on the delivered glyphs at `c2ab3d0` (this seat makes no axis verdict):

- **Box 1 — `SHONEN.md:5` `[ ]` "SKILL.md contains real decision tables, error patterns,
  checklists, cited sources" — unchanged.** No `SKILL.md` exists (`test -e SKILL.md` →
  ABSENT; `git ls-files | grep -Ei 'skill'` → no output). The r91 material (C9 watch, R8/R9/R10
  addenda, the tools README checklist) does not live in a `SKILL.md`.
- **Box 2 — `SHONEN.md:6` `[~]` "At least one end-to-end domain task executed and logged in
  LOG.md" — lane assertion retained; evidence improved.** LOG records now: r87 `:1699`, r88
  `:1908`, the unheaded r89 record `:2089-2253`, r90 `:2256-2411`. Round 91 adds the
  166-dir census (0 changed, 0 exit/stderr changes, 421 violation lines both revisions), the
  two discriminating fixtures (both README after-states replayed), the C9 watch pin, the
  support receipts (`14/14+8/8`, `10/10`+WARN) with two inventory controls, and the C3
  decisions. r91's own LOG entry is unlanded (proposal only). The box's evidence pointer
  (`:7`) is stale (round-1 only); recommend adding `LOG.md:1699`, `:1908`, `:2089`, `:2256`.
  No external promotion verification → no `[x]`.
- **Box 3 — `SHONEN.md:8` `[ ]` "Instructions executable by an agent without oral context" —
  proposal: RETAIN `[ ]` (do not move to `[~]` in this round).** Positive evidence measured on
  the delivered tree would, on its own, support `[~]` as r90's P4 proposed: a committed,
  documented, reproducible command (`corpus/tools/support_check.py` + `corpus/tools/README.md`)
  returns exit 0 with per-category receipts and enforced inventory/anchor checks; the two
  documented contract deviations are named rather than hidden. The blocking bound is the
  contract file itself: `corpus/fixtures/README.md:1006` names
  `corpus/knowledge/holder-assessment-boundary.md` as the current contract, and the delivered
  revision (a) documents retired behavior in decision-table row `:179` — the r89 hedged tick
  form the delivered checker no longer emits, falsified by `r91-c1-tick-unresolved` and
  contradicted by the corrected row `:184` — and (b) lost three section headings and ten
  boundary bullets present at `ca7f9ef` (emission order, ambiguous-SOURCE non-stop, three
  states, no-truth-claims, measurement ceiling, …). Under r90-P4's own safe criterion ("no
  delivered instruction now describes retired behavior"), this fails. After a verified
  contract repair, `[~]` is supported. Other bounds: no Round-91 section in
  `corpus/fixtures/README.md` (r91 fixtures unindexed; `:1014` still says "(r89 refresh)");
  cluster READMEs still omit the maps and the command (Q89-016 carried); R9's verification
  command cites a committed wave patch; no named non-author cold-execution record exists.
- **Box 4 — `SHONEN.md:9` `[~]` "No cross-domain bleed (PROVINCE.md still accurate)" — lane
  assertion retained; evidence strengthened.** `PROVINCE.md` byte-unchanged (11 lines),
  `l0-questions.md` untouched (5 lines), `SHONEN.md` unchanged; all 77 changed paths are under
  `corpus/` (20) or `.ufo/` (57); every changed path check in §Revision state passes. The new
  surfaces keep the province's separations: `r91-c9-watch.md` states the ruling "is a
  statement about the checker's local integer ordering rule, not real-world chronology, source
  reliability, ownership, or canon"; `corpus/tools/README.md` states the check is "a
  reproducible lexical preflight, not a judgment that the whole claim is supported … or
  canonical"; the R8/R9/R10 addenda keep attribution / rights / AI-training separate and
  assert no rights conclusion.

**Blocking-check result:** the checker freeze holds (`ff9fd2aa…` at `a7c6a17`, in the
worktree, and pinned by the C9 watch) and the census reproduces exactly; the blocking finding
this round is the boundary-document regression above, not checker drift.

**Named-debt discrepancy (for the closure record):** the campaign wording "10 of CB1's r90
sections applied … 2 items named as skipped debt" is not supported by the delivered tree: the
doc header (`:6`) names exactly one skipped item (D1); the row-3 replacement text *is*
present (as the corrected `:184` row) but the stale `:179` row it should have replaced
remains. Independent same-wave seats reach the same conclusion (`followup/H5.md` F1/F4/F5;
`followup/CB1.md` §applied/skipped).

### Proposed SHONEN block for the round-91 report (proposal only — do not edit `SHONEN.md`)

> `SHONEN.md` is unchanged this round (`git diff --stat a7c6a17 c2ab3d0 -- SHONEN.md` →
> empty); four boxes at `SHONEN.md:5,6,8,9` (`[ ]`, `[~]`, `[ ]`, `[~]`). No `[x]` is
> claimed — no named non-author verifier has been asked to execute the lane's instructions
> cold. Drafted by follow-up seat `P4` (`followup/P4-shonen.md`); the boundary-document
> regression (row `:179` falsified by the delivered checker; three headings and ten boundary
> bullets lost vs `ca7f9ef`) is the blocking bound on box 3.

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists,
  cited sources* — **unchanged.** No `SKILL.md` exists (`test -e SKILL.md` → ABSENT). R91's
  decision material (`r91-c9-watch.md`, the R8/R9/R10 addenda, `corpus/tools/README.md`) does
  not live in a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* —
  **lane assertion retained; evidence improved.** Pointers: `LOG.md:1699` (r87), `:1908`
  (r88), `:2089` (r89 record, unheaded), `:2256` (r90), `reports/round-1/baseline-probes.json`.
  Round 91 adds a fourth delivered end-to-end set: 166-dir census (0 changed + 2 new, 0
  exit/stderr changes, 421 violation lines both revisions), the two discriminating fixtures
  (`r91-c1-null-chain`, `r91-c1-tick-unresolved` — both fail a silent revert of the repaired
  lines), the C9 watch pin + falsification trigger, the support receipts
  (`14/14+8/8` and `10/10`+WARN, exit 0) with negative inventory controls (exit 2), and the
  C3 R8/R9/R10 decisions. r91's own LOG entry is a proposal only
  (`.ufo/waves/round-91/patches/W2-log-r91.proposal.md`).
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* —
  **proposal: retain `[ ]`; do not promote to `[~]` until the contract repair lands.**
  Positive, measured: `python3 corpus/tools/support_check.py <cluster>` (documented in
  `corpus/tools/README.md`) returns exit 0 with `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS
  8/8; … RESULT PASS` (r87) and `10/10` + an expected WARN (r88-m3); inventory edits or a
  dropped declaration return exit 2 with named diagnostics; M2's two contract deviations are
  README-documented. Blocking bound: `corpus/fixtures/README.md:1006` names
  `corpus/knowledge/holder-assessment-boundary.md` as the current contract, and the delivered
  revision contains a decision-table row (`:179`) documenting the retired r89 hedged tick form
  — falsified by `r91-c1-tick-unresolved` output and contradicted by the corrected row `:184`
  — plus lost headings/bullets (vs `ca7f9ef`: `## The contract`, `## Commands`,
  `## Status split`; ten distinctive boundary bullets 0/1). Bounds also: no Round-91 section
  in `corpus/fixtures/README.md` (fixtures unindexed; `:1014` still "(r89 refresh)"); cluster
  READMEs omit maps/command (Q89-016); R9's verification command cites a wave patch.
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — **lane
  assertion retained; evidence strengthened.** `PROVINCE.md` bytes unchanged (11 lines; `:3-11`
  resolves), `l0-questions.md` untouched (5 lines), all 77 changed paths under `corpus/` (20)
  or `.ufo/` (57), no non-corpus path changed; the new surfaces state explicitly that the C9
  ruling and the support check make no canon/rights/real-world claim.

## Handoff

- **Deliverables:** `.ufo/waves/round-91/followup/P4-shonen.md` (this file) and
  `.ufo/waves/round-91/followup/P4.md` (seat note). No tracked file was written outside the
  seat's allowed paths; no commit, no push, no sibling-repo write, no `SHONEN.md` edit.
- **Judged revision:** `c2ab3d0` (baseline `a7c6a17`; `e97613c` used only as the pre-repair
  checker via `git show`, `ca7f9ef` only as the pre-reconstruction doc revision). Checker
  freeze verified (`ff9fd2aa…`); census reproduced (166 dirs, 0 changed + 2 new); support
  receipts reproduced; C9 watch pin matches.
- **Headline for L1:** all four boxes keep `[~]`/`[ ]` in the delivered file; the block
  retains box 2 `[~]` and box 4 `[~]` with improved evidence pointers, keeps box 1 `[ ]`
  (no `SKILL.md`), and proposes **box 3 stays `[ ]`** because the reconstruction left the
  current contract (`corpus/knowledge/holder-assessment-boundary.md`) documenting retired
  behavior (row `:179`) and missing boundary content; the support-command evidence alone
  would support `[~]` after that repair. No `[x]` is claimed.
- **Named debt handed forward (all outside this seat's write scope):** (1) repair or
  explicitly retire decision-table row `:179` and re-anchor the decision table (the row-2
  code-refs skip named at `:6`; D6/D7/D9/D13 unapplied per `followup/CB1.md`); (2) restore or
  explicitly retire the three dropped headings, the ten lost limit bullets, and the dangling
  "Commands"/"emission-order" cross-references; (3) clean the reconstruction seams (duplicate
  H1 `:1`/`:8`, stale r89 banner `:9-16`, spliced prose `:37-40`, dual `verified-at:`,
  truncated scope bullet `:227-229` / orphan lead `:243`); (4) land a Round-91 section in
  `corpus/fixtures/README.md` (and fix `:1014`'s "(r89 refresh)"); (5) extend the cluster
  READMEs with the maps and support command (Q89-016 carried); (6) prefer a durable corpus
  target over the wave patch in R9's verification command; (7) record honestly in the closure
  that only one skipped item is named, not two.
- **Process notes:** the two 60 s wait-checks ran at `08:32:56`/`08:33:56` with terminal
  `08:34:56 -03:00`; the follow-up dir (created by this seat) then held the sibling wave's
  `H1`–`H5`, `JCAL1/2/3/5`, `JCOV1/3/4`, `JDEP1/3/4`, `CB1`, `K1`, `P3-log-r91`, `SE2`, `V2`,
  `W1` artifacts at seat end, read for corroboration only after my own measurements. `/tmp`
  inode preflight: `1048576` inodes, `1890` free at seat start; my only scratch (`/tmp/p4`,
  one 11-file cluster copy + two output captures) was swept (`rm -rf /tmp/p4`) — no archive
  files were created. At seat end the working tree holds the sibling artifacts untracked
  (and `Q1`-era files committed); none of it is mine.