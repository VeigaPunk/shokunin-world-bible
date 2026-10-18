#!/bin/bash
# V31 poll-wait: artifacts AND producer reports. 20s cadence, 40 tries.
# Existence + content gates so r98 placeholders are not treated as delivered.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V31-scratch/poll.log"
cd "$ROOT" || exit 1

need_files=(
  corpus/fixtures/r99-window-lapse/entities.json
  corpus/fixtures/r99-window-lapse/relations.json
  corpus/fixtures/r99-window-lapse/timeline.json
  corpus/fixtures/r99-window-lapse/sources.json
  corpus/fixtures/r99-window-lapse/contradictions.json
  corpus/fixtures/r99-window-lapse/README.md
  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
  corpus/fixtures/r99-window-lapse/inspiration-note.md
  corpus/fixtures/r99-window-lapse/source-excerpt.md
  corpus/knowledge/r99-gate-blind-spot-table.md
  corpus/knowledge/r99-lapse-scope-note.md
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
)

echo "POLL-START $(date '+%Y-%m-%d %H:%M:%S %z')" >> "$LOG"

for try in $(seq 1 40); do
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  missing=()
  for f in "${need_files[@]}"; do
    if [[ ! -s "$f" ]]; then
      missing+=("ABSENT:$f")
    fi
  done

  # content gates: not the r98 placeholder
  if [[ -s corpus/fixtures/r99-window-lapse/README.md ]]; then
    if grep -q 'Round 98 clerk-filing continuation' corpus/fixtures/r99-window-lapse/README.md \
       && ! grep -q 'r99-window-lapse' corpus/fixtures/r99-window-lapse/README.md; then
      missing+=("PLACEHOLDER:README")
    fi
  fi
  if [[ -s corpus/fixtures/r99-window-lapse/claim-excerpt-map.md ]]; then
    if grep -q 'r98 clerk-filing: canonical claim-to-excerpt map' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
       && ! grep -q 'r99-window-lapse' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md; then
      missing+=("PLACEHOLDER:MAP")
    fi
  fi
  if [[ -s corpus/fixtures/r99-window-lapse/timeline.json ]]; then
    if ! grep -q 'clerk-lapse-recorded' corpus/fixtures/r99-window-lapse/timeline.json; then
      missing+=("PLACEHOLDER:TIMELINE")
    fi
  fi
  if [[ -s corpus/tools/dependency-freeze-contract.json ]]; then
    if ! python3 -c '
import json,sys
d=json.load(open("corpus/tools/dependency-freeze-contract.json"))
pins=d.get("pins") or {}
chain=["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing"]
ok=True
for name in chain:
    pin=pins.get(name) or {}
    files=pin.get("files") or {}
    if len(files)!=10 or pin.get("payload_schema_version")!=2:
        ok=False
exp=d.get("self_test",{}).get("expected",{})
if not isinstance(exp, dict) or "markdown_tamper" not in exp or len(exp)<18:
    ok=False
sys.exit(0 if ok else 1)
'; then
      missing+=("CONTRACT-NOT-FULLFILE")
    fi
  fi

  reports=()
  for s in S1 S2 S3 S4 S5; do
    found=""
    for p in "$SEATS"/${s}-*.md "$SEATS"/${s}.md; do
      [[ -f "$p" ]] || continue
      base=$(basename "$p")
      [[ "$base" == *scratch* ]] && continue
      if [[ -s "$p" ]]; then
        found="$p"
        break
      fi
    done
    if [[ -z "$found" ]]; then
      missing+=("REPORT:$s")
    else
      reports+=("$s=$(basename "$found"):$(wc -c < "$found")")
    fi
  done

  if [[ ${#missing[@]} -eq 0 ]]; then
    echo "TRY $try $ts ALL-PRESENT reports=${reports[*]}" >> "$LOG"
    echo "ALL-PRESENT try=$try"
    exit 0
  fi
  echo "TRY $try $ts MISSING ${#missing[@]} ${missing[*]} reports=${reports[*]:-none}" >> "$LOG"
  if [[ "$try" -eq 40 ]]; then
    echo "ABSENT after 40 tries" >> "$LOG"
    echo "ABSENT"
    exit 2
  fi
  sleep 20
done
