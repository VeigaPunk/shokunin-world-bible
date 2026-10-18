#!/usr/bin/env bash
# V04 poll: wait for P1's r95 tool (sha change) AND P1's report, 20s cadence, 40 tries.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$R/.ufo/waves/round-95/seats
OLD=cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790
for i in $(seq 1 40); do
  sha=$(sha256sum "$R/corpus/tools/map_obligations.py" | cut -d' ' -f1)
  p1report=$(ls "$SEATS"/P1-*.md 2>/dev/null | head -1 || true)
  changed=no; [ "$sha" != "$OLD" ] && changed=yes
  if [ "$changed" = yes ] && [ -n "$p1report" ]; then
    echo "READY try=$i tool_sha=$sha p1_report=$p1report"
    exit 0
  fi
  echo "WAIT try=$i t=$((i*20))s tool_changed=$changed tool_sha=$sha p1_report=${p1report:-none}"
  sleep 20
done
echo "POLL_TIMEOUT tries=40"
exit 1
