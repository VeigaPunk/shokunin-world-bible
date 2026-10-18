# V14 adjacency-final — working baseline (to be folded into V14-adjacency.md)

Baseline r101 closure `542021a`; observed live HEAD `8fa2e87b40b74f8f78864b7044ed0345712af605`
(r102 declaration commit). Diff `542021a..8fa2e87` = LOG.md (+44) + SCORECARD.md (+33) only;
corpus/ byte-identical to r101 closure.

## Province preservation (verified at baseline, re-run at close)

- `git show 542021a:PROVINCE.md | sha256sum` → 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
- `git show 8fa2e87:PROVINCE.md | sha256sum` → 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
- work-tree `sha256sum PROVINCE.md` → same digest. Same value r101 V17 recorded (continuity).
- audit.py (V14-scratch): PROVINCE_IDENT_BASE_WORK True / HEAD_WORK True.

## Write confinement at baseline

- TRACKED_CHANGES [] (pre-delivery).
- Untracked at baseline: V-scratch dirs under .ufo/waves/round-102/seats/ (V06, V09, V10, V13, V14, V18, V19…), lane-root `.scratch/` (V02 + v26 variants; mtimes 00:04:55 / 00:16:42 = r101 carryover, recorded by r101 V17 mechanics note 2), pre-existing r98 stray `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`.
- Knowledge inventory baseline: 22 files, sha256 list captured (V14-scratch).

## Mechanics observations (pre-delivery)

1. Roster-sum erratum (evidence, not adjudication): brief says "roster U1–U2 + V01–V19" (21 labels for a 20-seat round); LOG r102 declaration says "U1–U2, V01–V18". V19-scratch exists → V19 dispatched. Same append-only erratum class as r100/r101. V13-doc.md records the same observation independently.
2. Mtime-only touches: corpus/knowledge/r101-r10-register-first-entry.md + r99-gate-blind-spot-table.md (06:10:06) and r91-c9-watch.md (06:10:59) — before first r102 seat activity (06:22); bytes identical to HEAD (tracked-clean); no content write. Likely operator pre-round git op.
3. Outside-lane mtime scan (find . -maxdepth 2 -newermt '2026-10-18 06:15' excluding lore-shokunin): only sibling lanes' .git dirs + root MANIFEST.json (mtime 06:15:04 = r101 fleet-close commit 97ac852; root status clean). Parallel-lane/operator bookkeeping; no lore-wave write outside the lane.

## Cross-pins for the rights/mechanics scan

- checker pin: sha256sum corpus/fixtures/check_bible.py → ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
- r91-c9-watch.md: 369 lines; r101 row ends "Next re-check: r102"; gate 3 not met.
- corpus/README.md: 44 lines; nav section dated (2026-10-17).

## Poll log (protocol 20s x 40)

- Poll 1 (tries 1–~30): background task killed by 600s runner timeout before the 40-try cap; no artifacts, no U reports at kill. Recorded (runner mechanics, not protocol deviation).
- escape1-probe try=31 (06:28:42): knowledge=0/3 Ureports=0/2. V reports landing: V11-gates.md, V13-doc.md (producer-independent scopes).
- STALL-ESCAPE-1 (bounded 40 tries, launched 06:28:45): RUNNING — result to record.
