#!/bin/bash
# V29 poller: exits 0 when all producer artifacts are present/complete, else after 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
for i in $(seq 1 40); do
  ok=1
  [ -f corpus/tools/dependency_freeze.py ] || ok=0
  [ -f corpus/tools/dependency-freeze-contract.json ] || ok=0
  grep -q "Round-96" corpus/tools/README.md || ok=0
  [ -f corpus/fixtures/r96-crossing-response/README.md ] || ok=0
  [ -f corpus/fixtures/r96-crossing-response/claim-excerpt-map.md ] || ok=0
  [ -f corpus/knowledge/r96-response-scope-note.md ] || ok=0
  # map_obligations self-test must report 24 cases
  st=$(python3 corpus/tools/map_obligations.py --self-test 2>/dev/null | grep -c "SELF-TEST PASS")
  [ "$st" -ge 24 ] || ok=0
  # producer reports
  pr=$(ls .ufo/waves/round-96/seats/Q[1-6]*.md 2>/dev/null | wc -l)
  [ "$pr" -ge 6 ] || ok=0
  if [ "$ok" = 1 ]; then echo "ALL_PRESENT try=$i"; exit 0; fi
  echo "try=$i ok=$ok st=$st pr=$pr"
  sleep 20
done
echo "TIMEOUT_AFTER_40"
exit 1
