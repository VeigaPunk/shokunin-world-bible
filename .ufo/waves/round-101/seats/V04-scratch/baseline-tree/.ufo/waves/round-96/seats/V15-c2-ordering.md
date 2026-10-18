# V15 — c2-ordering (round 96)

Seat: V15 c2-ordering. Scope: verify the C2 depth claim's **chain ordering** on
`corpus/fixtures/r96-crossing-response/` — ticks `9,9,10,11,12` across
r88/r94/r95/r96, every `depends_on` strictly backward — and replay the r19/r20
semantic calibration classes (negative tick, negative endpoint) on scratch copies.
Leaf seat: no nested agents, no commits, no pushes, no network. Only writes:
this report (absolute path) and `.ufo/waves/round-96/seats/V15-scratch/`.

Baseline `dcb2d92` (r95 closure). Working-tree HEAD at verification time `60dba0c`
plus the round's uncommitted producer edits.

## 0. Revision pins

```
$ sha256sum corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response/timeline.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  corpus/fixtures/r96-crossing-response/timeline.json
```

`check_bible.py` is byte-unchanged from the r95-closure revision (`ff9fd2aa…`,
the pin reproduced in the r95 C9 watch row 4). All results below are on these bytes.

Delivered r96 fixture digests (stable across the producer's write window —
identical at 17:39 and 17:43 local):

```
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  timeline.json
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  fictional-excerpts.md
```

## 1. Poll-wait protocol (Q4)

`corpus/fixtures/r96-crossing-response/` and Q4's producer report
`.ufo/waves/round-96/seats/Q4-fixture-json.md` were both absent at seat start
(17:37). Poll cadence 20 s, script `.ufo/waves/round-96/seats/V15-scratch/poll.sh`:

```
try=1 fixture=0 report=0 17:38:43
try=2 fixture=1 report=0 17:39:03
...
try=10 fixture=1 report=0 17:41:43
try=11 fixture=1 report=1 17:42:03
READY
```

Fixture bytes landed at try 2; the producer report at try 11 (11 tries, ~3 min
20 s). All verification below ran **after** the report existed. No plan was
verified; nothing fabricated.

## 2. Chain ordering — CONFIRMED

`python3 .ufo/waves/round-96/seats/V15-scratch/order_probe.py <fixtures…>` (probe
reads `timeline.json`, checks every `depends_on` target exists and has a strictly
smaller tick):

```
--- corpus/fixtures/r88-m3-maya-cluster
ids/tick: aru-ninth-bell=9, evin-ninth-bell=9
tick-sequence: [9, 9]
backward-check: OK all deps strictly backward
edges:
--- corpus/fixtures/r94-paired-crossing
tick-sequence: [9, 9, 10]
backward-check: OK all deps strictly backward
edges: aru-ninth-bell->paired-crossing-decision, evin-ninth-bell->paired-crossing-decision
--- corpus/fixtures/r95-crossing-aftermath
tick-sequence: [9, 9, 10, 11]
backward-check: OK all deps strictly backward
edges: … paired-crossing-decision->aftermath-missing-evin
--- corpus/fixtures/r96-crossing-response
ids/tick: aru-ninth-bell=9, evin-ninth-bell=9, paired-crossing-decision=10,
          aftermath-missing-evin=11, response-evin-salt-court=12
tick-sequence: [9, 9, 10, 11, 12]
backward-check: OK all deps strictly backward
edges: … aftermath-missing-evin->response-evin-salt-court
```

- Claimed sequence `9,9,10,11,12` **holds exactly**, in row order and in tick order.
- The only new edge is `aftermath-missing-evin` (tick 11) → `response-evin-salt-court`
  (tick 12): strictly backward (11 < 12). No edge added or re-targeted elsewhere.
- Edge inventories are monotone along the chain: 0 → 2 → 3 → 4 edges; each fixture
  is a strict prefix-extension of its predecessor. Row-level parsed-value prefix
  equality checked explicitly: r94[:2]==r88, r95[:3]==r94, r96[:4]==r95 — all `True`.
  So the inherited ordering is inherited, not re-authored.

`check_bible` on the delivered fixture:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

No double-booking introduced: `evin` appears at tick 9 (salt-court, r88 row) and
tick 12 (salt-court); the occupancy slot is `(entity_id, tick)`, so ticks 9≠12 do
not collide, and the CLEAN exit 0 confirms it.

## 3. Byte-copy preservation (supporting the ordering claim)

All five spec'd byte copies hash-match `dcb2d92` r95 bytes (via `git show`):

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/$f | sha256sum  # == delivered
entities.json      SAME 026af0bc…
relations.json     SAME c279254b…
contradictions.json SAME 37517e5f…
inspiration-note.md SAME 58f5390e…
source-excerpt.md  SAME b5edc2fd…
```

`contradictions.json` is `[]` (3 bytes) — no contradiction asserted, matching the
"UNRESOLVED, no winner" framing. Sources 4 → 5 (`evin-response-note` appended;
the four inherited source rows are parsed-value identical). Timeline 4 → 5 events.

## 4. r19/r20 semantic probes replayed (calibration classes reproduce)

Scratch copies under `.ufo/waves/round-96/seats/V15-scratch/probes/`, run with the
pinned `check_bible.py`:

| fixture | exit | observed |
|---|---|---|
| r19-negative-tick | 1 | two `must be nonnegative`; no double-booked |
| r19-negative-first-valid | 1 | nonnegative + tick-9 double-booked (valid pair retained) |
| r19-valid-around-negative | 1 | nonnegative + tick-9 double-booked (valid pair retained) |
| r19-valid-tick | 1 | tick-9 double-booked only (positive control) |
| r20-both-negative | 1 | two `must be nonnegative`; no inversion |
| r20-negative-dependent | 1 | nonnegative only; **no inversion** |
| r20-negative-prereq | 1 | nonnegative only; **no inversion** |
| r20-mixed-edges | 1 | nonnegative + valid-to-valid inversion retained |
| r20-valid-order | 0 | CLEAN |
| r20-valid-equal | 1 | double-booked + equal-tick inversion |
| r20-valid-inversion | 1 | inversion `tick 2 not before … tick 1` |

Both prior classes reproduce exactly: (a) negative tick is reported and the
negative-tick row is excluded from occupancy; (b) the dependency comparison is
**gated** by nonnegative ticks — a negative endpoint yields the nonnegative finding
and no spurious inversion, while a valid-tick inversion still fires.

**Chain-level injection (stronger form, same classes on r96 bytes).** Mutated
scratch copies of the delivered fixture (`chain2/`), one field each:

```
=== chain2/neg-tick      (response-evin-salt-court tick 12 → -1)
VIOLATION: timeline[4].tick: must be nonnegative
exit=1
=== chain2/neg-endpoint  (aftermath-missing-evin tick 11 → -1)
VIOLATION: timeline[3].tick: must be nonnegative
exit=1
=== chain2/inversion     (aftermath-missing-evin tick 11 → 12)
VIOLATION: timeline[4].depends_on: timeline inversion 'aftermath-missing-evin' tick 12 not before 'response-evin-salt-court' tick 12
exit=1
```

The negative-endpoint case emits **only** the nonnegative finding — no inversion
against `response-evin-salt-court` — confirming the gate holds on the new edge.
The inversion case confirms the new edge is genuinely load-bearing for the
ordering rule, not decorative.

## 5. Observations (non-blocking, not defects against C2)

- `sources.json` formatting: the appended fifth object is preceded by a line
  containing only `  ,` (`}\n,\n  {`). Valid JSON, parses cleanly, `check_bible`
  exit 0; the same quirk is visible in Q4's own diff (`24a25,30`). Cosmetic only —
  worth a tidy if `sources.json` is ever re-frozen, no action required for C2.
- Scope note: this seat verified **input-structural** ordering and checker
  behavior. It asserts nothing about source-text chronology or canon truth; the
  fixture descriptions and excerpts are explicitly input-scoped, and I did not
  read them as world facts.

## Bottom line

**PASS** — on the frozen r96 revision (`timeline.json ea0225f9…`, `check_bible.py
ff9fd2aa…`), the chain ticks are exactly `9,9,10,11,12` with every `depends_on`
strictly backward and `check_bible` CLEAN exit 0, and both r19/r20 calibration
classes (negative tick; nonnegative-gated endpoint comparison) reproduce on
scratch copies including chain-level injections.
