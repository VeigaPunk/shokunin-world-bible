# V20 — scope-creep (round 98, COMPLETION-WAVE re-dispatch)

Seat: V20-scope-creep. Model: hyper/deepseek-v4.1-flash (re-dispatch; original seat aborted mid-wave).
Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin` (all commands run from here with `python3`).
Baseline named in brief: r97 closure `9a3d648`. Observed `HEAD = dd4df1b` (`lore r97: close round — SCORECARD admitted section`), i.e. one r97-closure commit ahead of the named baseline; `receipt.json` records `baseline_commit = 9a3d648…`, `head_at_snapshot = dd4df1b…`.

Task: run `git status --porcelain -uall`, bucket every path against the declared set, verify report-path exclusivity, check `__pycache__` / `*-self-test-*` (gitignored class), verify zero parent-tree strays, and flag the V37-scratch mirror for L1 removal.

## Method / raw evidence

```
$ git status --porcelain -uall | wc -l
44825
$ git status --porcelain -uall | grep -v '^?? '
 M LOG.md
 M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
 M corpus/knowledge/r95-aftermath-scope-note.md
 M corpus/knowledge/r96-response-scope-note.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
$ git status --porcelain -uall | grep '^?? ' | sed 's/^?? //' | awk -F/ '{print $1"/"$2}' | sort | uniq -c
     10 corpus/fixtures
      1 corpus/knowledge
  44807 .ufo/waves
$ git diff --stat | tail -1
 7 files changed, 371 insertions(+), 11 deletions(-)
```

## Bucket table

| Bucket | Paths | Count | Verdict |
|---|---|---|---|
| Producer: freeze tool | `corpus/tools/dependency_freeze.py` | 1 (M) | DECLARED |
| Producer: freeze contract | `corpus/tools/dependency-freeze-contract.json` | 1 (M) | DECLARED |
| Producer: tools docs | `corpus/tools/README.md` | 1 (M) | DECLARED |
| Producer: r95 map repair | `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` | 1 (M, 2-line diff) | DECLARED |
| Producer: r98 fixture | `corpus/fixtures/r98-clerk-filing/*` | 10 (??) | DECLARED |
| Producer: knowledge notes | `corpus/knowledge/r95-aftermath-scope-note.md` (M), `r96-response-scope-note.md` (M), `r98-clerk-scope-note.md` (??) | 3 | DECLARED |
| Round claims | `LOG.md` (M, +61) | 1 | DECLARED |
| Wave receipt | `.ufo/waves/round-98/receipt.json` (`record_type=round-98-receipt`) | 1 | DECLARED |
| Seat reports | `.ufo/waves/round-98/seats/*.md` | 58 | DECLARED |
| Seat scratch | `.ufo/waves/round-98/seats/*-scratch/**`, `seats/scratch/**` | ~44 111 ?? | DECLARED |
| Wave scratch | `.ufo/waves/round-98/scratch/**` | 692 ?? | DECLARED |
| **Round-98 root strays** | `.ufo/waves/round-98/V14-poll.sh`, `V14-poll.log`, `V14-poll2.log` | 3 | **FINDING (minor)** |
| **Parent-tree stray** | `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` | 1 | **FINDING** |

Every `??` path filters cleanly into a declared bucket:

```
$ git status --porcelain -uall | grep '^?? ' | sed 's/^?? //' \
  | grep -vE '^(\.ufo/waves/round-98/|corpus/fixtures/r98-clerk-filing/|corpus/knowledge/r98-clerk-scope-note\.md)'
(no output)
```

## Findings

### F1 — Parent-tree stray: `baseline-analyze.txt` (violates "zero parent-tree strays")
```
$ (cd /home/vgpnk/Projects/shokunin && git status --porcelain -uall)
?? baseline-analyze.txt
$ cat baseline-analyze.txt
python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory
$ stat -c '%s %y' baseline-analyze.txt
105 2026-10-17 20:30:10.645271523 -0300
```
105-byte file, born 20:30:10 during this wave, in the fleet-root repo (parent), not the lane. It is the stderr of `python3 analyze.py > baseline-analyze.txt` executed with cwd = the parent dir, where no `analyze.py` exists. The output filename matches `V57-scratch/baseline-analyze.txt` (25 209 B, the successful run saved inside scratch), so the redirect was run twice — once from the wrong cwd (leaking the stray) and once correctly. Attribution: high confidence to seat **V57** (aborted). This is the only parent-repo untracked path; parent repo has no tracked modifications.
Note: V24-scratch/outside-final.txt already recorded `./baseline-analyze.txt` in its fleet-root scan, and V20-scratch/snap/parent-full-final.txt contains the same path — the stray was visible to two seats but not removed.

### F2 — Round-98 root strays: V14 poll files at wave root (minor)
`.ufo/waves/round-98/V14-poll.sh`, `V14-poll.log`, `V14-poll2.log` sit directly under the wave root instead of the seat's own scratch dir `seats/V14-scratch/` (which exists and holds `check_v14.py`, `base/`). They are inside the declared `.ufo/waves/round-98/` bucket, so this is a placement deviation, not an out-of-scope write. The poll script itself is well-formed (polls S3/S4/S5 report presence). Recommendation: move under `seats/V14-scratch/` or leave as admitted wave scratch.

### F3 — V37-scratch 243 MB mirror (flag for L1 removal; not deleted)
```
$ du -sh .ufo/waves/round-98/seats/V37-scratch
243M
$ du -sh .ufo/waves/round-98/seats/V37-scratch/archive
242M
$ ls .ufo/waves/round-98/seats/V37-scratch/archive
corpus  .gitignore  l0-questions.md  LOG.md  PROVINCE.md  README.md  reports  SCORECARD.md  SHONEN.md  SKILL.md  .ufo
```
`archive/` is a full plain copy of the lane repo (corpus 7.7M, reports 6.4M, LOG.md 752K). No nested `.git` found (`find … -name .git` empty), so unlike r97's `9a3d648` ("drop embedded scratch clone (V37 mirror-freeze gitlink)") it is not a gitlink — but the bulk is a recurrence of the same mirror-bloat class. **Flagged for L1 removal; not deleted by this seat.** It is the single largest object in the wave (243M of 307M total under round-98).

### F4 — gitignored-class residue present (expected class, hygiene note)
```
$ find . -name '__pycache__' -not -path './.git/*' | head -3
./corpus/tools/__pycache__            <- inside a producer dir
./.ufo/waves/round-95/seats/V16-scratch/__pycache__
./.ufo/waves/round-96/seats/V38-scratch/lb/corpus/tools/tools/__pycache__
$ find . -maxdepth 3 -name '*-self-test-*' -not -path './.git/*'
./v05-self-test-scratch               <- lane root
$ git check-ignore -v corpus/tools/__pycache__ v05-self-test-scratch
.gitignore:2:__pycache__/	corpus/tools/__pycache__
.gitignore:4:*-self-test-*/	v05-self-test-scratch
```
Both classes exist on disk and are correctly matched by `.gitignore` (`__pycache__/`, `*-self-test-*/`), so neither appears in `git status` and neither can be committed. Round-98-specific instances: `seats/V36-scratch/__pycache__`, `seats/V54-scratch/__pycache__` (both aborted/other seats). `corpus/tools/__pycache__` is inside a producer directory but is ignored, so it is not a scope violation — noted for cleanliness only.

## Report-path exclusivity

- `seats/` top level = 58 `*.md` reports + one non-md artifact `V33-debt.json` (V33's declared JSON companion). Every `*.md` filename maps to a seat id; no report was written outside `seats/` (no `.md` under `corpus/`, lane root, or `scratch/`).
- V-number coverage `01..59`: missing reports are exactly **V20, V31, V36, V51, V57, V58** — the six aborted endgame seats, matching the brief. This seat (V20) fills one of them.
- Producer (S1–S5) reports all present; the 7 modified tracked files are exactly the declared producer paths (verified by `git diff --stat`). No undeclared tracked modification anywhere.
- Scratch location deviations observed but all still inside the declared round-98 bucket: V31 kept its scratch at `.ufo/waves/round-98/scratch/V31/` (no `seats/V31-scratch/`), V02 at `seats/scratch/V02/`; V14's poll files at the wave root (F2).

## Verdicts

- Bucket completeness: **PASS** — 44 825 `-uall` lines, 100 % map to declared buckets (1 producer-path set, 3 knowledge notes, 10 r98 fixture files, wave receipt, seat reports/scratch); zero undeclared untracked paths.
- Report-path exclusivity: **PASS** — all 58 reports live at `seats/<SEAT>.md`; the only missing reports are the 6 aborted seats.
- `__pycache__` / `*-self-test-*` class: **PASS (clean, ignored)** — present on disk, correctly gitignored, not committable.
- Parent-tree strays: **FAIL** — one stray: `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (F1).
- V37 mirror: **FLAGGED** — 243 MB `seats/V37-scratch/` (242 MB `archive/` repo copy) for L1 removal; not deleted.

No writes were made outside the declared report path. No separate per-seat receipt path was declared for V20 in this re-dispatch brief, so none was created (inventing one would itself be an undeclared stray).

Bottom line: FAIL — scope is clean inside the lane, but one parent-tree stray (`/home/vgpnk/Projects/shokunin/baseline-analyze.txt`, F1) plus a 243 MB V37-scratch mirror (F3) need L1 cleanup.
