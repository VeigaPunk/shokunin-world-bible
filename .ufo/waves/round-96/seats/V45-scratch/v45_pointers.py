#!/usr/bin/env python3
"""V45 pointer cross-check: resolve every JSON-fact row's pointer directly and
confirm the bound source_id equals the row's declared in-world source ID."""
import json
import re
import sys
from pathlib import Path

MAP = Path(sys.argv[1])
base = MAP.resolve().parent


def parse_rows(path):
    rows = {}
    for line in Path(path).read_text().split("\n"):
        m = re.match(r"^\s*\|(.+)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if re.fullmatch(r"J\d+", cells[0]) and len(cells) == 8:
            rows[cells[0]] = {
                "pointer": re.search(r"`([^`]*)`", cells[1]).group(1),
                "source": cells[2].strip("`"),
                "ns": cells[3].strip("`"),
            }
    return rows


def resolve(doc, parts):
    cur = doc
    for p in parts:
        if isinstance(cur, list):
            cur = cur[int(p)]
        else:
            cur = cur[p]
    return cur


def bound_source(pointer, value):
    parts = pointer.split("#/")[1].split("/")
    leaf = parts[-1]
    if leaf == "first_appearance":
        return value if isinstance(value, str) else None
    if isinstance(value, dict):
        return value.get("source_id")
    return None


rows = parse_rows(MAP)
cache = {}
bad = []
for rid in sorted(rows):
    r = rows[rid]
    fn, ptr = r["pointer"].split("#/")
    if fn not in cache:
        cache[fn] = json.loads((base / fn).read_text())
    try:
        val = resolve(cache[fn], ptr.split("/"))
    except Exception as e:  # noqa: BLE001
        bad.append((rid, f"UNRESOLVED {r['pointer']}: {e}"))
        print(f"  {rid} {r['pointer']}: UNRESOLVED ({e})")
        continue
    src = bound_source(r["pointer"], val)
    ok = src == r["source"]
    ns_ok = r["ns"] == f"r96-crossing-response:{r['source']}"
    if not ok:
        bad.append((rid, f"source bound {src!r} != row {r['source']!r}"))
    print(f"  {rid} {r['pointer']}: exists, source_id={src!r} row={r['source']!r} "
          f"match={ok} ns={r['ns']} ns-ok={ns_ok}")
print(f"POINTER CHECK: {len(rows) - len(bad)}/{len(rows)} rows resolve and bind; bad={bad}")
sys.exit(1 if bad else 0)
