#!/usr/bin/env python3
"""Report pin path scope from the delivered freeze contract. Read-only."""
import json
from pathlib import Path

p = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json")
data = json.loads(p.read_text())
print("top_keys", sorted(data.keys()) if isinstance(data, dict) else type(data).__name__)
print("schema_version", data.get("schema_version"))


def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(obj, str) and ("/" in obj or obj.endswith(".md") or obj.endswith(".json")):
        yield path, obj


outside = []
pins = data.get("pins") or data.get("fixtures") or data.get("chain")
print("pins_type", type(pins).__name__ if pins is not None else None)
if isinstance(pins, dict):
    print("pin_count", len(pins))
    for name, pin in pins.items():
        files = None
        if isinstance(pin, dict):
            files = pin.get("files") or pin.get("payload") or pin.get("digests")
        print("PIN", name, "keys", sorted(pin.keys()) if isinstance(pin, dict) else type(pin).__name__)
        if isinstance(files, dict):
            print("  file_count", len(files))
            for rel in files:
                ok = str(rel).startswith("corpus/fixtures/") or "/" not in str(rel)
                print("  FILE", rel, "OK" if ok else "OUTSIDE?")
                if str(rel).startswith("/") or ".." in str(rel) or not (
                    str(rel).startswith("corpus/fixtures/") or "/" not in str(rel)
                ):
                    outside.append((name, rel))
        elif isinstance(files, list):
            print("  file_count", len(files))
            for rel in files:
                print("  FILE", rel)
elif isinstance(pins, list):
    print("pin_count", len(pins))
    for pin in pins:
        if isinstance(pin, dict):
            print("PIN", pin.get("path") or pin.get("fixture") or pin.get("id"), "keys", sorted(pin.keys()))

print("OUTSIDE", outside)
