#!/bin/bash
# V35 round-98 doc-parity + ownership + stray scan. Run from repo root.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
BASE=9a3d648
OUT=.ufo/waves/round-98/scratch/V35/battery-out
mkdir -p "$OUT"

echo "== change set vs $BASE (declared ownership check) =="
git status --porcelain > "$OUT/ownership.txt"
git diff --name-only "$BASE" >> "$OUT/ownership.txt"
cat "$OUT/ownership.txt"

echo
echo "== untracked (excluding wave tree) =="
git status --porcelain --untracked-files=all | grep '^??' | grep -v '^?? .ufo/waves/round-98/' | sed 's|^?? ||' | sort > "$OUT/untracked.txt"
cat "$OUT/untracked.txt"

echo
echo "== doc parity greps =="
{
  echo "--- SKILL.md dependency_freeze row ---"
  grep -n "16 cases\|six fixtures\|frozen chain\|four fixtures\|17 cases" SKILL.md | head -8
  echo "--- SKILL.md map_obligations row (case count) ---"
  grep -n "25 cases\|24 cases" SKILL.md | head -4
  echo "--- corpus/README.md ---"
  grep -n "dependency_freeze\|Round-97\|Round-98\|round 98" corpus/README.md | head -12
  echo "--- corpus/tools/README.md tail (r98 addendum?) ---"
  grep -n "Round-98\|Round 98\|r98" corpus/tools/README.md | head -8
  echo "--- corpus/fixtures/README.md census text ---"
  grep -n "census re-declaration" corpus/fixtures/README.md | tail -3
  grep -n "Round 98\|Round-98" corpus/fixtures/README.md | head -4
  echo "--- r91-c9-watch row 6 ---"
  grep -n "dependency_freeze" corpus/knowledge/r91-c9-watch.md | head -6
  echo "--- LOG.md round-98 entry ---"
  grep -n "^## Round 98" LOG.md
  echo "--- SCORECARD round-98 ---"
  grep -n "Round 98\|round-98" SCORECARD.md | head -5
} > "$OUT/doc-parity.txt" 2>&1
cat "$OUT/doc-parity.txt"

echo
echo "== commits by seats? =="
git log --oneline "$BASE"..HEAD 2>/dev/null | head -5
echo "(empty above = no commits since $BASE)"
echo done
