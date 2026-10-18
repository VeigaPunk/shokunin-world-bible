#!/bin/bash
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$ROOT/.ufo/waves/round-99/seats/V117-scratch/poll.log
cd "$ROOT"
for i in $(seq 1 36); do
  ts=$(date -Is)
  reports=$(ls -1 .ufo/waves/round-99/seats/S*.md 2>/dev/null | wc -l)
  s1=$(ls -1 .ufo/waves/round-99/seats/S1-*.md 2>/dev/null | wc -l)
  s2=$(ls -1 .ufo/waves/round-99/seats/S2-*.md 2>/dev/null | wc -l)
  s5=$(ls -1 .ufo/waves/round-99/seats/S5-*.md 2>/dev/null | wc -l)
  know=$(ls -1 corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md 2>/dev/null | wc -l)
  pins=$(python3 -c 'import json;c=json.load(open("corpus/tools/dependency-freeze-contract.json"));pins=c.get("pins",{});
print(len(pins), ",".join(sorted(pins)), "ten="+str(sum(1 for p in pins.values() if isinstance(p.get("files"),dict) and len(p["files"])==10)))' 2>/dev/null)
  seatmd=$(ls -1 .ufo/waves/round-99/seats/*.md 2>/dev/null | wc -l)
  echo "$ts try=$i s_reports=$reports s1=$s1 s2=$s2 s5=$s5 know=$know pins=[$pins] seatmd=$seatmd" >> "$LOG"
  if [ "$s1" -ge 1 ] && [ "$s2" -ge 1 ] && [ "$s5" -ge 1 ] && [ "$know" -ge 2 ]; then
    echo "$ts READY" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "$(date -Is) EXHAUSTED" >> "$LOG"
exit 3
