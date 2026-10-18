#!/usr/bin/env python3
"""V53 byte-prefix-2 verification: r95 -> r96 crossing-response preservation."""
import hashlib, json, sys, os

L = "/home/vgpnk/Projects/shokunin/lore-shokunin"
R95 = os.path.join(L, "corpus/fixtures/r95-crossing-aftermath")
R96 = os.path.join(L, "corpus/fixtures/r96-crossing-response")

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

fails = []
print("== CHECK 1: byte-identical copied files (cmp) ==")
for name in ["entities.json", "relations.json", "contradictions.json",
             "inspiration-note.md", "source-excerpt.md"]:
    a, b = os.path.join(R95, name), os.path.join(R96, name)
    ha, hb = sha(a), sha(b)
    ba, bb = open(a, "rb").read(), open(b, "rb").read()
    same = ba == bb
    print(f"{name}: r95={ha[:16]} r96={hb[:16]} byte_equal={same} sizes={len(ba)}/{len(bb)}")
    if not same:
        fails.append(f"CHECK1 {name} NOT byte-identical")

print()
print("== CHECK 2: sources.json / timeline.json json-level diff ==")
for name in ["sources.json", "timeline.json"]:
    a, b = os.path.join(R95, name), os.path.join(R96, name)
    ja = json.load(open(a)); jb = json.load(open(b))
    print(f"{name}: r95 rows={len(ja)} r96 rows={len(jb)} delta={len(jb)-len(ja)}")
    if not isinstance(ja, list) or not isinstance(jb, list):
        fails.append(f"CHECK2 {name} not a JSON list")
        continue
    if len(jb) != len(ja) + 1:
        fails.append(f"CHECK2 {name} expected exactly 1 appended row, delta={len(jb)-len(ja)}")
    # shared prefix must be parsed-value identical
    prefix_ok = jb[:len(ja)] == ja
    print(f"  shared-prefix parsed-equal: {prefix_ok}")
    if not prefix_ok:
        # locate first mismatch
        for i, (x, y) in enumerate(zip(ja, jb)):
            if x != y:
                print(f"  first mismatch at index {i}:")
                print(f"    r95: {json.dumps(x, ensure_ascii=False)}")
                print(f"    r96: {json.dumps(y, ensure_ascii=False)}")
                break
        fails.append(f"CHECK2 {name} shared prefix NOT parsed-equal")
    for row in jb[len(ja):]:
        print(f"  appended row: {json.dumps(row, ensure_ascii=False)}")
    # supplementary: textual preservation of inherited rows (strip r95 closing bracket)
    ra = open(a, "rb").read()
    rb = open(b, "rb").read()
    stripped = ra.rstrip()
    if stripped.endswith(b"]"):
        stripped = stripped[:-1].rstrip()
    textual_prefix = rb.lstrip().startswith(stripped) if False else rb.startswith(stripped)
    print(f"  supplementary raw-text inherited-rows prefix (r95 minus closing ]): {textual_prefix}")
    # ids uniqueness
    ids = [r.get("id") for r in jb]
    print(f"  r96 ids: {ids}")
    if len(set(ids)) != len(ids):
        fails.append(f"CHECK2 {name} duplicate ids")

print()
print("== CHECK 3: fictional-excerpts.md strict byte-prefix + appended section ==")
a, b = os.path.join(R95, "fictional-excerpts.md"), os.path.join(R96, "fictional-excerpts.md")
ra, rb = open(a, "rb").read(), open(b, "rb").read()
print(f"r95 bytes={len(ra)} r96 bytes={len(rb)}")
is_prefix = rb.startswith(ra)
print(f"strict byte-prefix (rb.startswith(ra)): {is_prefix}")
if not is_prefix:
    # find first differing byte
    n = min(len(ra), len(rb))
    for i in range(n):
        if ra[i] != rb[i]:
            print(f"first differing byte at offset {i}: r95={ra[i]:#x} r96={rb[i]:#x}")
            print(f"  r95 context: {ra[max(0,i-60):i+60]!r}")
            print(f"  r96 context: {rb[max(0,i-60):i+60]!r}")
            break
    else:
        print("  r96 shorter than r95 (no differing byte within min length)")
    fails.append("CHECK3 fictional-excerpts.md NOT a strict byte-prefix")
else:
    appended = rb[len(ra):]
    print(f"appended bytes={len(appended)}")
    print("--- appended section verbatim ---")
    sys.stdout.write(appended.decode("utf-8"))
    print("--- end appended section ---")
    if len(appended) == 0:
        fails.append("CHECK3 no appended section")

print()
print("== SUMMARY ==")
if fails:
    for f in fails:
        print("FAIL:", f)
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
