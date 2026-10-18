#!/bin/bash
# V69 poll-wait. 20s cadence, max 40 tries. Never verify a plan.
# READY when producer artifacts AND producer reports exist:
#   - S1 report nonempty AND contract has >=1 pin with >=10 files (full-file pinning)
#   - S3 report nonempty AND r99 timeline has clerk-lapse-recorded AND sources has clerk-lapse-note
#   - S4 report nonempty
#   - S5 report nonempty AND r99-gate-blind-spot-table.md nonempty
#   - V30 report nonempty (compare target; not a producer)
# SELF (V69) is never in the wait set.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V69-scratch/poll.log
FIX=$LANE/corpus/fixtures/r99-window-lapse
CONTRACT=$LANE/corpus/tools/dependency-freeze-contract.json
TABLE=$LANE/corpus/knowledge/r99-gate-blind-spot-table.md
i=0
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  ev=0; srcnote=0
  s1=no; s3=no; s4=no; s5=no; v30=no
  table=no
  pins10=0; npins=0; schema=?
  if [ -f "$FIX/timeline.json" ]; then ev=$(grep -c 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || true); fi
  if [ -f "$FIX/sources.json" ]; then srcnote=$(grep -c 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || true); fi
  if [ -f "$CONTRACT" ]; then
    read -r schema npins pins10 < <(python3 - << 'PY'
import json
c=json.load(open("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json"))
pins=c.get("pins") or {}
n10=0
if isinstance(pins, dict):
    for v in pins.values():
        files=v.get("files") if isinstance(v, dict) else None
        if isinstance(files, dict) and len(files) >= 10:
            n10 += 1
        elif isinstance(files, list) and len(files) >= 10:
            n10 += 1
print(c.get("schema_version"), len(pins) if isinstance(pins, dict) else -1, n10)
PY
)
  fi
  nonempty() { local f; f=$(ls $SEATS/$1 2>/dev/null | head -1); [ -n "$f" ] && [ -s "$f" ]; }
  nonempty 'S1-*.md' && s1=yes
  nonempty 'S3-*.md' && s3=yes
  nonempty 'S4-*.md' && s4=yes
  nonempty 'S5-*.md' && s5=yes
  nonempty 'V30-*.md' && v30=yes
  [ -s "$TABLE" ] && table=yes
  echo "try=$i ts=$ts ev=$ev note=$srcnote schema=$schema npins=$npins pins10=$pins10 table=$table s1=$s1 s3=$s3 s4=$s4 s5=$s5 v30=$v30" | tee -a "$LOG"
  if [ "$ev" -ge 1 ] && [ "$srcnote" -ge 1 ] && [ "$s1" = yes ] && [ "$s3" = yes ] && [ "$s4" = yes ] && [ "$s5" = yes ] && [ "$pins10" -ge 1 ] && [ "$table" = yes ] && [ "$v30" = yes ]; then
    echo "HIT try=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$i" -ge 40 ]; then break; fi
  sleep 20
done
echo "ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
