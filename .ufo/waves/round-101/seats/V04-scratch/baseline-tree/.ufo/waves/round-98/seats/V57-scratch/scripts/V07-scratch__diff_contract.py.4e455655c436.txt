#!/usr/bin/env python3
"""V07: deep-diff r98 contract vs baseline 9a3d648; classify every changed path."""
import json, sys

BASE = ".ufo/waves/round-98/seats/V07-scratch/contract-baseline-9a3d648.json"
CUR = "corpus/tools/dependency-freeze-contract.json"

base = json.load(open(BASE))
cur = json.load(open(CUR))

def walk(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            p = f"{path}.{k}" if path else k
            if k not in a:
                out.append(("ADDED", p))
            elif k not in b:
                out.append(("REMOVED", p))
            else:
                walk(a[k], b[k], p, out)
    elif isinstance(a, list) and isinstance(b, list):
        if a != b:
            out.append(("CHANGED", path))
    else:
        if a != b:
            out.append(("CHANGED", path))

out = []
walk(base, cur, "", out)
for kind, p in out:
    print(f"{kind} {p}")

print()
print("=== allowed-change classification ===")
allowed = []
unexpected = []
for kind, p in out:
    if kind == "ADDED" and (p.startswith("pins.r97-crossing-acknowledgment.") or p.startswith("pins.r98-clerk-filing.")):
        allowed.append((kind, p, "new pin"))
    elif kind == "ADDED" and p in ("pins.r97-crossing-acknowledgment", "pins.r98-clerk-filing"):
        allowed.append((kind, p, "new pin"))
    elif p.startswith("self_test.expected."):
        allowed.append((kind, p, "self-test expectation"))
    elif p == "precedence":
        allowed.append((kind, p, "precedence text"))
    elif p == "revision":
        allowed.append((kind, p, "top-level revision (freeze-mechanism side effect)"))
    else:
        unexpected.append((kind, p))
print("allowed:")
for kind, p, why in allowed:
    print(f"  {kind} {p}  [{why}]")
print("unexpected:")
for kind, p in unexpected:
    print(f"  {kind} {p}")

print()
print("=== r96 pin revision field ===")
b96 = base["pins"]["r96-crossing-response"]["revision"]
c96 = cur["pins"].get("r96-crossing-response", {}).get("revision")
print(f"baseline r96 revision: {b96}")
print(f"current  r96 revision: {c96}")
print(f"UNCHANGED: {b96 == c96}")

print()
print("=== existing pins deep-equality (r88, r94, r95, r96) ===")
for name in ("r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response"):
    same = base["pins"].get(name) == cur["pins"].get(name)
    print(f"{name}: byte-identical JSON value: {same}")

print()
print("=== new pins present ===")
for name in ("r97-crossing-acknowledgment", "r98-clerk-filing"):
    pin = cur["pins"].get(name)
    if pin is None:
        print(f"{name}: ABSENT")
    else:
        print(f"{name}: fixture={pin.get('fixture')} revision={pin.get('revision')} counts={pin.get('counts')}")
        print(f"  events={sorted(pin.get('events', {}).keys())}")

print()
print("=== self_test.expected key diff ===")
be = set(base["self_test"]["expected"])
ce = set(cur["self_test"]["expected"])
print(f"baseline {len(be)} cases, current {len(ce)} cases")
print(f"added: {sorted(ce - be)}")
print(f"removed: {sorted(be - ce)}")
for k in sorted(be & ce):
    if base["self_test"]["expected"][k] != cur["self_test"]["expected"][k]:
        print(f"MODIFIED {k}: {base['self_test']['expected'][k]} -> {cur['self_test']['expected'][k]}")

print()
print("=== precedence ===")
print(f"baseline: {base['precedence']!r}")
print(f"current : {cur['precedence']!r}")

print()
print("=== top-level revision ===")
print(f"baseline: {base['revision']}")
print(f"current : {cur['revision']}")
