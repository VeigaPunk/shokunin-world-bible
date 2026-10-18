# V23 — scope-creep (round 99)

Seat: V23-scope-creep. Model: xai-oauth/grok-4.7-fast (re-dispatch; the blocked attempt wrote no reports).
Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Parent repo: `/home/vgpnk/Projects/shokunin`.
Baseline named in the brief: r98 closure `4265df5`. Observed HEAD at every scan: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`lore r99: record blocked dispatch attempt — zero increment`, 2026-10-17 21:53:33 -0300). `git log --oneline 4265df5..HEAD`:

```
337f0fa lore r99: record blocked dispatch attempt (xai-oauth credential pool missing) — zero increment
111b9a3 lore r98: close round — SCORECARD admitted section
```

`4265df5` is an ancestor of HEAD. Recorded, not a finding. No commits, no pushes, no deletes, no network from this seat. Writes: this report and `.ufo/waves/round-99/seats/V23-scratch/` only.

Check axes: lane porcelain buckets; report-path exclusivity; `__pycache__` committable; parent-tree strays; oversized scratch mirror (flag, do not delete).

## Poll-wait

Cadence 20s, max 40 tries. Ready gate: 16 producer artifact paths present AND `seats/S*.md` count >= 5. Log: `.ufo/waves/round-99/seats/V23-scratch/poll.log`.

```
try=1 ts=2026-10-17T22:01:10-03:00 arts=14/16 srep=0 allrep=0 porcelain=33
try=15 ts=2026-10-17T22:05:51-03:00 arts=14/16 srep=2 allrep=6 porcelain=50290
try=16 ts=2026-10-17T22:13:13-03:00 arts=14/16 srep=2 allrep=11 porcelain=51684
try=40 ts=2026-10-17T22:21:16-03:00 arts=14/16 srep=2 allrep=14 porcelain=52116
CAP arts/srep not ready
```

The gap between try 15 and try 16 is this seat's first poll process hitting its 300s tool timeout; `poll2.sh` continued the same log from try 16. Try count still exhausted at 40. Missing at cap: `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and producer reports S1/S2/S5 (S3 and S4 had landed). ENDGAME stall-escape: recorded, not treated as a claim verification. This seat does not verify C1 or C2; it buckets the tree that exists.

Post-cap confirm scan (tree still moving after the cap): 2026-10-17T22:49:42-03:00. Knowledge notes still absent. Producer reports present: `S1-full-file-pins.md` (22:48, after the cap), `S3-fixture-author.md`, `S4-fixture-docs.md`. Still absent: `S2-*.md`, `S5-*.md`.

## Lane buckets — 22:49:42

Command: `git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain -uall`, then path-bucketed in Python (declared exact: the four S1/S2 paths + the two r99 knowledge paths + `LOG.md`; prefixes: `.ufo/waves/round-99/seats/`, `corpus/fixtures/r99-window-lapse/`).

```
porcelain_lines 67704
diff --name-status:
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py
cached: (empty)
counts {'M_or_other_tracked': 2, 'fixture': 10, 'knowledge': 0, 'log': 0, 'reports': 81, 'scratch': 67609, 'wave_other': 1, 'other': 1}
OTHER_PATHS:
?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
?? .ufo/waves/round-99/receipt.json
```

`git diff --stat` at 22:50:55 (still only those two paths):

```
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  67 ++++++++++-
 2 files changed, 207 insertions(+), 23 deletions(-)
```

| Bucket | Paths | Count at 22:49:42 | Verdict |
|---|---|---|---|
| S1 declared | `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json` | 2 (M) | DECLARED |
| S2 declared | `corpus/tools/README.md`, `SKILL.md` | 0 dirty at 22:49:42; both M by 22:56:15 | DECLARED (see confirm) |
| S3/S4 fixture | `corpus/fixtures/r99-window-lapse/` exact 10-file set | 10 (??) | DECLARED |
| S5 knowledge | `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md` | absent at 22:49:42; both ?? by 22:57:50 | DECLARED once present (see confirm) |
| Orchestrator | `LOG.md` | clean (mtime 21:53:33, matches HEAD) | not dirty |
| Seat reports | `.ufo/waves/round-99/seats/*.md` | 81 | DECLARED |
| Seat scratch | `.ufo/waves/round-99/seats/*-scratch/**` and other files under `seats/` | 67609 | DECLARED scratch |
| Wave receipt | `.ufo/waves/round-99/receipt.json` | 1 | classified receipt, not creep (below) |
| Other | `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md` | 1 | FINDING |

Fixture listing (`ls -1a corpus/fixtures/r99-window-lapse`) is exactly `.`, `..`, and the ten declared names (`README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`). No extra file.

S2 paths were not edited by 22:50:55. `stat`:

```
2026-10-17 21:32:05 32577 corpus/tools/README.md
2026-10-17 21:34:23 16802 SKILL.md
```

Both mtimes predate the wave directory (created 22:00). Absence of an S2 edit is not a stray write.

## Findings

### F1 — parent-tree strays (zero-strays criterion fails)

`git -C /home/vgpnk/Projects/shokunin status --porcelain -uall` at 22:49:42 and again at 22:50:55 (8 lines, parent `git diff --name-status` empty). These paths are not gitignored (`git check-ignore` on the V69 py path returned `NOT ignored`).

```
?? .ufo/waves/round-99/seats/V69-scratch/before/baseline-root/corpus/tools/dependency-freeze-contract.json
?? .ufo/waves/round-99/seats/V69-scratch/before/baseline-root/corpus/tools/dependency_freeze.py
?? .ufo/waves/round-99/seats/V73-scratch/selftests/boundary.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/boundary.out
?? .ufo/waves/round-99/seats/V73-scratch/selftests/freeze.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/freeze.out
?? .ufo/waves/round-99/seats/V73-scratch/selftests/map.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/map.out
```

Absolute root: `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` (fleet parent), not `lore-shokunin/.ufo/waves/round-99/`. `du -sh` of that tree: 12K. File sizes:

```
0  2026-10-17 22:11:27  .../V69-scratch/before/baseline-root/corpus/tools/dependency_freeze.py
0  2026-10-17 22:11:27  .../V69-scratch/before/baseline-root/corpus/tools/dependency-freeze-contract.json
0  2026-10-17 22:17:58  .../V73-scratch/selftests/boundary.out
129 .../V73-scratch/selftests/boundary.err
0  .../V73-scratch/selftests/map.out
126 .../V73-scratch/selftests/map.err
0  .../V73-scratch/selftests/freeze.out
128 .../V73-scratch/selftests/freeze.err
```

V73 stderr (wrong cwd = parent, where no `corpus/tools/` exists):

```
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/boundary_doc_check.py': [Errno 2] No such file or directory
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/map_obligations.py': [Errno 2] No such file or directory
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/dependency_freeze.py': [Errno 2] No such file or directory
```

Same class as r98's parent stray (`baseline-analyze.txt`): a seat ran with cwd = the fleet root and a relative `.ufo/waves/round-99/seats/...` redirect landed in the parent repo. V69's lane scratch (`lore-shokunin/.ufo/waves/round-99/seats/V69-scratch/before/baseline-root/`) holds real fixture copies; the parent copies are 0-byte tool files. Attribution: V69 and V73. Not deleted.

Sibling hunt (`find /home/vgpnk/Projects/shokunin -maxdepth 4` for `round-99`, `r99-window-lapse`, the two knowledge names, excluding `lore-shokunin`): the only this-wave hit is the parent `.ufo/waves/round-99` above. `audio-shokunin/reports/round-99`, `game-dev-2d-shokunin/reports/round-99`, and `game-dev-3d-shokunin/reports/round-99` are dated 2026-10-16, not this wave. Kotodama `.scratch` files touched after 21:55 are that lane's own work, not lore paths.

### F2 — lane undeclared untracked path (resumed r98 seat, not an r99 producer)

```
$ stat -c '%y %s %n' .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
2026-10-17 22:32:40.247271032 -0300 4208 .../original-run-resume-note.md
```

Created during this r99 wave, outside every declared r99 path. Header of the file: "V58 (original run, agent-294) — resumed-run record"; it says the original r98 V58 resumed at ~22:29 after r98 had already been closed, refused to overwrite the pinned `V58-presence-final.md`, and wrote this note instead. It is a real extra porcelain path. It is not an r99 seat writing into another seat's report. Not deleted.

### F3 — V40 scratch mirror, flagged for L1, not deleted

```
$ du -sh .ufo/waves/round-99/seats/V40-scratch/archive
307M
$ find .ufo/waves/round-99/seats/V40-scratch/archive -type f | wc -l
44799
$ find .ufo/waves/round-99/seats/V40-scratch -name .git | wc -l
0
```

`ls -la` of `archive/` at 22:03 showed a plain lane copy: `corpus`, `reports`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, `l0-questions.md`, `PROVINCE.md`, `README.md`, `.gitignore`, `.ufo`. No nested `.git` (not a gitlink). Same class as r98's 243M V37 mirror. Flagged for L1 removal. Not deleted.

Smaller `archive/` copies, not the 300MB class, noted so L1 can see them: `V93-scratch/archive` 8.6M (corpus + LOG.md + SCORECARD + SKILL), `V20-scratch/archive` 7.8M (corpus + SKILL), `V70-scratch/archive` 4.3M (corpus). This seat's own `V23-scratch/snap/` is porcelain dumps plus one failed-filter evidence file, not a repo mirror.

### Not findings

- `receipt.json` (50183 bytes, mtime 22:37:23, `record_type` `round-99-receipt`, `baseline_commit` `4265df5…`, `head_at_snapshot` `337f0fa…`). Wave-root receipt, r97/r98 precedent, and `V39-receipt.md` is present. Classified as the receipt artifact, not creep. The standing declaration names seat reports, not this path; called out so L1 can reclassify if it wants a stricter reading.
- `__pycache__`: `git status --porcelain -uall | grep -c '__pycache__'` = 0 at 22:49:42. `git check-ignore -v corpus/tools/__pycache__/dependency_freeze.cpython-314.pyc` → `.gitignore:2:__pycache__/`. The `dependency_freeze` pyc was recompiled during the wave (mtime 22:36:25, later than the 20:31 r98 pyc) and remains ignored, so not committable. `v05-self-test-scratch` matches `.gitignore:4:*-self-test-*/`. No self-test path appears in porcelain OTHER.
- Report-path exclusivity inside `seats/`: 81 `*.md`, zero non-md top-level files, zero non-`*-scratch` directories, zero names failing `^(S[1-5]|V\d+)-.+\.md$`. No r99 report written under `corpus/` or the lane root.
- Staged index empty (`git diff --cached --name-status` empty).

## Confirm scan after this report was written

The 22:49:42 / 22:50:55 numbers above are the poll-cap scan. A later pass, because seats were still landing, does not change F1–F3.

At 22:56:15 `git diff --name-status` gained the two S2 paths (declared, not creep). `git diff --stat` then:

```
 SKILL.md                                     |   6 +-
 corpus/tools/README.md                       |  63 +++++++++++
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  67 ++++++++++-
 4 files changed, 273 insertions(+), 26 deletions(-)
```

`stat` mtime on both S2 files: 2026-10-17 22:51:39. No `S2-*.md` yet.

At 22:57:50 both S5 files appeared, and at 23:01:33 they were the only new knowledge names:

```
2026-10-17 22:57:50 20526 corpus/knowledge/r99-gate-blind-spot-table.md
2026-10-17 22:57:50 14990 corpus/knowledge/r99-lapse-scope-note.md
?? corpus/knowledge/r99-gate-blind-spot-table.md
?? corpus/knowledge/r99-lapse-scope-note.md
```

No extra file under `corpus/knowledge/` matching `r99`. `S5-*.md` still absent. Parent porcelain at 23:01:33 was still the same 8 lines as F1.

Rebucket at 23:05:44 (`git status --porcelain -uall`, same classifier): porcelain 78240; tracked 4 (the S1+S2 paths only); fixture 10; knowledge 2; reports 100; scratch 78122; wave_other 1 (`receipt.json`); other 1 (the r98 V58 note). Producer reports still only `S1-full-file-pins.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`. This report is one of the 100. No new outside path.

## Verdicts

- Lane bucket completeness: **FAIL** on one undeclared untracked path (F2). Every other lane path at 23:05:44 is a declared producer path, the exact r99 fixture, the two declared knowledge notes, seat reports, seat scratch, or the wave receipt.
- Report-path exclusivity (r99 seats): **PASS**.
- `__pycache__` committable: **PASS** (present under `corpus/tools/__pycache__`, gitignored, absent from porcelain at 22:49:42).
- Parent-tree strays: **FAIL** (F1, 8 files, V69 + V73; unchanged at 23:01:33).
- Oversized mirror: **FLAGGED** (F3, V40 307M / 44799 files, no `.git`). Not deleted.
- Producer reports: S2 and S5 reports still **ABSENT** at 23:05:44. Poll cap at try 40 (22:21:16) with arts 14/16 and srep 2/5. Stall-escape recorded. This seat did not verify C1 or C2.

Bottom line: FAIL — eight parent-tree strays under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` (V69 empty tool copies + V73 wrong-cwd selftest redirects) and one lane undeclared path (resumed r98 V58 `original-run-resume-note.md`); V40's 307MB archive mirror is flagged for L1 and was not deleted; S2 bytes and both knowledge notes landed on declared paths by 23:05:44, but S2 and S5 reports were still absent.
