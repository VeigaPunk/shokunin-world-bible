#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-97/seats
for i in $(seq 1 40); do
  echo "poll $i $(date +%T)"
  REPORT=$(ls $S/R3-*.md 2>/dev/null | grep -v scratch | head -1)
  if [ -n "$REPORT" ]; then
    echo "REPORT_FOUND=$REPORT"
    # stability gate: wait 30s, then confirm both artifacts present and report unchanged
    sleep 30
    H1=$(sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>/dev/null)
    sleep 15
    H2=$(sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>/dev/null)
    if [ "$H1" = "$H2" ] && [ -n "$H1" ]; then
      echo "POLL_STABLE"
      echo "$H1"
      exit 0
    else
      echo "UNSTABLE_RETRY"
    fi
  fi
  sleep 20
done
echo "POLL_ABSENT"
exit 1
