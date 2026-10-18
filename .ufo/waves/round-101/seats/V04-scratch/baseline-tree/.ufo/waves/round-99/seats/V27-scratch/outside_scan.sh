#!/bin/sh
# V27 r99 adjacency — outside-write scans. Usage: outside_scan.sh <outfile> [since]
cd /home/vgpnk/Projects/shokunin || exit 1
OUT="${1:-/tmp/v27-outside.txt}"
SINCE="${2:-2026-10-17 21:50}"
{
  echo "== fleet-root scan: files newer than '$SINCE' outside lore-shokunin, excl .git =="
  find . -newermt "$SINCE" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" 2>/dev/null | sort
  echo "== lore/r99-named files outside lane =="
  find . -newermt "$SINCE" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" 2>/dev/null | grep -i -E "lore|r99|window-lapse|blind-spot" || echo "(none)"
  echo "== parent repo git status =="
  git -C /home/vgpnk/Projects/shokunin status --porcelain 2>&1 | head -40
  echo "== parent .ufo/waves/round-99 presence =="
  ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-99 2>&1
  echo "== /tmp in-window (names only, maxdepth 1) =="
  find /tmp -maxdepth 1 -newermt "$SINCE" 2>/dev/null | sort
  echo "== sibling PROVINCE.md mtimes =="
  ls -la --time-style=long-iso /home/vgpnk/Projects/shokunin/*/PROVINCE.md 2>/dev/null
} > "$OUT" 2>&1
wc -l "$OUT"
