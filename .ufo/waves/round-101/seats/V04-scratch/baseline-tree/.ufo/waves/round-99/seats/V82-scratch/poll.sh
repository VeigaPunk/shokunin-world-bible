#!/bin/bash
# V82 poll-wait: producer artifacts (content-gated) AND S1-S5 reports.
# 20s cadence, 40 tries. Never treats r98 placeholders as delivered.
# Does not wait on V31 or SELF (comparison poll is separate).
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V82-scratch/poll.log"
cd "$ROOT" || exit 1
echo "POLL-START $(date -Is)" >> "$LOG"

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

for try in $(seq 1 40); do
  ts=$(date -Is)
  missing=()
  for f in "${need_files[@]}"; do
    if [[ ! -s "$f" ]]; then
      missing+=("ABSENT:$f")
    fi
  done
  if [[ -s corpus/fixtures/r99-window-lapse/README.md ]]; then
    if ! grep -q 'r99-window-lapse' corpus/fixtures/r99-window-lapse/README.md; then
      missing+=("PLACEHOLDER:README")
    fi
  fi
  if [[ -s corpus/fixtures/r99-window-lapse/claim-excerpt-map.md ]]; then
    if ! grep -q 'clerk-lapse-recorded\|r99-window-lapse' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md; then
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
exp=d.get("self_test",{}).get("expected",{})
n=len(exp) if isinstance(exp, dict) else 0
blob=json.dumps(d.get("pins",{}))
md = ("claim-excerpt-map.md" in blob) or ("README.md" in blob) or ("fictional-excerpts.md" in blob)
files=d.get("data_files") or d.get("required_files") or d.get("pinned_files") or []
grew = isinstance(files, list) and len(files) >= 10
# schema version may live under payload/schema
schema = json.dumps(d)
ver = ("schema_version" in schema) or ("payload_schema" in schema)
ok = n >= 18 or md or grew
sys.exit(0 if ok else 1)
'; then
      missing+=("BASELINE:CONTRACT")
    fi
  fi
  if [[ -s corpus/tools/README.md ]]; then
    if ! grep -q 'Round-99\|Round 99\|r99' corpus/tools/README.md; then
      missing+=("BASELINE:TOOLS-README")
    fi
  fi
  if [[ -s SKILL.md ]]; then
    if ! grep -q '18 cases\|18-case\|markdown' SKILL.md; then
      missing+=("BASELINE:SKILL")
    fi
  fi
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
    fi
  done
  if [[ ${#missing[@]} -eq 0 ]]; then
    echo "TRY $try $ts ALL-PRESENT" | tee -a "$LOG"
    exit 0
  fi
  echo "TRY $try $ts MISSING ${#missing[@]} ${missing[*]}" | tee -a "$LOG"
  if [[ "$try" -eq 40 ]]; then
    echo "ABSENT after 40 tries" | tee -a "$LOG"
    exit 2
  fi
  sleep 20
done
