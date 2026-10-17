#!/bin/bash
# V36 poll: 20s cadence, 40 tries. Logs producer digests + seat reports + r97 artifacts.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-97/seats/V36-scratch/poll.log
: > "$LOG"
for i in $(seq 0 39); do
  t=$(date +%H:%M:%S)
  r1=$(sha256sum corpus/tools/map_obligations.py 2>/dev/null | cut -c1-16)
  r2c=$(sha256sum corpus/tools/map-obligations-contract.json 2>/dev/null | cut -c1-16)
  r2r=$(sha256sum corpus/tools/README.md 2>/dev/null | cut -c1-16)
  r3t=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-16)
  r3c=$(sha256sum corpus/tools/dependency-freeze-contract.json 2>/dev/null | cut -c1-16)
  r4m=$(sha256sum corpus/fixtures/r96-crossing-response/claim-excerpt-map.md 2>/dev/null | cut -c1-16)
  fx=$(ls corpus/fixtures/r97-crossing-acknowledgment/ 2>/dev/null | wc -l)
  r6=$(sha256sum corpus/knowledge/r97-acknowledgment-scope-note.md 2>/dev/null | cut -c1-16)
  prods=$(ls .ufo/waves/round-97/seats/R[1-6]-*.md 2>/dev/null | wc -l)
  seats=$(ls .ufo/waves/round-97/seats/V*.md .ufo/waves/round-97/seats/Q*.md 2>/dev/null | wc -l)
  rep97=$(test -f /home/vgpnk/Projects/shokunin/.ufo/reports/round-97/lore.md && echo YES || echo no)
  printf 'POLL i=%02d t=%s r1=%s r2c=%s r2r=%s r3t=%s r3c=%s r4m=%s fx=%s r6=%s prods=%s seats=%s rep97=%s\n' \
    "$i" "$t" "$r1" "$r2c" "$r2r" "$r3t" "$r3c" "$r4m" "$fx" "$r6" "$prods" "$seats" "$rep97" >> "$LOG"
  # early exit: all six producers reported AND fixture at 10 files AND note present
  if [ "$prods" -ge 6 ] && [ "$fx" -ge 10 ] && [ -n "$r6" ]; then
    echo "POLL_EARLY_EXIT i=$i t=$t prods=$prods fx=$fx" >> "$LOG"
    break
  fi
  sleep 20
done
echo "POLL DONE $(date +%H:%M:%S)" >> "$LOG"
