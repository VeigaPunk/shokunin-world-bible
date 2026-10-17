#!/usr/bin/env python3
"""V14 c3-inherited-equality: r97 vs POST-REPAIR r96 inheritance checks.

Checks:
  A. Parsed-value equality, KEY-ORDER SENSITIVE, inherited rows:
     entities.json (5/5), relations.json (1/1), timeline.json[:5],
     sources.json[:5], contradictions.json (all).
  B. Byte-prefix / byte-copy claims via cmp semantics (filecmp / bytes).
  C. r96 JSON tables byte-unchanged vs f3e09f9 (git diff, run outside).
"""
import json
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = ROOT / "corpus/fixtures/r96-crossing-response"
R97 = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"

fail = 0


def order_sensitive(o):
    """Canonical, key-order-preserving serialization (dupes impossible after json.load)."""
    return json.dumps(o, sort_keys=False, ensure_ascii=False, separators=(",", ":"))


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def row_keys(o):
    return list(o.keys()) if isinstance(o, dict) else None


print("== A. parsed-value equality (key-order sensitive) ==")
for name, n_inherit in [("entities.json", 5), ("relations.json", 1),
                        ("contradictions.json", None)]:
    a = load(R96 / name)
    b = load(R97 / name)
    print(f"-- {name}: r96 rows={len(a)} r97 rows={len(b)}")
    rows = range(len(a)) if n_inherit is None else range(min(n_inherit, len(a), len(b)))
    ok = True
    for i in rows:
        same = order_sensitive(a[i]) == order_sensitive(b[i])
        kord = row_keys(a[i]) == row_keys(b[i])
        if not (same and kord):
            ok = False
            fail += 1
            print(f"   row[{i}] MISMATCH same={same} key-order-same={kord}")
            print(f"     r96: {order_sensitive(a[i])}")
            print(f"     r97: {order_sensitive(b[i])}")
    print(f"   inherited rows compared: {len(list(rows))} -> {'IDENTICAL' if ok else 'MISMATCH'}")
    if len(b) > len(a):
        extra = b[len(a):]
        print(f"   NEW rows in r97 [{len(a)}:]: {order_sensitive(extra)}")

for name, n_inherit in [("timeline.json", 5), ("sources.json", 5)]:
    a = load(R96 / name)
    b = load(R97 / name)
    print(f"-- {name}: r96 rows={len(a)} r97 rows={len(b)}")
    ok = True
    for i in range(min(n_inherit, len(a), len(b))):
        same = order_sensitive(a[i]) == order_sensitive(b[i])
        kord = row_keys(a[i]) == row_keys(b[i])
        if not (same and kord):
            ok = False
            fail += 1
            print(f"   row[{i}] MISMATCH same={same} key-order-same={kord}")
            print(f"     r96: {order_sensitive(a[i])}")
            print(f"     r97: {order_sensitive(b[i])}")
    print(f"   inherited rows [:{n_inherit}] -> {'IDENTICAL' if ok else 'MISMATCH'}")
    if len(b) > len(a):
        print(f"   NEW rows in r97 [{len(a)}:]: {order_sensitive(b[len(a):])}")
    if len(b) < len(a):
        fail += 1
        print("   ERROR: r97 shorter than r96")

print()
print("== B. byte-copy claims (copied files) ==")
for name in ["entities.json", "relations.json", "contradictions.json",
             "inspiration-note.md", "source-excerpt.md"]:
    ba = (R96 / name).read_bytes()
    bb = (R97 / name).read_bytes()
    print(f"-- {name}: bytes r96={len(ba)} r97={len(bb)} identical={ba == bb}")

print()
print("== B2. byte-prefix probe for extended tables ==")
for name in ["timeline.json", "sources.json"]:
    ba = (R96 / name).read_bytes()
    bb = (R97 / name).read_bytes()
    # strip trailing whitespace + closing bracket from r96 to get the shared prefix
    core = ba.rstrip()
    assert core.endswith(b"]"), name
    core = core[:-1].rstrip()
    pref_ok = bb.startswith(core)
    print(f"-- {name}: r96 core len={len(core)}; r97 startswith(core)={pref_ok};"
          f" tail r96={core[-40:]!r} tail r97={bb[:len(core)+40][len(core)-40:]!r}")

print()
print(f"FAILURES: {fail}")
sys.exit(1 if fail else 0)
