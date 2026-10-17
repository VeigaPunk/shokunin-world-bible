# JDEP4 — Capabilities assessment (round-91 FOLLOW-UP)

Seat JDEP4, world-bible lane (`lore-shokunin`). Judged tree: delivered HEAD
`c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (work `6332115` + amendment
`c2ab3d0`; baseline `a7c6a17`). `git status --porcelain --untracked-files=no`
was empty at seat start and end; the only untracked path is
`.ufo/waves/round-91/followup/` itself. All probes ran from
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No tracked file was modified; no
commit or push. Scratch: none (the e97613c checker source was fed through
`python3 -`/`python3 -c` pipelines; no `/tmp` file or directory was created —
`/tmp` sat at `IFree=1770..1880`, inode pressure).

**Question posed to this seat:** recommend for or against a THIRD `capabilities`
row, candidate *regression-discrimination fixtures* — the r91 pair
(`r91-c1-null-chain`, `r91-c1-tick-unresolved`) plus
`corpus/knowledge/r91-c9-watch.md` claimed as a durable mechanism to detect
silent checker regressions. Evidence must be a runnable command.

**Recommendation: FOR — admit a third row, narrowly phrased as
`checker-regression discrimination` and carrying the bounds in F2.** The round
demonstrates the capability running: the pair discriminates the pre-repair
`e97613c` checker from the delivered checker on exactly the repaired lines, the
C9 watch pins the shipped hash and expectations (corpus-resident, tracked), an
independent census pins the two added rows (`0 changed + 2 new of 166`), and a
mechanical check returns `DISCRIMINATION HELD` on the delivered tree versus
`REGRESSION-DETECTED` when the pre-repair source is fed as the checker. See
`followup/JDEP4-check.md` (verbatim script) and `followup/JDEP4-evidence.json`
(all raw receipts).

## Work performed

- Read `AXES.md` §Capabilities (row contract: name → what it can now do →
  evidence pointer → first-working round; "Rows enter only through a round that
  demonstrates the capability running; a capability without a passing
  demonstration in the round report is pre-claiming"), the delivered
  `SCORECARD.md` capabilities table (two rows; the r90 note "no third row
  (JDEP4's pre-claiming argument accepted); row 2's evidence pointer updated to
  the corpus-resident commands"), the r90 follow-up JDEP4 (the "against a third
  row as phrased" precedent and its F4 bar: "a command returns the decided
  verdict"), the r91 wave spec C1 claim, and the r91 C1 work seats
  (X1/F2/B3/C5/C8/C10/CB1/S1) plus Q1's debt ledger and r92 proposal.
- Ran the delivered-tree probes below: identity/pin, the two fixtures under
  both checkers, an independent 166-dir census against B1's committed manifest,
  census path-sensitivity control, the mechanical regression check in both
  delivered and revert-simulation modes.
- Two 60 s dependency wait-checks (one background call, timestamped):
  `08:33:12` and `08:34:12`, checked for `JDEP1-3/JDEP5/P1/P2/Q1/Q2/K1/
  W2-scorecard` artifacts in `followup/` — none present in the window.
  Post-window listing found `H4.md` + `H4-*.json` (08:33:29–08:34:59) and
  `JCAL5-delta.json` (08:35:08); both were cross-checked against this seat's
  independent measurements and agree exactly (M7).

## Before → after measurements

**M1 — delivered identity and the pinned checker.** Commands and observed
output:

```sh
git rev-parse HEAD                                   → c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
git status --porcelain --untracked-files=no          → (empty)
sha256sum corpus/fixtures/check_bible.py
git show e97613c:corpus/fixtures/check_bible.py | sha256sum
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

The delivered hash equals the value pinned in `corpus/knowledge/r91-c9-watch.md`
(pin occurs once; watch and both fixture directories are tracked at `6332115`).

**M2 — the pair under the delivered checker** (the watch's own commands,
verbatim; both exit 1 by design because the fixtures carry intentional
violations):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed                                        exit=1

VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed                                        exit=1
```

**M3 — the same pair under the pre-repair `e97613c` checker** (silent-revert
target; no scratch files):

```sh
git show e97613c:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-null-chain
git show e97613c:corpus/fixtures/check_bible.py | python3 - corpus/fixtures/r91-c1-tick-unresolved
```

```text
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
1 violation(s); no canon changed                                        exit=1

VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed                                        exit=1
```

Each fixture differs from its delivered output by exactly one line pair (the
repaired line); the tick fixture's qualified chain-break line is byte-identical
under both checkers. This reproduces X1/C5/C8/C10's receipts independently.

**M4 — mechanical regression check (the runnable command answering the
mission).** Script verbatim in `followup/JDEP4-check.md`; it parses both README
expectation blocks, asserts byte-exact delivered stdout, asserts the phrase
gates (definite `got None` with no vacuous clause; integer-only tick with the
qualified chain-break retained), and it runs the e97613c source as a wrapper
for the differential. Observed:

```text
run_check delivered
mode=delivered checker_sha256=ff9fd2aa... matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0

run_check e97613c          # pre-repair source executed as the checker
r91-c1-null-chain: ... README_exact=False ... pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: ... README_exact=False ... pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
exit=2
```

**M5 — independent census at the delivered tree.** Command: one
`python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<dir>` per direct
fixture dir (repo-relative args, cwd repo root), tuples `(exit, stdout
sha256, violation count, stderr len)` compared path-wise against the committed
baseline authority `.ufo/waves/round-91/patches/B1-tuples.json`
(sha256 `5433f6af7b7dcee2989eb4354b20e944aab76ea2305af6c06814911f2ae0a6e1`),
and the same 166 dirs re-run with the e97613c source for the old↔new delta:

```text
shared=164 added=['r91-c1-null-chain', 'r91-c1-tick-unresolved'] removed=[] tuple_mismatches=0
delivered_exits={0: 32, 1: 134} violations=421 stderr_nonempty=0
old_vs_new_166: changed=2 paths=['r91-c1-null-chain', 'r91-c1-tick-unresolved'] exit_changes=0
  r91-c1-null-chain      new=615dc0564f531352 old=3a337ba4bba9c829
  r91-c1-tick-unresolved new=d754e96f7c01e6fb old=71b4ea433d85ba52
```

This independently reproduces the claimed "0 changed + 2 new of 166", with the
"+4 violations" (1+3) exactly the two added dirs. Method note: a first pass
using absolute-path arguments reported 5 false mismatches (same exits and
counts, different stdout bytes) — see M6.

**M6 — census path-sensitivity control.** Relative vs absolute argument, all
166 dirs:

```text
path_sensitive_fixtures=5 ['r5-missing-file', 'r62-missing', 'r67-claim-source-unavailable-control', 'r67-claim-source-unavailable-empty', 'r67-claim-source-unavailable-whitespace']
example rel: ... [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
example abs: ... [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
```

The missing-file error text embeds the invocation path, so a drift census must
use the documented repo-relative invocation or it manufactures 5 false
positives.

**M7 — dependency waits and sibling cross-checks.** Timestamped checks:

```text
=== CHECK 1 at 2026-10-17T08:33:12-03:00 ===
=== CHECK 2 at 2026-10-17T08:34:12-03:00 ===
TERMINAL-DONE
```

No `JDEP1-3/JDEP5/P1/P2/Q1/Q2/K1/W2-scorecard` artifact existed in the window
(gap noted, non-blocking). Post-window, `H4.md`/`H4-census.json`/
`H4-c1-discrimination.json` and `JCAL5-delta.json` had landed; cross-check:
H4's census (166/164/2 added/0 changed, exits `{0:32,1:134}`, 421 violations)
and its delivered stdout hashes `615dc056…`/`d754e96f…` are identical to M5,
and JCAL5's `cross_check` reports B1/B2 164 rows with 0 mismatches. Two seats
plus this one agree on every number.

**M8 — post-window cross-check (dated addendum, completed wave; after 08:44).**
The full follow-up roster landed after this seat's two checks (JDEP1/2/3,
JAXIS, P2, Q1/Q2, W1, P3, V2, SE2, H1/H2/H3/H5, JCAL1–5, JCOV1–4, CB1, E1,
P4). Seats bearing on this verdict, read and cross-checked:

- **JAXIS** (axis-verdict synthesizer, 08:43; recommendation only — L1 owns the
  verdict): claim-verification note 5 transmits this seat's recommendation —
  "JDEP4 (with JDEP4-check.md's runnable mechanical companion) recommends
  **FOR** a third row — `checker-regression discrimination` — with the F2
  bounds attached (scope, raw-output receipts, wave-resident wrapper,
  path-convention, prospective trigger). This reverses r90's 'against' for the
  reason r90 wrote it: the capability now runs, with a mechanical verdict
  (exit 0 `DISCRIMINATION HELD` vs exit 2 `REGRESSION-DETECTED`)." JAXIS's own
  receipts agree with M1–M6: census 166 / exits `{0:32,1:134}` / 421
  violations / stdout differing only on the two added dirs; single-gate
  reverts flip only their own fixture (corroborated by JCAL2's X2/X3 reverts
  and V2's hybrids). No JAXIS finding contradicts M4.
- **P2-scorecard-r91.md:185** (scorecard proposal, 08:41): the contrary
  classification — "Capabilities: no third row — C1 is regression coverage and
  C2 is hardening of the existing capability, not new repertoire", plus a
  row-2 pointer update from C2's hardening. P2 does not cite this seat's
  report; JAXIS read both and transmits mine. This is the wave's one open
  disagreement, addressed in F4.
- **Other seats** (JDEP1/2/3, JCOV1–4, JCAL1–5, H1–H5, Q1/Q2, K1, W1, P3):
  none disputes the discrimination or census evidence; none rules the
  capabilities classification. JAXIS's debt list consolidates M6 as **CAL-D4**
  (census path-convention sensitivity, with JCAL1-4), matching this report.

## Findings & named debt

**F1 — Recommendation: FOR a third row, bounded.** Proposed row text:

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| checker-regression discrimination | Detect a silent revert of the r90-repaired checker gates: the pinned SHA-256 plus the two durable differential fixtures (`r91-c1-null-chain`, `r91-c1-tick-unresolved`) pin the definite null-chain `got None` wording and the integer-only tick wording, so a revert reproduces the hedged `e97613c` lines and diverges from the tracked delivered receipt | `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa…`; `python3 corpus/fixtures/check_bible.py corpus/fixtures/{r91-c1-null-chain,r91-c1-tick-unresolved}` → definite lines (both exit 1 by design); differential `git show e97613c:corpus/fixtures/check_bible.py \| python3 - corpus/fixtures/r91-c1-null-chain` → hedged line; mechanical companion `followup/JDEP4-check.md` → `DISCRIMINATION HELD` (exit 0) vs `REGRESSION-DETECTED` (exit 2) | r91 |

Grounds: (a) the capability ran in the round, with receipts — M2/M3/M5, plus
X1/C5/C8/C10's independent replays; (b) it is corpus-resident and durable —
fixtures, READMEs, and the watch are tracked at `6332115`, and the watch pins
the hash plus expected lines and names a falsification trigger; (c) it closes
the exact r90 named bound ("the repaired shapes have no discriminating durable
fixture — a silent revert would evade every census", Q90-001); (d) the r90
"against" precedent fails here for the reason it was written — r90's candidate
had no runnable demonstration at all, while this one discriminates, is
independently verified, and returns a mechanical verdict (M4). Row 2's own
precedent (admitted at r89 with a wave-resident pointer, later updated to
corpus-resident at r90) is at least as permissive.

**F2 — Bounds the row must carry (named, not netted).**
(i) Scope is the two r90-repaired gates; other semantic checker changes are
visible only through comparing the printed hash against the pin, not via these
fixtures.
(ii) The watch's commands are raw-output receipts — both fixtures exit 1 by
design, so detection is the comparison of printed lines/hashes against the
pinned expectations, not an exit code.
(iii) The pass/fail wrapper is currently wave-resident (`X1.md`'s tracked
verifier; this seat's `JDEP4-check.md`). If L1 reads the r90 F4 bar strictly
("a command returns the decided verdict", corpus-resident pointer), a
corpus-resident wrapper is the one polish item that would satisfy it; this
seat does not treat its absence as disqualifying, for the row-2 precedent
above.
(iv) A full-census drift comparison must use repo-relative fixture arguments
(M6).
(v) The C9 falsification trigger remains prospective and untouched.

**F3 — Named debts adjacent to this verdict.**
- The census invocation-path sensitivity (M6) is a methodology bound for any
  future drift census; H4's and B1's use of relative paths is the correct
  convention.
- `Q1-r92-proposal.md` (work wave) proposes "making the r90 repaired
  provenance rules regression-visible" as r92 C1 work "from the currently
  scratch-tested r91 C1 candidate" — at the delivered tree that work is already
  done, tracked, and watch-pinned (`6332115`). That candidate is satisfied
  ahead of plan; L1/Q1 should reconcile the proposal rather than re-run it.
- Carried from H4 (not this seat's remit, unchanged at r91): the three
  ambiguous r85 probes still do not match their sealed `.txt` receipts under
  any generation since r86; and B1/B2 manifests are semantically identical but
  not byte-equal — compare tuples, not file bytes.
- Followup artifacts for `JDEP1-3/JDEP5/P1/P2/Q1/Q2/K1` were absent in this
  seat's wait window (M7); this judgement uses the delivered tree, the work
  artifacts, and the two landed followup receipts only. *(Superseded by the
  completed-wave state recorded in M8.)*

**F4 — reconciliation with P2's "no third row" classification (open item for
L1; this seat's verdict unchanged).** `P2-scorecard-r91.md:185` classifies C1
as "regression coverage … not new repertoire" and would leave the repertoire
table at two rows (adding only the row-2 pointer update from C2). This seat's
FOR stands on the admission rule as written: (a) `AXES.md` §Capabilities admits
a row through "a round that demonstrates the capability running" — r91 does,
and M4's mechanical verdict is the strongest evidence class used for any row so
far; (b) the table's charter sentence is "what the shokunin can now *do*" —
before r91 a silent revert of either repaired gate evaded every census (the r90
record's own Q90-001 bound), after r91 it does not; (c) precedent: row 1 (r88)
is likewise an instrument-behaviour admission (the checker's per-record
disclosure), so P2's line separates the candidate from row 1 only by the
first-order/second-order difference, not by a stated rule. P2's classification
call is defensible; if L1 holds the table to content-facing abilities only, the
correct outcome is **no third row**, with the mechanism carried by the
calibration-axis record plus the F2 bounds — the two artifacts are
reconcilable, and L1 should adopt one classification rather than blend them
(no row while citing the fixtures as a capability would be the worst of both).
Under either classification, entering the row without the F2 bounds would be
the pre-claiming error r90 named.

## Handoff

- **Verdict: FOR a third capabilities row — `checker-regression
  discrimination`, r91 — with the F2 bounds attached.** The runnable evidence
  required by the mission is `followup/JDEP4-check.md` (run from
  `lore-shokunin/`: delivered → exit 0 `DISCRIMINATION HELD`; `e97613c` source
  → exit 2 `REGRESSION-DETECTED`), supported by M1–M6 raw receipts in
  `followup/JDEP4-evidence.json`.
- Files written by this seat: `followup/JDEP4.md`, `followup/JDEP4-evidence.json`,
  `followup/JDEP4-check.md`. No tracked-file edits, no commit, no push, no
  sibling-repo writes; no scratch remained.
- Gaps / live conflict: the full follow-up roster landed after this seat's wait
  window (M8). JAXIS (08:43) transmits this FOR recommendation with the F2
  bounds; `P2-scorecard-r91.md:185` proposes the opposite classification
  ("no third row") — see F4 for the reconciliation and the fallback if L1
  adopts P2's reading. P2's proposal and `P3-log-r91.md:176` ("capabilities
  table is unchanged") currently reflect the pre-JDEP4 state; if L1 adopts FOR,
  both need the corresponding closure update. All other seats either agree
  with this seat's discrimination/census numbers or are silent on the
  classification. Full axis verdicts and SCORECARD bookkeeping remain with L1;
  this seat rules only the capabilities question.