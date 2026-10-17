# Round-90 wave spec (persisted; roster-as-data per r88 Q2-I3)

Regimen: luna round 4 of 12. Baseline HEAD: `e97613c` (r89 closure; tree clean).
Phase 1 (this spec): WORK wave, 32 seats, `openai-codex/gpt-6-luna-max`.
Phase 2 (follow-up): judging/integration/report — PLANNED LANE
`opencode-go/deepseek-v4.1-flash` (hyper exhausted at r89; the declared tier-2
fallback; `lane_requested=hyper/deepseek-v4.1-flash, lane_served=opencode-go/
deepseek-v4.1-flash, failover=hyper-402` recorded per Q2-I3).
Process debts baked in (r89 Q2): I1 poll loops stay inside the tool cap with
timestamped machine-checkable cadence; I2 the closure commit carries a
hash-stamped freeze; I3 this roster + lane fields + landing record are the
run's data.

Wait protocol: dependent seats poll every 60 s to a 20-minute deadline
(r89 data: all first artifacts landed ≤ 25 min; 10 seats hit a 600 s tool
cap — polls must fit inside one tool call), timestamping each check.

## Declared claims (L1, adopted from r89 SCORECARD planned)

- **C1 calibration** (lowest-axis obligation continues): (i) the r89 hedged
  shapes are repaired — the FN-2 qualifier is gated on non-null ids and on
  identity-dependent comparisons only: `from_holder: null` chains and tick
  findings under unrelated identity uncertainty return to their definite
  wording, while genuinely unresolved holder identities stay qualified;
  (ii) durable fixtures pin FN-1's raw-present half (raw-present/schema-
  invalid `to_holder`, `from_holder`, `source_id` variants) and a ≥3-cause
  valid-key record; (iii) the FN-2 pair joins the canonical census manifest
  so the qualification is regression-visible. Prior 160 tuples preserved
  except enumerable deltas, 0 exit changes.
- **C2 coverage**: (i) in-corpus claim→excerpt maps with R9 delivery-mode
  declarations land for both clusters (r87 gains a map covering all 22 facts
  + the four r89 excerpts get mode labels; r88-m3 gains its map); (ii) one
  reproducible support command lands — a committed checker script whose
  exit code + N/N print IS the receipt (the r89 lesson: a receipt whose own
  command doesn't reproduce is disqualified); (iii) the script enforces R9:
  paraphrase/summary-mode entries cannot count as source-text support.
- **C3 depth**: JDEP2's three undecided sub-cases get decided governance —
  R8 (a general motif carrying a plausible-but-unrecorded influence claim),
  R9 (a translation with named translator but unknown version),
  R10 (two clusters sharing a referent name but different occasions) — each
  as a decided row or an authoritative clarification of R8/R9/R10; the
  cross-cluster register is re-verified correctly empty (no shared referent
  exists; r90 work must not manufacture one).

## Roster (32 seats, phase field)

| seat | phase | claim | mission |
|---|---|---|---|
| B1 | 1 | — | census captain at e97613c (160 dirs) + r90-baseline-tuples.json + hedge before-receipts |
| B2 | 1 | — | independent census #2 |
| B3 | 1 | C1 | before-state: the two hedged shapes verbatim (null-chain, unrelated-identity tick) |
| S1 | 1 | C1 | code scout: predicate-fix + tick-gating edit points and predicted deltas |
| S2 | 1 | C2 | map-format scout: R9 modes for both clusters + script interface design |
| X1 | 1 | C1 | primary (both fixes) + census + delta |
| X2 | 1 | C1 | alternative: null-only fix |
| X3 | 1 | C1 | alternative: tick-gating-only |
| F1 | 1 | C1 | raw-present fixtures ×3 + ≥3-cause fixture |
| C5 | 1 | C1 | design critic (attack X1: gating completeness) |
| C6 | 1 | C1 | separability + exit-risk critic |
| C8 | 1 | C1 | independent delta predictor |
| E1 | 1 | C1 | wording panel (unhedged strings) |
| M1 | 1 | C2 | r87 claim→excerpt map (22 facts, R9 modes incl. four r89 excerpts + hymn) |
| M2 | 1 | C2 | r88-m3 claim→excerpt map |
| M3 | 1 | C2 | the reproducible support command (committed script + README) |
| M4 | 1 | C2 | script verifier + R9-enforcement attack |
| C7 | 1 | C2/C3 | discipline critic |
| K1 | 1 | C2 | connector (chousa/kotodama boundary) |
| D1 | 1 | C3 | sub-case decision drafts #1 (R8-motif, R9-translation, R10-same-name) |
| D2 | 1 | C3 | drafts #2, independent |
| T1 | 1 | C3 | cross-verifier |
| R1 | 1 | C3 | reviewer + retroactivity check |
| J3 | 1 | C3 | register re-verification (stays empty; no false referent) |
| E2 | 1 | C3 | wording for the decisions |
| W1 | 1 | — | wave clerk (landing record) |
| W2 | 1 | — | scribe (SCORECARD/LOG/report proposals) |
| Q1 | 1 | — | r89 debt-auditor + r91 planner |
| SE1 | 1 | — | sentinel (runs last) |

Integration rule (unchanged): authors produce patches; the parent integrates
chosen artifacts; the phase-2 wave verifies the delivered tree (freeze-then-
verify, r88-I1: no integrator amendment without re-verification).

## Landing record

Snapshot cutoff: 2026-10-17T06:12:29-03:00 (poll 20; 17 of 29 listed seats had at least one artifact).
Lane/attempt: `lane_requested=openai-codex/gpt-6-luna-max` (phase-1 declaration); `lane_served=unknown` (not exposed to W1); `attempt=1` (this invocation only); `failover=unknown` (no per-seat dispatch record).

The spec declares 32 seats, but its roster table contains 29 rows. Paths are repository-relative; mtimes are local time (`-0300`). The wave spec is listed as the input artifact; clerk outputs are post-cutoff and omitted from this inventory.

| seat | delivered artifact | mtime (`-0300`) |
|---|---|---|
| — | `.ufo/waves/round-90/wave-spec.md` | 2026-10-17 05:49:46.333569781 -0300 |
| B1 | `.ufo/waves/round-90/B1.md` | 2026-10-17 05:59:58.140747989 -0300 |
| B1 | `.ufo/waves/round-90/patches/B1-tuples.json` | 2026-10-17 05:58:51.509756921 -0300 |
| B2 | `.ufo/waves/round-90/B2.md` | 2026-10-17 06:07:24.673438589 -0300 |
| B2 | `.ufo/waves/round-90/patches/B2-tuples.json` | 2026-10-17 06:00:49.658655231 -0300 |
| B3 | `.ufo/waves/round-90/B3.md` | 2026-10-17 06:00:16.987778909 -0300 |
| B3 | `.ufo/waves/round-90/patches/B3-before-state.json` | 2026-10-17 06:00:16.987778909 -0300 |
| C8 | `.ufo/waves/round-90/C8.md` | 2026-10-17 06:12:20.706865434 -0300 |
| C8 | `.ufo/waves/round-90/patches/C8-delta.json` | 2026-10-17 06:05:09.495451411 -0300 |
| D1 | `.ufo/waves/round-90/D1.md` | 2026-10-17 06:05:58.671311002 -0300 |
| D1 | `.ufo/waves/round-90/patches/D1-decisions.md` | 2026-10-17 06:06:20.719343907 -0300 |
| D2 | `.ufo/waves/round-90/patches/D2-decisions.md` | 2026-10-17 06:11:31.666795791 -0300 |
| E1 | `.ufo/waves/round-90/E1.md` | 2026-10-17 06:10:18.835691680 -0300 |
| E1 | `.ufo/waves/round-90/patches/E1-r90-wording.md` | 2026-10-17 05:59:21.028686476 -0300 |
| F1 | `.ufo/waves/round-90/F1.md` | 2026-10-17 06:06:36.545367435 -0300 |
| F1 | `.ufo/waves/round-90/patches/F1-fixtures.patch` | 2026-10-17 05:58:19.237582060 -0300 |
| K1 | `.ufo/waves/round-90/patches/K1-d1-crossrefs.patch` | 2026-10-17 06:02:46.901018307 -0300 |
| M1 | `.ufo/waves/round-90/M1.md` | 2026-10-17 06:10:34.960714806 -0300 |
| M1 | `.ufo/waves/round-90/patches/M1-r87-map.patch` | 2026-10-17 06:02:35.494000459 -0300 |
| M2 | `.ufo/waves/round-90/patches/M2-r88m3-map.patch` | 2026-10-17 06:07:03.013406625 -0300 |
| M3 | `.ufo/waves/round-90/patches/M3-support-script.patch` | 2026-10-17 06:07:54.765602319 -0300 |
| S1 | `.ufo/waves/round-90/S1.md` | 2026-10-17 06:06:28.341355250 -0300 |
| W2 | `.ufo/waves/round-90/W2.md` | 2026-10-17 06:00:46.123826312 -0300 |
| W2 | `.ufo/waves/round-90/patches/W2-log-r90.proposal.md` | 2026-10-17 06:10:48.869734718 -0300 |
| W2 | `.ufo/waves/round-90/patches/W2-report-r90.skeleton.md` | 2026-10-17 06:00:46.123826312 -0300 |
| W2 | `.ufo/waves/round-90/patches/W2-scorecard-r90.proposal.md` | 2026-10-17 06:10:37.663718679 -0300 |
| X1 | `.ufo/waves/round-90/X1.md` | 2026-10-17 06:11:31.974796230 -0300 |
| X1 | `.ufo/waves/round-90/patches/X1-c1.patch` | 2026-10-17 06:05:08.685235888 -0300 |
| X1 | `.ufo/waves/round-90/patches/X1-tuple-delta.json` | 2026-10-17 06:04:55.990216702 -0300 |
| X2 | `.ufo/waves/round-90/X2.md` | 2026-10-17 06:11:12.860768990 -0300 |
| X2 | `.ufo/waves/round-90/patches/X2-c1-nullonly.patch` | 2026-10-17 05:57:51.204533796 -0300 |
| X3 | `.ufo/waves/round-90/X3.md` | 2026-10-17 06:12:12.821854259 -0300 |
| X3 | `.ufo/waves/round-90/patches/X3-c1-tickonly.patch` | 2026-10-17 05:59:26.679695898 -0300 |

No artifact was present at cutoff for listed seats S2, C5, C6, M4, C7, T1, R1, J3, E2, W1, Q1, or SE1. Three of the declared 32 seats have no roster row, so their identities and delivery state cannot be determined from this spec.

The post-cutoff final status at 2026-10-17T06:12:35-03:00 shows `E1.md` subsequently touched to mtime 2026-10-17 06:12:33.540883604 -0300; its cutoff mtime above is from poll 20. W1's report and this patch are clerk outputs created after the snapshot and are not listed as pre-cutoff artifacts.

## Closure amendments (L1)

- Roster correction: the spec header said "32 seats" while the roster table lists 29; the
  delivered wave is 33 — the four-seat supplementary batch (M5 span fix, C9 tick-gating
  ruling, W3 C7-repair verification, SE3 sentinel) joins the manifest.
- C9 ruling (supersedes the spec's C1 boundary): SHIP the integer-only tick reading
  (X2 null-gate + X3 tick-gating composed; seat C9, 2026-10-17). Tick ordering is an integer
  comparison; holder-identity uncertainty does not qualify it. The spec's "compared holders"
  phrasing is superseded. r91 falsification path: if a case emerges where the tick finding
  needed identity context, the C9 ruling is revisited.
- Follow-up phase lane: opencode-go/deepseek-v4.1-flash (hyper exhausted at r89).

