#!/usr/bin/env python3
"""V49 contract-diff audit: for each corpus/tools/*contract*.json that differs from
f3e09f9, show whether the change is purely additive (no existing key removed or
value changed). Exit 1 if any pre-existing case/value is modified or removed."""
import json
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "f3e09f9"
CONTRACTS = [
    "corpus/tools/boundary-doc-contract.json",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/map-obligations-contract.json",
]


def run(*a):
    return subprocess.run(a, cwd=REPO, capture_output=True, text=True)


def base_text(p):
    return run("git", "show", f"{BASE}:{p}").stdout


def walk(old, new, path="$", out=None):
    if out is None:
        out = []
    if type(old) is not type(new):
        out.append(f"TYPE-CHANGE {path}: {type(old).__name__} -> {type(new).__name__}")
        return out
    if isinstance(old, dict):
        for k in old:
            if k not in new:
                out.append(f"REMOVED-KEY {path}.{k}")
            else:
                walk(old[k], new[k], f"{path}.{k}", out)
        for k in new:
            if k not in old:
                out.append(f"ADDED-KEY {path}.{k}")
    elif isinstance(old, list):
        if len(new) < len(old):
            out.append(f"LIST-SHRUNK {path}: {len(old)} -> {len(new)}")
        for i in range(min(len(old), len(new))):
            walk(old[i], new[i], f"{path}[{i}]", out)
        for i in range(len(old), len(new)):
            out.append(f"APPENDED {path}[{i}]")
    elif old != new:
        out.append(f"VALUE-CHANGE {path}: {old!r} -> {new!r}")
    return out


def main():
    rc = 0
    for p in CONTRACTS:
        old = json.loads(base_text(p))
        try:
            new = json.loads(open(f"{REPO}/{p}", encoding="utf-8").read())
        except OSError as e:
            print(f"## {p}: unreadable ({e})")
            rc = 1
            continue
        if old == new:
            print(f"## {p}: BYTE-SEMANTIC IDENTICAL to {BASE}")
            continue
        deltas = walk(old, new)
        bad = [d for d in deltas if not d.startswith(("ADDED-KEY", "APPENDED"))]
        print(f"## {p}: {len(deltas)} deltas, {len(bad)} non-additive")
        for d in deltas:
            print(f"   {d}")
        if bad:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
