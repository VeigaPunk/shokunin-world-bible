## clean_r99
Expected exit=0 IDs=[]
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/clean_r99/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/clean_r99/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/clean_r99/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/clean_r99/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0 stderr=''
```
## semantic_drop_tick15_edge
Expected exit=1 IDs=['REDUCTION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_add_tick15_edge
Expected exit=1 IDs=['ADDITION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_tick15_edge/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_tick15_edge/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 8/7; relations 1/1
FINDING ADDITION-DETECTED: event clerk-lapse-recorded gained depends_on ['v03-phantom']
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_tick15_edge/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_tick15_edge/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 8/7; relations 1/1
FINDING ADDITION-DETECTED: event clerk-lapse-recorded gained depends_on ['v03-phantom']
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_remove_tick15_event
Expected exit=1 IDs=['REDUCTION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_remove_tick15_event/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_remove_tick15_event/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 7/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded is missing; 1 frozen dependency edge(s) gone
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_remove_tick15_event/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_remove_tick15_event/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 7/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded is missing; 1 frozen dependency edge(s) gone
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_add_event_with_dependency
Expected exit=1 IDs=['ADDITION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_event_with_dependency/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_event_with_dependency/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 9/8; dependency-edges 8/7; relations 1/1
FINDING ADDITION-DETECTED: unpinned event v03-added-event introduces depends_on ['clerk-lapse-recorded']
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_event_with_dependency/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_add_event_with_dependency/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 9/8; dependency-edges 8/7; relations 1/1
FINDING ADDITION-DETECTED: unpinned event v03-added-event introduces depends_on ['clerk-lapse-recorded']
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_event_endpoint_tick
Expected exit=1 IDs=['ENDPOINT-CHANGE']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_tick/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_tick/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.tick: 15 -> 150
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_tick/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_tick/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.tick: 15 -> 150
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_event_endpoint_entity_id
Expected exit=1 IDs=['ENDPOINT-CHANGE']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_entity_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_entity_id/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.entity_id: 'clerk-maren' -> 'aru'
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_entity_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_entity_id/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.entity_id: 'clerk-maren' -> 'aru'
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_event_endpoint_place_id
Expected exit=1 IDs=['ENDPOINT-CHANGE']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_place_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_place_id/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.place_id: 'chalk-stair' -> 'salt-court'
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_place_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_event_endpoint_place_id/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: event clerk-lapse-recorded.place_id: 'chalk-stair' -> 'salt-court'
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_relation_endpoint_flip
Expected exit=1 IDs=['ENDPOINT-CHANGE']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_endpoint_flip/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_endpoint_flip/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_endpoint_flip/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_endpoint_flip/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_relation_remove
Expected exit=1 IDs=['REDUCTION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_remove/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_remove/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 0/1
FINDING REDUCTION-DETECTED: relation edge(s) removed: [aru, evin, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_remove/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_remove/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 0/1
FINDING REDUCTION-DETECTED: relation edge(s) removed: [aru, evin, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_relation_add
Expected exit=1 IDs=['ADDITION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_add/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_add/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 2/1
FINDING ADDITION-DETECTED: relation edge(s) added: [aru, clerk-maren, v03-unpinned]
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_add/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_relation_add/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 2/1
FINDING ADDITION-DETECTED: relation edge(s) added: [aru, clerk-maren, v03-unpinned]
RESULT FAIL
observed_exit=1 stderr=''
```
## semantic_precedes_digest
Expected exit=1 IDs=['REDUCTION-DETECTED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_precedes_digest/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_precedes_digest/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_precedes_digest/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_precedes_digest/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1 stderr=''
```
## digest_newline_entities.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_entities.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_entities.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d938eefd5dc106154b3630015c055b3cadb359c251fdb7e4f8fb00ceea2036c5 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> 457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_entities.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_entities.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d938eefd5dc106154b3630015c055b3cadb359c251fdb7e4f8fb00ceea2036c5 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> 457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_relations.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d3d46771bab7eb4a1dd3614b69b4db533f9d3ea211d74f0afba2ad32479d6206 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: relations.json (sha256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 -> 811144128783ee753fa02b1612d4d560318e49685dc68360fd8766f130a9b086); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d3d46771bab7eb4a1dd3614b69b4db533f9d3ea211d74f0afba2ad32479d6206 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: relations.json (sha256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 -> 811144128783ee753fa02b1612d4d560318e49685dc68360fd8766f130a9b086); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_timeline.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 35b9c67b0a0fbd2d6000d76020e819eb616cdf6150cd3d6c6801c077b88e6d7b != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: timeline.json (sha256 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 -> b0fbe75127fe755e10a0db0bf77c29ec8a4bf2e5baa29597f59aafa7a2c0cbbe); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 35b9c67b0a0fbd2d6000d76020e819eb616cdf6150cd3d6c6801c077b88e6d7b != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: timeline.json (sha256 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 -> b0fbe75127fe755e10a0db0bf77c29ec8a4bf2e5baa29597f59aafa7a2c0cbbe); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_sources.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_sources.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_sources.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest c7ef697e9d2e2b221a8b50ebe44cc22376563db5d37a90028d8736dd385597eb != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: sources.json (sha256 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 -> 647415129fd5220c873bed4cbb0c44248d1cedca6de0183f499a6db65eb8f494); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_sources.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_sources.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest c7ef697e9d2e2b221a8b50ebe44cc22376563db5d37a90028d8736dd385597eb != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: sources.json (sha256 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 -> 647415129fd5220c873bed4cbb0c44248d1cedca6de0183f499a6db65eb8f494); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_contradictions.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_contradictions.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_contradictions.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 2312a9e81c8c3f87261639383317d2efee2b307f17cac7d713a1fb6c75af63fe != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: contradictions.json (sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 -> 5239a7754876b9a70871c45e41f1bd9abbd91ed2de67af926c1cfcc9c9377d51); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_contradictions.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_contradictions.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 2312a9e81c8c3f87261639383317d2efee2b307f17cac7d713a1fb6c75af63fe != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: contradictions.json (sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 -> 5239a7754876b9a70871c45e41f1bd9abbd91ed2de67af926c1cfcc9c9377d51); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_README.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_README.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_README.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 184fc88016259ee0327d137e9bf15ec95a6a97dfa6bb6e7f6a16b0f26bac9f62 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: README.md (sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 -> 01ff4f3710ac03a17d8b35d9adda8504218e033bf89c60920815171e56d45919); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_README.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_README.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 184fc88016259ee0327d137e9bf15ec95a6a97dfa6bb6e7f6a16b0f26bac9f62 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: README.md (sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 -> 01ff4f3710ac03a17d8b35d9adda8504218e033bf89c60920815171e56d45919); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_claim-excerpt-map.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_claim-excerpt-map.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_claim-excerpt-map.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d86bb9b4a2ca25d0b7e236f17342230e65297d4fee289d6e71142531a151e3d4 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: claim-excerpt-map.md (sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d -> 53a10ca3631784e843ed64f4a8aa4042b8d5af3bda09fd6ca45a7cb41b95530c); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_claim-excerpt-map.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_claim-excerpt-map.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest d86bb9b4a2ca25d0b7e236f17342230e65297d4fee289d6e71142531a151e3d4 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: claim-excerpt-map.md (sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d -> 53a10ca3631784e843ed64f4a8aa4042b8d5af3bda09fd6ca45a7cb41b95530c); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_fictional-excerpts.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_fictional-excerpts.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_fictional-excerpts.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest cce8f18813ed6fc24ec8032a28b687c4731efdc72d05434c124c89a0dcd1c49f != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> ee276abf20eb37adc44e6d5fc8cbf08615851734aad4b5eeec8c333af7f70408); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_fictional-excerpts.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_fictional-excerpts.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest cce8f18813ed6fc24ec8032a28b687c4731efdc72d05434c124c89a0dcd1c49f != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> ee276abf20eb37adc44e6d5fc8cbf08615851734aad4b5eeec8c333af7f70408); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_inspiration-note.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_inspiration-note.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_inspiration-note.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 388727aa98aa5bfade009eda67168b2290c6ed9fed61389326e4e5d5d5bc45a0 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> a1be0d5b00e0c695acbebbdee55d1fc00e8956e53f71ec8f6fde1157c055b3af); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_inspiration-note.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_inspiration-note.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 388727aa98aa5bfade009eda67168b2290c6ed9fed61389326e4e5d5d5bc45a0 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> a1be0d5b00e0c695acbebbdee55d1fc00e8956e53f71ec8f6fde1157c055b3af); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## digest_newline_source-excerpt.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_source-excerpt.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_source-excerpt.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 2dd18f5975516792213958a5e7a8d174b481ff64742a6f021756527e6ca07e34 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> 5426ef14362d94f3388ec24a3d29973add977e369a368271a3ae50c4f0dfac3e); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_source-excerpt.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/digest_newline_source-excerpt.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 2dd18f5975516792213958a5e7a8d174b481ff64742a6f021756527e6ca07e34 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> 5426ef14362d94f3388ec24a3d29973add977e369a368271a3ae50c4f0dfac3e); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_entities.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_entities.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_entities.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 779ce0693d3d7faa215f6628549013a773585e85db635343d5617d9d981683f0 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_entities.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_entities.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 779ce0693d3d7faa215f6628549013a773585e85db635343d5617d9d981683f0 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_relations.json
Expected exit=2 IDs=['FILE-MISSING']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: relations.json is missing from /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: relations.json is missing from /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_relations.json/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_timeline.json
Expected exit=2 IDs=['FILE-MISSING']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: timeline.json is missing from /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: timeline.json is missing from /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_timeline.json/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_sources.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_sources.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_sources.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest a1f4e5aa6bca1b5278f064653aa58a855272bd9962e6616f7f30af7079e65cba != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: sources.json (sha256 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_sources.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_sources.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest a1f4e5aa6bca1b5278f064653aa58a855272bd9962e6616f7f30af7079e65cba != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: sources.json (sha256 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_contradictions.json
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_contradictions.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_contradictions.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest c8d0d6378a4fa19bead036cec3728b9cacec5fc7370b57e2a8124fcb5e228800 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: contradictions.json (sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_contradictions.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_contradictions.json/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest c8d0d6378a4fa19bead036cec3728b9cacec5fc7370b57e2a8124fcb5e228800 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: contradictions.json (sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_README.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_README.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_README.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest ac32d1dea515cb0d3b20c8c126c5fd74bd7295e9b9276ce487a85537dc5338d4 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: README.md (sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_README.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_README.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest ac32d1dea515cb0d3b20c8c126c5fd74bd7295e9b9276ce487a85537dc5338d4 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: README.md (sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_claim-excerpt-map.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_claim-excerpt-map.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_claim-excerpt-map.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest ec89d574487715189204e8b872ae693659963a998e21dfd657fea07a722be023 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: claim-excerpt-map.md (sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_claim-excerpt-map.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_claim-excerpt-map.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest ec89d574487715189204e8b872ae693659963a998e21dfd657fea07a722be023 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: claim-excerpt-map.md (sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_fictional-excerpts.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_fictional-excerpts.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_fictional-excerpts.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest b55465905f0bc3aa55c21113438476182480e17b97258fdda6426b9af6df9f56 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_fictional-excerpts.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_fictional-excerpts.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest b55465905f0bc3aa55c21113438476182480e17b97258fdda6426b9af6df9f56 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_inspiration-note.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_inspiration-note.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_inspiration-note.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest e5e0bd6c81c9a536ba10582d93879cda3185b395847601f5b6a64e067ff5fa1f != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_inspiration-note.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_inspiration-note.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest e5e0bd6c81c9a536ba10582d93879cda3185b395847601f5b6a64e067ff5fa1f != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_source-excerpt.md
Expected exit=2 IDs=['DIGEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_source-excerpt.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_source-excerpt.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 41d1fd53f86a9b5eca8f2170765c8a74fc59d9ec058404b245b6c2eed9454a7c != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_source-excerpt.md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_source-excerpt.md/corpus/fixtures/r99-window-lapse
```
```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 41d1fd53f86a9b5eca8f2170765c8a74fc59d9ec058404b245b6c2eed9454a7c != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_json_syntax
Expected exit=2 IDs=['MALFORMED-JSON']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_syntax/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_syntax/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 3)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_syntax/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_syntax/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 3)
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_json_utf8
Expected exit=2 IDs=['MALFORMED-JSON']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_utf8/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_utf8/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: timeline.json is not UTF-8: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_utf8/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_utf8/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: timeline.json is not UTF-8: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_json_sources
Expected exit=2 IDs=['MALFORMED-JSON']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_sources/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_sources/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: sources.json: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_sources/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_json_sources/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-JSON: sources.json: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_object_timeline.json
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_timeline.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_timeline.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_object_relations.json
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_relations.json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_object_relations.json/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_empty_event_id
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_event_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_event_id/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7] needs a nonempty string id
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_event_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_event_id/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7] needs a nonempty string id
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_duplicate_event_id
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_duplicate_event_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_duplicate_event_id/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7] repeats event id clerk-filing-open
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_duplicate_event_id/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_duplicate_event_id/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7] repeats event id clerk-filing-open
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_dep_not_list
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_dep_not_list/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_dep_not_list/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].depends_on must be an array of nonempty strings
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_dep_not_list/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_dep_not_list/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].depends_on must be an array of nonempty strings
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_empty_dep
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_dep/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_dep/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].depends_on must be an array of nonempty strings
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_dep/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_empty_dep/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].depends_on must be an array of nonempty strings
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_nonscalar_endpoint
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_nonscalar_endpoint/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_nonscalar_endpoint/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].tick must be a scalar
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_nonscalar_endpoint/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_nonscalar_endpoint/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: timeline[7].tick must be a scalar
RESULT ERROR
observed_exit=2 stderr=''
```
## malformed_model_relation_from_missing
Expected exit=2 IDs=['MALFORMED-MODEL']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_relation_from_missing/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_relation_from_missing/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: relations[0] needs nonempty string from/to/type
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_relation_from_missing/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/malformed_model_relation_from_missing/corpus/fixtures/r99-window-lapse
```
```text
FINDING MALFORMED-MODEL: relations[0] needs nonempty string from/to/type
RESULT ERROR
observed_exit=2 stderr=''
```
## unpinned_real_nonchain_r93
Expected exit=2 IDs=['UNPINNED-FIXTURE']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/fixtures/r93-m2-kojiki-cluster
```
```text
FINDING UNPINNED-FIXTURE: no pin for 'r93-m2-kojiki-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/fixtures/r93-m2-kojiki-cluster
```
```text
FINDING UNPINNED-FIXTURE: no pin for 'r93-m2-kojiki-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
observed_exit=2 stderr=''
```
## missing_known_fixture
Expected exit=2 IDs=['FIXTURE-MISSING']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/fixtures/r99-window-lapse
```
```text
FINDING FIXTURE-MISSING: fixture directory not found: /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/fixtures/r99-window-lapse
```
```text
FINDING FIXTURE-MISSING: fixture directory not found: /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/missing_known_fixture/corpus/fixtures/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
## same_name_foreign_path
Expected exit=2 IDs=['PATH-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/foreign/r99-window-lapse
```
```text
FINDING PATH-MISMATCH: pin r99-window-lapse names corpus/fixtures/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/corpus/fixtures/r99-window-lapse); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/foreign/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/foreign/r99-window-lapse
```
```text
FINDING PATH-MISMATCH: pin r99-window-lapse names corpus/fixtures/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/corpus/fixtures/r99-window-lapse); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/same_name_foreign_path/foreign/r99-window-lapse
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_absent
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: contract not found: corpus/tools/dependency-freeze-contract.json
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: contract not found: corpus/tools/dependency-freeze-contract.json
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_malformed_json
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_malformed_json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_malformed_json/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: corpus/tools/dependency-freeze-contract.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_malformed_json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_malformed_json/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: corpus/tools/dependency-freeze-contract.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_root_not_object
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_root_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_root_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: contract root must be an object with a pins object
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_root_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_root_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: contract root must be an object with a pins object
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_not_object
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse must be an object
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse must be an object
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_fixture_absent
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a repo-relative fixture path
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a repo-relative fixture path
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_fixture_absolute
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absolute/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absolute/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a repo-relative fixture path
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absolute/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_absolute/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a repo-relative fixture path
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_fixture_outside_scope
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_outside_scope/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_outside_scope/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse names corpus/tools/v03, outside corpus/fixtures/**
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_outside_scope/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_fixture_outside_scope/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse names corpus/tools/v03, outside corpus/fixtures/**
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_payload_schema_1
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_payload_schema_1/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_payload_schema_1/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse payload_schema_version 1 != 2 (full-file pin of 10 files)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_payload_schema_1/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_payload_schema_1/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse payload_schema_version 1 != 2 (full-file pin of 10 files)
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_pinned_files_short
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_pinned_files_short/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_pinned_files_short/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse pinned_files ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md'] != ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_pinned_files_short/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_pinned_files_short/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse pinned_files ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md'] != ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_content_digest_bad
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_content_digest_bad/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_content_digest_bad/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a sha256 content digest
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_content_digest_bad/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_content_digest_bad/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs a sha256 content digest
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_file_digest_absent
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_file_digest_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_file_digest_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs sha256 digests for all 10 pinned files (entities.json, relations.json, timeline.json, sources.json, contradictions.json, README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, source-excerpt.md)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_file_digest_absent/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_file_digest_absent/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs sha256 digests for all 10 pinned files (entities.json, relations.json, timeline.json, sources.json, contradictions.json, README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, source-excerpt.md)
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_events_not_object
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_events_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_events_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs an events object
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_events_not_object/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_events_not_object/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs an events object
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_event_entry_invalid
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_event_entry_invalid/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_event_entry_invalid/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse has an invalid event entry for 'v03'
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_event_entry_invalid/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_event_entry_invalid/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse has an invalid event entry for 'v03'
RESULT ERROR
observed_exit=2 stderr=''
```
## contract_pin_relations_invalid
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_relations_invalid/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_relations_invalid/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs relation endpoint triples
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_relations_invalid/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/contract_pin_relations_invalid/corpus/fixtures/r99-window-lapse
```
```text
FINDING CONTRACT-INVALID: pin r99-window-lapse needs relation endpoint triples
RESULT ERROR
observed_exit=2 stderr=''
```
## freeze_foreign_scope
Expected exit=2 IDs=['SCOPE-REFUSED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse
```
```text
FINDING SCOPE-REFUSED: --freeze refuses /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse
```
```text
FINDING SCOPE-REFUSED: --freeze refuses /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_foreign_scope/foreign/r99-window-lapse); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
observed_exit=2 stderr=''
```
## freeze_scope_root
Expected exit=2 IDs=['SCOPE-REFUSED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_scope_root/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_scope_root/corpus/fixtures
```
```text
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_scope_root/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_scope_root/corpus/fixtures
```
```text
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR
observed_exit=2 stderr=''
```
## freeze_same_name_other_in_scope
Expected exit=2 IDs=['SCOPE-REFUSED']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_same_name_other_in_scope/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_same_name_other_in_scope/corpus/fixtures/nested/r99-window-lapse
```
```text
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r99-window-lapse: pin r99-window-lapse already names 'corpus/fixtures/r99-window-lapse'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_same_name_other_in_scope/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_same_name_other_in_scope/corpus/fixtures/nested/r99-window-lapse
```
```text
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r99-window-lapse: pin r99-window-lapse already names 'corpus/fixtures/r99-window-lapse'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
observed_exit=2 stderr=''
```
## freeze_missing_pinned_markdown
Expected exit=2 IDs=['FILE-MISSING']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_missing_pinned_markdown/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_missing_pinned_markdown/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/r99-window-lapse: pinned file(s) missing: README.md
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_missing_pinned_markdown/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/freeze_missing_pinned_markdown/corpus/fixtures/r99-window-lapse
```
```text
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/r99-window-lapse: pinned file(s) missing: README.md
RESULT ERROR
observed_exit=2 stderr=''
```
## args_none
Expected exit=2 IDs=['INVALID-ARGUMENTS']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_none/corpus/tools/dependency_freeze.py
```
```text
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_none/corpus/tools/dependency_freeze.py
```
```text
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR
observed_exit=2 stderr=''
```
## args_combined_verify_freeze
Expected exit=2 IDs=['INVALID-ARGUMENTS']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/fixtures/r99-window-lapse --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/fixtures/r99-window-lapse --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_combined_verify_freeze/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
observed_exit=2 stderr=''
```
## args_selftest_fixture
Expected exit=2 IDs=['INVALID-ARGUMENTS']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_fixture/corpus/tools/dependency_freeze.py --self-test /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_fixture/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_fixture/corpus/tools/dependency_freeze.py --self-test /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_fixture/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
observed_exit=2 stderr=''
```
## args_selftest_freeze
Expected exit=2 IDs=['INVALID-ARGUMENTS']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_freeze/corpus/tools/dependency_freeze.py --self-test --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_freeze/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_freeze/corpus/tools/dependency_freeze.py --self-test --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_selftest_freeze/corpus/fixtures/r99-window-lapse
```
```text
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
observed_exit=2 stderr=''
```
## args_unknown_flag
Expected exit=2 IDs=['INVALID-ARGUMENTS']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_unknown_flag/corpus/tools/dependency_freeze.py --v03-unknown-option
```
```text
FINDING INVALID-ARGUMENTS: unrecognized arguments: --v03-unknown-option
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/args_unknown_flag/corpus/tools/dependency_freeze.py --v03-unknown-option
```
```text
FINDING INVALID-ARGUMENTS: unrecognized arguments: --v03-unknown-option
RESULT ERROR
observed_exit=2 stderr=''
```
## selftest_clean_control
Expected exit=0 IDs=[]
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_clean_control/corpus/tools/dependency_freeze.py --self-test
```
```text
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
observed_exit=0 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_clean_control/corpus/tools/dependency_freeze.py --self-test
```
```text
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
observed_exit=0 stderr=''
```
## selftest_expectation_flip
Expected exit=2 IDs=['SELF-TEST-MISMATCH']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expectation_flip/corpus/tools/dependency_freeze.py --self-test
```
```text
CASE clean: exit=0 expected=1 findings=[] MISMATCH
  observed stdout: ['FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1', 'DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710', 'RESULT PASS']
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expectation_flip/corpus/tools/dependency_freeze.py --self-test
```
```text
CASE clean: exit=0 expected=1 findings=[] MISMATCH
  observed stdout: ['FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1', 'DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710', 'RESULT PASS']
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
observed_exit=2 stderr=''
```
## selftest_expected_case_missing
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expected_case_missing/corpus/tools/dependency_freeze.py --self-test
```
```text
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['markdown_tamper'] extra=[]
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expected_case_missing/corpus/tools/dependency_freeze.py --self-test
```
```text
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['markdown_tamper'] extra=[]
RESULT ERROR
observed_exit=2 stderr=''
```
## selftest_expected_case_extra
Expected exit=2 IDs=['CONTRACT-INVALID']
IDs stable=True full-output stable=True status=PASS
### Repeat 1
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expected_case_extra/corpus/tools/dependency_freeze.py --self-test
```
```text
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=[] extra=['v03-extra']
RESULT ERROR
observed_exit=2 stderr=''
```
### Repeat 2
```sh
$ python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expected_case_extra/corpus/tools/dependency_freeze.py --self-test
```
```text
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=[] extra=['v03-extra']
RESULT ERROR
observed_exit=2 stderr=''
```
