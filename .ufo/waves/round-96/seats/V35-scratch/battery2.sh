#!/bin/sh
# V35 r96 operability battery v2 — run from repo root on the frozen delivered revision.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
T=corpus/tools/map_obligations.py
D=corpus/tools/dependency_freeze.py
S=.ufo/waves/round-96/seats/V35-scratch

run() { echo "=== $1"; shift; "$@"; echo "exit=$?"; }

echo "##### REVISION"
sha256sum $T corpus/tools/map-obligations-contract.json corpus/tools/README.md $D corpus/tools/dependency-freeze-contract.json
python3 -c "import json;c=json.load(open('corpus/tools/map-obligations-contract.json'));print('map contract cases:',len(c.get('self_test',{}).get('expected',c.get('self_test_cases',{}))))" 2>/dev/null

echo "##### A. map_obligations self-test (expect 24/24, exit 0)"
run "A1" python3 $T --self-test

echo "##### B. documented cluster commands"
run "B1 r96-crossing-response" python3 $T corpus/fixtures/r96-crossing-response
run "B2 r95-crossing-aftermath" python3 $T corpus/fixtures/r95-crossing-aftermath
run "B3 r94-paired-crossing" python3 $T corpus/fixtures/r94-paired-crossing
run "B4 r93-m2-kojiki-cluster" python3 $T corpus/fixtures/r93-m2-kojiki-cluster
run "B5 r88-m3-maya-cluster" python3 $T corpus/fixtures/r88-m3-maya-cluster
run "B6 r87 fail-closed" python3 $T corpus/fixtures/r87-myth-cluster
run "B7 r89 fail-closed" python3 $T corpus/fixtures/r89-inspiration-paraphrase
run "B8 frozen-r93 replay" python3 $T --frozen .ufo/waves/round-94/frozen/map-obligations-r93
run "B9 no-arg" python3 $T
run "B10 --help" python3 $T --help

echo "##### C. live mutation matrix (scratch copies)"
run "C1 deletion class (expect 1 inventory_mismatch)" python3 $T $S/r95-base
run "C2 dual pointer legacy (expect 1 dual_pointer)" python3 $T $S/r88-base
run "C3 missing row (expect 1 missing_obligation)" python3 $T $S/live-missing
run "C4 duplicate row (expect 1 duplicate_mapping)" python3 $T $S/live-duplicate
run "C5 source_id mismatch (expect 1 source_id_mismatch)" python3 $T $S/live-sid
run "C6 malformed json (expect 2 malformed_json)" python3 $T $S/live-malformed
run "C7 map missing (expect 2 map_missing)" python3 $T $S/live-nomap
run "C8 self-test+cluster misuse" python3 $T --self-test corpus/fixtures/r95-crossing-aftermath
run "C9 frozen+cluster misuse" python3 $T --frozen .ufo/waves/round-94/frozen/map-obligations-r93 corpus/fixtures/r95-crossing-aftermath

echo "##### D. dependency_freeze"
run "D1 chain r88-m3" python3 $D corpus/fixtures/r88-m3-maya-cluster
run "D2 chain r94" python3 $D corpus/fixtures/r94-paired-crossing
run "D3 chain r95" python3 $D corpus/fixtures/r95-crossing-aftermath
run "D4 chain r96" python3 $D corpus/fixtures/r96-crossing-response
run "D5 self-test" python3 $D --self-test
run "D6 no-arg" python3 $D
run "D7 BR-01 reduction (expect 1 REDUCTION-DETECTED)" python3 $D $S/dep-reduction/r95-crossing-aftermath
run "D8 added-edge (expect 1 ADDITION-DETECTED)" python3 $D $S/dep-addition/r95-crossing-aftermath
run "D9 malformed json (expect 2)" python3 $D $S/dep-malformed/r95-crossing-aftermath
run "D10 unpinned fixture r93 (expect 2 UNPINNED-FIXTURE)" python3 $D corpus/fixtures/r93-m2-kojiki-cluster
run "D11 self-test+fixture misuse (expect 2)" python3 $D --self-test corpus/fixtures/r94-paired-crossing

echo "##### E. fixture gates on r96"
run "E1 check_bible r96" python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
run "E2 support_check r96" python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
run "E3 check_bible r95" python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
run "E4 support_check r95" python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath

echo "##### F. write-hygiene"
git status --porcelain
