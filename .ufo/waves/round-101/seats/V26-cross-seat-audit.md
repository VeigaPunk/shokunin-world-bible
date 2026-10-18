# V26 — cross-seat-audit (round 101, lore-shokunin)

Seat: V26 · lane: lore-shokunin · date: 2026-10-18 · model: zai-coding-plan/glm-5.3-flash-low
Task: re-run load-bearing quoted outputs from other seats; verdict REPRODUCED / MISMATCHED per quote. All commands below were executed by me from the lane root; quotes compared byte-for-byte against the cited seat reports.

## Method

1. Pre-round baseline captured before any producer write (00:03–00:05): chain 7/7 `RESULT PASS` with per-fixture digests; `r100-docket-review` → `UNPINNED-FIXTURE / RESULT ERROR`; `--self-test` → `SELF-TEST 18/18 / RESULT PASS`; contract `revision b5fe4729…`, 7 pins, 18 cases; `corpus/knowledge/r101-r10-register-first-entry.md` absent.
2. Poll-wait per protocol: 40 tries × 20s (00:03–00:16). Outcome: U1's contract+tool landed mid-window; U1 producer report never landed; U2's knowledge file never landed (`r101file=N` on all 40 tries; still ABSENT at 00:17:46). Stall-escape recorded, not fatal: audit proceeds on the reports that exist (V02 final; V13/V22 stubs marked IN PROGRESS).
3. Six load-bearing quoted outputs selected (V02 ×5, V22 ×1 — the only reports with quoted terminal outputs). Each re-run independently; mutation scratch rebuilt under `.scratch/v26/` (my own), not V02's.

## Re-run ledger

**R1 — V02 quote B, delivered r100 verify.** Quoted: `FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1` / `DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19` / `RESULT PASS` / exit 0. Mine: `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review` → identical 4 lines, `exit=0`. **REPRODUCED.**

**R2 — V02 self-test tail (C3 witness).** Quoted: `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok` / `SELF-TEST 19/19` / `RESULT PASS` / exit 0. Mine: `python3 corpus/tools/dependency_freeze.py --self-test | tail` → identical tail incl. the `repointed_edge` line, `exit=0`. Baseline was 18/18 (my 00:04 run), so 18→19 is real and the new case enforces both findings in one run. **REPRODUCED.**

**R3 — V02 quote A1, clean scratch copy.** Rebuilt the same structure (`ROOT = parents[2]` ⇒ mirror `corpus/{tools,fixtures}`) under `.scratch/v26/scratch-root/`: `python3 .scratch/v26/scratch-root/corpus/tools/dependency_freeze.py .scratch/v26/scratch-root/corpus/fixtures/r100-docket-review` → identical `FREEZE 9/9; 8/8; 1/1`, same DIGEST `77debadf…`, `exit=0`. Also validates V02's structural claim that the copy is self-contained. **REPRODUCED.**

**R4 — V02 quote A3, scratch mutation.** Set `depends_on=[]` on timeline index 8 (`clerk-review-first-passage`, tick 16) in my own scratch copy, re-ran: `FREEZE r100-docket-review: events 9/9; dependency-edges 7/8; relations 1/1` / `FINDING REDUCTION-DETECTED: event clerk-review-first-passage lost depends_on ['clerk-lapse-recorded']` / `RESULT FAIL` / `exit=1` — byte-identical to V02's A3. Pin is live against its own edge, not a paper pin. **REPRODUCED.**

**R5 — V02 chain table, 8/8 clean.** Quoted: all eight fixtures `exit=0 RESULT PASS`. Mine (per-fixture, digests recorded): r88-m3 `acf677a7085b…`, r94 `048b8ff39e4a…`, r95 `97cffd7bfe6e…`, r96 `43911900923c…`, r97 `a28b9ea0d65e…`, r98 `5ecf84e19121…`, r99 `7fe7e3b06508…`, r100 `77debadf5c0f…` — all `exit=0 RESULT PASS`. First seven digests identical to my pre-round baseline run (no pin drift on existing pins — C1's "no other pin's fields change" corroborated from the behavior side). **REPRODUCED.**

**R6 — V22 baseline blob-anchor table.** V22 quoted four baseline blobs (`git rev-parse HEAD:<f>`): tool `ac590a83445a…`, contract `936a2082e134…`, README `309341ba810d…`, SKILL `27b9b6ff201c…`, "all four clean" at baseline. Mine now: HEAD blobs match all four quoted values exactly. Worktree delta: tool `CHANGED` (worktree `49c41c8d…`) and contract `CHANGED` (`3beb22ef…`) — exactly the two U1-owned files; README and SKILL still `CLEAN` vs HEAD, corroborating V02's gap #1 (README/SKILL freeze-row updates not landed while I verified). Anchors and the baseline-vs-now narrative both hold. **REPRODUCED** (anchors byte-confirmed; the two-file delta is the expected post-baseline change, not a mismatch of V22's claim).

## ABSENT items (reported, not verified)

- `corpus/knowledge/r101-r10-register-first-entry.md` (U2, C2): ABSENT through the full 40-try window and at 00:17:46. No seat could have verified it; none of the existing reports quote it. C2 is **unverifiable at audit time** — not judged PASS or FAIL from this seat.
- U1 producer report: ABSENT (U1's scratch dir `U1-chain-eight-scratch/` present; artifacts landed). V02's poll record matches mine.
- V13/V22 are IN-PROGRESS stubs; their final reports may supersede. R6 audits V22's already-quoted baseline table, which its stub presents as completed work.

## Incidental evidence (my own runs, not charged to any seat)

- Guarded `--freeze` scope guard live at baseline: `--freeze /tmp/not-a-fixture` → `FINDING SCOPE-REFUSED … frozen scope is corpus/fixtures/**`, exit 2.
- One verifier-side incident, disclosed: an exploratory `--freeze corpus/fixtures/r99-window-lapse` (intended as a guard test) actually rebuilt that pin — payload identical (same DIGEST `7fe7e3b0…`) but the writer refreshed top-level + per-pin `revision` to HEAD `ebec6bb…`, exactly the disclosed writer-managed refresh. I restored the contract from git (`git checkout --`, verified `revision b5fe4729…`, 7 pins, 18 cases) before producers landed; the delivered contract diff is U1's, not mine. Confirms the r100 disclosure that the refresh touches both revision fields.
- No repo byte modified by this seat apart from this report and `.scratch/v26/` (noted by V13's sweep as lane-root scratch — protocol-permitted, flagged non-standard; accepted).

## Bottom line

PASS — 6/6 quoted outputs REPRODUCED byte-for-byte (V02 ×5, V22 ×1); C2's artifact ABSENT at audit time (unverifiable here, not judged); U1 producer report ABSENT while its artifacts verify clean.
