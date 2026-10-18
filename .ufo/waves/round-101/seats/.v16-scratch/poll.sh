#!/bin/bash
# V16 poll: wait for U2 artifact + both producer reports. 40 tries x 20s.
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats
ART=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r101-r10-register-first-entry.md
for i in $(seq 1 40); do
  ok=1
  [ -f "$ART" ] || ok=0
  ls "$SEATS"/U1-*.md >/dev/null 2>&1 || ok=0
  ls "$SEATS"/U2-*.md >/dev/null 2>&1 || ok=0
  if [ "$ok" -eq 1 ]; then echo "ALL-PRESENT try=$i $(date +%H:%M:%S)"; ls "$SEATS"; exit 0; fi
  echo "try=$i absent $(date +%H:%M:%S) art=$([ -f "$ART" ] && echo Y || echo N) u1=$(ls "$SEATS"/U1-*.md 2>/dev/null | wc -l) u2=$(ls "$SEATS"/U2-*.md 2>/dev/null | wc -l)"
  sleep 20
done
echo "STILL-ABSENT after 40 tries"
exit 1
