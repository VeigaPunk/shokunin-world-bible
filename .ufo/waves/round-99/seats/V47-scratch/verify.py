#!/usr/bin/env python3
"""V47 byte-prefix-2: r98 vs r99 copied files, JSON append, fictional-excerpts prefix."""
import hashlib
import json
import os
import subprocess

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
R98 = os.path.join(LANE, "corpus/fixtures/r98-clerk-filing")
R99 = os.path.join(LANE, "corpus/fixtures/r99-window-lapse")
BASE = "4265df5e86e4121bde4125b649b89bb1676676a5"
ALL = [
    "contradictions.json",
    "entities.json",
    "relations.json",
    "sources.json",
    "timeline.json",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
    "README.md",
    "claim-excerpt-map.md",
]
PURE = [
    "contradictions.json",
    "entities.json",
    "inspiration-note.md",
    "relations.json",
    "source-excerpt.md",
]
JSONS = ["entities.json", "sources.json", "timeline.json", "relations.json", "contradictions.json"]


def git_show(path):
    p = subprocess.run(
        ["git", "-C", LANE, "show", f"{BASE}:{path}"],
        capture_output=True,
    )
    if p.returncode != 0:
        raise SystemExit(f"git show failed {path}: {p.stderr.decode()[:400]}")
    return p.stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


print("== 0. baseline identity: working-tree r98 vs 4265df5 ==")
r98_clean = True
for f in ALL:
    wt = open(os.path.join(R98, f), "rb").read()
    blob = git_show(f"corpus/fixtures/r98-clerk-filing/{f}")
    ok = wt == blob
    r98_clean &= ok
    print(f"  {'MATCH' if ok else 'DIFF '} r98-wt vs 4265df5 {f} wt={len(wt)} blob={len(blob)}")

print("\n== 1. cmp: pure copied files r98 vs r99 and vs 4265df5 ==")
pure_ok = True
for f in PURE:
    a = open(os.path.join(R98, f), "rb").read()
    b = open(os.path.join(R99, f), "rb").read()
    blob = git_show(f"corpus/fixtures/r98-clerk-filing/{f}")
    ok = a == b == blob
    pure_ok &= ok
    rc = subprocess.run(["cmp", os.path.join(R98, f), os.path.join(R99, f)]).returncode
    print(f"  {'IDENTICAL' if ok else 'DIFFER   '} {f} cmp_rc={rc} r98={len(a)} r99={len(b)} vs4265={b==blob}")

print("\n== 2. JSON-level diff: inherited rows exact prefix, extras appended ==")
json_ok = True
for f in JSONS:
    a = json.loads(open(os.path.join(R98, f), encoding="utf-8").read())
    b = json.loads(open(os.path.join(R99, f), encoding="utf-8").read())
    la, lb = len(a), len(b)
    prefix_ok = lb >= la and b[:la] == a
    extras = b[la:] if lb >= la else []
    ids = [r.get("id") for r in extras] if extras and isinstance(extras[0], dict) else extras
    json_ok &= prefix_ok and (lb == la or lb == la + 1)
    print(f"  {f}: r98={la} r99={lb} prefix-exact={prefix_ok} appended={ids}")
    for r in extras:
        print("    +", json.dumps(r, ensure_ascii=False))

print("\n== 2b. raw append junction (r98 bytes up to '\\n]' preserved; r99 inserts ',\\n  {') ==")
junction_ok = True
for f in ["sources.json", "timeline.json", "entities.json", "relations.json", "contradictions.json"]:
    b98 = open(os.path.join(R98, f), "rb").read()
    b99 = open(os.path.join(R99, f), "rb").read()
    idx = b98.rfind(b"\n]")
    shared = idx >= 0 and b99.startswith(b98[:idx])
    junction_ok &= shared or b98 == b99
    nxt = b99[idx:idx + 48] if idx >= 0 else b""
    print(f"  {f}: r98={len(b98)} r99={len(b99)} shared-to-\\n]={shared} r99-at-junction={nxt!r}")

print("\n== 3. fictional-excerpts.md strict byte-prefix ==")
b98 = open(os.path.join(R98, "fictional-excerpts.md"), "rb").read()
b99 = open(os.path.join(R99, "fictional-excerpts.md"), "rb").read()
blob = git_show("corpus/fixtures/r98-clerk-filing/fictional-excerpts.md")
prefix = b99.startswith(b98) and b98 == blob
print(f"  r98={len(b98)} r99={len(b99)} strict-prefix={b99.startswith(b98)} r98==4265df5={b98==blob} appended={len(b99)-len(b98)}")
if b99.startswith(b98):
    tail = b99[len(b98):]
    print("  appended head:", tail[:500])
    print("  both end with newline:", b98.endswith(b"\n"), b99.endswith(b"\n"))
    print("  r99 lines", b99.count(b"\n"), "r98 lines", b98.count(b"\n"))
else:
    n = min(len(b98), len(b99))
    d = next((i for i in range(n) if b98[i] != b99[i]), n)
    print(f"  FIRST DIVERGENCE byte {d}: r98={b98[d:d+40]!r} r99={b99[d:d+40]!r}")

print("\n== 4. informational: README + claim-excerpt-map (S4-owned, not copies) ==")
for f in ["README.md", "claim-excerpt-map.md"]:
    a = open(os.path.join(R98, f), "rb").read()
    b = open(os.path.join(R99, f), "rb").read()
    print(
        f"  {f}: r98={len(a)} r99={len(b)} identical={a==b} r98-is-prefix={b.startswith(a)} "
        f"r99-sha={sha(b)[:16]}"
    )

print("\n== 5. referential integrity of appended rows ==")
src = json.loads(open(os.path.join(R99, "sources.json"), encoding="utf-8").read())
tl = json.loads(open(os.path.join(R99, "timeline.json"), encoding="utf-8").read())
ent = json.loads(open(os.path.join(R99, "entities.json"), encoding="utf-8").read())
rel = json.loads(open(os.path.join(R99, "relations.json"), encoding="utf-8").read())
con = json.loads(open(os.path.join(R99, "contradictions.json"), encoding="utf-8").read())
src_ids = {r["id"] for r in src}
ent_ids = {r["id"] for r in ent}
tl_ids = {r["id"] for r in tl}
places = {r["id"] for r in ent if r.get("kind") == "place"} | {r.get("id") for r in ent}
new_src = src[-1]
new_ev = tl[-1]
print("counts", "entities", len(ent), "relations", len(rel), "sources", len(src), "events", len(tl), "contradictions", len(con))
print("ticks", [r["tick"] for r in tl])
print("new source id resolves in timeline", new_ev.get("source_id") in src_ids, new_ev.get("source_id"))
print("new event entity resolves", new_ev.get("entity_id") in ent_ids, new_ev.get("entity_id"))
print("new event place in entity ids", new_ev.get("place_id") in ent_ids, new_ev.get("place_id"))
deps = new_ev.get("depends_on")
print("depends_on", deps, "all resolve", all(d in tl_ids for d in deps) if isinstance(deps, list) else False)
print("new source id", new_src.get("id"), "new event id", new_ev.get("id"), "tick", new_ev.get("tick"))

print("\n== SUMMARY ==")
print("r98 working tree == 4265df5:", r98_clean)
print("pure copies identical:", pure_ok)
print("json prefix-exact:", json_ok)
print("raw junction ok:", junction_ok)
print("fictional strict prefix:", prefix)
