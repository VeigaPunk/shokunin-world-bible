#!/usr/bin/env python3
"""V39: build differential probe copies of r88 in my scratch dir.

Creates under OUT:
  raw-mut/<slug>   one per enumerated raw obligation: that source value is
                   changed to the sentinel "v39-mutated" (map untouched), so a
                   tool that sees the obligation must report exactly one
                   source_id_mismatch naming that pointer.
  raw-mut-all      every raw source value changed to the sentinel.
  row-drop/<slug>  one per map row: that table row removed (raw untouched), so
                   a tool that maps the row must report missing_obligation (or
                   its editorial equivalent) naming that pointer.
  editorial-drop   both editorial rows removed.
Each copy is a full byte copy of the fixture except the single intended change.
"""
import json
import shutil
import sys
from pathlib import Path

SRC = Path("corpus/fixtures/r88-m3-maya-cluster")
OUT = Path(".ufo/waves/round-95/seats/V39-scratch/probes")

OBLIGATIONS = [
    ("entities-0-first", "entities.json", ["0"], "first_appearance"),
    ("entities-0-claim-0", "entities.json", ["0", "claims", "0"], "source_id"),
    ("entities-1-first", "entities.json", ["1"], "first_appearance"),
    ("entities-1-claim-0", "entities.json", ["1", "claims", "0"], "source_id"),
    ("entities-2-first", "entities.json", ["2"], "first_appearance"),
    ("entities-2-claim-0", "entities.json", ["2", "claims", "0"], "source_id"),
    ("entities-3-first", "entities.json", ["3"], "first_appearance"),
    ("entities-3-claim-0", "entities.json", ["3", "claims", "0"], "source_id"),
    ("timeline-0", "timeline.json", ["0"], "source_id"),
    ("timeline-1", "timeline.json", ["1"], "source_id"),
]

SENTINEL = "v39-mutated"


def copy_cluster(dest):
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest)


def set_value(data, path, key):
    node = data
    for part in path:
        node = node[int(part)] if part.isdigit() else node[part]
    node[key] = SENTINEL


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    # raw-side mutations
    for slug, filename, path, key in OBLIGATIONS:
        dest = OUT / "raw-mut" / slug
        copy_cluster(dest)
        data = json.loads((dest / filename).read_text(encoding="utf-8"))
        set_value(data, path, key)
        (dest / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    dest = OUT / "raw-mut-all"
    copy_cluster(dest)
    by_file = {}
    for slug, filename, path, key in OBLIGATIONS:
        data = by_file.setdefault(filename, json.loads((dest / filename).read_text(encoding="utf-8")))
        set_value(data, path, key)
    for filename, data in by_file.items():
        (dest / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    # map-side row drops: only rows of tables whose header names the anchor columns
    map_text = (SRC / "claim-excerpt-map.md").read_text(encoding="utf-8")
    map_lines = map_text.splitlines()
    data_rows = []
    in_map_table = False
    for i, line in enumerate(map_lines):
        if line.lstrip().startswith("|"):
            if "Excerpt path:line" in line:
                in_map_table = True
                continue
            if not in_map_table:
                continue
            first = line.strip().strip("|").split("|")[0].strip()
            if first == "ID" or first.startswith("---"):
                continue
            data_rows.append((i, line))
        else:
            in_map_table = False
    slugs = []
    for i, line in data_rows:
        first = line.strip().strip("|").split("|")[0].strip()
        if first in ("ID", "") or first.startswith("---"):
            continue
        slug = first.lower().replace(" ", "-")
        slugs.append((slug, i, first))
    for slug, i, first in slugs:
        dest = OUT / "row-drop" / slug
        copy_cluster(dest)
        kept = [line for j, line in enumerate(map_lines) if j != i]
        (dest / "claim-excerpt-map.md").write_text("\n".join(kept) + "\n", encoding="utf-8")
    dest = OUT / "editorial-drop"
    copy_cluster(dest)
    kept = [line for j, line in enumerate(map_lines)
            if not (line.startswith("| S1 ") or line.startswith("| S2 "))]
    (dest / "claim-excerpt-map.md").write_text("\n".join(kept) + "\n", encoding="utf-8")
    print(f"built raw-mut x{len(OBLIGATIONS)}, raw-mut-all, row-drop x{len(slugs)}, editorial-drop")
    print("row-drop slugs:", ", ".join(slug for slug, _, _ in slugs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
