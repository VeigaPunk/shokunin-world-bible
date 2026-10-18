#!/bin/bash
# V73 producer poll. Records presence; does not verify a plan.
set -u
LANE="/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS="$LANE/.ufo/waves/round-99/seats"
LOG="$SEATS/V73-scratch/poll.log"
cd "$LANE" || exit 1
stamp() { date '+%Y-%m-%dT%H:%M:%S%z'; }
{
  echo "POLL $(stamp) try=${1:-?}"
  echo "-- producer reports --"
  ls -la "$SEATS"/S1*.md "$SEATS"/S2*.md "$SEATS"/S3*.md "$SEATS"/S4*.md "$SEATS"/S5*.md 2>&1
  echo "-- artifacts --"
  stat -c '%y %s %n' \
    corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/tools/README.md \
    SKILL.md \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    corpus/knowledge/r99-gate-blind-spot-table.md \
    corpus/knowledge/r99-lapse-scope-note.md 2>&1
  echo "-- SKILL names --"
  rg -n '^- \*\*name:\*\*' SKILL.md || true
  echo "-- SKILL vs 4265df5 --"
  if git diff --quiet 4265df5 -- SKILL.md; then echo "SKILL.md IDENTICAL to 4265df5"; else echo "SKILL.md DIFFERS from 4265df5"; git diff --stat 4265df5 -- SKILL.md; fi
  echo "-- contract schema version grep --"
  python3 -c 'import json; p="corpus/tools/dependency-freeze-contract.json"; d=json.load(open(p)); print("top_keys", sorted(d)[:30]); st=d.get("self_test",{}); exp=(st.get("expected") if isinstance(st,dict) else None); print("self_test_cases", len(exp) if isinstance(exp,dict) else None); pins=d.get("pins") or d.get("fixtures") or {}; print("pin_container", type(pins).__name__, len(pins) if hasattr(pins,"__len__") else "?")'
  echo
} >> "$LOG" 2>&1
