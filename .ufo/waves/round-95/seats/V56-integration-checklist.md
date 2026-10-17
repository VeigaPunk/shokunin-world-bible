# V56 — integration-checklist (round 95)

**Seat:** V56 integration-checklist (leaf verifier; no nested agents; no commits; no network).
**Role per seat spec:** after all seats land, enumerate L1's exact pre-closure checklist with
priorities (README Round-95 section + census 169, corpus/README bullets, C9 row 4 append with
V17/V48 outputs, receipt fill with real agent IDs, wave bookkeeping reconciliation, any
doc-wording fixes from V41/V46), each with its evidence source.
**Baseline:** r94 closure `fb118c4` (`git rev-parse HEAD` → `fb118c42038ed27a747eec704b9aab41bb4b2ebe`).
**Cutoff:** 2026-10-17 16:45 -03 (wave dispatched ~16:16). Only this file was written; all other
commands were read-only. Census scratch went to `/tmp` (`/tmp/v56-census.py`, `/tmp/v56-census.out`,
`/tmp/v56-poll*.out`), no repo scratch dir declared for this seat.

## 0. Poll-wait record and status at cutoff

Polled every 20 s from 16:17 (four loops, ~28 min total) for the producer artifacts, then for the
specific verifier outputs this checklist cites (V17, V41, V46, V48) and the r95 receipt.

| Target | First present | Status at 16:45 |
|---|---|---|
| P3 fixture tables (`corpus/fixtures/r95-crossing-aftermath/`) | 16:18 | present (10 files, stable) |
| P4 README + map | 16:21 | present |
| P1 tool (`map_obligations.py`) | 16:22 (iterating) → stable 16:26:27 | present, `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` |
| P2 contract + `corpus/tools/README.md` addendum | 16:27:02 / 16:28:26 | present, contract `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` |
| P5 knowledge note | 16:22 → final 16:25:15 (9718 B) | present |
| P1/P2/P3/P4/P5 seat reports | 16:20–16:29 | all five present |
| V17 gates-boundary report (C9 outputs) | 16:28 | present |
| V48 pins-fresh report (C9 row-4 spec) | 16:30 | present |
| V41 r88-doc-consistency report | 16:32 | present |
| **V46 report** | — | **ABSENT at cutoff** (no `V46*` file anywhere under `/home/vgpnk/Projects/shokunin`, excluding unrelated lanes) |
| **r95 receipt `.ufo/waves/round-95/receipt.json`** | — | **ABSENT at cutoff** (V59's generator exists: `.ufo/waves/round-95/seats/V59-scratch/gen_receipt.py`; V59 has no seat report yet) |

Lane seat reports at cutoff: **56** `.md` files in `.ufo/waves/round-95/seats/` (P1–P5 plus 51
verifier reports incl. V30 re-landed in-lane and V53). No seat report was verified from a plan.

## 1. Evidence base (my own commands, all from repo root)

```
$ git rev-parse HEAD                      → fb118c42038ed27a747eec704b9aab41bb4b2ebe
$ git status --porcelain                  → M LOG.md; M corpus/tools/README.md;
                                            M corpus/tools/map-obligations-contract.json;
                                            M corpus/tools/map_obligations.py;
                                            ?? .ufo/waves/round-95/;
                                            ?? corpus/fixtures/r95-crossing-aftermath/;
                                            ?? corpus/knowledge/r95-aftermath-scope-note.md
$ python3 /tmp/v56-census.py              → direct_fixture_dirs=169
                                            exit0=35 exit1=134 other=0 violations=421 stderr_nonempty=0
                                            (reproduces V20 §1 and V31's `ls -d … | wc -l` → 169)
$ wc -l corpus/fixtures/README.md corpus/README.md corpus/knowledge/r91-c9-watch.md SKILL.md corpus/tools/README.md
                                          → 1175 / 37 / 257 / 90 / 119
$ grep -c "r95|Round-95" corpus/fixtures/README.md corpus/README.md SKILL.md → 0 / 0 / 0
  (c9-watch: 1 match, `:253` "Next re-check: r95" only)
$ python3 -c "…json.load…" on the r95 fixture tables → entities 5, relations 1, contradictions 0,
  timeline 4 (ticks 9,9,10,11), sources 4; last event `aftermath-missing-evin` tick 11, actor
  `aru`, place `chalk-stair`, depends_on ["paired-crossing-decision"]
$ sha256sum /home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/*.md
  → V09-c2-inherited-equality.md a5c859ea1361ff549f5e28fd32b6cb3a0aaefaeb6d69294e2baa45e9657025b9 (8376 B, 16:23:48)
  → V18-scope-creep.md           d8d3d6389a0cd80220705a534ff941c3ee11d5c34a49d552cabfb788ae7e9f56 (5792 B, 16:36:20)
$ sha256sum .ufo/waves/round-95/seats/V30-shonen-format.md
  → 833ac442e54db48a068f8aad287cca50e7a10f9be280cae621f1e8f6b2b0c888
  (differs from the earlier parent-repo copy `66344da7…`, now gone from the parent — V30 was
   re-landed in-lane at a new revision)
```

## 2. The checklist (priority order)

### P0 — Decide admission before anything is appended (gate)

Per the LOG.md r95 declaration (uncommitted; V58 audited `LOG.md:2751-2806`): admit iff C1, C2 and
C3 each verify on the delivered revision and no axis is harmed; per-axis verdicts, no scalars.
Inputs now on the delivered revision (all seat reports, lane paths):

- depth — V23 `.ufo/waves/round-95/seats/V23-verdict-depth.md` (IMPROVED, bounded) + V54 crosscheck PASS.
- coverage — V24 `…/V24-verdict-coverage.md` (bottom line, revised: PASS; r88 exit 2→0, "12/12" is total-row count) + V05/V39/V40/V06.
- calibration — V25 `…/V25-verdict-calibration.md` (PASS, bounded) + V55 crosscheck PASS.
- operability — V26 `…/V26-verdict-operability.md` (PASS, bounded). freshness — V27 `…/V27-verdict-freshness.md` (UNCHANGED; conditions C-F1/C-DOC/C-WORD below). adjacency — V28 `…/V28-verdict-adjacency.md` (PASS).
- Adjudicator seat: **no adjudicator report exists at cutoff** (no `V57*` file anywhere). r94 ran an explicit all-axis adjudicator (F27) before its closure; L1 must either obtain one, run the same reconciliation explicitly, or record the absence — not silently skip it (V31 ST-01 flags the verdict set as incomplete at its v1 compile).

### P1 — `corpus/fixtures/README.md`: append the Round-95 section + census 169 (REQUIRED; pin-affecting)

- Site: EOF, after `:1175` (file is 1175 lines; `grep -c "r95|Round-95"` → 0; the Round-94 section occupies `:1154-1175`; append-only precedent `ac69044`).
- Required content (V20 §2A, V31 CL-01): preserving copy of `r94-paired-crossing` + `aru-aftermath-note` + tick-11 `aftermath-missing-evin` (`aru` / `chalk-stair` / `depends_on:["paired-crossing-decision"]`); counts 5/1/4, 4 sources; 15 map obligations = 14 inherited + 1 new; replay receipts measured on the delivered revision (`check_bible` CLEAN exit 0 — V08; `support_check` 15/15 + 2/2 PASS exit 0 — P4; `map_obligations` `OBLIGATIONS raw=15 mapped=15` + `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` exit 0 — P1/P2); **census re-declaration: 169 directories, 35 clean (exit 0), 134 intentional negative (exit 1), 421 violation lines, zero stderr**; dated pin note (the r94 W05 pin `a13d1af3…` for this file was already invalidated by the Round-94 append; this append changes the bytes again — same pattern as `:1175`).
- Wording rule: if the r88 dialect is cited here, use `10/10` obligations + `2/2` editorial = `12/12` total rows, never "12/12 obligations" (P1 §6.1; P2 §6.2; V41 O-1; V58 F1; V27 C-WORD).
- Evidence sources: `V20-doc-parity.md` §1/§2A/bottom line; my census output above; `V08-c2-checker.md`; `P3-fixture-json.md`; `P4-fixture-docs.md`; `V31-debt.md` CL-01; `V27-verdict-freshness.md` C-DOC.

### P2 — `corpus/README.md`: navigation bullets (REQUIRED; pin-neutral)

Four edits, exact sites (V20 §2B; file is 37 lines, no r95 mention):

1. after `:21` (`fixtures/r94-paired-crossing/README.md` bullet) — add the `fixtures/r95-crossing-aftermath/README.md` bullet in the same "Myth-comparison fixture clusters" list;
2. after `:30` (`knowledge/r94-cross-myth-design-comparison.md` bullet) — add the `knowledge/r95-aftermath-scope-note.md` bullet;
3. `:29` — the C9-watch bullet says "including the **r93** re-check entry" (stale by two rows: r94 landed, r95 due); refresh;
4. `:35` — the `tools/map_obligations.py` bullet says "(round 94)" and "`--self-test` (**20** persisted cases)" and "canonical one-obligation-per-row cluster maps"; refresh to 22 cases and point to the Round-95 addendum (`corpus/tools/README.md:101-119`), optionally "(round 94; r95 addendum)". Optional fold-in: `:36` omits `map_obligations.py` from the tools/README description (V41 O-2).

- Evidence sources: `V20-doc-parity.md` §2B; `V41-r88-doc-consistency.md` S-3/O-2; `V31-debt.md` CL-02; `V27-verdict-freshness.md` C-DOC.

### P3 — `corpus/knowledge/r91-c9-watch.md`: append row 4 (REQUIRED; unowned — no producer byte-owns this file)

- Site: EOF (file 257 lines; last check-log row is r94 at `:253`, ending "Next re-check: r95"). Append-only, following the r94 pattern: dated section + cumulative table row (**r92=1, r93=2, r94=3 → this is row 4 / re-check 4**).
- Cite the outputs reproduced by V17 and independently by V48 (both in-lane): checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD …` exit 0 (V17 §1.3); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED …` exit 2 (V17 §1.4, expected control; note the mode field, not the printed hash, identifies the control). Optional fuller due set: the two r91 fixture commands (V48 §4 item 4).
- Row text (V48 §4 item 5): `| 2026-10-17 (r95) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 4 (r95): delivered discrimination held; the `e97613c` control reported REGRESSION-DETECTED as expected; ruling retained. Next re-check: r96. |`
- Carry the gate-3 sentence (re-verified this round, not copied blind): gate 3 remains **not met**, the four-gate falsification trigger remains unsatisfied (`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story evidence.`).
- Evidence sources: `V48-pins-fresh.md` §4 (spec + outputs); `V17-gates-boundary.md` §1.3–1.5; `V20-doc-parity.md` §C; `V31-debt.md` CL-04.

### P4 — `SKILL.md`: refresh the gate-registry row (REQUIRED; unowned extra finding)

Row `:83-89` is stale in three fields (V20 §2E; V41 S-1/S-2):

- `:86` exit-class list — add `schema_drift` to the `1 → failed` class (currently `missing_obligation` / `duplicate_mapping` / `phantom_obligation` / `source_id_mismatch`);
- `:87` "**20 cases**" → 22 persisted cases (`corpus/tools/map-obligations-contract.json`);
- `:89` scope — "for the canonical map form used by the **r93 and r94** clusters; legacy map forms exit 2" is now false as written: the r88 `JSON fact and fields` dialect exits 0 `RESULT PASS` while r87 (co-mapped) and r89 (no source-ID column) stay exit 2; drop BR-02/BR-03 from the residual list (closed by C1) and keep BR-01/BR-04/BR-16 (V41 S-1). Add the `INVENTORY` receipt line (non-gating) if the row describes outputs.

- Evidence sources: `V20-doc-parity.md` §2E; `V41-r88-doc-consistency.md` S-1/S-2; `V31-debt.md` CL-03; r94 precedent (the same row landed as condition C-1 in `ac69044`).

### P5 — fill the r95 receipt with real agent IDs (REQUIRED; receipt ABSENT at cutoff)

- Artifact: `.ufo/waves/round-95/receipt.json` (V59's generator `.ufo/waves/round-95/seats/V59-scratch/gen_receipt.py`; `record_type: "round-95-receipt"`; `EXPECTED = P1–P5 + V01–V59`; per-seat `report_path` + `report_sha256`; `agent_id: null, outcome: null` **by design — only L1 fills them after the batched dispatch returns**).
- L1 must: run/finish the generator on the final report set (it also records duplicate-seat files, missing seats, header/seat mismatches, and the collection curve), then fill `agent_id` and `outcome` from the AgentSwarm dispatch result, plus `dispatch_tool_call_id` and `served_backend_echo`. **Do not invent IDs** (r94 F40/CC-15 precedent: the skeleton with null IDs was usable; the placeholder-filled report was not).
- Reference shape: `.ufo/waves/round-94/followup-receipt.json` (fields: `record_type`, `record_owner`, `phase`, `requested_model`, `requested_seats`, `candidate_commit`, `baseline_commit`, `declaration_commit`, `state`, `agent_id_note`, `collection_snapshot`, `seats[]`, `dispatch_tool_call_id`, `served_backend_echo`, `known_seat_output_defects`).
- Status at cutoff: receipt absent; V59 has no report yet. If V59's own report lands, it is a seat report under the same directory (record it in the roster accounting, P6b).

### P6 — wave bookkeeping reconciliation

- **a. Stranded reports (durability decision).** `V09-c2-inherited-equality.md` (parent path `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/`, sha256 `a5c859ea…`, 8376 B, 16:23:48) and `V18-scope-creep.md` (same parent dir, sha256 `d8d3d638…`, 5792 B, 16:36:20) exist **only in the parent repo**; the lane copies are absent. Parent `git status --short` → `?? .ufo/waves/round-95/`. Same class as r94 CC-11 (fleet-root copy needed an explicit durability decision). V30 was initially parent-only (`66344da7…`) but has been re-landed in-lane at a different revision (`833ac442…`) — treat the lane copy as current. Evidence: my `ls`/`sha256sum` above; `V30-shonen-format.md:206`; `V31-debt.md` CL-06; `V54-crosscheck-depth.md` (V09 note).
- **b. Roster accounting.** 64 seats declared (5 producers + 59 verifiers); 56 lane reports at my cutoff. Absent everywhere at cutoff: **V46, V57, V59 (report)**; parent-only: V09, V18. Record absent seats and any report-quality defects, do not smooth (r94 W20/F40 precedent; `V31-debt.md` CL-08). My seat's brief names V46 as a doc-wording seat — **its output is unavailable to this checklist**; if it lands after this cutoff, L1 should fold its items in.
- **c. No r95 wave-spec.** `.ufo/waves/round-95/` holds only `scratch/` and `seats/`; r94 had `wave-spec.json` + `wave-spec.md` (with its own stale-field history, CC-01). Record or explicitly declare non-applicability (`V31-debt.md` CL-07).
- **d. Closure commits.** r94 pattern: one commit landing conditions (docs/registry/census/C9/receipt — `ac69044` touched exactly `SKILL.md`, `corpus/README.md`, `corpus/fixtures/README.md`, `corpus/knowledge/r91-c9-watch.md`, `corpus/tools/README.md` + receipt) and one closure commit (`fb118c4` = `SCORECARD.md` + `LOG.md`). The r95 declaration in `LOG.md` is uncommitted (`M LOG.md`, +57 lines); the round's producer files are uncommitted. Decide the commit split; SHONEN stays four `[~]`, no `[x]`, no promotion; SCORECARD capabilities row unchanged unless admission decides otherwise.
- **e. Declaration corrections to carry into LOG/SCORECARD.** (1) r88 "12/12 PASS over the r88 map's obligations" → delivered receipt wording `10/10` obligations + `2/2` editorial = `12/12` total rows (V58 F1; P1 §6.1; P2 §6.2; V27 C-WORD; V31 NB-04). (2) "closed BR-02/BR-03" is bounded/partial: drift is entity-claim-container-only and not pinned by the self-test; `map_missing` exercises the absent-map-file variant only, `invalid_arguments` the no-argument path only (V58 F2/F3; V31 NB-01/NB-07).
- **f. Mid-flight defects to disclose, not smooth.** P2 found `invalid_arguments` unimplemented on P1's 16:24:43 revision (fixed 16:26:27; P2 §1a); P1's mid-flight revisions raised an uncaught `ValueError` on r93/r94/r95 (observed by P4/V10/V31; NB-09); the 16:22–16:27 window where the 22-case tool met the 20-case contract and `--self-test` fail-closed with `self_test_contract` exit 2 (PR-01). Receipts must cite the frozen revision (`map_obligations.py` `d1c239cc…`, contract `8173bb97…`).
- **g. P5 note stale pin (C-F1).** `corpus/knowledge/r95-aftermath-scope-note.md:51` pins `map_obligations.py` `9224a684…` (mid-flight) vs delivered `d1c239cc…`; the note self-caveats ("Re-run all three commands against the delivered revision before citing these receipts") and the receipts re-verify green. L1 applies a dated erratum or re-pins (`V19-freshness.md` F-1; `V27-verdict-freshness.md` C-F1; V31 NB-08).
- Evidence sources: `V31-debt.md` CL-05…CL-08/PR-01…PR-03; `V58-claim-text-audit.md` §1; `V27-verdict-freshness.md`; `V30-shonen-format.md`; my own `git status`/`sha256sum`/`ls`.

### P7 — doc-wording fixes (V41 list; V46 ABSENT at cutoff)

- Live sites (fold into P2/P4): `SKILL.md:87`, `SKILL.md:89`, `corpus/README.md:35` (V41 S-1…S-3).
- r94 historical records — deliberate dated-history pattern; at most an inline cross-reference: `SCORECARD.md:374/399/400/416`, `corpus/tools/README.md:95` (V41 S-4…S-8; the Round-95 addendum at `corpus/tools/README.md:101-119` already supersedes the `20/20` example).
- Declaration precision (O-1) and the `corpus/README.md:36` omission (O-2) — fold into P6e/P2.
- **V46: ABSENT at cutoff** — no report anywhere; this checklist cannot incorporate its doc-wording output. If it lands, L1 folds it in.

## 3. Do-not-touch constraints (verified this round)

- Boundary document `corpus/knowledge/holder-assessment-boundary.md` sha256 `7f815a93…` and delivered checker `corpus/fixtures/check_bible.py` sha256 `ff9fd2aa…` are whole-file digest-pinned; `git diff --stat fb118c4` on both is empty and V17's 600 s watcher recorded zero pin violations. No r95 doc edit may touch them (`V17-gates-boundary.md` §2; `V48-pins-fresh.md` §1).
- `corpus/fixtures/README.md` is the only doc in the r94 census pin set whose append invalidates a declared pin; `corpus/README.md`, `SKILL.md`, `corpus/tools/README.md` and `corpus/knowledge/r91-c9-watch.md` are pin-neutral (r94 F30 census analysis; V20 §1).
- r94 fixture and its map are byte-frozen (`git status` empty; V50 §4); the r94 history text in `corpus/tools/README.md` is append-only (P2 verified `new.startswith(old)` → True).

## 4. Verification boundary

This seat ran read-only commands (census sweep, `git`, `sha256sum`, `wc`, `grep`, JSON parses) on
the delivered working tree and read seat reports; it implemented nothing and edited no corpus,
tool, or sibling artifact. All cited outputs are from commands quoted in §1 or from the named seat
reports; items depending on V46 and the receipt are marked ABSENT rather than guessed. No verdict
on any axis is issued here; the checklist's P0 is an input list for L1's admission ruling, not a
ruling.

**Bottom line: PASS (checklist produced; two inputs ABSENT)** — the prioritized pre-closure
checklist is enumerated with exact sites and evidence sources: P1 fixtures-README Round-95
section + census 169/35/134/421/zero-stderr (V20 §2A, my sweep), P2 corpus/README bullets
`:21/:29/:30/:35` (V20 §2B, V41 S-3), P3 C9 row-4 append with V17 §1.3–1.5 outputs and V48 §4
row text, P4 SKILL.md row `:86-89` refresh (V20 §2E, V41 S-1/S-2), P5 receipt fill from the
dispatch result via V59's generator (receipt **ABSENT** at cutoff), P6 bookkeeping (strays
V09/V18 in the parent, absent seats V46/V57/V59, no wave-spec, closure-commit split, declaration
corrections, mid-flight disclosures, C-F1 stale pin), P7 V41 wording list (V46 **ABSENT** at
cutoff); admission itself remains with L1 pending the P0 verdict inputs and any adjudicator.
