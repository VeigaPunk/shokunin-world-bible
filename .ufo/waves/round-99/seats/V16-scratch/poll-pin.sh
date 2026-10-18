#!/bin/sh
# Resume pin poll. Previous run died at try 15 (shell timeout). Append, do not truncate.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
CONTRACT=$LANE/corpus/tools/dependency-freeze-contract.json
LOG=$LANE/.ufo/waves/round-99/seats/V16-scratch/poll-pin.log
i=15
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  pin=$(python3 -c '
import json,sys
c=json.load(open(sys.argv[1]))
p=c.get("pins",{}).get("r99-window-lapse")
if not isinstance(p, dict):
    print("no")
    raise SystemExit(0)
ev=(p.get("events") or {}).get("clerk-lapse-recorded") or {}
print("yes")
print("deps="+json.dumps(ev.get("depends_on")))
print("nfiles="+str(len(p.get("files") or {})))
print("counts="+json.dumps(p.get("counts")))
' "$CONTRACT" 2>/dev/null || echo no)
  s1=$(ls -1 "$LANE"/.ufo/waves/round-99/seats/S1*.md 2>/dev/null | head -3 | tr '\n' ',')
  echo "try=$i ts=$ts s1=${s1:-none}" | tee -a "$LOG"
  echo "$pin" | tee -a "$LOG"
  case "$pin" in
    yes*)
      echo "PIN_HIT try=$i ts=$ts" | tee -a "$LOG"
      exit 0
      ;;
  esac
  if [ "$i" -ge 40 ]; then
    break
  fi
  sleep 20
done
echo "PIN_ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
