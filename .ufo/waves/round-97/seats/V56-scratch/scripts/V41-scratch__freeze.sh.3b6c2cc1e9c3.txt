#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
{
  find corpus/fixtures/r97-crossing-acknowledgment -maxdepth 1 -type f | sort
  echo corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
  echo corpus/fixtures/check_bible.py
  echo corpus/tools/map_obligations.py
  echo corpus/tools/map-obligations-contract.json
  echo corpus/tools/dependency_freeze.py
  echo corpus/tools/dependency-freeze-contract.json
  echo corpus/tools/README.md
  if [ -f corpus/knowledge/r97-acknowledgment-scope-note.md ]; then
    echo corpus/knowledge/r97-acknowledgment-scope-note.md
  fi
} | xargs sha256sum > .ufo/waves/round-97/seats/V41-scratch/freeze-manifest.sha256
sha256sum -c .ufo/waves/round-97/seats/V41-scratch/freeze-manifest.sha256
