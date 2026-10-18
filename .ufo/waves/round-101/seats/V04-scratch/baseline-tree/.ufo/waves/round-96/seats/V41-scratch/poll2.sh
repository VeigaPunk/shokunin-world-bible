#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
need() {
  [ -f "$S/Q2-contract-docs.md" ] || ls "$S"/Q2*.md >/dev/null 2>&1 || return 1
  [ "$(md5sum $R/corpus/tools/map-obligations-contract.json | cut -d' ' -f1)" != "d2a77aa09e5cd38d73d772bb11a5914e" ] || return 1
  [ "$(md5sum $R/corpus/tools/README.md | cut -d' ' -f1)" != "9334067f0aeb3151beff341da9d18758" ] || return 1
  return 0
}
for i in $(seq 1 60); do
  if need; then echo "Q2 READY at try $i $(date +%T)"; ls $S/Q2*.md; exit 0; fi
  echo "q2 try $i $(date +%T) contract=$(md5sum $R/corpus/tools/map-obligations-contract.json|cut -c1-8) readme=$(md5sum $R/corpus/tools/README.md|cut -c1-8)"
  sleep 20
done
echo "Q2 TIMEOUT $(date +%T)"; exit 1
