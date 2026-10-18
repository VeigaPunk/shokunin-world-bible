#!/bin/bash
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V78-scratch/poll.log
cd "$ROOT"
for try in $(seq 16 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  {
    echo "=== TRY $try $ts ==="
    missing=0
    for r in S1-freeze-hygiene.md S2-tools-docs.md S3-fixture-author.md S4-fixture-docs.md S5-knowledge-notes.md; do
      if [ -s "$SEATS/$r" ]; then echo "PRESENT $r $(stat -c '%y %s' "$SEATS/$r")"; else echo "ABSENT $r"; missing=1; fi
    done
    if [ -d corpus/fixtures/r99-window-lapse ]; then echo "FIXTURE_FILES $(ls corpus/fixtures/r99-window-lapse | wc -l)"; else echo "ABSENT fixture"; missing=1; fi
    for k in corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md; do
      if [ -s "$k" ]; then echo "PRESENT $k $(stat -c '%y %s' "$k")"; else echo "ABSENT $k"; missing=1; fi
    done
    sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
    python3 - << 'PY'
import json
d=json.load(open("corpus/tools/dependency-freeze-contract.json"))
pins=d.get("pins") or {}
print("PINS", list(pins))
print("R99_PINNED", "r99-window-lapse" in pins)
nfiles={k: len((v or {}).get("files") or {}) for k,v in pins.items()}
print("NFILES", nfiles)
print("EXPECTED", len((d.get("self_test") or {}).get("expected") or {}))
print("SCHEMA", d.get("schema_version"))
PY
    if [ "$missing" = 0 ]; then echo "ALL-PRESENT try=$try"; else echo "WAITING try=$try"; fi
  } >> "$LOG"
  if [ "$missing" = 0 ]; then
    echo "ALL-PRESENT try=$try $ts"
    exit 0
  fi
  sleep 20
done
echo "POLL-EXHAUSTED" >> "$LOG"
echo "POLL-EXHAUSTED"
exit 1
