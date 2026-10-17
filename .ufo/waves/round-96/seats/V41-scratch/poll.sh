#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
F=$R/corpus/fixtures/r96-crossing-response
need() {
  # Q1 tool revision changed
  [ "$(md5sum $R/corpus/tools/map_obligations.py | cut -d' ' -f1)" != "d31b8182953e9088a155f4ed2978af5b" ] && \
  [ "$(md5sum $R/corpus/tools/map-obligations-contract.json | cut -d' ' -f1)" != "d2a77aa09e5cd38d73d772bb11a5914e" ] && \
  [ "$(md5sum $R/corpus/tools/README.md | cut -d' ' -f1)" != "9334067f0aeb3151beff341da9d18758" ] && \
  [ -f $R/corpus/tools/dependency_freeze.py ] && [ -f $R/corpus/tools/dependency-freeze-contract.json ] && \
  [ -f $F/sources.json ] && [ -f $F/timeline.json ] && [ -f $F/fictional-excerpts.md ] && [ -f $F/README.md ] && [ -f $F/claim-excerpt-map.md ] && \
  [ -f $R/corpus/knowledge/r96-response-scope-note.md ] && \
  [ -n "$(ls $S/Q1* 2>/dev/null)" ] && [ -n "$(ls $S/Q2* 2>/dev/null)" ] && [ -n "$(ls $S/Q3* 2>/dev/null)" ] && \
  [ -n "$(ls $S/Q4* 2>/dev/null)" ] && [ -n "$(ls $S/Q5* 2>/dev/null)" ] && [ -n "$(ls $S/Q6* 2>/dev/null)" ]
}
for i in $(seq 1 45); do
  if need; then echo "READY at try $i $(date +%T)"; ls $S/Q*.md 2>/dev/null; exit 0; fi
  echo "try $i $(date +%T) not-ready: q1=$( [ "$(md5sum $R/corpus/tools/map_obligations.py|cut -d' ' -f1)" != d31b8182953e9088a155f4ed2978af5b ] && echo y || echo n) q3=$( [ -f $R/corpus/tools/dependency_freeze.py ] && echo y || echo n) q4=$( [ -f $F/claim-excerpt-map.md ] && echo y || echo n) q6=$( [ -f $R/corpus/knowledge/r96-response-scope-note.md ] && echo y || echo n) reports=$(ls $S/Q*.md 2>/dev/null | wc -l)"
  sleep 20
done
echo "TIMEOUT after 45 tries $(date +%T)"; exit 1
