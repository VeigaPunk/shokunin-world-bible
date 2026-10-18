#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  ts=$(date +%H:%M:%S)
  pins=$(python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print('pins='+','.join(sorted(c['pins']))+' n='+str(len(c['pins']))+' st='+str(len(c.get('self_test',{}).get('expected',{}))))" 2>&1)
  rep=""
  for s in S1 S2 S3 S4 S5; do
    if ls .ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1; then rep="$rep $s:Y"; else rep="$rep $s:N"; fi
  done
  c1=$(grep -c 'clerk-maren' corpus/fixtures/r98-clerk-filing/entities.json 2>/dev/null || echo 0)
  c2=$(grep -c 'clerk-filing-note' corpus/fixtures/r98-clerk-filing/sources.json 2>/dev/null || echo 0)
  c3=$(grep -c 'clerk-filing-open' corpus/fixtures/r98-clerk-filing/timeline.json 2>/dev/null || echo 0)
  c4=$(test -f corpus/knowledge/r98-clerk-scope-note.md && echo Y || echo N)
  c5=$(grep -c 'r98' corpus/knowledge/r95-aftermath-scope-note.md 2>/dev/null || echo 0)
  c6=$(grep -c 'r98' corpus/knowledge/r96-response-scope-note.md 2>/dev/null || echo 0)
  echo "$ts try=$i $pins rep:$rep r98[ent=$c1 src=$c2 tl=$c3 note=$c4 r95add=$c5 r96add=$c6]"
  if [ "$c1" -ge 1 ] && [ "$c2" -ge 1 ] && [ "$c3" -ge 1 ] && [ "$c4" = Y ] && [ "$c5" -ge 1 ] && [ "$c6" -ge 1 ] && [ "$rep" = " S1:Y S2:Y S3:Y S4:Y S5:Y" ]; then
    echo "ALL PRESENT try=$i"; exit 0
  fi
  sleep 20
done
echo "POLL EXHAUSTED"; exit 3
