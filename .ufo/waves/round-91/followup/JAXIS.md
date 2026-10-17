# JAXIS — Axis-verdict synthesizer (round 91 follow-up, world-bible lane)

Seat JAXIS. Judged tree: **delivered** `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7`
(`c2ab3d0`; work commits `6332115` + `c2ab3d0`), baseline `a7c6a1773d5994246a76e4eff30d645f161920e0`.
Every verdict below rests on delivered-tree artifacts: my own re-runs are pasted under
"Before → after measurements", and each seat-cited number names the follow-up report that
carries its receipt. Scratch was `/tmp/jaxis-r91/` only (2 files; swept at close); no commit,
no push.

**This file is a RECOMMENDATION to the L1, not the round's verdict.** The L1 owns the admission
decision and the SCORECARD wording. Per-axis verdicts use the lane's standing rule —
`improved / harmed / unchanged / unprovable-but-better` — and a trade anywhere is NOT an
improvement.

## Work performed

- Wait protocol. Two 60 s polls (r90-Q2-P1 pattern): checks at
  `08:32:34` (followup/ created, empty), `08:33:34` (`H4-probes.json`), `08:34:34`
  (H4 x4 + `JCAL5-delta.json`), terminal `poll_done=true` at `08:34:34`.
  Extended poll (r90 JAXIS precedent) to `08:36:58`: `J_md_count` 0 → 2 → 7,
  terminal `j_reports_present=true 2026-10-17T08:36:58-03:00`. Final poll for
  `JCAL1/JCAL4/JCOV2/JDEP2` (60 s cadence): `JCAL1.md` and `JDEP2.md` landed during it;
  terminal `TERMINAL deadline reached; missing=[JCAL4] 2026-10-17T08:43:32-03:00` —
  `JCAL4.md` (and any JCAL4 receipt) was never observed. (My first poll's `printf` mis-rendered the
  check timestamps — shell `printf: --` — but emitted every file listing and the terminal
  line; mtimes serve as the per-file arrival ledger.)
- Read all landed `followup/J*.md` — **12 seats**: `JCAL1`, `JCAL2`, `JCAL3`, `JCAL5`,
  `JCOV1`, `JCOV2`, `JCOV3`, `JCOV4`, `JDEP1`, `JDEP2`, `JDEP3`, `JDEP4` (+ `JDEP4-check.md`,
  the seat's runnable companion). J JSON receipts consulted where they carry the numbers:
  `JCAL1-delta.json`, `JCAL2-receipts.json`, `JCAL3-receipt.json`, `JCAL5-delta.json`,
  `JDEP1-replay.json`, `JDEP3-namespace.json`, `JDEP4-evidence.json`.
- Non-J follow-up seats read for cross-cutting findings: `H1` (tree-diff + conformance +
  boundary-doc audit), `H4` (live probes + lineage), `H5` (doc-state judge),
  `V2` (delivered-revision verifier), `SE2` (sentinel), `K1` (connector),
  `W1` + `W1-disposition.json` (clerk). **Gap:** no `JCAL4.md` (or JCAL4 receipt) at write
  time; the wave's phase-2 roster is not persisted anywhere I could read, so I cannot say
  whether `JCAL4`/`JCOV5` were dispatched. If either lands later, the L1 should fold it in.
- Independent re-runs on the delivered tree (cwd `lore-shokunin/`, scratch `/tmp/jaxis-r91/`):
  checker hash at HEAD/worktree/e97613c; a full 166-directory census with the delivered
  checker against the `e97613c` checker (stdout/exit/stderr per directory); both r91 fixtures
  under both checkers including the README expectation blocks; the support command on r87 and
  r88-m3; the C9-watch file and its probe; the `a7c6a17..c2ab3d0` decision-table diff and the
  R9 embedded verification command; boundary-doc lineage hashes, heading/stamp counts, and a
  hunk-level diff `e97613c..c2ab3d0` to enumerate which CB1 r90 sections actually landed.

## Before → after measurements

**Tree identity and checker freeze (my run).**

```sh
git rev-parse HEAD
sha256sum corpus/fixtures/check_bible.py
git show e97613c:corpus/fixtures/check_bible.py > /tmp/jaxis-r91/check_bible_e97613c.py && sha256sum /tmp/jaxis-r91/check_bible_e97613c.py
```

```text
c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  /tmp/jaxis-r91/check_bible_e97613c.py
```

The r91 checker is byte-identical to the r90-closure `ff9fd2aa` baseline and is absent from
the r91 diff; the C9 watch pins the same hash. Corroborated by JCAL1/JCAL2/JCAL3/JCAL5, H1,
H4, V2, JDEP4, K1, JCOV2/JCOV3 (each with its own command).

**Census — 166 dirs, delivered vs `e97613c` (my harness, one process per dir per checker).**

```text
dirs=166
delivered exits={1: 134, 0: 32} violations=421
baseline  exits={1: 134, 0: 32} violations=421
changed_stdout=['r91-c1-null-chain', 'r91-c1-tick-unresolved']
exit_flips=[]
new fixtures: r91-c1-null-chain rc=1/1 violation; r91-c1-tick-unresolved rc=1/3 violations
```

Delivered-over-all-dirs differs from the `e97613c` checker **only on the two new fixtures**;
exits and stderr never move. The 164-row committed-baseline comparison ("0 changed + 2 new of
166", 417 → 421 violations, exits {0:32,1:132} → {0:32,1:134}) reproduces exactly in JCAL1
(re-run twice; plus a `git archive` baseline regeneration with 0 mismatches after the
path-convention correction), JCAL5 (third method, `python3 -I`, seeded shuffle, replicate),
H4 (against B1's committed tuple manifest), V2, JDEP4, and H1 (reduction proof from the
checker freeze + the 3 inert map `.md` edits). H1/JCAL5/JCAL3/JCAL1 all note that the "0
changed" is **tuple-level**: three pre-existing fixture directories carry map-markdown edits
(editorial only; the checker cannot read `.md`).

**Discrimination — both fixtures under both checkers (my run; README blocks match).**

```text
r91-c1-null-chain @ delivered: VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None   (exit 1)
r91-c1-null-chain @ e97613c : … possible provenance chain break … got None; from_holder None is not uniquely resolvable (0 raw …)  (exit 1)
r91-c1-tick-unresolved @ delivered: …tick: provenance tick 1 must be greater than previous tick 3   (+ qualified chain-break line, byte-identical across checkers)
r91-c1-tick-unresolved @ e97613c : …tick: input-structural finding…holder identity is not uniquely resolvable…; provenance tick 1 must be greater than previous tick 3
```

Exactly one line pair changes per fixture, on the declared repaired lines; the tick fixture's
qualified chain-break line and its deliberate `entities[1].first_appearance` diagnostic are
byte-identical across revisions. Independent receipts: JCAL2 (paired diffs + **X3-revert flips
only the tick fixture, X2-revert only the null fixture**, restoring the e97613c stdout hash
byte-for-byte), JCAL3 (README blocks byte-exact both ways; fixture construction verified
against parent `item-chain-valid`), JCAL5, V2 (single-gate hybrids) and JDEP4-check
(`DISCRIMINATION HELD` exit 0 delivered; `REGRESSION-DETECTED` exit 2 with the e97613c source
as the checker), H1, JDEP4, JCOV4.

**C9 watch.** `corpus/knowledge/r91-c9-watch.md` (43 lines, landed `6332115`) pins the
`ff9fd2aa…` hash, states the r90-carried integer-only tick ruling, gives the three-command
boundary probe, a four-gate falsification trigger, and owner S1. My probe reproduces the
pinned hash and both expected outputs; JCAL2 verified the trigger is runnable (with the
placeholder-substitution nuance), JCAL3 byte-compared the landed file against S1's patch
(identical; file sha `698a8456…`), V2 traced the "carried from r90 C9" attribution to
`round-90/C9.md:68-70`, JCOV4 confirmed the four gates are operational and the ruling stays
checker-local.

**C2 receipts (my run).**

```text
r87: INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22 … RESULT PASS (exit 0)
r88-m3: INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6; repeated-references=4
        WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim); RESULT PASS WITH WARNINGS (exit 0)
```

Reproduced identically by JCOV1, JCOV2, JCOV3, JCOV4, H1, H4 (census side), JDEP2, JDEP4.
The M2 contract deviations are README-documented (`corpus/tools/README.md`, "Named debt — S2
terminal-status contract": missing inventory → stderr FAIL + exit 2; no terminal
`RESULT FAIL`/`RESULT ERROR`). The r90 tool on the same mutant inputs passed green
(JCOV1: header-rename/dropped-section/duplicate-row all exit 0 on the baseline vs exit 1
delivered; JCOV2 same; JCOV4's 8-mutation matrix; my own run confirms the delivered behavior).

**C3 decision table (my diff + JDEP evidence).** `git diff a7c6a17..c2ab3d0 --
corpus/knowledge/r88-sourced-inspiration-decision-table.md` shows the R8 failed-gate
disposition + withhold precedence (insert at `:40-47`), the R9 appendix rebuilt with
Owner/Trigger/Decision/Worked example/Verification command (`:49-91`), and the R10 namespace
scoping (`:105-108`); the R9-embedded verification command replays 11/11 (mine + JDEP1).
JDEP1: all three clarifications landed; retroactivity byte-held; R9 complete; **R8/R10 carry
no Owner/Trigger/Worked-example labels** (rule content present; the D1 patch holds the drafted
elements unapplied). JDEP2's three constructed attack cases: R8 inseparable-detail case
uncovered (the deciding clause D1 and R1 both drafted — "withhold the whole element … no
independently supportable remainder" — has **0 hits in the delivered text**); R9
privately-held reprint record uncovered/ambiguous ("auditable" undefined; support command
counts it green); R10 deliberate shared-id convention mis-governed (no intent category).
JDEP3: register correctly absent, namespace rule operative, no harm.

**Boundary-doc reconstruction (my forensics; H1/H5 are the reference audits).**

```text
lineage (git show <rev>:corpus/knowledge/holder-assessment-boundary.md | sha256sum):
e97613c = ca7f9ef = a4b1b331… (630 lines)   |   a7c6a17 = 0d42c988… (316) = the r90 CB1 proposal verbatim
c2ab3d0 = c0c59daf… (549 lines, sha c0c59dafc32c7fdc…)
delivered doc: H1 headings=2 (identical titles :1/:8); `verified-at:` lines=2 (:46, :51); banners=2 (:3-6 r91, :9-12 r89)
stamps: 1b09f3f x15, ca7f9ef x7, e2bb9639 x3, ff9fd2aa x2 (H1 count)
hunk diff e97613c..c2ab3d0: 91 insertions / 172 deletions, 9 hunks
applied section texts: D3, D4-verified-at, D5, D11/D12-census, D1/D2-row-3, D2-limits, D11, D10, D8/D12 (9 present)
NOT applied: D4-header/banner, D6/D7 cause anchors (heading still `delivered 1b09f3f`; 36 stale sites per H5), D9-second range, D13 relabels, D2's new bullet; only D1 named as skipped debt
```

H1 named the same condition `R91-H1-BOUNDARY-RECONSTRUCTION-SPLICED` /
`…-SECTIONS-LOST` / `…-STALE-REVISION-LABELS` / `…-UNRECEIPTED` / `…-SKIPPED-DEBT-COUNT`;
H5 quantified it (54 delivered-context anchors: 18 resolve / 36 stale; 3 `##` headings
dropped with dangling `"The contract"`/`"Commands"` references; seam fragments at
`:33-40`, `:46-61`, `:380-385`, `:405-406`; replay claims verified 14/14 byte-identical);
K1 and JDEP3 independently flagged the skipped-debt count discrepancy. H5's verdict:
the integrator's "10 sections applied, 2 items named as skipped debt" is **not supported**
(9 present, ≥4 unapplied, 1 named). H1/H5 both: **do not certify the boundary document
delivered-true.**

*My additional finding (not named by any seat I read):* the applied D11 paragraph still says
(delivered `:394-397`) "Still scratch-only, with no durable fixture in the tree: … and the
null-chain definite form. The tick-under-unresolved-holder FN-2 sub-branch no longer exists
— …; its would-be fixture was never built and is not owed." At the delivered tree the
r91-c1-null-chain fixture **is** the durable fixture of the null-chain definite form and
r91-c1-tick-unresolved **is** the tick-under-unresolved fixture — the doc contradicts the
corpus shipped in the same commit.

## Findings & named debt

### Per-axis verdict table (recommendation to the L1)

| axis | verdict at `c2ab3d0` | verdict after the R1–R3 repairs | one-line evidence pointer |
|---|---|---|---|
| **calibration** | **improved (bounded)** | **improved (bounded)** | Checker freeze `ff9fd2aa` at HEAD/worktree/`a7c6a17` (my run + JCAL1/2/3/5, H1, H4, V2, JDEP4); census 0 changed + 2 new of 166, 0 exit/stderr changes (my run + JCAL1/5, H4, V2, JDEP4, H1); discrimination exact on the repaired lines and **per-gate**: each single-gate revert flips only its own fixture (my run + JCAL2 X2/X3, V2 hybrids, JDEP4-check); C9 watch pin/probe/trigger reproduce (JCAL2/3/5, V2, JCOV4, H1). Bounds: CAL-D1…D6 below. |
| **coverage** | **improved (bounded)** | **improved (bounded)** | Receipts reproduce: r87 14+8, r88-m3 10 + expected WARN, exit 0 (my run + JCOV1-4, H1, JDEP2); all r90 silent vectors now fail/warn (JCOV1 5 attacks; JCOV2 A/B/C/E/G; JCOV4 8 mutations) while the baseline tool passed the same mutants green (JCOV1/JCOV2); the two S2 deviations are README-named and behavior-matching (my grep + JCOV1/2/3/4, H1). Bounds: COV-D1…D5 below. |
| **depth** | **harmed (bounded)** [gains real, not netted] | **improved (bounded)** | Gains verified: R8/R9/R10 text landed (my diff + JDEP1/2/3); register absent; namespace rule operative as delivered (JDEP3 worked case); retroactivity byte-held (JDEP1/JDEP2). Harm: the boundary-doc reconstruction is **uncertifiable as delivered** — seams (2 H1, 2 `verified-at`, contradictory banners), 3 lost headings with dangling refs, 36/54 stale delivered-context anchors, 15 stale `1b09f3f` labels incl. a superseded checker pinned as "delivered" (`:429-430`), 1-of-2 skipped items named, no wave receipt (H1, H5, K1, JDEP3; my forensics), plus a doc-vs-r91-fixtures contradiction (my finding) and the C3 integration drops (R8 deciding clause: JDEP2; R8/R10 labels: JDEP1). A trade anywhere is NOT an improvement, so depth cannot be recorded improved while these stand. |

No other axis harmed: H1's path enumeration and protected-file freeze hold; H4/V2 find no
probe or lineage regression; JCOV4's province/three-question sweep is clean; SE2 finds no
stray tracked writes, no seat commits, no push; K1 finds no L0 need; the checker is untouched
so the C1 census cannot reopen.

### Attribution note (for the L1's wording)

H1 and H5 charge the boundary-doc damage as content-integrity of a tracked contract (doc-parity
class) without assigning an axis; H5 explicitly finds "no calibration claim breaks". r88/r89/r90
precedent assigned the identical condition (a knowledge/contract doc contradicting the shipped
tree) to **depth**; under a V2-style attribution (V2 did not assess depth this round) it would
sit on calibration instead. Under either attribution the instruction is identical: repair (or
explicitly record harmed) before writing "improved" anywhere the condition is charged, and do
not net the C1/C2/C3 gains against it.

### Claim-verification notes (C1 / C2 / C3 vs the delivered tree)

1. **C1 verifies (bounded).** Census, discrimination, watch-pin and trigger all reproduce
   exactly; the "0 changed" statement is tuple-level and must keep the checker-level wording
   (3 inert map `.md` edits ride inside pre-existing dirs — JCAL1/JCAL3/JCAL5, H1, SE2 F3).
   The null chain's B3 scratch-probe byte-identity holds; the tick probe's B3 receipt is
   shape-exact but not byte-exact (`previous tick 2` vs the fixture's `3`) — CAL-D1.
2. **C2 verifies (bounded).** The receipts and the three silent vectors reproduce; the
   inventory assertion is load-bearing (my run + JCOV1/2/4) but **self-attested** (a
   coordinated row+declaration edit can still agree — JCOV2-F1/JCOV4-1, the already-named
   M2 bound); the "14/14" counts mapped rows against the declaration, not the raw JSON census
   (20/22 row-represented for r87 — JCOV2-F2/JCOV4; wording bound). The Spence WARN is
   declaration-conditioned and warn-only (JCOV2-F3 controls D/F); the R9-enforcement path
   under the hardened contract still counts a privately-held translation green (JDEP2 — an
   editorial-gate limit, not a checker defect).
3. **C3 verifies in substance, with integration drops.** R9 landed complete; R8/R10 landed
   without the spec's per-decision Owner/Trigger/Worked-example (JDEP1) and R8's drafted
   inseparable/constitutive branch was dropped at integration (JDEP2 D-JDEP2r91-1); R10
   mis-governs deliberate shared-id conventions (D-JDEP2r91-3). The wave-spec C3 sentence
   ("each as a decided clarification with owner, trigger, and worked example") is therefore
   **not fully met** for R8/R10; the r91 record should say "decided, with per-decision
   traceability owed for R8/R10".
4. **Boundary-doc reconstruction.** It is real and repairs the r90-closure proposal-copy
   regression (lineage above; H1 M8), but as delivered it is spliced/partially applied and
   uncertifiable; H5's audit refutes the "10 applied / 2 named" summary (9 present, ≥4
   unapplied items, 1 named). The repair is fully specified (the r90 remap table is preserved
   at `.ufo/waves/round-90/followup/CB1-boundary-refresh.md`; H1 §M8(e) and H5 give the
   applied/skipped inventory).
5. **Capabilities.** JDEP4 (with JDEP4-check.md's runnable mechanical companion) recommends
   **FOR** a third row — `checker-regression discrimination` — with the F2 bounds attached
   (scope, raw-output receipts, wave-resident wrapper, path-convention, prospective trigger).
   This reverses r90's "against" for the reason r90 wrote it: the capability now runs, with a
   mechanical verdict (exit 0 `DISCRIMINATION HELD` vs exit 2 `REGRESSION-DETECTED`).

### Named debt (consolidated; receipts in the named seats)

**Calibration-side:**
- **CAL-D1 B3 tick receipt not byte-exact** — shape-exact only (`previous tick 2` vs `3`);
  the fixture-exact pair lives in the READMEs (JCAL3-1, V2-2, JCOV4 watch note).
- **CAL-D2 Watch wording** — the "pinned in B3 + READMEs" sentence; the surviving
  ambiguous-source prefix on tick lines (V2-3); `e97613c`'s hash not pinned in the watch
  though the trigger asks the recorder for two hashes (JCOV4-3).
- **CAL-D3 Tick README parent/composition note** (V2-4); the r91 fixtures' shared
  scaffolding ids and per-dataset id uniqueness context (JCAL3-3).
- **CAL-D4 Census path-convention sensitivity** — 5 missing-file fixtures embed the invocation
  path in stdout; future censuses must use repo-relative arguments (JCAL1-4, JDEP4 M6).
- **CAL-D5 `corpus/fixtures/README.md` has no Round-91 section/index row** — closure-scope by
  precedent (V2-5, H5-F7, JCAL1-5).
- **CAL-D6 C9 successor not named at closure** (JCAL3-2).

**Coverage-side:**
- **COV-D1 Inventory is self-attested; mapped-scope vs raw-census wording** (JCOV2-F1/F2,
  JCOV4-1; the raw-denominator ask stands).
- **COV-D2 S2 terminal-status deviations** — README-named, not fixed: missing inventory
  exits 2; no `RESULT FAIL`/`RESULT ERROR` summaries (JCOV1, JCOV2-F5, JCOV3-4, H1).
- **COV-D3 Spence comparison rows** — r92 (JCOV2-F4; the WARN is declaration-conditioned).
- **COV-D4 Old receipt probes need re-pointing** under the hardened contract (the r90 R9
  probe now exits 2; JDEP1-1/5, JDEP2).
- **COV-D5 Retelling anchor tolerance + r88 WARN not labeled "expected"** (JCOV4-2, JCOV2).

**Depth-side:**
- **DEP-H1 (blocking-class repair) Boundary-doc re-derivation** — apply-or-name D4-header,
  D6/D7 (36 sites; the r90 remap table), D9-second range, D13, D2's new bullet; delete the
  seam fragments; restore or retire `## The contract` / `## Commands` / `## Status split` and
  fix the dangling references; land the D11 update for the two r91 fixtures; add a wave
  receipt naming applied/skipped items; re-verify heading/`verified-at`/label counts
  (H1 §M8(e), H5 F1-F7, K1, JDEP3, my forensics). No checker change → census cannot reopen.
- **DEP-D1 Skipped-debt count reconciliation** — the delivered header names D1 only; name the
  second item or apply it (H1, H5-A4, K1, JDEP3, my forensics).
- **DEP-D2 R8/R10 traceability transplant** — Owner/Trigger/Worked example (and routing) from
  `D1-edges.patch`; R8's inseparable/constitutive branch; R9's "auditable"/private-custody
  definition; R10's intentional-convention channel (JDEP1-2, JDEP2 D-JDEP2r91-1…-3).
- **DEP-D3 R9 verification command targets the wave patch, not the delivered doc** —
  a text-completeness receipt that cannot detect doc drift (JDEP2 D-JDEP2r91-4).
- **DEP-D4 Namespace naming convention / manual gate** (JDEP3).
- **DEP-D5 Capabilities row** — JDEP4 FOR with F2 bounds; L1 decides (r90's "do not enter a
  third row" is superseded by the runnable demonstration).

**Closure/process:**
- **PROC-1 Closure prose from delivered figures** — census wording (checker-level), no
  "10 applied/2 named" for the doc (H5), roster arithmetic 32/30/33 unreconciled (H1 M9/SE1).
- **PROC-2 P1 round-91 fleet report not yet written** — `.ufo/reports/round-91/lore.md`
  absent, single-location convention intact (SE2 F2) — closure duty.
- **PROC-3 `/tmp` inode exhaustion persisted wave-wide** (every J seat; several shifted to
  `/dev/shm`); r90 pycache debt resolved at r91 (`.gitignore` now carries `__pycache__/`;
  SE2 item 6); carried r85 sealed-receipt debt unchanged (H4).

### Admission recommendation to the L1

**Do not admit as-is; repair, then admit (recommended).** Calibration and coverage verify with
named, non-blocking bounds. Depth carries a bounded, independently corroborated (H1, H5, K1,
JDEP3 + my re-run) boundary-doc harm plus two C3 integration drops; under the round's rule it
cannot be recorded improved as delivered.

1. **R1 (blocking-class, documentation-only):** re-derive `corpus/knowledge/holder-assessment-boundary.md`
   from `e97613c` by applying CB1's r90 D-items **by anchor, replace-not-insert-before** —
   apply or explicitly name D4-header, D6/D7, D9-second range, D13, D2's new bullet; delete
   the seam fragments (duplicate H1/`verified-at`/banners/dangling clauses); restore or retire
   the three dropped headings and fix the `"The contract"`/`"Commands"` references; update the
   D11 clause for the two r91 fixtures; add a reconstruction receipt to the wave evidence
   naming applied and skipped items; re-verify the heading/`verified-at`/revision-label counts
   with an independent seat (H1's procedure). No checker change → the C1 census cannot reopen.
2. **R2 (closure-scope by precedent):** add `## Round 91` to `corpus/fixtures/README.md`;
   transplant R8/R10 Owner/Trigger/Worked-example (from `D1-edges.patch`) and R8's drafted
   inseparable branch; re-point the R9 receipt-parity probe to the hardened contract.
3. **R3 (cheap, non-blocking):** B3 tick-receipt byte-exact pair or watch rewording; watch
   `e97613c` hash + ambiguous-source sentence; tick README parent note; name the C9 successor;
   path-convention note in the census records.

Then record: **calibration improved (bounded), coverage improved (bounded), depth improved
(bounded)**, with CAL-D1…D6, COV-D1…D5, DEP-D1…D5, PROC-1…3 carried as named debt; and decide
the capabilities row per JDEP4 (FOR, with F2 bounds). If the doc repair cannot be completed
and independently re-verified in the closure window — this file has now been botched twice
(r90 closure, r91 integration) — prefer explicit deferral over another rushed landing.

**Alternative — admit with recorded harm:** if the L1 prefers not to reopen the round, record
depth **harmed (bounded)** explicitly (boundary doc uncertifiable: seams, 36 stale anchors,
stale "delivered" checker pin, doc-vs-r91-fixtures contradiction; R8/R10 traceability dropped)
with R1/R2 as the first closure/r92 items; do not write depth improved while DEP-H1 stands;
do not net the C1/C2/C3 gains against the harm. Under a V2-style attribution the recorded-harm
sentence moves to calibration.

Either way: the C1 record keeps the checker-level census wording; the C2 headline keeps the
row denominators (14 JSON facts + 8 editorial rows; 10); the C3 record must not claim
spec-complete owner/trigger/worked-example for R8/R10 until R2 lands.

## Handoff

- Deliverables: `.ufo/waves/round-91/followup/JAXIS.md` (this file) and
  `.ufo/waves/round-91/followup/JAXIS-verdicts.json` (machine-readable verdict table,
  admission options, consolidated debt ids, seat inventory). No other repo write; no commit;
  no push. Scratch `/tmp/jaxis-r91/` (2 files: the e97613c checker copy and the boundary-doc
  diff) was **swept** at close.
- Reproduce my central measurements (cwd `lore-shokunin/`): (1) `sha256sum
  corpus/fixtures/check_bible.py` → `ff9fd2aa…`; (2) delivered-vs-`e97613c` checker over all
  166 dirs → stdout differs only on the two r91 fixtures, 0 exit/stderr changes, 421
  violations; (3) the two fixtures under both checkers → exactly the repaired lines flip;
  (4) `support_check.py` on r87/r88-m3 → 14+8 / 10+WARN, exit 0; (5) `git diff
  e97613c..c2ab3d0 -- corpus/knowledge/holder-assessment-boundary.md` → the partial
  application (9 section texts present, D4/D6/D7/D9/D13/D2-bullet absent) — the R1 worklist.
- Claim status for the integrator: **C1 verifies (bounded); C2 verifies (bounded); C3
  verifies in substance with R8/R10 traceability owed; the boundary-doc reconstruction is
  uncertifiable as delivered (repair artifact fully specified); capabilities row FOR per
  JDEP4.**
- Not done here: `JCAL4.md` not observed (no JCAL4 receipt either — fold in if it lands);
  I field-audited the J receipts' key numbers rather than every JSON row; I did not
  re-run H5's 54-anchor audit line-by-line (spot-checked against my own greps and H1's);
  I did not adjudicate the R8/R9/R10 edge substance beyond reporting JDEP1/JDEP2/JDEP3;
  no external sources re-fetched. All remediation is the L1's decision.