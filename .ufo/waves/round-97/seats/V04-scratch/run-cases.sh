#!/usr/bin/env bash
# V06 c1-negative-rerun runner (round 96): each case twice, capture stdout+stderr+exit.
# Usage: run-cases.sh <tool-path> <run-label>
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$ROOT/.ufo/waves/round-97/seats/V04-scratch
TOOL="${1:?tool path}"
LABEL="${2:?run label}"
RUNS=$SC/runs-$LABEL
rm -rf "$RUNS"; mkdir -p "$RUNS"
cd "$ROOT" || exit 9

run_case() {
  local label="$1"; shift
  for pass in 1 2; do
    local out="$RUNS/$label-run$pass.out"
    printf '$ python3 %s %s\n' "$TOOL" "$*" > "$out"
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
run_case f4    "$SC/case-f" --map .
run_case g1    "$SC/case-g1"
run_case g2    "$SC/case-g2"
run_case h1    "$SC/case-h1"
run_case h2    "$SC/case-h2"
run_case i1    "$SC/case-i1"
run_case i2    "$SC/case-i2"
run_case i3    "$SC/case-i3"
run_case i4    "$SC/case-i4"
run_case i5    "$SC/case-i5"
run_case i6    "$SC/case-i6"
run_case i7    "$SC/case-i7"
run_case ctrl-legacy-note      "$SC/ctrl-legacy-note"
run_case ctrl-legacy-prose     "$SC/ctrl-legacy-prose"
run_case ctrl-canonical-note   "$SC/ctrl-canonical-note"
run_case ctrl-inv-declared-wrong "$SC/ctrl-inv-declared-wrong"
run_case ctrl-inv-malformed    "$SC/ctrl-inv-malformed"

LABELS="base a b c d e f1 f2 f3 f4 g1 g2 h1 h2 i1 i2 i3 i4 i5 i6 i7 ctrl-legacy-note ctrl-legacy-prose ctrl-canonical-note ctrl-inv-declared-wrong ctrl-inv-malformed"

echo "=== $LABEL STABILITY (run1 vs run2, byte diff) ==="
for label in $LABELS; do
  if diff -q "$RUNS/$label-run1.out" "$RUNS/$label-run2.out" >/dev/null; then
    echo "$label: IDENTICAL"
  else
    echo "$label: DIFFERS"
    diff "$RUNS/$label-run1.out" "$RUNS/$label-run2.out"
  fi
done

echo "=== $LABEL FINDING IDS PER PASS ==="
for label in $LABELS; do
  for pass in 1 2; do
    ids=$(grep -o '^FINDING [a-z_]*' "$RUNS/$label-run$pass.out" | sed 's/^FINDING //' | paste -sd, -)
    res=$(grep -o '^RESULT [A-Z]*' "$RUNS/$label-run$pass.out" | sed 's/^RESULT //')
    code=$(grep -o '^EXIT=[0-9]*' "$RUNS/$label-run$pass.out" | sed 's/^EXIT=//')
    printf '%-22s pass%s result=%-5s exit=%s findings=[%s]\n' "$label" "$pass" "${res:-none}" "${code:-?}" "${ids:-none}"
  done
done
