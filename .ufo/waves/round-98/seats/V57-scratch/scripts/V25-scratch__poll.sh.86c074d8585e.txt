#!/bin/bash
# V25 bounded poll: 40 tries, 20s cadence. Checks C1 artifacts + S1/S2 reports.
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  missing=""
  # artifact change: contract precedence must differ from baseline OR tool differs
  if [ "$(sha256sum corpus/tools/dependency_freeze.py | cut -d' ' -f1)" = "b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130" ]; then missing="$missing TOOL-UNCHANGED"; fi
  if [ ! -f .ufo/waves/round-98/seats/S1-*.md ] 2>/dev/null; then :; fi
  ls .ufo/waves/round-98/seats/S1*.md >/dev/null 2>&1 || missing="$missing REPORT:S1"
  ls .ufo/waves/round-98/seats/S2*.md >/dev/null 2>&1 || missing="$missing REPORT:S2"
  if [ -z "$missing" ]; then echo "try $i $(date +%H:%M:%S) ALL-PRESENT"; exit 0; fi
  echo "try $i $(date +%H:%M:%S) missing:$missing"
  sleep 20
done
echo "POLL-EXHAUSTED"
