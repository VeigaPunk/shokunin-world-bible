#!/bin/bash
# V75 poll-wait: producer artifacts AND producer reports. 20s cadence, max 40.
# Never treats existence of a plan as verification. ENDGAME: subtract SELF.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V75-scratch/poll.log"
cd "$ROOT" || exit 1

need_files=(
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
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
)

hashset() {
  local f h
  for f in "${need_files[@]}"; do
    if [[ -f "$f" ]]; then
      h=$(sha256sum "$f" | awk '{print $1}')
      printf '%s %s\n' "$h" "$f"
    else
      printf 'ABSENT %s\n' "$f"
    fi
  done
}

report_missing() {
  local miss=""
  local seat
  for seat in S1 S2 S3 S4 S5; do
    if ! compgen -G "$SEATS/${seat}-*.md" >/dev/null; then
      miss="$miss REPORT:$seat"
    fi
  done
  # V38 is the comparison seat; wait for it but do not block artifact verification forever.
  if ! compgen -G "$SEATS/V38-*.md" >/dev/null; then
    miss="$miss REPORT:V38"
  fi
  printf '%s' "$miss"
}

prev=""
stable=0
for try in $(seq 1 40); do
  ts=$(date '+%Y-%m-%dT%H:%M:%S%z')
  cur=$(hashset)
  abs=$(printf '%s\n' "$cur" | grep -c '^ABSENT ' || true)
  rmiss=$(report_missing)
  echo "try=$try ts=$ts absent_files=$abs reports_missing='$rmiss'" >> "$LOG"
  if [[ "$cur" == "$prev" && "$abs" == "0" && -z "$rmiss" ]]; then
    stable=$((stable+1))
    echo "  STABLE-WINDOW $stable" >> "$LOG"
    if [[ "$stable" -ge 1 ]]; then
      echo "READY-STABLE try=$try ts=$ts" >> "$LOG"
      printf '%s\n' "$cur" > "$SEATS/V75-scratch/ready-hashes.txt"
      exit 0
    fi
  else
    stable=0
  fi
  prev="$cur"
  printf '%s\n' "$cur" > "$SEATS/V75-scratch/last-hashes.txt"
  sleep 20
done
echo "POLL-TIMEOUT ts=$(date '+%Y-%m-%dT%H:%M:%S%z')" >> "$LOG"
printf '%s\n' "$cur" > "$SEATS/V75-scratch/timeout-hashes.txt"
exit 2
