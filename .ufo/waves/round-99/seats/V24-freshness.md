# V24 — freshness (round 99)

Seat: V24 freshness. Brief: *after producers* — stale-pin sweep of new bytes (no HEAD pins; metadata headers; README commands replay); the blind-spot table's commands are current-revision (spot-check 3).

Axes named for this seat: **freshness** only. Calibration, depth, coverage, operability, and adjacency were not scored. Leaf seat: no nested agents, no commits, no pushes, no network. Only writes: this report and `.ufo/waves/round-99/seats/V24-scratch/` (`poll.log`, `poll-start.txt`, `landed-only.txt`). Both paths resolve under `/home/vgpnk/Projects/shokunin/lore-shokunin/`. Commands ran from that lane root with `python3`. Baseline named in the standing r99 declaration: `4265df5`. Working-tree HEAD during the poll: `337f0fa` (`lore r99: record blocked dispatch attempt … — zero increment`). `git diff --name-status 4265df5 HEAD` is `M LOG.md` and `M SCORECARD.md` only.

## Poll-wait

Cadence 20 s, 40 tries, producer reports `S1*.md`…`S5*.md` at `.ufo/waves/round-99/seats/` maxdepth 1, plus the declared artifacts (`corpus/fixtures/r99-window-lapse/`, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`). SELF was not in the waited set (no all-reports poll, no stall-escape that waited on this seat).

```
POLL-START 2026-10-17 22:01:42
try=1 ts=22:01:42 … kn=[ABSENT] note=[ABSENT] reports:[ S1=ABSENT S2=ABSENT S3-fixture-author.md  S4=ABSENT S5=ABSENT]
try=15 ts=22:06:22 … kn=[ABSENT] note=[ABSENT] reports:[ S1=ABSENT S2=ABSENT S3-fixture-author.md  S4-fixture-docs.md  S5=ABSENT]
POLL-RESTART 2026-10-17 22:13:14 after 300s tool cap killed first loop
try=40 ts=22:21:14 fx=[files=10 sig=966ff9f0fafe] kn=[ABSENT] note=[ABSENT] mtime py=1792285653 ct=1792285726 rd=1792283525 sk=1792283663 reports:[ S1=ABSENT S2=ABSENT S3-fixture-author.md  S4-fixture-docs.md  S5=ABSENT]
POLL-END 2026-10-17 22:21:34
```

The first loop was killed by the tool's 300 s cap after try 15 (during the sleep before try 16). Tries 16–40 continued the same counter; the gap is recorded, not an extra budget. No `ALL-PRESENT` line.

Confirmation after the budget, still missing the same three reports and both knowledge files:

```
CONFIRM 2026-10-17 22:25:03 -03
find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md'
# 2026-10-17+22:01:40 5069 S3-fixture-author.md
# 2026-10-17+22:03:54 9303 S4-fixture-docs.md
ls corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
# cannot access … No such file or directory (both)
```

Reconfirmed at `2026-10-17 22:35:21`: same two producer reports, both knowledge paths still `No such file or directory`, `corpus/tools/README.md` and `SKILL.md` still mtime `21:32:05` / `21:34:23`.

## What was not verified (the brief's required set)

Not run, because the producer set was incomplete. Verifying these would have been verifying a plan.

1. **Blind-spot table, current-revision spot-check of 3 commands.** `corpus/knowledge/r99-gate-blind-spot-table.md` does not exist. S5 report does not exist. Zero commands to replay.
2. **Metadata headers on the new knowledge records.** `corpus/knowledge/r99-lapse-scope-note.md` does not exist either. No `source:` / `verified-at:` / `recheck:` header to check.
3. **Stale-pin sweep of the full new-byte set.** S1's `dependency_freeze.py` and `dependency-freeze-contract.json` changed during the poll (mtimes `22:07:33` and `22:08:46`) but S1 never reported. S2's owned bytes did not change. Those files were not swept as a delivered revision.

## Landed-only observations (not a freshness PASS)

S3 and S4 reports exist. The ten fixture files were swept and the three README replay commands were re-run at `22:31:37`. This does not close the seat.

**No HEAD pins in the ten fixture files.** Pattern `\bHEAD\b|rev-parse|latest revision|current revision|sha256:…|[0-9a-f]{40}` over every file in `corpus/fixtures/r99-window-lapse/`: `hits=0` on all ten (`landed-only.txt`).

**Fixture README / map do not carry the knowledge-note metadata header.** First lines are `# Round 99 window-lapse continuation` and `# r99 window-lapse: canonical claim-to-excerpt map`. No `source:` / `verified-at:` / `recheck:` / `citation-convention:` line. That header form belongs on the absent S5 notes, not on these two files.

**README commands replay on the landed fixture (exit 0):**

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
# CLEAN: schema, citations, relations, timeline; 0 violations
# bible_exit=0
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
# SOURCE-SUPPORT 21/21; … RESULT PASS
# support_exit=0
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
# OBLIGATIONS raw=21 mapped=21
# RESULT PASS
# map_exit=0
```

Those are the three commands at `corpus/fixtures/r99-window-lapse/README.md:26-28`. SHA-256 of the replayed README is `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`, matching S4's reported hash. Map sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`, also matching S4.

**S2 owned bytes unchanged vs baseline** (so there is no new tools-README command and no new SKILL freeze row to replay):

```
git diff --quiet 4265df5 -- corpus/tools/README.md && echo README_UNCHANGED
git diff --quiet 4265df5 -- SKILL.md && echo SKILL_UNCHANGED
# README_UNCHANGED
# SKILL_UNCHANGED
```

The carried SKILL freeze row still says 17 cases and "content SHA-256 over the five JSON tables" (`SKILL.md:98-100`). That is pre-round text, not a new pin. S2 did not land a supersession.

## Unreported in-flight bytes (not a verdict)

Observed at `22:25:03`, not classified, because S1 has no report and these bytes may still move:

```
git diff --stat 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
# dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
# dependency_freeze.py            |  65 ++++++++++-
python3 -c '…json.load contract…'
# schema 2 payload 2
# revision 337f0fa52b02626b7687eedbb2d99fab30446fe4
# pins [r88 … r98]          # no r99-window-lapse
# pinned_files = ten names
# self_test expected = 18   # includes markdown_tamper
# literal HEAD in contract False
git rev-parse HEAD
# 337f0fa52b02626b7687eedbb2d99fab30446fe4
```

The contract `revision` field equals the current HEAD sha. The literal token `HEAD` is not in the file. That is a fixed sha captured from `git rev-parse HEAD` at whatever moment S1 last wrote the contract, not a stored `HEAD` pin, and not a closed delivery. r99 is not in `pins`. No freshness classification is made from this snapshot.

## Bottom line

**ABSENT** — poll budget exhausted at try 40 (`22:21:14`) with S1, S2, and S5 reports missing and both S5 knowledge files missing; the blind-spot table's current-revision spot-check (3 commands), the knowledge-note metadata headers, and the stale-pin sweep of the full new-byte set were not run, and were not inferred from a plan. Landed S3/S4 fixture README replay is green and those ten files have no HEAD pins; that is not a freshness PASS.
