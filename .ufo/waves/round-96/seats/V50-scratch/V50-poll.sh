#!/bin/bash
# V50 poll-wait: wait until key producer artifacts exist, 20s cadence, 40 tries
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for i in $(seq 1 40); do
  ok=1
  for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response/sources.json corpus/fixtures/r96-crossing-response/timeline.json corpus/fixtures/r96-crossing-response/README.md corpus/fixtures/r96-crossing-response/claim-excerpt-map.md; do
    [ -s "$f" ] || ok=0
  done
  # map_obligations.py must be newer than round start (17:37)
  if [ -f corpus/tools/map_obligations.py ]; then
    mt=$(stat -c %Y corpus/tools/map_obligations.py)
    [ "$mt" -ge 1792269000 ] || ok=0
  else ok=0; fi
  if [ "$ok" = "1" ]; then echo "ALL-PRESENT try=$i $(date -Is)"; exit 0; fi
  sleep 20
done
echo "TIMEOUT $(date -Is)"
exit 1
