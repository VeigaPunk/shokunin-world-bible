# PROPOSAL ONLY — Round 90 LOG entry (P3, follow-up wave)

Draft by seat P3 of the round-90 follow-up wave; supersedes W2's pre-delivery draft
(`.ufo/waves/round-90/patches/W2-log-r90.proposal.md`) where they differ. Do not append to
`LOG.md` before L1 adjudication. Every measurement below was re-run on the delivered tree
`ca7f9ef` (clean while measured, through 06:59:15 −03:00; a sibling follow-up seat has since
revised the tracked `followup/Q1-r90-debt.json` in place — its own receipt also shows the
freeze MATCH `ff9fd2aa…`); probe/control scratch is labelled. All verdicts are proposed,
**PENDING-L1**; no admission is claimed here.

## Round 90 — 2026-10-17 (r89 hedged-shape repair + claim→excerpt maps + span-enforced support command + R8/R9/R10 sub-cases decided; luna-max work wave; work commit `ca7f9ef`)

- Baseline before this round is `e97613cc276f5fa9cac49ff1900798cf6863c020`
  (`e97613c`, r89 closure; tree clean). The round ran as a world-bible work wave
  recorded under `.ufo/waves/round-90/` — 33 seat reports (the spec declares 32
  seats but lists 29 roster rows; the four-seat supplementary batch M5/C9/W3/SE3
  joins the manifest, recorded in the spec's Closure amendments) — landed as
  `ca7f9ef` (95 files, +12619/−11), followed by a follow-up wave under
  `.ufo/waves/round-90/followup/` (Q1's debt audit, H2/H4/JCAL1/JCAL2/JCAL5
  verification, this record). No push and no merge this round.

- **Motivating evidence — C1 (calibration).** r89 closed with two hedged wording
  shapes recorded as a bounded definiteness regression and queued as r90's first
  calibration fix. Measured at `e97613c` (`patches/B3-before-state.json`): a null
  `from_holder` in a later record printed the vacuous clause
  `…expected from_holder 'mira'; got None; from_holder None is not uniquely
  resolvable (0 raw entity rows carry this id, but only 0 is in the resolved
  index)`; a tick inversion under an unrelated raw-duplicate holder printed
  `…holder identity is not uniquely resolvable: expected from_holder
  'uncertain-holder' …; provenance tick 1 must be greater than previous tick 2`.

- **C1 landed — `ca7f9ef`.** `corpus/fixtures/check_bible.py` (+4/−11, net −7;
  SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`)
  **hash-matches `X2-c1-nullonly.patch` + `X3-c1-tickonly.patch` composed on
  `e97613c`** (baseline `e2bb9639…`; patches `900514ee…` / `16e55359…`) —
  freeze-then-verify PASS, no integrator amendment beyond the composition
  (corroborated by `H2-delta.json` `freeze_then_verify_match: true` and
  `JCAL5-delta.json`, tarball vs disk equal over 860 JSON files). Before→after on
  identical probe inputs (baseline vs delivered checker; seat S1's scratch
  probes): null-from chain → definite `provenance chain break; expected
  from_holder 'mira', got None`; null-from tick → definite `provenance tick 0
  must be greater than previous tick 0`; compared-unresolved tick → tick definite
  while the non-null chain-break correctly stays qualified
  (`possible provenance chain break … 'f3-dup' is not uniquely resolvable`).
  Census replay on the delivered tree: 164 dirs, exits `{0: 32, 1: 132}`, 417
  violation lines, empty stderr; **0 changed tuples of the 160 baseline, 4 new, 0
  exit changes**; B2 agrees 160/160 (`H4-census.json`: 0 mismatches, same
  exits/violations; `H2-delta.json`: 0 exit flips; the FN-2 pair's stdout is
  byte-identical, `1->1` and `2->2` violations). Four new durable fixtures —
  `r90-c1-rawpresent-from`, `r90-c1-rawpresent-to`, `r90-c1-rawpresent-source`,
  `r90-c1-three-causes` — each matching its README-declared after-state. The
  FN-2 pair is present in both census manifests and regression-visible.
  **C9 ruling (recorded in the spec's Closure amendments, not applied silently):
  tick ordering is an integer comparison and holder-identity uncertainty does not
  qualify it; the spec's "compared holders" phrasing is superseded.** r91
  falsification path: if a case emerges where the tick finding needed identity
  context, the ruling is revisited. Bound: the superseding case (unresolved
  *compared* holder tick) is pinned by probes only; no durable fixture carries
  that exact shape.

- **C2 landed — `ca7f9ef` (coverage).**
  `corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md` (22 facts) and
  `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md` (10 facts) with R9
  delivery modes; the five r87 excerpt files carry `Delivery mode (R9): verbatim`
  labels (the four r89 excerpts plus the hymn). One support command,
  `corpus/tools/support_check.py` (+ README). Receipts run on the delivered tree:
  r87 `SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
  MODES 22/22` `RESULT PASS`, exit 0; r88-m3 `SOURCE-SUPPORT 10/10; … MODES
  10/10`, exit 0; paraphrase demo `SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1
  entries (1/1 anchors); MODES 1/1`, exit 0 — a paraphrase anchor cannot count as
  source support. Span enforcement verified on the delivered script (M4's
  blocking D-M4-1 attack replayed): declared line span 7→6 for a line-7 anchor →
  exit 1, `FAIL E1 … span=6; outside-span=7`, `SOURCE-SUPPORT 21/22`; a duplicate
  hit outside the span → exit 1. M5's span fix is integrated. Bound: D-M4-2 is
  unsettled — the script emits per-cluster `N/N` (`22/22`, `10/10`), not a single
  aggregate invocation; the README also states the check is a lexical preflight,
  not fidelity evidence.

- **C3 landed — `ca7f9ef` (depth).**
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` gains three decided
  appendices (37 added lines), merged from seats D1/D2 per seat R1's
  recommendation with a provenance note and retroactivity check: **R8** plausible
  but unrecorded influence → dated, neutral `possible influence: unverified` note
  plus a two-part R2 gate (creator's no-source account AND no contrary
  source-specific evidence AND only a commonplace motif); the
  `external-only / unverified inspiration` marker is reserved for established
  general-motif use. **R9** translator known / source-version unknown → FAILS R5
  support; keep `Delivery mode: translation`, record `Source text/version:
  unidentified; unverified`; a narrow bibliographic-tie exception supports only a
  claim about the identified translation's own wording. **R10** matching name/ID →
  a comparison key, not identity; compared-but-dismissed overlaps are recorded in
  the incoming cluster README under `## R10 comparison outcomes`; the live
  register is reserved for a source-backed shared referent, field, and occasion.
  Register correctly absent: no `corpus/knowledge/cross-cluster-contradictions.md`
  exists; only the r89 worked example (second cluster explicitly hypothetical).
  Drift: the commit message's "R8/R9 chousa cross-references added per K1"
  describes the wave-dir proposal (`patches/D1-decisions.md`); `grep -rn chousa
  corpus/` is empty, so the delivered table carries no such cross-reference.

- **Documentation-parity debt (measured, unrepaired; record-don't-net).**
  `corpus/knowledge/holder-assessment-boundary.md` — the file
  `corpus/fixtures/README.md` names as the current contract — is stale on the tick
  surface: it still documents identity-qualified tick wording
  (`holder identity is not uniquely resolvable: {details}; provenance tick …`,
  refs `:327-333`, `:334-344`, `:345-350`) that the delivered checker no longer
  emits (tick at `:326`; the string occurs nowhere in `check_bible.py`), and its
  definite-form refs `:343-344`/`:349-350`/`:333` now address `:337`/`:326`/`:341`.
  Its own recheck clause (re-verify whenever the provenance branch changes) fired
  without a recheck record. `corpus/fixtures/README.md` has no Round 90 section:
  the four new fixtures, the two maps, and `corpus/tools/` are unindexed; neither
  cluster README names its new map. (Carries r89's open parity items
  Q89-016/017/030/031 forward.)

- **Process and inode pressure.** Two 60 s wait-checks (P3, 06:56:44 / 06:57:44
  −03:00; only `Q1-r90-debt.json` present at the first). The C9 supersession is
  written into the spec's Closure amendments; the four-seat supplementary batch is
  disclosed in the manifest and the commit message; W1's landing record documents
  the 06:12:29 cutoff (17/29 listed seats); SE1/SE3 sentinel inventories exist;
  Q1's debt audit ran inside the work wave and its "freeze not observed" predates
  `ca7f9ef`. `/tmp` was at 100% inodes through the window (0–2,947 free of
  1,048,576): W2's and B1's fixture archives were blocked by `No space left on
  device`, M4 freed only its own partial archive, and `__pycache__` is still
  unnamed in `.gitignore` (a transient `corpus/tools/__pycache__/` was removed by
  P3; Q89-044 remains open).

- **Per-axis verdicts (proposed; L1 adjudication pending — the round is NOT
  admitted here).** calibration **improved (bounded)** — both r89 hedges repaired
  on the delivered tree, freeze hash-match, 0 changed tuples / 0 exit changes
  over the 160 baseline, 4 new durable pins; bounds: the documentation-parity
  debt above and the r91 falsification path for the C9 tick reading. coverage
  **improved (bounded)** — maps plus one span-enforced command whose exit + `N/N`
  is reproducible from the delivered tree; bounds: D-M4-2 per-cluster receipt and
  the lexical-preflight limit. depth **improved (bounded)** — R8/R9/R10 decided
  with owners, triggers, and worked examples; register correctly absent. No axis
  `unchanged`; no `unprovable-but-better` at axis scope. Every claim above
  verifies from the delivered tree; the documentation debt is recorded, not
  netted.

- **Province.** Every changed path is under `corpus/` or `.ufo/`; `PROVINCE.md`
  and `SHONEN.md` bytes are unchanged; the delivered table carries no
  foreign-province content (`grep -rn chousa corpus/` empty; K1's cross-references
  remain proposal-only).

- **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this round
  (no `[x]`); the capabilities table is unchanged; no saturation or retirement is
  declared.

- **Round record.** `LOG.md` and `SCORECARD.md` are unchanged at `ca7f9ef`; this
  entry is the round's LOG record proposal (with a `## Round 90` heading — r89's
  entry lacks one, per Q1) and the SCORECARD proposal is
  `patches/W2-scorecard-r90.proposal.md`. L1 verdicts and any admission are not
  claimed here.
