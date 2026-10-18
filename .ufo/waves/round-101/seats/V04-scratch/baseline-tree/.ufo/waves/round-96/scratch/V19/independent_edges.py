#!/usr/bin/env python3
"""V19 independent (non-Q3) edge-inventory extractor for the continuation chain.

Deliberately written without reading dependency_freeze.py: raw json.load of
timeline.json / relations.json, print sorted edges + digests.
"""
import hashlib
import json
import os
import sys


def main(dirs):
    for d in dirs:
        tl = json.load(open(os.path.join(d, "timeline.json")))
        rel = json.load(open(os.path.join(d, "relations.json")))
        edges = {}
        for rec in tl:
            deps = rec.get("depends_on")
            edges[rec["id"]] = sorted(deps) if isinstance(deps, list) else deps
        rends = sorted((r.get("from"), r.get("to")) for r in rel) if isinstance(rel, list) else rel
        print(f"== {d}")
        print(f"   events={len(tl)} edges={json.dumps({k: edges[k] for k in sorted(edges)})}")
        print(f"   relations={len(rel)} endpoints={json.dumps(rends)}")
        for f in ("timeline.json", "relations.json"):
            p = os.path.join(d, f)
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            print(f"   sha256 {f} {h}")


if __name__ == "__main__":
    main(sys.argv[1:])
