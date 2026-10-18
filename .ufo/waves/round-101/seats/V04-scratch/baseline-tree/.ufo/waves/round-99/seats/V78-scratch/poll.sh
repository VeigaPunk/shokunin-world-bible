#!/bin/bash
# V78 producer poll. Existence + content gates. Never verifies a plan.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V78-scratch/poll.log
cd "$ROOT"
for try in $(seq 1 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  {
    echo "=== TRY $try $ts ==="
    missing=0
    for r in S1-freeze-hygiene.md S2-tools-docs.md S3-fixture-author.md S4-fixture-docs.md S5-knowledge-notes.md; do
      if [ -s "$SEATS/$r" ]; then
        echo "PRESENT $r $(stat -c '%y %s' "$SEATS/$r")"
      else
        echo "ABSENT $r"
        missing=1
      fi
    done
    if [ -d corpus/fixtures/r99-window-lapse ]; then
      echo "FIXTURE_FILES $(ls corpus/fixtures/r99-window-lapse | wc -l)"
      ls -la corpus/fixtures/r99-window-lapse
    else
      echo "ABSENT fixture"
      missing=1
    fi
    for k in corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md; do
      if [ -s "$k" ]; then echo "PRESENT $k $(stat -c '%y %s' "$k")"; else echo "ABSENT $k"; missing=1; fi
    done
    sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>/dev/null || true
    python3 - << 'PY'
import json, os
p="corpus/tools/dependency-freeze-contract.json"
try:
    d=json.load(open(p))
except Exception as e:
    print("CONTRACT_UNREADABLE", e)
    raise SystemExit
st=d.get("self_test") or {}
cases=st.get("cases") if isinstance(st, dict) else None
n=len(cases) if isinstance(cases, (list, dict)) else None
pins=list((d.get("pins") or {}))
print("CONTRACT schema", d.get("schema_version"), "cases", n, "expected", st.get("expected") if isinstance(st, dict) else None)
print("PINS", pins)
print("R99_PINNED", "r99-window-lapse" in (d.get("pins") or {}))
req=d.get("required_files") or d.get("data_files")
print("FILE_LIST_KEY", "required_files" if "required_files" in d else "", "data_files" if "data_files" in d else "")
PY
    if [ "$missing" = 0 ]; then
      echo "ALL-PRESENT try=$try"
    else
      echo "WAITING try=$try"
    fi
  } >> "$LOG"
  if [ "$missing" = 0 ]; then
    echo "ALL-PRESENT try=$try $ts"
    exit 0
  fi
  sleep 20
done
echo "POLL-EXHAUSTED"
exit 1
