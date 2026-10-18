# V25 — receipt (round 101)

Seat: V25, the receipt seat. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Baseline: r100 closure `6f86bf26c26abfd76b7f489ad4a5bb447e7cbc5d`; HEAD at audit time `ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026` (r101 declaration commit, LOG/SCORECARD only; `git merge-base --is-ancestor 6f86bf2 HEAD` → exit 0).
Deliverables: this report + the skeleton receipt `.ufo/waves/round-101/receipt.json` (28-report audit + 1 excess, `agent_id` null for L1 fill).
Byte-ownership honored: I wrote only this report, `receipt.json`, and scratch under `seats/V25-scratch/`. No commits, no pushes, no network.

## Method

Poll-wait protocol executed as specified: census of `seats/` every 20s, max 40 tries per budget, all-reports polls subtract SELF (V25). Census script `V25-scratch/audit_seats.py` (read-only); receipt writer `V25-scratch/build_receipt.py` (writes only `receipt.json`); per-try snapshots `V25-scratch/poll-<n>.json`; raw command log `V25-scratch/stall-escapes.log` + `V25-scratch/evidence.md`.

Presence criteria: file exists, non-empty, ≥200 bytes, seat token within first 20 lines. **Presence is not adjudication** — no claim (C1/C2/C3) is verified by this seat; receipt presence does not admit the round.

## Poll trajectory (SELF subtracted throughout)

| budget | tries (UTC) | non-SELF present | outcome |
|---|---|---|---|
| 1/2 | 03:06:15–03:19:16 (poll-1…40) | 1 → 5 | exhausted → STALL-ESCAPE-1 (recorded, not fatal) |
| 2/2 | 03:19:49–03:32:50 (poll-41…80) | 5 → 19 | exhausted → STALL-ESCAPE-2 (recorded, not fatal; U2 report landed try 79) |
| 3/3 | 03:33:09–03:44:0x (poll-81…~112) | 19 → 27 | stopped early: all 27 non-SELF roster reports present; the script's no-excess exit condition was unsatisfiable while the V28 erratum stands → bounded early stop, recorded, not fatal |

## Final census (pre-SELF snapshot `final-census.json`, 03:44Z; my report lands after it by construction)

- Roster seats present: **27/27** (U1, U2, V01–V26). Missing: none (SELF excluded by convention).
- Excess seat: **`V28`** (`V28-late-bookkeeper.md`, 9766 B, mtime 2026-10-18T03:19:15.570218+00:00) — outside the declared roster U1,U2,V01–V26. Recorded as a **roster erratum** (cf. the r100 precedent, 32 declared / 34 dispatched); the report is kept, not dropped; reconciliation is an L1 follow-up.
- Quality gates: header token in first 20 lines — 28/28 pass; empty reports — 0; tiny (<200 B) — 0; duplicate report prefixes — 0.
- Scratch directories present (not credited as reports): `.V11-scratch`, `.v05-scratch`, `.v14-scratch`, `.v16-scratch`, `.v28-scratch`, `U1-chain-eight-scratch`, `U2-scratch`, `V03-scratch`, `V04-scratch`, `V06-scratch`, `V09-scratch`, `V13-scratch`, `V17-scratch`, `V20-scratch`, `V21-scratch`, `V23-scratch`, `V25-scratch`.

| seat | report | bytes | sha256 (16) | mtime UTC |
|---|---|---|---|---|
| U1 | `.ufo/waves/round-101/seats/U1-chain-eight.md` | 9758 | `7f67a3cde48d8020…` | 2026-10-18T03:21:40 |
| U2 | `.ufo/waves/round-101/seats/U2-r10-register.md` | 7933 | `c550a80f64d1fee0…` | 2026-10-18T03:32:16 |
| V01 | `.ufo/waves/round-101/seats/V01-c1-chain.md` | 8178 | `21af1cfb7debaade…` | 2026-10-18T03:28:20 |
| V02 | `.ufo/waves/round-101/seats/V02-c1-discharge.md` | 7047 | `79ddb64d9da33ac0…` | 2026-10-18T03:21:36 |
| V03 | `.ufo/waves/round-101/seats/V03-c1-repointed.md` | 7492 | `52790db52791245c…` | 2026-10-18T03:23:38 |
| V04 | `.ufo/waves/round-101/seats/V04-c1-selftest.md` | 6977 | `dea196fda3d8a8c2…` | 2026-10-18T03:29:07 |
| V05 | `.ufo/waves/round-101/seats/V05-c1-negative.md` | 12999 | `8ed1db78ee9d3c57…` | 2026-10-18T03:34:01 |
| V06 | `.ufo/waves/round-101/seats/V06-c1-code-review.md` | 9142 | `a9257395bba52012…` | 2026-10-18T03:28:24 |
| V07 | `.ufo/waves/round-101/seats/V07-c2-procedure.md` | 7379 | `fe8f548e9fce82bb…` | 2026-10-18T03:36:37 |
| V08 | `.ufo/waves/round-101/seats/V08-c2-compatibility.md` | 9565 | `a07a57dd4a4bf9b5…` | 2026-10-18T03:28:05 |
| V09 | `.ufo/waves/round-101/seats/V09-c2-no-winner.md` | 9753 | `9dec930023d3b5b0…` | 2026-10-18T03:36:30 |
| V10 | `.ufo/waves/round-101/seats/V10-c2-crossrefs.md` | 7731 | `8ff86a20c6768dc1…` | 2026-10-18T03:30:17 |
| V11 | `.ufo/waves/round-101/seats/V11-preservation-census.md` | 5366 | `b466c714a8743136…` | 2026-10-18T03:36:37 |
| V12 | `.ufo/waves/round-101/seats/V12-gates-boundary.md` | 5933 | `2295da36a065568f…` | 2026-10-18T03:23:42 |
| V13 | `.ufo/waves/round-101/seats/V13-scope-creep.md` | 2450 | `83b5e8220699bf89…` | 2026-10-18T03:15:34 |
| V14 | `.ufo/waves/round-101/seats/V14-freshness.md` | 11325 | `354d3c8f5b809aa5…` | 2026-10-18T03:31:50 |
| V15 | `.ufo/waves/round-101/seats/V15-doc-parity.md` | 10754 | `213c62ded9b181d8…` | 2026-10-18T03:36:09 |
| V16 | `.ufo/waves/round-101/seats/V16-operability.md` | 9845 | `ffab8788a342f10b…` | 2026-10-18T03:34:12 |
| V17 | `.ufo/waves/round-101/seats/V17-adjacency.md` | 7729 | `22ed5caf29ecadf5…` | 2026-10-18T03:34:39 |
| V18 | `.ufo/waves/round-101/seats/V18-verdict-coverage.md` | 8516 | `b70097124dbe3c34…` | 2026-10-18T03:25:55 |
| V19 | `.ufo/waves/round-101/seats/V19-verdict-depth.md` | 8426 | `4d5f4c471e1ef8c7…` | 2026-10-18T03:30:40 |
| V20 | `.ufo/waves/round-101/seats/V20-verdict-calibration.md` | 12610 | `8cd1ca6c4306971d…` | 2026-10-18T03:40:00 |
| V21 | `.ufo/waves/round-101/seats/V21-verdict-operability.md` | 9139 | `833bff22bd271720…` | 2026-10-18T03:31:20 |
| V22 | `.ufo/waves/round-101/seats/V22-verdict-freshness.md` | 10333 | `d97653526b548377…` | 2026-10-18T03:27:09 |
| V23 | `.ufo/waves/round-101/seats/V23-verdict-adjacency.md` | 14468 | `d2fc64291613442e…` | 2026-10-18T03:38:26 |
| V24 | `.ufo/waves/round-101/seats/V24-adjudicator.md` | 14782 | `a076116b72f9e4b4…` | 2026-10-18T03:42:46 |
| V26 | `.ufo/waves/round-101/seats/V26-cross-seat-audit.md` | 6126 | `3eaecff898a54e82…` | 2026-10-18T03:18:18 |
| V28 | `.ufo/waves/round-101/seats/V28-late-bookkeeper.md` | 9766 | `b76fab131b2e206c…` | 2026-10-18T03:19:15 |

## Candidate artifacts at receipt time (presence-level evidence, quoted commands/outputs)

**Baseline/protected.** `git rev-parse HEAD` → `ebec6bbd…`; `git rev-parse 6f86bf2` → `6f86bf26…`; ancestor check exit 0. All five protected files sha256-identical to baseline: PROVINCE.md `94a7a77e…`, SHONEN.md `03b832c7…`, README.md `ad4adb1e…`, l0-questions.md `93105c95…`, corpus/fixtures/check_bible.py `ff9fd2aa…`.

**Wave tree byte-clean.** `git status --porcelain` (minus `.ufo`/`.scratch` noise):
```
 M SKILL.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/knowledge/r101-r10-register-first-entry.md
```
Tracked modifications are exactly U1's four owned files; U2's file is new; no other tracked file touched.

**C1 (pin).** Contract `pins` → 8 keys, new pin `r100-docket-review` (chain r88-m3 → r100); top-level `revision` = `ebec6bbd…` (the disclosed writer-managed refresh). All ten `corpus/fixtures/r100-docket-review/*` files sha256-identical to baseline (`SAME` × 10) — the pin covers an unchanged fixture. `python3 corpus/tools/dependency_freeze.py --help` → exit 0.

**C3 (case).** Contract `self_test.expected` → **19** cases; `repointed_edge` = `{"exit": 1, "finding_ids": ["ADDITION-DETECTED","REDUCTION-DETECTED"], "forbid_traceback": true}` — the claimed both-findings-in-one-run, exit-1 gate. SKILL.md freeze row reads "19 cases … r101 added `repointed_edge`, the wrong-but-earlier repointed dependency edge".

**C2 (entry).** `corpus/knowledge/r101-r10-register-first-entry.md` present (20 565 B, mtime 2026-10-18 00:20 -03:00). Title: "R10 register — first worked entry: an examined NON-conflict at the agreed bell"; record `r101-crossing-agreed-bell-nonconflict-01`; Outcome row: "Examined NON-conflict. Shared referent demonstrated; … the two assertions are COMPATIBLE as stated; no conflict; both claims preserved. No winner, no world-truth assertion, no register entry"; the register destination stays uncreated by design. (Adjudication belongs to the C2 verifier seats; recorded here as presence + claim-shape match.)

## Deviations and bounded stall-escapes

1. Three poll-budget escapes (table above) — all recorded in `stall-escapes.log`, none fatal; wave completed within the third budget window.
2. Roster erratum: declared 28 seats, observed 29 report ids (27 roster + excess `V28`). Recorded in the receipt's `collection_snapshot.excess_seat_ids` and `known_seat_output_defects`; L1 to reconcile (mirrors r100's erratum handling). No report dropped, none invented.
3. Timezone note: file mtimes from `ls` are local (UTC-3); all census mtimes in the receipt are UTC.
4. Poll budget 3 ended by deliberate early stop (condition above) rather than 40 full tries; the stop and reason are recorded in `stall-escapes.log`.

## Skeleton receipt

`.ufo/waves/round-101/receipt.json` — schema mirrors round-100: `seats` rows for U1, U2, V01–V26 (+V28 row, `report_status: "present"`, flagged excess), `agent_id` and `outcome` **null** (this seat cannot observe the AgentSwarm dispatch result), `state` = skeleton, `l1_follow_up` instructs L1 to fill dispatch metadata and adjudicate claims. Hashes in the receipt cover every report file at receipt time.

## Bottom line

PASS — 27/27 declared non-SELF reports present and well-formed (plus recorded excess V28); skeleton receipt emitted; receipt presence is not admission, and no claim was adjudicated by this seat.
