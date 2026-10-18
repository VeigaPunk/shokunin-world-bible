#!/usr/bin/env bash
# V09 poll-wait loop: artifact + producer report, 20s spacing, max 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
LOG=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats/V09-scratch/poll.log
ART=corpus/knowledge/r101-r10-register-first-entry.md
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  a=no; r=no
  [ -f "$ART" ] && a=yes
  ls .ufo/waves/round-101/seats/ 2>/dev/null | grep -qi '^U2' && r=yes
  echo "try=$i ts=$ts artifact=$a u2report=$r" >> "$LOG"
  if [ "$a" = yes ] && [ "$r" = yes ]; then
    echo "try=$i ts=$ts BOTH_PRESENT" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "try=40 ts=$(date +%H:%M:%S) EXHAUSTED" >> "$LOG"
exit 3
