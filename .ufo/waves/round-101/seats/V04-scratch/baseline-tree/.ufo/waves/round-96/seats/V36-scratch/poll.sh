#!/bin/bash
# V36 poll: wait for Q1-Q6 producer reports + artifacts + V28/V29 reports
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats
for i in $(seq 1 40); do
  q=""
  for n in 1 2 3 4 5 6; do ls "$S"/Q$n*.md >/dev/null 2>&1 && q="$q Q$n=1" || q="$q Q$n=0"; done
  for v in 28 29; do ls "$S"/V$v-*.md >/dev/null 2>&1 && q="$q V$v=1" || q="$q V$v=0"; done
  # key artifacts
  a=""
  [ -f "$R/corpus/tools/dependency_freeze.py" ] && a="$a df=1" || a="$a df=0"
  [ -f "$R/corpus/fixtures/r96-crossing-response/sources.json" ] && a="$a src=1" || a="$a src=0"
  [ -f "$R/corpus/fixtures/r96-crossing-response/README.md" ] && a="$a rm=1" || a="$a rm=0"
  [ -f "$R/corpus/knowledge/r96-response-scope-note.md" ] && a="$a note=1" || a="$a note=0"
  echo "try=$i$q$a $(date +%H:%M:%S)"
  if [ "${q#*Q1=1 Q2=1 Q3=1 Q4=1 Q5=1 Q6=1 V28=1 V29=1}" != "$q" ]; then echo "ALL-REPORTS"; exit 0; fi
  sleep 20
done
echo "TIMEOUT"
