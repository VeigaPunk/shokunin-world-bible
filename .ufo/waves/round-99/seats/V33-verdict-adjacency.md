# V33 — adjacency verdict (round 99)

**Seat:** V33 (verdict-adjacency), round-99 single wave (128 seats), lane `lore-shokunin`.
**Subject that was supposed to be measured:** the delivered r99 working tree vs baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD at seat start and at the post-window recheck was `337f0fa` (`337f0fa52b02626b7687eedbb2d99fab30446fe4`, "lore r99: record blocked dispatch attempt … — zero increment"). No r99 seat commit was observed. This seat makes **no** C1/C2 verdict, no admission verdict, and no lore-truth ruling.
**Mandate:** one ADJACENCY verdict, full battery, only after artifacts **and** all five producer reports exist. Poll-wait: 20 s cadence, max 40 tries; if still absent, report ABSENT and never verify a plan.
**Axes named (not measured):** (1) `PROVINCE.md` byte-identity vs `4265df5`; (2) write boundary and declared producer byte-ownership; (3) mythology editorial-only plus rights/canon/mechanics refusal scan over new bytes; (4) reports-vs-bytes ordering and post-report stability; (5) r99-specific adjacency — SKILL.md freeze-row-only, full-file pin stays inside `corpus/fixtures/**`, chain fixtures unmutated. None of these was scored. The producer gate failed, so running the battery would have been verifying a plan.

This seat's only writes are this report and `.ufo/waves/round-99/seats/V33-scratch/` (`poll.sh`, `poll2.sh`, `poll.log`, `audit.py` unused, charter hash snapshots). No corpus write, no commit, no push, no network, no nested agent.

## Poll-wait record

Gate (all required before any battery): the 16 producer artifacts (S1 tool + contract, S2 `corpus/tools/README.md` + `SKILL.md`, the ten `corpus/fixtures/r99-window-lapse/` files, S5's two knowledge notes) **and** five `S*-*.md` reports under `.ufo/waves/round-99/seats/`.

- Poll 1: `.ufo/waves/round-99/seats/V33-scratch/poll.sh`, started `2026-10-17 22:01:29 -0300`. Tries 1–30 logged. The hosting background command was killed at its 600 s tool ceiling (`task bash-pz7suf1h timed_out`, wall 600.001 s) **before** the script's own 40-try exit. That kill is a tool-timeout, not a protocol stall-escape and not an ABSENT declaration. Last line before the kill: `POLL t=22:11:10 try=30 arts=14/16 reps=2/5 … names=[S3-fixture-author.md S4-fixture-docs.md ] missing=[ corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md]`.
- Gap disclosed: try 30 at 22:11:10, resume at 22:16:09. About five minutes, caused by the tool timeout plus the restart, not by an extra sleep. Tries were not restarted from 1 and were not extended past 40.
- Poll 2: `V33-scratch/poll2.sh`, `POLL2_START 2026-10-17 22:16:09 -0300 resume_from_try=31`, tries 31–40, exit 2. Closing lines:

```
POLL t=22:19:09 try=40 arts=14/16 reps=2/5 py=6f81f8be1974 ct=8c2561b043c2 readme=294dd56f29ce skill=22ffaa822ec7 tbl= note= names=[S3-fixture-author.md S4-fixture-docs.md ] missing=[ corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md]
TIMEOUT t=2026-10-17 22:19:29 -0300 arts_last see log reps see log
```

`grep -c '^POLL t=' .ufo/waves/round-99/seats/V33-scratch/poll.log` → `40`. No `ALL-PRESENT` line. Endgame convention: the gate was the five producer reports, not all 128 seats; SELF (V33) was never in the count.

Post-window recheck, still absent (not a 41st protocol try; recorded so a late landing is not hidden):

```
$ date '+%Y-%m-%d %H:%M:%S %z'
2026-10-17 22:25:40 -0300
ABSENT corpus/knowledge/r99-gate-blind-spot-table.md
ABSENT corpus/knowledge/r99-lapse-scope-note.md
producer reports present:
  .ufo/waves/round-99/seats/S3-fixture-author.md
  .ufo/waves/round-99/seats/S4-fixture-docs.md
S1 reports=0
S2 reports=0
S5 reports=0
ls -d .ufo/waves/round-99/seats/S5-scratch → NO-S5-SCRATCH
```

**Battery not run.** `V33-scratch/audit.py` was written during the wait and was not executed. No `check_bible`, `support_check`, `map_obligations`, or `dependency_freeze` invocation by this seat. No province diff scored. No sibling-lane sweep scored. No rights/canon/mechanics scan scored.

## What the poll saw (observations, not a verdict)

These are poll facts. They are not an adjacency result. The tree at try 40 was not a delivered revision: three producer reports were missing, and the two S5 artifacts did not exist.

- Present reports: `S3-fixture-author.md` (mtime 22:01, 5069 bytes) from try 2; `S4-fixture-docs.md` (mtime 22:03, 9303 bytes) from try 9.
- Absent reports for the whole window: S1, S2, S5. `S2-scratch` exists and stayed empty (directory mtime 22:00:49). `S5-scratch` was never created. `S1-scratch/before/mirror/` exists (mtime 22:08:46) and is seat scratch, not a report.
- Absent artifacts for the whole window: `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`. `arts` stayed `14/16`.
- `corpus/fixtures/r99-window-lapse/` was present from try 1. At the first content look (before any battery, and before S4's report) it was not a finished beat: seven files matched `r98-clerk-filing`, while `timeline.json` / `sources.json` / `fictional-excerpts.md` already differed. README and map hashes later moved (`rd` `32efc78f70e6` → `1c95ca05aab6` → `b93209417a91`; `map` `c1099d0ee9ee` → `d2fe20e581d1`) before S4's report. That churn is why an existence-only check is not a delivered revision. Not scored.
- S1 bytes moved during the window and never acquired a report: `dependency_freeze.py` prefixes `03d04365cf00` (try 1, the r98 hash) → `c620324f543b` → `65c1ae309385` → `1728ed892442` → `6f81f8be1974` (stable from try 20 through try 40). Contract `153ebc5b2092` → `8f9c1f531614` → `8c2561b043c2` (stable from try 23 through try 40). A non-scoring peek at 22:25:40 showed `schema_version 2`, `pin_count 6`, `files_per_pin [10]`, sha256 prefixes `6f81f8be19742372` and `8c2561b043c25db7`. Without S1's report those bytes are not frozen and are not judged.
- S2 owned files were not part of the dirty set at the post-window check: `git diff --stat HEAD -- SKILL.md corpus/tools/README.md` was empty at 22:21:41. `git status --porcelain` outside `.ufo/waves/round-99/` at 22:25:40 was only:

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/fixtures/r99-window-lapse/
```

- HEAD stayed `337f0fa`. `git reflog -3` showed only the pre-dispatch commits `337f0fa` (21:53:33), `111b9a3` (21:37:06), `4265df5` (21:36:10). No seat commit observed. Not a push audit.

## Why this is ABSENT and not INCONCLUSIVE

INCONCLUSIVE would mean the delivered revision existed and a required check could not be completed. Here the delivered revision was not assembled inside the poll window: S5's two knowledge files were never written, and S1/S2/S5 never filed the reports the protocol requires before measurement. Scoring province identity, ownership, or mythology on that partial tree would be verifying a plan. The r99 declaration in `LOG.md` (standing, including the blocked-dispatch zero-increment note) was read and was not treated as a substitute for producer bytes.

## Bottom line

**ABSENT — after 40 poll tries (22:01:29–22:19:09 -0300, with a disclosed tool-timeout gap between try 30 and try 31) the producer gate was not met: S1/S2/S5 reports missing, and `corpus/knowledge/r99-gate-blind-spot-table.md` plus `corpus/knowledge/r99-lapse-scope-note.md` never appeared (still absent at the 22:25:40 recheck); the adjacency battery was not run.**
