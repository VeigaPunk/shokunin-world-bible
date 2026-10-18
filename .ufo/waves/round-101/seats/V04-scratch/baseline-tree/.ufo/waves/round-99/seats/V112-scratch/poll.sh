#!/bin/bash
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$ROOT/.ufo/waves/round-99/seats
LOG=$SEATS/V112-scratch/poll.log
BASE=4265df5
: > "$LOG"
for i in $(seq 1 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  s1=$(ls -1 "$SEATS"/S1*.md 2>/dev/null | tr '\n' ' ')
  s2=$(ls -1 "$SEATS"/S2*.md 2>/dev/null | tr '\n' ' ')
  readme_diff=$(git -C "$ROOT" diff --stat "$BASE" -- corpus/tools/README.md)
  skill_diff=$(git -C "$ROOT" diff --stat "$BASE" -- SKILL.md)
  contract_diff=$(git -C "$ROOT" diff --stat "$BASE" -- corpus/tools/dependency-freeze-contract.json)
  {
    echo "TRY $i $ts"
    echo "S1=[$s1]"
    echo "S2=[$s2]"
    echo "README_DIFF=[$readme_diff]"
    echo "SKILL_DIFF=[$skill_diff]"
    echo "CONTRACT_DIFF=[$contract_diff]"
  } >> "$LOG"
  if [[ -n "$s1" && -n "$s2" && -n "$readme_diff" && -n "$skill_diff" && -n "$contract_diff" ]]; then
    h1=$(sha256sum "$ROOT/corpus/tools/README.md" "$ROOT/SKILL.md" "$ROOT/corpus/tools/dependency-freeze-contract.json" $s1 $s2)
    echo "STABLE_CANDIDATE try=$i $ts" >> "$LOG"
    echo "$h1" >> "$LOG"
    sleep 20
    h2=$(sha256sum "$ROOT/corpus/tools/README.md" "$ROOT/SKILL.md" "$ROOT/corpus/tools/dependency-freeze-contract.json" $s1 $s2)
    if [[ "$h1" == "$h2" ]]; then
      echo "READY try=$i $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
      echo "$h2" >> "$LOG"
      exit 0
    fi
    echo "UNSTABLE try=$i" >> "$LOG"
  fi
  sleep 20
done
echo "TIMEOUT $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
exit 2
