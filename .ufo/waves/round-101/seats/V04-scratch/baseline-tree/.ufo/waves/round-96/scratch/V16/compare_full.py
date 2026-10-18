#!/usr/bin/env python3
"""V16 one-to-one pin comparison, independent of dependency_freeze.py.

Recomputes, from raw fixture bytes with stdlib only:
  - per-file sha256 for the 5 declared DATA_FILES that exist
  - content_sha256 exactly as the contract's precedence defines it
    (sha256 of json.dumps({name: sha256(raw)}, sort_keys=True,
     separators=(",", ":")).encode())
  - event -> sorted(set(depends_on)) and endpoint {tick, entity_id, place_id}
  - relation triples [from, to, type] sorted
  - counts {events, dependency_edges, relations, entities, sources}
then compares each field one-to-one against contract pins[name].
"""
import hashlib
import json
import os
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
CONTRACT = os.path.join(ROOT, "corpus/tools/dependency-freeze-contract.json")
CHAIN = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath",
         "r96-crossing-response"]
DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json",
              "contradictions.json")

contract = json.load(open(CONTRACT))
pins = contract["pins"]
fails = []
checks = 0


def ck(label, ok, detail=""):
    global checks
    checks += 1
    if not ok:
        fails.append(f"{label}: {detail}")
    return ok


def build(fixture):
    d = os.path.join(ROOT, "corpus", "fixtures", fixture)
    files = {}
    for name in DATA_FILES:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            files[name] = open(p, "rb").read()
    payload = json.dumps({n: hashlib.sha256(r).hexdigest() for n, r in files.items()},
                         sort_keys=True, separators=(",", ":"))
    content = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    parsed = {n: json.loads(r.decode("utf-8")) for n, r in files.items()}
    events = {}
    for rec in parsed["timeline.json"]:
        events[rec["id"]] = {
            "depends_on": sorted(set(rec.get("depends_on", []))),
            "endpoint": {k: rec.get(k) for k in ("tick", "entity_id", "place_id")},
        }
    triples = sorted([r["from"], r["to"], r["type"]] for r in parsed["relations.json"])
    counts = {
        "events": len(events),
        "dependency_edges": sum(len(e["depends_on"]) for e in events.values()),
        "relations": len(triples),
    }
    for fname, key in (("entities.json", "entities"), ("sources.json", "sources")):
        if isinstance(parsed.get(fname), list):
            counts[key] = len(parsed[fname])
    return {"files": {n: hashlib.sha256(r).hexdigest() for n, r in files.items()},
            "content_sha256": content, "events": events, "relations": triples,
            "counts": counts, "dir": d}


print(f"contract revision pin: {contract.get('revision')}")
print(f"contract pins: {sorted(pins)}")
print(f"chain under test: {CHAIN}")
print("=" * 74)

for fx in CHAIN:
    obs = build(fx)
    pin = pins.get(fx)
    print(f"\n### {fx}")
    if pin is None:
        ck(f"{fx}/pinned", False, "no pin present")
        print("  NO PIN")
        continue
    print(f"  fixture path pin={pin.get('fixture')} observed dir={obs['dir']}")
    ck(f"{fx}/fixture-path", pin.get("fixture") == f"corpus/fixtures/{fx}",
       f"pin {pin.get('fixture')!r}")
    # per-file digests
    for name in sorted(set(pin["files"]) | set(obs["files"])):
        pv, ov = pin["files"].get(name), obs["files"].get(name)
        ck(f"{fx}/file:{name}", pv == ov, f"pin={pv} observed={ov}")
        print(f"  file {name:<22} {'MATCH' if pv == ov else 'MISMATCH'} {ov}")
    ck(f"{fx}/content_sha256", pin["content_sha256"] == obs["content_sha256"],
       f"pin={pin['content_sha256']} observed={obs['content_sha256']}")
    print(f"  content_sha256 {'MATCH' if pin['content_sha256'] == obs['content_sha256'] else 'MISMATCH'}"
          f" {obs['content_sha256']}")
    # events one-to-one
    pe, oe = pin["events"], obs["events"]
    ck(f"{fx}/event-id-set", set(pe) == set(oe),
       f"pin-only={sorted(set(pe) - set(oe))} observed-only={sorted(set(oe) - set(pe))}")
    print(f"  event ids {'MATCH' if set(pe) == set(oe) else 'MISMATCH'} ({len(oe)}): {sorted(oe)}")
    for eid in sorted(set(pe) & set(oe)):
        pd = sorted(set(pe[eid]["depends_on"]))
        od = sorted(set(oe[eid]["depends_on"]))
        ck(f"{fx}/deps:{eid}", pd == od, f"pin={pd} observed={od}")
        if pd != od:
            print(f"    deps {eid}: MISMATCH pin={pd} observed={od}")
        pend, oend = pe[eid].get("endpoint", {}), oe[eid]["endpoint"]
        ck(f"{fx}/endpoint:{eid}", pend == oend, f"pin={pend} observed={oend}")
        if pend != oend:
            print(f"    endpoint {eid}: MISMATCH pin={pend} observed={oend}")
    # relations
    pr = [list(t) for t in pin["relations"]]
    ck(f"{fx}/relations", sorted(pr) == sorted(obs["relations"]),
       f"pin={sorted(pr)} observed={sorted(obs['relations'])}")
    print(f"  relations {'MATCH' if sorted(pr) == sorted(obs['relations']) else 'MISMATCH'}"
          f" pin={sorted(pr)} observed={sorted(obs['relations'])}")
    # counts
    pc = pin.get("counts", {})
    for key in sorted(set(pc) | set(obs["counts"])):
        ck(f"{fx}/count:{key}", pc.get(key) == obs["counts"].get(key),
           f"pin={pc.get(key)} observed={obs['counts'].get(key)}")
    print(f"  counts {'MATCH' if pc == obs['counts'] else 'MISMATCH'} pin={pc} observed={obs['counts']}")

print("\n" + "=" * 74)
print(f"checks run: {checks}; failures: {len(fails)}")
for f in fails:
    print("  FAIL " + f)
print("VERDICT:", "ALL PINS MATCH INDEPENDENT RECOMPUTE" if not fails else "DISCREPANCIES")
sys.exit(0 if not fails else 1)
