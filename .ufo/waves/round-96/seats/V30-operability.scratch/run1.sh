#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R"
run() { # run <label> <cmd...>
  local label="$1"; shift
  echo "### $label"
  echo "\$ $*"
  local out; out=$("$@" 2>&1); local rc=$?
  echo "$out"
  echo "EXIT=$rc"
  echo
}
echo "=== BLOCK A: Q5 fixture README replay block (exactly as written) ==="
run "A1 check_bible r96" python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
run "A2 support_check r96" python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
run "A3 map_obligations r96" python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
echo "=== BLOCK B: Q6 note receipts block ==="
run "B1 check_bible r96" python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
run "B2 support_check r96" python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
run "B3 map_obligations r96" python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
echo "=== BLOCK C: tools README Round-96 addendum ==="
run "C1 self-test 24" python3 corpus/tools/map_obligations.py --self-test
run "C2 r88" python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
run "C3 r93" python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
run "C4 r94" python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
run "C5 r95" python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
run "C6 frozen r93" python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
run "C7 r87 fail-closed" python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
run "C8 r89 fail-closed" python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
