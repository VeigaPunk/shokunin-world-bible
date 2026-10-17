#!/bin/bash
# V11 c2-anchors poll for Q4/Q5 r96 artifacts (40 tries, 20 s cadence, 20 s stability window)
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SC=.ufo/waves/round-96/seats/V11-scratch
FIX=corpus/fixtures/r96-crossing-response
SEATS=.ufo/waves/round-96/seats
LOG=$SC/poll.log
: > "$LOG"
rm -f "$SC/READY"
prev=""
for try in $(seq 1 40); do
  ts=$(date -u +%H:%M:%S)
  map=n; fx=n; src=n; q4rep=none; q5rep=none
  [ -f "$FIX/claim-excerpt-map.md" ] && map=y
  [ -f "$FIX/fictional-excerpts.md" ] && fx=y
  [ -f "$FIX/source-excerpt.md" ] && src=y
  q4=$(ls $SEATS/Q4*.md 2>/dev/null | head -1); [ -n "$q4" ] && q4rep=$q4
  q5=$(ls $SEATS/Q5*.md 2>/dev/null | head -1); [ -n "$q5" ] && q5rep=$q5
  if [ "$map" = y ] && [ "$fx" = y ] && [ "$src" = y ] && [ "$q4rep" != none ] && [ "$q5rep" != none ]; then
    cur=$(cat "$FIX/claim-excerpt-map.md" "$FIX/fictional-excerpts.md" | md5sum | cut -d' ' -f1)
    if [ -n "$prev" ] && [ "$cur" = "$prev" ]; then
      md5sum "$FIX/claim-excerpt-map.md" "$FIX/fictional-excerpts.md" "$FIX/source-excerpt.md" > "$SC/pins.txt"
      echo "try=$try $ts READY-STABLE md5set=$cur map=$map fx=$fx src=$src q4rep=$q4rep q5rep=$q5rep" >> "$LOG"
      date -u +%H:%M:%S > "$SC/READY"
      exit 0
    fi
    prev=$cur
    echo "try=$try $ts stability-wait md5set=$cur map=$map fx=$fx src=$src q4rep=$q4rep q5rep=$q5rep" >> "$LOG"
  else
    prev=""
    echo "try=$try $ts map=$map fx=$fx src=$src q4rep=$q4rep q5rep=$q5rep" >> "$LOG"
  fi
  sleep 20
done
echo "TIMEOUT-NO-READY after 40 tries" >> "$LOG"
date -u +%H:%M:%S > "$SC/TIMEOUT"
exit 3
