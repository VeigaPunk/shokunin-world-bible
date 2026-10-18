#!/bin/bash
# V45 pins-c9 poll. Subtract SELF. Never verify a plan.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
SCR="$SEATS/V45-scratch"
LOG="$SCR/poll.log"
cd "$ROOT" || exit 1

# Producer reports (r98 names + r99 brief names).
PRODUCERS=(
  S1-freeze-hygiene.md
  S2-tools-docs.md
  S3-fixture-author.md
  S4-fixture-docs.md
  S5-knowledge-notes.md
)
# V22 report candidates. The brief says "from V22 outputs".
V22_CANDIDATES=(
  V22-doc-parity.md
  V22-gates-boundary.md
  V22-pins-c9.md
  V22.md
)
ARTS=(
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
  corpus/fixtures/r99-window-lapse/README.md
  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
  corpus/fixtures/r99-window-lapse/entities.json
  corpus/fixtures/r99-window-lapse/timeline.json
  corpus/fixtures/r99-window-lapse/sources.json
  corpus/fixtures/r99-window-lapse/relations.json
  corpus/fixtures/r99-window-lapse/contradictions.json
  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
  corpus/fixtures/r99-window-lapse/inspiration-note.md
  corpus/fixtures/r99-window-lapse/source-excerpt.md
  corpus/knowledge/r99-gate-blind-spot-table.md
  corpus/knowledge/r99-lapse-scope-note.md
)

: > "$LOG"
for try in $(seq 1 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  miss_p=()
  for f in "${PRODUCERS[@]}"; do
    [[ -s "$SEATS/$f" ]] || miss_p+=("$f")
  done
  v22_hit=""
  for f in "${V22_CANDIDATES[@]}"; do
    if [[ -s "$SEATS/$f" ]]; then v22_hit="$f"; break; fi
  done
  # also accept any seats/V22*.md that is not under scratch
  if [[ -z "$v22_hit" ]]; then
    while IFS= read -r p; do
      [[ -s "$p" ]] && v22_hit="${p#$SEATS/}" && break
    done < <(find "$SEATS" -maxdepth 1 -name 'V22*.md' -type f 2>/dev/null)
  fi
  miss_a=()
  for a in "${ARTS[@]}"; do
    [[ -e "$ROOT/$a" ]] || miss_a+=("$a")
  done
  # seat reports excluding SELF
  nreports=$(find "$SEATS" -maxdepth 1 -name '*.md' ! -name 'V45-pins-c9.md' -type f | wc -l)
  printf 'try=%s t=%s producers_missing=%s v22=%s arts_missing=%s other_reports=%s\n' \
    "$try" "$ts" "${miss_p[*]:-NONE}" "${v22_hit:-ABSENT}" "${miss_a[*]:-NONE}" "$nreports" >> "$LOG"
  if [[ ${#miss_p[@]} -eq 0 && -n "$v22_hit" && ${#miss_a[@]} -eq 0 ]]; then
    echo "ALL-PRESENT try=$try t=$ts v22=$v22_hit" >> "$LOG"
    exit 0
  fi
  sleep 20
done
echo "ABSENT after 40 tries t=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
exit 2
