# V19 — presence-final (round 102, lore-shokunin)

- Seat: V19 presence-final · model zai-coding-plan/glm-5.3-flash-low · date 2026-10-18
- Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline: r101 closure `542021a5e54e86edc441577f93fa639082d02877`; HEAD at round start `8fa2e87b40b74f8f78864b7044ed0345712af605` (r102 declaration, LOG/SCORECARD only: `git diff --stat 542021a..HEAD` → 2 files changed, 77 insertions); `git merge-base --is-ancestor 542021a HEAD` → exit 0. Wave tree uncommitted during the round.
- Assignment: LAST seat. Poll until 18 others exist (SELF subtracted), 20-report audit, producer artifacts, finalize the receipt `collection_snapshot`. Writes confined to this report, `V19-scratch/`, and the collection_snapshot/state/l1_follow_up patch to the wave receipt `.ufo/waves/round-102/receipt.json` (the seat-brief assignment "finalize the receipt collection_snapshot", r101 V25 precedent). No commits, no pushes, no network. All commands from the lane root with `python3`.
- Presence is not adjudication: claim adjudication belongs to the C-seats and V18 (adjudicator, ADMIT); this seat audits presence, well-formedness, and cross-artifact consistency at claim-shape level.

## Poll trajectory (SELF subtracted throughout; scripts `V19-scratch/poll.sh`, `poll2.sh`, `grace.sh`; raw logs in `V19-scratch/`)

| budget | window | non-SELF present at end | outcome |
|---|---|---|---|
| 1 (60×20 s, bound 1200 s) | start → t=1200 s | 5 (`synth=no ledger=yes fresh=yes` at terminal) | exhausted → **STALL-ESCAPE-1** (recorded in `stall-escapes.log`, not fatal) |
| 2 (60×20 s, bound 1200 s) | → t=160 s | 18 + all three producer artifacts | **POLL_HIT** per the seat-brief condition (18 others); note: declared seats V12 and V18 still absent at hit |
| grace (30×20 s, bound 600 s) | → t=360 s | V12 landed t=80 s; V18 landed t=360 s | **GRACE_HIT** — full declared roster present; window closed, recorded |

Final census (pre-self snapshot `V19-scratch/final-census.json`; my report lands after it by construction, hash taken post-write for the receipt):

- Non-SELF reports present: **20/20 declared** (U1, U2, V01–V18). Missing: none. Excess: SELF (V19) — see roster erratum below.
- Quality gates: header seat token in first 20 lines — 20/20 pass; empty reports — 0; tiny (<200 B) — 0; duplicate report prefixes — 0; non-report files in `seats/` — none; scratch directories present but not credited: `U1-scratch`, `U2-scratch` (as observed), `V03…V18-scratch`, `V19-scratch`.

| seat | report | bytes | sha256 (16) | mtime UTC |
|---|---|---|---|---|
| U1 | `U1-synthesis.md` | 4918 | `e9af8120b3b3410b…` | 09:42:30.802830 |
| U2 | `U2-freshness.md` | 5019 | `fb4b94259ae2de4b…` | 09:36:08.462300 |
| V01 | `V01-c1-commits.md` | 6231 | `e431a4126f2d0c51…` | 09:48:36.237683 |
| V02 | `V02-c1-deltas.md` | 8262 | `7e7b2fb195c78274…` | 09:47:47.448575 |
| V03 | `V03-c1-tools.md` | 8355 | `2a5f38a49e565fdd…` | 09:46:19.066371 |
| V04 | `V04-c1-honesty.md` | 9107 | `f506ba085f631907…` | 09:50:59.307981 |
| V05 | `V05-c2-ledger.md` | 7915 | `76f980760eede0fb…` | 09:50:39.384941 |
| V06 | `V06-c2-dispositions.md` | 11227 | `25b83c4e33afd92f…` | 09:47:55.694594 |
| V07 | `V07-c2-json.md` | 5736 | `e49d271f31f62efe…` | 09:44:05.440035 |
| V08 | `V08-c3-sweep.md` | 9799 | `dbcfd3d66c65a83b…` | 09:44:37.598119 |
| V09 | `V09-c3-addenda.md` | 5830 | `7e97eaa0537ff307…` | 09:38:03.395461 |
| V10 | `V10-preservation.md` | 7149 | `702545ab3704cf09…` | 09:46:30.097397 |
| V11 | `V11-gates.md` | 8399 | `18278babef7fe88a…` | 09:27:25.944533 |
| V12 | `V12-scope.md` | 8677 | `87f95e777fcc889c…` | 09:53:18.560252 |
| V13 | `V13-doc.md` | 17177 | `544a71fd0f412dd7…` | 09:50:25.631913 |
| V14 | `V14-adjacency.md` | 8891 | `7d984bb4397db9ac…` | 09:48:54.646723 |
| V15 | `V15-verdict-depth.md` | 11574 | `6bdc559586c69096…` | 09:47:03.874476 |
| V16 | `V16-verdict-calibration.md` | 11009 | `28ea0eeb5fa1a094…` | 09:47:48.001576 |
| V17 | `V17-verdict-freshness.md` | 6393 | `47c0dba0f0f0ec71…` | 09:35:47.691271 |
| V18 | `V18-adjudicator.md` | 12200 | `be17c7259c96b7e4…` | 09:57:57.023751 |

## Producer artifacts (presence + audit; sha16 stable across two censuses 09:44Z and 09:59Z — no producer edits after landing)

| artifact | bytes | sha256 (16) | mtime UTC |
|---|---|---|---|
| `corpus/knowledge/r102-push-synthesis-r95-r102.md` (U1) | 15804 | `426ed8262115903f…` | 09:41:42.330764 |
| `corpus/knowledge/r102-debt-ledger.json` (U1) | 122763 | `70fbed21d45ecf2e…` | 09:39:33.060586 |
| `corpus/knowledge/r102-freshness-sweep.md` (U2) | 12093 | `816a4522ec5a4219…` | 09:35:28.394244 |

### Verified clean (my own re-runs, commands quoted)

- **All 24 hashes in the synthesis self-audit exist:** `git cat-file -e <h>` for each of `9c2eea3 abbc3e0 65a9329 ac69044 fb118c4 dcb2d92 60dba0c f3e09f9 2393934 9d25df9 9a3d648 4265df5 111b9a3 337f0fa fe1ce46 ae67105 b5fe472 6f86bf2 a04f986 ebec6bb ceeef43 542021a 60e88bf 8fa2e87` → 24×OK, 0 MISSING.
- **SHONEN:** `grep -c "\[~\]" SHONEN.md` → 4; `grep -c "\[x\]" SHONEN.md` → 0. Matches the synthesis honesty ledger.
- **Census:** `find corpus/fixtures -maxdepth 1 -type d | wc -l` → 175 (− root = **174**, as claimed).
- **Freeze self-test live:** `python3 corpus/tools/dependency_freeze.py --self-test` → `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok` / `SELF-TEST 19/19` / `RESULT PASS`, exit 0. Matches synthesis §3 and sweep receipt line.
- **Ledger internals:** parses as JSON; 264 items; `totals` = `{items: 264, carry_records: 97, source_entries: 361, dispositions: {closed: 111, addressed: 108, carried: 45}}` — sums consistent (111+108+45=264); per-`origin_round` = {94:51, 95:24, 96:51, 97:50, 98:42, 99:25, 100:11, 101:10}, reconciling with the `sources[]` notes' own arithmetic (e.g. r95 own = 10 NB + 10 CL + 3 PR + 1 ST = 24; r98 sections 12+10+13+7 = 42).
- **Ledger source pointers:** all 9 cited files exist (`.ufo/waves/round-94/followup/F29-debt.json` 25 658 B; r95 `V31-debt.json` 27 784 B; r96 `V40-debt.json` 28 015 B; r97 `V37-debt.json` 25 768 B; r98 `V33-debt.json` 17 510 B; r99 `V36-debt.json` 8 496 B + `V74-debt-2.md` 23 613 B; r100 `V29-adjudicator.md` 28 745 B; r101 `V24-adjudicator.md` 14 782 B).
- **Evidence-hash sample:** 16 distinct commit-like tokens across all 264 items' `evidence` fields; 12 sampled → 12/12 `git cat-file -t` = commit.
- **r95 delta row vs SCORECARD:** synthesis §2 r95 row (verdicts calibration/depth/coverage/operability improved (bounded), freshness unchanged, adjacency unchanged; claims schema_drift 20→22, `r95-crossing-aftermath` 5/1/3→5/1/4, r88 dialect; census 168→169; `fb118c4`→`dcb2d92`) matches the SCORECARD "Round 95 — closed, ADMITTED" section line-for-line.
- **Sweep F1 confirmed and corrected on disk:** `git cat-file -t b6ca1e902f2bf08b8acddaef665d9764f8636981` → fatal, exit 128; `git log --all | grep -c b6ca1e90` → 0; dated addendum present at `2026-10-12-malformed-error-patterns.md:22` ("Correction addendum (2026-10-18, round 102, freshness seat U2)"), file mtime 06:34:24 −03:00.
- **Sweep F2 confirmed on disk:** `r91-c9-watch.md:371` "2026-10-18 — r102 re-check (eleventh)" with the cadence-end note; same mtime.
- **Protected files 5/5 byte-identical to baseline:** PROVINCE.md `94a7a77e1810f37f…`, SHONEN.md `03b832c75efbf813…`, README.md `ad4adb1e6cfbec41…`, l0-questions.md `93105c95247bb80e…`, corpus/fixtures/check_bible.py `ff9fd2aa6811a813…` (worktree sha256 == `git show 542021a:<path>` sha256, `SAME` ×5).

### Cross-artifact defects found by this seat (all non-blocking, wording/counting class; corroboration from other seats noted)

- **D1 — "46 carried" vs ledger 45.** Synthesis §5.9: "46 debt items carry past the lane (of 264 consolidated) … owner `r103+ (operator)`". Ledger: `carried` = 45 (per-round carried sums 24+4+8+6+2+1 = 45); of those, 44 have `carried_owner` "r103+ (operator; lane closes at r102)" and **1 (`r97-NB-20`) has a null `carried_owner`**. Corroborated independently by V02, V04 (FAIL, bounded), V15.
- **D2 — dangling r96 debt pointer in the synthesis header.** Header source glob `` `.ufo/waves/round-9{5,6,7}/seats/V3{1,0,7}-debt.json` `` expands r96 → `V30-debt.json`, which does not exist (`ls` → No such file); the real r96 source is `V40-debt.json`, exactly as the ledger's own `sources[]` cites. Corroborated by V05 (its D2).
- **D3 — ledger self-contradictory `bottom_line`.** Top-level `bottom_line` string: "273 items + 88 carry records = 361 source entries accounted" vs the same JSON's `totals` and delivered items: **264 items + 97 carry records = 361**. Same total, wrong split — a stale draft string inside the delivered artifact. Corroborated by V15.
- **D4 — synthesis self-audit undercount.** §4 claims "all 24 hashes cited in this record were checked"; the body cites **25** distinct 7-hex tokens — `e97613c` (the `discriminate_check.py` negative-control revision, §3 gate table) is absent from the self-audit list. All 24 listed still verify. Corroborated by V01.

Also witnessed: the r102 LOG declaration's debt-source citation "r100 V33" names a seat that does not exist (round-100 roster was T1–T4 + V01–V30; `ls .ufo/waves/round-100/seats/ | grep V3[123]` → empty) — the ledger's `sources[]` itself records this anomaly and substitutes `V29-adjudicator.md` + LOG r100 closure.

## Receipt finalization

V18 (adjudicator) wrote the skeleton `.ufo/waves/round-102/receipt.json` (state "SKELETON written by V18 adjudicator (FINAL seat)…") including its own `collection_snapshot` taken at 09:58Z, when my report did not yet exist ("NO V19 report exists" — accurate at write time). This seat, per its brief ("finalize the receipt collection_snapshot"), patched **only** `collection_snapshot` (replaced with the finalized census: 21 filed reports incl. SELF, 20 non-SELF, 0 missing, excess `[V19]` vs the LOG-declared 20-roster, both roster variants recorded), appended a `V19` row to `seats` (real bytes/sha256/mtime, `agent_id`/`outcome` null), and appended V19-finalization notes to `state` and `l1_follow_up`. V18's `adjudication`, all existing seat rows, hashes, and every other key are preserved untouched. Finalizer script: `V19-scratch/finalize_receipt.py`.

## Deviations, errata, and bounded escapes (all recorded in `V19-scratch/stall-escapes.log`)

1. STALL-ESCAPE-1 (budget 1 exhausted at 5 others) and the grace window (opened because the poll condition "18 others" was met while declared seats V12/V18 were absent; V12 landed t=80 s, V18 t=360 s) — both recorded, neither fatal.
2. **Roster erratum (standing class, third of the push):** LOG declares 20 seats (U1–U2 + V01–V18); the dispatch brief read "U1–U2 + V01–V19" (21 ids) and this seat is V19. Filed set after this report: 21 reports — 20 declared + SELF as the excess, exactly the brief's 21-id roster. Recorded in the finalized snapshot (`roster_arithmetic_note`); reconciliation is an L1 follow-up. No report dropped, none invented.
3. **Dual-final-seat overlap:** V18's brief also says FINAL (adjudicator + skeleton receipt); V19's brief says LAST (finalize collection_snapshot). Resolved without conflict: V18 owns adjudication and the skeleton; V19 owns the finalized snapshot; the patch preserved V18's bytes outside the three patched fields.
4. V17's freshness verdict is ABSENT-at-cutoff (its 40-try window expired before U2's sweep artifact landed at 09:35:28Z; V17's report filed 09:35:47Z). The artifact has since landed and was audited above; V17's report stands as filed — supersession is the adjudicator's/L1's to record, not this seat's.
5. Timezone note: receipt/snapshot timestamps are UTC; `ls` mtimes quoted in prose are local (UTC−3).

## Bottom line

PASS — full declared roster 20/20 present and well-formed (plus SELF as the recorded excess per the 21-id brief roster), all three producer artifacts delivered and audited (verified-clean list above; four non-blocking cross-artifact defects D1–D4 pinned and corroborated), collection_snapshot finalized into V18's skeleton receipt without disturbing the adjudication; receipt presence is not admission — but V18 adjudicated ADMIT on the same delivered bytes.
