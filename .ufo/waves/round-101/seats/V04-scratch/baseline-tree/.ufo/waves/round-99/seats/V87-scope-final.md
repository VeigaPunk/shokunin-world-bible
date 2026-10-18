# V87 — scope-final (round 99)

Seat: V87-scope-final. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Named baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at every check: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa lore r99: record blocked dispatch attempt (xai-oauth credential pool missing) — zero increment`).

This is a cap-time snapshot, not a closed-wave confirmation. The producer gate never opened. C1/C2 were not scored.

## Poll-wait

Cadence 20s, max 40 tries. Gate (all required): `S1*.md`…`S5*.md` present; ten `corpus/fixtures/r99-window-lapse/` files non-empty; both S5 knowledge notes non-empty; `dependency_freeze.py` or the contract dirty vs HEAD.

Tries 1–15 ran `2026-10-17T22:03:40-03:00` → `22:08:20-03:00`, then the host killed that waiter at its 300s cap (pid 1700910, exit -1). Bounded stall, recorded, not fatal: continuation tries 16–40 started `22:14:43-03:00` and finished `22:22:43-03:00` with `ABSENT` (script exit 2). Log: `.ufo/waves/round-99/seats/V87-scratch/poll.log`.

Try 40 line:

```
try=40 t=2026-10-17T22:22:43-03:00 reports=16 s_reports=2 fixture_files=10 kb_table=0 kb_note=0 tools=[ corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---  corpus/tools/dependency_freeze.py            |  65 ++++++++++-  2 files changed, 206 insertions(+), 22 deletions(-) ]
ABSENT try=40 t=2026-10-17T22:22:43-03:00
```

Absent at the cap, and still absent at the write-time recheck `2026-10-17T22:45:16-03:00`:

- Producer reports present: `S3-fixture-author.md`, `S4-fixture-docs.md` only. No `S1*.md`, `S2*.md`, `S5*.md`.
- `corpus/knowledge/r99-gate-blind-spot-table.md` — No such file.
- `corpus/knowledge/r99-lapse-scope-note.md` — No such file.
- `git diff --quiet -- SKILL.md corpus/tools/README.md` exit 0 (S2 freeze-row and tools README not landed). HEAD freeze row still says 17 cases and "the pin payload covers the JSON tables only" (`SKILL.md` lines 98–100).
- S5 scratch existed by 22:40 (`S5-scratch/replay.py`, `S5-scratch/work/m*`) but that is scratch, not the declared knowledge paths. Not treated as delivery.

Endgame (subtract SELF): other seat reports were 16 at try 40, 20 at the 22:27 audit, 71 at 22:45:16. Expected others = 127. Stall recorded, not fatal. No all-reports confirmation was attempted.

## Declared set (LOG.md r99 declaration, standing)

Tracked, owned: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json` (S1); `corpus/tools/README.md`, `SKILL.md` freeze row only (S2).

New, owned: `corpus/fixtures/r99-window-lapse/` ten files (S3 JSON + excerpts, S4 README + map); `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md` (S5).

Else read-only, except seat artifacts under `.ufo/waves/round-99/seats/`.

HEAD is two commits ahead of `4265df5`. Those commits are pre-wave, not this wave's dirt:

```
337f0fa lore r99: record blocked dispatch attempt … — zero increment
111b9a3 lore r98: close round — SCORECARD admitted section
```

`git diff --stat 4265df5 -- . ':(exclude).ufo'` therefore also shows `LOG.md` (+91) and `SCORECARD.md` (+32). Neither is dirty vs HEAD.

## Cap-adjacent bucket (audit 2026-10-17T22:27:08-03:00)

Commands from the lane root. Raw log: `seats/V87-scratch/audit-raw.txt`. Full `??` list of that instant: `seats/V87-scratch/untracked-paths.txt` (52717 lines).

```
$ git status --porcelain=v1 -uall | wc -l
52718
$ git status --porcelain=v1 -uall | awk '{print substr($0,1,2)}' | sort | uniq -c
  52716 ??
      2  M
$ git status --porcelain=v1 -uall | grep -v '^?? '
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
$ git diff --stat
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  65 ++++++++++-
 2 files changed, 206 insertions(+), 22 deletions(-)
$ git diff --numstat
146	17	corpus/tools/dependency-freeze-contract.json
60	5	corpus/tools/dependency_freeze.py
```

The second `git status` (listing written to `untracked-paths.txt`) counted 52717 `??` lines — one more than the first count. In-flight race, not an unclassified path. Classifier on that listing:

| Bucket | Count | Verdict at 22:27 |
|---|---|---|
| Tracked S1 (`dependency_freeze.py`, contract) | 2 M | in declared set; S1 report absent |
| `corpus/fixtures/r99-window-lapse/` (exactly the ten; no extras) | 10 ?? | in declared set (S3/S4 reports present) |
| Declared S5 knowledge notes | 0 | ABSENT |
| `SKILL.md`, `corpus/tools/README.md` | clean vs HEAD | ABSENT (S2 edit not landed) |
| Seat reports `seats/*.md` | 20 | declared seat artifacts (SELF not yet written) |
| Seat scratch `seats/**` | 52687 | declared seat artifacts |
| Wave root outside `seats/` | 0 | — |
| Other lane paths | 0 | — |

10 + 20 + 52687 = 52717. Tracked dirt outside the four owned paths: none.

Fixture ten, sizes at 22:27: README 6176, claim-excerpt-map 17119, contradictions 3, entities 1793, fictional-excerpts 5114, inspiration-note 1956, relations 139, source-excerpt 640, sources 3293, timeline 2998. No extra path under the fixture dir.

## Write-time recheck (2026-10-17T22:45:16-03:00)

Lane tracked dirt unchanged (same two `M` lines). Producer absence unchanged (commands above). One lane path now sits outside the declared prefixes — it was not in the 22:27 listing (mtime 22:32:40, after that audit):

```
$ git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain=v1 -uall \
    | grep '^?? ' | sed 's/^?? //' \
    | grep -vE '^(\.ufo/waves/round-99/|corpus/fixtures/r99-window-lapse/)'
.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
```

`git ls-files` on that path: empty (new untracked file in the closed round-98 tree).

Parent repo (`/home/vgpnk/Projects/shokunin`, HEAD `9a74e25`) does not see lane dirt (`gitignore:1:*-shokunin/` matches `lore-shokunin`). Its own porcelain is only the stray below (8 files).

## Findings (observed writes, not a plan score)

### F1 — parent-repo stray (out of declared ownership)

`/home/vgpnk/Projects/shokunin/.ufo/` is a different tree from `lore-shokunin/.ufo/`. Created during this wave:

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 -uall
?? .ufo/waves/round-99/seats/V69-scratch/before/baseline-root/corpus/tools/dependency-freeze-contract.json
?? .ufo/waves/round-99/seats/V69-scratch/before/baseline-root/corpus/tools/dependency_freeze.py
?? .ufo/waves/round-99/seats/V73-scratch/selftests/boundary.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/boundary.out
?? .ufo/waves/round-99/seats/V73-scratch/selftests/freeze.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/freeze.out
?? .ufo/waves/round-99/seats/V73-scratch/selftests/map.err
?? .ufo/waves/round-99/seats/V73-scratch/selftests/map.out
```

V69 files are 0 bytes, mtime `2026-10-17 22:11:27 -0300`, plus an empty `corpus/fixtures/` directory. V73 files mtime `22:17:58`. V73 stderr (wrong cwd = fleet root):

```
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/dependency_freeze.py': [Errno 2] No such file or directory
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/boundary_doc_check.py': [Errno 2] No such file or directory
python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/map_obligations.py': [Errno 2] No such file or directory
```

Not removed by this seat. Same class as r98's parent stray.

### F2 — write into closed round-98 (out of declared ownership)

`.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`, 4208 bytes, mtime `2026-10-17 22:32:40.247271032 -0300`. Header says it is the original r98 V58 seat (agent-294) resumed at ~22:29, and that it did not overwrite the pinned completion-wave report. It is still a new untracked file outside `.ufo/waves/round-99/seats/` and outside producer ownership. Not removed.

### F3 — V40-scratch mirror (inside declared scratch; flag only)

```
$ du -sh .ufo/waves/round-99/seats/V40-scratch/archive
307M
$ ls archive
corpus  l0-questions.md  LOG.md  PROVINCE.md  README.md  reports  SCORECARD.md  SHONEN.md  SKILL.md
```

44825 of the 22:27 `??` lines were `V40-scratch`. `find archive -name .git` printed nothing (not a gitlink). Seats total at 22:27: 370M, of which V40-scratch was 308M. Flagged for L1 removal; not deleted. Same class as r98 V37.

### F4 — gitignored class (not a scope violation)

`.gitignore` matches `__pycache__/` and `*-self-test-*/`. Round-99 ignored hits at 22:27 were four `!!` pyc paths under `seats/` (V119, V43, V75). `corpus/tools/__pycache__/dependency_freeze.cpython-314.pyc` mtime `2026-10-17T22:03:26-03:00` (wave window) and is ignored, so it is not in porcelain. `./v05-self-test-scratch` mtime `2026-10-17T20:36:16-03:00` is pre-wave.

## Not done

Closed-wave confirmation that the change set is exactly declared ownership plus seat artifacts: not possible. S1 report, S2 edits and report, and S5 notes and report were absent at try 40 and at 22:45:16. Seat-report count was still climbing (71 other reports, not 127). C1/C2 were not verified. F1 and F2 are already outside the declared set on the in-flight tree; they are findings, not a substitute for the missing producer gate.

Bottom line: ABSENT — producer gate failed at try 40 and still at 22:45:16 (no S1/S2/S5 reports; SKILL.md and corpus/tools/README.md clean vs HEAD; both S5 knowledge notes missing); not a closed-wave confirmation; observed out-of-ownership writes already on disk are 8 parent-repo files under /home/vgpnk/Projects/shokunin/.ufo/waves/round-99/ (V69, V73) and one lane file in closed round-98 (V58 original-run resume note).
