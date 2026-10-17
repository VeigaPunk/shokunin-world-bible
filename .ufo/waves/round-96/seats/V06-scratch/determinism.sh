#!/usr/bin/env bash
# V06 determinism: third pass over every case with varied PYTHONHASHSEED.
# Usage: determinism.sh <tool-path> <label>
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$ROOT/.ufo/waves/round-96/seats/V06-scratch
TOOL="${1:?tool path}"
LABEL="${2:?run label}"
OUT=$SC/determinism-$LABEL.txt
rm -f "$OUT"
cd "$ROOT" || exit 9
labels_and_args() {
  printf '%s\n' \
    "base|$SC/base" "a|$SC/case-a" "b|$SC/case-b" "c|$SC/case-c" "d|$SC/case-d" \
    "e|$SC/case-e" "g1|$SC/case-g1" "g2|$SC/case-g2" "h1|$SC/case-h1" "h2|$SC/case-h2" \
    "i1|$SC/case-i1" "i2|$SC/case-i2" "i3|$SC/case-i3" "i4|$SC/case-i4" \
    "ctrl-legacy-note|$SC/ctrl-legacy-note" "ctrl-legacy-prose|$SC/ctrl-legacy-prose" \
    "ctrl-canonical-note|$SC/ctrl-canonical-note" \
    "ctrl-inv-declared-wrong|$SC/ctrl-inv-declared-wrong" \
    "ctrl-inv-malformed|$SC/ctrl-inv-malformed"
}
while IFS='|' read -r label target; do
  prev=""
  for seed in 0 1 2; do
    out=$(PYTHONHASHSEED=$seed python3 "$TOOL" "$target" 2>&1); code=$?
    ids=$(printf '%s\n' "$out" | grep -o '^FINDING [a-z_]*' | sed 's/^FINDING //' | paste -sd, -)
    key="exit=$code findings=[${ids:-none}]"
    if [ -n "$prev" ] && [ "$prev" != "$key" ]; then
      printf '%-22s VARIED seed=%s %s | %s\n' "$label" "$seed" "$prev" "$key" | tee -a "$OUT"
      prev="$key"; continue
    fi
    prev="$key"
  done
  printf '%-22s STABLE %s (seeds 0,1,2)\n' "$label" "$prev" | tee -a "$OUT"
done < <(labels_and_args)
echo "determinism label=$LABEL written to $OUT"
