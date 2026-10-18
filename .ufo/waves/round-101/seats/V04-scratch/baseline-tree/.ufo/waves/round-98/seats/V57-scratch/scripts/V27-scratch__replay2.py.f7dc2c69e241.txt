#!/usr/bin/env python3
"""V27 (round 98) replay battery 2: census receipt, inherited map-row equality,
dependency-chain audit, dangling/duplicate audit, class assertions."""
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
os.chdir(ROOT)
R97 = "corpus/fixtures/r97-crossing-acknowledgment"
R98 = "corpus/fixtures/r98-clerk-filing"

# --- census: exit + stdout hash for every fixture dir -------------------
dirs = sorted(d for d in os.listdir("corpus/fixtures")
              if os.path.isdir(os.path.join("corpus/fixtures", d)))
clean = neg = vl = 0
odd = []
receipts = {}
for d in dirs:
    rel = f"corpus/fixtures/{d}"
    p = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", rel],
                       capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    receipts[rel] = {"exit": p.returncode,
                     "sha256": hashlib.sha256(out.encode()).hexdigest()}
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        neg += 1
        vl += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else:
        odd.append((rel, p.returncode, out))
print("CENSUS", json.dumps({"dirs": len(dirs), "clean": clean, "negative": neg,
                            "violation_lines": vl, "odd": odd}))
json.dump(receipts, open(".ufo/waves/round-98/seats/V27-scratch/census-receipts.json", "w"),
          indent=1, sort_keys=True)

# --- map row equality J01..J17 (modulo namespace column) ----------------
def rows(path):
    txt = open(path).read()
    out = {}
    for m in re.finditer(r"^\| (J\d+) \|(.+)\|\s*$", txt, re.M):
        cells = [c.strip() for c in m.group(2).split("|")]
        out[m.group(1)] = cells
    return out

r97, r98 = rows(f"{R97}/claim-excerpt-map.md"), rows(f"{R98}/claim-excerpt-map.md")
print("row counts r97/r98:", len(r97), len(r98))
print("r98 new row ids:", sorted(set(r98) - set(r97)))
diffs = []
for k in sorted(set(r97) & set(r98)):
    a, b = r97[k], r98[k]
    if len(a) != len(b):
        diffs.append((k, "cell-count", len(a), len(b)))
        continue
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            diffs.append((k, i, x[:60], y[:60]))
print("inherited-row diffs (modulo namespace col 2):",
      [d for d in diffs if not (d[1] == 2)] or "NONE")
print("namespace-column diffs:", len([d for d in diffs if d[1] == 2]))

# --- chain audit on r98 ------------------------------------------------
t = json.load(open(f"{R98}/timeline.json"))
ids = [e["id"] for e in t]
ticks = [e["tick"] for e in t]
idx = {e["id"]: i for i, e in enumerate(t)}
edges = [(e["id"], d) for e in t for d in e["depends_on"]]
backward = all(idx[d] < idx[e] and t[idx[d]]["tick"] < t[idx[e]]["tick"]
               for e, d in edges)
print("ticks:", ticks)
print("ids:", ids)
print("edges:", len(edges), "all strictly backward+earlier-tick:", backward)
print("last event:", json.dumps(t[-1], ensure_ascii=False))

# --- dangling / duplicate audit ---------------------------------------
e = json.load(open(f"{R98}/entities.json"))
r = json.load(open(f"{R98}/relations.json"))
s = json.load(open(f"{R98}/sources.json"))
eids = {x["id"] for x in e}
sids = {x["id"] for x in s}
pids = {x["id"] for x in e if x["kind"] == "place"}
dups = {k: [i for i in {x["id"] for x in v} if [y["id"] for y in v].count(i) > 1]
        for k, v in (("entities", e), ("sources", s), ("events", t))}
dangling = []
for ev in t:
    if ev["entity_id"] not in eids:
        dangling.append(("entity", ev["id"], ev["entity_id"]))
    if ev["place_id"] not in eids:
        dangling.append(("place", ev["id"], ev["place_id"]))
    if ev["source_id"] not in sids:
        dangling.append(("source", ev["id"], ev["source_id"]))
    for d in ev["depends_on"]:
        if d not in ids:
            dangling.append(("dep", ev["id"], d))
for x in e:
    if x["first_appearance"] not in sids:
        dangling.append(("first_appearance", x["id"], x["first_appearance"]))
    for c in x.get("claims", []):
        if c["source_id"] not in sids:
            dangling.append(("claim-source", x["id"], c["source_id"]))
for rel in r:
    if rel["from"] not in eids or rel["to"] not in eids or rel["source_id"] not in sids:
        dangling.append(("relation", rel))
print("duplicates:", dups)
print("dangling:", dangling)

# --- class assertions (institutional no-finding) ----------------------
note = json.load(open(f"{R98}/sources.json"))[-1]
ex = open(f"{R98}/fictional-excerpts.md").read().splitlines()
print("source[-1] id/kind:", note["id"], "/", note["kind"])
for phrase in ["no finding", "no verdict", "no reconciliation", "no resolution",
               "not evidence of a breach", "no winner"]:
    print(f"  reliability note contains {phrase!r}:", phrase in note["reliability_note"])
print("excerpt tail lines 54-64:")
for i, line in enumerate(ex[53:64], 54):
    print(f"  {i}: {line}")
