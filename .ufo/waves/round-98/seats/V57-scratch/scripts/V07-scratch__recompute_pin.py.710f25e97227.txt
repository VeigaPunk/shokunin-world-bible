#!/usr/bin/env python3
"""V07: independently recompute a fixture's pin-shape (events/digests/counts)
mirroring dependency_freeze.py build_model, without importing the tool."""
import hashlib, json, sys
from pathlib import Path

DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")
REQUIRED = ("relations.json", "timeline.json")

fixture = Path(sys.argv[1])
files = {}
for name in DATA_FILES:
    p = fixture / name
    if p.is_file():
        files[name] = p.read_bytes()
for name in REQUIRED:
    if name not in files:
        print(f"MISSING required {name}"); sys.exit(2)

parsed = {name: json.loads(raw.decode("utf-8")) for name, raw in files.items()}
timeline, relations = parsed["timeline.json"], parsed["relations.json"]
events = {}
for rec in timeline:
    deps = sorted(set(rec.get("depends_on", [])))
    events[rec["id"]] = {"depends_on": deps,
                         "endpoint": {k: rec.get(k) for k in ("tick", "entity_id", "place_id")}}
triples = sorted([r["from"], r["to"], r["type"]] for r in relations)
counts = {"events": len(events), "dependency_edges": sum(len(e["depends_on"]) for e in events.values()),
          "relations": len(triples)}
for name, key in (("entities.json", "entities"), ("sources.json", "sources")):
    v = parsed.get(name)
    if isinstance(v, list):
        counts[key] = len(v)

def sha(raw): return hashlib.sha256(raw).hexdigest()
file_digests = {n: sha(raw) for n, raw in sorted(files.items())}
payload = json.dumps(file_digests, sort_keys=True, separators=(",", ":"))
content = sha(payload.encode("utf-8"))

out = {"fixture": str(fixture), "content_sha256": content, "files": file_digests,
       "events": events, "relations": triples, "counts": counts}
print(json.dumps(out, indent=2, sort_keys=True))
