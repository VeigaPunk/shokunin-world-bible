#!/usr/bin/env python3
"""Control: prove the V09 comparator is key-order sensitive and value sensitive.

Imports ordered() from compare_inherited.py and mutates in-memory copies.
A comparator that cannot fail is not evidence.
"""
import importlib.util
import json
import sys

spec = importlib.util.spec_from_file_location(
    "ci", "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/"
          "V09-c2-inherited-equality.scratch/compare_inherited.py")
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)   # executes the real comparison as a side effect
except SystemExit:
    pass

ordered = mod.ordered

base = json.loads('{"id":"evin","kind":"character","name":"Evin","first_appearance":"paired-clock"}')
reordered = json.loads('{"kind":"character","id":"evin","name":"Evin","first_appearance":"paired-clock"}')
value_changed = json.loads('{"id":"evin","kind":"character","name":"Evan","first_appearance":"paired-clock"}')
extra_key = json.loads('{"id":"evin","kind":"character","name":"Evin","first_appearance":"paired-clock","extra":1}')
dropped_key = json.loads('{"id":"evin","kind":"character","name":"Evin"}')
nested_reordered = json.loads(
    '[{"id":"evin","claims":[{"source_id":"paired-clock","statement":"x"}]}]')
nested_ok = json.loads(
    '[{"id":"evin","claims":[{"statement":"x","source_id":"paired-clock"}]}]')

cases = [
    ("identical", ordered(base), ordered(json.loads(json.dumps(base))), True),
    ("key-order-only change", ordered(base), ordered(reordered), False),
    ("value change", ordered(base), ordered(value_changed), False),
    ("extra key", ordered(base), ordered(extra_key), False),
    ("dropped key", ordered(base), ordered(dropped_key), False),
    ("nested key-order change", ordered(nested_ok), ordered(nested_reordered), False),
]

fails = 0
for label, a, b, expect_equal in cases:
    got_equal = (a == b)
    ok = (got_equal == expect_equal)
    fails += (not ok)
    print("%-24s detected-as-equal=%-5s expected=%-5s %s" % (
        label, got_equal, expect_equal, "OK" if ok else "CONTROL FAILURE"))
    if not got_equal:
        for i, (ca, cb) in enumerate(zip(a, b)):
            if ca != cb:
                print("      divergence@%d: %r vs %r" % (i, a[i:i + 90], b[i:i + 90]))
                break

print("CONTROL:", "PASS" if fails == 0 else "FAIL (%d)" % fails)
sys.exit(0 if fails == 0 else 1)
