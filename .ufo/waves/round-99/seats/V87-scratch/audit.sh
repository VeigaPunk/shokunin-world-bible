#!/bin/bash
# V87 scope-final audit. Read-only. Writes only under V87-scratch.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
PARENT=/home/vgpnk/Projects/shokunin
SEATS="$LANE/.ufo/waves/round-99/seats"
OUT="$SEATS/V87-scratch"
STAMP=$(date --iso-8601=seconds)
cd "$LANE" || exit 1

exec > >(tee "$OUT/audit-raw.txt") 2>&1

echo "=== V87 SCOPE-FINAL AUDIT $STAMP ==="
echo "pwd=$(pwd)"
echo "HEAD=$(git rev-parse HEAD)"
echo "HEAD_ONELINE=$(git log -1 --oneline)"
echo "NAMED_BASELINE=4265df5e86e4121bde4125b649b89bb1676676a5"
echo "commits HEAD not in 4265df5:"
git log --oneline 4265df5..HEAD

echo
echo "=== 1. porcelain summary ==="
echo "-- porcelain -uall line count --"
git status --porcelain=v1 -uall | wc -l
echo "-- status letters --"
git status --porcelain=v1 -uall | awk '{print substr($0,1,2)}' | sort | uniq -c
echo "-- non-untracked (tracked changes) --"
git status --porcelain=v1 -uall | grep -v '^?? ' || echo "(none)"
echo "-- diff --stat vs HEAD --"
git diff --stat
echo "-- diff --numstat vs HEAD --"
git diff --numstat

echo
echo "=== 2. declared tracked ownership vs actual tracked dirt ==="
# owned tracked paths
OWNED_TRACKED=(
  corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/README.md
  SKILL.md
)
echo "-- owned tracked status --"
git status --porcelain=v1 -- "${OWNED_TRACKED[@]}"
echo "-- tracked dirt NOT in owned set --"
git status --porcelain=v1 -uall | grep -v '^?? ' | awk '{print $NF}' | while read -r p; do
  case "$p" in
    corpus/tools/dependency_freeze.py|corpus/tools/dependency-freeze-contract.json|corpus/tools/README.md|SKILL.md) ;;
    *) echo "OUT-OF-OWNERSHIP $p" ;;
  esac
done

echo
echo "=== 3. untracked path classification ==="
git status --porcelain=v1 -uall | grep '^?? ' | sed 's/^?? //' > "$OUT/untracked-paths.txt"
echo "untracked_count=$(wc -l < "$OUT/untracked-paths.txt")"
python3 - << 'PY'
from pathlib import Path
out = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V87-scratch")
paths = (out / "untracked-paths.txt").read_text().splitlines()
buckets = {
    "fixture_r99": [],
    "knowledge_r99_declared": [],
    "seat_reports": [],
    "seat_scratch": [],
    "wave_root_outside_seats": [],
    "other": [],
}
declared_knowledge = {
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
}
for p in paths:
    if p.startswith("corpus/fixtures/r99-window-lapse/"):
        buckets["fixture_r99"].append(p)
    elif p in declared_knowledge:
        buckets["knowledge_r99_declared"].append(p)
    elif p.startswith("corpus/knowledge/r99"):
        buckets["other"].append(p)  # r99 knowledge not in the declared pair
    elif p.startswith(".ufo/waves/round-99/seats/") and p.endswith(".md") and p.count("/") == 4:
        buckets["seat_reports"].append(p)
    elif p.startswith(".ufo/waves/round-99/seats/"):
        buckets["seat_scratch"].append(p)
    elif p.startswith(".ufo/waves/round-99/"):
        buckets["wave_root_outside_seats"].append(p)
    else:
        buckets["other"].append(p)

print("bucket_counts:")
for k, v in buckets.items():
    print(f"  {k}: {len(v)}")
print("fixture_files:")
for p in sorted(buckets["fixture_r99"]):
    print(f"  {p}")
print("knowledge_declared:")
for p in sorted(buckets["knowledge_r99_declared"]):
    print(f"  {p}")
print("seat_reports:")
for p in sorted(buckets["seat_reports"]):
    print(f"  {p}")
print("wave_root_outside_seats:")
for p in buckets["wave_root_outside_seats"][:200]:
    print(f"  {p}")
if len(buckets["wave_root_outside_seats"]) > 200:
    print(f"  ... {len(buckets['wave_root_outside_seats'])-200} more")
print("OTHER (out of declared set):")
for p in buckets["other"][:400]:
    print(f"  {p}")
if len(buckets["other"]) > 400:
    print(f"  ... {len(buckets['other'])-400} more")
# top-level seat dir prefixes for scratch
from collections import Counter
c = Counter()
for p in buckets["seat_scratch"]:
    parts = p.split("/")
    # .ufo/waves/round-99/seats/<dir>/...
    if len(parts) >= 5:
        c[parts[4]] += 1
print("scratch_top_counts (top 30):")
for name, n in c.most_common(30):
    print(f"  {n:6d}  {name}")
(out / "bucket-other.txt").write_text("\n".join(buckets["other"]) + ("\n" if buckets["other"] else ""))
(out / "bucket-wave-root.txt").write_text("\n".join(buckets["wave_root_outside_seats"]) + ("\n" if buckets["wave_root_outside_seats"] else ""))
(out / "bucket-reports.txt").write_text("\n".join(sorted(buckets["seat_reports"])) + ("\n" if buckets["seat_reports"] else ""))
PY

echo
echo "=== 4. expected fixture ten ==="
EXPECTED="README.md claim-excerpt-map.md contradictions.json entities.json fictional-excerpts.md inspiration-note.md relations.json source-excerpt.md sources.json timeline.json"
for f in $EXPECTED; do
  p="corpus/fixtures/r99-window-lapse/$f"
  if [[ -f "$p" ]]; then
    stat -c '%s %y %n' "$p"
  else
    echo "MISSING $p"
  fi
done
echo "-- extra files under fixture (not the ten) --"
find corpus/fixtures/r99-window-lapse -mindepth 1 | while read -r p; do
  base=$(basename "$p")
  case " $EXPECTED " in
    *" $base "*) ;;
    *) echo "EXTRA $p" ;;
  esac
done

echo
echo "=== 5. knowledge r99 ==="
ls -l corpus/knowledge/r99* 2>&1 || true
find corpus/knowledge -maxdepth 1 -name 'r99*' -printf '%s %y %p\n'

echo
echo "=== 6. SKILL.md diff (freeze-row-only check) ==="
if git diff --quiet -- SKILL.md; then
  echo "SKILL.md clean vs HEAD (S2 freeze row NOT landed or identical)"
else
  echo "-- SKILL.md diff --"
  git diff -- SKILL.md
fi
echo "=== 6b. tools README diff stat ==="
if git diff --quiet -- corpus/tools/README.md; then
  echo "corpus/tools/README.md clean vs HEAD"
else
  git diff --stat -- corpus/tools/README.md
  echo "-- README diff (first 200 lines) --"
  git diff -- corpus/tools/README.md | head -200
fi
echo "=== 6c. contract diff stat ==="
if git diff --quiet -- corpus/tools/dependency-freeze-contract.json; then
  echo "contract clean vs HEAD"
else
  git diff --stat -- corpus/tools/dependency-freeze-contract.json
fi
echo "=== 6d. dependency_freeze.py diff stat ==="
git diff --stat -- corpus/tools/dependency_freeze.py

echo
echo "=== 7. producer reports ==="
find "$SEATS" -maxdepth 1 -name 'S*.md' -printf '%s %y %f\n' | sort

echo
echo "=== 8. report-path exclusivity ==="
echo "-- md files under round-99 not directly in seats/ --"
find .ufo/waves/round-99 -name '*.md' -type f ! -path '.ufo/waves/round-99/seats/*.md' ! -path '.ufo/waves/round-99/seats/*/*' -printf '%p\n'
echo "-- md directly in seats/ --"
find "$SEATS" -maxdepth 1 -name '*.md' -printf '%f\n' | sort
echo "seat_md_count=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f | wc -l)"
echo "-- subtracting self --"
find "$SEATS" -maxdepth 1 -name '*.md' -type f ! -name 'V87-scope-final.md' | wc -l

echo
echo "=== 9. parent tree ==="
echo "-- parent HEAD --"
git -C "$PARENT" rev-parse --short HEAD
git -C "$PARENT" log -1 --oneline
echo "-- parent porcelain -uall (first 80) --"
git -C "$PARENT" status --porcelain=v1 -uall | head -80
echo "parent_porcelain_count=$(git -C "$PARENT" status --porcelain=v1 -uall | wc -l)"
echo "-- parent check-ignore lore-shokunin --"
git -C "$PARENT" check-ignore -v lore-shokunin || true

echo
echo "=== 10. ignored class created/touched since 22:00 local (wave window) ==="
# list ignored paths that are round-99 or lane-root self-test or corpus/tools pycache with mtime >= 2026-10-17 22:00
echo "-- git check-ignore samples --"
git check-ignore -v corpus/tools/__pycache__ v05-self-test-scratch 2>&1 || true
echo "-- round-99 ignored --"
git status --porcelain=v1 --ignored -uall -- .ufo/waves/round-99 | awk '$1=="!!" {print}' | head -50
echo "round99_ignored_count=$(git status --porcelain=v1 --ignored -uall -- .ufo/waves/round-99 | awk '$1=="!!"' | wc -l)"
echo "-- lane-root self-test dirs mtime --"
find . -maxdepth 2 -name '*-self-test-*' -printf '%T@ %y %p\n' 2>/dev/null | head -40
echo "-- corpus/tools __pycache__ mtime --"
find corpus/tools -name '__pycache__' -printf '%T@ %p\n' 2>/dev/null
find corpus/tools -name '*.pyc' -printf '%T@ %s %p\n' 2>/dev/null | head -20

echo
echo "=== 11. scratch size (top 15 seat dirs) ==="
du -sh "$SEATS"/*-scratch "$SEATS"/scratch 2>/dev/null | sort -h | tail -15
echo "-- seats total --"
du -sh "$SEATS"

echo
echo "=== 12. diff vs named baseline 4265df5 (tracked, excluding .ufo) ==="
git diff --stat 4265df5 -- . ':(exclude).ufo'

echo
echo "=== AUDIT-END $STAMP ==="
