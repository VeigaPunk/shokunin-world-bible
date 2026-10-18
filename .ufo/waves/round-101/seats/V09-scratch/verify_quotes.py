#!/usr/bin/env python3
"""V09 byte-level verification of r101-r10-register-first-entry.md claims."""
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
ok = fail = 0

def check(name, cond, observed=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} :: {observed}")

def lines(rel):
    return (ROOT / rel).read_text(encoding="utf-8").splitlines()

def rng(rel, a, b):  # 1-based inclusive
    return lines(rel)[a-1:b]

# --- excerpt quotes ---
q = rng("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 26, 29)
exp = ["> Tick 11: I waited at the Chalk Stair through the agreed bell.",
       "> Evin did not come.",
       "> The agreement we chalked covered this crossing only.",
       "> I assert no other duty, no breach, and no obligation beyond this crossing."]
check("r95:26-29 quote", [l.strip() for l in q] == exp, repr(q))
check("r95:26 has 'agreed bell'", "the agreed bell" in q[0], repr(q[0]))
check("r95:27 non-arrival", q[1].strip() == "> Evin did not come.", repr(q[1]))
check("r95:28 chalked agreement", "The agreement we chalked covered this crossing only." in q[2], repr(q[2]))
check("r95:29 no-breach bound", "asserts no breach" in q[3], repr(q[3]))

q = rng("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 37, 40)
exp = ["> Tick 12: I was at Salt Court through the same agreed bell.",
       "> I make no accusation against Aru.",
       "> I select no winner between our two accounts.",
       "> Both accounts stand unresolved."]
check("r96:37-40 quote", [l.strip() for l in q] == exp, repr(q))
check("r96:38-40 accuse/winner/false bounds",
      all(s in " ".join(x.strip() for x in q[1:]) for s in ("no accusation", "select no winner", "stand unresolved")), repr(q[1:]))

q = rng("corpus/fixtures/r94-paired-crossing/fictional-excerpts.md", 19, 20)
check("r94:19 minute sentence",
      "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair." in q[0], repr(q[0]))
check("r94:20 ninth-bell + tick-10 meeting",
      "ninth-bell" in q[1] and "tick 10" in q[1], repr(q[1]))

# --- README / scope-note citations ---
r = lines("corpus/fixtures/r96-crossing-response/README.md")
check("r96 README:3 lineage", "continuation" in r[2], repr(r[2]))
check("r96 README:11 second account same occasion", "second account of the same occasion" in r[10], repr(r[10]))
r = lines("corpus/fixtures/r94-paired-crossing/README.md")
check("r94 README:13 editorial encodings", "editorial" in r[12] and "not literal JSON wording" in r[12], repr(r[12]))
check("r94 README:5 namespace heading", r[4].strip() == "## Namespace and occasion comparison", repr(r[4]))
r = lines("corpus/fixtures/r95-crossing-aftermath/README.md")
check("r95 README:5 namespace heading", r[4].strip() == "## Namespace and occasion comparison", repr(r[4]))
check("r95 README:11 no breach", "no breach" in r[10] or "asserts no breach" in r[10], repr(r[10]))
r = lines("corpus/fixtures/r96-crossing-response/README.md")
check("r96 README:5 namespace heading", r[4].strip() == "## Namespace and occasion comparison", repr(r[4]))
s = lines("corpus/knowledge/r96-response-scope-note.md")
check("r96 scope:31 different actors/places", "Different actors at different places" in s[30], repr(s[30]))
check("r96 scope:13 r35 distinction", ("r35" in s[12] or "bell" in s[12].lower()), repr(s[12]))
check("r96 scope:40 r35 distinction", ("r35" in s[39] or "different" in s[39].lower()), repr(s[39]))
f = lines("corpus/fixtures/README.md")
check("fixtures README:761 Neither wins", "Neither wins." in f[760], repr(f[760]))

# --- r35 precedent ---
c = json.load(open(ROOT / "corpus/fixtures/r35-bell7-conflict/contradictions.json"))
check("r35 contradictions#/0 id", c and c[0].get("id") == "bell7-location-reports", repr(c)[:200])
check("r35 field place_id", c and c[0].get("field") == "place_id", repr(c)[:200])
t = json.load(open(ROOT / "corpus/fixtures/r35-bell7-conflict/timeline.json"))
check("r35 timeline#/2-3 exist", len(t) >= 4 and all("place_id" in t[i] for i in (2, 3)), repr([e.get("id") for e in t]))

# --- r88 table row/appendix quotes ---
tab = lines("corpus/knowledge/r88-sourced-inspiration-decision-table.md")
check("r88:26 R10 row compare-clause",
      "confirm a shared referent, field, and occasion" in tab[25], repr(tab[25]))
check("r88:26 manual-gate quote",
      "cross-cluster comparison and register-reference checks are an explicit manual integration gate" in tab[25], repr(tab[25]))
block = " ".join(tab[89:92])
check("r88:90-92 comparison-outcomes clause",
      "## R10 comparison outcomes" in block and "NOT the live register" in block, repr(block)[:300])
gate = " ".join(tab[92:94])
check("r88:93-94 gate incompatible-only",
      "Only a source-backed shared referent, field, and occasion with incompatible assertions enters" in gate
      and "corpus/knowledge/cross-cluster-contradictions.md" in gate, repr(gate)[:300])
check("r88:97 first real entry awaits conflict", "first real entry awaits a genuine conflict" in tab[96], repr(tab[96]))
ns = " ".join(tab[98:100])
check("r88:99-100 cluster-local namespace clause",
      "cluster-local" in ns and "(cluster-relative path, source_id)" in ns, repr(ns)[:300])
check("r88:110 clean-replay bound", "clean fixture replay" in tab[109], repr(tab[109]))

# --- sources.json line numbers ---
s95 = lines("corpus/fixtures/r95-crossing-aftermath/sources.json")
check("r95 sources:21 aru-aftermath-note", '"aru-aftermath-note"' in s95[20], repr(s95[20]))
s96 = lines("corpus/fixtures/r96-crossing-response/sources.json")
check("r96 sources:27 evin-response-note", '"evin-response-note"' in s96[26], repr(s96[26]))
s94 = lines("corpus/fixtures/r94-paired-crossing/sources.json")
check("r94 sources:15 crossing-minute", '"crossing-minute"' in s94[14], repr(s94[14]))

# --- LOG citations ---
lg = lines("LOG.md")
check("LOG:2656-2658 zero shared referents",
      any("zero shared referents or supported conflicts" in lg[i] for i in range(2655, 2658)),
      repr(lg[2655:2658])[:300])

# --- receipts replay ---
hashes = []
for fx in ["r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing","r99-window-lapse","r100-docket-review"]:
    b = (ROOT / f"corpus/fixtures/{fx}/relations.json").read_bytes()
    hashes.append((fx, hashlib.sha256(b).hexdigest()[:16], len(b)))
check("relation byte-identity 7/7", all(h == ("r94-paired-crossing", "c279254bc7de0636", 139) for _, h in hashes[1:]) and hashes[0][1:] == ("c279254bc7de0636", 139), repr(hashes))

rel0 = json.load(open(ROOT / "corpus/fixtures/r94-paired-crossing/relations.json"))[0]
check("relations#/0 value", rel0 == {"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}, repr(rel0))

t95 = json.load(open(ROOT / "corpus/fixtures/r95-crossing-aftermath/timeline.json"))
e = t95[3]
check("r95 timeline#/3", e["id"] == "aftermath-missing-evin" and e["tick"] == 11 and e["entity_id"] == "aru"
      and e["place_id"] == "chalk-stair" and e["depends_on"] == ["paired-crossing-decision"] and e["source_id"] == "aru-aftermath-note", repr(e))
t96 = json.load(open(ROOT / "corpus/fixtures/r96-crossing-response/timeline.json"))
e = t96[4]
check("r96 timeline#/4", e["id"] == "response-evin-salt-court" and e["tick"] == 12 and e["entity_id"] == "evin"
      and e["place_id"] == "salt-court" and e["depends_on"] == ["aftermath-missing-evin"] and e["source_id"] == "evin-response-note", repr(e))

b94 = (ROOT / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md").read_bytes()
b95 = (ROOT / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md").read_bytes()
b96 = (ROOT / "corpus/fixtures/r96-crossing-response/fictional-excerpts.md").read_bytes()
check("prefix r95 starts with r94", b95.startswith(b94))
check("prefix r96 starts with r95", b96.startswith(b95))

r100 = lines("corpus/fixtures/r100-docket-review/fictional-excerpts.md")
check("r100 snapshot has Aru note at :26", "Tick 11: I waited at the Chalk Stair through the agreed bell." in r100[25], repr(r100[25]))
check("r100 snapshot has Evin note at :37", "Tick 12: I was at Salt Court through the same agreed bell." in r100[36], repr(r100[36]))

check("register file absent", not (ROOT / "corpus/knowledge/cross-cluster-contradictions.md").exists())

for fx in ("r95-crossing-aftermath", "r96-crossing-response"):
    c = json.load(open(ROOT / f"corpus/fixtures/{fx}/contradictions.json"))
    check(f"{fx} contradictions []", c == [], repr(c))

print(f"\nSUMMARY: {ok} PASS / {fail} FAIL")
