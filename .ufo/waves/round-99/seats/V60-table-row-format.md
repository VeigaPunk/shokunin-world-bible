# V60 table-row-format — round 99

Seat: V60 table-row-format. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline named in the standing r99 declaration: `4265df5`. Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report and `.ufo/waves/round-99/seats/V60-scratch/` (`poll.log`, `poll.sh`).

Axes named, not scored: (1) every table row has the columns the table itself declares; (2) every replay command is copy-paste runnable from the lane root; (3) quoted outputs match observed stdout/stderr/exit verbatim. None of the three can be scored. The artifact was absent for the whole poll window.

Target artifact: `corpus/knowledge/r99-gate-blind-spot-table.md` (S5). Companion producer report: any `S5*.md` directly under `.ufo/waves/round-99/seats/`. Protocol: 20 s cadence, 40 tries; ABSENT, never verify a plan.

## Poll-wait record

Poll log: `.ufo/waves/round-99/seats/V60-scratch/poll.log`. Tries 1–10 were inline shell checks. Tries 11–40 were `.ufo/waves/round-99/seats/V60-scratch/poll.sh 11 40` (exit 2, `POLL_EXHAUSTED`).

Try 1, 2026-10-17T22:01:26-03:00:

```
ls -la /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r99*
ls: cannot access '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r99*': No such file or directory
ls -la /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S*.md
ls: cannot access '.../seats/S*.md': No such file or directory
```

Producer reports that did land during the window (not the table owner):

- try 2, 2026-10-17T22:01:59-03:00: `S3-fixture-author.md` 5069 bytes
- try 7, 2026-10-17T22:04:01-03:00: `S4-fixture-docs.md` 9303 bytes

Try 40, 2026-10-17T22:17:30-03:00 (script, exit 2):

```
table: ABSENT
S5: ABSENT
producer reports:
S3-fixture-author.md 5069
S4-fixture-docs.md 9303
POLL_EXHAUSTED try=40 table_and_or_S5 still absent
```

Tries 11–39 recorded the same absence. S1 and S2 reports never appeared under `seats/S*.md`. S5 scratch directory never appeared.

Post-window check, 2026-10-17T22:23:49-03:00, from the lane root:

```
ls -la corpus/knowledge/r99*
ls: cannot access 'corpus/knowledge/r99*': No such file or directory
find corpus/knowledge -name '*blind*' -o -name '*r99*'
(no output)
find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md'
S3-fixture-author.md 5069
S4-fixture-docs.md 9303
```

Write-time check, 2026-10-17T22:29:58-03:00, from the lane root:

```
ls -la corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
find .ufo/waves/round-99/seats -maxdepth 1 -name 'S5*.md'
(no output)
test -f corpus/knowledge/r99-gate-blind-spot-table.md; echo table_exists=$?
table_exists=1
```

`table_exists=1` is the shell test failure (file missing), not a checker exit.

## What was not verified

No table header, no declared columns, no row, no fenced command, and no quoted output were present to replay. Zero commands from the table were run. A plan, a declaration paragraph, and another seat's scratch inventory are not the delivered table.

Observed and not used as the artifact:

- `LOG.md` Round 99 declaration (standing text only) names the future columns: mutation class, gates that DO catch it, gates that do NOT, replayed command, observed output. That is a claim, not a table.
- `.ufo/waves/round-99/seats/V18-scratch/blind-spot-inventory.md` (3234 bytes, mtime 2026-10-17T22:13:39-03:00) is another seat's scratch. Not read as the table. Not replayed.
- Mid-window `stat` (between polls, not a table receipt): `corpus/tools/dependency_freeze.py` mtime 2026-10-17 22:07:33 size 29104; `corpus/tools/dependency-freeze-contract.json` mtime 2026-10-17 22:08:46 size 25987; both `git status --short` dirty. `corpus/tools/README.md` and `SKILL.md` were still at 21:32 / 21:34. No S1 or S2 report. Those bytes are not this seat's target and were not replayed as table rows.
- S3 report states the fixture is 6/1/8 and quotes `check_bible` CLEAN exit 0. S4 report states a 21-row map. Neither file is `r99-gate-blind-spot-table.md`. Their claims were not re-run here.

## Limits

This seat did not score column completeness, copy-paste runnability, or verbatim output match. No stall-escape was taken; the 40-try cap was reached with the artifact absent, which the protocol records as ABSENT rather than as a failed verification of contents.

Handoff recheck, 2026-10-17T22:39:46-03:00, from the lane root:

```
ls -la corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
find .ufo/waves/round-99/seats -maxdepth 1 -name 'S5*.md'
(no output)
```

ABSENT: `corpus/knowledge/r99-gate-blind-spot-table.md` and the S5 producer report were absent through 40 polls (22:01:26–22:17:30-03:00) and still absent at the 22:39:46-03:00 handoff recheck; no table row was replayed.
