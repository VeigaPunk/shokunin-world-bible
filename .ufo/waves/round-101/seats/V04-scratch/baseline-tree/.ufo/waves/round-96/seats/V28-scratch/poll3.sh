#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  c=0
  if python3 -c "
import json,sys
try:
    d=json.load(open('$R/corpus/tools/map-obligations-contract.json'))
    n=len(d.get('self_test',{}).get('cases',d.get('cases',[])))
    sys.exit(0 if n>=24 else 1)
except Exception:
    sys.exit(1)
" 2>/dev/null; then c=1; fi
  r=0
  [ "$R/corpus/tools/README.md" -nt "$R/.ufo/waves/round-96/seats/V28-scratch/wavestart.stamp" ] && r=1
  q2=0
  ls "$R/.ufo/waves/round-96/seats/" 2>/dev/null | grep -q '^Q2.*\.md$' && q2=1
  echo "try=$i contract24=$c readme_new=$r q2report=$q2 $(date +%H:%M:%S)"
  if [ "$c" -eq 1 ] && [ "$r" -eq 1 ] && [ "$q2" -eq 1 ]; then echo "Q2-LANDED"; exit 0; fi
  sleep 20
done
echo "POLL-TIMEOUT"
