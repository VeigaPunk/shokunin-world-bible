# V14 — adjacency-final (round 102, capstone)

Seat scope: PROVINCE byte-identity, write confinement, and rights/mechanics boundaries of the new r102 records, judged after production. Axes: charter preservation; lane confinement; producer byte-ownership separation; wave-mechanics hygiene. Baseline r101 closure `542021a`; observed live HEAD `8fa2e87b40b74f8f78864b7044ed0345712af605` (r102 declaration commit, unchanged through close — no commits, no pushes). This is a bounded adjacency verdict over the delivered tree — not round-wide admission; C1/C2/C3 substantive depth is other seats' scope (V15/V07/V08 et al.). Scratch: `.ufo/waves/round-102/seats/V14-scratch/` (audit.py, draft-baseline.md).

## Delivery prerequisite

Protocol poll (every 20 s; artifacts = the three producer byte targets, reports = `U1-*.md`/`U2-*.md` under `.ufo/waves/round-102/seats/`; ENDGAME CONVENTION observed, no self-inclusion):

- **Poll 1** (tries 1–~30): background runner killed at its own 600 s timeout before the 40-try cap; artifacts 0/3, U reports 0/2 at kill. Recorded (runner mechanics, not a protocol deviation).
- **escape1-probe try=31** (06:28:42): knowledge=0/3, Ureports=0/2. Producer-independent V reports landing (V11-gates 06:27, V13-doc 06:23).
- **STALL-ESCAPE-1** (bounded 40 tries, 06:28:45–06:42:05): exhausted at `knowledge=3/3 ureports=1/2` — U1's artifacts landed mid-window (ledger 06:38→06:39 revised, synthesis 06:41), U1's report not yet. U1 demonstrably active, not dead: `U1-scratch/` created 06:30:58.
- **STALL-ESCAPE-2** (bounded 20 tries): `POLL_HIT escape2-try=1` — full delivery present: `r102-freshness-sweep.md` (06:35), `r102-debt-ledger.json` (06:39, 122,763 bytes), `r102-push-synthesis-r95-r102.md` (06:41), `U1-synthesis.md` (06:42), `U2-freshness.md` (06:36). Both escapes recorded per convention; neither fatal. All checks below ran on the delivered bytes.

Both producer reports were read after readiness. U1 claims exactly its two owned files plus declared scratch `U1-scratch/gen_ledger.py`; U2 claims the sweep + two dated addenda. No plan was verified as implementation.

## 1. Province preservation — PASS

Declared audit script `V14-scratch/audit.py`, run from the lane root; terminal output at close on the fully delivered tree:

```text
PROVINCE_BASE_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_HEAD_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_WORK_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_IDENT_BASE_WORK True
PROVINCE_IDENT_HEAD_WORK True
```

Baseline bytes via `git show 542021a:PROVINCE.md | sha256sum`; identical at `8fa2e87` and in the work tree — exact-byte equality, and the same digest r101's V17 recorded (charter continuity). `git diff --stat 542021a..8fa2e87` = LOG.md +44 / SCORECARD.md +33 only (the declaration commits), i.e. the charter did not move pre-round either.

## 2. Write confinement — PASS

Method: `git diff --name-only HEAD` + `git ls-files --others --exclude-standard`, classified against the declared ownership (U1: push-synthesis + debt-ledger.json; U2: freshness-sweep + dated addenda in knowledge files). Terminal lines at close:

```text
TRACKED_CHANGES ["corpus/knowledge/2026-10-12-malformed-error-patterns.md", "corpus/knowledge/r91-c9-watch.md"]
U2_ADDENDA_CANDIDATES ["corpus/knowledge/2026-10-12-malformed-error-patterns.md", "corpus/knowledge/r91-c9-watch.md"]
UNAUTHORIZED_TRACKED []
UNTRACKED_OUTSIDE []
PREEXISTING_STRAY_PRESENT True
HEAD 8fa2e87 lore r102: declare capstone round before dispatch — final round of the loop
```

- Every tracked delta is a U2 addendum, and both are append-only: `git diff --stat` → `15 +` and `46 +` with zero deletions; each carries a dated header ("2026-10-18, round 102, freshness seat U2" / "## 2026-10-18 — r102 re-check (eleventh)").
- New untracked content outside `seats/` is exactly the three U1/U2 artifacts (`corpus/knowledge/r102-*`). Everything else under `.ufo/waves/round-102/seats/` (21 entries at close: 2 U reports, 8 V reports, per-seat scratch incl. U1's declared `gen_ledger.py`).
- Lane-root `.scratch/` (V02 + v26 variants, mtimes 00:04:55/00:16:42 — pre-dispatch r101 carryover, the class r101's V17 recorded) and the r98 stray are present-and-unchanged, not round-102 writes.
- No commits: HEAD at close is still the pre-round declaration commit `8fa2e87`; wave tree uncommitted as the round requires. Outside-lane check (`find . -maxdepth 2 -newermt '2026-10-18 06:15'` excluding lore-shokunin): only sibling lanes' `.git` dirs and root `MANIFEST.json` (mtime 06:15:04 = r101 fleet-close commit `97ac852`, root repo clean) — parallel-lane/operator bookkeeping, no lore-wave write outside the lane.

Mechanics notes (recorded, not adjudicated):

1. **Roster-sum erratum (append-only class):** dispatch brief says "roster U1–U2 + V01–V19" (21 labels) vs LOG declaration "20 seats … U1–U2, V01–V18"; `V19-scratch/` exists so V19 was dispatched. Same mis-sum class as r100/r101 errata; V13-doc.md records it independently; integrator-level.
2. **Pre-round mtime-only touches:** `r101-r10-register-first-entry.md` + `r99-gate-blind-spot-table.md` (06:10:06) and `r91-c9-watch.md` (06:10:59) show post-r101-closure mtimes but tracked-clean bytes — no content write; likely operator git op before first r102 seat activity (06:22).
3. **LOG r102 declaration mis-cite:** C2 names "r100 V33" as a source ledger; no V33 seat/file exists in r100. U1 did not silently fix the LOG (outside its write set) and recorded it as ledger anomaly #1 with the actual r100 surface (V29 conditions + FAILs). Correctly routed, not smoothed.
4. **Carried-count nuance for the C2 seat:** `totals` sum correctly (264 = 111 closed + 108 addressed + 45 carried; 361 = 264 + 97), but 46 items carry a `carried_owner` — two `addressed` items (r96-NB-15, r99-NB-14) hold named residual carries. Synthesis non-achievement 9 says "46 carry past the lane"; `dispositions.carried` = 45. Both defensible under the ledger's counting rules; V07's adjudication scope.

## 3. Rights/mechanics scan of the new records — PASS

All five new/modified knowledge records read (sweep 118 lines in full; synthesis 177 lines in full; ledger parsed; both addenda diffed line-by-line):

- **No real-world rights claims.** PROVINCE keeps attribution/rights/AI-training-permission as distinct questions; nothing in the new records adjudicates any of them. The synthesis asserts the boundary outright (non-achievement 2: "No gate judges entailment, testimony truth, chronology truth, rights, permission, or canon"). Grep for rights/copyright/licence/permission/AI-training across the three new files hits only in-world receipt-attribution titles. `reference-ledger.md` untouched (not in the tracked delta).
- **No game-mechanics verification creep** (game-dev-2d refusal): no `game-dev*` or mechanics-verification language anywhere in the new records; all gate/case vocabulary is this lane's own freeze/map/boundary/support/discriminate/checker suite.
- **No canon claims, no contradiction resolution** (examination-not-canon held): synthesis non-achievement 12 states "no world-truth, winner, or reconciliation is asserted anywhere in the arc"; the addenda supersede only a dangling comparison instruction and append a re-check row — "History above remains unrewritten" / append-only diffs confirm.
- **Claims pinned to verifiable bytes** (mechanics honesty): I independently reproduced — checker pin `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (matches sweep F2, watch addendum, synthesis §3); all 24 commit pins cited by the synthesis exist (`git cat-file -e` → 24/24 OK); SHONEN `grep -c "\[~\]"` = 4, `"\[x\]"` = 0 (honesty ledger exact); ledger JSON parses (python3 json.load) with self-consistent totals and four recorded anomalies.
- **Seat-report hygiene:** all round-102 seat output lives under `.ufo/waves/round-102/seats/`; no report or scratch escaped to another round's or lane's area (audit `UNTRACKED_OUTSIDE []`).

## Bounds

Bounded to this lane's git-visible tree during the observed window (06:20 first seat activity → 06:47 close audit). Not verified here: C1/C2/C3 substantive correctness (V15/V07/V08 scopes), V-seat verdict quality, anything outside the lane root, or post-report writes.

**Bottom line: PASS — PROVINCE byte-identical to baseline `542021a` (digest `94a7a77e…27262aa`, unchanged since r100), all round-102 writes confined to the two producers' declared sets (2 U1 files, 3 U2 files, both addenda append-only), no commits/pushes/outside-lane writes, and the new records make no rights, mechanics, canon, or reconciliation claims while every spot-checked pin (checker sha, 24/24 commits, SHONEN 4/0) reproduces.**
