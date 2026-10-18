#!/usr/bin/env python3
"""V46 scratch: relation census across corpus/fixtures/*/relations.json (rows, types)."""
import json
import os
import sys
from collections import Counter

root = sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures"
rows = 0
types = Counter()
files = 0
for d in sorted(os.listdir(root)):
    p = os.path.join(root, d, "relations.json")
    if not os.path.isfile(p):
        continue
    files += 1
    with open(p, encoding="utf-8") as fh:
        data = json.load(fh)
    for r in data:
        rows += 1
        types[r.get("type")] += 1
print(f"files={files} rows={rows} types={len(types)}")
for t, c in sorted(types.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"  {c} {t}")
