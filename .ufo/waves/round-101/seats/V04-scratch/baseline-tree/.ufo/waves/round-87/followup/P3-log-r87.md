# P3 — Round 87 LOG entry (draft for append to LOG.md)

Seat: P3 (LOG-entry writer), round-87 follow-up wave, world-bible lane.
Measured tree: `lore-shokunin` HEAD `2b48ca72033dfd1060b6f81c4cf27ad83deae57f`
(work-wave evidence commit). This file is a **draft**, not an append: `LOG.md`
is unmodified by this seat. Append-only voice; every figure below was measured
on the delivered tree or re-read from the delivered seat artifacts, never from
a scratch patch.

The section below is the proposed `LOG.md` text.

---

## Round 87 — 2026-10-17 (calibration repair + coverage cluster; luna-max wave; evidence commit `2b48ca7`)

- Baseline before this round is `28706dc73a9b7667851fd82adb71e905ae5eb896`
  (the r86 sync/hardening commit), lane tree clean. The round ran as one
  world-bible work wave recorded under `.ufo/waves/round-87/` — 39 seat
  reports plus prefixed patch artifacts, landed as `2b48ca7` ("39 seat
  reports + patches …, luna-max wave"). No `.ufo/rounds/r87/` plan or
  registry was persisted; the wave is evidenced by that commit and its
  artifacts. Commits: C1 `03c6746`, C3 `e4708cb`, wave evidence `2b48ca7`.
  No push and no merge this round.

- **Motivating evidence — C1 (calibration).** r85 admitted (bounded) that a
  duplicated holder entity silently latches `can_check_chain=False`, hiding a
  real later chain break; r86 was blocked before landing the repair. Measured
  at `28706dc`, the checker emits **one** item-global notice at the first
  ambiguous-holder record and **no** local disclosure on any later record, so
  the later holder mismatch is neither reported nor disclosed. Command from
  the lane root:
  `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous`
  → three findings (duplicate `vault` id, ambiguous `entities[3].provenance[1].to_holder`,
  the single "…unassessed at this and all later records…" notice), `3 violation(s); no canon changed`, exit 1.
  Baseline checker SHA-256 `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132`.
  Cross-checked independently by `C5`, `C6`, `F1`, `S1`, `T1`, `V2`, `CB1` at the same pin.

- **C1 landed — `03c6746`.** `corpus/fixtures/check_bible.py` +17 lines and
  four regression fixtures (`r87-chain-unique-valid`, `r87-chain-unique-broken`,
  `r87-masked-break-to-ambiguous`, `r87-masked-break-from-ambiguous`), 509
  insertions total. After: every provenance record at and after the ambiguous-holder
  stop carries a local disclosure naming the ambiguous field, the holder id, and the
  origin record; the original item-global notice is retained byte-for-byte; the latch
  never resumes and no duplicate identity is chosen. Delivered checker SHA-256
  `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`.
  Reproduce: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous`
  → six findings, exit 1; the three tail lines are
  `VIOLATION: entities[3].provenance[N]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]`
  (N = 0,1,2); both ambiguity directions covered.

- **C1 measurements (delivered tree).** Own full replay of all 138 fixture
  dirs + the 5 round-85 live probes at `28706dc` vs `2b48ca7`: 3 pre-existing
  inputs change stdout — `r85-harbor-repro` (5→7 findings), `r85-isolated-ambiguous`
  (3→4), `r85-masked-ambiguous` (3→5) — with **5 added finding tuples, 0 removed,
  0 reworded, all exit codes unchanged**; the 133 inherited `corpus/fixtures` dirs
  are output-identical apart from the harness-absolute path that five missing-file
  fixtures echo. Fixture-only census 133 → 138 dirs, exits `{0:28,1:105}` → `{0:30,1:108}`.
  Independent corroboration: `C6` (142-input X1 census: `unchanged=139 changed=3
  added_findings=5 removed_findings=0`, exits `{0:32,1:110}` unchanged, `input_hash_differences=0`);
  `V1` (zero changes in the 133 `corpus/fixtures` dirs, five added lines across three
  r85 probes, no control change); `V4` (8/8 provenance mutations disclosed, 0 silent
  passes, per `H3`); `JCAL1` (156 replayed cases, purely additive, zero removals/exit
  changes). The landed diff is byte-identical in added lines to the `X1-c1` candidate
  (independently re-derived by `P4`): `X1` differs from `X2`/`X3`/`X4` by 32/19/68 lines.

- **Motivating evidence + C3 landed — `e4708cb`.** The corpus had no fixture
  exercising a sourced real-world mythology parallel (`S2`), so C3 adds
  `corpus/fixtures/r87-myth-cluster/` (9 files, 256 insertions), selected by
  `M4`/`C7`/`R2` convergence from three independent drafts `M1`/`M2`/`M3`
  (same target paths; only one may land). Inventory on the delivered tree:
  7 entities incl. 2 factions (`shellweavers`, `reedwardens`); 4 relations incl.
  a reciprocal `allied_with` pair sharing source `shell-charter`; 4 timeline
  events with 3 `depends_on` edges; one place contradiction reported-not-resolved
  (`moon-basin-vow-location`: gate-witness vs dune-register); 5 sources; and the
  real-world inspiration note keeping **attribution, rights, and AI-training
  permission as three distinct open questions**. Replay:
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` →
  `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.
  Bounded by `C7`/`JCOV1`: the cluster is a clean input, so it adds positive-path
  surface, **not** a new checker finding template; many cited in-world texts are
  metadata-only and the checker cannot establish source-text support.

- **C2 (depth) — table delivered in the working tree, uncommitted.** The C2
  drafts were evidence-only at `2b48ca7` (`patches/D1-decision-table.md`, 23 rows;
  `patches/D2-decision-table.md`, 30 replay blocks; `SE1`/`T2` replayed 30/30
  outputs) and neither proposed `corpus/knowledge/` destination existed there.
  The D1/D2 merge then landed during this follow-up wave as seat I1's
  `corpus/knowledge/r87-provenance-chain-decision-table.md` (30 rows, lifecycle
  order, `Receipts` section, snapshot pinned to `2b48ca7` and checker SHA-256
  `3ae4134d…`) plus two durable probe fixtures
  (`corpus/fixtures/r87-probe-entry-shape`, `corpus/fixtures/r87-probe-record-and-chain`).
  It refreshes every ambiguous-holder row to the C1 after-state and re-points each
  row at a fixture that ships in the tree, superseding D1/D2's scratch-only probes.
  Both the table and its probes are **untracked/uncommitted** at the time this entry
  was written, so depth is measurable but not yet recorded against a commit:
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain`
  → 35 findings, exit 1; `… r87-probe-entry-shape` → 2 findings, exit 1. I1's census
  (`followup/I1-census.json`) reports 140 dirs, `identical_output=137`, `changed=3`,
  exits `{0:30,1:110}`.

- **Axis verdicts (judged on the delivered tree, per-claim, not by intent).**
  Calibration **improved (bounded)** — `JCAL1` (156 cases, purely additive) and
  the C1 replay above. Coverage **improved (bounded)** — `JCOV1`/`JCOV2` (first
  fixture combining a reported-not-resolved contradiction, 2 factions with a
  sourced reciprocal alliance, and 3 dependency edges). Depth **not yet judged** —
  no seat issued a depth verdict against the committed tree, because I1's
  decision-table landed only in the uncommitted working tree; `P2`/`P1` record
  depth as `TBD-by-parent` / `PENDING-L1`. No axis harmed on any measurement
  (`H2`/`H3`/`H4` harm sweeps: 0 fixtures losing a reported finding, 0 exit-code
  changes). No score is assigned: the bounded 0–10 rubric the plan required was not
  established, so the three owned axes remain unmeasured and unordered. These are
  the follow-up seats' per-axis verdicts; L1 adjudication is still pending
  (`.ufo/reports/round-87/lore.md` records `PENDING-L1`).

- **Census extension (measurement, not an axis claim).** 133 fixture dirs / exits
  `{0:28,1:105}` / 259 violations / 705 tracked corpus JSON at `28706dc` →
  138 dirs / `{0:30,1:108}` / 272 violations / 730 tracked corpus JSON at `2b48ca7`;
  0 non-empty stderr before and after (`I3`, independently reproduced by `P2`/`P4`;
  `S4`'s pre-landing `133+1=134` arithmetic superseded — five dirs were added, four by C1, one by C3).

- **Honest debt (all named, none hidden).**
  - *Mixed-stop over-attribution caveat.* The shipped wording names the holder
    ambiguity as the cause of continued non-assessment even when an earlier invalid
    record latched the gate first (`C5`/`C6`/`D2`). Confirmed on the delivered
    checker: a probe with an unknown `source_id` at `[0]` plus an ambiguous holder at
    `[0]` still emits "…because ambiguous holder identity … first occurred at …" on
    every later record. No delivered fixture covers the mixed-cause case; the fix
    is either a non-causal wording or tracking the original stop cause.
  - *Shipped variant is not the recommended one.* C1 landed the `X1` wording, while
    `R1` ranked `X3` first (minimal, no duplicate stop-row notice, 2 changed inputs
    vs 3). `X1` emits a second disclosure at the stop record already covered by the
    retained global notice. `X2`/`X3`/`X4` remain unlanded alternatives; `V1`/`V3`/`V4`
    verified scratch patches of a *different* wording than the one shipped.
  - *Unlanded variants and fixtures.* `F2`'s five `r87-f2-*` fixtures (incl. the
    null-post-stop variant) are unlanded — only `F1`'s four fixtures landed. `M1`/`M2`
    cluster drafts unlanded by design (paths collide with the landed `M3`). `E1`'s three
    wording candidates are unlanded; the shipped text matches none of them.
  - *Boundary knowledge stale / partial.* At `2b48ca7`,
    `corpus/knowledge/holder-assessment-boundary.md` still describes "exactly one
    notice per item" and self-labels `STATIC PENDING PARENT RUNTIME`, contradicting
    delivered behavior (`CB1`/`X3`/`P4`). Seat I2's refresh is present in the working
    tree but **uncommitted** (25 insertions/17 deletions) and leaves four stale blocks
    (`:104`, `:177-188`, `:222-239`, `:241-245`). The doc's named recheck helper
    `corpus/fixtures/measure_holder_disclosure.py` is absent, so no five-gate score is claimed.
  - *Decision-table merge debt — resolved in the working tree by I1, uncommitted.*
    I1's `corpus/knowledge/r87-provenance-chain-decision-table.md` supersedes both
    D1/D2 drafts and re-points every row at a fixture that ships in the tree
    (`followup/I1-census.json`: 140 dirs, `identical_output=137`, `changed=3`).
    Residual: D1/D2's own scratch probes stay undocumented generators; D2's omission
    of a clean nonempty-chain control (`T2`) is moot only for the superseded draft;
    and the table is untracked, so no committed revision carries it yet.
  - *C3 content gap (`OBS-1`).* `entities.json:33` asserts the Low-Water Hymn names
    the Mother-Tide Gate, but the delivered `lowwater-hymn-excerpt.md` does not contain
    that phrase; the claim's support is not verifiable from the delivered excerpt (`Q2` D-C3-002).
  - *Documentation gaps.* No `## Round 87` section in `corpus/fixtures/README.md`; the
    new fixtures' READMEs declare no expected exit; the ETCSL inspiration is not listed
    in `corpus/knowledge/reference-ledger.md` (`grep -c etcsl` → 0).
  - *Uncovered checker surface.* `S1` enumerated 13 silent-skip classes with no active
    fixture (unavailable source table, duplicate item id, non-array/empty provenance,
    malformed holder shape, invalid tick, etc.); the round's new fixtures cover only the
    ambiguous-holder class (`Q2` D-C1-006).
  - *Evidence-labeling limits.* `B1`'s tuple artifacts carry no revision field, so they
    cannot by themselves establish which revision they ran (`B2`); the `S4` comparator
    uses `text=True`, so "preservation" means return codes and decoded strings, not raw
    bytes; `B6`'s randomized-order run and `V4`'s mutation suite live only in scratch and
    were not independently replayed; `V2`'s X2 verification stayed blocked because the
    patch was absent at its check (`Q2` D-CEN-003/005/007, D-REP-003).
  - *Scope/boundary items.* `F1` ran `git apply` from the main checkout (four untracked
    `r87-*` fixture dirs), then reversed it — a transient out-of-allowlist write, no
    residue. C3's source-method adjacency with `chousa-shokunin` and the newly minted
    `kotodama-shokunin` boundary is escalated as one L0 line (`K2`); `art-east-asian-design`
    is named as a rights recipient in `PROVINCE.md` but is not a fleet-root sibling.
    `K1`'s sibling list is one lane short (kotodama, minted after K1's scan). The round-87
    follow-up roster names a seat `JCAL4` for which no report or artifact exists anywhere
    in the fleet (`Q2` D-C3-009/010/011, D-PROT-002).
  - *No saturation or retirement declared.* The `capabilities` table is still empty and
    no rubric exists, so the stagnation window N is not declarable and the saturation
    line is not set. The historical duplicate-name rejection remains in force.

- **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this round
  (`git diff --name-only 28706dc..2b48ca7 -- SHONEN.md` → empty); all four boxes stay
  `[~]`/`[ ]` with no `[x]` claimed (`P4`). The `[~]` box "logged in LOG.md" is
  satisfied only once this entry is appended. Dispatched reviewers do not qualify as
  outside promotion/discernment verifiers.

---

## Notes for the integrating owner (not part of the LOG text)

- This entry is written to be appended verbatim under the `## 2026-10-16 — protocol
  conformance` section at the end of `LOG.md`. No tracked file was written by P3.
- Figures sourced from seats rather than re-measured by P3 are attributed in-line
  (`C6`, `I3`, `I1`, `JCAL1`, `JCOV1`, `H3`, `P4`). P3's own re-measurements: the 143-input
  before/after replay, the fixture-only census, the delivered/baseline checker SHA-256s,
  the C3 structural counts, the C3/C1/four-fixture replays, the two I1 probe replays,
  and the mixed-stop probe.
- Working-tree state at draft time (01:45 `-03:00`): untracked I1 decision table +
  `r87-probe-*` dirs; uncommitted I2 boundary refresh and K2 `l0-questions.md` append.
  If the integrating owner commits these before appending, drop the "uncommitted"
  qualifiers on the C2 and boundary-doc lines and re-check `git status --porcelain`.
- Depth is the one axis with no judge verdict against a committed tree; once I1's
  table is committed, a depth verdict is the remaining adjudication step.
- Scratch probes used by P3 lived under `/tmp/r87-P3-*` and are not deliverables.
