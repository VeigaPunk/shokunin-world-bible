#!/usr/bin/env bash
# V06 poll: artifacts (S1 contract pins + r98 fixture) AND producer reports.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  s1rep=$(ls .ufo/waves/round-98/seats/ 2>/dev/null | grep -E '^S1' | tr '\n' ' ')
  pins=$(python3 - <<'PY' 2>/dev/null
import json
try:
    c=json.load(open('corpus/tools/dependency-freeze-contract.json'))
    print(','.join(sorted(c.get('pins',{}))))
except Exception as e:
    print('ERR',e)
PY
)
  r98fix=$([ -f corpus/fixtures/r98-clerk-filing/timeline.json ] && echo yes || echo no)
  r97fix=$([ -f corpus/fixtures/r97-crossing-acknowledgment/timeline.json ] && echo yes || echo no)
  echo "try $i $ts | S1reports=[$s1rep] r98fix=$r98fix r97fix=$r97fix pins=[$pins]"
  if echo "$pins" | grep -q r97-crossing-acknowledgment && echo "$pins" | grep -q r98-clerk-filing && [ "$r98fix" = yes ] && [ -n "$s1rep" ]; then
    echo "POLL-SATISFIED at try $i"
    exit 0
  fi
  sleep 20
done
echo "POLL-TIMEOUT"
exit 1
