# Round-89 wave spec (persisted; roster-as-data per r88 Q2-I3)

Regimen: luna round 3 of 12. Baseline HEAD: `51b286b` (r88 closure; tree clean).
Phase 1 (this spec): WORK wave, 32 seats, `openai-codex/gpt-6-luna-max`.
Phase 2 (follow-up): judging/integration/report, `hyper/deepseek-v4.1-flash`
(fallback: opencode-go deepseek flash, then zai glm flash). Evidence:
`.ufo/waves/round-89/` + `followup/`.

Wait protocol (r88 debt I2): dependent seats poll every 60 s to a 25-minute
deadline, timestamping each check; at deadline, proceed with what exists and
record the gap. Integrator amendments must be re-verified on the delivered
tree (r88 debt I1) — phase 2 re-runs the census against the committed hash.

## Declared claims (L1, adopted from r88 SCORECARD planned)

- **C1 calibration** (lowest-axis obligation): (i) durable fixtures pin the
  six unexercised first-cause branches — invalid tick, invalid `from_holder`,
  invalid `to_holder`, dangling `to_holder`, dangling `from_holder`, invalid
  `source_id` — each naming that cause as the first stop with per-record
  disclosures; (ii) valid-key multi-defect records emit the complete combined
  cause summary (extending the r88 shape-branch behavior; precedence question
  settled by naming ALL simultaneous latching causes); (iii) FN-2: chain-break
  findings are qualified when the expected holder identity is not uniquely
  resolvable; FN-1: cause wording distinguishes "absent from the resolved
  index" from truly absent. Prior 149 tuples preserved except enumerable
  deltas, 0 exit changes.
- **C2 coverage**: the r87 cluster reaches 22/22 supported facts under the D1
  support rule by delivering four in-world source excerpts (`gate-witness`,
  `dune-register`, `shell-charter`, `tide-bell-tally`) whose prose supports
  the 14 currently metadata-only facts (6 entity claims, 4 relation edges, 4
  timeline events) with grep-verifiable anchors; the ETCSL ledger row gains
  the `external-only / text not delivered` marker.
- **C3 depth**: the D1 table gains three verified rows governing r88 JDEP3's
  uncovered classes — R8 rights-blocked element disposition (materiality test
  + disposition), R9 in-world excerpt delivery-mode (verbatim / translation /
  paraphrase; a paraphrase cannot serve as the source's own text), R10
  cross-cluster contradiction procedure — plus one durable demo fixture for
  R9, replay-verified.

## Roster (32 seats, phase field)

| seat | phase | claim | mission |
|---|---|---|---|
| B1 | 1 | — | census captain at 51b286b (149 dirs) + r89-baseline-tuples.json + before-receipts |
| B2 | 1 | — | independent census #2 |
| B3 | 1 | C1 | before-state reproducer (multi-invalid output, six-branch probes, FN-1/2 repro) |
| S1 | 1 | C1 | code scout: edit points + predicted deltas for the three amendments |
| S2 | 1 | C2 | support-sweep scout: the 14 unsupported r87 facts + per-fact anchor needs |
| S3 | 1 | C3 | D1-row scout: R8–R10 drafts + r87-cluster compliance needs |
| S4 | 1 | C2 | excerpt-consistency scout: existing r87 narrative context for the 4 sources |
| X1 | 1 | C1 | primary implementation (all three amendments) + census + delta |
| X2 | 1 | C1 | alternative: combined-summary-only |
| X3 | 1 | C1 | alternative: FN-2-qualification-only |
| F1 | 1 | C1 | cause-branch fixtures (tick, from_holder, to_holder) + multi-cause-valid |
| F2 | 1 | C1 | cause-branch fixtures (dangling-to, dangling-from, invalid source_id) |
| F3 | 1 | C1 | FN-2 fixture pair (dup holder w/ one schema-invalid row + control) |
| C5 | 1 | C1 | design critic (attack X1 in scratch) |
| C6 | 1 | C1 | design critic (precedence + over-claim) |
| C8 | 1 | C1 | independent delta predictor (X1 patch census in scratch) |
| M1 | 1 | C2 | gate-witness + dune-register excerpts |
| M2 | 1 | C2 | shell-charter + tide-bell-tally excerpts |
| M3 | 1 | C2 | full-set alternative excerpts |
| M4 | 1 | C2 | excerpt synthesis + fact-to-source map + anchor verification |
| M5 | 1 | C2 | ETCSL ledger-row external-only marker patch |
| C7 | 1 | C2/C3 | discipline critic (locator/rule conformance of drafts) |
| K1 | 1 | C2 | connector (chousa method check) |
| D1 | 1 | C3 | R8–R10 row-set draft #1 |
| D2 | 1 | C3 | R8–R10 row-set draft #2 |
| T1 | 1 | C3 | cross-check D1/D2 vs JDEP3 probes |
| R1 | 1 | C3 | row-set reviewer |
| D3 | 1 | C3 | R9 paraphrase demo fixture + R10 procedure demo |
| E1 | 1 | C1/C3 | wording panel (new cause/qualification strings + R8–R10 phrasing) |
| W1 | 1 | — | wave clerk: maintain this roster's status column during the wave |
| W2 | 1 | — | scribe: SCORECARD/LOG/report proposals |
| SE1 | 1 | — | sentinel (runs last, two wait-checks) |

Integration rule (unchanged): authors produce patches; the parent integrates
chosen artifacts; the phase-2 wave verifies the delivered tree.

## Landing record

Snapshot cutoff: 2026-10-17T03:52:53-03:00 (21 of 31 non-clerk seats had artifacts).
The X1 artifacts appeared at 03:52:46 and were present in the 03:52:53 cutoff inventory.
Mtimes are local time (`-0300`); paths are relative to the repository root.

| seat | delivered artifact | mtime (`-0300`) |
|---|---|---|
| B1 | `.ufo/waves/round-89/B1.md` | 2026-10-17 03:32:08.242863832 -0300 |
| B1 | `.ufo/waves/round-89/patches/B1-tuples.json` | 2026-10-17 03:30:58.425819612 -0300 |
| B2 | `.ufo/waves/round-89/B2.md` | 2026-10-17 03:39:11.839471665 -0300 |
| B2 | `.ufo/waves/round-89/patches/B2-tuples.json` | 2026-10-17 03:28:38.601767059 -0300 |
| B3 | `.ufo/waves/round-89/B3.md` | 2026-10-17 03:31:04.453822589 -0300 |
| B3 | `.ufo/waves/round-89/patches/B3-before-state.json` | 2026-10-17 03:30:51.526492160 -0300 |
| S1 | `.ufo/waves/round-89/S1.md` | 2026-10-17 03:43:30.385021108 -0300 |
| S2 | `.ufo/waves/round-89/S2.md` | 2026-10-17 03:48:07.969690365 -0300 |
| S2 | `.ufo/waves/round-89/patches/S2-fact-map.json` | 2026-10-17 03:45:31.174304570 -0300 |
| S3 | `.ufo/waves/round-89/patches/S3-r8-r10-sketches.md` | 2026-10-17 03:50:22.783034384 -0300 |
| S4 | `.ufo/waves/round-89/S4.md` | 2026-10-17 03:34:30.202011350 -0300 |
| X1 | `.ufo/waves/round-89/patches/X1-c1.patch` | 2026-10-17 03:52:46.130267242 -0300 |
| X1 | `.ufo/waves/round-89/patches/X1-tuple-delta.json` | 2026-10-17 03:52:46.130707982 -0300 |
| X2 | `.ufo/waves/round-89/X2.md` | 2026-10-17 03:50:48.971102278 -0300 |
| X2 | `.ufo/waves/round-89/patches/X2-c1-summary-only.patch` | 2026-10-17 03:30:13.474802801 -0300 |
| X3 | `.ufo/waves/round-89/patches/X3-c1-qualify-only.patch` | 2026-10-17 03:50:19.587026120 -0300 |
| F1 | `.ufo/waves/round-89/F1.md` | 2026-10-17 03:40:57.381684774 -0300 |
| F1 | `.ufo/waves/round-89/patches/F1-cause-fixtures.patch` | 2026-10-17 03:29:55.040525580 -0300 |
| F2 | `.ufo/waves/round-89/F2.md` | 2026-10-17 03:47:16.269561241 -0300 |
| F2 | `.ufo/waves/round-89/patches/F2-cause-fixtures.patch` | 2026-10-17 03:43:20.189997840 -0300 |
| F3 | `.ufo/waves/round-89/F3.md` | 2026-10-17 03:52:44.424405041 -0300 |
| F3 | `.ufo/waves/round-89/patches/F3-fn2-fixtures.patch` | 2026-10-17 03:36:06.884148059 -0300 |
| C5 | — | no artifact at cutoff |
| C6 | — | no artifact at cutoff |
| C8 | — | no artifact at cutoff |
| M1 | `.ufo/waves/round-89/M1.md` | 2026-10-17 03:49:13.478856318 -0300 |
| M1 | `.ufo/waves/round-89/patches/M1-excerpts.patch` | 2026-10-17 03:40:10.747588460 -0300 |
| M2 | — | no artifact at cutoff |
| M3 | `.ufo/waves/round-89/patches/M3-excerpts.patch` | 2026-10-17 03:49:42.519930640 -0300 |
| M4 | — | no artifact at cutoff |
| M5 | `.ufo/waves/round-89/M5.md` | 2026-10-17 03:42:06.684833515 -0300 |
| M5 | `.ufo/waves/round-89/patches/M5-ledger-marker.patch` | 2026-10-17 03:30:55.387818172 -0300 |
| C7 | — | no artifact at cutoff |
| K1 | — | no artifact at cutoff |
| D1 | `.ufo/waves/round-89/D1.md` | 2026-10-17 03:46:27.326440673 -0300 |
| D1 | `.ufo/waves/round-89/patches/D1-rows.md` | 2026-10-17 03:48:36.058761219 -0300 |
| D2 | `.ufo/waves/round-89/D2.md` | 2026-10-17 03:41:58.500815618 -0300 |
| D2 | `.ufo/waves/round-89/patches/D2-rows.md` | 2026-10-17 03:48:09.574694401 -0300 |
| T1 | — | no artifact at cutoff |
| R1 | — | no artifact at cutoff |
| D3 | — | no artifact at cutoff |
| E1 | `.ufo/waves/round-89/E1.md` | 2026-10-17 03:50:42.584085690 -0300 |
| E1 | `.ufo/waves/round-89/patches/E1-r89-wording.md` | 2026-10-17 03:45:39.119323674 -0300 |
| W1 | — | clerk artifacts created after the cutoff; see `W1.md` |
| W2 | `.ufo/waves/round-89/W2.md` | 2026-10-17 03:49:21.407876566 -0300 |
| W2 | `.ufo/waves/round-89/patches/W2-log-r89.proposal.md` | 2026-10-17 03:49:21.407876566 -0300 |
| W2 | `.ufo/waves/round-89/patches/W2-report-r89.skeleton.md` | 2026-10-17 03:31:25.912834516 -0300 |
| W2 | `.ufo/waves/round-89/patches/W2-scorecard-r89.proposal.md` | 2026-10-17 03:49:21.407876566 -0300 |
| SE1 | `.ufo/waves/round-89/SE1.md` | 2026-10-17 03:33:23.571933383 -0300 |

W1's report and landing-record patch are clerk outputs created after this snapshot; their mtimes are recorded in `W1.md`.
