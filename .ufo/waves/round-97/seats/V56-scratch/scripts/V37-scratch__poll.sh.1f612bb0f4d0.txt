#!/bin/bash
# V37 poll: producer artifacts + producer reports; 40 tries x 20s.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-97/seats/V37-scratch/poll.log
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date +%FT%T%z)
  have=1; miss=""
  # artifacts
  [ -f corpus/fixtures/r97-crossing-acknowledgment/entities.json ] || { have=0; miss="$miss r97-entities"; }
  [ -f corpus/fixtures/r97-crossing-acknowledgment/sources.json ] || { have=0; miss="$miss r97-sources"; }
  [ -f corpus/fixtures/r97-crossing-acknowledgment/timeline.json ] || { have=0; miss="$miss r97-timeline"; }
  [ -f corpus/fixtures/r97-crossing-acknowledgment/README.md ] || { have=0; miss="$miss r97-README"; }
  [ -f corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md ] || { have=0; miss="$miss r97-map"; }
  [ -f corpus/knowledge/r97-acknowledgment-scope-note.md ] || { have=0; miss="$miss r97-note"; }
  # producer reports
  for p in R1 R2 R3 R4 R5 R6; do
    ls .ufo/waves/round-97/seats/${p}-*.md >/dev/null 2>&1 || { have=0; miss="$miss $p-report"; }
  done
  # quick artifact-state snapshot
  mc=$(python3 -c "import json;print(len(json.load(open('corpus/tools/map-obligations-contract.json'))['self_test']['cases']))" 2>/dev/null)
  fc=$(python3 -c "import json;d=json.load(open('corpus/tools/dependency-freeze-contract.json'));st=d.get('self_test');print(len(st['cases']) if isinstance(st,dict) and 'cases' in st else 'nocases')" 2>/dev/null)
  mh=$(sha256sum corpus/tools/map_obligations.py | cut -c1-12)
  fh=$(sha256sum corpus/tools/dependency_freeze.py | cut -c1-12)
  mapdiff=$(git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | tail -1)
  echo "$ts try=$i have=$have miss=[$miss] mapcases=$mc freezecases=$fc map_ob=$mh dep_fr=$fh r96map=[$mapdiff]" >> "$LOG"
  if [ "$have" = 1 ]; then echo "ALL-PRESENT at try $i" >> "$LOG"; exit 0; fi
  sleep 20
done
echo "TIMEOUT after 40 tries" >> "$LOG"
exit 1
