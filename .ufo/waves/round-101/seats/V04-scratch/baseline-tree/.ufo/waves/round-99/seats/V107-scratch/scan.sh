#!/bin/bash
# Rights / mechanics / path scan over r99 new bytes and round diffs.
# Read-only except the scratch transcript.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
OUT="$ROOT/.ufo/waves/round-99/seats/V107-scratch"
cd "$ROOT" || exit 1
BLOB="$OUT/round-new-bytes.txt"
{
  echo "===== DIFF 4265df5 corpus/tools SKILL ====="
  git diff 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
  echo "===== KNOWLEDGE ====="
  cat corpus/knowledge/r99-gate-blind-spot-table.md
  echo "===== SCOPE NOTE ====="
  cat corpus/knowledge/r99-lapse-scope-note.md
  echo "===== FIXTURE ====="
  for f in corpus/fixtures/r99-window-lapse/*; do
    echo "----- $f -----"
    cat "$f"
  done
} > "$BLOB"
echo "BLOB_BYTES $(wc -c < "$BLOB")"
echo "===== mechanics / rights-grant ====="
grep -n -i -E "mechanic|gameplay|ruleset|damage|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)|licensed under|permission is granted" "$BLOB" || echo "(no mechanics/grant hits)"
echo "===== path / sibling leaks ====="
grep -n -E "/home/|\.\./|/tmp/|kotodama|game-dev|art-east|kengaku|mado-shokunin|tabi-shokunin" "$BLOB" || echo "(no path/sibling hits)"
echo "===== external names in fixture JSON ====="
grep -n -i -E "Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche" corpus/fixtures/r99-window-lapse/*.json || echo "(no json external-name hits)"
echo "SCAN_END $(date '+%Y-%m-%d %H:%M:%S %z')"
