#!/usr/bin/env python3
"""V18 independent oracle: canonical dependency inventory + relation endpoints.

Usage: oracle.py <fixture_dir> [...]
Prints JSON: {fixture: {"edges": {event: [deps]}, "endpoints": [[from,to],...]}}
"""
import json
import sys
from pathlib import Path


def oracle(d):
    p = Path(d)
    tl = json.loads((p / "timeline.json").read_text())
    rels = json.loads((p / "relations.json").read_text())
    edges = {ev["id"]: sorted(ev.get("depends_on", [])) for ev in tl}
    endpoints = [[r["from"], r["to"]] for r in rels]
    return {"edges": edges, "endpoints": endpoints}


if __name__ == "__main__":
    out = {}
    for d in sys.argv[1:]:
        out[Path(d).name] = oracle(d)
    print(json.dumps(out, indent=2, sort_keys=True))
