#!/bin/sh
# V35 r96 operability battery — run from repo root on the frozen delivered revision.
# Usage: sh .ufo/waves/round-96/seats/V35-scratch/battery.sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
T=corpus/tools/map_obligations.py
D=corpus/tools/dependency_freeze.py
S=.ufo/waves/round-96/seats/V35-scratch

run() {  # run <label> <cmd...>
  echo "=== $1"
  shift
  "$@"
  echo "exit=$?"
}

echo "##### A. map_obligations self-test"
run "A1 self-test" python3 $T --self-test

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

echo "##### C. exit-contract probes (scratch copies)"
run "C1 deletion-class live (expect 1 inventory_mismatch)" python3 $T $S/r95-base
run "C2 dual-pointer live (expect 1 dual_pointer)" python3 $T $S/r88-base
run "C3 self-test+cluster misuse" python3 $T --self-test corpus/fixtures/r95-crossing-aftermath
run "C4 frozen+cluster misuse" python3 $T --frozen .ufo/waves/round-94/frozen/map-obligations-r93 corpus/fixtures/r95-crossing-aftermath

echo "##### D. dependency_freeze"
run "D1 chain r88-m3" python3 $D corpus/fixtures/r88-m3-maya-cluster
run "D2 chain r94" python3 $D corpus/fixtures/r94-paired-crossing
run "D3 chain r95" python3 $D corpus/fixtures/r95-crossing-aftermath
run "D4 chain r96" python3 $D corpus/fixtures/r96-crossing-response
run "D5 self-test" python3 $D --self-test
run "D6 no-arg" python3 $D
run "D7 BR-01 reduction mutation (expect 1)" python3 $D $S/dep-reduction
run "D8 added-edge mutation (expect 1)" python3 $D $S/dep-addition
run "D9 malformed cluster (expect 2)" python3 $D $S/dep-malformed

echo "##### E. fixture gates on r96"
run "E1 check_bible r96" python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
run "E2 support_check r96" python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
