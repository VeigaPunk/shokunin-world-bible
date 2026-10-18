# V86 c2-no-new-entity — round 99

Seat: V86. Task: confirm r99 adds zero entities, claims, and relations (`entities.json` byte-identical to r98's; relations byte-identical; map row-count delta exactly +1 event row). Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Working-tree HEAD at measurement: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (ahead of the baseline commit; r98 fixture files used below match the baseline blob). Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive write: this report. Scratch: `.ufo/waves/round-99/seats/V86-scratch/r98-blob/` (extracted baseline fixture, not a corpus write).

Axes for this seat: entity-record identity, claim-record identity, relation-record identity, map-row delta (must be exactly one new event row and no new claim or relation row). A pass requires all four; a miss on any is a fail.

## Poll

Artifacts were already on disk when this seat started: `corpus/fixtures/r99-window-lapse/` held all ten files, including `entities.json`, `relations.json`, and `claim-excerpt-map.md`.

Producer reports required for this check: S3 (JSON tables) and S4 (map).

- S3 report present and read in full: `.ufo/waves/round-99/seats/S3-fixture-author.md` (5069 bytes, mtime 22:01).
- S4 report was absent from the seats root on the first `S4*.md` glob (only archive copies under other seats' scratch). The next existence check, before any 20s sleep, found `.ufo/waves/round-99/seats/S4-fixture-docs.md` (9303 bytes, mtime 22:03). Read in full. No stall-escape. Not an all-reports poll, so ENDGAME self-subtraction did not apply.
- Conclusive measurements below were taken at 2026-10-17 22:09:34 -03, after both reports existed. The delivered map sha256 matches the digest S4 recorded.

S3's report says README and `claim-excerpt-map.md` were still r98 byte copies and that gates should be expected to see 20 rows until S4 lands. That was true of S3's write set at S3's report time. It is not the delivered tree: S4 rewrote the map, and the measurements below are of that delivered map (21 JSON-fact rows). Recorded as a stale producer note, not a current contradiction.

## Check 1 and 2 — entities.json and relations.json byte-identical to r98

Claims live in `entities.json` (`claims` arrays). There is no separate `claims.json`. Byte identity of `entities.json` is therefore the claim-record check as well as the entity-record check. Relations are `relations.json`.

Command (lane root):

```
date '+%Y-%m-%d %H:%M:%S %Z'
git rev-parse HEAD
git rev-parse 4265df5
cmp -s <(git show 4265df5:corpus/fixtures/r98-clerk-filing/entities.json) corpus/fixtures/r99-window-lapse/entities.json && echo 'entities.json IDENTICAL' || echo 'entities.json DIFFER'
cmp -s <(git show 4265df5:corpus/fixtures/r98-clerk-filing/relations.json) corpus/fixtures/r99-window-lapse/relations.json && echo 'relations.json IDENTICAL' || echo 'relations.json DIFFER'
sha256sum corpus/fixtures/r99-window-lapse/entities.json corpus/fixtures/r99-window-lapse/relations.json corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
git show 4265df5:corpus/fixtures/r98-clerk-filing/entities.json | sha256sum
git show 4265df5:corpus/fixtures/r98-clerk-filing/relations.json | sha256sum
wc -c corpus/fixtures/r99-window-lapse/entities.json corpus/fixtures/r99-window-lapse/relations.json
```

Observed:

```
2026-10-17 22:09:34 -03
337f0fa52b02626b7687eedbb2d99fab30446fe4
4265df5e86e4121bde4125b649b89bb1676676a5
entities.json IDENTICAL
relations.json IDENTICAL
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r99-window-lapse/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  -
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  -
1793 corpus/fixtures/r99-window-lapse/entities.json
 139 corpus/fixtures/r99-window-lapse/relations.json
```

Working-tree `corpus/fixtures/r98-clerk-filing/entities.json` and `relations.json` were also byte-identical to the same blob (checked in the earlier python comparison: `wt r98 entities == blob True`, `wt r98 relations == blob True`). `git diff --name-only 4265df5 -- corpus/fixtures/*/entities.json corpus/fixtures/*/relations.json corpus/fixtures/*/claim-excerpt-map.md` printed nothing. `git status --short -- corpus/fixtures` printed only `?? corpus/fixtures/r99-window-lapse/`. No other fixture's entity or relation table was edited.

Parsed inventory of the identical entity/relation files (same python comparison, before the 22:09 block): 6 entities (`aru`, `evin`, `quiet-rise`, `salt-court`, `chalk-stair`, `clerk-maren`), 6 nested claims (one per entity), 1 relation (`aru` → `evin`, type `agreed_co_stewardship_for_this_crossing`). Claim count r98 6, r99 6. Relation tuples equal.

## Check 3 — map row-count delta exactly +1 event row

Baseline map extracted from the blob, then both clusters run through the lane tool:

```
rm -rf .ufo/waves/round-99/seats/V86-scratch/r98-blob
mkdir -p .ufo/waves/round-99/seats/V86-scratch/r98-blob
git archive 4265df5 corpus/fixtures/r98-clerk-filing | tar -x --strip-components=3 -C .ufo/waves/round-99/seats/V86-scratch/r98-blob
python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/V86-scratch/r98-blob; echo EXIT:$?
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse; echo EXIT:$?
```

Observed:

```
-- r98 blob --
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
EXIT:0
-- r99 delivered --
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
EXIT:0
```

Raw and mapped obligation delta is 21 − 20 = 1. Editorial rows stay 2. Total mapped rows 22 → 23, the same +1.

Row classification of the `## JSON facts` tables (r98 from the extracted blob, r99 from the delivered map). Kind is taken from the pointer cell: `first_appearance`, `/claims/`, `relations.json#`, `timeline.json#`.

Observed:

```
r98 JSON 20 {'first_appearance': 6, 'claim': 6, 'relation': 1, 'event': 7}
r99 JSON 21 {'first_appearance': 6, 'claim': 6, 'relation': 1, 'event': 8}
r98 editorial ['S01', 'S02'] r99 editorial ['S01', 'S02']
JSON delta 1 editorial delta 0 total delta 1
only_new ['J21']
missing []
inherited pointer cells changed []
J21 kind event
J21 pointer `timeline.json#/7` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`)
J21 source `clerk-lapse-note`
inherited rows changed after namespace swap []
claim rows r98 6 r99 6
relation rows r98 1 r99 1
event rows r98 7 r99 8
first_appearance rows r98 6 r99 6
```

The single added map row is J21, an event row pointing at `timeline.json#/7`. No claim row, relation row, first-appearance row, or editorial row was added or removed. After replacing the token `r99-window-lapse` with `r98-clerk-filing`, inherited JSON-fact rows J01–J20 are cell-identical to the r98 map. The namespace token is path qualification, not a new entity, claim, or relation.

Raw class counts from the JSON tables (same earlier comparison; entities and relations byte-identical, so those classes cannot have moved):

```
raw class r98 {'first_appearance': 6, 'claim': 6, 'relation': 1, 'event': 7}
raw class r99 {'first_appearance': 6, 'claim': 6, 'relation': 1, 'event': 8}
timeline prefix equal True r98_n 7 r99_n 8
```

The appended timeline event does not introduce an entity or a relation:

```
new event {'id': 'clerk-lapse-recorded', 'tick': 15, 'entity_id': 'clerk-maren', 'place_id': 'chalk-stair', 'depends_on': ['clerk-filing-open'], 'description': 'At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.', 'source_id': 'clerk-lapse-note'}
new event entity_id in entities True
new event place_id in entities True
new event introduces no relation keys ['depends_on', 'description', 'entity_id', 'id', 'place_id', 'source_id', 'tick']
```

`clerk-maren` and `chalk-stair` are already in the byte-identical entity table. The event has no `claims` field and no relation fields. "No claim was lodged" is wording inside the event description, not a new claim record.

## Bounds

- Not checked here: C1 freeze pinning, C2 component 2 (blind-spot table), census 172→173, `check_bible`, `support_check`, whole-claim entailment. `map_obligations` was run only as the row-count gate.
- S4's map digest `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` matches the file measured at 22:09:34.
- No axis of this seat was harmed: entity file identical, claim records identical (inside that file; map claim rows 6→6), relation file identical, map delta is the one declared event row.

## Bottom line

PASS — r99 adds zero entities, claims, and relations: `entities.json` and `relations.json` are byte-identical to `4265df5` r98 (sha256 `db2d8e5d…` and `c279254b…`), and the map row-count delta is exactly +1 event row (J21 `timeline.json#/7`; claim rows 6→6, relation rows 1→1, editorial rows 2→2).
