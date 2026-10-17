#!/usr/bin/env python3
"""R5 scratch: verify r97 inherited rows/anchors/parsed values against r96."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = ROOT / "corpus/fixtures/r96-crossing-response"
R97 = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"

# 16 inherited rows: (id, pointer, source_id, span, anchor) from the r96 map
INHERITED = [
    ("J01", "entities.json#/0/first_appearance", "paired-clock", "12", "Aru carried the north lantern at Quiet Rise"),
    ("J02", "entities.json#/1/first_appearance", "paired-clock", "13", "Evin held the south bell at Salt Court"),
    ("J03", "entities.json#/2/first_appearance", "paired-clock", "12", "Aru carried the north lantern at Quiet Rise"),
    ("J04", "entities.json#/3/first_appearance", "paired-clock", "13", "Evin held the south bell at Salt Court"),
    ("J05", "entities.json#/4/first_appearance", "crossing-minute", "17", "The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court."),
    ("J06", "entities.json#/0/claims/0", "paired-clock", "12", "Tick 9: Aru carried the north lantern at Quiet Rise."),
    ("J07", "entities.json#/1/claims/0", "paired-clock", "13", "Tick 9: Evin held the south bell at Salt Court."),
    ("J08", "entities.json#/2/claims/0", "paired-clock", "12", "north lantern at Quiet Rise"),
    ("J09", "entities.json#/3/claims/0", "paired-clock", "13", "south bell at Salt Court"),
    ("J10", "entities.json#/4/claims/0", "crossing-minute", "18", "After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10."),
    ("J11", "relations.json#/0", "crossing-minute", "19", "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair."),
    ("J12", "timeline.json#/0", "paired-clock", "12", "Aru carried the north lantern at Quiet Rise"),
    ("J13", "timeline.json#/1", "paired-clock", "13", "Evin held the south bell at Salt Court"),
    ("J14", "timeline.json#/2", "crossing-minute", "18-20", "Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint."),
    ("J15", "timeline.json#/3", "aru-aftermath-note", "22-31", "Tick 11: I waited at the Chalk Stair through the agreed bell."),
    ("J16", "timeline.json#/4", "evin-response-note", "33-42", "Tick 12: I was at Salt Court through the same agreed bell."),
]

def grep_line(anchor, path):
    r = subprocess.run(["grep", "-nF", "--", anchor, str(path)], capture_output=True, text=True)
    lines = []
    if r.returncode == 0:
        for ln in r.stdout.splitlines():
            num = ln.split(":", 1)[0]
            if num.isdecimal():
                lines.append(int(num))
    return lines

print("== inherited anchor line numbers in r97 fictional-excerpts.md ==")
ok = True
for jid, ptr, src, span, anchor in INHERITED:
    hits = grep_line(anchor, R97 / "fictional-excerpts.md")
    parts = span.split("-")
    first = int(parts[0]); last = int(parts[1]) if len(parts) > 1 else first
    in_span = [h for h in hits if first <= h <= last]
    status = "OK" if hits and in_span and all(first <= h <= last for h in hits) else "CHECK"
    if status != "OK":
        ok = False
    print(f"{jid}: span={span} hits={hits} -> {status}")
print("INHERITED ANCHORS ALL-OK" if ok else "INHERITED ANCHORS PROBLEM")

print()
print("== byte-prefix: r96 excerpt is a prefix of r97 excerpt ==")
b96 = (R96 / "fictional-excerpts.md").read_bytes()
b97 = (R97 / "fictional-excerpts.md").read_bytes()
print("r96 bytes:", len(b96), "r97 bytes:", len(b97), "prefix:", b97[:len(b96)] == b96)
print("append starts at line:", b96.decode().count("\n") + 1)

print()
print("== parsed-value identity of inherited JSON rows ==")
for name in ("sources.json", "timeline.json"):
    a = json.loads((R96 / name).read_text())
    b = json.loads((R97 / name).read_text())
    n = len(a)
    print(f"{name}: r96 rows={n} r97 rows={len(b)} inherited-identical={a == b[:n]} new={b[n:]}")

print()
print("== r97 structural checks ==")
tl = json.loads((R97 / "timeline.json").read_text())
src = json.loads((R97 / "sources.json").read_text())
ent = json.loads((R97 / "entities.json").read_text())
rel = json.loads((R97 / "relations.json").read_text())
con = json.loads((R97 / "contradictions.json").read_text())
last = tl[-1]
print("counts entities/relations/events/sources:", len(ent), len(rel), len(tl), len(src), "contradictions:", len(con))
print("last event:", json.dumps(last, sort_keys=True))
print("last source:", json.dumps(src[-1], sort_keys=True))
exp = {"id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru", "place_id": "chalk-stair",
       "depends_on": ["response-evin-salt-court"], "source_id": "aru-acknowledgment-note"}
checks = {k: last[k] == v for k, v in exp.items()}
print("event field checks:", checks)
print("ALL STRUCTURAL OK" if all(checks.values()) else "STRUCTURAL PROBLEM")
