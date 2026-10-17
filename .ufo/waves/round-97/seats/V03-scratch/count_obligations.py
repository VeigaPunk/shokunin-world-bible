#!/usr/bin/env python3
"""V03 independent obligation counter (does not import map_obligations.py).

Counts, per the contract's scope, one obligation per:
  entities[i].first_appearance, entities[i].claims[j], relations[k], timeline[l]
and prints the pointers so they can be compared with the map's row pointers.
Usage: count_obligations.py <cluster-dir>
"""
import json, sys, pathlib

cluster = pathlib.Path(sys.argv[1])
ents = json.loads((cluster / "entities.json").read_text())
rels = json.loads((cluster / "relations.json").read_text())
tl = json.loads((cluster / "timeline.json").read_text())

ptrs = []
for i, e in enumerate(ents):
    ptrs.append(f"entities.json#/{i}/first_appearance")
    for j, _ in enumerate(e.get("claims", [])):
        ptrs.append(f"entities.json#/{i}/claims/{j}")
for k, _ in enumerate(rels):
    ptrs.append(f"relations.json#/{k}")
for l, _ in enumerate(tl):
    ptrs.append(f"timeline.json#/{l}")
for p in ptrs:
    print(p)
print(f"TOTAL={len(ptrs)}")
