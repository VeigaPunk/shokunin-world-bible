# F28 — Round 93 log scribe: LOG record proposal + append-only correction text

Seat: F28 (fresh REQUIRED DeepSeek FOLLOW-UP, regimen 7/12). Requested route:
`opencode-go/deepseek-v4.1-flash` (`.ufo/waves/round-93/deepseek/dispatch-declaration.json`).
Deliverable: this file only. No `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, source,
or fleet write; no commit; no push; no admission claimed.

Judged candidate: `4780cf088ab338f42b85739517aa237c968c4aea` (lane `HEAD`). Pre-round baseline
`87779a00f25bd1855ede479e490123843e5f056e`; original work commit
`65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`. Both are ancestors of `4780cf0`
(`git merge-base --is-ancestor … HEAD` → exit 0 each).

## 1. Measurement boundary and routing limits

- `git rev-parse HEAD` → `4780cf088ab338f42b85739517aa237c968c4aea` (exit 0).
- `git status --porcelain` → only `?? .ufo/waves/round-93/deepseek/`; tracked tree clean.
- `git diff --check` → exit 0.
- Record blobs byte-identical between `87779a0` and `4780cf0`:
  `LOG.md` `e0ff9954ef36c82af44bd0127c291da97dfa1fc6`, `SCORECARD.md` `82de499234b171b6f65221a1f4e1cdae245c857e`,
  `SHONEN.md` `49ec72720a1c49025cab26d99bc0d519c1a2e123`, `PROVINCE.md` `7c599c395e1710b6a7c7aca6d485c373bed6deb7`;
  `git diff --stat 65838f8 4780cf0 -- LOG.md SCORECARD.md SHONEN.md PROVINCE.md README.md` → empty.
- Worktree content hashes at `4780cf0`: `LOG.md` `cbbcd4a255cd0802ff7fb6ae79dcfb63bb013fdcbb52aa2614ec59b8c9b4e158`,
  `SCORECARD.md` `6d1a77ee296c879dbdcb33d951aca269a9952cad4800c144ec8c0b44cc6a5a5b`,
  `SHONEN.md` `9658065ec269bb274eaf34f5c4f65ef48acbcafbf79e05ffd0752c3c318983ef`,
  `SKILL.md` `c9af1afe8c5eab44220568911be2aac7cd6aec9ee17a5f99fe8eae3d82ba65ee`,
  `corpus/fixtures/check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`,
  `corpus/knowledge/holder-assessment-boundary.md` `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`,
  `corpus/tools/boundary_doc_check.py` `ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053`,
  `corpus/tools/discriminate_check.py` `6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef`,
  `corpus/knowledge/r91-c9-watch.md` `7d2647b3854ea05b761dd75c064616751fed69e902ecba4a3cc46c9cb837dc7e`,
  `corpus/knowledge/r93-r8-worked-example.md` `ddac48a1c7690ea31a1871847662fa74d29ef4ed7279338a0af64055524735ef`,
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` `80490adcc8144f0604a4f28ff6008bde037e9a32843530d4c537fa5a2338bb54`,
  `corpus/tools/boundary-doc-contract.json` `e89d2a76d3c8c5c4926c830f6576531d22cf9c18a370cf70ef2657eae1539871`.
- **Routing limit (named, not invented).** The declared request is a model route; the dispatch
  declaration states `backend serving echo is not yet available`, and `served_model_independently_verified`
  is `false` in `.ufo/waves/round-93/recovery/work-dispatch.json`. Invocation is routing evidence only.
  `validate_wave_spec.py --self-test` encodes this: `unknown_backend_echo_is_warning` (observed warning,
  closure still `closure_ready`), exit 0. No provider-serving identity is asserted anywhere in this report.
- **External-verification limit.** This is a dispatched subagent seat. Per `AXES.md` §Working the axes and
  `PROTOCOL.md` §Promotion gates, same-lane/manual review and a dispatched subagent are not an external
  non-author reviewer. Nothing here is a promotion, an `[x]` mark, or an external approval.

## 2. Work performed (commands, observed output, exits)

Run from the lane root at `4780cf0`, exit codes preserved (no pipes around exit codes).

| # | Command | Observed | Exit |
|---|---|---|---|
| 1 | `python3 corpus/tools/boundary_doc_check.py` | `CHECK pinned inputs: PASS / CHECK receipt replay: PASS / CHECK explicit anchor ranges: PASS / CHECK document structure: PASS`; `replay_receipts=3/3`, `replay_cases=14/14`, `anchors=2/2`, `h1_count=1`, `duplicate_headings=0`, `instruction_markers=0`; `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)` | 0 |
| 2 | `python3 corpus/tools/boundary_doc_check.py --self-test` | 8 cases, each `SELF-TEST PASS`: `anchor_range_control` (exit 1, `findings=['anchor_range']`, anchors 1/2), `committed_default` (exit 0), `comment_parked_c9` (1, `document_drift`), `wrong_bare_anchor` (1, `document_drift`), `checker_drift` (1), `missing_document` (1), `missing_checker` (1), `receipt_drift` (1); `SELF-TEST PASS` | 0 |
| 3 | `python3 corpus/tools/discriminate_check.py` | `matches_pin=True`; both fixtures `run_exit=1 stderr_empty=True README_exact=True … pinned_semantic_gate=PASS`; `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression` | 0 |
| 4 | `python3 corpus/tools/discriminate_check.py --checker e97613c` | `pinned_semantic_gate=FAIL` on both fixtures; `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` | **2** (expected negative control, not a passing delivered result) |
| 5 | `python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster` | `INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15`; `RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15`; `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; MODES 15/15; VALIDATED-ROWS 15/15`; `RESULT PASS` | 0 |
| 6 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster` | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 |
| 7 | R8 corrected replay (fenced `sh` block extracted from `corpus/knowledge/r93-r8-worked-example.md` §Corrected replay, run via `bash`) | `R8 replay: PASS / delivered R8 appendix: VERIFIED / record cells: 12/12 / canonical record SHA-256: da934a7e…c7e05` | 0 |
| 8 | R9 completeness block (fenced block under `### r93 R9 completeness-verifier correction`) | `R9 appendix-only baseline: PASS (36/36 requirements)`; 36 named single-clause removals each `FAIL as expected` with the matching sole finding id; `R9 clause-removal controls: 36/36` | 0 |
| 9 | `python3 .ufo/waves/round-93/validate_wave_spec.py --self-test` | 9 controls PASS (closure_ready, corrective count mismatch, requested-model mismatch, served-backend-echo mismatch, duplicate seat id, missing report, phase unresolved, failure-reason missing, unknown-backend-echo warning) | 0 |
| 10 | `python3 .ufo/waves/round-93/recovery/R08-skill-check.py` | 45 source references checked, all PASS; `R08_ARTIFACT_CONTENT_SHA256=c5e6958a…531d` | 0 |
| 11 | `git ls-tree -d --name-only <rev>:corpus/fixtures \| wc -l` | `87779a0` → 166; `4780cf0` → 167 | 0 |
| 12 | `grep -c "^## Round 93" LOG.md` | `0` (no r93 entry; last header is `## Round 92`); `wc -l LOG.md` → 2637 | 1 (expected: pattern absent) |

Independent re-derivation of the r89 replay (F28, not quoted from R24): fixture
`corpus/fixtures/r89-fn2-unresolved-chain-break` copied to a scratch tree under `/dev/shm`,
`entities[4].provenance[0].to_holder` set to `mira` and `provenance[1].from_holder` set to `null`;
each revision's committed checker extracted with `git show <rev>:corpus/fixtures/check_bible.py`
and invoked on the mutated tree (tick 3 = chain only; tick 0 = chain plus tick). Scratch removed
after the run (`ls -d /dev/shm/f28*` → 0). Observed:

| revision | tick=3 | tick=0 |
|---|---|---|
| `51b286b` (r88 closure, pre-r89) | definite chain break | definite tick error **and** definite chain break |
| `e97613c` (r89 closure) | chain break downgraded to *possible*, qualified `from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)` | tick finding identity-qualified by the same vacuous clause; chain break *possible* |
| `ca7f9ef` (r90 repair) | definite chain break restored | definite tick error + definite chain break restored |

All six runs exit 1; the mutation changes finding *strength*, not the exit code. R24's result is
reproduced exactly, including the vacuous `0 raw / 0 indexed` clause.

## 3. Proposed Round 93 `LOG.md` entry (append-only; L1 writes, not this seat)

Supersedes `.ufo/waves/round-93/followup/P3.md`'s fenced proposal, which was measured at `65838f8`
and is superseded by the corrective commit; and W2's pre-delivery draft
(`.ufo/waves/round-93/patches/W2-log-r93.proposal.md`), which records the pre-integration state.

````markdown
## Round 93 — 2026-10-17 (R9 venue repair + replayable R8 dossier + committed bounded certifier; third sourced family — Kojiki; C9 watch re-check 2 + promoted discriminator; work commit `65838f8`, corrective commit `4780cf0`)

- See the fleet report and SCORECARD for the full record. The required FOLLOW-UP was
  re-dispatched as a fresh 32-seat `opencode-go/deepseek-v4.1-flash` wave against the
  committed candidate `4780cf0`; its verdicts are not claimed in this entry.

- **Work wave, 63 seats (accounting corrected).** Baseline `87779a0` (r92 closure, clean).
  The original WORK batch was dispatched with **31** seats against a spec that declared 32 —
  a one-seat shortfall, disclosed in the work commit subject and in
  `.ufo/waves/round-93/recovery/work-dispatch.json`. A separately authorized corrective
  Luna batch returned **32** completed seats (R01–R32) on the same requested route
  `openai-codex/gpt-6-luna-max`, bringing WORK to **31 + 32 = 63 unique dispatched seats**;
  parent strengthening is not a seat and resumes do not add to the count. The original
  shortfall is repaired by the corrective batch, which does not retroactively change the
  original count. Served-model identity remains unverified (no backend echo was present in
  either saved result); the requested route is invocation evidence only.

- **C1 depth (delivered).** The manual R9 gate block sits INSIDE the R9 appendix
  (`r88-sourced-inspiration-decision-table.md`: R8 appendix :28, R8 Kesh worked example :42,
  R9 appendix :44, gate/record/receipt :73/:75/:77, single R9 worked example :79, R10 :87) —
  Q92-002 closes. The R8 worked example gains a replayable dossier
  (`corpus/knowledge/r93-r8-worked-example.md`): the corrected record parses 12 cells and
  compares them against the frozen digest `da934a7e…c7e05` → `R8 replay: PASS`, 12/12, exit 0;
  blank/filler cells fail, and any other noncanonical cell edit returns `R8_RECORD_DRIFT`
  (a bounded frozen-record replay, not a general meaning evaluator). Certification is a
  committed tool: `corpus/tools/boundary_doc_check.py` exits 0 `CERTIFIED` (receipts 3/3,
  cases 14/14, anchors 2/2, h1 1, duplicate headings 0, instruction markers 0) with a
  checker-hash pin (`ff9fd2aa…d1421`) and C9 marker gate; `--self-test` exits 0 over 8 cases
  including the `anchor_range` control that reaches range validation. Scope is bounded:
  frozen-document drift, receipts, explicit-anchor range and structure — no semantic or AST
  validation (named r94 debt).

- **C2 coverage (delivered).** The third sourced-mythology family lands —
  `corpus/fixtures/r93-m2-kojiki-cluster` (Japanese *Kojiki* / Chamberlain translation;
  5 JSON + 6 md). Claim-excerpt map: **12 JSON facts + 3 editorial rows = 15 mapped rows**.
  Receipt: `support_check.py` → `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; MODES 15/15;
  VALIDATED-ROWS 15/15; RESULT PASS`, exit 0; structural checker `CLEAN`, exit 0. **Receipt
  correction:** the work commit message's "10 JSON + 3 editorial" was wrong — the delivered
  cluster measures **12 JSON + 3 editorial** (10 was the unselected candidate's count).
  Census 166 → 167 dirs, 0 changed + 1 new, 0 exit flips; checker bytes unchanged.
  Zero shared referents with the two prior clusters holds at the id/normalized-key level
  (three independent scans, pairwise intersections empty including the r87∩r88 control);
  the integrated conclusion is lexical/author-side and does not close the M2-specific
  semantic review, edition identity, translation fidelity, rights or AI-training permission.

- **C3 calibration (delivered).** The C9 watch gains its SECOND dated re-check row
  (`r91-c9-watch.md` check-log rows :49 and :50): `DISCRIMINATION HELD`, gate 3 not met,
  trigger unsatisfied, ruling retained, `Next re-check: r94.` The discrimination harness is
  promoted to `corpus/tools/discriminate_check.py`: delivered mode exit 0
  `DISCRIMINATION HELD` (`matches_pin=True`); `--checker e97613c` mode exit **2**
  `REGRESSION-DETECTED` — the expected negative control, never a passing delivered result.
  Residuals: row 2 abbreviates the checker hash and shares row 1's calendar date; the
  negative-control mode depends on `e97613c` staying reachable.

- **Corrective commit `4780cf0` (this commit).** Appended corrections to the R8 dossier and
  the R9 completeness verifier (R02/R03/R21/R32), the r88 evidence-cell provenance correction,
  the watch-row correction (R07), a lane `SKILL.md` with the decision table, error signatures,
  the executable integration checklist and the gate/probe registry, the fixtures README
  Round 91 and Round 93 sections, and the tools README Round-93 addendum. `wave-spec.json` +
  `validate_wave_spec.py` land (r92-Q2 debt), the validator exiting 0 over 9 self-test controls.

- **Named debt (recorded, not netted).** (1) Q92-004 open: the R9 verification command still
  reads `.ufo/waves/round-91/patches/D2-edges.patch` rather than the delivered appendix.
  (2) AST/content-signature anchor validation in the certifier — r94. (3) `support_check.py`
  and `discriminate_check.py` have no protocol self-test mode — explicit conformance debt.
  (4) Boundary-doc header carries no r92/r93 re-derivation provenance (R92-E1-06).
  (5) Poll-helper residuals and the unnumbered scratch/inode budget (Q92-006/009); `/tmp`
  measured at ~99% inode use. (6) The M1/M2 candidate selection is an L1 decision recorded in
  the integration record; M6's review was M1-specific, so the M2-specific semantic review
  stays open.

- **Preliminary reports are not the required verdict.** The failed opencode FOLLOW-UP attempt
  (31 parent-declared failures, no raw result available) and the subsequent GLM preliminary
  batch (33 requested, 32 completed, 1 returned failure whose detail says an instance was
  already running) are **not** the required `opencode-go/deepseek-v4.1-flash` verdicts. Their
  per-axis recommendations — including any "admit" recommendation — are preliminary evidence
  and must not be represented as the required-model judgment or as closure. Every GLM seat
  predates the corrective commit `4780cf0`; several of its recorded bounds (missing Round 91/93
  fixture index sections, absent certifier documentation, dossier owner/element-map fields,
  SKILL.md registry drift) are already closed by `4780cf0` and must not be carried forward
  un-reconciled.

- **SHONEN.** No promotion, no push, no merge; `SHONEN.md` bytes unchanged (`49ec7272…`) and
  still carries no `[x]`; capabilities table unchanged; no saturation or retirement declared.
  Box-1's evidence surface changed at `4780cf0` (the lane `SKILL.md` now exists) and box-3's
  filed status is reconciled in the appended correction below — L1's disposition.

- **Round record.** `LOG.md` and `SCORECARD.md` are unchanged at `4780cf0`; this entry is the
  round's LOG record proposal (L1 may append or adapt), and the SCORECARD proposal remains
  `.ufo/waves/round-93/patches/W2-scorecard-r93.proposal.md`. L1 verdicts and any admission
  are not claimed here.
````

## 4. Append-only correction text (proposed for the lane's next record write)

These blocks are written to be appended to the lane's append-only `LOG.md` (and, for the
SCORECARD item, referenced from the round record). They never rewrite filed bytes. They exist
because R24's completion-contract audit of rounds 87–92 returned real protocol debt and the
integration record explicitly requires a re-adjudication/correction record and a re-filed
checklist before the whole 12-round contract can be called satisfied. F28 re-derived the
load-bearing r89 measurement independently (§2, table) rather than citing R24's conclusion.

### 4a. r89 harm re-adjudication (supersedes the r89 closure's no-harm wording)

```markdown
## Round 93 appended correction — r89 admission re-adjudicated (record integrity)

- **Supersedes, never rewrites:** the `## Round 89` closure wording "Every claim verifies; no
  unresolved trade; the round is **admitted**" and the r89 SCORECARD row's
  "recorded as a bounded wording-definiteness regression … disclosed, not netted". The filed
  bytes stay as filed; this entry is the correction.

- **Correction:** the r89 closure commit `e97613c` changed delivered checker semantics against
  the pre-round state `51b286b`: a definite provenance chain break was downgraded to *possible*
  and a tick finding was identity-qualified even where the identity question is vacuous
  (`from_holder None` → "0 raw entity rows carry this id, but only 0 is in the resolved index").
  Independently replayed at F28 (fixture `r89-fn2-unresolved-chain-break`, mutated
  `to_holder=mira` / `from_holder=null`, both revisions' committed checkers, tick 3 and tick 0):
  `51b286b` reports definite findings, `e97613c` reports the downgraded/qualified forms, and
  `ca7f9ef` (r90) restores the definite findings. Exit codes are 1 in every case — the change is
  a loss of finding strength, not of exit status.

- **Verdict correction:** the r89 round carried a real delivered-surface regression. Under
  `AXES.md` §Working the axes ("a round is admitted only if every claim verifies **and no axis
  is harmed**"), recording the regression as a disclosed bound and still declaring "no unresolved
  trade" was a no-harm admission that its own evidence contradicted. r89 is re-adjudicated as
  **harmed (bounded)** in its delivered checker surface, with the harm repaired at r90 `ca7f9ef`.
  The historical row is not relabelled in place.

- **Retroactivity rule (explicit):** the repaired current checker and the current certifier do
  **not** retroactively prove that r89 had no harm. `1b09f3f` and `e97613c` carry identical
  checker bytes, so the regression was present in the admitted r89 closure; only r90's fix
  removed it. No current measurement may be read backwards as a clean r89.
```

### 4b. r91 report `SHONEN` heading defect — re-filed checklist

```markdown
## Round 93 appended correction — r91 report SHONEN re-file (report contract)

- **Supersedes, never rewrites:** `.ufo/reports/round-91/lore.md` is filed once. It carries the
  required work, landed-change and measurement sections but **no `## SHONEN` heading** and no
  four-box assessment; the phrase "Round record, SHONEN…" is not the heading. Per
  `PROTOCOL.md` §Round-robin rounds this is a conformance defect and **disqualifies that report
  as promotion evidence** for the lane's promotion review; the report is otherwise substantial
  and cites real committed work, so it is a defective report, not a contentless marker.

- **Re-filed assessment (this round's report, under the required heading).** `[~]` asserted by
  the lane with a resolvable pointer; no `[x]` — no named non-author verifier exists.
  - Box 1 `[ ]` — SKILL.md now exists (`4780cf0`, decision table + error signatures + checklist
    + registry) but the mark is L1's to set; no `[x]`.
  - Box 2 `[~]` — end-to-end census + probes are logged; six LOG records now.
  - Box 3 `[~]` — the instruction surfaces (checker contract doc, decision tables, fixture
    READMEs, tools README) are delivered-tree-true at `4780cf0`, with reproducible commands;
    still no external verifier.
  - Box 4 `[~]` — province-clean; kotodama acknowledgement still pending (L0 line 6).

- r92's own report carried a four-box section but did not identify it as the r91 re-file; this
  entry is the explicit re-file and closes the defect class for the promotion review.
```

### 4c. SHONEN box-3 record mismatch reconciliation

```markdown
## Round 93 appended correction — SHONEN box-3 record mismatch

- **Supersedes, never rewrites:** the r89 (`:213–219`), r90 (`:254–258`), r91 (`:297–300`) and
  r92 (`:333–336`) SCORECARD SHONEN summaries record box 3 as `[~]` with a pointer, while
  `SHONEN.md:8` reads `[ ]` and has carried that byte since `28706dc`
  (`git rev-parse <rev>:SHONEN.md` → `49ec7272…` at r89, r90, r91, r92, `65838f8`, `4780cf0`).
  r92's report flagged the mismatch and its SCORECARD section repeated it.
- **Correction:** the `[~]` marks in those SCORECARD summaries are unsupported by the file of
  record; they described P4's r89 *proposal* to move box 3 to `[~]`, not a landed mark. The
  lane is the only allowed writer inside its repo, so the reconciliation is a lane write:
  either append the box-3 `[~]` mark plus one indented evidence line to `SHONEN.md`, or record
  the SCORECARD summaries as proposal-state. Marks stay confined to the box character plus one
  indented evidence line per box; no other prose.
- **Effect on calibration claims:** any no-harm or box-state claim resting on the SCORECARD
  summaries is unsupported until this reconciliation lands. The filed sections are not rewritten.
```

## 5. Findings, severity-ranked

1. **High — historical r89 no-harm admission contradicted by its own delivered state.**
   Independently reproduced by F28 (§2). Requires the §4a append-only correction; the repaired
   current checker does not retroactively clean r89.
2. **High — combined report + `MANIFEST.json` commits by the lane (r87–r92).** Per R24, each
   main-repo commit that landed a lore report also modified `MANIFEST.json`, which protocol
   assigns to the integrator-of-record; the lane's main-repo commit is pathspec-limited to its
   own report file. Route an integrator append-only correction record; do not rewrite history.
   F28 did not re-verify these six commits (outside this seat's scope) and reports it as
   R24's finding, not as F28's measurement.
3. **Medium — r91 report's missing `## SHONEN` heading** (§4b): conformance defect, and that
   report is disqualified as promotion evidence until re-filed.
4. **Medium — SHONEN box-3 mismatch persists at `4780cf0`** (§4c): four SCORECARD summaries
   assert `[~]` against a file that reads `[ ]`.
5. **Low-to-medium — record-surface residue still open at `4780cf0`:** Q92-004 (R9 command
   reads a wave patch), R92-E1-06 (boundary-doc header provenance), Q92-006/009 (poll helper,
   scratch/inode budget), and the missing self-test modes on `support_check.py` /
   `discriminate_check.py` (explicit, documented conformance debt — not hidden).
6. **Low — watch row 2** abbreviates the checker hash and shares row 1's date; the
   discriminator's negative-control mode depends on `e97613c` staying reachable.

**Debt closed at `4780cf0` (so it must not be carried forward):** the fixture README's missing
Round 91 and Round 93 sections (now `:1064`, `:1099`), the absent lane `SKILL.md`, the absent
certifier documentation in `corpus/tools/README.md` (Round-93 addendum present), and
`wave-spec.json` + validator (landed, validator self-test exit 0). R32's "R08 registry drift"
finding (a SKILL.md that said the boundary checker had no self-test) is closed by delivery:
`SKILL.md:46` now states the boundary tool exposes `--self-test` and that the missing
self-tests on the other two tools remain debt.

## 6. Per-axis recommendation for the record-scoped surface (F28's own scope)

F28 does not issue verdicts on C1/C2/C3 semantics — that is the follow-up's collective judgment
and L1's admission. For the **record/log surface** this seat owns:

- **calibration (record integrity): `improved (bounded)`** if and only if the §4 corrections
  land as appended entries in the lane's next record write, and **`harmed`/unresolved** if they
  do not — the four unsupported box-3 marks and the un-corrected r89 no-harm wording are
  honesty defects in the lane's own self-assessment, which is exactly the calibration axis.
  Named bounds: this seat verified the r89 replay and the `4780cf0` surfaces first-hand, but
  took the r87–r92 combined-commit defect from R24 without re-running it.
- **depth / coverage (record surface): `unchanged`** — the corrective commit added the lane
  `SKILL.md` and closed index debt, but that is C1/C2 substance owned by other seats; no
  record-scope depth or coverage move is claimed here.
- **Explicitly unprovable here:** served-model identity for either work batch or this wave;
  external non-author verification (no reviewer outside the lane/author set exists on record);
  translation fidelity, exact printed edition, rights and AI-training permission for the Kojiki
  excerpt (editorial comparison only, not an in-world witness or canon).

**Recommendation to L1:** append the §3 entry only after the fresh DeepSeek wave's per-axis
verdicts are recorded, and land §4's corrections in the same record write so the entry is not
filed with a known-false no-harm claim standing beside it. No admission is claimed by this seat.

## 7. Limits and handoff

- Scope honored: this file is the only artifact written by F28. No source, `LOG.md`,
  `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, fleet, staging, commit or push action. No
  delegation, no nested agent CLI, no quota/config/secret scan, no wait/poll loop.
- Scratch: one directory under `/dev/shm` (two scratch shell files plus a copied fixture tree),
  removed after use; `/tmp` untouched. Negative fixtures and the `--checker e97613c` mode were
  compared against their expected exits (1 and 2), not against an all-zero-exit expectation.
- The §3 entry is a proposal, not a filed record: `LOG.md` is byte-unchanged at `4780cf0`
  (`grep -c "^## Round 93" LOG.md` → 0, exit 1). L1 owns the append and every verdict.
- Everything above was measured at the read cutoff at `4780cf0`; the fresh DeepSeek wave's
  other seats were not consulted for evidence, and no peer result is treated as proof here.
