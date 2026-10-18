#!/bin/bash
# Continuation after the first poller was killed at the 300s tool cap (tries 1-15 logged).
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V38-scratch/poll.log"
cd "$ROOT" || exit 1
echo "=== CONTINUATION $(date -u +%Y-%m-%dT%H:%M:%SZ) first poller died at tool timeout after try 15 ===" >> "$LOG"
reports=(
  S1-freeze-hygiene.md
  S2-tools-docs.md
  S3-fixture-author.md
  S4-fixture-docs.md
  S5-knowledge-notes.md
)
arts=(
  corpus/knowledge/r99-gate-blind-spot-table.md
  corpus/knowledge/r99-lapse-scope-note.md
)
for try in $(seq 16 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  {
    echo "=== TRY $try $ts ==="
    missing=0
    for r in "${reports[@]}"; do
      if [[ -f "$SEATS/$r" ]]; then
        echo "REPORT $r $(stat -c '%s %y' "$SEATS/$r")"
      else
        echo "ABSENT $r"
        missing=1
      fi
    done
    for f in "$SEATS"/S[1-5]-*.md; do
      [[ -f "$f" ]] || continue
      base=$(basename "$f")
      known=0
      for r in "${reports[@]}"; do [[ "$base" == "$r" ]] && known=1; done
      if [[ $known -eq 0 ]]; then echo "EXTRA-REPORT $base"; fi
    done
    for a in "${arts[@]}"; do
      if [[ -f "$a" ]]; then
        echo "ART $a $(stat -c '%s' "$a") $(sha256sum "$a" | awk '{print $1}')"
      else
        echo "ABSENT $a"
        missing=1
      fi
    done
    sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
    python3 - <<'PY'
import json
c=json.load(open("corpus/tools/dependency-freeze-contract.json"))
pins=c.get("pins",{})
exp=(c.get("self_test") or {}).get("expected") or {}
print("CONTRACT schema", c.get("schema_version"), "pins", list(pins), "cases", len(exp))
for name, pin in pins.items():
    files=pin.get("files") or {}
    print("PIN", name, "nfiles", len(files) if isinstance(files, dict) else "NA", "payload_schema", pin.get("payload_schema_version"))
PY
    if [[ $missing -eq 0 ]]; then
      echo "ALL_PRESENT"
    else
      echo "STILL_WAITING"
    fi
  } >> "$LOG"
  # two consecutive ALL_PRESENT
  if [[ $(tail -n 8 "$LOG" | grep -c '^ALL_PRESENT$') -ge 1 ]]; then
    prev=$(grep -c '^ALL_PRESENT$' "$LOG")
    if [[ $prev -ge 2 ]]; then
      echo "STABLE_EXIT try=$try" >> "$LOG"
      exit 0
    fi
  fi
  sleep 20
done
echo "EXHAUSTED 40" >> "$LOG"
exit 2
