# V16 c3-dependency-probe — round 98 seat report

- Seat: V16 (verifier, C3 dependency probes). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `9a3d648`; all commands run from the lane repo root with `python3`.
- Producer polled: **S3** (`S3-fixture-author.md` + `corpus/fixtures/r98-clerk-filing/**`). Two background polls, 20 s cadence. Poll 1 (dir presence): `FOUND at try 4 20:28:38` — but that state was still the raw r97 byte-copy (`timeline.json` 2173 bytes, `grep -c clerk-filing-open` → 0), so artifact presence alone was not accepted as delivery. Poll 2 (authored revision: clerk event present AND S3 report present): `HIT try=8 ev=1 report=yes 20:31:16` — within the 40-try budget. Verdict bound to the delivered revision.
- Scratch (mine, absolute): `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V16-scratch/` (`probe.py`, `probe-run-final.txt`, `tmp/`, `r95-baseline/`). No commits, no pushes, no network; the live fixture was never modified (every mutation ran on a `shutil.copytree` copy under scratch `TMPDIR`).

## Binding evidence (delivered revision)

```
$ sha256sum corpus/fixtures/r98-clerk-filing/{timeline,entities,sources}.json corpus/fixtures/check_bible.py
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ stat -c '%y' corpus/fixtures/r98-clerk-filing/timeline.json
2026-10-17 20:28:55.985040083 -0300
```

The three tables were byte-stable from 20:28:55 through the final probe run (two `sha256sum` sets 15 s apart, identical; S3's report landed 20:31:16 after the last table write). `check_bible.py` is byte-identical to the closure revision (`git show 9a3d648:corpus/fixtures/check_bible.py | sha256sum` → same `ff9fd2aa…`). Mid-flight observation recorded, not a finding: between 20:28:38 and 20:28:55 the r98 tables were the raw r97 copy and the clerk event had not yet landed — S3's copy-then-extend order is consistent with what I observed.

Probed shape (delivered `timeline.json`, index 6 = the new event):

```json
{ "id": "clerk-filing-open", "tick": 14, "entity_id": "clerk-maren", "place_id": "chalk-stair",
  "depends_on": ["acknowledgment-aru-records"],
  "description": "At the Chalk Stair at tick 14, the clerk filed both pending accounts and recorded the matter OPEN, asserting no finding and no resolution.",
  "source_id": "clerk-filing-note" }
```

Inherited continuity (context, read-only): `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical to r97 (`cmp -s` → IDENTICAL each); parsed arrays of `timeline.json`, `entities.json`, `sources.json` are exactly the r97 arrays plus the appended rows (`inherited prefix equal: True` for all three; 5/1/6 → 6/1/7, sources 6 → 7). So every probe below mutates exactly one thing in the delivered revision.

## Probe battery (commands and observed outputs)

Harness: `TMPDIR=…/V16-scratch/tmp python3 .ufo/waves/round-98/seats/V16-scratch/probe.py corpus/fixtures/r98-clerk-filing` — copies the delivered fixture to a scratch temp tree, applies one mutation to `timeline.json`, then runs `python3 corpus/fixtures/check_bible.py <copy>`. Full transcript: `.ufo/waves/round-98/seats/V16-scratch/probe-run-final.txt`.

Baseline on the live (unmutated) delivered fixture:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Mandated probes:

| # | Mutation | Exit | Checker output (verbatim) |
|---|---|---:|---|
| P1 | drop `depends_on` key from `clerk-filing-open` | 1 | `VIOLATION: timeline[6].depends_on: required nonempty list` |
| P2 | `depends_on = ["no-such-event-id"]` | 1 | `VIOLATION: timeline[6].depends_on: unknown event 'no-such-event-id'` |
| P3 | clerk event `tick = 13` (dependency stays tick 13) | 1 | `VIOLATION: timeline[6].depends_on: timeline inversion 'acknowledgment-aru-records' tick 13 not before 'clerk-filing-open' tick 13` |
| P4 | remove event `acknowledgment-aru-records` | 1 | `VIOLATION: timeline[5].depends_on: unknown event 'acknowledgment-aru-records'` |

All four mandated probes report as expected on the delivered revision. The seat-requested "dangling" case is reported by the checker as `unknown event` (its dangling-reference wording is reserved for entity references — P11 below); the dependency edge dangles exactly as intended. Note the P4 mechanism changed vs r97: there the acknowledgment event was terminal and removing it stayed CLEAN; here it is the clerk event's predecessor, so its removal is now caught — the fourth beat is what makes that edge load-bearing.

Extra probes run in the same battery (discrimination boundary, not defects):

| # | Mutation | Exit | Output |
|---|---|---:|---|
| P0 | none (control) | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| P5 | `depends_on = []` | 0 | `CLEAN … 0 violations` |
| P6 | self dependency `[clerk-filing-open]` | 1 | `timeline[6].depends_on[0]: self dependency 'clerk-filing-open'` + `timeline inversion 'clerk-filing-open' tick 14 not before 'clerk-filing-open' tick 14` |
| P7 | repeated `[ack, ack]` | 1 | `timeline[6].depends_on[1]: repeated dependency 'acknowledgment-aru-records'` |
| P8 | `depends_on = ["response-evin-salt-court"]` (tick 12, earlier but the wrong edge) | 0 | `CLEAN … 0 violations` |
| P9 | remove terminal event `clerk-filing-open` (nothing depends on it) | 0 | `CLEAN … 0 violations` |
| P10 | duplicate `clerk-filing-open` row | 1 | `timeline[7].id: duplicate timeline id 'clerk-filing-open'` |
| P11 | remove entity `clerk-maren` | 1 | `timeline[6].entity_id: dangling entity 'clerk-maren'` |
| P12 | remove source `clerk-filing-note` | 1 | `entities[5].first_appearance: unknown in-world source 'clerk-filing-note'` + `entities[5].claims[0].source_id: …` + `timeline[6].source_id: …` (3 violations) |

P11/P12 ran inline (same copy-then-mutate method, entities/sources tables instead of timeline).

**Boundaries worth recording for adjudication.** `check_bible` enforces dependency key presence/type, id resolvability/uniqueness, self/repeat exclusion, and strict tick ordering (`dep >= row` fails, so equal ticks fail; P3). It does **not** enforce that the dependency list is non-empty (P5 passes), that the edge names the *semantically correct* predecessor (P8 passes), or that a terminal event exists at all (P9 passes). So "the clerk event depends on the acknowledgment event" is a claim the checker can only partially police: it catches a dropped key, an unknown/ambiguous/self/repeated id, and any non-increasing tick — but an emptied list, a wrong-but-earlier edge, or a deleted terminal row all stay `CLEAN`. The map/README/census obligations (other seats) carry that half; my probes confirm the structural half holds on the delivered bytes.

## Cross-check context (bounded, read-only, at my read times)

r95 repair half (S3's other ownership): the whole-file diff vs `9a3d648` is exactly one line (`49c49`, the carried-wording repair), and receipts reproduce unchanged by independent re-run — baseline cluster extracted via `git archive 9a3d648 corpus/fixtures/r95-crossing-aftermath` into scratch:

```
$ python3 corpus/tools/map_obligations.py <baseline>/r95-crossing-aftermath | tail -2   → INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; RESULT PASS
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath | tail -2 → same receipt
$ python3 corpus/tools/support_check.py <baseline>/r95-crossing-aftermath | tail -2     → SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17; RESULT PASS
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath | tail -2  → same receipt
```

Delivered r98 map (S4, landed 20:30:21 — before S3's report): `map_obligations` → `OBLIGATIONS raw=20 mapped=20; INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; RESULT PASS`; `support_check` → `RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22` / `SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22` / `RESULT PASS` (an earlier mid-flight run on the pre-S4 placeholder copy read 17/17 — that state was not a finding). `dependency_freeze` at my final read still listed only `['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']` — r97/r98 pins (S1/C2) had not landed; recorded as pending producer state, not a C3 finding.

## Host condition

None observed in this seat. Scratch `TMPDIR` was set proactively (r96/r97 `/tmp` inode-exhaustion class did not recur here; no `Errno 28`).

## Bottom line

**PASS** — on the delivered r98 revision (`timeline.json` `eb24e084…`, `entities.json` `db2d8e5d…`, `sources.json` `32ee15b1…`, checker `ff9fd2aa…` byte-identical to closure), baseline `check_bible` is CLEAN exit 0, and all four mandated dependency probes report exactly as expected: dropped `depends_on` → `required nonempty list` exit 1; unknown id → `unknown event` exit 1; tick 13 → `timeline inversion … tick 13 not before … tick 13` exit 1; removed acknowledgment event → dangling edge reported as `unknown event` exit 1 (bounded: an emptied list, a wrong-but-earlier edge, or a deleted terminal row all stay CLEAN; the r95 repair receipts and the r98 map 20/20 reproduce independently).
