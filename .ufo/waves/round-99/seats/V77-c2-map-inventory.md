# V77 c2-map-inventory — r99 raw obligations

Seat: V77. Leaf verifier. No commits, no corpus writes. Scratch parser only: `.ufo/waves/round-99/seats/V77-scratch/enumerate_obligations.py` (does not import `map_obligations.py`). Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`.

Claim checked: C2 component 1 says 21 map obligations = 20 inherited rows + 1 new event row, and the new row's pointer / anchor / source-ID triple is the tick-15 lapse event.

## Poll

- First look: `corpus/fixtures/r99-window-lapse/` absent; no seat reports. Slept 20s.
- Poll 2 (22:01:59): directory present. `timeline.json` already had 8 events including `clerk-lapse-recorded`. `claim-excerpt-map.md` was still the r98 byte copy (`**Expected inventory:** 20 JSON facts`). `S3-fixture-author.md` present (5069 bytes). `S4` report absent. Did not count that map.
- Poll 3 (22:03:01): map rewritten (17119 bytes, mtime 22:02:39). Inventory line now `21 JSON facts`. J21 present. S4 report still absent.
- Poll 4 (22:03:25): map mtime unchanged. S4 report still absent. JSON tables stable (`timeline.json` mtime 22:01:13). Counted the delivered map rather than waiting on the producer narrative.
- Before this report was written, `S4-fixture-docs.md` had landed (9303 bytes, mtime 22:03). Both producer reports exist. No stall-escape. No ABSENT.

## Independent raw enumeration

Grammar used (contract `corpus/tools/map-obligations-contract.json`, reimplemented, not imported): one obligation per entity `first_appearance`, one per entity claim, one per relation record, one per timeline record. `sources.json` is not a raw-obligation file. Editorial rows are not raw obligations.

```
$ python3 .ufo/waves/round-99/seats/V77-scratch/enumerate_obligations.py corpus/fixtures/r99-window-lapse
INDEPENDENT raw=21 mapped_rows=21
KINDS first_appearance=6 claim=6 relation=1 event=8
MISSING []
PHANTOM []
```

The 21 raw pointers and bound source IDs:

| kind | pointer | source_id | label |
|---|---|---|---|
| first_appearance | `entities.json#/0/first_appearance` | `paired-clock` | aru |
| claim | `entities.json#/0/claims/0` | `paired-clock` | aru |
| first_appearance | `entities.json#/1/first_appearance` | `paired-clock` | evin |
| claim | `entities.json#/1/claims/0` | `paired-clock` | evin |
| first_appearance | `entities.json#/2/first_appearance` | `paired-clock` | quiet-rise |
| claim | `entities.json#/2/claims/0` | `paired-clock` | quiet-rise |
| first_appearance | `entities.json#/3/first_appearance` | `paired-clock` | salt-court |
| claim | `entities.json#/3/claims/0` | `paired-clock` | salt-court |
| first_appearance | `entities.json#/4/first_appearance` | `crossing-minute` | chalk-stair |
| claim | `entities.json#/4/claims/0` | `crossing-minute` | chalk-stair |
| first_appearance | `entities.json#/5/first_appearance` | `clerk-filing-note` | clerk-maren |
| claim | `entities.json#/5/claims/0` | `clerk-filing-note` | clerk-maren |
| relation | `relations.json#/0` | `crossing-minute` | agreed_co_stewardship_for_this_crossing |
| event | `timeline.json#/0` | `paired-clock` | aru-ninth-bell |
| event | `timeline.json#/1` | `paired-clock` | evin-ninth-bell |
| event | `timeline.json#/2` | `crossing-minute` | paired-crossing-decision |
| event | `timeline.json#/3` | `aru-aftermath-note` | aftermath-missing-evin |
| event | `timeline.json#/4` | `evin-response-note` | response-evin-salt-court |
| event | `timeline.json#/5` | `aru-acknowledgment-note` | acknowledgment-aru-records |
| event | `timeline.json#/6` | `clerk-filing-note` | clerk-filing-open |
| event | `timeline.json#/7` | `clerk-lapse-note` | clerk-lapse-recorded |

Every map row J01–J21 bound to that source ID (`BIND-OK` on all 21). No missing raw pointer, no phantom map pointer.

Why 20+1 and not a reshuffle:

```
r98_events=7 r99_events=8 prefix_equal=True new_id=clerk-lapse-recorded new_source=clerk-lapse-note
entities_equal=True relations_equal=True
```

`entities.json` and `relations.json` are equal to r98, so they still contribute 6+6+1 = 13. Timeline contributes 7 inherited + 1 new = 8. Total 21. The only new raw obligation is `timeline.json#/7`.

r98 control with the same parser: `INDEPENDENT raw=20 mapped_rows=20`.

## Tool count

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
map_exit:0
```

Independent raw count 21 equals the tool's `raw=21`. Mapped rows also 21. The inventory line's 21 JSON facts agree. Editorial rows stay 2 (not part of the 21). Total mapped rows 23 = 21 facts + 2 editorial. r98 control on the same tool: `OBLIGATIONS raw=20 mapped=20` / `RESULT PASS` / exit 0.

Declared map line (file line 5): `**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.` Section heading: `## JSON facts (21 canonical pointers)`.

## Inherited rows

J01–J20 pointer, in-world source ID, excerpt path, span, and exact anchor are identical to the r98 map. Diff count on those five fields: 0. The only inherited-cell change is the path-qualified namespace (`r98-clerk-filing:` → `r99-window-lapse:`), 20/20 rows. New row id is only `J21`, appended at map line 42 (inherited rows stay on lines 22–41).

## J21 triple

Map row (line 42):

`| J21 | timeline.json#/7 (tick, entity_id, place_id, depends_on, description, source_id) | clerk-lapse-note | r99-window-lapse:clerk-lapse-note | fictional-excerpts.md | 66-76 | verbatim | Tick 15: The crossing-window named in the original minute has closed. |`

Pointer. `timeline.json` index 7 is the eighth event (0-based), and the r98 prefix is the first seven. Resolved record:

```
{"id": "clerk-lapse-recorded", "tick": 15, "entity_id": "clerk-maren", "place_id": "chalk-stair", "depends_on": ["clerk-filing-open"], "description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.", "source_id": "clerk-lapse-note"}
```

That matches the declaration (tick-15 `clerk-lapse-recorded`, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`).

Source ID. Cell `clerk-lapse-note` equals `timeline[7].source_id`. It is also a `sources.json` id (8th source, after the seven inherited ids). Path-qualified cell is `r99-window-lapse:clerk-lapse-note`.

Anchor. Exact cell text `Tick 15: The crossing-window named in the original minute has closed.` occurs once in `fictional-excerpts.md`, at line 70, inside the declared span 66–76 and inside no inherited span:

```
$ grep -nF -- "Tick 15: The crossing-window named in the original minute has closed." corpus/fixtures/r99-window-lapse/fictional-excerpts.md
70:> Tick 15: The crossing-window named in the original minute has closed.
```

`support_check` accepts that triple (lexical anchor check, not entailment):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
support_exit:0
```

## Bytes checked

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r99-window-lapse/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
```

Map sha256 matches the hash S4 recorded. S3's report said the map was still the r98 20-row copy; that was true at S3's write time and is stale against these bytes.

Not measured here: census 172→173, freeze pins, whole-claim entailment.

PASS: independent raw obligations = 21 = tool `raw=21` (exit 0); 20 inherited + 1 new event; J21 pointer `timeline.json#/7` / source ID `clerk-lapse-note` / anchor at excerpt line 70 inside span 66-76 are correct.
