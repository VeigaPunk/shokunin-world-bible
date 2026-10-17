#!/usr/bin/env python3
"""F15 mutation-replays: build mutant scratch copies of r94-paired-crossing.

Reads the live fixture read-only, writes only under F15-scratch/.
Each mutant prints the exact textual change applied (asserted single-occurrence).
"""
import difflib
import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
SRC = REPO / "corpus" / "fixtures" / "r94-paired-crossing"
BASE = Path(__file__).resolve().parent


def fresh(name):
    dest = BASE / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest)
    return dest


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert text.count(old) == 1, f"{path.name}: expected 1 occurrence of {old!r}, got {text.count(old)}"
    path.write_text(text.replace(old, new), encoding="utf-8")


def drop_line(path, prefix):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [line for line in lines if not line.startswith(prefix)]
    assert len(kept) == len(lines) - 1, f"{path.name}: expected exactly 1 line starting {prefix!r}"
    path.write_text("".join(kept), encoding="utf-8")


def show(name, dest, files):
    print(f"\n=== {name} ===")
    for rel in files:
        original = (SRC / rel).read_text(encoding="utf-8").splitlines(keepends=True)
        mutated = (dest / rel).read_text(encoding="utf-8").splitlines(keepends=True)
        diff = difflib.unified_diff(original, mutated, fromfile=f"live/{rel}", tofile=f"{name}/{rel}")
        print("".join(diff).rstrip() or f"(no change in {rel})")


# --- (a) break the tick-10 dependency: drop one tick-9 id from depends_on -----
dest = fresh("mut-a-drop-dep")
replace_once(dest / "timeline.json",
             '      "aru-ninth-bell",\n      "evin-ninth-bell"\n',
             '      "aru-ninth-bell"\n')
show("mut-a-drop-dep", dest, ["timeline.json"])

# --- (a2) variant: delete the tick-9 event record named by the tick-10 dep ----
dest = fresh("mut-a2-drop-event")
data = json.loads((dest / "timeline.json").read_text(encoding="utf-8"))
removed = [event for event in data if event["id"] == "evin-ninth-bell"]
assert len(removed) == 1
data = [event for event in data if event["id"] != "evin-ninth-bell"]
(dest / "timeline.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
show("mut-a2-drop-event", dest, ["timeline.json"])

# --- (b) remove one map row (relation J11) and self-consistently restate ------
INVENTORY_OLD = ("**Expected inventory:** 14 JSON facts; 2 editorial rows; "
                 "16 total mapped rows; 12 distinct excerpt anchors.")
INVENTORY_NEW = ("**Expected inventory:** 13 JSON facts; 2 editorial rows; "
                 "15 total mapped rows; 11 distinct excerpt anchors.")
dest = fresh("mut-b-drop-j11-row")
drop_line(dest / "claim-excerpt-map.md", "| J11 |")
replace_once(dest / "claim-excerpt-map.md", INVENTORY_OLD, INVENTORY_NEW)
show("mut-b-drop-j11-row", dest, ["claim-excerpt-map.md"])

# --- (b2) variant: remove entity first-appearance row J05 instead -------------
dest = fresh("mut-b2-drop-j05-row")
drop_line(dest / "claim-excerpt-map.md", "| J05 |")
replace_once(dest / "claim-excerpt-map.md", INVENTORY_OLD, INVENTORY_NEW)
show("mut-b2-drop-j05-row", dest, ["claim-excerpt-map.md"])

# --- (c) break one declared anchor span (J05: 17 -> 20) -----------------------
dest = fresh("mut-c-break-span")
replace_once(dest / "claim-excerpt-map.md",
             "| `fictional-excerpts.md` | 17 | `verbatim` | `The Chalk Stair is the named rain-dark crossing",
             "| `fictional-excerpts.md` | 20 | `verbatim` | `The Chalk Stair is the named rain-dark crossing")
show("mut-c-break-span", dest, ["claim-excerpt-map.md"])

# --- (d) change one raw source_id (timeline event 3: crossing-minute -> paired-clock)
dest = fresh("mut-d-source-id")
replace_once(dest / "timeline.json",
             '"source_id": "crossing-minute"',
             '"source_id": "paired-clock"')
show("mut-d-source-id", dest, ["timeline.json"])

print("\nmutants built under", BASE)
