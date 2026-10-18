#!/usr/bin/env python3
"""V48 independent computation: per-fixture dependency-edge inventory,
relation endpoint pairs, and sha256 digests of timeline.json / relations.json.
Not affiliated with the producer tool; used to cross-check its pin."""
import hashlib
import json
import sys
from pathlib import Path


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(fixture: Path) -> dict:
    timeline = json.loads((fixture / "timeline.json").read_text())
    relations = json.loads((fixture / "relations.json").read_text())
    edges = {ev["id"]: sorted(ev.get("depends_on", [])) for ev in timeline}
    endpoints = sorted((r["from"], r["to"]) for r in relations)
    return {
        "fixture": fixture.name,
        "events": edges,
        "event_count": len(timeline),
        "endpoints": endpoints,
        "digests": {
            "timeline.json": digest(fixture / "timeline.json"),
            "relations.json": digest(fixture / "relations.json"),
        },
    }


if __name__ == "__main__":
    out = {}
    for name in sys.argv[1:]:
        out[name] = inventory(Path(name))
    print(json.dumps(out, indent=2, sort_keys=True))
