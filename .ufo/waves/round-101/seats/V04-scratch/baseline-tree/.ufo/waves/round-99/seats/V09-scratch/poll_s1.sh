#!/bin/bash
# Poll for S1 report + stable schema-2 ten-file r96 pin. 20s cadence.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V09-scratch/poll.log
MAX=${1:-32}
prev=""
i=0
while [ "$i" -lt "$MAX" ]; do
  i=$((i+1))
  now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  reports=$(ls -1 "$SEATS"/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ')
  s1=$(ls -1 "$SEATS"/S1*.md 2>/dev/null | head -1)
  tool_sha=$(sha256sum "$LANE/corpus/tools/dependency_freeze.py" | awk '{print $1}')
  contract_sha=$(sha256sum "$LANE/corpus/tools/dependency-freeze-contract.json" | awk '{print $1}')
  pin=$(python3 - <<'PY'
import json
c=json.load(open("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json"))
p=c.get("pins",{}).get("r96-crossing-response",{})
files=sorted((p.get("files") or {}))
print(f"schema={p.get('payload_schema_version')} nfiles={len(files)} md={'fictional-excerpts.md' in files} cases={len(c.get('self_test',{}).get('expected',{}))}")
PY
)
  echo "===== $now TRY i=$i reports=[${reports:-none}] s1=${s1:-ABSENT} tool=$tool_sha contract=$contract_sha $pin" | tee -a "$LOG"
  key="$tool_sha $contract_sha $pin"
  if [ -n "$s1" ] && echo "$pin" | grep -q 'schema=2 nfiles=10' && [ "$key" = "$prev" ]; then
    echo "POLL_STABLE try=$i s1=$s1 tool=$tool_sha contract=$contract_sha" | tee -a "$LOG"
    exit 0
  fi
  prev=$key
  if [ "$i" -lt "$MAX" ]; then
    sleep 20
  fi
done
echo "POLL_EXHAUSTED tries=$i s1=${s1:-ABSENT}" | tee -a "$LOG"
exit 2
