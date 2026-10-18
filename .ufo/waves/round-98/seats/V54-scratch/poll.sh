#!/bin/bash
# V54 poll: six pins in contract + r97/r98 fixture data files (artifacts);
# producer reports S1/S3 logged each try (endgame: SELF not in wait list).
R=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$R/.ufo/waves/round-98/seats/V54-scratch
LOG=$SC/V54-poll.log
: > "$LOG"
for i in $(seq 1 40); do
  missing=""
  out=$(python3 - "$R/corpus/tools/dependency-freeze-contract.json" <<'PY'
import json,sys
c=json.load(open(sys.argv[1]))
want=["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing"]
miss=[w for w in want if w not in c.get("pins",{})]
print(",".join(miss))
PY
)
  [ -n "$out" ] && missing="$missing PINS:$out"
  for f in r97-crossing-acknowledgment/timeline.json r97-crossing-acknowledgment/entities.json r97-crossing-acknowledgment/sources.json r97-crossing-acknowledgment/relations.json r98-clerk-filing/timeline.json r98-clerk-filing/entities.json r98-clerk-filing/sources.json r98-clerk-filing/relations.json; do
    [ -s "$R/corpus/fixtures/$f" ] || missing="$missing $f"
  done
  reports=""
  for s in S1 S3 S4 S5; do
    ls "$R"/.ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 && reports="$reports $s" || reports="$reports -$s"
  done
  if [ -z "$missing" ]; then
    echo "ARTIFACTS-PRESENT try $i $(date -u +%H:%M:%S) reports:$reports" | tee -a "$LOG"
    exit 0
  fi
  echo "try $i $(date -u +%H:%M:%S) missing:$missing reports:$reports" >> "$LOG"
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries $(date -u +%H:%M:%S)" | tee -a "$LOG"
exit 1
