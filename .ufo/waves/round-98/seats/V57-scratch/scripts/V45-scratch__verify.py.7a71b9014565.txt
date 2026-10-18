#!/usr/bin/env python3
"""V45 byte-prefix-2 verification: r97 vs r98 fixture copies + appended rows + byte-prefix."""
import json, subprocess, sys, os

R97 = "corpus/fixtures/r97-crossing-acknowledgment"
R98 = "corpus/fixtures/r98-clerk-filing"

def sh(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

print("== 1. cmp: pure copied files (r97 vs r98) ==")
pure = ["contradictions.json", "inspiration-note.md", "relations.json", "source-excerpt.md"]
pure_ok = True
for f in pure:
    rc, out, err = sh(f"cmp {R97}/{f} {R98}/{f}")
    ok = rc == 0
    pure_ok &= ok
    print(f"  {'IDENTICAL' if ok else 'DIFFER   '}  {f}  (cmp rc={rc}) {err.strip()}")

print("\n== 2. json-level diff: r97 rows preserved as exact prefix, extras appended ==")
json_ok = True
for f in ["entities.json", "sources.json", "timeline.json"]:
    a = json.load(open(f"{R97}/{f}"))
    b = json.load(open(f"{R98}/{f}"))
    la, lb = len(a), len(b)
    prefix_ok = (lb >= la) and (b[:la] == a)
    extras = b[la:] if lb >= la else []
    ids_new = [r.get("id") for r in extras]
    json_ok &= prefix_ok
    print(f"  {f}: r97={la} r98={lb} prefix-exact={prefix_ok} appended={ids_new}")
    for r in extras:
        print(f"     + {json.dumps(r, ensure_ascii=False)}")

print("\n== 3. fictional-excerpts.md strict byte-prefix ==")
b97 = open(f"{R97}/fictional-excerpts.md", "rb").read()
b98 = open(f"{R98}/fictional-excerpts.md", "rb").read()
prefix = b98.startswith(b97)
print(f"  r97={len(b97)}B r98={len(b98)}B strict-prefix={prefix} appended={len(b98)-len(b97)}B")
if not prefix:
    # find first divergence
    n = min(len(b97), len(b98))
    d = next((i for i in range(n) if b97[i] != b98[i]), n)
    print(f"  FIRST DIVERGENCE at byte {d}: r97={b97[d:d+40]!r} r98={b98[d:d+40]!r}")
else:
    print(f"  appended tail repr: {b98[len(b97):][:400]!r}")

print("\n== 4. informational: r98-authored files (README.md, claim-excerpt-map.md) ==")
for f in ["README.md", "claim-excerpt-map.md"]:
    p = os.path.exists(f"{R98}/{f}")
    if not p:
        print(f"  {f}: ABSENT"); continue
    rc, _, _ = sh(f"cmp -s {R97}/{f} {R98}/{f}")
    b97f = open(f"{R97}/{f}", "rb").read(); b98f = open(f"{R98}/{f}", "rb").read()
    print(f"  {f}: r97={len(b97f)}B r98={len(b98f)}B identical={rc==0} r97-is-prefix={b98f.startswith(b97f)}")

print("\n== SUMMARY ==")
print(f"pure-copies identical: {pure_ok}")
print(f"json prefix-exact:     {json_ok}")
print(f"fictional byte-prefix: {prefix}")
