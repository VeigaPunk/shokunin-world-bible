#!/bin/bash
# V27 final replay harness: run a command from the lane root, capture
# stdout+stderr and the true exit code into final-transcript.txt.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR="$ROOT/.ufo/waves/round-97/seats/V27-scratch"
T="$SCR/final-transcript.txt"
{
  echo "##### $(date -Is) CMD: $*"
} >> "$T"
cd "$ROOT"
"$@" > "$SCR/.out.tmp" 2>&1
rc=$?
cat "$SCR/.out.tmp" >> "$T"
echo "EXIT=$rc" >> "$T"
echo "----- output (exit=$rc):"
cat "$SCR/.out.tmp"
echo "EXIT=$rc"
