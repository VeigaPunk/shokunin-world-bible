# V97 c1-selftest-isolation — round 99

- Seat: **V97 c1-selftest-isolation** (verifier). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure
  `4265df5e86e4121bde4125b649b89bb1676676a5`. HEAD during this seat
  `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`lore r99: record blocked
  dispatch attempt … — zero increment`). Wave tree uncommitted. Commands
  from the lane root with `python3` unless noted.
- Claim under test: `--self-test` writes nothing outside its scratch dir
  (hash repo root before/after; list new entries).
- Wrote only this report (absolute path) and
  `.ufo/waves/round-99/seats/V97-scratch/`. Leaf seat: no nested agents,
  no commits, no pushes, no network. `--self-test` was **not** run.

## 0. Poll-wait (20 s cadence, 40 tries; artifacts AND S1 report)

Required before any isolation measurement: S1 producer report
(`seats/S1*.md` or `seats/s1*.md`, non-empty) **and** a stable
tool+contract pair whose contract `self_test.expected` contains
`markdown_tamper` and whose six pins each name at least ten files.
Two consecutive tries with the same hash pair required, so a mid-write
was not treated as delivered. No all-reports poll (endgame convention
not triggered; this seat's producer dependency is S1 only).

Stall-escape (recorded, not fatal): the first poll process was killed
by a 300 s tool timeout after try 15 (`2026-10-17T22:08:27-0300`).
Resumed at try 16 (`2026-10-17T22:15:00-0300`). Tries are numbered 1–40
across both processes. Log:
`.ufo/waves/round-99/seats/V97-scratch/poll.log`.

```
try=1 ts=2026-10-17T22:03:47-0300 s1n=0 s1=NONE pair=1728ed892442c498:153ebc5b2092948e exp 17 md 0 ... schema 1
try=3 ts=2026-10-17T22:04:27-0300 s1n=0 s1=NONE pair=1728ed892442c498:73b28933f1488280 exp 18 md 1 ...
try=13 ts=2026-10-17T22:07:47-0300 s1n=0 s1=NONE pair=6f81f8be19742372:8f9c1f5316141b61 exp 18 md 1 ...
try=15 ts=2026-10-17T22:08:27-0300 s1n=0 s1=NONE pair=6f81f8be19742372:8f9c1f5316141b61 exp 18 md 1 ...
poll-resume 2026-10-17T22:15:00-0300 prior_tries=15 reason=first-poll-killed-at-tool-timeout-300s
try=16 ts=2026-10-17T22:15:00-0300 s1n=0 s1=NONE pair=6f81f8be19742372:8c2561b043c25db7 exp 18 md 1 schema 2 2 pins r88-m3-maya-cluster:10 r94-paired-crossing:10 r95-crossing-aftermath:10 r96-crossing-response:10 r97-crossing-acknowledgment:10 r98-clerk-filing:10
try=40 ts=2026-10-17T22:23:01-0300 s1n=0 s1=NONE pair=6f81f8be19742372:8c2561b043c25db7 exp 18 md 1 schema 2 2 pins r88-m3-maya-cluster:10 ... r98-clerk-filing:10
ABSENT after 40 tries 2026-10-17T22:23:21-0300
```

Resume poll exit code: `2` (the script's ABSENT exit). No `READY` line.
No `ready-py.sha256` / `ready-contract.sha256` / `ready.ts` written.

Producer reports present at try 40 and at the post-budget check: only
`S3-fixture-author.md` and `S4-fixture-docs.md`. No `S1*.md`, no
`s1*.md`, no `S2*.md`, no `S5*.md`.

Post-budget check (not a 41st try; absence had already been decided):

```
$ date '+%Y-%m-%dT%H:%M:%S%z'
2026-10-17T22:28:13-0300
$ ls seats/S1*.md seats/s1*.md
ls: cannot access '.../seats/S1*.md': No such file or directory
ls: cannot access '.../seats/s1*.md': No such file or directory
$ find seats -maxdepth 1 -type f \( -name 'S1*' -o -name 's1*' \) | wc -l
0
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git rev-parse --verify 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5
```

`S1-scratch/` exists (mtime `2026-10-17+22:08:46`) and contains only
`before/mirror/` (a copied tool, contract, and fixture tree). It is not
a producer report.

## 1. Isolation measurement — not run

`--self-test` was not executed. Repo-root before/after hashes were not
taken around a self-test run. New entries were not listed for a
self-test window. Doing so without an S1 report would verify an
unreported delivery (the poll rule: absent → ABSENT, never verify a
plan).

On-disk bytes observed during the wait are **not** a verdict. From try
16 through the 22:28 post-check the pair
`6f81f8be19742372…` / `8c2561b043c25db7…` did not change, the contract
reported `exp 18`, `markdown_tamper` present, `schema 2`, and six pins
at 10 files each. That stability is recorded only so a later seat can
see the poll did not miss a moving target. It is not a substitute for
S1's report, and it is not an isolation result.

Scratch dir the delivered code would use, read but not exercised:
`tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-", dir=ROOT)`
at `corpus/tools/dependency_freeze.py` (the `with` that wraps
`self_test_cases`). `.gitignore` line 4 is `*-self-test-*/`. Neither
fact was confirmed by a run.

## Bottom line

**ABSENT** — S1 producer report never landed in 40 tries (22:03:47–22:23:21, one recorded stall-escape); `--self-test` isolation was not measured.
