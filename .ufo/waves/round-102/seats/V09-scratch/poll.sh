#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  U2ART=""; [ -f corpus/knowledge/r102-freshness-sweep.md ] && U2ART=yes
  U1ART=""; [ -f corpus/knowledge/r102-push-synthesis-r95-r102.md ] && [ -f corpus/knowledge/r102-debt-ledger.json ] && U1ART=yes
  U2REP=$(ls .ufo/waves/round-102/seats/U2-*.md 2>/dev/null | head -1)
  U1REP=$(ls .ufo/waves/round-102/seats/U1-*.md 2>/dev/null | head -1)
  MODS=$(git status --short -- corpus/knowledge/ | head -5)
  echo "try=$i $(date +%H:%M:%S) U2art=${U2ART:-no} U1art=${U1ART:-no} U2rep=${U2REP:-no} U1rep=${U1REP:-no}"
  [ -n "$MODS" ] && echo "  mods: $MODS"
  if [ -n "$U2ART" ] && [ -n "$U2REP" ]; then echo "GATE: U2 artifact+report present"; exit 0; fi
  sleep 20
done
echo "GATE: exhausted 40 tries"
exit 1
