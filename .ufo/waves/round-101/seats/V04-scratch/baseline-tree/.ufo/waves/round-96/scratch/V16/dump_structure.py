#!/usr/bin/env python3
"""V16 contract shape dumper: prints the structure of the Q3 contract JSON
so the comparator can be written against the real shape."""
import json
import sys

path = sys.argv[1]
obj = json.load(open(path))


def walk(node, prefix="", depth=0):
    if depth > 6:
        print(f"{prefix} ... (depth cap)")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            t = type(v).__name__
            if isinstance(v, (dict, list)):
                print(f"{prefix}{k}: {t}[{len(v)}]")
                walk(v, prefix + "  ", depth + 1)
            else:
                s = repr(v)
                if len(s) > 120:
                    s = s[:117] + "..."
                print(f"{prefix}{k}: {t} = {s}")
    elif isinstance(node, list):
        for i, v in enumerate(node[:4]):
            if isinstance(v, (dict, list)):
                print(f"{prefix}[{i}]: {type(v).__name__}[{len(v)}]")
                walk(v, prefix + "  ", depth + 1)
            else:
                s = repr(v)
                if len(s) > 120:
                    s = s[:117] + "..."
                print(f"{prefix}[{i}]: {type(v).__name__} = {s}")
        if len(node) > 4:
            print(f"{prefix}... {len(node) - 4} more list items")


walk(obj)
