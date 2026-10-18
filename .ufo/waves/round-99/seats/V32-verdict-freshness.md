# V32 — verdict-freshness (round 99)

Seat: **V32 verdict-freshness** (verifier). Role: one **FRESHNESS** verdict on the delivered bytes of round 99. Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the round: `337f0fa` (`337f0fa52b02626b7687eedbb2d99fab30446fe4`, the blocked-dispatch record). Wave tree uncommitted. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` / `sha256sum`; every write resolved under `lore-shokunin/` (this report absolute; scratch under `.ufo/waves/round-99/seats/V32-scratch/`). Leaf seat: no nested agents, no commits, no pushes, no network. ENDGAME: no all-reports poll waited on SELF.

## Verdict

**FRESHNESS: ABSENT** — not scored. The bytes this axis judges (S5's two new knowledge notes, plus producer reports for the pin-owning seats) were not on disk after the 40-try budget, and were still absent at the post-expire recheck. I did not replay gates, compare contract digests to files, or treat the in-flight freeze pair or the r99 fixture as a finished freshness surface. That would be verifying an unfinished wave.

## Poll-wait record (artifact-based)

Required before any freshness score: the ten `corpus/fixtures/r99-window-lapse/` files, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, the freeze pair, and at least five `S[1-5]*.md` producer reports under `.ufo/waves/round-99/seats/` (SELF subtracted; no V-seat report was a gate).

- Poll 1 (`V32-scratch/poll.sh`, pid 1671686, 20 s cadence, log `V32-scratch/poll.log`) started `2026-10-17T22:01:17-0300`. The hosting shell cap was 300 s, so the process was killed after try 15 (`22:05:57`, `art=no rep=no`, reports only `S3-fixture-author.md`, freeze pair still moving). That kill is a recorded stall-escape, not a protocol expire. Tries 1–15 stand.
- Poll 2 resumed tries 16–40 in the same log (`POLL_RESUME … from_try=16`). Try 40 at `2026-10-17T22:22:00-0300`:

```
try=40 t=2026-10-17T22:22:00-0300 art=no rep=no sreports=[S3-fixture-author.md S4-fixture-docs.md ] freeze12=[6f81f8be1974 8c2561b043c2 ] know=[]
POLL_EXPIRE try=40 2026-10-17T22:22:20-0300
```

`grep -c '^try=' V32-scratch/poll.log` → `40`. No further extension.

- Recheck at report time, same targets, still absent:

```
$ date
2026-10-17T22:31:14-0300
$ find .ufo/waves/round-99/seats -maxdepth 1 -type f -name 'S*.md' -printf '%f\n'
S3-fixture-author.md
S4-fixture-docs.md
$ test -s corpus/knowledge/r99-gate-blind-spot-table.md; echo ABSENT
$ test -s corpus/knowledge/r99-lapse-scope-note.md; echo ABSENT
$ ls corpus/knowledge/ | awk '/r99/'
(no output)
```

Host: `df -i /tmp` at start and at recheck was 3% used (`IUse% 3%`). No scratch relocation.

## What was absent (the judged set)

| Target | State at try 40 and at 22:31:14 |
|---|---|
| `corpus/knowledge/r99-gate-blind-spot-table.md` | ABSENT (no `corpus/knowledge/r99*` file) |
| `corpus/knowledge/r99-lapse-scope-note.md` | ABSENT |
| S1 producer report (`S1*.md`) | ABSENT. `S1-scratch/` exists (mtime 22:08) and holds only an empty-looking `before/` subdirectory; no report. |
| S2 producer report (`S2*.md`) | ABSENT. `S2-scratch/` is empty (mtime 22:00, size 0). |
| S5 producer report (`S5*.md`) | ABSENT. No `S5-scratch/` directory. |

S2's owned docs had not moved off the r98 closure bytes:

```
$ git diff --stat 4265df5 -- corpus/tools/README.md SKILL.md
(no output)
$ stat -c '%y %n' corpus/tools/README.md SKILL.md
2026-10-17 21:32:05 … corpus/tools/README.md
2026-10-17 21:34:23 … SKILL.md
```

Those mtimes predate this wave. I do not score the r98 wording still in those files as a freshness harm: S2 had not delivered, and scoring that text would be scoring a plan.

## What was present, and not scored

Recorded only so the absence claim is not a misread of an empty tree. Not a freshness movement.

- `corpus/fixtures/r99-window-lapse/` — all ten files present by try 9 (README/map rewritten off the r98 placeholders by 22:03; S3 report 22:01:40, S4 report 22:03:54). No hash-shaped pins in those ten files at the early read (`grep` for `[0-9a-f]{12,}` / `HEAD` / `4265df5` / `sha256` → no matches). Not re-scored after expire.
- Freeze pair, stable from the 22:08:46 contract mtime through the 22:31:14 recheck (same sha at try 22, try 40, and recheck):

```
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

`git status --porcelain` at 22:31:14 (excluding `.ufo/`) was exactly `M` those two files plus `?? corpus/fixtures/r99-window-lapse/` (ten paths). No knowledge notes. S1's report never arrived, so those hashes are an in-flight observation, not a delivered pin I accepted.

- Other V-seat reports had started landing by 22:31. They were not a gate and were not read as a substitute for the missing notes.

## What was not done

No receipt replay, no digest-vs-file comparison, no self-test, no chain run, no classification of live pins as fresh or stale. The r98 carried corrections (r95/r96 addenda, r98 note's dated contract-pin correction) were not re-opened. Closure-side docs were not judged.

## Bottom line

**ABSENT** — after 40 poll tries (expire `2026-10-17T22:22:20-0300`) and a 22:31:14 recheck, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and producer reports S1/S2/S5 were absent; freshness was not scored.
