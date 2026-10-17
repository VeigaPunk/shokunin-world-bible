#!/bin/sh
# V35 r96 poll: every 20s, up to 40 tries, report which targets are present.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 3
S=.ufo/waves/round-96/seats
i=0
while [ "$i" -lt 40 ]; do
  i=$((i+1))
  v02=$(ls $S/V02*.md 2>/dev/null | tr '\n' ' ')
  v19=$(ls $S/V19*.md 2>/dev/null | tr '\n' ' ')
  v30=$(ls $S/V30*.md 2>/dev/null | tr '\n' ' ')
  dep=$(ls corpus/tools/dependency_freeze.py 2>/dev/null)
  q4=$(ls corpus/fixtures/r96-crossing-response/timeline.json corpus/fixtures/r96-crossing-response/README.md corpus/fixtures/r96-crossing-response/claim-excerpt-map.md 2>/dev/null | wc -l)
  q6=$(ls corpus/knowledge/r96-response-scope-note.md 2>/dev/null)
  h=$(sha256sum corpus/tools/map_obligations.py 2>/dev/null | cut -c1-8)
  echo "POLL t=$((i*20)) V02='$v02' V19='$v19' V30='$v30' dep='$dep' q4files=$q4 q6='$q6' tool=$h"
  if [ -n "$v02" ] && [ -n "$v19" ] && [ -n "$v30" ] && [ -n "$dep" ] && [ "$q4" -eq 3 ] && [ -n "$q6" ]; then
    echo "POLL_ALL_PRESENT t=$((i*20))"
    exit 0
  fi
  sleep 20
done
echo "POLL_DEADLINE"
exit 1
