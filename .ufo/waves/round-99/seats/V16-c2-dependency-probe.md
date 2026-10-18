# V16 c2-dependency-probe — round 99 seat report

- Seat: V16 (verifier, C2 dependency probes). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from the lane root with `python3`. No commits, no pushes, no network. Live fixture, tool, and contract were not written by this seat.
- Producer polled: **S3** (`S3-fixture-author.md` + `corpus/fixtures/r99-window-lapse/`). Content-gated poll (r98 placeholder class): directory presence was not enough. HIT required `clerk-lapse-recorded` in `timeline.json`, `clerk-lapse-note` in `sources.json`, and a nonempty `S3-fixture-author.md`.
- Scratch (mine, absolute): `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V16-scratch/` (`poll.sh`, `poll.log`, `poll-pin.sh`, `poll-pin.log`, `probe.py`, `probe-run-1.txt`, `freeze_probe.py`, `freeze-copy/`, `r99-depdropped/`). Mutations ran only on `shutil.copytree` copies.

## Poll

```
try=1 ts=2026-10-17 22:01:01 -0300 dir=yes tl=yes ev=0 src=yes note=0 report=no
try=2 ts=2026-10-17 22:01:21 -0300 dir=yes tl=yes ev=1 src=yes note=1 report=no
try=3 ts=2026-10-17 22:01:41 -0300 dir=yes tl=yes ev=1 src=yes note=1 report=yes
HIT try=3 ts=2026-10-17 22:01:41 -0300
```

Try 1 was the copy-then-extend placeholder (`ev=0`). Verdict is bound to the post-HIT revision, not that placeholder.

The freeze half also needed an `r99-window-lapse` pin ("pinned now"). Separate pin poll, 20 s cadence, 40 tries, then one recorded stall-escape (tool mtime moved at 22:38:11 during try 35, one minute before the cap):

```
PIN_ABSENT after 40 tries ts=2026-10-17 22:39:44 -0300
STALL-ESCAPE start 2026-10-17 22:51:30 -0300 reason=tool rewritten after try-40 cap
STALL-ESCAPE ABSENT 2026-10-17 22:53:50 -0300
```

S1's report `S1-full-file-pins.md` (mtime `2026-10-17 22:48:57`) was read at 23:00:13. It is the delivered freeze revision, not an in-flight plan. Quoted: "`r99-window-lapse` was not pinned: C1's chain is the existing six, and that fixture is other seats' bytes (it was being written during this seat)." Re-check at 23:00:13: `r99` still absent; pinned names still the six chain fixtures. No further wait.

## Binding evidence

Delivered lapse event (read from `corpus/fixtures/r99-window-lapse/timeline.json`, index 7):

```json
{ "id": "clerk-lapse-recorded", "tick": 15, "entity_id": "clerk-maren", "place_id": "chalk-stair",
  "depends_on": ["clerk-filing-open"],
  "description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.",
  "source_id": "clerk-lapse-note" }
```

Predecessor unchanged from r98: `clerk-filing-open` tick 14, `depends_on: ["acknowledgment-aru-records"]`.

Hashes. `timeline.json` was byte-stable from the probe run through the final read (`2026-10-17 22:58:20`). Checker is the r98 closure pin.

```
$ sha256sum corpus/fixtures/r99-window-lapse/timeline.json corpus/fixtures/check_bible.py \
    corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
$ stat -c '%y %n' corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r99-window-lapse/timeline.json
2026-10-17 22:38:11.814368253 -0300 corpus/tools/dependency_freeze.py
2026-10-17 22:08:46.248249589 -0300 corpus/tools/dependency-freeze-contract.json
2026-10-17 22:01:13.842835114 -0300 corpus/fixtures/r99-window-lapse/timeline.json
```

Same `timeline.json` digest at the 22:02 probe-time measurement. `sources.json` `8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15`, `entities.json` `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984`. S4 later rewrote `README.md` and `claim-excerpt-map.md`; those files are not inputs to the checker probes. Contract `payload_schema_version` 2, `schema_version` 2, pins exactly `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`.

Live control, unmutated fixture, `2026-10-17 22:47:57`:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0
```

## Checker probes (scratch copies)

Harness: `python3 .ufo/waves/round-99/seats/V16-scratch/probe.py` — copies the delivered fixture under scratch `TemporaryDirectory`, one mutation per copy, then `python3 corpus/fixtures/check_bible.py <copy>`. Transcript: `.ufo/waves/round-99/seats/V16-scratch/probe-run-1.txt`. Script printed `LIVE BYTE-STABLE True` after the battery.

| # | Mutation | Exit | Checker output (verbatim) |
|---|---|---:|---|
| P0 | none (copy control) | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| P1 | drop `depends_on` key from `clerk-lapse-recorded` | 1 | `VIOLATION: timeline[7].depends_on: required nonempty list` |
| P2 | `depends_on = ["no-such-event-id"]` | 1 | `VIOLATION: timeline[7].depends_on: unknown event 'no-such-event-id'` |
| P3 | lapse event `tick = 14` (dependency stays tick 14) | 1 | `VIOLATION: timeline[7].depends_on: timeline inversion 'clerk-filing-open' tick 14 not before 'clerk-lapse-recorded' tick 14` |
| P4 | remove event `clerk-filing-open` | 1 | `VIOLATION: timeline[6].depends_on: unknown event 'clerk-filing-open'` |

Each failing run also printed `1 violation(s); no canon changed`. P3 before-state printed by the harness: `clerk-lapse-recorded tick=15 depends_on=['clerk-filing-open']; clerk-filing-open tick=14`. P4 count printed `8 -> 7 events`.

P4 is the dangling-edge case. The checker does not use the word `dangling` for a missing dependency; that wording is reserved for entity references (`check_bible.py` entity path). The missing predecessor is reported as `unknown event`. That is the report. It is not a miss.

Discrimination, not a mandated probe: emptying the list (`depends_on ['clerk-filing-open'] -> []`, key retained) stays checker-green:

```
=== P5 emptied depends_on (bible, discrimination) check_bible exit=0 ===
CLEAN: schema, citations, relations, timeline; 0 violations
```

That is the class `dependency_freeze` is supposed to catch once the edge is pinned. It is not pinned.

## dependency_freeze on the dropped-edge copy

Expected by the seat brief: `REDUCTION-DETECTED` exit 1, because the edge would be pinned. Observed on the delivered contract: `UNPINNED-FIXTURE` exit 2. `compare()` never ran. `pin_for` keys on `fixture.resolve().name` and fails before `bind_path`, so this is not `PATH-MISMATCH`.

Delivered-tool run, `2026-10-17 22:51:30`, after S1's final tool write (`22:38:11`, sha `fb9bb9ff…`) and after the contract write (`22:08:46`, sha `8c2561b0…`). Both digests still matched at `22:58:20`. Copy kept the fixture basename. Only change: `clerk-lapse-recorded.depends_on` `['clerk-filing-open']` → `[]`.

```
$ python3 corpus/tools/dependency_freeze.py \
    .ufo/waves/round-99/seats/V16-scratch/freeze-copy/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT 2
```

Same finding on the earlier battery (P5 and P5b, copies also named `r99-window-lapse`), against the then-current tool, also exit 2 `UNPINNED-FIXTURE` / `RESULT ERROR`. A copy renamed `r99-depdropped` (22:47:57, same tool sha `fb9bb9ff…`) reported `no pin for 'r99-depdropped'` — basename lookup, not a path bind. Quoted so the mechanism is the observed one, not an inference.

I did not `--freeze` r99 into the live contract (S1 owns it) and did not manufacture a scratch pin in order to force `REDUCTION-DETECTED`. That would not be the delivered revision. S1's report is explicit that the omission is intentional on their reading of C1 (chain stays six). On those delivered bytes the dropped r99 edge is invisible to `dependency_freeze`.

## What this seat did not claim

Map obligations, census, excerpt wording, and the C1 ten-file pin behavior on the six pinned fixtures were not this seat's probes. S4's README/map edits are noted only as hash drift that does not touch `timeline.json`.

## Bottom line

**FAIL** — checker probes on the delivered r99 revision (`timeline.json` `2cdb9fda…`, checker `ff9fd2aa…`) match: dropped `depends_on` → `required nonempty list` exit 1; unknown id → `unknown event` exit 1; tick 14 → `timeline inversion … tick 14 not before … tick 14` exit 1; removed `clerk-filing-open` → dangling edge reported as `unknown event` exit 1; live control CLEAN exit 0. The freeze half does not: dropped-edge copy of `r99-window-lapse` is `FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse'` / `RESULT ERROR` exit 2, not `REDUCTION-DETECTED` exit 1. S1's delivered report states r99 was not pinned; the contract at `8c2561b0…` still lists only the six earlier fixtures.
