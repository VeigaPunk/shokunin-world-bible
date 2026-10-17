#!/bin/bash
# poll for Q3 artifacts + producer report
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  if [ -f "$R/corpus/tools/dependency_freeze.py" ] && [ -f "$R/corpus/tools/dependency-freeze-contract.json" ]; then
    echo "TOOLS_PRESENT try=$i $(date -Iseconds)"
    ls -la "$R/corpus/tools/dependency_freeze.py" "$R/corpus/tools/dependency-freeze-contract.json"
    break
  fi
  sleep 20
done
for i in $(seq 1 20); do
  RPT=$(ls "$R"/.ufo/waves/round-96/seats/Q3*.md 2>/dev/null | head -1)
  if [ -n "$RPT" ]; then echo "Q3_REPORT_PRESENT $RPT"; break; fi
  sleep 20
done
echo "POLL_DONE $(date -Iseconds)"
