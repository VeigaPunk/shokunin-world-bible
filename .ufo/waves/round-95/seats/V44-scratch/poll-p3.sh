#!/usr/bin/env bash
# V44 poll for P3 artifact: 8 P3-owned files in corpus/fixtures/r95-crossing-aftermath,
# stable timeline.json across two 20s checks, plus (best-effort) a ^P3 seat report.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-95/seats
F=corpus/fixtures/r95-crossing-aftermath
need=(entities.json relations.json contradictions.json sources.json timeline.json inspiration-note.md source-excerpt.md fictional-excerpts.md)
for i in $(seq 1 40); do
  ok=1
  for f in "${need[@]}"; do [ -e "$F/$f" ] || ok=0; done
  rep=$(ls "$S" 2>/dev/null | grep -c '^P3' || true)
  if [ "$ok" -eq 1 ]; then
    h1=$(sha256sum "$F/timeline.json" | cut -d' ' -f1)
    sleep 20
    h2=$(sha256sum "$F/timeline.json" | cut -d' ' -f1)
    if [ "$h1" = "$h2" ]; then
      echo "READY try=$i p3report_files=$rep timeline_sha256=$h2"
      exit 0
    fi
  fi
  sleep 20
done
echo "TIMEOUT after 40 tries; fixture_present=$( [ -d "$F" ] && echo yes || echo no )"
exit 1
