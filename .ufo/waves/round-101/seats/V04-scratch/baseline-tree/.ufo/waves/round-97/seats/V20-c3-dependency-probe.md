# V20 c3-dependency-probe — round 97 seat report

- Seat: V20 (verifier, C3 dependency probes). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands run from the lane repo root with `python3`.
- Producer polled: **R4** (`R4-fixture-author.md` + `corpus/fixtures/r97-crossing-acknowledgment/**`). Poll protocol: 20 s cadence. First fixture file set present at try 4 (18:44:20); R4's report present at **try 22, 18:50:20** — within the 40-try budget. Verdict bound to the delivered revision.
- Scratch (mine, absolute): `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V20-scratch/` (`probe.py`, `probe-run-final.txt`, `r97-hash-*.txt`). No commits, no pushes, no network; the live fixture was never modified (every mutation ran on a `shutil.copytree` copy under scratch `TMPDIR`).

## Binding evidence (delivered revision)

```
$ sha256sum corpus/fixtures/r97-crossing-acknowledgment/timeline.json corpus/fixtures/r97-crossing-acknowledgment/sources.json corpus/fixtures/check_bible.py
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  corpus/fixtures/r97-crossing-acknowledgment/sources.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ stat -c '%y' corpus/fixtures/r97-crossing-acknowledgment/timeline.json
2026-10-17 18:44:30.293362420 -0300
```

`timeline.json` was byte-stable from 18:44:30 through the final probe run after R4's report landed (`diff` of pre-report vs post-report `sha256sum` sets → no change). The checker hash `ff9fd2aa…` matches the lane's pinned checker recorded at r96 closure. All probes ran against `73063a86…`; no probe result is carried from a different revision.

Probed shape (from the delivered `timeline.json`, index 5 = the new event):

```json
{ "id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru", "place_id": "chalk-stair",
  "depends_on": ["response-evin-salt-court"], "source_id": "aru-acknowledgment-note" }
```

Inherited continuity checks (context, read-only): `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` are byte-identical to `r96-crossing-response` (`cmp -s` → IDENTICAL each); the parsed r96 timeline array equals the r97 array's first 5 rows (`inherited prefix equal: True`); only the tick-13 row is new. So every probe below mutates exactly one thing in the delivered revision.

## Probe battery (commands and observed outputs)

Harness: `TMPDIR=…/V20-scratch/tmp python3 .ufo/waves/round-97/seats/V20-scratch/probe.py corpus/fixtures/r97-crossing-acknowledgment` — copies the delivered fixture to a scratch temp tree, applies one mutation to `timeline.json`, then runs `python3 corpus/fixtures/check_bible.py <copy>`. Full transcript: `.ufo/waves/round-97/seats/V20-scratch/probe-run-final.txt`.

Baseline on the live (unmutated) delivered fixture:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

| # | Mutation | Exit | Checker output (verbatim) |
|---|---|---:|---|
| P1 | drop `depends_on` key from `acknowledgment-aru-records` | 1 | `VIOLATION: timeline[5].depends_on: required nonempty list` |
| P2 | `depends_on = ["no-such-event-id"]` | 1 | `VIOLATION: timeline[5].depends_on: unknown event 'no-such-event-id'` |
| P3 | ack event `tick = 11` (dependency stays tick 12) | 1 | `VIOLATION: timeline[5].depends_on: timeline inversion 'response-evin-salt-court' tick 12 not before 'acknowledgment-aru-records' tick 11` |
| P4 | remove event `response-evin-salt-court` | 1 | `VIOLATION: timeline[4].depends_on: unknown event 'response-evin-salt-court'` |

All four mandated probes report as expected on the delivered revision. The seat-requested "dangling" case is reported by the checker as `unknown event` (its dangling-reference wording is reserved for entity references); the dependency edge dangles exactly as intended.

Extra probes run in the same battery (discrimination boundary, not defects):

| # | Mutation | Exit | Output |
|---|---|---:|---|
| P1b | `depends_on = []` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| P5 | self dependency `[ack…]` | 1 | `self dependency 'acknowledgment-aru-records'` + `timeline inversion … tick 13 not before … tick 13` |
| P6 | repeated `[resp, resp]` | 1 | `repeated dependency 'response-evin-salt-court'` |
| P7 | ack `tick = 12` (equal) | 1 | `timeline inversion 'response-evin-salt-court' tick 12 not before 'acknowledgment-aru-records' tick 12` |
| P8 | `depends_on = ["paired-crossing-decision"]` (tick 10, earlier but the wrong edge) | 0 | `CLEAN … 0 violations` |
| P9 | remove terminal event `acknowledgment-aru-records` (nothing depends on it) | 0 | `CLEAN … 0 violations` |
| P10 | duplicate `response-evin-salt-court` | 1 | `duplicate timeline id 'response-evin-salt-court'` + `ambiguous dependency event 'response-evin-salt-court'` |

**Boundaries worth recording for adjudication.** `check_bible` enforces dependency key presence/type, id resolvability/uniqueness, self/repeat exclusion, and strict tick ordering (`dep >= row` fails, so equal ticks fail). It does **not** enforce that the dependency list is non-empty (P1b passes), that the edge names the *semantically correct* predecessor (P8 passes), or that a terminal event exists at all (P9 passes). So "the ack event depends on the response event" is a claim the checker can only partially police: it catches a dropped key, an unknown/ambiguous/self/repeated id, and any non-increasing tick — but an emptied list, a wrong-but-earlier edge, or a deleted terminal row all stay `CLEAN`. The map/README/census obligations (other seats) carry that half; my probes confirm the structural half holds on the delivered bytes.

Cross-check of the fixture the probes ride on (observed after R5's map landed, read-only):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS            (exit 0)
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -3
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS            (exit 0)
```

(The pre-R5 map was still the r96 byte-copy at my first probe run; that state is mid-flight, not a finding — the delivered map now maps `timeline.json#/5`.)

## Host condition

`/tmp` hit 100% inode exhaustion during this seat's run (`df -i /tmp` → `1048576 1048575 1 100% /tmp`; one probe run died with `OSError: [Errno 28] No space left on device: '/tmp/tmperqjgqx/fixture'`). Re-run with `TMPDIR` set to scratch, as r96 seats did. Recorded as a host condition, not a repo finding.

## Bottom line

**PASS** — on the delivered r97 revision (`timeline.json` `73063a86…`, checker `ff9fd2aa…`), baseline `check_bible` is CLEAN exit 0, and all four mandated dependency probes report exactly as expected: dropped `depends_on` → `required nonempty list` exit 1; unknown id → `unknown event` exit 1; tick 11 → `timeline inversion … tick 12 not before … tick 11` exit 1; removed response event → dangling edge reported as `unknown event` exit 1 (bounded: an emptied list, a wrong-but-earlier edge, or a deleted terminal row all stay CLEAN).
