#!/usr/bin/env bash
# F11 c2-negative runner: each case twice, capture exact stdout/stderr and exit code.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$ROOT/.ufo/waves/round-94/followup/F11-scratch
TOOL=$ROOT/corpus/tools/map_obligations.py
RUNS=$SC/runs
rm -rf "$RUNS"; mkdir -p "$RUNS"
cd "$ROOT" || exit 9

run_case() {
  local label="$1"; shift
  for pass in 1 2; do
    local out="$RUNS/$label-run$pass.out"
    printf '$ python3 corpus/tools/map_obligations.py %s\n' "$*" > "$out"
    python3 "$TOOL" "$@" >> "$out" 2>&1
    local code=$?
    printf 'EXIT=%s\n' "$code" >> "$out"
  done
}

run_case base  "$SC/base"
run_case a     "$SC/case-a"
run_case b     "$SC/case-b"
run_case c     "$SC/case-c"
run_case d     "$SC/case-d"
run_case e     "$SC/case-e"
run_case f1    "$SC/case-f" --map missing-map.md
run_case f2    "$SC/case-f" --map "$SC/outside-map/claim-excerpt-map.md"
run_case f3    "$SC/case-f" --map ../outside-map/claim-excerpt-map.md

echo "=== RUN 1 outputs ==="
for label in base a b c d e f1 f2 f3; do
  echo "--- $label (run1) ---"
  cat "$RUNS/$label-run1.out"
done

echo "=== STABILITY (run1 vs run2, byte diff) ==="
for label in base a b c d e f1 f2 f3; do
  if diff -q "$RUNS/$label-run1.out" "$RUNS/$label-run2.out" >/dev/null; then
    echo "$label: IDENTICAL"
  else
    echo "$label: DIFFERS"
    diff "$RUNS/$label-run1.out" "$RUNS/$label-run2.out"
  fi
done

echo "=== FINDING IDS PER PASS ==="
for label in base a b c d e f1 f2 f3; do
  for pass in 1 2; do
    ids=$(grep -o '^FINDING [a-z_]*' "$RUNS/$label-run$pass.out" | sed 's/^FINDING //' | paste -sd, -)
    res=$(grep -o '^RESULT [A-Z]*' "$RUNS/$label-run$pass.out" | sed 's/^RESULT //')
    code=$(grep -o '^EXIT=[0-9]*' "$RUNS/$label-run$pass.out" | sed 's/^EXIT=//')
    printf '%-5s pass%s result=%-5s exit=%s findings=[%s]\n' "$label" "$pass" "${res:-none}" "${code:-?}" "${ids:-none}"
  done
done
