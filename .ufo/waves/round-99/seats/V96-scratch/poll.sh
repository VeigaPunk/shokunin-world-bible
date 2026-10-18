#!/bin/bash
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SCRATCH=$LANE/.ufo/waves/round-99/seats/V96-scratch
LOG=$SCRATCH/poll.log
cd "$LANE"
max=40
for i in $(seq 1 $max); do
  ts=$(date -Is)
  reports=$(ls -1 .ufo/waves/round-99/seats/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ')
  s1=$(ls -1 .ufo/waves/round-99/seats/S1*.md 2>/dev/null | wc -l)
  s2=$(ls -1 .ufo/waves/round-99/seats/S2*.md 2>/dev/null | wc -l)
  skill_m=$(stat -c '%y' SKILL.md)
  readme_m=$(stat -c '%y' corpus/tools/README.md)
  py_m=$(stat -c '%y' corpus/tools/dependency_freeze.py)
  con_m=$(stat -c '%y' corpus/tools/dependency-freeze-contract.json)
  py_h=$(sha256sum corpus/tools/dependency_freeze.py | awk '{print $1}')
  con_h=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
  skill_h=$(sha256sum SKILL.md | awk '{print $1}')
  schema=$(python3 - << 'PY'
import json
from pathlib import Path
d=json.loads(Path("corpus/tools/dependency-freeze-contract.json").read_text())
pins=d.get("pins",{})
vers=sorted({str((p or {}).get("payload_schema_version")) for p in pins.values()}) if isinstance(pins, dict) else []
exp=d.get("self_test",{}).get("expected",{})
print(f"schema_top={d.get('schema_version')!s} pin_vers={','.join(vers)} pins={len(pins)} cases={len(exp)} case_has_md={'markdown_tamper' in exp}")
PY
)
  echo "try=$i ts=$ts s1=$s1 s2=$s2 reports=[$reports] skill_m=$skill_m readme_m=$readme_m py_m=$py_m con_m=$con_m" >> "$LOG"
  echo "  hashes py=$py_h con=$con_h skill=$skill_h $schema" >> "$LOG"
  if [ "$s1" -ge 1 ] && [ "$s2" -ge 1 ]; then
    # require non-empty and size-stable vs previous try
    s1f=$(ls -1 .ufo/waves/round-99/seats/S1*.md | head -1)
    s2f=$(ls -1 .ufo/waves/round-99/seats/S2*.md | head -1)
    s1sz=$(stat -c '%s' "$s1f")
    s2sz=$(stat -c '%s' "$s2f")
    echo "  landed s1=$s1f:$s1sz s2=$s2f:$s2sz" >> "$LOG"
    if [ -f "$SCRATCH/poll-prev-sizes" ]; then
      prev=$(cat "$SCRATCH/poll-prev-sizes")
      now="$s1sz $s2sz $py_h $con_h $skill_h"
      if [ "$prev" = "$now" ] && [ "$s1sz" -gt 200 ] && [ "$s2sz" -gt 200 ]; then
        echo "STABLE try=$i" >> "$LOG"
        echo STABLE
        exit 0
      fi
    fi
    echo "$s1sz $s2sz $py_h $con_h $skill_h" > "$SCRATCH/poll-prev-sizes"
  fi
  if [ "$i" -eq "$max" ]; then
    echo "EXHAUSTED try=$i s1=$s1 s2=$s2" >> "$LOG"
    echo EXHAUSTED
    exit 3
  fi
  sleep 20
done
