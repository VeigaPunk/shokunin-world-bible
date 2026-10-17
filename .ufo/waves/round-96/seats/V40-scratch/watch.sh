#!/bin/bash
S=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats
L=$S/V40-scratch/watch.log
R=/home/vgpnk/Projects/shokunin/lore-shokunin
declare -A seen
for f in "$S"/*.md; do [ -e "$f" ] && seen["$(basename "$f")"]=1; done
echo "$(date -Iseconds) WATCHER start; existing=$(ls "$S"/*.md 2>/dev/null | wc -l)" >> "$L"
for i in $(seq 1 180); do
  for f in "$S"/*.md; do
    [ -e "$f" ] || continue
    b=$(basename "$f")
    if [ -z "${seen[$b]}" ]; then
      seen["$b"]=1
      echo "$(date -Iseconds) NEW $b" >> "$L"
    fi
  done
  echo "$(date -Iseconds) tick $i seats=$(ls "$S"/*.md 2>/dev/null | wc -l) tool=$(sha256sum $R/corpus/tools/map_obligations.py 2>/dev/null | cut -c1-8) contract=$(sha256sum $R/corpus/tools/map-obligations-contract.json 2>/dev/null | cut -c1-8) dfz=$([ -f $R/corpus/tools/dependency_freeze.py ] && echo yes || echo no) fixture=$(ls $R/corpus/fixtures/r96-crossing-response/ 2>/dev/null | wc -l) note=$([ -f $R/corpus/knowledge/r96-response-scope-note.md ] && echo yes || echo no)" >> "$L"
  sleep 20
done
echo "$(date -Iseconds) WATCHER end" >> "$L"
