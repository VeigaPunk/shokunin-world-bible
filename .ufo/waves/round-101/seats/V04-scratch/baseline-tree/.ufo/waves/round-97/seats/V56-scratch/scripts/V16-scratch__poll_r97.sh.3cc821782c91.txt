#!/bin/bash
# V16 poll-wait: r97 fixture artifacts (R4: excerpts+JSON; R5: map+README) + R4/R5 seat reports
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-97/seats/V16-scratch/poll.log
F=corpus/fixtures/r97-crossing-acknowledgment
: > "$LOG"
for i in $(seq 1 40); do
  map=$([ -f $F/claim-excerpt-map.md ] && echo y || echo n)
  rme=$([ -f $F/README.md ] && echo y || echo n)
  fx=$([ -f $F/fictional-excerpts.md ] && echo y || echo n)
  src=$([ -f $F/source-excerpt.md ] && echo y || echo n)
  sj=$([ -f $F/sources.json ] && echo y || echo n)
  tj=$([ -f $F/timeline.json ] && echo y || echo n)
  ent=$([ -f $F/entities.json ] && echo y || echo n)
  r4=$(ls .ufo/waves/round-97/seats/R4-*.md 2>/dev/null | head -1)
  r5=$(ls .ufo/waves/round-97/seats/R5-*.md 2>/dev/null | head -1)
  echo "try=$i $(date +%H:%M:%S) map=$map rme=$rme fx=$fx src=$src sj=$sj tj=$tj ent=$ent r4=${r4:-none} r5=${r5:-none}" >> "$LOG"
  if [ "$map$rme$fx$src$sj$tj$ent" = "yyyyyyy" ] && [ -n "$r4" ] && [ -n "$r5" ]; then
    m1=$(md5sum $F/claim-excerpt-map.md $F/README.md $F/fictional-excerpts.md $F/source-excerpt.md $F/sources.json $F/timeline.json 2>/dev/null | md5sum | cut -d' ' -f1)
    sleep 20
    m2=$(md5sum $F/claim-excerpt-map.md $F/README.md $F/fictional-excerpts.md $F/source-excerpt.md $F/sources.json $F/timeline.json 2>/dev/null | md5sum | cut -d' ' -f1)
    if [ "$m1" = "$m2" ]; then
      echo "READY-STABLE try=$i md5set=$m2" >> "$LOG"
      exit 0
    else
      echo "UNSTABLE try=$i m1=$m1 m2=$m2" >> "$LOG"
    fi
  fi
  sleep 20
done
echo "POLL-TIMEOUT tries=40" >> "$LOG"
exit 1
