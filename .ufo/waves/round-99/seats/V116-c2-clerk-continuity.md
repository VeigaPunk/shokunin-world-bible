# V116 — c2-clerk-actor-continuity (round 99)

- **Seat:** V116 c2-clerk-actor-continuity (verifier). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands below ran from that root with `python3` unless noted. No commits, no pushes, no network, no nested agents. Exclusive write: this report. No scratch files.
- **Axis under test:** C2 depth, actor-continuity slice only. Not a gate-replay seat and not a census seat.
- **Question:** are clerk-maren's r98 and r99 rows parsed-identical, with the same source-id discipline (`first_appearance` unchanged; `clerk-lapse-note` only on r99's new rows)?
- **Baseline:** r98 closure `4265df5` = `4265df5e86e4121bde4125b649b89bb1676676a5` (`git rev-parse 4265df5`). Working-tree `corpus/fixtures/r98-clerk-filing/` matched that blob for every clerk file measured (entities, timeline, sources, relations, contradictions, map, README, fictional-excerpts). r99 was compared to those baseline blobs, not to a plan.
- **Poll-wait:** S3 report `/.ufo/waves/round-99/seats/S3-fixture-author.md` was already present (5,069 bytes, mtime 22:01 local). The first read of `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` was still the r98 placeholder (title "r98 clerk-filing", 20 obligations). That placeholder was not treated as the delivered map. S4 report `S4-fixture-docs.md` was present before the final battery (9,303 bytes, mtime 22:03 local), and the map/README hashes below are the post-S4 bytes. S1/S2/S5 were not required for this slice; `corpus/knowledge/r99-*` was absent at report time and was not verified. No stall-escape. Producer prose was cross-checked after the measurements, not used as evidence.

## Delivered hashes (this seat, final battery)

| file | sha256 |
|---|---|
| r98 and r99 `entities.json` (byte-identical) | `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` |
| r99 `timeline.json` | `2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069` |
| r99 `sources.json` | `8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15` |
| r99 `claim-excerpt-map.md` | `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` |

## What was compared

clerk-maren's r98 rows, against baseline `4265df5:corpus/fixtures/r98-clerk-filing/`:

- entity object `id=clerk-maren` (index 5): `kind`, `name`, `first_appearance`, and the single claim
- inherited timeline event `clerk-filing-open` (`entity_id` `clerk-maren`)
- inherited source object `clerk-filing-note` (the id `first_appearance` points at)
- map obligation rows J18, J19, J20 (the three r98 clerk rows)

r99's new rows, which must be the only carriers of `clerk-lapse-note`:

- appended source object
- appended timeline event `clerk-lapse-recorded`
- appended map row J21

## Commands and observed output

`git rev-parse 4265df5` → `4265df5e86e4121bde4125b649b89bb1676676a5`.

Final comparison (lane root, `python3` heredoc: `json.loads` of `git show 4265df5:corpus/fixtures/r98-clerk-filing/{entities,timeline,sources}.json` versus the r99 working-tree files; map J-rows split on `|`; `clerk-lapse-note` walked as a string hit). Observed flags, exit 0:

```
ENTITY_PARSED_IDENTICAL True
ENTITY_BYTE_FILE_IDENTICAL True
ENTITY_INDEX [5] [5]
ENTITY_SHA db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
FIRST_APPEARANCE clerk-filing-note clerk-filing-note
CLAIM_SOURCES ['clerk-filing-note'] ['clerk-filing-note']
CLAIM_COUNT 1 1
FILING_EVENT_PARSED_IDENTICAL True
FILING_SOURCE clerk-filing-note clerk-filing-note clerk-maren clerk-maren
TIMELINE_PREFIX_EQUAL True lens 7 8
NEW_EVENTS [('clerk-lapse-recorded', 'clerk-maren', 'clerk-lapse-note', 15)]
FILING_SOURCE_PARSED_IDENTICAL True
SOURCE_PREFIX_EQUAL True new ['clerk-lapse-note']
LAPSE_IN_ENTITIES []
LAPSE_IN_INHERITED_TIMELINE []
LAPSE_IN_NEW_TIMELINE ['$[0].source_id']
LAPSE_IN_INHERITED_SOURCES []
LAPSE_IN_NEW_SOURCES ['$[0].id']
LAPSE_IN_RELATIONS []
LAPSE_IN_CONTRADICTIONS []
FIRST_APPEARANCE_IS_LAPSE []
CLAIMS_CITING_LAPSE []
MAP_COUNTS 20 21
J18 lines 39 39 source_equal True rest_equal True ns `r98-clerk-filing:clerk-filing-note` `r99-window-lapse:clerk-filing-note`
J19 lines 40 40 source_equal True rest_equal True ns `r98-clerk-filing:clerk-filing-note` `r99-window-lapse:clerk-filing-note`
J20 lines 41 41 source_equal True rest_equal True ns `r98-clerk-filing:clerk-filing-note` `r99-window-lapse:clerk-filing-note`
J21_SOURCE `clerk-lapse-note` line 42
INHERITED_J_ROWS_CITING_LAPSE []
EXCERPT_PREFIX True lapse_in_prefix False lapse_in_suffix 1
FILING_SECTION_LINES_55_64_EQUAL True
R98_WORKTREE_EQ_BASELINE_ENTITIES True
VERDICT_FLAGS_OK
```

The entity object on both sides is:

```json
{
  "id": "clerk-maren",
  "kind": "character",
  "name": "Maren",
  "first_appearance": "clerk-filing-note",
  "claims": [
    {
      "statement": "The filing note names Maren, the clerk of the Chalk Stair registry, as the officer who filed both pending accounts.",
      "source_id": "clerk-filing-note"
    }
  ]
}
```

Checker, same root:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
MAP_EXIT:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
MAP98_EXIT:0
```

## Findings

1. **Entity row parsed-identical.** `entities.json` is byte-identical to the baseline r98 file (sha `db2d8e5d…`). One `clerk-maren` object, still index 5. `kind` `character`, `name` `Maren`, one claim, claim `source_id` `clerk-filing-note`. No second clerk entity. No claim cites `clerk-lapse-note`.

2. **`first_appearance` unchanged.** Both sides: `clerk-filing-note`. No entity's `first_appearance` is `clerk-lapse-note`. The r98 filing section of `fictional-excerpts.md` (lines 55–64, including the self-naming sentence the map anchors at line 60) is byte-equal to the baseline prefix. The r99 file startswith that baseline excerpt (`EXCERPT_PREFIX True`); `clerk-lapse-note` occurs once, in the appended suffix only.

3. **Inherited actor event parsed-identical.** `clerk-filing-open` matches the baseline object: tick 14, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["acknowledgment-aru-records"]`, `source_id` `clerk-filing-note`. Timeline prefix `t99[:-1] == t98` (7 events). The only appended event is `clerk-lapse-recorded` (tick 15, same `entity_id` `clerk-maren`, `source_id` `clerk-lapse-note`). Reusing the existing actor id on the new event is continuity, not a new clerk.

4. **Inherited source object parsed-identical.** `clerk-filing-note` matches the baseline source object. Sources prefix equal; the only appended source id is `clerk-lapse-note`.

5. **Source-id discipline on rows.** String walk of the parsed JSON: `clerk-lapse-note` is absent from entities, relations, contradictions, the inherited timeline prefix, and the inherited sources prefix. The only JSON hits are the new source object's `id` and the new event's `source_id`. Map obligation rows: J18–J20 keep raw source cell `` `clerk-filing-note` ``; every other cell matches the baseline row; only the path-qualification token changes (`r98-clerk-filing:` → `r99-window-lapse:`), which is the fixture's own cluster-local namespace rule, not a source-id change. No inherited J-row (J01–J20) cites `clerk-lapse-note`. The only new obligation row, J21 at map line 42, cites `` `clerk-lapse-note` `` / `` `r99-window-lapse:clerk-lapse-note` `` against `timeline.json#/7`.

6. **Non-row mentions, not retcons.** `clerk-lapse-note` also appears in prose that names the added source: r99 README line 7; map declaration line 11 (namespace list for the widened excerpt span 12–74); map prose line 18; excerpt line 68 (inside the appended section). Those lines do not change any inherited `source_id` or `first_appearance`. Same pattern r98 used when it added `clerk-filing-note` to the declaration list without restamping inherited obligation source cells. Not counted as a row leak.

## Cross-check against producer reports

- S3 (`S3-fixture-author.md`) says `entities.json` is identical to `4265df5` r98, timeline/sources prefixes equal, and the appended event is `clerk-lapse-recorded` / `clerk-lapse-note` / actor `clerk-maren`. Independent parse agrees. S3's note that README and the map still said r98 was true at S3's report time (this seat's first map read was that placeholder) and is stale after S4. Not a contradiction in the delivered bytes.
- S4 (`S4-fixture-docs.md`) says J18–J20 are unchanged modulo namespace and J21 is the only new obligation row, anchored in the lapse section. Independent cell compare agrees for the three clerk rows and for J21's source cell. Map sha `d2fe20e5…` matches the sha S4 recorded.

No contradiction between the delivered rows and either producer report.

## Bounds

- This seat did not replay `support_check.py`, freeze pins, or the census. `check_bible` CLEAN and `map_obligations` 21/21 are corroboration that the source ids still resolve and that the new event is the 21st obligation, not a whole-claim entailment verdict.
- `corpus/fixtures/README.md` has a Round 98 clerk bullet and no Round 99 bullet. Out of this seat's rows; not treated as a retcon.
- S5's lapse scope note was absent. If a later note restamps `first_appearance`, that would be a new claim, not a finding against the fixture rows measured here.

## Bottom line

PASS — clerk-maren's r98 and r99 entity row and inherited filing event are parsed-identical (entities.json byte-identical to `4265df5`); `first_appearance` remains `clerk-filing-note`; `clerk-lapse-note` appears only on r99's new source row, new timeline event, and new map row J21.
