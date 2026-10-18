#!/usr/bin/env python3
"""V16 independent recomputation of dependency edges + digests from RAW fixture JSON.

No import of dependency_freeze.py. Pure stdlib read of corpus/fixtures/<dir>/timeline.json
and relations.json.
"""
import hashlib
import json
import os
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
CHAIN = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath",
         "r96-crossing-response"]


def raw_sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def canonical_sha256(obj):
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def recompute(fixture):
    d = os.path.join(ROOT, "corpus", "fixtures", fixture)
    tl_path = os.path.join(d, "timeline.json")
    rel_path = os.path.join(d, "relations.json")
    out = {"fixture": fixture, "dir": d}
    tl = json.load(open(tl_path))
    rel = json.load(open(rel_path))
    edges = {ev["id"]: sorted(ev.get("depends_on", [])) for ev in tl}
    out["edge_count"] = sum(len(v) for v in edges.values())
    out["edges"] = edges
    out["event_ids"] = sorted(edges)
    out["relations"] = sorted(
        [{"from": r["from"], "to": r["to"], "type": r["type"]} for r in rel],
        key=lambda r: (r["from"], r["to"], r["type"]),
    )
    out["digests"] = {
        "timeline_raw_sha256": raw_sha256(tl_path),
        "relations_raw_sha256": raw_sha256(rel_path),
        "timeline_canonical_sha256": canonical_sha256(tl),
        "relations_canonical_sha256": canonical_sha256(rel),
        "timeline_bytes": os.path.getsize(tl_path),
        "relations_bytes": os.path.getsize(rel_path),
    }
    return out


if __name__ == "__main__":
    results = {}
    for fx in CHAIN:
        try:
            results[fx] = recompute(fx)
        except Exception as exc:  # noqa: BLE001
            results[fx] = {"fixture": fx, "error": f"{type(exc).__name__}: {exc}"}
    print(json.dumps(results, indent=2, sort_keys=True))
