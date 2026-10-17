# PROPOSAL ONLY — Round 91 LOG entry (P3, follow-up wave)

Draft by seat P3 of the round-91 follow-up wave; supersedes W2's pre-delivery draft
(`.ufo/waves/round-91/patches/W2-log-r91.proposal.md`) where they differ. Do not append to
`LOG.md` before L1 adjudication. Every measurement below was re-run on the delivered tree
`c2ab3d0` (tracked tree clean; the only porcelain line is the untracked `followup/`
directory); corroborating sibling follow-up receipts are cited by path; scratch probes are
labelled. All verdicts are proposed, **PENDING-L1**; no admission is claimed here.

## Round 91 — 2026-10-17 (discriminating C1 fixtures + C9 watch, hardened support command, R8/R9/R10 edge decisions, boundary-doc reconstruction; luna-max work wave; work commits `6332115` + `c2ab3d0`)

- Baseline before this round is `a7c6a1773d5994246a76e4eff30d645f161920e0` (`a7c6a17`,
  r90 closure; tree clean). The round ran as a world-bible work wave recorded under
  `.ufo/waves/round-91/` — 33 seat reports (the spec declares 32 seats and names 30;
  unrostered `CB1` delivered the boundary-doc audit; `CB-prep` never reported) plus
  `wave-spec.md` with W1's landing record and `wave-spec.json`, and 22 `patches/` artifacts —
  landed as `6332115` (76 files, +11136/−227) and amendment `c2ab3d0` (2 files, +18; the r89
  paraphrase demo's missed Inventory line and the R8/R10 r91 decisions), followed by a
  follow-up wave under `.ufo/waves/round-91/followup/` (H3/H4/JCAL5/K1/P3, this record). No
  push and no merge this round.

- **Motivating evidence — C1 (calibration).** r90 closed with the C9 integer-only tick ruling
  pinned by probes only and Q90-001 open: no durable fixture carried the superseding shape,
  and the r90-repaired shapes (null-chain definite, integer tick definite under an unresolved
  compared holder) had no regression-visible pins; the r91 spec (C1) required two durable
  DISCRIMINATING fixtures and a falsification path for the C9 ruling.

- **C1 landed — `6332115`.** Two durable fixtures with per-checker expected outputs.
  `corpus/fixtures/r91-c1-null-chain` (exit 1, one violation, sha256 `615dc056…`): under
  `e97613c` the finding is hedged — `input-structural finding … possible provenance chain
  break … from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but
  only 0 is in the resolved index)` — while the delivered checker prints the definite
  `provenance chain break; expected from_holder 'mira', got None`;
  `corpus/fixtures/r91-c1-tick-unresolved` (exit 1, three violations incl. its deliberate
  `first_appearance` row, sha256 `d754e96f…`): under `e97613c` the tick line carries the
  identity hedge (`… holder identity is not uniquely resolvable …; provenance tick 1 must be
  greater than previous tick 3`), while the delivered checker prints the definite
  `provenance tick 1 must be greater than previous tick 3` and the separate chain-break line
  stays qualified, byte-for-byte. Census replay on the delivered tree: 166 fixture dirs,
  exits `{0: 32, 1: 134}`, 421 violation lines, empty stderr; **0 changed tuples of the 164
  baseline, 2 new, 0 exit changes** (B2 agrees 164/164; H4-census.json reproduces the same
  counts against B1's manifest sha `5433f6af…`; H3-r91-scan.json shows the two new dirs are
  the only stdout-differing dirs of 166 between `e97613c` and delivered, with 0 exit diffs).
  `corpus/knowledge/r91-c9-watch.md` pins the shipped hash
  (`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, delivered checker at
  `a7c6a17`; equal at `c2ab3d0` and in the worktree), restates the ruling, and names its
  owner and the exact four-gate falsification trigger with the probe to run. **The r91
  checker is unchanged** — no checker-touching commit in `a7c6a17..c2ab3d0`; the round's
  calibration contribution is durable discriminating regression coverage and the watch, not
  a checker change. Bound: the C9 reopen path remains prospective (spec's r91 falsification
  path), and no durable fixture carries a genuinely unresolved *compared* holder tick beyond
  the pinned shape itself.

- **C2 landed — `6332115` (coverage).** The support command is hardened against the r90
  follow-up's silent-failure vectors: an exactly-one inventory declaration is asserted
  (`**Expected inventory:** N JSON facts; N editorial rows; N total mapped rows; N distinct
  excerpt anchors.`) against parsed category counts, total rows, and distinct
  `(excerpt path, anchor)` pairs; fact tables must sit under `## JSON facts` or
  `## Editorial rows`; duplicate mapped rows fail while repeated anchors are reported; and
  receipts split `JSON-FACTS` / `EDITORIAL-ROWS` / `TOTAL-ROWS` with `EDITORIAL-ANCHORS`
  separate from `SOURCE-SUPPORT`. Measured on the delivered script: r87 `INVENTORY
  JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22 … SOURCE-SUPPORT
  14/14; EDITORIAL-ANCHORS 8/8; … MODES 22/22; VALIDATED-ROWS 22/22 — RESULT PASS` (exit 0);
  r88-m3 `… 10/10 … 6/6; ANCHORS repeated-references=4; DUPLICATE-ROWS 0 … SOURCE-SUPPORT
  10/10 … WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim) — RESULT
  PASS WITH WARNINGS` (exit 0, the expected warning: the two Spence comparisons are bullets,
  not rows — queued r92); paraphrase demo `1/1 … RETELLING-SUPPORT-ONLY 1 entries (1/1) —
  RESULT PASS` (exit 0, its inventory line restored by `c2ab3d0`). Scratch negative controls
  (P3, copy of the demo under `/tmp`, swept): missing inventory → exit 2, `FAIL: map must
  contain exactly one expected inventory declaration`; renamed `## JSON facts` heading →
  exit 2, `FAIL: fact table must be under a JSON facts or Editorial rows heading`; duplicated
  mapped row → exit 1, `INVENTORY JSON-FACTS 2/1; … DUPLICATE-ROWS 1` +
  `FAIL: duplicate mapped row … appears 2 times`. M2's two contract deviations (missing
  inventory returns 2; no `RESULT FAIL` terminal summaries) are named debt in
  `corpus/tools/README.md`, explicitly "not accepted equivalents". Bounds: those exit-status
  deviations, the lexical-preflight limit (README states the check is not fidelity
  evidence), and the r88-m3 unreferenced-declaration WARN/Spence-bullet case.

- **C3 landed — `6332115` + `c2ab3d0` (depth).**
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` gains three decided r91 edges
  (63 changed lines at `6332115`, 14 more at `c2ab3d0`): **R8 failed-gate disposition** — a
  failed two-part R2 gate leaves the element NOT proven influenced, keeps the uncertainty
  note, withholds the affected detail, and withholds detail-level over element-level when
  they conflict; **R9 reprint boundary** — a later reprint can qualify for the narrow R9
  exception only with an auditable, item-specific record of the delivered reprint, its
  translator and source work, and the checked passage, with owner, trigger, worked example,
  and a verification command, and support extends only to the identified reprint's wording;
  **R10 namespace scoping** — `source_id` is cluster-local, so a shared id across clusters is
  a namespace collision, not identity, compared as `(cluster-relative path, source_id)` and
  never entering the register by itself. The live register is correctly absent
  (`corpus/knowledge/cross-cluster-contradictions.md` does not exist); W2's caveat stands:
  absence alone is not proof the register is correctly empty.

- **Integration defect found and repaired inside the round (boundary doc).** CB1 (r91) found
  that the r90 closure had committed CB1's r90 section-replacement *instruction sheet* as the
  tracked boundary document: at `a7c6a17` the path is byte-identical to
  `.ufo/waves/round-90/followup/CB1-boundary-refresh.md` (`0d42c988…`, 316 lines, first line
  `# CB1 — Boundary-doc refresh proposal (for the round-90 closure)`, `Status: proposal
  only`), while the r90-delivered contract never existed beyond `e97613c`'s r89 refresh
  (`a4b1b331…`, 630 lines; `ca7f9ef` is byte-identical — the r90 work wave never applied it).
  Q1's work-wave ledger flagged the contradiction with the r90 SCORECARD repair assertion for
  L1 review. The work commit reconstructed the contract from the r89-landed base: delivered
  `corpus/knowledge/holder-assessment-boundary.md` is `c0c59daf…`, 549 lines, with a
  reconstruction banner (`:3-6`) naming the base (`e97613c`), CB1's r90 instruction set
  (D1–D13), and one skipped item as named debt: `D1 — Decision-table row 2 code refs.`
  Measured residue (recorded, not netted): the H1 title appears twice (`:1`, `:8`); the stale
  r89 banner `Refreshed at round-89 closure … at 1b09f3f (checker e2bb9639)` remains `:9-11`
  (no round-90 banner was written); two mid-sentence splice fragments survive — the r90
  revision clause inserted before a leftover `delivered checker at 1b09f3f` fragment (`:37-41`)
  and the r90 `verified-at` block inserted mid-sentence after `… the multi-cause joining rule,
  the qualified` (`:46-56`); stale r89 labels remain at the cause-section heading `:139`,
  `:412` (`does not exist at 1b09f3f`), and the tail `:543` (`No five-gate score is recorded
  for the delivered tree 1b09f3f`; tail byte-identical to `e97613c`, i.e. the D14 label
  replacement is visibly unapplied); the instruction sheet's `## Consolidated anchor remap`
  section did not land (`grep -c` = 0). **Accounting reconciled by CB1's follow-up audit
  (`.ufo/waves/round-91/followup/CB1.md` + `CB1-docstate.json`):** of the sheet's 13 fenced
  doc-edit blocks, 9 landed verbatim and 5 prescribed items are unapplied (D4 header/banner,
  D6/D7 anchor remap, D1 row 2, D9 labels, D13 labels) plus the absent D2 bullet, while the
  doc header names only D1 as skipped debt; 3 headings and 12–13 `Precise limits` bullets are
  lost from `ca7f9ef` (content regression, `R91-CB1-LIMITS-LOSS`), the decision table carries
  a duplicate contradictory state row (`:179` retired vs `:184` current), 35 delivered-state
  citations are stale (14 of 26 needle tests fail), and 4 splice/duplicate sites remain. Sound:
  all 9 landed blocks are verbatim, 7/7 fenced blocks are byte-identical to `ca7f9ef`, and the
  r85 five-case replay still matches the delivered checker. CB1's verdicts: doc-state fidelity
  vs the declared target **harmed** (improved vs `a7c6a17`), reconstruction accounting
  **harmed**, internal coherence **harmed**, checker freeze **unchanged**; E1's follow-up
  likewise grades prose consistency **harmed (bounded)** while replayable wording fidelity and
  boundary-doc coverage are **improved (bounded)**. H5 confirms the integration accounting claim
  is not supported ("10 applied / 2 named" → 9 section texts present, ≥4 unapplied items, only 1
  named), and finds the D9 second range and D6/D7 unapplied and unnamed; JAXIS adds that the D11
  paragraph (`:394-397`) still asserts the null-chain definite form has no fixture "and is not
  owed" — contradicted by the two fixtures shipped in the same commit. CB1's recommendation is
  to re-derive the doc from `git show ca7f9ef:…` and apply the sheet by anchor (replace, not
  insert-before) — not to patch the delivered file in place.

- **Follow-up verification (this wave).** H4: checker lineage `ff9fd2aa…` across
  r90-work/r90-closure/r91 (9 generations replayed over the 5 r85 probes; all five probe
  outputs byte-identical `c2ab3d0` vs `a7c6a17`; two control probes still receipt-exact;
  determinism control stable under `PYTHONHASHSEED`); census exact vs B1's manifest; the two
  new dirs discriminate verbatim as declared; the `c2ab3d0` amendment moved no
  checker-observed output. H3: whole-corpus scan — only the two new dirs differ. JCAL5:
  independent calibration delta with the C9-watch pin cross-checked. K1: L0 stable (5
  entries, unchanged baseline→delivered, no append; kotodama/chousa standing checks
  unchanged; no r91 artifact requests an operator decision). Carried debt (H4): the three
  ambiguous r85 probes have not matched their sealed `.txt` receipts since r86 — unchanged at
  r91; B1/B2 tuple manifests are semantically identical but not byte-equal (compare tuples,
  not file bytes).

- **Documentation-parity / index debt (measured, unrepaired).** `corpus/fixtures/README.md`
  has no Round 91 section (last is Round 90): the two new fixtures, `corpus/knowledge/r91-c9-watch.md`,
  and the hardened support command's receipt-split wording are unindexed;
  `r91-c9-watch.md` is referenced by no `corpus/` text. The reconstructed doc's `:494`
  statement ("There is no `## Round 90` section at `ca7f9ef`") is as-of-r90 and now
  ambiguous. These are the same class of index debt r90's follow-up found and repaired at
  closure.

- **Process and inode pressure.** Two 60 s wait-checks per follow-up seat (K1 08:32:33 /
  08:33:33; H4 08:33:15 / 08:34:15; P3 08:33:34 / 08:34:34 −03:00; `followup/` went 0 → 1 →
  5+ artifacts as H3/H4/JCAL5/K1 landed). `/tmp` was at 100% inode use through the window
  (K1 1,875 free; H4 1,880→1,724; P3 1,713–1,816 free of 1,048,576); P3 swept its scratch
  (`/tmp/p3r91/neg` removed; 3 small files left then swept); `__pycache__/` is now named in
  `.gitignore` (r90-closure repair; Q89-044 closed). W1's landing record (cutoff
  2026-10-17T07:36:41−03:00; 15 of 30 named seats with any artifact) shipped in the work
  commit as the spec's Landing record plus `wave-spec.json`; Q2's later inventory reached
  29/30 named reports with only `CB-prep` absent. The round-91 fleet report
  (`.ufo/reports/round-91/lore.md`) was written by P3 under explicit parent authorization
  (the P1 seat delivered no artifact — SE2 F2); the umbrella MANIFEST `rounds[]` entry and its
  commit remain owed.

- **Per-axis verdicts (judge recommendations on record; L1 owns — the round is NOT admitted
  here).** JAXIS's follow-up synthesis (recommendation only; the J-reports read in full):
  calibration **improved (bounded)**, coverage **improved (bounded)**, depth **harmed
  (bounded) at the delivered tree** — improved (bounded) only after its repair set R1–R3 —
  with admission options **A. repair, then admit (recommended)** or **B. admit with recorded
  harm**. P2's SCORECARD draft proposed improved for all three and differs on depth; the CAL
  judges (JCAL1/2/3/5, V2) propose calibration improved with bounds. Evidence behind the
  recommendations: two durable discriminating fixtures verified against both checker revisions
  with single-gate revert controls (JCAL2/V2/JDEP4: `DISCRIMINATION HELD` /
  `REGRESSION-DETECTED`), census 0 changed + 2 new + 0 exit changes over 164; one hardened
  command whose declared-inventory, section, duplicate-row, and receipt-split behaviors
  reproduce from the delivered tree with positive and negative controls (JCOV1 reproduces the
  M2+M6 composition byte-identically and all five attack cases); R8/R9/R10 decided with the
  register correctly absent — versus the boundary-doc assembly harm above. Consolidated
  bounds/debts (recorded, not netted): CAL-D1…D6, COV-D1…D5, DEP-H1/D1/D2/D2b/D3/D4/D5,
  PROC-1…3. Every claim above verifies from the delivered tree; the harm, residue, and index
  debt remain open for L1's disposition.

- **Province.** Every changed path is under `corpus/` or `.ufo/`; `PROVINCE.md`, `SHONEN.md`,
  `LOG.md`, and `SCORECARD.md` bytes are unchanged at `c2ab3d0` (empty diff from `a7c6a17`);
  the two `chousa` cross-references in the decision table predate the round (present at
  `a7c6a17`, absent from the r91 diff); K1's L0 scan found no new operator-level need.

- **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this round (no
  `[x]`); the capabilities table is unchanged; no saturation or retirement is declared.

- **Round record.** `LOG.md` and `SCORECARD.md` are unchanged at `c2ab3d0`; this entry is the
  round's LOG record proposal (supersedes W2's pre-delivery draft) and the SCORECARD proposal
  remains `.ufo/waves/round-91/patches/W2-scorecard-r91.proposal.md` (L1 may adopt or
  adjust). L1 verdicts and any admission are not claimed here.