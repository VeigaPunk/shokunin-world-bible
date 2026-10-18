# V88 — freshness-3 (round 99)

Seat: **V88 freshness-3**. Brief: third freshness angle — run the F14-style pinned-replay script if present; confirm historical captures stay valid. Leaf seat. No nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V88-scratch/` only. Commands from lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Baseline named in the standing declaration: r98 closure `4265df5`. HEAD during this seat: `337f0fa` (`lore r99: record blocked dispatch attempt … — zero increment`). Wave tree uncommitted.

Axes used: poll-completeness (artifacts and producer reports, not a plan), script-presence (F14-style pinned-replay, run only if present), capture-validity (withheld until a frozen delivered revision), evidence (quoted commands), isolation (exclusive paths only).

## Poll-wait — budget exhausted, set still incomplete

Background poll started `2026-10-17T22:02:23-0300`, 20 s cadence, 40 tries. Each try required the seven round artifacts and S1–S5 reports (SELF subtracted: no V-seat report was ever a gate). No stall-escape. Log: `.ufo/waves/round-99/seats/V88-scratch/poll.log`.

Try 1 (`22:02:23`): arts 5/7, reports S3 only, r99 fixture already had all ten files. Try 6 (`22:04:03`): S4 report appeared. Tries 6–40: no further producer report and no knowledge artifact. Try 40 (`22:15:23`):

```
TIMEOUT missing_arts=['corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/knowledge/r99-lapse-scope-note.md'] missing_reports=['S1', 'S2', 'S5'] fixture_files=['README.md', 'claim-excerpt-map.md', 'contradictions.json', 'entities.json', 'fictional-excerpts.md', 'inspiration-note.md', 'relations.json', 'source-excerpt.md', 'sources.json', 'timeline.json']
```

Post-timeout snapshots (not a second 40-try poll) still ABSENT:

```
$ date -Is
2026-10-17T22:32:11-03:00
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git status --porcelain
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-99/
?? corpus/fixtures/r99-window-lapse/
```

Producer glob at `22:32:11`: S1 ABSENT, S2 ABSENT, S3 `S3-fixture-author.md`, S4 `S4-fixture-docs.md`, S5 ABSENT. Knowledge paths `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`: ABSENT. Tool mtimes at the `22:29:51` recheck (unchanged at `22:32:11`): `dependency_freeze.py` `22:07:33`, contract `22:08:46`, `corpus/tools/README.md` `21:32:05`, `SKILL.md` `21:34:23`, `check_bible.py` `06:50:47`. README and SKILL.md are not in `git status --porcelain`, so S2's freeze-row edit has not landed as a content change. S1's pair is dirty and newer than the poll start, but S1 never filed a report — those bytes are not a frozen delivered revision.

Partial presence is not a freeze. S3/S4 reports and the ten-file `corpus/fixtures/r99-window-lapse/` directory exist. That is not the round's delivered set.

## F14-style pinned-replay script — not present

Searched standing lane locations (`corpus/`, `scripts/` which does not exist, `.ufo/waves/round-94/`, `.ufo/waves/round-93/`) for a script that replays inherited `corpus/fixtures/` checker tuples against pinned receipts the way round-94 follow-up F14 did. No file named `pinned-replay`, `pinned_replay`, `f14-style`, or `F14-replay`. `corpus/tools/*.py` is only `boundary_doc_check.py`, `dependency_freeze.py`, `discriminate_check.py`, `map_obligations.py`, `support_check.py`.

Round-94 F14 (`.ufo/waves/round-94/followup/F14-preservation-regression.md`) states its intermediates were deleted: "No scratch files were retained; the two temporary `/tmp/F14-*.json` intermediates were deleted." That script is not in the tree.

Nearby scripts are a different job and were not run as a substitute:

- `.ufo/waves/round-93/deepseek/F14-postrepair-check.py` — r93 namespace post-repair replay of three fixture input trees, not the 167-dir preservation tuple replay.
- `F19-independent-replay.py` — two r91 differential fixtures.
- `F25-replay.py` — one r89 fixture across three git revisions.
- `.ufo/waves/round-94/work/W09-replay.py`, `W14-replay.py`, `W15-replay.py`, `W22-replay.py` — single-fixture or case replays, not a pinned census of inherited captures.

Historical capture files are on disk and were not opened as a verdict: `.ufo/waves/round-94/work/W04-baseline.json`, `.ufo/waves/round-93/followup/JCAL5-tuples.json`, `corpus/live/runs/` (timestamped dirs plus the later `round-85` generation, not enumerated here). Replaying them against an unfrozen producer set would be verifying a plan. Not done.

## What this does not establish

No exit-code, stdout-SHA, or violation-count comparison against W04, JCAL5, F01, F02, JCAL1, or `corpus/live/runs/`. No claim that historical captures stayed valid. No claim that they drifted. S1/S2/S5 may still land after this report; a later seat can replay on the frozen revision. This seat's poll budget is spent.

## Bottom line

**ABSENT** — after 40 tries (22:02:23–22:15:23) and rechecks through 22:32:11, S1/S2/S5 reports and both r99 knowledge artifacts are still missing, so there is no frozen delivered revision; the F14-style pinned-replay script is not present, and historical captures were not replayed.
