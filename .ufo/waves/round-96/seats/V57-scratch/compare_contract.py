#!/usr/bin/env python3
"""V57: full independent comparison of dependency-freeze-contract.json vs my own extraction.
Implements the contract's declared semantics from scratch (not importing the tool)."""
import json, hashlib, os

L = "/home/vgpnk/Projects/shokunin/lore-shokunin"
FIX = os.path.join(L, "corpus/fixtures")
CONTRACT = os.path.join(L, "corpus/tools/dependency-freeze-contract.json")
CHAIN = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response"]
DATA = ["entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json"]

def sha(raw): return hashlib.sha256(raw).hexdigest()

def model(d):
    files = {}
    for n in DATA:
        p = os.path.join(d, n)
        if os.path.isfile(p): files[n] = open(p, "rb").read()
    tl = json.loads(files["timeline.json"])
    rel = json.loads(files["relations.json"])
    events = {}
    for rec in tl:
        events[rec["id"]] = {
            "depends_on": sorted(set(rec.get("depends_on", []))),
            "endpoint": {k: rec.get(k) for k in ("tick", "entity_id", "place_id")},
        }
    triples = sorted([[r["from"], r["to"], r["type"]] for r in rel])
    content = sha(json.dumps({n: sha(raw) for n, raw in sorted(files.items())},
                             sort_keys=True, separators=(",", ":")).encode())
    counts = {"events": len(events),
              "dependency_edges": sum(len(e["depends_on"]) for e in events.values()),
              "relations": len(triples)}
    for n, key in (("entities.json", "entities"), ("sources.json", "sources")):
        if n in files:
            v = json.loads(files[n])
            if isinstance(v, list): counts[key] = len(v)
    return {"events": events, "relations": triples, "content_sha256": content,
            "files": {n: sha(raw) for n, raw in sorted(files.items())}, "counts": counts}

contract = json.load(open(CONTRACT))
ok = True
for name in CHAIN:
    pin = contract["pins"][name]
    mine = model(os.path.join(FIX, name))
    checks = {
        "events": pin["events"] == mine["events"],
        "relations": pin["relations"] == mine["relations"],
        "content_sha256": pin["content_sha256"] == mine["content_sha256"],
        "files": pin["files"] == mine["files"],
        "counts": pin["counts"] == mine["counts"],
    }
    bad = [k for k, v in checks.items() if not v]
    ok &= not bad
    print(f"{name}: {'ALL-MATCH' if not bad else 'MISMATCH ' + str(bad)}")
    if bad:
        for k in bad:
            print(f"   pin  {k}: {json.dumps(pin[k], sort_keys=True)[:200]}")
            print(f"   mine {k}: {json.dumps(mine[k], sort_keys=True)[:200]}")
print("OVERALL:", "ALL PINS MATCH MY INDEPENDENT EXTRACTION" if ok else "PIN DIVERGENCE FOUND")
# self-test expectation set vs tool's FROZEN_CASES
expected = sorted(contract["self_test"]["expected"].keys())
print("self_test cases in contract:", len(expected), expected)
