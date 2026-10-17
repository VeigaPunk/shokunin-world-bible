# V24 — scope-creep (round 97)

- Seat: V24 scope-creep. Baseline: the round-97 declaration names r96 closure `f3e09f9`; lane HEAD at wave start is **`2393934`** ("lore r96: close round — SCORECARD admitted section"), one commit *after* `f3e09f9` (`git log --oneline f3e09f9..HEAD` → `2393934` only). Recorded, not a finding. Scan window 2026-10-17 18:42–19:58 -0300.
- Mandate: after all seats, bucket every `git status --porcelain -uall` path — declared producer paths, seat reports/scratch, orchestrator declaration, anything else = finding; check no `__pycache__` under `corpus/`; confirm report-path exclusivity; check nothing at the parent repo root (stray-write class r94-F01). Report-only seat: no commits, no cleanup.
- Evidence (absolute, under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V24-scratch/`): `poll.sh`+`poll.log` (tree poll), `watch-artifacts.sh`+`artifacts.log` (first-seen), `analyze.py`+`snap/` (`buckets-`, `porcelain-`, `diff-`, `excl-`, `pycache-`, `parent-`, `elsewhere-md-`, `transients-` at labels `early` 18:46, `mid1` 19:11, `final` 19:45, `confirm2` 19:54:50).

## Protocol compliance

- Poll-wait task `bash-g96kh6fj` (`poll.sh`), 20 s cadence, 75 min cap, started 18:43:27; logged report counts, producer-artifact signature, seats signature, porcelain count every 20 s. Exit at cap 19:58:36: `CAP all=62 stable=0 elapsed=4500s`. The all-64 stability gate never fired because **V35 never landed** (and this seat's own report is written after the scan by design).
- First-seen watcher `bash-1fjm17w0` (`watch-artifacts.sh`), 20 s cadence, 18:46:18–19:56:30 (cap).
- Producer artifacts first observed 18:46:18; all six producer reports present by 18:59:48 (`R=6`); producer-artifact signature stable from 18:59:48 (`e4d3ebbb98e6`) through the last check 19:57:55.
- Verifier landing curve: 8/64 @18:48:47 → 35/64 @18:55:28 → 52/64 @19:00:08 → 59/64 @19:05:09 → 61/64 @19:19:51 → 62/64 @19:29:52; V35 absent at cap; V24 = this report (63rd).
- Rewrite-after-first-seen (watcher): V37-debt.md first seen 19:13:02 (25369 B) → final 19:14:06 (25389 B); V40-receipt.md first seen 19:29:05 (12835 B) → final 19:44:41 (13117 B); V58 first seen 19:16:42 → final 19:18:03. Same pattern r96 V27 observed.

## 1. Tracked modifications — `git diff --name-status` (19:54:50)

```
M	LOG.md
M	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

All seven are declared: LOG.md diff is exactly the 61-line `## Round 97 — declaration before dispatch` block (bucket B0, not creep); R1/R2/R3 tool files; R4's r96 cosmetic repair. Staged changes: none (`git diff --cached` empty). `git diff --stat`: 7 files, +653/−401. No other tracked file modified.

## 2. Bucketing — `git status --porcelain -uall` (final run 19:54:50, 10820 entries)

| Count | Bucket |
|---|---|
| 1 | B0 orchestrator declaration: `LOG.md` |
| 3 | B1a tools-modified: `corpus/tools/{map_obligations.py, map-obligations-contract.json, README.md}` |
| 2 | B1b R3 tool files: `corpus/tools/{dependency_freeze.py, dependency-freeze-contract.json}` |
| 1 | B1c r96 cosmetic repair: `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` |
| 10 | B1d r97 fixture: `corpus/fixtures/r97-crossing-acknowledgment/*` — the exact declared 10-file set (entities/relations/contradictions/inspiration-note/source-excerpt/sources/timeline + fictional-excerpts + README + claim-excerpt-map). `ls -la` shows no hidden/extra files; `diff <(ls r96-crossing-response/) <(ls r97-crossing-acknowledgment/)` → empty (file-name sets identical) |
| 1 | B1e knowledge note: `corpus/knowledge/r97-acknowledgment-scope-note.md` |
| 10801 | B2 seat reports/scratch under `.ufo/waves/round-97/seats/` (62 reports + `V37-debt.json` + 64 scratch dirs incl. this seat's snap evidence) |
| 1 | B2b wave-level: `.ufo/waves/round-97/receipt.json` (19:44:47, 17908 B, receipt seat — r96 precedent) |
| 0 | T transient (self-test temp dirs at repo root) |
| **0** | **OTHER — none** |

Churn checks: porcelain 10780 @19:11 → 10803 @19:20 → 10806 @19:30 → 10819 @19:49 → 10820 @19:54:50 → 10832 @19:55. Sorted path-set diffs of the two `porcelain-*.txt` snapshots taken 19:45:00 and 19:50:07 show the only added paths are this seat's own `V24-scratch/snap/*-final.txt` files (12 paths); every path since 19:52 is likewise this seat's own snap writes (`find -newermt 19:52` → only V24 files + poll.log). OTHER=0 held at all four scans (early/mid1/final/confirm2).

## 3. `__pycache__` under `corpus/` (reported, not cleaned)

- Only dir under `corpus/`: `corpus/tools/__pycache__/` (pre-existing; gitignored via `.gitignore` line 2 `__pycache__/`; never appears in porcelain).
- 18:44:19: 4 `.pyc` — `boundary_doc_check` (14:04, 52190 B), `support_check` (15:41, 24721 B), `map_obligations` (18:43:14, 57727 B), `dependency_freeze` (18:44:19, 34636 B).
- Final (19:54:50): 3 `.pyc` — `dependency_freeze.cpython-314.pyc` is **gone** (dir mtime 18:57); `map_obligations.cpython-314.pyc` recompiled 18:49:38 (58629 B); `boundary_doc_check`/`support_check` unchanged.
- No new `__pycache__` dir under `corpus/`; no `.pyc` outside `corpus/tools/__pycache__/` (full `find corpus`).
- Ignored sweep (`git status --porcelain --ignored -uall`): under `corpus/` only the 3 above; under round-97 only `V05-scratch/baseline/__pycache__/map_obligations.cpython-314.pyc` (B2 scratch); legacy r95/r96 scratch `.pyc` unchanged.
- Classification: hygiene observation from declared tool runs plus one `.pyc` removal (~18:57) by an unidentified seat; ignored, inside a pre-existing dir, nothing tracked. Flagged for the adjudicator; not cleaned per report-only mandate.

## 4. Report-path exclusivity

- `seats/` at 19:54:50: 63 top-level files = 62 `*.md` reports + `V37-debt.json`; 64 scratch dirs (63 `*-scratch` + `scratch-R1`).
- Pattern check: all reports match `^(R[1-6]|V\d{2})-.*\.md$` — `pattern_mismatch: (none)`. Content spot-check (seat id in first 30 lines): `header_seat_mismatch: (none)`. Cross-scratch scan (report-pattern `.md` inside a scratch dir with a mismatched owner prefix): `cross_scratch_mismatch: (none)`.
- One noted pattern: multi-file prefix `V37` (`V37-debt.md` + `V37-debt.json` sidecar) — same shape as r96 `V40-debt.json`/`V31-debt.json`; not a cross-write. No other seat has more than one file besides its own scratch dir.
- `R1`'s scratch dir is `scratch-R1` (nonstandard order; still seat-owned, no other content).
- Report-like `.md` elsewhere in the lane repo (mtime ≥ 18:41, outside `seats/`): only declared corpus paths — r96 repair map, r97 fixture `*.md`, knowledge note, `corpus/tools/README.md`. No stray report.
- Missing at scan: **V35** (its scratch holds `report-final-draft.md` mtime 19:35; no report by the 19:58:36 cap) and V24 (this report, by design).
- Method limitation: byte authorship is not observable from the tree; exclusivity is checked by path/name/content structure, not by attributing each byte to a seat.

## 5. Parent-tree stray check (r94-F01 class)

- Parent `git status --porcelain -uall`: 0 lines at 18:42:47, 19:11, 19:54:50 scans; parent `git diff` clean.
- `find` for lore-signature files outside `lore-shokunin/` (crossing-acknowledgment/crossing-response, `claim-excerpt-map.md`, `map_obligations.py`, `dependency_freeze.py`, both contracts, `boundary_doc_check.py`, `support_check.py`): none.
- No `round-97` under the parent `.ufo/waves/` (parent waves are `shokunin-train-*`); parent ignored list carries only `!! lore-shokunin/` (the lane repo itself).
- Parent root new file during the window: `MANIFEST.json` (18:58:06, 211015 B) — attributed to kotodama's round-10 closure commit `b0bb880` in the parent repo (`git log -1 -- MANIFEST.json` → `b0bb880 18:58:06 close kotodama round-10`), not a lore-r97 write. No lore seat artifact at the parent root.

## 6. Transients / ignored sweep

- One live `map-obligations-self-test-h5wymz0d/` tree (73 files) at the lane repo root caught mid-run at the 18:46 early scan — a self-cleaning temp dir from a declared `map_obligations --self-test` run; absent at the 19:11, 19:45 and 19:54:50 scans (`transients-*.txt` empty).
- `dependency-freeze-*`, `support-check-*`, `boundary-doc-check-*` transients: none observed at any scan.
- Visibility caveat: self-cleaning dirs are only observable if a scan coincides with them.

## Caveats

- Boundary: final bucket scan 19:54:50; the poll's all-64 stability gate never fired (V35 absent). V35's activity observed was confined to its own `V35-scratch/` (B2); a late V35 report would also be B2, so it cannot change the OTHER=0 result for the declared/producer buckets.
- This report itself and the `confirm2` snap files are the only post-scan additions, all inside V24's declared report/scratch paths; a post-write scan at 20:01:39 (`snap/*-post.txt`) re-ran the full bucketing with 63 reports present and still returned OTHER=0 (only additions since `confirm2`: this report + V24 snap files).
- Baseline note: HEAD `2393934` vs declared `f3e09f9` (one commit; `f3e09f9` is its ancestor) — recorded for the adjudicator.

Bottom line: PASS — every persistent working-tree path at the 19:54:50 scan falls inside a declared bucket (producer paths / seat reports+scratch / LOG.md / wave receipt); OTHER=0 across four scans with all churn confined to `.ufo/waves/round-97/`; report-path exclusivity clean (one V37 `.md`+`.json` sidecar pair, r96-precedent shape); no new `__pycache__` dir under `corpus/` (one gitignored `.pyc` removed mid-wave, reported not cleaned); no lore-r97 strays in the parent tree (parent-root `MANIFEST.json` is kotodama's `b0bb880`); V35 report absent at the 19:58:36 poll cap (scratch-only activity, inside its own B2 paths).
