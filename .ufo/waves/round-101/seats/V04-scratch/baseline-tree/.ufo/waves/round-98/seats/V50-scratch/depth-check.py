#!/usr/bin/env python3
"""V50 independent depth check: r97->r98 preservation, counts, map inheritance."""
import json, hashlib, sys, re

R97 = "corpus/fixtures/r97-crossing-acknowledgment"
R98 = "corpus/fixtures/r98-clerk-filing"

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def load(p):
    return json.load(open(p))

fails = []
def check(name, cond, detail=""):
    print(("OK   " if cond else "FAIL ") + name + ((" | " + detail) if detail else ""))
    if not cond:
        fails.append(name)

# 1. byte-identical copies
for f in ["contradictions.json", "inspiration-note.md", "relations.json", "source-excerpt.md"]:
    a, b = f"{R97}/{f}", f"{R98}/{f}"
    check(f"byte-identical {f}", sha(a) == sha(b), f"r97={sha(a)[:16]} r98={sha(b)[:16]}")

# 2. JSON counts + prefix equality
e97, e98 = load(f"{R97}/entities.json"), load(f"{R98}/entities.json")
s97, s98 = load(f"{R97}/sources.json"), load(f"{R98}/sources.json")
t97, t98 = load(f"{R97}/timeline.json"), load(f"{R98}/timeline.json")
r98, c98 = load(f"{R98}/relations.json"), load(f"{R98}/contradictions.json")
check("entities 5->6", len(e97) == 5 and len(e98) == 6, f"{len(e97)}->{len(e98)}")
check("relations 1", len(r98) == 1, str(len(r98)))
check("timeline 6->7", len(t97) == 6 and len(t98) == 7, f"{len(t97)}->{len(t98)}")
check("sources 6->7", len(s97) == 6 and len(s98) == 7, f"{len(s97)}->{len(s98)}")
check("contradictions []", c98 == [], str(c98))
check("entities[:5] parsed-equal", e98[:5] == e97, "")
check("sources[:6] parsed-equal", s98[:6] == s97, "")
check("timeline[:6] parsed-equal", t98[:6] == t97, "")

# 3. new rows exact
new_ent = e98[5]
check("clerk-maren fields", new_ent.get("id") == "clerk-maren" and new_ent.get("kind") == "character"
      and new_ent.get("name") == "Maren" and new_ent.get("first_appearance") == "clerk-filing-note"
      and len(new_ent.get("claims", [])) == 1
      and new_ent["claims"][0].get("source_id") == "clerk-filing-note",
      json.dumps(new_ent, ensure_ascii=False)[:200])
new_src = s98[6]
check("clerk-filing-note id/title", new_src.get("id") == "clerk-filing-note"
      and "Maren" in new_src.get("title", ""), new_src.get("title", ""))
print("RELIABILITY-NOTE:", new_src.get("reliability_note", ""))
new_ev = t98[6]
check("clerk-filing-open fields", new_ev.get("id") == "clerk-filing-open" and new_ev.get("tick") == 14
      and new_ev.get("entity_id") == "clerk-maren" and new_ev.get("place_id") == "chalk-stair"
      and new_ev.get("depends_on") == ["acknowledgment-aru-records"]
      and new_ev.get("source_id") == "clerk-filing-note",
      json.dumps(new_ev, ensure_ascii=False)[:260])

# 4. fictional-excerpts byte-prefix
b97 = open(f"{R97}/fictional-excerpts.md", "rb").read()
b98 = open(f"{R98}/fictional-excerpts.md", "rb").read()
check("r97 excerpts is byte-prefix of r98", b98.startswith(b97),
      f"r97={len(b97)}B r98={len(b98)}B delta={len(b98)-len(b97)}B")

# 5. map rows: inherited modulo namespace, new rows exact, none gone
def rows(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\| (J\d\d|S\d\d) \|(.*)$", line.rstrip("\n"))
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            out[m.group(1)] = cells
    return out
m97 = rows(f"{R97}/claim-excerpt-map.md")
m98 = rows(f"{R98}/claim-excerpt-map.md")
check("row id sets", set(m97) <= set(m98) and set(m98) - set(m97) == {"J18", "J19", "J20"},
      f"r97={sorted(m97)} new={sorted(set(m98)-set(m97))} gone={sorted(set(m97)-set(m98))}")
ns_old, ns_new = "r97-crossing-acknowledgment:", "r98-clerk-filing:"
diff_cells = 0
for rid in m97:
    a = [c.replace(ns_old, ns_new) for c in m97[rid]]
    b = m98[rid]
    if a != b:
        diff_cells += 1
        print(f"DIFFCELL {rid}\n  r97->qual: {a}\n  r98:       {b}")
check("inherited rows equal modulo namespace", diff_cells == 0, f"{len(m97)} inherited rows compared")
for rid in ["J18", "J19", "J20"]:
    print(rid, json.dumps(m98[rid], ensure_ascii=False))
check("J18 pointer", "entities.json#/5/first_appearance" in m98["J18"][0], "")
check("J19 pointer", "entities.json#/5/claims/0" in m98["J19"][0], "")
check("J20 pointer", "timeline.json#/6" in m98["J20"][0], "")

# 6. obligation arithmetic
oblig = len(e98) + sum(len(e.get("claims", [])) for e in e98) + len(r98) + len(t98)
check("obligation arithmetic == 20", oblig == 20, f"{len(e98)} fa + {sum(len(e.get('claims',[])) for e in e98)} claims + {len(r98)} rel + {len(t98)} ev = {oblig}")

print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
