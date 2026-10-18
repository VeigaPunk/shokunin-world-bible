#!/bin/bash
# V74 debt-2 content-gated poll. Existence is not delivery (r98 placeholder class).
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V74-scratch/poll.log
BASE=4265df5
MAX=40
i=0
ready() {
  local miss=0
  for s in S1 S2 S3 S4 S5; do
    if ! ls "$SEATS"/${s}-*.md >/dev/null 2>&1; then
      echo "MISS report $s"
      miss=1
    fi
  done
  if git -C "$LANE" diff --quiet "$BASE" -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json; then
    echo "MISS S1 bytes unchanged vs $BASE"
    miss=1
  fi
  if git -C "$LANE" diff --quiet "$BASE" -- corpus/tools/README.md SKILL.md; then
    echo "MISS S2 bytes unchanged vs $BASE"
    miss=1
  fi
  python3 - << 'PY' || miss=1
import sys
from pathlib import Path
lane = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
r98 = lane/"corpus/fixtures/r98-clerk-filing"
r99 = lane/"corpus/fixtures/r99-window-lapse"
need = ["entities.json","sources.json","timeline.json","relations.json","contradictions.json","fictional-excerpts.md"]
for n in need:
    b = r99/n
    if not b.exists():
        print(f"MISS r99 missing {n}")
        sys.exit(1)
tl = (r99/"timeline.json").read_text(encoding="utf-8")
src = (r99/"sources.json").read_text(encoding="utf-8")
ok = ("clerk-lapse" in tl or "lapse" in tl) and ("clerk-lapse" in src or "lapse" in src)
if not ok:
    print("MISS r99 JSON still placeholder (no lapse marker in timeline/sources)")
    sys.exit(1)
if tl == (r98/"timeline.json").read_text(encoding="utf-8") and src == (r98/"sources.json").read_text(encoding="utf-8"):
    print("MISS r99 timeline+sources byte-identical to r98")
    sys.exit(1)
print("S3 content markers present")
PY
  python3 - << 'PY' || miss=1
import sys
from pathlib import Path
lane = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
r98 = lane/"corpus/fixtures/r98-clerk-filing"
r99 = lane/"corpus/fixtures/r99-window-lapse"
for n in ("README.md","claim-excerpt-map.md"):
    b = r99/n
    if not b.exists():
        print(f"MISS r99 missing {n}")
        sys.exit(1)
    text = b.read_text(encoding="utf-8")
    if "lapse" not in text.lower() and "window" not in text.lower():
        print(f"MISS {n} no lapse/window marker (placeholder?)")
        sys.exit(1)
    if text == (r98/n).read_text(encoding="utf-8"):
        print(f"MISS {n} byte-identical to r98")
        sys.exit(1)
print("S4 content markers present")
PY
  if [ ! -s "$LANE/corpus/knowledge/r99-gate-blind-spot-table.md" ]; then
    echo "MISS r99-gate-blind-spot-table.md"
    miss=1
  fi
  if [ ! -s "$LANE/corpus/knowledge/r99-lapse-scope-note.md" ]; then
    echo "MISS r99-lapse-scope-note.md"
    miss=1
  fi
  if ! ls "$SEATS"/V36-*.md >/dev/null 2>&1; then
    echo "MISS V36 report"
    miss=1
  fi
  return $miss
}

while [ "$i" -lt "$MAX" ]; do
  i=$((i+1))
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  echo "=== TRY $i $ts ===" >> "$LOG"
  out=$(ready 2>&1)
  echo "$out" >> "$LOG"
  if ! echo "$out" | grep -q '^MISS '; then
    echo "ALL-PRESENT try $i $ts" | tee -a "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after $MAX tries $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
exit 2
