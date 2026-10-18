#!/usr/bin/env python3
"""V51 independent depth checks for r99-window-lapse vs r98-clerk-filing.

Read-only. Prints PASS/FAIL lines. Exit 0 iff no FAIL.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R98 = ROOT / "corpus/fixtures/r98-clerk-filing"
R99 = ROOT / "corpus/fixtures/r99-window-lapse"
fails = []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ok(cond: bool, msg: str) -> None:
    tag = "OK" if cond else "FAIL"
    print(f"{tag} {msg}")
    if not cond:
        fails.append(msg)


def load(p: Path):
    return json.loads(p.read_text())


print(f"r98={R98} r99={R99}")
print(f"r99 exists={R99.is_dir()} files={sorted(x.name for x in R99.iterdir()) if R99.is_dir() else None}")

byte_same = [
    "contradictions.json",
    "entities.json",
    "inspiration-note.md",
    "relations.json",
    "source-excerpt.md",
]
for name in byte_same:
    a, b = R98 / name, R99 / name
    same = a.read_bytes() == b.read_bytes()
    ok(same, f"byte-identical {name} | r98={sha(a)[:16]} r99={sha(b)[:16]}")

e98, e99 = load(R98 / "entities.json"), load(R99 / "entities.json")
s98, s99 = load(R98 / "sources.json"), load(R99 / "sources.json")
t98, t99 = load(R98 / "timeline.json"), load(R99 / "timeline.json")
r98, r99 = load(R98 / "relations.json"), load(R99 / "relations.json")
c98, c99 = load(R98 / "contradictions.json"), load(R99 / "contradictions.json")

ok(len(e98) == 6 and len(e99) == 6, f"entities 6->6 | {len(e98)}->{len(e99)}")
ok(len(r98) == 1 and len(r99) == 1, f"relations 1 | {len(r98)}|{len(r99)}")
ok(len(t98) == 7 and len(t99) == 8, f"timeline 7->8 | {len(t98)}->{len(t99)}")
ok(len(s98) == 7 and len(s99) == 8, f"sources 7->8 | {len(s98)}->{len(s99)}")
ok(c98 == [] and c99 == [], f"contradictions [] | {c98}|{c99}")
ok(e99 == e98, "entities parsed-equal")
ok(r99 == r98, "relations parsed-equal")
ok(s99[:-1] == s98, "sources[:7] parsed-equal")
ok(t99[:-1] == t98, "timeline[:7] parsed-equal")

claims98 = sum(len(e.get("claims") or []) for e in e98)
claims99 = sum(len(e.get("claims") or []) for e in e99)
ok(claims98 == claims99 == 6, f"claims 6 | {claims98}|{claims99}")

new_src = s99[-1]
ok(
    new_src.get("id") == "clerk-lapse-note"
    and "Lapse" in new_src.get("title", "")
    and new_src.get("kind") == "fictional first-person note",
    f"clerk-lapse-note id/title/kind | {new_src.get('id')!r} {new_src.get('title')!r} {new_src.get('kind')!r}",
)
note = new_src.get("reliability_note", "")
for phrase in (
    "crossing-window named in the original minute has closed",
    "agreement was unfulfilled",
    "no claim was lodged",
    "historical open entry",
    "no resolution",
    "no blame",
    "no reconciliation",
):
    ok(phrase in note, f"reliability note contains {phrase!r}")

new_ev = t99[-1]
ok(new_ev.get("id") == "clerk-lapse-recorded", f"event id | {new_ev.get('id')!r}")
ok(new_ev.get("tick") == 15, f"tick 15 | {new_ev.get('tick')!r}")
ok(new_ev.get("entity_id") == "clerk-maren", f"actor clerk-maren | {new_ev.get('entity_id')!r}")
ok(new_ev.get("place_id") == "chalk-stair", f"place chalk-stair | {new_ev.get('place_id')!r}")
ok(new_ev.get("depends_on") == ["clerk-filing-open"], f"depends_on | {new_ev.get('depends_on')!r}")
ok(new_ev.get("source_id") == "clerk-lapse-note", f"source_id | {new_ev.get('source_id')!r}")
desc = new_ev.get("description", "")
for phrase in (
    "crossing-window named in the original minute has closed",
    "agreement was unfulfilled",
    "no claim was lodged",
    "historical open entry",
):
    ok(phrase in desc, f"event description contains {phrase!r}")

# dependency chain: ticks nondecreasing; every edge strictly earlier
ticks = [ev["tick"] for ev in t99]
ok(ticks == sorted(ticks), f"ticks nondecreasing | {ticks}")
by_id = {ev["id"]: ev for ev in t99}
ok(len(by_id) == len(t99), f"unique event ids | {len(by_id)}/{len(t99)}")
edge_ok = True
edges = []
for ev in t99:
    for dep in ev.get("depends_on") or []:
        target = by_id.get(dep)
        strictly = target is not None and target["tick"] < ev["tick"]
        edges.append((ev["id"], dep, target is not None, strictly))
        if not strictly:
            edge_ok = False
ok(edge_ok and len(edges) == 7, f"edges strictly earlier | n={len(edges)} edges={edges}")

# excerpts byte-prefix
ex98 = (R98 / "fictional-excerpts.md").read_bytes()
ex99 = (R99 / "fictional-excerpts.md").read_bytes()
ok(ex99.startswith(ex98), f"r98 excerpts is byte-prefix of r99 | r98={len(ex98)}B r99={len(ex99)}B delta={len(ex99)-len(ex98)}B")
# also accept prefix-plus-newline if producer inserted a separator after the inherited trailing newline
ok(
    ex99.startswith(ex98) or ex99.startswith(ex98 + b"\n") or ex98.endswith(b"\n") and ex99.startswith(ex98),
    "excerpt prefix form recorded",
)

# obligation arithmetic: 6 fa + 6 claims + 1 rel + 8 events = 21
fa = sum(1 for e in e99 if e.get("first_appearance"))
obl = fa + claims99 + len(r99) + len(t99)
ok(obl == 21, f"obligation arithmetic == 21 | {fa} fa + {claims99} claims + {len(r99)} rel + {len(t99)} ev = {obl}")

# map parse if present
map_path = R99 / "claim-excerpt-map.md"
text = map_path.read_text()
print(f"MAP sha={sha(map_path)}")
print(f"MAP bytes={len(text.encode())} lines={text.count(chr(10))+ (0 if text.endswith(chr(10)) else 1)}")
# declaration line
decl = [ln for ln in text.splitlines() if "JSON fact" in ln or "mapped row" in ln or "obligation" in ln.lower()]
print("MAP decl-ish:")
for ln in decl[:12]:
    print("  " + ln)

row_re = re.compile(r"^\|\s*(J\d+|S\d+)\s*\|")
rows = []
for i, ln in enumerate(text.splitlines(), 1):
    m = row_re.match(ln)
    if m:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append((m.group(1), i, cells, ln))
ids = [r[0] for r in rows]
print(f"MAP row ids ({len(ids)}): {ids}")
j_ids = [i for i in ids if i.startswith("J")]
s_ids = [i for i in ids if i.startswith("S")]
print(f"MAP J={len(j_ids)} S={len(s_ids)}")

# compare inherited rows to r98 map, allowing only namespace cell change
map98 = (R98 / "claim-excerpt-map.md").read_text()
rows98 = {}
for ln in map98.splitlines():
    m = row_re.match(ln)
    if m:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows98[m.group(1)] = cells

ns_only = 0
other = 0
missing = []
for rid, lineno, cells, raw in rows:
    if rid not in rows98:
        continue
    a, b = rows98[rid], cells
    if a == b:
        continue
    diffs = []
    n = max(len(a), len(b))
    for k in range(n):
        ca = a[k] if k < len(a) else "<missing>"
        cb = b[k] if k < len(b) else "<missing>"
        if ca != cb:
            diffs.append((k, ca, cb))
    ns_diffs = [
        d
        for d in diffs
        if "r98-clerk-filing" in d[1] and "r99-window-lapse" in d[2] and d[1].replace("r98-clerk-filing", "r99-window-lapse") == d[2]
    ]
    if len(diffs) == len(ns_diffs) and diffs:
        ns_only += 1
    elif diffs:
        other += 1
        print(f"ROW-OTHER-DIFF {rid} line={lineno} diffs={diffs}")
inherited_present = [rid for rid in rows98 if rid in ids]
print(f"inherited rows in r98 map={len(rows98)} present in r99={len(inherited_present)} ns-only-diffs={ns_only} other-diffs={other}")
new_rows = [rid for rid in ids if rid not in rows98]
print(f"new map rows vs r98: {new_rows}")
for rid, lineno, cells, raw in rows:
    if rid in new_rows:
        print(f"NEWROW {rid} line={lineno} cells={cells}")

# forbidden positive assertions in new excerpt tail
tail = ex99[len(ex98):].decode() if ex99.startswith(ex98) else ex99.decode()
print("--- NEW EXCERPT TAIL ---")
print(tail)
print("--- END TAIL ---")

print(f"FAILS: {fails if fails else 'none'}")
sys.exit(1 if fails else 0)
