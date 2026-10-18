#!/bin/bash
# V49 poll: S1/S3 reports + V26 report + C2 artifacts (contract pins r97+r98, r98 JSON tables)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  missing=""
  # contract pins
  python3 - "$R" <<'PY' || missing="$missing CONTRACT-PINS"
import json,sys
r=sys.argv[1]
try:
    c=json.load(open(r+"/corpus/tools/dependency-freeze-contract.json"))
    p=c.get("pins",{})
    for k in ("r97-crossing-acknowledgment","r98-clerk-filing"):
        if k not in p: raise SystemExit(1)
except Exception:
    raise SystemExit(1)
PY
  # r98 json tables
  for f in entities.json relations.json timeline.json sources.json contradictions.json; do
    [ -s "$R/corpus/fixtures/r98-clerk-filing/$f" ] || missing="$missing r98/$f"
  done
  # producer reports + V26
  for s in S1 S3 V26; do
    ls "$R"/.ufo/waves/round-98/seats/${s}-*.md >/dev/null 2>&1 || missing="$missing REPORT:$s"
  done
  if [ -z "$missing" ]; then echo "ALL-PRESENT at try $i $(date -u +%H:%M:%S)"; exit 0; fi
  echo "try $i $(date -u +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-TIMEOUT after 40 tries $(date -u +%H:%M:%S)"
exit 1
