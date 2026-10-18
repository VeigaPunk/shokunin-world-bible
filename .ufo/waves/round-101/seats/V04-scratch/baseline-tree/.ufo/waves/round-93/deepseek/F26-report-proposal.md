# F26 — round-93 fleet-report proposal (fleet-report scribe seat)

Status: **proposal only** — not the actual fleet report, not an axis verdict, not closure, not
promotion. Grounded on the committed corrective candidate `4780cf088ab338f42b85739517aa237c968c4aea`
(tracked worktree == that commit) with this seat's own run headline measurements at
`2026-10-17T14:08-03:00`, plus the committed corrective record. All C1–C3 verdicts remain
**PENDING-L1**. Prelim GLM provenance, no outside `[x]`, source open questions and the historical
correction queue are recorded below.

## Work performed

- Axes under review: depth (C1), coverage (C2), calibration (C3). Scribe dimensions: evidence
  completeness, measurement traceability, write-boundary compliance.
- Scoped reads: `.ufo/waves/round-93/recovery/integration-record.md` first; fleet
  `PROTOCOL.md`/`AXES.md`; committed corpus/tools, corpus/knowledge, `corpus/fixtures/r93-m2-kojiki-cluster/`,
  `SKILL.md` gate registry, `l0-questions.md`; recovery R-reports and R23/R24 evidence; GLM
  `followup/` reports (preliminary, not this wave). Judged `4780cf0` against `87779a0`
  (pre-round) and `65838f8` (original work) where relevant.
- Write scope: only this file. No source edits, staging, commits or pushes; no delegation; no
  nested agent CLIs; no scratch trees created (in-memory heredoc extraction only;
  `PYTHONDONTWRITEBYTECODE=1` on every Python run, so no bytecode or live-tree writes). Stdlib only.
- No sleep/poll/wait loops per this wave's no-wait constraint: no 60 s cadence was run. Two
  non-waiting freeze snapshots instead — opening `git status --porcelain` showed only
  `?? .ufo/waves/round-93/deepseek/`; the closing snapshot at `2026-10-17T14:08:28-03:00` showed the
  same single untracked-dir line, tracked tree clean, HEAD unchanged.
- Seat accounting (committed / declared): original WORK invocation **31 completed** + corrective
  Luna batch **32 completed** = **63 unique WORK seats**, all on the explicitly requested
  `openai-codex/gpt-6-luna-max` route (`recovery/original-work-results.xml` summary `completed: 31`;
  `work-results.xml` `completed: 32`; `work-dispatch.json` seat IDs R01–R32). Model invocation is
  routing evidence only: no served-backend echo exists and none is invented; the wave validator
  treats an unknown echo as a warning, not a closure prerequisite
  (`validate_wave_spec.py --self-test` control `unknown_backend_echo_is_warning`).
- Front-matter note on reports: recovery carries R01–R30 and R32 as Markdown (30 files, including
  `R29-record-errata.md`); R23 is `R23-prior-dispatches.json`; R23/R29/R31 have no local Markdown —
  their completion rests on dispatch-receipt records, per `recovery/R09.md:60`.
- Preliminary GLM provenance (explicitly **not** this required follow-up): `followup/` holds 51
  files; `glm-preliminary-results.xml` summary `completed: 32, failed: 1` against 33 declared
  seats. `wave-spec.json#prior_followup_attempts` records it `status: ineligible`,
  `counts_as_required_followup: false`, `model_independently_verified: false`. Its reports were not
  relabeled and are cited here only as preliminary evidence. Several GLM measurements were taken at
  `65838f8` and are **superseded** where the corrective commit changed the surface (e.g. Q92-004
  R9 re-anchor, Q92-005 fixtures-README index, R93-N3 dossier replay, R93-N4 tools README) — do not
  cite them against `4780cf0` without re-measuring.
- Fresh required wave (this one): `.ufo/waves/round-93/deepseek/` — declared F01–F32 on requested
  route `opencode-go/deepseek-v4.1-flash` (`dispatch-declaration.json`). At the 14:08 cutoff, 15 of
  32 seats had artifacts (F01–F04, F07–F11, F13, F14, F17, F19, F23, F25; 45 seat files plus
  `dispatch-declaration.json`). **Fresh-wave
  peer coverage is unknown until all seats return**; no peer verdict is consumed or synthesized
  here. F26 = this proposal file only.
- Fleet-root state at cutoff (read-only): `?? .ufo/reports/round-93/` exists untracked and holds a
  pre-correction draft `lore.md` (mtime 12:33, written by prelim seat P1, all measurements on
  `65838f8`; its own header says "written by seat P1"); `.ufo/l0-questions.md` is modified-
  uncommitted; `MANIFEST.json` has no round-93 entry (last closure commit `77508a6`, r92).
  The actual r93 fleet report is not yet written/committed at the corrected revision.

### Landed changes at `4780cf0` (as committed; 109 files, +17957/−123)

- C1 depth: R9 manual-gate/required-record/receipt-boundary block repaired into the R9 appendix
  with its worked example; R8 dossier `corpus/knowledge/r93-r8-worked-example.md` with a corrected
  12-cell canonical record and an exact-digest replay; `corpus/tools/boundary_doc_check.py` committed
  certifier + `corpus/tools/boundary-doc-contract.json` pins; `SKILL.md` gate registry for the
  bounded tools.
- C2 coverage: `corpus/fixtures/r93-m2-kojiki-cluster/` (11 tracked files: README, excerpt files,
  claim/excerpt map, symbolism-clause map, inspiration note, and entities/relations/timeline/
  sources/contradictions JSON; third family, M-17
  margin register + bounded Chamberlain/Kojiki editorial comparison); fixtures-README Round 91 and
  Round 93 sections; corpus README wiring.
- C3 calibration: `corpus/tools/discriminate_check.py` committed; C9 watch full-hash clarification
  (row 2 wording replaced, no third row); `wave-spec.json` + `validate_wave_spec.py` landed;
  `l0-questions.md` +2 round-93 lines.
- Corrective-record context: `recovery/` R-reports R01–R30/R32, `integration-record.md`,
  `work-dispatch.json`, three results XMLs; `followup/` GLM batch preserved as preliminary.

### Commands run (this seat, all from `lore-shokunin/`)

1. `git rev-parse HEAD; git status --porcelain; git diff --check`
2. `python3 corpus/tools/boundary_doc_check.py`
3. `python3 corpus/tools/boundary_doc_check.py --self-test`
4. `python3 corpus/tools/discriminate_check.py`
5. `python3 corpus/tools/discriminate_check.py --checker e97613c`
6. `python3 .ufo/waves/round-93/validate_wave_spec.py --self-test`
7. `python3 .ufo/waves/round-93/recovery/R08-skill-check.py`
8. `python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster`
9. `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster`
10. Last `sh` fenced block of `corpus/knowledge/r93-r8-worked-example.md` (`### Corrected replay`),
    extracted in memory and run via `bash -c` (exit captured, not piped away)
11. Last `sh` fenced block of `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
    (the active R9 replacement; historical patch-reading command left untouched as superseded)
12. `sha256sum` of `corpus/fixtures/check_bible.py` and `corpus/knowledge/holder-assessment-boundary.md`
    vs `git show 65838f8:<path>` and `git show 87779a0:<path>`
13. `git ls-tree -d 87779a0 corpus/fixtures/ | wc -l` vs `4780cf0`; `df -i /tmp`

## Before → after measurements

Frames (repeat of the correction queue, so nothing below is misread): negative fixtures
intentionally exit 1; `discriminate_check --checker e97613c` exit 2 is an **expected negative
control**, not a delivered pass; the R8 dossier's first historical block (`5/5` substring checks)
and the R9 table's historical patch-reading command are superseded — only the `### Corrected
replay` block and the last (delivered-text) R9 block were run.

### Baseline identity and integrity

- `87779a0` (r92 closure) → `65838f8` (work; 72 files, +12375/−17) → `4780cf0` (corrective;
  109 files, +17957/−123), dated 2026-10-17 11:54:11 / 14:01:10 −03:00. `HEAD` =
  `4780cf088ab338f42b85739517aa237c968c4aea`, tracked-clean; `git diff --check` → exit 0.
- Fixture census: `git ls-tree -d` count **166 → 167** direct fixture dirs; the only fixture-dir
  delta in `87779a0..4780cf0` is the added `r93-m2-kojiki-cluster/` (9 JSON/MD additions + README +
  symbols; 11 tracked files) and the modified `corpus/fixtures/README.md`. No other fixture-dir
  change — consistent with the committed census claims.
- Frozen pins unchanged the whole round: `corpus/fixtures/check_bible.py` sha256
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` and
  `corpus/knowledge/holder-assessment-boundary.md` sha256
  `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e` are byte-identical at
  `87779a0`, `65838f8` and `4780cf0` (`sha256sum` vs `git show` both sides, 2/2 unchanged).
- `df -i /tmp`: 1,035,522 used / 13,054 free = **1.24% free (99% use)** — the inode gate remains
  over budget and moved the wrong way vs r92's recorded 1.477%. No scratch was created by this seat.

### C1 DEPTH — PENDING-L1 (run headline measurements on `4780cf0`)

- `python3 corpus/tools/boundary_doc_check.py` → exit 0: `CHECK pinned inputs: PASS`, `receipt
  replay: PASS`, `explicit anchor ranges: PASS`, `document structure: PASS`,
  `replay_receipts=3/3 replay_cases=14/14 anchors=2/2 h1_count=1 duplicate_headings=0
  instruction_markers=0`, `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor
  range + structure; no semantic/AST validation)`.
- `--self-test` → exit 0, 8/8 persisted expectations met: `committed_default exit=0`,
  `anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2
  legacy_anchor=check_bible.py:212-224@5eb9451b…`, `comment_parked_c9`, `wrong_bare_anchor`,
  `checker_drift`, `missing_document`, `missing_checker`, `receipt_drift` each exit 1 with its
  named finding.
- R8 dossier active block (`### Corrected replay`) → exit 0: `R8 replay: PASS`, `delivered R8
  appendix: VERIFIED`, `record cells: 12/12`, canonical digest
  `da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05`. The gate is an exact
  normalized-cell drift check over the 12 fixed fields, not a prose-meaning evaluator (blank/
  filler/other-cell edits fail; whitespace-only edits pass by stated policy).
- R9 delivered-text block (last block of the decision table) → exit 0: `R9 appendix-only baseline:
  PASS (36/36 requirements)`, then `R9 clause-removal controls: 36/36` (each single-clause removal
  fails with its own named finding). This is textual completeness of the delivered appendix only —
  not translation fidelity, source identity, rights, or an R9 manual-review PASS.
- Bounds (named debt, not netted): no AST/content-signature anchor validation (deferred to r94);
  the delivered-checker pin is a hardcoded constant, not B3 Gate A's CLI expected-hash argument;
  the colocated contract manifest is not independently pinned against coordinated edits; the
  certifier does no semantic validation of the frozen document's prose. `SKILL.md:44-46` registers
  `discriminate_check` and `support_check` self-tests as missing conformance debt.
- Adjacent, unchanged: `corpus/knowledge/holder-assessment-boundary.md` header still says refreshed
  at round-90 closure (R92-E1-06 residue, untouched this round).

### C2 COVERAGE — PENDING-L1

- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster` → exit 0:
  `CLEAN: schema, citations, relations, timeline; 0 violations`.
- `python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster` → exit 0:
  `RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15`, `SOURCE-SUPPORT 12/12;
  EDITORIAL-ANCHORS 3/3; MODES 15/15; VALIDATED-ROWS 15/15`, `RESULT PASS`. Receipt counts mapped
  rows under declared modes/spans; it is lexical preflight, not whole-claim semantic support or
  rights review.
- Cluster shape as committed: 4 entities, 2 relations, 2 ordered events (Entry A/B), 12 mapped
  in-world JSON fact rows; 3 separately bounded Chamberlain/Kojiki editorial rows; no in-world
  referent from the external translation.
- Cross-cluster claim (author-side/same-lane bound): the selected-cluster review used the
  normalized-key scan `.ufo/waves/round-93/recovery/R10-key-scan.{py,json}` — its **measured
  revision is `65838f8`**, a historical capture, not current HEAD; the input-hash check remains
  useful, and the cluster README's own addendum states the review is the R10 seat's same-lane
  manual inspection (M6's report covers M1's separate candidate), not an outside review. The
  README itself records the M2-specific independent referent/semantic review as pending. Zero
  shared referent/field/occasion was found against r87 and r88-m3; no cross-cluster contradiction
  was registered (`contradictions.json` = `[]`).
- Source open questions (C2, by design): attribution — the source page labels the translator only
  “B.H. Chamberlain, translator 1882”; full-name expansion, the exact printed edition underlying
  the transcription, and translation fidelity are **not independently verified**; rights —
  `Open question — not assessed; no rights grant asserted`; AI-training permission —
  `Open question — not assessed; no permission inferred` (`inspiration-note.md` §§Attribution/
  Rights/AI-training; excerpt `kojiki-chamberlain-excerpt.md:8-10`).

### C3 CALIBRATION — PENDING-L1

- `python3 corpus/tools/discriminate_check.py` → exit 0:
  `mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
  matches_pin=True`; both durable fixtures `README_exact=True`, `baseline_README_exact=True`,
  `changed_line_pairs=1/1`; `RESULT: DISCRIMINATION HELD — silent-revert check would fail on
  regression`.
- `python3 corpus/tools/discriminate_check.py --checker e97613c` → **exit 2**:
  `pinned_semantic_gate=FAIL` on both fixtures, `REGRESSION-DETECTED on
  r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present`. This is the
  declared negative control for the historical-baseline mode; exit 2 alone is not proof of
  regression — the result text plus a valid invocation is (tools README).
- C9 watch (`corpus/knowledge/r91-c9-watch.md`): check-log row 2 (r93, seat X1) records
  `DISCRIMINATION HELD — re-check 2`; the appended r93 clarification replaces the abbreviated hash
  with the full 64-hex value and supersedes the ambiguous “all four gates reproduce” wording with
  the two-fixture discriminator result; falsification-trigger gate 3 remains unmet; next re-check
  r94. No third row was added.
- `python3 .ufo/waves/round-93/validate_wave_spec.py --self-test` → exit 0: eight controls met —
  the `closure_ready` positive plus seven mismatch/missing-receipt controls
  (`corrective_result_counts_mismatch`, `requested_model_mismatch`,
  `served_backend_echo_mismatch`, `duplicate_seat_id`, `required_report_missing`,
  `phase_unresolved`, `failure_reason_missing`) — plus the
  `unknown_backend_echo_is_warning` warning control (`observed_warning=True`).
- `python3 .ufo/waves/round-93/recovery/R08-skill-check.py` → exit 0:
  `source_references_checked=45`, `R08_ARTIFACT_CONTENT_SHA256=c5e6958a82900b07a13c21d80d2dca18899ebd6a92b9d7c0a54830c241ff531d`;
  active dossier anchors, pin manifest and registry fields resolve; register destination correctly
  absent.

### Integrated measurements — frozen at `4780cf0`

Every receipt above is a **delivered/frozen** run at HEAD `4780cf0` (tracked worktree identical to
the commit; only `deepseek/` untracked). No integration amendment occurred after the runs. Labels:
baseline = `87779a0`; candidate = `65838f8`; delivered = `4780cf0`. Peer (F-wave) artifacts are not
integrated evidence and were not read into any receipt above.

## Findings & named debt

- **C1 depth — PENDING-L1:** the C1 trio (venue repair, replayable R8 dossier with its
  12-cell exact-drift gate, committed bounded certifier) verifies by run on `4780cf0`; the frozen
  doc/checker pins prove no drift against `65838f8`. The certifier's bounded scope, the hardcoded
  pin, the missing AST/content-signature anchor validation, the unpinned manifest, and the missing
  self-test modes (`discriminate_check`, `support_check`) are named bounds — none is a passed
  invariant.
- **C2 coverage — PENDING-L1:** the third family is indexed, replays CLEAN, and its support and
  edit rows pass their lexical receipts with row counts (12/12 + 3/3; total 15). The
  zero-shared-referent result is same-lane/author-side at measured revision `65838f8` with the
  independent M2-specific review still pending by the README's own statement; attribution/edition
  verification, rights and AI-training permission stay open questions by design.
- **C3 calibration — PENDING-L1:** second dated re-check row and the promoted discriminator both
  verify (positive exit 0; historical negative control exit 2); the watch wording is corrected and
  gate 3 remains unmet as recorded. Residuals: row date duplicate convention (calendar date shared
  with row 1), no reference to the promoted tool in the watch, next re-check due r94.
- **SHONEN (committed `4780cf0` facts; unchanged since `87779a0`, byte-identical diff):** box 1
  `[ ]`; box 2 `[~]` (evidence `LOG.md` “Fleet round 1 — calibration declaration…” +
  `reports/round-1/baseline-probes.json`; lane assertion); box 3 `[ ]`; box 4 `[~]`
  (`PROVINCE.md:3-11`; lane assertion). **No `[x]` exists** and none is proposed: no named
  non-author verifier has been recorded; same-lane/manual review is not external non-author
  verification for promotion. The persistent SCORECARD-vs-SHONEN box-3 mismatch (R24 item 3) is
  still live — closure must reconcile explicitly, not silently.
- **Closure and records still owed:** `LOG.md` and `SCORECARD.md` are unchanged at `4780cf0`
  (no round-93 entry; `git diff 65838f8 4780cf0 -- LOG.md SCORECARD.md` empty; R93-N10):
  the r93 LOG entry and the SCORECARD r93 section (verdict words after L1 rules) are **owed**.
  Fleet `MANIFEST.json` has no round-93 row; the fleet-root draft `reports/round-93/lore.md` is a
  pre-correction, uncommitted P1 draft measured on `65838f8` — it must not serve as the final
  report for `4780cf0`. Public reporting must record **12 JSON facts** (R93-N5: the work commit
  message says “10”).
- **Prelim GLM provenance (restated for the record):** `followup/` = 51 files, 32 completed /
  1 failed of 33 declared, `ineligible`, not this wave, model not independently verified; its
  `65838f8`-era line items predating the corrective commit are superseded for closure purposes.
- **Historical correction queue (R24, committed; no rewrite permitted):** (1) high — r87–r92
  main-repo commits landing lane reports also modified `MANIFEST.json` under the lane identity —
  write-scope/attribution defect, route to an integrator append-only correction record;
  (2) high — r89’s admitted “no-harm” calibration verdict conflicts with its own evidenced
  regression (checker bytes identical `1b09f3f`..`e97613c`); re-adjudicate via append-only closure
  correction, never relabel silently; (3) medium — SCORECARD/SHONEN box-3 mismatch persists through
  r92; (4) medium — r91 report omits the required `SHONEN` heading; the next report must re-file
  the checklist explicitly. L1 must append the re-adjudication/correction record and re-file the
  checklist before the 12-round contract can be called satisfied.
- **Process/measurement debt:** no poll-helper changes this round (Q92-006); roster/accounting is
  now machine-readable via `wave-spec.json` + validator but the follow-up receipts stay
  parent-only-updated; `/tmp` inode free 1.24% (above-gate, worsening); R10 scan revision is a
  historical capture; `discriminate_check`/`support_check` self-test gaps registered.

## Handoff

- Baseline: `87779a00f25bd1855ede479e490123843e5f056e`; work: `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`;
  final frozen/delivered revision: `4780cf088ab338f42b85739517aa237c968c4aea` (tracked tree clean at
  the 14:08 cutoff).
- Scratch/archive: none created; no `/tmp` writes; no cleanup owed. `PYTHONDONTWRITEBYTECODE=1`
  used throughout.
- Candidate and delivered claim artifacts (paths): `corpus/tools/boundary_doc_check.py`,
  `corpus/tools/boundary-doc-contract.json`, `corpus/tools/discriminate_check.py`,
  `corpus/knowledge/r93-r8-worked-example.md`, `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
  (active R8/R9 appendices), `corpus/knowledge/r91-c9-watch.md`, `corpus/fixtures/r93-m2-kojiki-cluster/`,
  `SKILL.md`, `wave-spec.json`, `validate_wave_spec.py`, `recovery/`, `followup/`.
- Commands/outputs: the 13 command groups above, each with its exit code (exit 2 included only as
  the discriminated negative control; intentional exit-1 fixtures labelled as such). Peer reports
  reviewed: none from this wave (in-flight); prelim GLM `followup/` read as preliminary only.
- Remaining TODOs and named debt: L1 verdicts for C1–C3 (PENDING-L1); r93 LOG entry + SCORECARD
  section + MANIFEST row (closure, integrator acts); final fleet report to be re-grounded on
  `4780cf0` or later; reconcile SHONEN box 3 vs SCORECARD; R24 correction queue; r94 candidates
  (AST anchor validation, CLI expected-hash pin, self-tests for the two tools, watch row 3
  battery, independent M2 referent review, doc-header provenance, inode budget).
- L1 decisions: **PENDING-L1** — nothing in this proposal resolves admission, scores, verdicts or
  promotion.
