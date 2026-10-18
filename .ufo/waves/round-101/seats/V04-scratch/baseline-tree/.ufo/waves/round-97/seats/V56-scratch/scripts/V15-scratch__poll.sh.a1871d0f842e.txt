#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
F=corpus/fixtures/r97-crossing-acknowledgment
for i in $(seq 1 40); do
  files=0
  [ -f "$F/README.md" ] && files=$((files+1))
  [ -f "$F/claim-excerpt-map.md" ] && files=$((files+1))
  rep=$(ls .ufo/waves/round-97/seats/R5*.md 2>/dev/null | head -1)
  echo "try=$i $(date -Is) files=$files/2 report=${rep:-none}"
  if [ "$files" -eq 2 ] && [ -n "$rep" ]; then echo "READY"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"; exit 1
