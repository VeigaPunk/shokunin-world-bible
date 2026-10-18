#!/bin/bash
# V25 poll-wait: wait for producer artifacts (r96 fixture + hardened tools + producer reports)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  ok=1; miss=""
  for f in Q1 Q2 Q3 Q4 Q5 Q6; do
    ls "$S" | grep -q "^$f" || { ok=0; miss="$miss $f-report"; }
  done
  [ -f "$R/corpus/tools/dependency_freeze.py" ] || { ok=0; miss="$miss dependency_freeze.py"; }
  [ -f "$R/corpus/tools/dependency-freeze-contract.json" ] || { ok=0; miss="$miss dep-contract.json"; }
  [ -d "$R/corpus/fixtures/r96-crossing-response" ] || { ok=0; miss="$miss r96-dir"; }
  for g in entities.json relations.json timeline.json sources.json contradictions.json inspiration-note.md source-excerpt.md fictional-excerpts.md README.md claim-excerpt-map.md; do
    [ -f "$R/corpus/fixtures/r96-crossing-response/$g" ] || { ok=0; miss="$miss r96:$g"; }
  done
  python3 - "$R/corpus/tools/map-obligations-contract.json" <<'PY' || { ok=0; miss="$miss contract!=24"; }
import json,sys
c=json.load(open(sys.argv[1]))
assert len(c.get("self_test",{}).get("cases",[]))>=24
PY
  if [ "$ok" = 1 ]; then echo "ALL PRESENT after try $i"; exit 0; fi
  echo "try $i: missing:$miss"
  sleep 20
done
echo "POLL TIMEOUT"
exit 3
