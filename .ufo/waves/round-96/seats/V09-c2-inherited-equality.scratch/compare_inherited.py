#!/usr/bin/env python3
"""V09 c2-inherited-equality: key-order-sensitive parsed-value equality of
inherited r96 rows against their r95 originals."""
import json
import sys

R95 = sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures/r95-crossing-aftermath"
R96 = sys.argv[2] if len(sys.argv) > 2 else "corpus/fixtures/r96-crossing-response"

failures = []
notes = []


def load_ordered(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=lambda pairs: list(pairs))


def ordered(obj):
    """Render parsed value as an order-preserving canonical text."""
    if isinstance(obj, list) and obj and all(isinstance(p, list) and len(p) == 2 for p in obj):
        # object_pairs_hook produced a pair-list; could also be a real JSON array
        # of 2-element arrays. Distinguish: object pairs are (str, value).
        if all(isinstance(p[0], str) for p in obj):
            return "{" + ", ".join("%s:%s" % (json.dumps(k), ordered(v)) for k, v in obj) + "}"
    if isinstance(obj, list):
        return "[" + ", ".join(ordered(v) for v in obj) + "]"
    return json.dumps(obj)


def cmp_value(label, a, b):
    """a = r95 row, b = r96 row. Returns True if key-order-sensitively equal."""
    oa, ob = ordered(a), ordered(b)
    plain = a == b  # python dict equality: key-order INSENSITIVE
    same = oa == ob
    if same:
        notes.append("%-46s ORDER-SENSITIVE EQUAL (plain==: %s)" % (label, plain))
    else:
        # Is it equal ignoring key order? If yes, that's an order-only drift.
        detail = "ORDER-SENSITIVE DIFF"
        if plain:
            detail += " but order-INSENSITIVE equal -> key-order-only drift"
            # locate first divergence for evidence
            for i, (ca, cb) in enumerate(zip(oa, ob)):
                if ca != cb:
                    detail += "; first divergence at char %d: r95 %r vs r96 %r" % (i, oa[i:i + 120], ob[i:i + 120])
                    break
        else:
            detail += " and value differs"
            for i, (ca, cb) in enumerate(zip(oa, ob)):
                if ca != cb:
                    detail += "; first divergence at char %d: r95 %r vs r96 %r" % (i, oa[i:i + 160], ob[i:i + 160])
                    break
        failures.append("%s: %s" % (label, detail))
        notes.append("%-46s %s" % (label, detail))
    return same


def pair_rows(kind, key):
    a = load_ordered("%s/%s.json" % (R95, kind))
    b = load_ordered("%s/%s.json" % (R96, kind))
    a = [dict(r) for r in a]
    b = [dict(r) for r in b]
    print("== %s: r95 n=%d r96 n=%d" % (kind, len(a), len(b)))
    for i, row in enumerate(a):
        k = row.get(key)
        match = [r for r in b if r.get(key) == k]
        if not match:
            failures.append("%s[%s=%s]: MISSING in r96" % (kind, key, k))
            notes.append("%-46s MISSING in r96" % ("%s[%s=%s]" % (kind, key, k)))
            continue
        if len(match) > 1:
            failures.append("%s[%s=%s]: %d rows in r96 (duplicate key)" % (kind, key, k, len(match)))
        cmp_value("%s[%s=%s]" % (kind, key, k), row, match[0])
    return a, b


def report_order(kind, key, a, b):
    """Check inherited rows occupy the same indices (appended-new-row claim)."""
    ai = [r.get(key) for r in a]
    bi = [r.get(key) for r in b]
    if bi[:len(ai)] == ai:
        notes.append("%-46s inherited rows are an exact index-prefix (new rows appended)" % (kind + " order"))
    else:
        notes.append("%-46s ORDER CHANGED: r95 %s -> r96 %s" % (kind + " order", ai, bi))


print("### r95:", R95)
print("### r96:", R96)

e_a, e_b = pair_rows("entities", "id")
r_a, r_b = pair_rows("relations", "from")
t_a, t_b = pair_rows("timeline", "id")
s_a, s_b = pair_rows("sources", "id")
c_a, c_b = pair_rows("contradictions", "id")

report_order("entities", "id", e_a, e_b)
report_order("relations", "from", r_a, r_b)
report_order("timeline", "id", t_a, t_b)
report_order("sources", "id", s_a, s_b)

print()
print("== timeline prefix (brief says timeline[:4] inherited) ==")
if len(t_b) >= len(t_a):
    for i in range(len(t_a)):
        cmp_value("timeline[%d] %s" % (i, t_a[i].get("id")), t_a[i], t_b[i])
    print("r96 tail rows:", [x.get("id") for x in t_b[len(t_a):]])
else:
    failures.append("timeline: r96 shorter than r95 (%d < %d)" % (len(t_b), len(t_a)))

print("== sources prefix (brief says sources[:4] inherited) ==")
if len(s_b) >= len(s_a):
    for i in range(len(s_a)):
        cmp_value("sources[%d] %s" % (i, s_a[i].get("id")), s_a[i], s_b[i])
    print("r96 tail rows:", [x.get("id") for x in s_b[len(s_a):]])
else:
    failures.append("sources: r96 shorter than r95 (%d < %d)" % (len(s_b), len(s_a)))

print()
print("== NOTES ==")
for n in notes:
    print(" ", n)
print()
print("== FAILURES: %d ==" % len(failures))
for f in failures:
    print(" FAIL", f)
print()
print("VERDICT:", "PASS" if not failures else "FAIL")
sys.exit(0 if not failures else 1)
