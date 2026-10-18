#!/bin/bash
# V26 poll: producers S1/S3/S4 reports + contract r97/r98 pins + r98 fixture complete
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=.ufo/waves/round-98/seats
for i in $(seq 1 40); do
  S1=$(ls $SEATS/S1-*.md 2>/dev/null | head -1)
  S3=$(ls $SEATS/S3-*.md 2>/dev/null | head -1)
  S4=$(ls $SEATS/S4-*.md 2>/dev/null | head -1)
  PINS=$(python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print('r97-crossing-acknowledgment' in c['pins'] and 'r98-clerk-filing' in c['pins'])" 2>/dev/null)
  CLERK=$(python3 -c "import json;e=json.load(open('corpus/fixtures/r98-clerk-filing/entities.json'));print(any(r.get('id')=='clerk-maren' for r in e))" 2>/dev/null)
  echo "try=$i S1=${S1:-none} S3=${S3:-none} S4=${S4:-none} pins_r97r98=$PINS clerk_maren=$CLERK $(date +%H:%M:%S)"
  if [ -n "$S1" ] && [ -n "$S3" ] && [ -n "$S4" ] && [ "$PINS" = "True" ] && [ "$CLERK" = "True" ]; then
    echo "READY"; exit 0
  fi
  sleep 20
done
echo "TIMEOUT"; exit 1
