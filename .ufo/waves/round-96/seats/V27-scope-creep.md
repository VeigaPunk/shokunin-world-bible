# V27 — scope-creep (round 96)

- Seat: V27 scope-creep. Baseline: r95 closure `dcb2d92` (lane HEAD at wave start `60dba0c`, the r95 SCORECARD close commit). Scan window 2026-10-17 17:37–17:59 -0300.
- Mandate: after all seats, bucket every `git status --porcelain -uall` path — declared producer paths, seat reports/scratch, anything else = finding; check no `__pycache__` under `corpus/`; confirm report-path exclusivity. Report-only seat: no commits, no cleanup. Evidence in `seats/V27-scratch/` (`poll.log`, `snap/porcelain{,-2,-3,-4}.txt`, `snap/bucket-final*.txt`, `snap/excl-final*.txt`, `snap/artifacts-{1,2}.txt`).

## Protocol compliance

- Poll-wait task `bash-x361lfvq` (script `seats/V27-scratch/poll.sh`, log `seats/V27-scratch/poll.log`), 20 s cadence, 46 tries, 17:40:27–17:55:28.
- Producer artifacts first seen: fixture `timeline.json` try 1 (17:40:27); `corpus/tools/dependency_freeze.py` try 7 (17:42:27); `dependency-freeze-contract.json` try 8 (17:42:47); `corpus/knowledge/r96-response-scope-note.md` try 14 (17:44:47).
- Producer reports: first observed try 6 (17:42:07); all six present try 37 (17:52:28) → `producers_done=1`. Q report final mtimes: Q5 17:45:37, Q6 17:47:16, Q4 17:47:19, Q3 17:47:26, Q2 17:52:12, Q1 17:52:17. Q4 was rewritten after first appearance (first seen 17:42:07, final mtime 17:47:19) — same rewrite-after-first-seen pattern r95 V18 observed.
- Poll exit: cap try 46 (17:55:28) with `stable=0` — tree-wide signature stability never accumulated because verifier reports kept landing in bucket B3 (r95 V18 saw the same). Producer-artifact stability verified separately: `find corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response corpus/knowledge/r96-response-scope-note.md -printf '%T@ %s %p\n' | sort` snapshotted twice 75 s apart (17:54:32 / 17:55:47) → byte-identical → `PRODUCER ARTIFACTS STABLE across 75s`.
- Final scans: porcelain at 17:54:32 (18011 entries), 17:56:07 (18139), 17:57:27 (18145), 17:58:2x (19162, final bucket run).

## 1. Tracked modifications — `git diff --name-status` (17:54:32)

```
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

Staged changes: none (`git diff --cached --name-status` empty). `git diff --stat`: 4 files, +234/−24 (LOG.md +67, tools/README.md +50, contract +2, tool +139/−24). No other tracked file modified. LOG.md content = exactly the `## Round 96 — declaration before dispatch` block (67 insertions, the text my brief quotes) → bucket B4, not creep.

## 2. Bucketing — `git status --porcelain -uall` (final run 17:58:2x, 19162 entries)

| Count | Bucket |
|---|---|
| 3 | B1 declared-producer-modified: `corpus/tools/{map_obligations.py, map-obligations-contract.json, README.md}` |
| 10 | B2a fixture-new `corpus/fixtures/r96-crossing-response/*` — exact declared 10-file set (Q4: entities/relations/contradictions/inspiration-note/source-excerpt + sources/timeline + fictional-excerpts; Q5: README + claim-excerpt-map). `ls -la` shows no hidden/extra files; `diff <(ls r95-crossing-aftermath/) <(ls r96-crossing-response/)` → empty (file-name set identical) |
| 2 | B2b tools-new: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json` |
| 1 | B2c knowledge-note-new: `corpus/knowledge/r96-response-scope-note.md` |
| 19145 | B3 seat reports/scratch under `.ufo/waves/round-96/` (60 `*.md` report files + `V40-debt.json` at 17:59; 55 scratch dirs incl. `V27-scratch/snap` evidence) |
| 1 | B4 orchestrator declaration `LOG.md` |
| **0** | **OTHER — none** |

Churn checks (sorted path-set diffs `comm`): 17:54:32→17:56:07 `added=128 removed=0`; →17:57:27 `+6/0`; →17:58:2x `+1017/0`. Every added/removed path filtered with `grep -v "^\.ufo/waves/round-96/"` returned nothing (three times). The +1017 jump is V38's scratch copy tree (`V38-scratch/sub/…`), late verifier reports (V30, V36), V40's sidecar, and my own snap files — all B3.

## 3. `__pycache__` under corpus/ (reported, not cleaned)

- Only dir under `corpus/`: `corpus/tools/__pycache__/` (pre-existing; gitignored via `.gitignore` line 2 `__pycache__/`; never appears in porcelain).
- Pre-round baseline: `boundary_doc_check` 14:04/52190 B; `support_check` 15:41/24721 B; `map_obligations` 16:26/52223 B.
- Final (17:54:32): `boundary_doc_check` 14:04/52190 unchanged; `support_check` 15:41/24721 unchanged; **new** `dependency_freeze.cpython-314.pyc` 17:44/34646 B; `map_obligations.cpython-314.pyc` recompiled 17:45/57585 B.
- No new `__pycache__` dir and no `.pyc` outside `corpus/tools/__pycache__/` (full `find corpus`). Ignored-sweep (`git status --porcelain --ignored -uall`) lists only these 4 under `corpus/`.
- Classification: hygiene observation caused by declared tool runs — not scope creep (ignored, inside a pre-existing dir, nothing tracked); flagged for the adjudicator; not cleaned per report-only mandate.

## 4. Report-path exclusivity

- `seats/` at 17:59: 60 `*.md` reports (6 Q + 54 V) plus `V40-debt.json`. Roster V01–V58 still missing at scan: V27 (this report), V38, V43, V58 (in flight; r95 saw equivalent late landings). Late landings inside the window: V30, V36, V40-debt.json.
- Checks (17:58 run): `unmatched names: (none)`; content spot-check (filename seat-id appears in first 30 lines): `(none)` mismatched; report-like files elsewhere in the lane repo (mtime ≥ 17:37, outside `seats/`): `hits: (none)`; cross-scratch scan (report-pattern `.md` inside a scratch dir whose owner prefix mismatches): none.
- One noted pattern: `duplicate seat-id prefixes: {'V40': ['V40-debt.json', 'V40-debt.md']}` — a `.md` report plus a `.json` sidecar under V40's own prefix, same as r95 `V31-debt.json`. Not a cross-write.
- Method limitation: byte authorship is not observable from the tree; exclusivity is checked by path/name/content structure, not by attributing each byte to a seat.

## 5. Parent-tree stray check (r95 defect class: reports mislanded in the parent tree)

- Baseline 17:38: parent `git status --porcelain -uall` → 1 line ` M .ufo/l0-questions.md`.
- Final 17:56: 2 lines — `?? mtk-zeichentragende.pdf` (243 B, 17:49:24) and `?? reports/round-9/metadata/v09-myth.md` (12251 B, 17:51:57). Both are **kotodama lane round-9 artifacts**, not lore-r96: kotodama-shokunin is running round 9 concurrently (`kotodama-shokunin/reports/round-9/` mtime 17:54, `.scratch-r9f04c/` active), and `v09-myth.md` content is kotodama's round-9 V09 metadata re-audit of `corpus/knowledge/myth-symbol/`.
- The baseline ` M .ufo/l0-questions.md` disappeared because kotodama's closure commit `b372a53` (2026-10-17 17:45:00, "close kotodama round-8") included `.ufo/l0-questions.md` (+2). The lore lane made no commit (`HEAD` still `60dba0c`).
- No `.ufo/waves/round-96/` exists under the parent; `find` for lore seat-report patterns (newer than 17:37, excluding `lore-shokunin`) → none.

## 6. Transients / ignored sweep

- Repo-root transients (`map-obligations-self-test-*`, `dependency-freeze-*`): none at the 17:54:32 / 17:55:47 / 17:57:00 scans. Visibility caveat: self-cleaning dirs are only observable if a scan coincides with them.
- `git status --porcelain --ignored -uall`: 23 `!!` entries — 3 `.ufo/interactive-sessions/` (pre-existing), 3 r95 scratch `.pyc` (legacy), 5 round-96 scratch `.pyc` (B3: V18/V07/V09/V25 scratch), 8 `V38-scratch/lb{,2}/…` copies (B3), 4 `corpus/tools/__pycache__` `.pyc` (§3). Nothing ignored outside allowed areas except the §3 item.
- Outside-repo check: two `/tmp` entries carry a `v27` prefix (`/tmp/v27_selftest_before.txt`, `/tmp/v27-br02/`) but are r95-window artifacts (mtime 16:17–16:33, pre-dating this wave); no r96-window `/tmp` strays from this seat (own writes failed and left nothing).

## Caveats

- Boundary: final bucket scan 17:58:2x; verifier seats were still landing (V38, V43, V58 absent then; V30/V36 landed during the window). All observed churn stayed inside B3, so later landings cannot change the OTHER=0 result for the declared/producer buckets.
- Transient environment condition: a churn-diff temp write to `/tmp` failed `No space left on device` (~17:56); rerun inside `V27-scratch/snap/` succeeded; `df -h /tmp` immediately after showed 8.5 G free — momentary, not a repo finding.

Bottom line: PASS — every persistent working-tree path at the 17:58:2x scan falls inside a declared bucket (producer paths / seat reports+scratch / orchestrator LOG.md); OTHER=0 across four scans with all churn confined to `.ufo/waves/round-96/`; report-path exclusivity clean (one V40 `.md`+`.json` sidecar pair noted, same as r95 V31); no lore-r96 strays in the parent tree (two new parent `??` files are kotodama r9's); one hygiene item reported not cleaned: `corpus/tools/__pycache__/` gained `dependency_freeze.cpython-314.pyc` and a recompiled `map_obligations.cpython-314.pyc` (gitignored, pre-existing dir).
