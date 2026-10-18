# V54 scratch notes — crosscheck depth verdict (round 95)

Baseline: fb118c4. Saved baselines:
- baseline/map_obligations_r94.py sha256 cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790
- baseline/contract_r94.json sha256 349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50

## My own read-only observations (corroboration, not primary basis)

Pre-round baseline on r94 (16:17 local):
- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` → CLEAN ... 0 violations, exit 0
- `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → OBLIGATIONS raw=14 mapped=14 / RESULT PASS, exit 0
- `ls corpus/fixtures/` dirs = 168 (V20 census-pre.json also 168)

Working tree during round (16:24 local, fixture 9/10 files, README.md pending):
- r95 fixture: check_bible → CLEAN exit 0
- r95 fixture: map_obligations (r94 tool revision) → raw=15 mapped=15 RESULT PASS exit 0
- r95 fixture: support_check → SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; RESULT PASS exit 0
- counts: entities 5→5, relations 1→1, timeline 3→4, sources 3→4, contradictions 0→0
- inherited parsed equality: entities/relations/contradictions byte-eq True; timeline[:3] parsed-eq True; sources[:3] parsed-eq True
- new event aftermath-missing-evin tick 11 entity aru place chalk-stair depends_on [paired-crossing-decision] source aru-aftermath-note
- aftermath note text (fictional-excerpts.md): "Tick 11: I waited at the Chalk Stair through the agreed bell. / Evin did not come. / The agreement we chalked covered this crossing only. / I assert no other duty, no breach, and no obligation beyond this crossing."

## Pending

- P4 README.md (10th file)
- V08–V14 evidence reports (depth cluster per V23 poll script)
- V23 depth verdict report
