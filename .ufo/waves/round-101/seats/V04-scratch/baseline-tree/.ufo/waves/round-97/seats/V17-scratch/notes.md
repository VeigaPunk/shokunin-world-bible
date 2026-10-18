# V17 c3-whole-claim — working notes (not the report)

Seat report (final): /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V17-c3-whole-claim.md
Scratch: /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V17-scratch/

## Interim state at ~18:47
- r97 dir exists (10 files, mtime 18:44). R4 delivered JSON tables + fictional-excerpts.md.
- R5 README.md + claim-excerpt-map.md are byte-identical to repaired r96 versions -> R5 NOT delivered yet.
- R4/R5 seat reports absent; poll bash-x9icbriq running (20s x 40).
- Interim hashes (r97 dir, 18:44):
  - claim-excerpt-map.md e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de (STALE r96 copy)
  - README.md ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456 (STALE r96 copy)
  - contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  - entities.json 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b
  - fictional-excerpts.md 8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c
  - inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  - relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  - source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  - sources.json 438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73
  - timeline.json 73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b

## Interim equality checks (python3, parsed)
- timeline r97[:5] == r96 -> True; new r97[5] = acknowledgment-aru-records (tick 13, aru, chalk-stair, ["response-evin-salt-court"], aru-acknowledgment-note)
- sources r97[:5] == r96 -> True; new r97[5] = aru-acknowledgment-note
- byte-identical to r96: entities.json, relations.json, contradictions.json, inspiration-note.md, source-excerpt.md -> all True
- r96 map repair present (git diff vs HEAD): delimiter line 44 8->7 cells; line 50 "new relation" -> "new tick-12 event" wording; no data-row changes in diff.

## Acknowledgment note clauses (fictional-excerpts.md:48-51), scope line 53
1. "Tick 13: I received Evin's response at the Chalk Stair." (receipt)
2. "I hold to my own account; both accounts stand unresolved." (maintain, not adjudicate)
3. "I make no accusation against Evin, and I select no winner between us." (explicit negation)
4. "I assert no reconciliation, no new duty, and no obligation beyond this crossing." (explicit negation)

Trace targets (stable, R4-delivered):
- sources.json#/5 reliability_note: "records receipt only and is not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact."
- timeline.json#/5 description: receipt + unresolved + no accusation/no reconciliation/no winner/no new duty beyond crossing.
- map J17 (R5, PENDING): expect anchor line 48 "Tick 13: I received Evin's response at the Chalk Stair.", span 44-53; expected inventory 17 JSON facts / 2 editorial / 19 total / 15 distinct anchors; README expected 5 entities / 1 relation / 6 events / 6 sources; 17 obligations.

## Negative constructibility checks (to execute on final revision)
- Resolution: clause 2+4 deny; no winner; contradictions.json empty; check README/map don't imply settlement.
- Accusation: clause 3 denies; tick-13 row must not re-assert non-arrival as blame; check.
- Reconciliation: clause 4 denies; "received" != reunion; check.
- New duty: clause 4 denies; relations.json byte-identical (only 1 relation); no new relation; check map/README.

## Receipts to run on final revision (from lane root)
- python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
- python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
- python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
Record tool file hashes at run time.
