# Round 88 fleet report skeleton (W2)

## Work performed

- Finalize this report only against the delivered/integrated tree; cite its full revision and the scratch copy used for each replay. Do not treat a proposal patch or baseline report as an after-state result.
- Evidence present at W2's second 60-second checkpoint: `B1.md`, `B2.md`, `B3.md`, `K1.md`, `M4.md`, `SE1.md`, and `X4.md`, plus their seat-prefixed patch/evidence files. No primary C1 implementation report, second-cluster draft, C3 decision table, cross-verification, or ledger-registration report was present at that checkpoint.
- Preserve the required section order and give independent, evidence-backed verdicts for C1 calibration, C2 coverage, and C3 depth.

## Before → after measurements

- **C1 CALIBRATION — [verdict].** The independent pinned-baseline censuses in B1/B2 agree on 145 fixture tuples: 30 exit 0, 115 exit 1, 331 violations, empty stderr for all; the tuple files are byte-identical (SHA-256 `76cf55c0cdce35c538bb869033e1c9642c92901f650304ce547328aec2efb106`). B3's before-state receipts report the shape-ambiguous case with 2 findings and no `unassessed` disclosure; the mixed-stop's first cause is unknown source at record `[0]` but later ambiguity is over-attributed; unknown-source-only has no disclosure. Record the delivered revision, exact scratch replay/census commands and outputs, all changed tuples, and confirmation that unchanged tuples are preserved. Verify that a shape-invalid dict carrying an ambiguous holder id arms the stop; every record at/after any provenance-chain stop carries a disclosure naming the actual first cause, including unknown-source and dangling-holder stops; wording makes no causal overclaim. X4's one-tuple prototype is not a C1-complete after-state.
- **C2 COVERAGE — [verdict].** Record the baseline→delivered inspiration-note count (required `1 → 2`), both cluster paths/families, and verify the new family is distinct from r87's Sumerian/ETCSL cluster. Include exact checker commands and exits for both clusters, and the delivered census count. Verify passage-level locators, the clause→element symbolism index, zero unsupported attributions mechanically resolvable against delivered excerpts, and the Mother-Tide Gate OBS-1 repair. M4's `repoint` and `excerpt` patches are alternatives, not cumulative; report only the selected delivered repair and its direct text checks (the checker alone does not validate prose-to-excerpt support).
- **C3 DEPTH — [verdict].** Link the delivered sourced-inspiration decision table and report its row count. Verify attribution, rights, and training-permission as three distinct fields; excerpt-delivery requirements; every row against the delivered clusters; and the r87 ETCSL registration in `corpus/knowledge/reference-ledger.md` using the format in `corpus/knowledge/seed.md:26-29`. Include exact commands and observed outputs; do not infer rights or training permission.
- **Integrated measurements — [revision].** Add the exact delivered-tree/scratch commands and observed outputs for each claim. Separate baseline receipts, candidate-patch results, and final integrated results; identify unavailable measurements rather than estimating them.

## Findings & named debt

- **C1:** [axis verdict, measured tuple delta, first-cause/tail-disclosure evidence, remaining debt]. Distinguish X4's rejected-record notice proposal from proof of the required structural stop and disclosures.
- **C2:** [axis verdict, both sourced clusters and passage/symbol evidence, OBS-1 repair evidence, remaining debt].
- **C3:** [axis verdict, table and row-verification evidence, ledger row evidence, remaining debt]. Keep K1's ownership boundary: lore retains the world-bible record and reference ledger; source research can support verification without turning a reference into canon or asserting a rights ruling.
- **Round-level debt:** [unresolved evidence, conflicts, or follow-up]. Do not claim closure from phase-1 proposals or baseline-only reports; state if the delivered tree or independent adjudication was unavailable.

## Handoff

- Delivered revision and verification scratch location: [full SHA and path].
- Integrated implementation / corpus artifacts: [paths and landed status].
- Evidence reports and exact replay receipts: [paths].
- Remaining TODOs or named debt carried forward: [items].
- Overall round assessment, if authorized by the integrator: [evidence-based statement; do not invent a SHONEN rating].
