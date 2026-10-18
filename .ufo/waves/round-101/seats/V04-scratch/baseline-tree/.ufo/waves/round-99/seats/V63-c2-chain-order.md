# V63 c2-chain-order — round 99

Seat: V63 c2-chain-order (verifier, leaf). Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline declared as r98 closure `4265df5`; working-tree HEAD during this seat `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa lore r99: record blocked dispatch attempt…`). Wave tree uncommitted. No nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V63-scratch/` only.

Axes checked (own enumeration, not the tool's verdict):

1. Tick span 9→15 across the chain fixtures.
2. Every `depends_on` strictly backward (target exists, target tick < dependent tick).
3. Freeze-pin edge sets equal raw JSON edge sets on all six pinned fixtures.

## 0. Poll-wait

Cadence 20 s, max 40. First poller (`V63-scratch/poll.sh`) was killed by the 300 s tool cap after try 15 (22:06:38); resumed as `poll2.sh` tries 16–40. Bounded stall-escape, recorded, not fatal. No plan was scored.

```
CHECK n=1  t=22:01:57 fixture=1 pins='r99 0 n 6 schema 1 files 0' s_reports=1 names=S3-fixture-author.md,
CHECK n=8  t=22:04:18 fixture=1 pins='r99 0 n 6 schema 2 files 0' s_reports=2 names=S3-fixture-author.md,S4-fixture-docs.md,
CHECK n=16 t=22:20:57 sha=8c2561b043c2 info='r99 0 n 6 schema 2 payload 2 r99files 0 tenfile_pins 6' s=S3-fixture-author.md,S4-fixture-docs.md,
CHECK n=40 t=22:28:58 sha=8c2561b043c2 info='r99 0 n 6 schema 2 payload 2 r99files 0 tenfile_pins 6' s=S3-fixture-author.md,S4-fixture-docs.md,
POLL_EXHAUSTED n=40 t=22:29:18
```

Contract sha `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` was stable from the schema-2 re-freeze (mtime 22:08:46) through the post-deadline recheck at 22:38:15. `S1*.md` was absent at try 40 and still absent at 22:32:57. S3 and S4 reports were present. Scoring below is against that stable contract and the fixture bytes, not against an S1 plan.

## 1. What "six" is on the delivered revision

The contract pins exactly six fixtures. There is no seventh pin.

```
$ python3 -c 'import json; c=json.load(open("corpus/tools/dependency-freeze-contract.json")); print(c.get("schema_version"), c.get("payload_schema_version"), list(c["pins"]))'
2 2 ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
```

Post-deadline (22:38:15) `sha256sum corpus/tools/dependency-freeze-contract.json` still `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Tool sha `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`.

`r99-window-lapse/timeline.json` exists and is the only fixture whose ticks reach 15. The arc that spans ticks 9→15 is seven directories (r88 through r99), not six. The only six that span 9→15 if r88 is dropped are r94–r99, and that set is not what the contract pins.

## 2. Raw ordering — ticks and strictly backward

Own reader (`V63-scratch/chain_order.py` and a second inline dump). Edge = `(depends_on target, dependent id)`. Backward means the target id exists in the same timeline and its tick is strictly less.

Terminal ticks of the seven timelines, row order:

| fixture | ticks | edges | backward |
|---|---|---|---|
| r88-m3-maya-cluster | 9, 9 | 0 | OK |
| r94-paired-crossing | 9, 9, 10 | 2 | OK |
| r95-crossing-aftermath | 9, 9, 10, 11 | 3 | OK |
| r96-crossing-response | 9, 9, 10, 11, 12 | 4 | OK |
| r97-crossing-acknowledgment | 9, 9, 10, 11, 12, 13 | 5 | OK |
| r98-clerk-filing | 9, 9, 10, 11, 12, 13, 14 | 6 | OK |
| r99-window-lapse | 9, 9, 10, 11, 12, 13, 14, 15 | 7 | OK |

Parsed-prefix chain (each timeline's leading events equal the previous fixture's full array):

```
r88-m3-maya-cluster -> r94-paired-crossing prefix_equal=True added=['paired-crossing-decision']
r94-paired-crossing -> r95-crossing-aftermath prefix_equal=True added=['aftermath-missing-evin']
r95-crossing-aftermath -> r96-crossing-response prefix_equal=True added=['response-evin-salt-court']
r96-crossing-response -> r97-crossing-acknowledgment prefix_equal=True added=['acknowledgment-aru-records']
r97-crossing-acknowledgment -> r98-clerk-filing prefix_equal=True added=['clerk-filing-open']
r98-clerk-filing -> r99-window-lapse prefix_equal=True added=['clerk-lapse-recorded']
```

New raw edge on r99, from `corpus/fixtures/r99-window-lapse/timeline.json`:

```
clerk-lapse-recorded tick=15 depends_on=['clerk-filing-open'] entity=clerk-maren place=chalk-stair
```

`clerk-filing-open` is tick 14 in the same file, so 14 < 15. No missing targets, no equal-tick edge, no forward edge, on any of the seven. The two tick-9 rows have `depends_on: []`.

`check_bible` on all seven (22:22:03, same bytes): each `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. That corroborates the ordering gate; it is not the pin comparison.

## 3. Pin edge sets vs raw JSON — six pinned fixtures MATCH

Independent of `dependency_freeze.py`: for each pin, the set of `(dep, event_id)` pairs taken from `pin["events"][*]["depends_on"]` equals the set taken from that fixture's `timeline.json`. Per-event `depends_on` equals `sorted(set(raw))`. Endpoints (`tick`, `entity_id`, `place_id`) match. No pin-only events, no raw-only events. Monotone along the pin chain: each pin adds edges and removes none (r88→r94 adds two; each later pin adds one).

```
r88  raw_edges []
     pin_edges []
     EDGE-SET MATCH   counts events=2 edges=0
r94  raw==pin [('aru-ninth-bell','paired-crossing-decision'), ('evin-ninth-bell','paired-crossing-decision')]
     EDGE-SET MATCH   edges=2
r95  added ('paired-crossing-decision','aftermath-missing-evin')  EDGE-SET MATCH  edges=3
r96  added ('aftermath-missing-evin','response-evin-salt-court')  EDGE-SET MATCH  edges=4
r97  added ('response-evin-salt-court','acknowledgment-aru-records')  EDGE-SET MATCH  edges=5
r98  added ('acknowledgment-aru-records','clerk-filing-open')  EDGE-SET MATCH  edges=6
r99  PIN ABSENT
     raw edges include ('clerk-filing-open','clerk-lapse-recorded')
```

Pin `files.timeline.json` equals `sha256` of the delivered timeline bytes (all six True):

```
r88 f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493
r94 f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c
r95 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177
r96 ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9
r97 73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b
r98 eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af
r99 timeline 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  (not in any pin)
```

Tool verify on the same contract (22:38:15), corroboration only — the edge-set claim above is the own enumeration:

```
### r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
exit=0
### r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
exit=0
### r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
exit=0
### r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
exit=0
### r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
exit=0
### r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
exit=0
```

## 4. Tick 15 is not frozen

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
r99_exit:2
```

Observed at 22:32:57 and unchanged at the 22:38:15 recheck (same contract sha). The tick-15 edge exists only in raw JSON. It is not in any pin's edge set. Same class as the r97 tick-13 edge before r98 pinned it: present in the fixture, invisible to the freeze gate.

No six-fixture set on this revision both spans ticks 9→15 and has pin edge sets matching raw JSON:

- The six pins (r88–r98) match raw edge sets and are strictly backward, but their ticks stop at 14.
- r94–r99 span 9→15 and are strictly backward in raw JSON, but r99 has no pin, so pin-match fails for that six.
- r88–r99 span 9→15 and are strictly backward, and that is seven fixtures, not six.

## 5. What this seat did not treat as a pass

S1's report never landed (ABSENT at try 40). C1's declaration text says the chain re-freezes 6/6; that 6/6 tool result is true of the six pins above and is not this seat's claim. This seat's claim is the conjunction ticks 9→15 and pin-match on all six. That conjunction is false on the delivered bytes. Not a plan: the contract and the r99 timeline were both on disk and stable.

Bottom line: FAIL — raw chain is ticks 9→15 with every depends_on strictly backward through r99, and the six freeze pins match raw edge sets, but those pins stop at tick 14; the tick-15 edge is unpinned (UNPINNED-FIXTURE exit 2).
