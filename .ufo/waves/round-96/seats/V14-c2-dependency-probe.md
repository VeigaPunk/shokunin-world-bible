# V14 — c2-dependency-probe (round 96)

Seat: V14 c2-dependency-probe. Scope: poll for Q4's
`corpus/fixtures/r96-crossing-response/`, then probe the dependency behaviors
of `corpus/fixtures/check_bible.py` on **scratch copies only** (live tree
untouched). Probes per brief: drop `depends_on`; unknown id; tick 11 on the
response event; remove the aftermath event row. Absolute paths used
throughout; no commits; no network.

Checker revision under test: `corpus/fixtures/check_bible.py` sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
(identical to the revision pinned in Q4's report).

## Poll protocol (20 s cadence)

Driver log `.ufo/waves/round-96/seats/V14-scratch/driver.log`:

```
try 1: absent (ok=1 q4report=none) 2026-10-17T20:39:24Z
...
try 8: absent (ok=1 q4report=none) 2026-10-17T20:41:44Z
FOUND at try 9 (2026-10-17T20:42:04Z); Q4 report: .../seats/Q4-fixture-json.md
```

All 8 Q4 fixture files were already on disk by try 1; polling continued per
protocol until Q4's producer report landed at try 9 (20:42:04Z). Target
verified only after the report existed.

## Target evidence

sha256 of delivered files (from driver.log):

```
026af0bc…  entities.json        c279254b…  relations.json
37517e5f…  contradictions.json  58f5390e…  inspiration-note.md
b5edc2fd…  source-excerpt.md    9f973f63…  sources.json
ea0225f9…  timeline.json        06b11bec…  fictional-excerpts.md
```

Counts (json row counts): `entities: 5`, `relations: 1`, `timeline: 5`,
`sources: 5`, `contradictions: 0` — matches C2's 5/1/5 and 5 sources.
Census: `ls -d corpus/fixtures/*/ | wc -l` → `170` (169→170 confirmed).

Preserving-copy check (r95 vs r96):

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r95-crossing-aftermath/$f r96-crossing-response/$f && echo IDENTICAL $f || echo DIFFERS $f; done
IDENTICAL entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md

$ diff r95-crossing-aftermath/timeline.json r96-crossing-response/timeline.json
41a42,52
>   }, { "id": "response-evin-salt-court", "tick": 12, "entity_id": "evin",
>     "place_id": "salt-court", "depends_on": ["aftermath-missing-evin"],
>     "source_id": "evin-response-note", ... }
diff-exit=1
```

Only an appended event; no inherited row changed (all additions, no
deletions/modifications).

## Control — pristine copy

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-96/seats/V14-scratch/ctrl-pristine
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

## Probes (each on a fresh scratch copy; live tree untouched)

Mutation mechanics: JSON load of `timeline.json`, edit
`response-evin-salt-court`, rewrite (idempotent copies under
`.ufo/waves/round-96/seats/V14-scratch/`).

**P1a — `depends_on` key removed:**

```
VIOLATION: timeline[4].depends_on: required nonempty list
1 violation(s); no canon changed
exit=1
```

**P1b — `depends_on` emptied to `[]` (the value-level drop):**

```
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Finding: check_bible cannot see a dropped dependency *edge* when the key is
present but empty. This is exactly the carried BR-01 blind spot; C2's claim
"check_bible CLEAN" is not affected (the delivered fixture is genuinely
CLEAN), but a reduction-only mutation of the response edge stays green here.

**P2 — unknown dependency id (`aftermath-missing-evin-missing`):**

```
VIOLATION: timeline[4].depends_on: unknown event 'aftermath-missing-evin-missing'
1 violation(s); no canon changed
exit=1
```

**P3 — response event tick 12 → 11 (inversion):**

```
VIOLATION: timeline[4].depends_on: timeline inversion 'aftermath-missing-evin' tick 11 not before 'response-evin-salt-court' tick 11
1 violation(s); no canon changed
exit=1
```

**P4 — aftermath event row removed (dangling dependency):**

```
VIOLATION: timeline[3].depends_on: unknown event 'aftermath-missing-evin'
1 violation(s); no canon changed
exit=1
```

(Index shifts to `timeline[3]` after removal; checker vocabulary for this
class is "unknown event", not "dangling".)

## Cross-evidence — freeze gate catches P1b

`corpus/tools/dependency_freeze.py` sha256 `f4b5208f…`, contract sha256
`2601c18a…` (pins: r88-m3-maya-cluster, r94-paired-crossing,
r95-crossing-aftermath, r96-crossing-response). The tool keys pins by
directory basename, so scratch copies were laid out as
`…/freeze-probe/{ctrl,red}/r96-crossing-response/`:

```
$ python3 corpus/tools/dependency_freeze.py …/freeze-probe/ctrl/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
exit=0

$ python3 corpus/tools/dependency_freeze.py …/freeze-probe/red/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 3/4; relations 1/1
FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']
RESULT FAIL
exit=1
```

P1b (check_bible CLEAN) is the same mutation the freeze gate reports as
REDUCTION-DETECTED — the blind spot is real and the new gate closes it for
the r96 fixture. Unpinned-basename runs exit 2 with `FINDING
UNPINNED-FIXTURE` (observed on my first attempt).

## Live-tree integrity

```
$ git status --short
 M LOG.md
?? .ufo/waves/round-96/
?? corpus/fixtures/r96-crossing-response/
?? corpus/tools/dependency-freeze-contract.json
?? corpus/tools/dependency_freeze.py

$ sha256sum corpus/fixtures/r96-crossing-response/timeline.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  (== pre-probe digest)
```

No probe touched the live fixture; all mutations confined to
`.ufo/waves/round-96/seats/V14-scratch/`.

## Notes / limits

- Seat scope is dependency-behavior probing only; C2's map-obligation count
  (16 rows), README/claim-excerpt-map, and Q6 note were not verified here.
- Q1/Q2 hardening of `map_obligations` was not yet on disk at 20:43Z
  (`git status` shows no modification) — not this seat's target.
- P1a/P1b together: field-presence is enforced, field-value reduction is
  not (by check_bible); both quoted verbatim above.

**Bottom line: PASS** — Q4 target delivered and polled to producer report;
all four dependency probe classes behave as documented (key-drop, unknown
id, tick inversion, row-removal each exit 1 with quoted findings), with one
confirmed blind spot (empty `depends_on` stays CLEAN) that the C3 freeze
gate demonstrably catches; live tree untouched.
