#!/bin/bash
# R1 poll: wait for R2's 25-case contract (and report presence). 20s cadence, 40 tries.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
LOG=.ufo/waves/round-97/seats/scratch-R1/poll-r2.log
: > "$LOG"
for i in $(seq 1 40); do
  n=$(python3 - <<'EOF'
import json
try:
    c = json.load(open("corpus/tools/map-obligations-contract.json", encoding="utf-8"))
    cases = c["self_test"]["cases"]
    print(len(cases), [x["id"] for x in cases if x["id"] == "dual_pointer"])
except Exception as e:
    print("ERR", e)
EOF
)
  rep=$(ls .ufo/waves/round-97/seats/R2*.md 2>/dev/null | head -1)
  sha=$(sha256sum corpus/tools/map-obligations-contract.json | cut -d' ' -f1)
  echo "try=$i contract=$n sha=$sha r2_report=${rep:-absent} $(date -u +%H:%M:%SZ)" >> "$LOG"
  case "$n" in
    25*) echo "POLL_HIT try=$i contract=$n sha=$sha r2_report=${rep:-absent}"; exit 0;;
  esac
  sleep 20
done
echo "POLL_TIMEOUT after 40 tries"; exit 1
