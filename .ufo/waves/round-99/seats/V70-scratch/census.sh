#!/bin/bash
# V70 census-3: shell-loop census of corpus/fixtures (r94–r98 convention).
# Counts dirs, exit 0/1, VIOLATION-substring lines. Does not write outside scratch.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R" || exit 9
export PYTHONDONTWRITEBYTECODE=1
dirs=0
clean=0
negative=0
viol=0
odd=0
receipts="$1"
: > "$receipts"
for d in corpus/fixtures/*/; do
  [ -d "$d" ] || continue
  name=${d%/}
  name=${name##*/}
  dirs=$((dirs+1))
  out=$(python3 corpus/fixtures/check_bible.py "${d%/}" 2>&1)
  rc=$?
  n=$(printf '%s\n' "$out" | grep -c 'VIOLATION' || true)
  viol=$((viol+n))
  if [ "$rc" -eq 0 ]; then
    clean=$((clean+1))
  elif [ "$rc" -eq 1 ]; then
    negative=$((negative+1))
  else
    odd=$((odd+1))
    printf 'ODD %s rc=%s\n' "$name" "$rc"
  fi
  # receipt: name exit violation_count sha256 of combined stdout+stderr
  hash=$(printf '%s\n' "$out" | sha256sum | awk '{print $1}')
  printf '%s\t%s\t%s\t%s\n' "$name" "$rc" "$n" "$hash" >> "$receipts"
done
printf 'CENSUS dirs=%s clean=%s negative=%s violation_lines=%s non01=%s\n' \
  "$dirs" "$clean" "$negative" "$viol" "$odd"
