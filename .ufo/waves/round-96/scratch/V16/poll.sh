#!/bin/bash
for i in $(seq 1 40); do
  if [ -s corpus/tools/dependency_freeze.py ] && [ -s corpus/tools/dependency-freeze-contract.json ]; then
    R=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -iE '^Q3|^P3' | head -1)
    if [ -n "$R" ]; then
      echo "READY after $i tries: tool=$(wc -c < corpus/tools/dependency_freeze.py) contract=$(wc -c < corpus/tools/dependency-freeze-contract.json) report=$R"
      exit 0
    fi
    echo "try $i: tool+contract present, Q3/P3 report pending"
  else
    echo "try $i: tool=$( [ -e corpus/tools/dependency_freeze.py ] && echo yes || echo no ) contract=$( [ -e corpus/tools/dependency-freeze-contract.json ] && echo yes || echo no )"
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries"
exit 1
