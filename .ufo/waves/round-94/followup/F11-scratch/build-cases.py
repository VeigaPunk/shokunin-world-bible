#!/usr/bin/env python3
"""Build F11 negative-control scratch copies from the r93 fixture (live tree untouched)."""
import json
import shutil
from pathlib import Path

SC = Path(__file__).resolve().parent
BASE = SC / "base"
MAP_NAME = "claim-excerpt-map.md"


def fresh(name):
    target = SC / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(BASE, target)
    return target


def map_lines(case):
    return (case / MAP_NAME).read_text(encoding="utf-8").splitlines(keepends=True)


def write_map(case, lines):
    (case / MAP_NAME).write_text("".join(lines), encoding="utf-8")


def e1_index(lines):
    hits = [i for i, line in enumerate(lines)
            if line.startswith("| E1 |") and "entities.json#/0/first_appearance" in line]
    assert len(hits) == 1, hits
    return hits[0]


# (a) raw claim with no map row
case = fresh("case-a")
entities = json.loads((case / "entities.json").read_text(encoding="utf-8"))
entities[0]["claims"].append({
    "statement": "Teva adds a second unregistered note to the folio margin.",
    "source_id": "m2-record-archive",
})
(case / "entities.json").write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")

# (b) duplicate map row (exact copy of the E1 row)
case = fresh("case-b")
lines = map_lines(case)
lines.insert(e1_index(lines) + 1, lines[e1_index(lines)])
write_map(case, lines)

# (c) map row pointing at a non-obligation (well-formed pointer, no raw record)
case = fresh("case-c")
lines = map_lines(case)
row = lines[e1_index(lines)]
phantom = row.replace("`entities.json#/0/first_appearance`", "`entities.json#/99/first_appearance`")
phantom = phantom.replace("| E1 |", "| E99 |", 1)
lines.insert(e1_index(lines) + 1, phantom)
write_map(case, lines)

# (d) map row source ID differs from the raw source ID
case = fresh("case-d")
lines = map_lines(case)
idx = e1_index(lines)
assert lines[idx].count("`m2-record-archive`") == 1, lines[idx]
lines[idx] = lines[idx].replace("`m2-record-archive`", "`m2-other-archive`")
write_map(case, lines)

# (e) malformed raw JSON (entities.json truncated mid-array)
case = fresh("case-e")
text = (case / "entities.json").read_text(encoding="utf-8")
(case / "entities.json").write_text(text[: len(text) // 2], encoding="utf-8")

# (f) invalid map path: base copy is intact; only the --map argument varies
case = fresh("case-f")
outside = SC / "outside-map"
if outside.exists():
    shutil.rmtree(outside)
outside.mkdir()
shutil.copy2(BASE / MAP_NAME, outside / MAP_NAME)

print("built:", sorted(p.name for p in SC.iterdir() if p.is_dir()))
