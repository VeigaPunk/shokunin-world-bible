#!/bin/bash
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V63-scratch/poll.log"
prev=""
stable=0
for n in $(seq 16 40); do
  ts=$(date +%H:%M:%S)
  sha=$(sha256sum "$LANE/corpus/tools/dependency-freeze-contract.json" | awk '{print $1}')
  info=$(python3 -c "
import json
c=json.load(open('$LANE/corpus/tools/dependency-freeze-contract.json'))
p=c.get('pins',{})
r99=p.get('r99-window-lapse')
nf=len((r99 or {}).get('files') or {})
ten=sum(1 for v in p.values() if len(v.get('files') or {})==10)
print('r99', int(r99 is not None), 'n', len(p), 'schema', c.get('schema_version'), 'payload', c.get('payload_schema_version'), 'r99files', nf, 'tenfile_pins', ten)
" 2>/dev/null || echo "parse-ERR")
  srep=$(ls "$SEATS"/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',')
  echo "CHECK n=$n t=$ts sha=${sha:0:12} info='$info' s=$srep" | tee -a "$LOG"
  has_r99=$(echo "$info" | awk '{print $2}')
  if [ "$sha" = "$prev" ]; then stable=$((stable+1)); else stable=0; fi
  prev=$sha
  if [ "$has_r99" = "1" ]; then
    echo "POLL_HIT_R99 n=$n t=$ts" | tee -a "$LOG"
    exit 0
  fi
  if echo "$srep" | grep -q 'S1' && [ "$stable" -ge 1 ]; then
    echo "POLL_HIT_S1_STABLE n=$n t=$ts stable=$stable" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_EXHAUSTED n=40 t=$(date +%H:%M:%S)" | tee -a "$LOG"
exit 1
