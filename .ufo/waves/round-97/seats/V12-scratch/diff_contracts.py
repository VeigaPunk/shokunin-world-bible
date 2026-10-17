#!/usr/bin/env python3
"""Structural leaf diff between two JSON contract snapshots (V12 seat scratch)."""
import json
import sys


def walk(a, b, path, out):
    if type(a) is not type(b):
        out.append((path, repr(a)[:160], repr(b)[:160]))
        return
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                out.append((f"{path}.{k}", "<absent>", repr(b[k])[:160]))
            elif k not in b:
                out.append((f"{path}.{k}", repr(a[k])[:160], "<absent>"))
            else:
                walk(a[k], b[k], f"{path}.{k}", out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((f"{path}[len]", str(len(a)), str(len(b))))
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", out)
    else:
        if a != b:
            out.append((path, repr(a)[:160], repr(b)[:160]))


def main():
    old = json.load(open(sys.argv[1]))
    new = json.load(open(sys.argv[2]))
    out = []
    walk(old, new, "", out)
    for path, before, after in out:
        print(f"{path}\n  before: {before}\n  after : {after}")
    print(f"TOTAL leaf diffs: {len(out)}")


if __name__ == "__main__":
    main()
