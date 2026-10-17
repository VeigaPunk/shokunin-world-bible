#!/usr/bin/env python3
"""V16 c3-anchors supplementary: resolve every map row's JSON pointer in the fixture.

For each J row in the map, extract the first backticked `*.json#/...` token,
resolve it against the fixture JSON files, and print OK/FAIL + a short value
preview. Exit 0 iff all 17 pointers resolve.
"""
import json
import re
import sys
from pathlib import Path

FIX = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("corpus/fixtures/r97-crossing-acknowledgment")
MAP = FIX / "claim-excerpt-map.md"

PTR = re.compile(r"`([\w.-]+\.json#/[^`]*)`")
ROW = re.compile(r"^\|\s*([JS]\d{2})\s*\|")


def resolve(doc, pointer):
    cur = doc
    for part in pointer.strip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


fails = []
rows = 0
for line in MAP.read_text(encoding="utf-8").splitlines():
    m = ROW.match(line)
    if not m:
        continue
    rows += 1
    rid = m.group(1)
    pm = PTR.search(line)
    if not pm:
        if rid.startswith("J"):
            fails.append(f"{rid}: no json pointer found")
            print(f"{rid}  NO-POINTER  (FAIL: J row must carry a pointer)")
        else:
            print(f"{rid}  no json pointer (editorial row, expected)")
        continue
    token = pm.group(1)
    fname, ptr = token.split("#", 1)
    p = FIX / fname
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
        val = resolve(doc, ptr)
        preview = json.dumps(val, ensure_ascii=False)
        print(f"{rid}  {token}  OK  {preview[:110]}")
    except Exception as exc:  # noqa: BLE001
        fails.append(f"{rid}: {token} failed: {exc}")
        print(f"{rid}  {token}  FAIL  {exc}")

print(f"rows={rows} pointer-failures={len(fails)}")
print("RESULT:", "ALL-POINTERS-RESOLVE" if not fails else "POINTER-FAILURES")
sys.exit(0 if not fails else 1)
