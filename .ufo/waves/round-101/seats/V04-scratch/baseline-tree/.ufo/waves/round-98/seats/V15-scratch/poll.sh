#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a
for i in $(seq 1 40); do
  cur=$(sha256sum corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | cut -d' ' -f1)
  s3=$(ls .ufo/waves/round-98/seats/S3*.md 2>/dev/null | head -1)
  echo "try=$i ts=$(date +%H:%M:%S) map=$cur s3report=${s3:-NONE}"
  if [ "$cur" != "$BASE" ] && [ -n "$s3" ]; then
    echo "READY try=$i"
    exit 0
  fi
  sleep 20
done
echo "POLL-TIMEOUT"
exit 1
