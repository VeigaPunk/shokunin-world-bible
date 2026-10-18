#!/bin/bash
# Read-only baseline battery against r98 closure bytes (4265df5).
# Copies tool+contract into scratch and runs them; never writes lane files.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR="$ROOT/.ufo/waves/round-99/seats/V38-scratch"
OUT="$SCR/baseline-battery.txt"
BASE=4265df5
cd "$ROOT" || exit 1
mkdir -p "$SCR/baseline-tool/corpus/tools" "$SCR/baseline-tool/corpus/fixtures"
git show "$BASE:corpus/tools/dependency_freeze.py" > "$SCR/baseline-tool/corpus/tools/dependency_freeze.py"
git show "$BASE:corpus/tools/dependency-freeze-contract.json" > "$SCR/baseline-tool/corpus/tools/dependency-freeze-contract.json"
# fixtures the baseline tool verifies must exist at ROOT/corpus/fixtures (tool ROOT is parents[2] of the script)
# so we run the baseline script FROM a mirror that also contains the live fixtures via symlink? 
# The baseline script's ROOT = parents[2] of the script path.
# Place script at $SCR/baseline-tool/corpus/tools/dependency_freeze.py so ROOT = $SCR/baseline-tool
# and symlink fixtures.
ln -sfn "$ROOT/corpus/fixtures" "$SCR/baseline-tool/corpus/fixtures"
{
  echo "=== baseline tool sha ==="
  sha256sum "$SCR/baseline-tool/corpus/tools/dependency_freeze.py" "$SCR/baseline-tool/corpus/tools/dependency-freeze-contract.json"
  echo "=== baseline self-test ==="
  python3 "$SCR/baseline-tool/corpus/tools/dependency_freeze.py" --self-test
  echo "BASELINE_SELFTEST_EXIT=$?"
  echo "=== baseline chain ==="
  for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    echo "-- $f --"
    python3 "$SCR/baseline-tool/corpus/tools/dependency_freeze.py" "$SCR/baseline-tool/corpus/fixtures/$f"
    echo "EXIT=$?"
  done
  echo "=== baseline on r99 (expect UNPINNED) ==="
  python3 "$SCR/baseline-tool/corpus/tools/dependency_freeze.py" "$SCR/baseline-tool/corpus/fixtures/r99-window-lapse"
  echo "EXIT=$?"
  echo "=== baseline prose-tamper invisibility ==="
  # copy r98 fixture into scratch (not under corpus/fixtures of the mirror? tool only reads files)
  mkdir -p "$SCR/prose-before"
  rm -rf "$SCR/prose-before/r98-clerk-filing"
  cp -a "$ROOT/corpus/fixtures/r98-clerk-filing" "$SCR/prose-before/r98-clerk-filing"
  # but PATH-MISMATCH: baseline pin names corpus/fixtures/r98-clerk-filing relative to tool ROOT.
  # So tamper a copy placed at the mirror's corpus/fixtures path — that would be the live tree via symlink.
  # Do NOT mutate the live tree. Instead: demonstrate on a private mirror root.
  echo "(prose-tamper demo deferred to private mirror; see prose-before.py)"
} > "$OUT" 2>&1
echo DONE >> "$OUT"
echo "wrote $OUT"
