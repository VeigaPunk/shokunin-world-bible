#!/usr/bin/env python3
"""V49 independent recompute of the dependency-freeze pin inventory.

Does NOT import the tool: re-derives each pinned fixture's event->depends_on
sets, endpoints, relation triples, per-file sha256 and content digest from raw
bytes, and compares against corpus/tools/dependency-freeze-contract.json.
"""
import hashlib, json, sys
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
CONTRACT = R / "corpus/tools/dependency-freeze-contract.json"
DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")

contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
problems = []
for name, pin in sorted(contract.get("pins", {}).items()):
    fx = R / pin["fixture"]
    if not fx.is_dir():
        problems.append(f"{name}: fixture dir missing {pin['fixture']}")
        continue
    files = {}
    for fn in DATA_FILES:
        p = fx / fn
        if p.is_file():
            files[fn] = p.read_bytes()
    digests = {fn: hashlib.sha256(raw).hexdigest() for fn, raw in files.items()}
    content = hashlib.sha256(json.dumps(digests, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    tl = json.loads(files["timeline.json"].decode())
    rel = json.loads(files["relations.json"].decode())
    events = {}
    for rec in tl:
        deps = rec.get("depends_on", [])
        events[rec["id"]] = {
            "depends_on": sorted(set(deps)),
            "endpoint": {k: rec.get(k) for k in ("tick", "entity_id", "place_id")},
        }
    triples = sorted([r["from"], r["to"], r["type"]] for r in rel)
    counts = {"events": len(events), "dependency_edges": sum(len(e["depends_on"]) for e in events.values()),
              "relations": len(triples)}
    ent = json.loads(files["entities.json"].decode()) if "entities.json" in files else None
    src = json.loads(files["sources.json"].decode()) if "sources.json" in files else None
    if isinstance(ent, list): counts["entities"] = len(ent)
    if isinstance(src, list): counts["sources"] = len(src)
    checks = [
        ("files", digests == pin.get("files")),
        ("content_sha256", content == pin.get("content_sha256")),
        ("events", events == pin.get("events")),
        ("relations", triples == pin.get("relations")),
        ("counts", counts == pin.get("counts")),
    ]
    bad = [k for k, ok in checks if not ok]
    status = "OK" if not bad else "MISMATCH:" + ",".join(bad)
    print(f"PIN {name}: path={pin['fixture']} revision={pin.get('revision')} {status}")
    if bad:
        problems.append(f"{name}: {bad}")
        if "events" in bad:
            print("  recomputed events:", json.dumps(events, sort_keys=True))
            print("  pinned events:   ", json.dumps(pin.get("events"), sort_keys=True))
        if "counts" in bad:
            print("  recomputed counts:", counts, "pinned:", pin.get("counts"))
print("RECOMPUTE", "ALL-PINS-MATCH" if not problems else f"PROBLEMS {problems}")
sys.exit(0 if not problems else 1)
