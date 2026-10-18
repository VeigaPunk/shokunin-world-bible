### delivered/no-args  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
EXIT=2 want=2 findings=['INVALID-ARGUMENTS'] result=RESULT ERROR
--- stdout ---
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR

### delivered/missing-dir-pinned-name  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/missing-parent/r95-crossing-aftermath
EXIT=2 want=2 findings=['FIXTURE-MISSING'] result=RESULT ERROR
--- stdout ---
FINDING FIXTURE-MISSING: fixture directory not found: /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/missing-parent/r95-crossing-aftermath
RESULT ERROR

### delivered/missing-unpinned-name  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/v118-not-a-pin
EXIT=2 want=2 findings=['UNPINNED-FIXTURE'] result=RESULT ERROR
--- stdout ---
FINDING UNPINNED-FIXTURE: no pin for 'v118-not-a-pin' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR

### delivered/r99-window-lapse  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r99-window-lapse
EXIT=2 want=2 findings=['UNPINNED-FIXTURE'] result=RESULT ERROR
NOTE r99 is not a chain pin
--- stdout ---
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR

### delivered/foreign-copy  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/foreign/r95-crossing-aftermath
EXIT=2 want=2 findings=['PATH-MISMATCH'] result=RESULT ERROR
--- stdout ---
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/foreign/r95-crossing-aftermath
RESULT ERROR

### delivered/freeze-outside  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/outside-target
EXIT=2 want=2 findings=['SCOPE-REFUSED'] result=RESULT ERROR
--- stdout ---
FINDING SCOPE-REFUSED: --freeze refuses /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/outside-target (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/outside-target); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
DELIVERED_CONTRACT_UNCHANGED_AFTER_REFUSED_FREEZE True 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628

## delivered chain verify

### delivered/clean/r95-crossing-aftermath  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r95-crossing-aftermath
EXIT=0 want=0 findings=[] result=RESULT PASS
NOTE control; not an exit-2 class
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS

### delivered/clean/r98-clerk-filing  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r98-clerk-filing
EXIT=0 want=0 findings=[] result=RESULT PASS
NOTE control; not an exit-2 class
--- stdout ---
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS

### mirror/digest-one/timeline.json  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-timeline_json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-timeline_json/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE trailing newline; must name this file
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest f79cefa3dce602264fc32a7e72578b1c0c7b109238761f466b550496ba247987 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: timeline.json (sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/digest-one/README.md  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-README_md/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-README_md/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE trailing newline; must name this file
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest c619deac7b7caecd93b8f0fd12ea388ea643ea2424a02d8336f09b88d868003b != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md (sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> 983c528cb88f0e589df97c77a8321814aebd61a80ddcb1ab5b45cbba93e40ae7); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/digest-two-files  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-two/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/tamper-two/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE precedence: names each changed pinned file
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 5bca961244338e1034b5875a6fefb96a93ddb50415e6c03a15251fae3c012553 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md (sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> 983c528cb88f0e589df97c77a8321814aebd61a80ddcb1ab5b45cbba93e40ae7), source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> 5426ef14362d94f3388ec24a3d29973add977e369a368271a3ae50c4f0dfac3e); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/digest-pin-content-sha-lie  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/digest-pin-lie/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/digest-pin-lie/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE bytes unchanged; pin content digest disagrees with its file digests
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710 != pin 0000000000000000000000000000000000000000000000000000000000000000; changed: (no per-file digest difference; the pin's file digests disagree with its content digest); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/missing-readme  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-readme/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-readme/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE markdown absence is digest class, not model-build FILE-MISSING
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest f3b25d47155ac13a93b68f68e45100145caaa13fa99eb3479ea79c842154b6b9 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md (sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/missing-entities-json  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-entities/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-entities/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['DIGEST-MISMATCH'] result=RESULT ERROR
NOTE entities.json is pinned but not required for model build
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 100fb439aa9f45a97b79191b1bb47d63d334e3d03e29bdc2b09a24089be2526f != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: entities.json (sha256 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR

### mirror/missing-timeline-masks-digest  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-timeline/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-timeline/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['FILE-MISSING'] result=RESULT ERROR
NOTE FILE-MISSING (model build) decides before DIGEST-MISMATCH
--- stdout ---
FINDING FILE-MISSING: timeline.json is missing from /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/missing-timeline/corpus/fixtures/r95-crossing-aftermath
RESULT ERROR

### mirror/unreadable-timeline  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/unreadable-timeline/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/unreadable-timeline/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['FILE-MISSING'] result=RESULT ERROR
--- stdout ---
FINDING FILE-MISSING: timeline.json is unreadable: [Errno 13] Permission denied: '/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/unreadable-timeline/corpus/fixtures/r95-crossing-aftermath/timeline.json'
RESULT ERROR

### mirror/malformed-json-truncated  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/bad-json/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/bad-json/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['MALFORMED-JSON'] result=RESULT ERROR
--- stdout ---
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 3)
RESULT ERROR

### mirror/malformed-model-not-array  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/model-not-array/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/model-not-array/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['MALFORMED-MODEL'] result=RESULT ERROR
--- stdout ---
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR

### mirror/semantic-before-digest-reduction  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/semantic-reduction/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/semantic-reduction/corpus/fixtures/r95-crossing-aftermath
EXIT=1 want=1 findings=['REDUCTION-DETECTED'] result=RESULT FAIL
NOTE dropped a depends_on on paired-crossing-decision
--- stdout ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['aru-ninth-bell']
RESULT FAIL

### mirror/contract-missing  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/contract-missing/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/contract-missing/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['CONTRACT-INVALID'] result=RESULT ERROR
--- stdout ---
FINDING CONTRACT-INVALID: contract not found: corpus/tools/dependency-freeze-contract.json
RESULT ERROR

### mirror/schema1-before-fixture-missing  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/schema-1-and-worse/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/schema-1-and-worse/corpus/fixtures/absent-parent/r95-crossing-aftermath
EXIT=2 want=2 findings=['CONTRACT-INVALID'] result=RESULT ERROR
NOTE first failing check: schema before FIXTURE-MISSING and before pinned_files
--- stdout ---
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath payload_schema_version 1 != 2 (full-file pin of 10 files)
RESULT ERROR

### mirror/pin-files-missing-markdown-key  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/files-missing-key/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/files-missing-key/corpus/fixtures/r95-crossing-aftermath
EXIT=2 want=2 findings=['CONTRACT-INVALID'] result=RESULT ERROR
NOTE pin that does not digest all ten pinned files
--- stdout ---
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs sha256 digests for all 10 pinned files (entities.json, relations.json, timeline.json, sources.json, contradictions.json, README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, source-excerpt.md)
RESULT ERROR

### mirror/path-mismatch-before-file-missing  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/path-mismatch-masks-missing/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/path-mismatch-masks-missing/corpus/fixtures/nested/r95-crossing-aftermath
EXIT=2 want=2 findings=['PATH-MISMATCH'] result=RESULT ERROR
--- stdout ---
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/path-mismatch-masks-missing/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/path-mismatch-masks-missing/corpus/fixtures/nested/r95-crossing-aftermath
RESULT ERROR

### mirror/freeze-scope-root  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/scope-root/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/scope-root/corpus/fixtures
EXIT=2 want=2 findings=['SCOPE-REFUSED'] result=RESULT ERROR
--- stdout ---
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR
scope-root contract unchanged True

### mirror/freeze-same-name-masks-file-missing  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/scope-same-name-incomplete/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/scope-same-name-incomplete/corpus/fixtures/nested/r95-crossing-aftermath
EXIT=2 want=2 findings=['SCOPE-REFUSED'] result=RESULT ERROR
NOTE same-name SCOPE-REFUSED is checked before freeze's missing-pinned FILE-MISSING
--- stdout ---
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR

### mirror/freeze-missing-pinned-markdown  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/freeze-missing-md/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/freeze-missing-md/corpus/fixtures/v118-incomplete
EXIT=2 want=2 findings=['FILE-MISSING'] result=RESULT ERROR
NOTE --freeze FILE-MISSING when a declared pinned file is absent
--- stdout ---
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/v118-incomplete: pinned file(s) missing: inspiration-note.md
RESULT ERROR
freeze-missing-md contract unchanged True

### mirror/freeze-migrates-pathless  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/migrate-null/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/migrate-null/corpus/fixtures/r95-crossing-aftermath
EXIT=0 want=0 findings=[] result=RESULT PASS
NOTE documented exception: path-less legacy pin is migrated, not SCOPE-REFUSED
--- stdout ---
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS

### mirror/freeze-upgrades-schema1  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/upgrade-schema1/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/upgrade-schema1/corpus/fixtures/r95-crossing-aftermath
EXIT=0 want=0 findings=[] result=RESULT PASS
NOTE re-freeze is the payload upgrade path; verify of schema 1 is CONTRACT-INVALID
--- stdout ---
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
upgraded payload_schema_version=2 files=['README.md', 'claim-excerpt-map.md', 'contradictions.json', 'entities.json', 'fictional-excerpts.md', 'inspiration-note.md', 'relations.json', 'source-excerpt.md', 'sources.json', 'timeline.json']

## extra files outside the declared ten
EXTRAS r88-m3-maya-cluster ['symbolism-clause-map.md']

### mirror/unpinned-extra-file/r88-m3-maya-cluster/symbolism-clause-map.md  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/extra-r88-m3-maya-cluster/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/extra-r88-m3-maya-cluster/corpus/fixtures/r88-m3-maya-cluster
EXIT=0 want=0 findings=[] result=RESULT PASS
NOTE edit outside the declared ten must not be an exit-2
--- stdout ---
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXTRAS r94-paired-crossing []
EXTRAS r95-crossing-aftermath []
EXTRAS r96-crossing-response []
EXTRAS r97-crossing-acknowledgment []
EXTRAS r98-clerk-filing []

### mirror/selftest-set-mismatch  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/selftest-set-mismatch/corpus/tools/dependency_freeze.py --self-test
EXIT=2 want=2 findings=['CONTRACT-INVALID'] result=RESULT ERROR
--- stdout ---
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['clean'] extra=[]
RESULT ERROR

## self-test mismatch (slow)

### mirror/selftest-mismatch-clean-exit-flipped  [PASS]
$ /usr/bin/python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V118-scratch/cases/selftest-mismatch/corpus/tools/dependency_freeze.py --self-test
EXIT=2 want=2 findings=['SELF-TEST-MISMATCH'] result=RESULT ERROR
NOTE persisted expectation disagrees with observed clean exit
--- stdout ---
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

END tool=fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c unchanged=True
END contract=8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628 unchanged=True

DEMONSTRATED_EXIT2 ['CONTRACT-INVALID', 'DIGEST-MISMATCH', 'FILE-MISSING', 'FIXTURE-MISSING', 'INVALID-ARGUMENTS', 'MALFORMED-JSON', 'MALFORMED-MODEL', 'PATH-MISMATCH', 'SCOPE-REFUSED', 'SELF-TEST-MISMATCH', 'UNPINNED-FIXTURE']
UNDEMONSTRATED_EXIT2 []
FAILED_ROWS []
ROW_COUNT 77 FAIL_COUNT 0