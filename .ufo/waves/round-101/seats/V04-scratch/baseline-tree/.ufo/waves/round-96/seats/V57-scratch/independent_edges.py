#!/usr/bin/env python3
"""V57 independent dependency-edge extractor. Own code, independent of the C3 tool.
Prints, per fixture dir: event_id -> sorted depends_on, relation endpoints, sha256 of timeline/relations."""
import json, hashlib, sys, os

FIX = "/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures"

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def edges(d):
    tl = json.load(open(os.path.join(d, "timeline.json")))
    rel = json.load(open(os.path.join(d, "relations.json")))
    out = {}
    for ev in tl:
        out[ev["id"]] = sorted(ev.get("depends_on", []))
    rel_eps = [[r["from"], r["to"], r.get("type")] for r in rel]
    return out, rel_eps

for name in ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response"]:
    d = os.path.join(FIX, name)
    if not os.path.isdir(d):
        print(f"{name}: ABSENT")
        continue
    e, r = edges(d)
    print(f"== {name}")
    for k in sorted(e):
        print(f"  {k} -> {e[k]}")
    print(f"  relations: {r}")
    print(f"  sha256 timeline.json: {sha(os.path.join(d,'timeline.json'))}")
    print(f"  sha256 relations.json: {sha(os.path.join(d,'relations.json'))}")
