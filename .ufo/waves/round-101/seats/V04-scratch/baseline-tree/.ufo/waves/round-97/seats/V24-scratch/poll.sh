#!/bin/bash
# V24 scope-creep poll — round 97. 20s cadence, 75 min cap.
SEATS=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
LOG=$SEATS/V24-scratch/poll.log
cd "$REPO" || exit 1
MAX=4500
s=0; n=0; stable=0; prevP=""; prevS=""; prevC=""
echo "$(date '+%F %H:%M:%S') POLL_START cap=${MAX}s" >> "$LOG"
while [ $s -lt $MAX ]; do
  R=$(ls "$SEATS" 2>/dev/null | grep -cE '^R[1-6]-.*\.md$')
  V=$(ls "$SEATS" 2>/dev/null | grep -cE '^V[0-9]{2}-.*\.md$')
  ALL=$((R+V))
  MISS=$(ls "$SEATS" 2>/dev/null | grep -E '^R[1-6]-.*\.md$' | sed 's/-.*//' | sort | tr '\n' ',')
  PSIG=$(find corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response/claim-excerpt-map.md corpus/fixtures/r97-crossing-acknowledgment corpus/knowledge/r97-acknowledgment-scope-note.md -type f -printf '%T@ %s %p\n' 2>/dev/null | sort | md5sum | cut -c1-12)
  SSIG=$(find "$SEATS" -maxdepth 1 -name '*.md' -printf '%T@ %s\n' 2>/dev/null | sort | md5sum | cut -c1-12)
  PORC=$(git status --porcelain -uall 2>/dev/null | wc -l)
  echo "$(date '+%H:%M:%S') t=${s}s R=$R V=$V all=$ALL producers=[$MISS] psig=$PSIG ssig=$SSIG porc=$PORC" >> "$LOG"
  if [ "$ALL" -ge 64 ]; then
    if [ "$PSIG" = "$prevP" ] && [ "$SSIG" = "$prevS" ] && [ "$PORC" = "$prevC" ]; then
      stable=$((stable+1))
    else
      stable=0
    fi
  fi
  prevP=$PSIG; prevS=$SSIG; prevC=$PORC
  if [ "$stable" -ge 3 ]; then
    echo "$(date '+%F %H:%M:%S') DONE all=$ALL stable=$stable elapsed=${s}s" >> "$LOG"
    exit 0
  fi
  sleep 20; s=$((s+20)); n=$((n+1))
done
echo "$(date '+%F %H:%M:%S') CAP all=$ALL stable=$stable elapsed=${s}s" >> "$LOG"
exit 0
