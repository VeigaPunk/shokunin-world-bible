#!/bin/bash
# V25 poll-wait: artifacts + producer reports. 20s cadence, max 40 tries.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V25-scratch/poll.log
cd "$ROOT" || exit 1
for try in $(seq 1 40); do
  ts=$(date -Is)
  s1rep=$(ls -1 "$SEATS"/S1*.md 2>/dev/null | wc -l)
  s2rep=$(ls -1 "$SEATS"/S2*.md 2>/dev/null | wc -l)
  s5rep=$(ls -1 "$SEATS"/S5*.md 2>/dev/null | wc -l)
  know=$(ls -1 corpus/knowledge/r99-* 2>/dev/null | wc -l)
  pinstate=$(python3 - << 'PY'
import json
c=json.load(open("corpus/tools/dependency-freeze-contract.json"))
pins=c.get("pins") or {}
ten=0
for name, pin in pins.items():
    files=pin.get("files")
    n=len(files) if isinstance(files, (list, dict)) else 0
    ver=pin.get("payload_schema_version")
    if n==10 and ver==2:
        ten+=1
print(f"pins={len(pins)} ten_v2={ten} cases={len(c.get('self_test',{}).get('expected',{}))} schema={c.get('schema_version')} payload={c.get('payload_schema_version')}")
PY
)
  skill18=$(grep -c "18 cases" SKILL.md || true)
  tools18=$(grep -c "18 cases\|18-case\|ten files\|ten-file\|payload_schema_version 2" corpus/tools/README.md || true)
  echo "try=$try ts=$ts s1rep=$s1rep s2rep=$s2rep s5rep=$s5rep know=$know skill18=$skill18 tools18=$tools18 $pinstate" | tee -a "$LOG"
  if [ "$s1rep" -ge 1 ] && [ "$s2rep" -ge 1 ] && [ "$s5rep" -ge 1 ] && [ "$know" -ge 1 ]; then
    echo "READY try=$try ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "TIMEOUT tries=40 ts=$(date -Is)" | tee -a "$LOG"
exit 2
