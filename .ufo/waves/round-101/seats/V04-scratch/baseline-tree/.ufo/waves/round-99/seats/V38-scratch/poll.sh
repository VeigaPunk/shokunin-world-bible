#!/bin/bash
# V38 poll-wait: artifacts AND producer reports. 20s cadence, max 40.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS="$ROOT/.ufo/waves/round-99/seats"
LOG="$SEATS/V38-scratch/poll.log"
cd "$ROOT" || exit 1
reports=(
  S1-freeze-hygiene.md
  S2-tools-docs.md
  S3-fixture-author.md
  S4-fixture-docs.md
  S5-knowledge-notes.md
)
arts=(
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
  corpus/fixtures/r99-window-lapse/entities.json
  corpus/fixtures/r99-window-lapse/relations.json
  corpus/fixtures/r99-window-lapse/timeline.json
  corpus/fixtures/r99-window-lapse/sources.json
  corpus/fixtures/r99-window-lapse/contradictions.json
  corpus/fixtures/r99-window-lapse/README.md
  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
  corpus/fixtures/r99-window-lapse/inspiration-note.md
  corpus/fixtures/r99-window-lapse/source-excerpt.md
  corpus/knowledge/r99-gate-blind-spot-table.md
  corpus/knowledge/r99-lapse-scope-note.md
)
for try in $(seq 1 40); do
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
    # also note any other S[1-5]-*.md not in the expected set
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
    if [[ -f corpus/tools/dependency-freeze-contract.json ]]; then
      python3 - <<'PY'
import json
c=json.load(open("corpus/tools/dependency-freeze-contract.json"))
pins=c.get("pins",{})
print("CONTRACT schema", c.get("schema_version"), "pins", list(pins), "self_test", len((c.get("self_test") or {})))
# payload file counts if present
for name, pin in pins.items():
    files=pin.get("files") or pin.get("digests") or pin.get("file_digests") or {}
    if isinstance(files, dict):
        print("PIN", name, "filekeys", len(files), "schema", pin.get("schema_version") or pin.get("payload_schema_version"))
PY
    fi
    if [[ $missing -eq 0 ]]; then
      echo "ALL_PRESENT"
    else
      echo "STILL_WAITING"
    fi
  } >> "$LOG"
  if grep -q '^ALL_PRESENT$' <(tail -n 30 "$LOG"); then
    # require two consecutive ALL_PRESENT so a mid-write is not treated as delivered
    if [[ $(grep -c '^ALL_PRESENT$' "$LOG") -ge 2 ]]; then
      echo "STABLE_EXIT try=$try" >> "$LOG"
      exit 0
    fi
  fi
  sleep 20
done
echo "EXHAUSTED 40" >> "$LOG"
exit 2
