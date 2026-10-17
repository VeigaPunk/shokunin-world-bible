#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  if [ -f corpus/tools/dependency_freeze.py ] && [ -f corpus/tools/dependency-freeze-contract.json ]; then
    if [ -f .ufo/waves/round-96/seats/Q3-dependency-freeze.md ] || ls .ufo/waves/round-96/seats/ | grep -qi "^Q3"; then
      echo "READY at try $i: $(date -Is)"; ls -la corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json; ls .ufo/waves/round-96/seats/ | grep -i Q3; exit 0
    fi
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries: $(date -Is)"; ls corpus/tools/; ls .ufo/waves/round-96/seats/ | grep -i "Q[1-6]" ; exit 3
