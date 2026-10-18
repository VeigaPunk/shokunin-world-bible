#!/bin/sh
# V24 r98 adjacency — outside-write scans. Usage: outside_scan.sh <outfile> [since]
cd /home/vgpnk/Projects/shokunin || exit 1
OUT="${1:-/tmp/v24-outside.txt}"
SINCE="${2:-2026-10-17 20:26}"
{
  echo "== fleet-root scan: files newer than '$SINCE' outside lore-shokunin, excl .git =="
  find . -newermt "$SINCE" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" 2>/dev/null | sort
  echo "== lore-side sibling attribution: lore/r98-named files outside lane =="
  find . -newermt "$SINCE" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" 2>/dev/null | grep -i -E "lore|r98|clerk" || echo "(none)"
  echo "== parent repo git status =="
  git -C /home/vgpnk/Projects/shokunin status --porcelain 2>&1 | head -20
  echo "== parent .ufo/waves/round-98 presence =="
  ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-98 2>&1
  echo "== /tmp in-window =="
  find /tmp -maxdepth 1 -newermt "$SINCE" 2>/dev/null | sort
  echo "== sibling PROVINCE.md mtimes =="
  ls -la --time-style=long-iso /home/vgpnk/Projects/shokunin/*/PROVINCE.md 2>/dev/null
} > "$OUT" 2>&1
wc -l "$OUT"
