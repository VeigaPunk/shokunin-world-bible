# V10 preservation-census — working evidence (round 102)

Seat: V10 preservation-census. Report path: `.ufo/waves/round-102/seats/V10-preservation.md`.
Scratch (declared): `.ufo/waves/round-102/seats/V10-scratch/`. Date: 2026-10-18.
Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Leaf seat: no nested agents, no commits, no pushes, no network.

## Commands and observed outputs (chronological)

1. Baseline census (06:19):
   - `ls corpus/fixtures | wc -l` → `176`
   - `git status --porcelain corpus/fixtures | wc -l` → `0`
   - Characterization: `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → `174`;
     `-type f` at top level → `2` (`corpus/fixtures/check_bible.py` 22880 B, `corpus/fixtures/README.md` 85211 B);
     `find corpus/fixtures -type f | wc -l` → `1050`; `git ls-files corpus/fixtures | wc -l` → `1050`.
   - ⇒ The census "174" counts fixture **directories**; the raw `ls` count of 176 = 174 dirs + the 2 top-level
     helper files. Matches LOG.md:3445 ("census 174/40/134/421") and LOG.md:3541 ("census 174 unchanged").
2. Baseline tree state:
   - `git log --oneline -1` → `8fa2e87 lore r102: declare capstone round before dispatch — final round of the loop`
     (r101 closure `542021a` is 2 commits back: 8fa2e87 → 60e88bf → 542021a).
   - `git diff --stat HEAD` → empty (exit 0) — zero tracked-file modifications pre-producer.
   - `git status --porcelain` → only `?? .scratch/`, `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`
     (later `?? .ufo/waves/round-102/` from seat activity).
   - `git rev-parse HEAD` → `8fa2e87b40b74f8f78864b7044ed0345712af605`.
3. corpus/knowledge inventory baseline (06:22): 22 files, no `r102*` (snapshot in `knowledge-inventory-baseline.txt`).
4. Poll windows (all checks: `ls .ufo/waves/round-102/seats/U1-*.md`, `U2-*.md`,
   `[ -f corpus/knowledge/r102-push-synthesis-r95-r102.md ]`, `r102-debt-ledger.json`, `r102-freshness-sweep.md`):
   - Window 1 (background, 20s cadence): try=1 06:19:50 … try=30 06:29:30 — all ABSENT
     (log: `poller1.log`; killed by the 600 s background-command cap, not by the 40-try budget).
   - Window 1b (foreground): try=31 06:30:18 … try=40 06:33:18 — all ABSENT. `POLL-40-EXHAUSTED`.
   - Full 40-try budget spent at 06:33:18 with producers + artifacts ABSENT.
   - At 06:33:57: `U1-scratch/` present (created 06:30, empty at 06:34) — producer demonstrably mid-work.
   - Window 2 (recorded stall-escape extension, 20s cadence, 14 tries): see report for outcome.
5. Final sweep at 06:33:57 (pre-extension):
   - `git log --oneline -1` → `8fa2e87` (HEAD unmoved).
   - `git status --porcelain` → only the three untracked-noise lines above + round-102 seats dir.
   - `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → `174`; `git ls-files corpus/fixtures | wc -l` → `1050`;
     `git status --porcelain corpus/fixtures | wc -l` → `0`.

## Census verdict logic

- Fixture census: expectation "174, no new fixture" — verified at baseline and re-verified at final sweep.
- Inherited changes: on every observed tree state, zero tracked-file changes existed, so there were no changes
  to classify — preservation vacuously holds on the observed state; the post-producer classification depends
  on whether producers land within the recorded windows.
