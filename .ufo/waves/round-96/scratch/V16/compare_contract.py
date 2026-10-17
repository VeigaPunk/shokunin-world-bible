#!/usr/bin/env python3
"""V16 comparator: contract pins vs V16 independent recomputation (raw JSON).

Generic: locates each chain fixture's node inside the contract JSON, extracts
- an edges mapping (event_id -> list[str]) by shape,
- relation endpoint records by shape,
- any sha256 hex digests by shape,
then compares one-to-one against .ufo/waves/round-96/scratch/V16/independent.json.

Usage: python3 compare_contract.py <contract.json>
"""
import json
import os
import re
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SCRATCH = os.path.join(ROOT, ".ufo/waves/round-96/scratch/V16")
CHAIN = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath",
         "r96-crossing-response"]
HEX64 = re.compile(r"^[0-9a-f]{64}$")

indep = json.load(open(os.path.join(SCRATCH, "independent.json")))
contract = json.load(open(sys.argv[1]))


def find_fixture_nodes(node, name, path=""):
    """Yield (path, node) for every dict/list node that mentions the fixture name."""
    hits = []
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str) and k == name:
                hits.append((f"{path}/{k}", v))
            hits.extend(find_fixture_nodes(v, name, f"{path}/{k}"))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            hits.extend(find_fixture_nodes(v, name, f"{path}[{i}]"))
    return hits


def collect_edges(node):
    """Find dicts mapping event-id-looking keys to lists of strings."""
    found = []
    if isinstance(node, dict):
        if node and all(isinstance(v, list) and all(isinstance(x, str) for x in v)
                        for v in node.values()) and any("-" in k for k in node):
            found.append(node)
        for v in node.values():
            found.extend(collect_edges(v))
    elif isinstance(node, list):
        for v in node:
            found.extend(collect_edges(v))
    return found


def collect_hex(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and HEX64.match(v):
                out.append((k, v))
            else:
                collect_hex(v, out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            if isinstance(v, str) and HEX64.match(v):
                out.append((f"[{i}]", v))
            else:
                collect_hex(v, out)
    return out


print("=" * 72)
print("CONTRACT TOP-LEVEL KEYS:", list(contract) if isinstance(contract, dict) else type(contract).__name__)
print("=" * 72)

overall_ok = True
for fx in CHAIN:
    mine = indep.get(fx, {})
    print(f"\n### {fx}")
    nodes = find_fixture_nodes(contract, fx)
    if not nodes:
        print("  NO CONTRACT NODE MENTIONING THIS FIXTURE NAME")
        overall_ok = False
        continue
    print(f"  contract paths: {[p for p, _ in nodes]}")
    my_edges = {k: sorted(v) for k, v in mine.get("edges", {}).items()}
    my_edge_pairs = sorted((k, tuple(v)) for k, v in my_edges.items())
    matched = False
    for path, node in nodes:
        cands = collect_edges(node)
        for cand in cands:
            c_edges = {k: sorted(v) for k, v in cand.items()}
            c_pairs = sorted((k, tuple(v)) for k, v in c_edges.items())
            if c_pairs == my_edge_pairs:
                print(f"  EDGES MATCH at {path} ({len(c_edges)} events, "
                      f"{sum(len(v) for v in c_edges.values())} edges)")
                matched = True
            elif set(c_edges) & set(my_edges):
                print(f"  EDGES MISMATCH at {path}:")
                for k in sorted(set(c_edges) | set(my_edges)):
                    a, b = my_edges.get(k), c_edges.get(k)
                    if a != b:
                        print(f"    {k}: independent={a} contract={b}")
                overall_ok = False
    if not matched:
        overall_ok = False
    # digests
    hexes = []
    for path, node in nodes:
        collect_hex(node, hexes)
    mydig = mine.get("digests", {})
    mine_vals = {v: k for k, v in mydig.items()}
    print(f"  contract digests found: {len(hexes)}")
    for k, v in hexes:
        where = mine_vals.get(v)
        print(f"    {k}: {v[:16]}… -> {'MATCHES independent ' + where if where else 'NO MATCH in independent digests'}")
        if not where:
            overall_ok = False

print("\n" + "=" * 72)
print("OVERALL:", "ALL PINS MATCH INDEPENDENT RECOMPUTE" if overall_ok else "DISCREPANCIES PRESENT")
