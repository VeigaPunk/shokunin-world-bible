#!/bin/bash
# V35 poll — 40 samples, 20s cadence. Read-only. Writes only this scratch dir.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
SCRATCH=$SEATS/V35-scratch
FLEET=/home/vgpnk/Projects/shokunin
LOG=$SCRATCH/poll.log
TSV=$SCRATCH/poll.tsv
FX=$SCRATCH/poll-fx.tsv
CHG=$SCRATCH/poll-changes.log
mkdir -p "$SCRATCH"
cd "$LANE" || exit 1

hash_file() {
  if [ -f "$1" ]; then sha256sum "$1" | awk '{print $1}'; else echo ABSENT; fi
}

fx_names=(contradictions.json entities.json relations.json sources.json timeline.json README.md claim-excerpt-map.md fictional-excerpts.md inspiration-note.md source-excerpt.md)

echo "POLL START $(date -Is)" > "$LOG"
printf 'i\tts\ts1py\ts1json\ts2readme\ts2skill\tfxn\tfxh\ts5table\ts5note\tlogh\tscoreh\tprods\tseats_exself\tfleet\tnonwave_status\n' > "$TSV"
printf 'i\tfile\thash\n' > "$FX"
: > "$CHG"

prev=""
for i in $(seq 0 39); do
  t0=$(date +%s)
  ts=$(date -Is)
  s1py=$(hash_file corpus/tools/dependency_freeze.py)
  s1json=$(hash_file corpus/tools/dependency-freeze-contract.json)
  s2readme=$(hash_file corpus/tools/README.md)
  s2skill=$(hash_file SKILL.md)
  s5table=$(hash_file corpus/knowledge/r99-gate-blind-spot-table.md)
  s5note=$(hash_file corpus/knowledge/r99-lapse-scope-note.md)
  logh=$(hash_file LOG.md)
  scoreh=$(hash_file SCORECARD.md)
  if [ -d corpus/fixtures/r99-window-lapse ]; then
    fxn=$(find corpus/fixtures/r99-window-lapse -maxdepth 1 -type f | wc -l)
    fxdump=""
    for f in "${fx_names[@]}"; do
      h=$(hash_file "corpus/fixtures/r99-window-lapse/$f")
      fxdump+="$f $h"$'\n'
      printf '%s\t%s\t%s\n' "$i" "$f" "$h" >> "$FX"
    done
    extra=$(find corpus/fixtures/r99-window-lapse -maxdepth 1 -type f -printf '%f\n' | sort | comm -23 - <(printf '%s\n' "${fx_names[@]}" | sort))
    fxh=$(printf '%s' "$fxdump" | sha256sum | awk '{print $1}')
  else
    fxn=ABSENT
    fxh=ABSENT
    extra=""
  fi
  prod_list=$(find "$SEATS" -maxdepth 1 -type f -name 'S*.md' -printf '%f\n' | sort | tr '\n' ',' | sed 's/,$//')
  prods=$(find "$SEATS" -maxdepth 1 -type f -name 'S*.md' | wc -l)
  seats_exself=$(find "$SEATS" -maxdepth 1 -type f -name '*.md' ! -name 'V35-shonen-format.md' | wc -l)
  if [ -f "$FLEET/.ufo/reports/round-99/lore.md" ]; then fleet=PRESENT; else fleet=ABSENT; fi
  nonwave=$(git status --porcelain | grep -v '.ufo/waves/round-99/' | tr '\n' ';' | sed 's/;$//')
  [ -z "$nonwave" ] && nonwave=CLEAN
  sig="$s1py|$s1json|$s2readme|$s2skill|$fxn|$fxh|$s5table|$s5note|$logh|$scoreh|$prod_list|$seats_exself|$fleet|$nonwave"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$i" "$ts" "$s1py" "$s1json" "$s2readme" "$s2skill" "$fxn" "$fxh" "$s5table" "$s5note" "$logh" "$scoreh" "$prods" "$seats_exself" "$fleet" "$nonwave" >> "$TSV"
  echo "i=$i ts=$ts s1py=${s1py:0:12} s1json=${s1json:0:12} s2readme=${s2readme:0:12} s2skill=${s2skill:0:12} fxn=$fxn fxh=${fxh:0:12} s5table=${s5table:0:12} s5note=${s5note:0:12} prods=$prods($prod_list) seats_exself=$seats_exself fleet=$fleet" >> "$LOG"
  if [ "$sig" != "$prev" ]; then
    {
      echo "CHANGE i=$i ts=$ts elapsed_setup=$(( $(date +%s) - t0 ))s"
      echo "  s1py=$s1py"
      echo "  s1json=$s1json"
      echo "  s2readme=$s2readme"
      echo "  s2skill=$s2skill"
      echo "  s5table=$s5table"
      echo "  s5note=$s5note"
      echo "  logh=$logh"
      echo "  scoreh=$scoreh"
      echo "  fxn=$fxn fxh=$fxh extra=${extra:-none}"
      echo "  fxfiles:"
      if [ -d corpus/fixtures/r99-window-lapse ]; then
        find corpus/fixtures/r99-window-lapse -maxdepth 1 -type f -printf '    %f %s\n' | sort
        printf '%s' "$fxdump" | sed 's/^/    /'
      fi
      echo "  prods=$prod_list"
      echo "  seats_exself=$seats_exself fleet=$fleet"
      echo "  nonwave=$nonwave"
      if [ -n "$prod_list" ]; then
        find "$SEATS" -maxdepth 1 -type f -name 'S*.md' -printf '    %f mtime=%TY-%Tm-%TdT%TH:%TM:%TS size=%s\n' | sort
      fi
    } >> "$CHG"
    prev=$sig
  fi
  t1=$(date +%s)
  echo "  sample_secs=$((t1 - t0))" >> "$LOG"
  if [ "$i" -lt 39 ]; then
    sleep 20
  fi
done
echo "POLL DONE $(date -Is)" >> "$LOG"
{
  echo "FINAL $(date -Is)"
  echo "--- sha256 producer + fixture ---"
  sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md 2>&1 || true
  sha256sum corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md 2>&1 || true
  if [ -d corpus/fixtures/r99-window-lapse ]; then
    find corpus/fixtures/r99-window-lapse -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum
  fi
  echo "--- producer reports ---"
  find "$SEATS" -maxdepth 1 -type f -name 'S*.md' -printf '%f %s\n' | sort
  echo "--- seat md count exself ---"
  find "$SEATS" -maxdepth 1 -type f -name '*.md' ! -name 'V35-shonen-format.md' | wc -l
  echo "--- fleet ---"
  ls -la "$FLEET/.ufo/reports/round-99/lore.md" 2>&1 || true
} > "$SCRATCH/poll-final.txt"
echo "POLL FINAL WRITTEN $(date -Is)" >> "$LOG"
