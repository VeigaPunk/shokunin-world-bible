#!/bin/bash
# V57 poll-wait: C3 tool artifacts + Q3 report + V33 report + r96 fixture
L=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$L/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  ok=1
  [ -f "$L/corpus/tools/dependency_freeze.py" ] || ok=0
  [ -f "$L/corpus/tools/dependency-freeze-contract.json" ] || ok=0
  ls "$S"/Q3*.md >/dev/null 2>&1 || ok=0
  ls "$S"/V33*.md >/dev/null 2>&1 || ok=0
  [ -d "$L/corpus/fixtures/r96-crossing-response" ] || ok=0
  if [ $ok -eq 1 ]; then echo "ALL_PRESENT at try $i $(date +%H:%M:%S)"; exit 0; fi
  echo "try $i $(date +%H:%M:%S): dep_freeze=$([ -f "$L/corpus/tools/dependency_freeze.py" ] && echo Y || echo N) contract=$([ -f "$L/corpus/tools/dependency-freeze-contract.json" ] && echo Y || echo N) Q3=$(ls "$S"/Q3*.md 2>/dev/null | wc -l) V33=$(ls "$S"/V33*.md 2>/dev/null | wc -l) r96fix=$([ -d "$L/corpus/fixtures/r96-crossing-response" ] && echo Y || echo N)"
  sleep 20
done
echo "TIMEOUT after 40 tries"; exit 1
