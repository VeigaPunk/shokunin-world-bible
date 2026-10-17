#!/usr/bin/env python3
"""V18 scratch mutation harness for dependency_freeze gate probes.

Usage:
  mutate.py phantom  <dir> <event_id> <phantom_dep_id>
  mutate.py flip     <dir>
  mutate.py endpoint <dir> <old_id> <new_id>
  mutate.py delete   <dir> <event_id>
Mutations are applied in place to <dir> (always a scratch copy).
"""
import json
import sys
from pathlib import Path


def load(p):
    return json.loads(Path(p).read_text())


def save(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2) + "\n")


def phantom(d, event_id, dep_id):
    tp = Path(d) / "timeline.json"
    tl = load(tp)
    for ev in tl:
        if ev["id"] == event_id:
            if dep_id in ev["depends_on"]:
                raise SystemExit(f"dep already present: {dep_id}")
            ev["depends_on"] = sorted(ev["depends_on"] + [dep_id])
            save(tp, tl)
            print(f"MUTATED phantom: {event_id}.depends_on += {dep_id} -> {ev['depends_on']}")
            return
    raise SystemExit(f"event not found: {event_id}")


def flip(d):
    rp = Path(d) / "relations.json"
    rels = load(rp)
    if not rels:
        raise SystemExit("no relations to flip")
    for r in rels:
        r["from"], r["to"] = r["to"], r["from"]
    save(rp, rels)
    print(f"MUTATED flip: relations from/to swapped -> {rels}")


def endpoint(d, old_id, new_id):
    rp = Path(d) / "relations.json"
    rels = load(rp)
    hit = False
    for r in rels:
        for k in ("from", "to"):
            if r[k] == old_id:
                r[k] = new_id
                hit = True
    if not hit:
        raise SystemExit(f"endpoint {old_id} not found")
    save(rp, rels)
    print(f"MUTATED endpoint: {old_id} -> {new_id} in relations -> {rels}")


def delete(d, event_id):
    tp = Path(d) / "timeline.json"
    tl = load(tp)
    kept = [ev for ev in tl if ev["id"] != event_id]
    if len(kept) == len(tl):
        raise SystemExit(f"event not found: {event_id}")
    # also strip dangling edges pointing at the deleted event
    for ev in kept:
        ev["depends_on"] = [x for x in ev["depends_on"] if x != event_id]
    save(tp, kept)
    print(f"MUTATED delete: removed event {event_id} and dangling edges; remaining ids={[e['id'] for e in kept]}")


def reduce_edge(d, event_id, dep_id):
    tp = Path(d) / "timeline.json"
    tl = load(tp)
    for ev in tl:
        if ev["id"] == event_id:
            if dep_id not in ev["depends_on"]:
                raise SystemExit(f"dep not present: {dep_id} in {event_id}")
            ev["depends_on"] = [x for x in ev["depends_on"] if x != dep_id]
            save(tp, tl)
            print(f"MUTATED reduce: {event_id}.depends_on -= {dep_id} -> {ev['depends_on']}")
            return
    raise SystemExit(f"event not found: {event_id}")


def texttamper(d, event_id):
    """Change description text only: digests change, frozen inventory does not."""
    tp = Path(d) / "timeline.json"
    raw = tp.read_text()
    tl = json.loads(raw)
    for ev in tl:
        if ev["id"] == event_id:
            before = ev["description"]
            ev["description"] = before.replace("the", "The", 1) if "the" in before else before + " (tampered)"
            if ev["description"] == before:
                ev["description"] = before + " (tampered)"
            save(tp, tl)
            print(f"MUTATED texttamper: {event_id}.description -> {ev['description']!r}")
            return
    raise SystemExit(f"event not found: {event_id}")


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "phantom":
        phantom(sys.argv[2], sys.argv[3], sys.argv[4])
    elif m == "flip":
        flip(sys.argv[2])
    elif m == "endpoint":
        endpoint(sys.argv[2], sys.argv[3], sys.argv[4])
    elif m == "delete":
        delete(sys.argv[2], sys.argv[3])
    elif m == "reduce":
        reduce_edge(sys.argv[2], sys.argv[3], sys.argv[4])
    elif m == "texttamper":
        texttamper(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit(f"unknown mode {m}")
