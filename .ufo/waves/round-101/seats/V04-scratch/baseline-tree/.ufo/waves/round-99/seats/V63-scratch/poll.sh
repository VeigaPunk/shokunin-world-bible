#!/bin/bash
# V63 poll: producer artifacts + producer reports. 20s cadence, max 40.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V63-scratch/poll.log"
: > "$LOG"
for n in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  # artifacts
  fx=0; [ -f "$LANE/corpus/fixtures/r99-window-lapse/timeline.json" ] && fx=1
  pins=$(python3 -c "
import json
c=json.load(open('$LANE/corpus/tools/dependency-freeze-contract.json'))
p=c.get('pins',{})
print('r99', int('r99-window-lapse' in p), 'n', len(p), 'schema', c.get('schema_version'), 'files', len((p.get('r99-window-lapse') or {}).get('files') or {}))
" 2>/dev/null || echo "r99 ERR")
  # producer reports: any S*.md
  srep=$(ls "$SEATS"/S*.md 2>/dev/null | wc -l)
  snames=$(ls "$SEATS"/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',' )
  line="CHECK n=$n t=$ts fixture=$fx pins='$pins' s_reports=$srep names=$snames"
  echo "$line" | tee -a "$LOG"
  # hit when r99 pin exists AND at least one producer report (S1 or S3)
  has_r99=$(echo "$pins" | awk '{print $2}')
  if [ "$fx" = "1" ] && [ "$has_r99" = "1" ] && [ "$srep" -ge 1 ]; then
    echo "POLL_HIT n=$n t=$ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "POLL_EXHAUSTED n=40 t=$(date +%H:%M:%S)" | tee -a "$LOG"
exit 1
