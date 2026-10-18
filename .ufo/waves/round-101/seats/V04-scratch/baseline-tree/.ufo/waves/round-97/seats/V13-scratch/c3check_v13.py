#!/usr/bin/env python3
"""V13 (round 97) c3-checker: check_bible + json.load counts for
corpus/fixtures/r97-crossing-acknowledgment, plus r96 post-repair CLEAN."""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
R97 = "corpus/fixtures/r97-crossing-acknowledgment"
R96 = "corpus/fixtures/r96-crossing-response"

out = {}

for name, rel in (("r97", R97), ("r96", R96)):
    p = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", rel],
                       cwd=REPO, capture_output=True, text=True)
    out[name + "_check_bible"] = {
        "argv": "python3 corpus/fixtures/check_bible.py %s" % rel,
        "exit": p.returncode,
        "stdout": p.stdout.strip(),
        "stderr": p.stderr.strip(),
    }

tables = {}
for t in ("entities", "relations", "timeline", "sources", "contradictions"):
    with open(os.path.join(REPO, R97, t + ".json")) as fh:
        tables[t] = json.load(fh)

out["r97_counts"] = {
    "entities": len(tables["entities"]),
    "relations": len(tables["relations"]),
    "events": len(tables["timeline"]),
    "sources": len(tables["sources"]),
    "contradictions": len(tables["contradictions"]),
}

ack = [e for e in tables["timeline"] if e["id"] == "acknowledgment-aru-records"]
out["ack_event"] = ack

# dangling / duplicate checks
ent_ids = [e["id"] for e in tables["entities"]]
src_ids = [s["id"] for s in tables["sources"]]
ev_ids = [e["id"] for e in tables["timeline"]]
dup = {
    "entities": sorted({i for i in ent_ids if ent_ids.count(i) > 1}),
    "sources": sorted({i for i in src_ids if src_ids.count(i) > 1}),
    "events": sorted({i for i in ev_ids if ev_ids.count(i) > 1}),
}
out["duplicates"] = dup

dangling = []
for e in tables["timeline"]:
    if e["entity_id"] not in ent_ids:
        dangling.append("event %s entity_id %s" % (e["id"], e["entity_id"]))
    if e["place_id"] not in ent_ids:
        dangling.append("event %s place_id %s" % (e["id"], e["place_id"]))
    if e["source_id"] not in src_ids:
        dangling.append("event %s source_id %s" % (e["id"], e["source_id"]))
    for d in e["depends_on"]:
        if d not in ev_ids:
            dangling.append("event %s depends_on %s" % (e["id"], d))
for r in tables["relations"]:
    if r["from"] not in ent_ids:
        dangling.append("relation from %s" % r["from"])
    if r["to"] not in ent_ids:
        dangling.append("relation to %s" % r["to"])
    if r["source_id"] not in src_ids:
        dangling.append("relation source_id %s" % r["source_id"])
for e in tables["entities"]:
    if e["first_appearance"] not in src_ids:
        dangling.append("entity %s first_appearance %s" % (e["id"], e["first_appearance"]))
    for c in e.get("claims", []):
        if c["source_id"] not in src_ids:
            dangling.append("entity %s claim source_id %s" % (e["id"], c["source_id"]))
out["dangling"] = dangling

# inherited-table byte identity vs r96 for entities/relations/contradictions
import hashlib
def sha(rel):
    with open(os.path.join(REPO, rel), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()

bytecmp = {}
for t in ("entities.json", "relations.json", "contradictions.json",
          "inspiration-note.md", "source-excerpt.md"):
    bytecmp[t] = {
        "r97": sha(R97 + "/" + t),
        "r96": sha(R96 + "/" + t),
        "identical": sha(R97 + "/" + t) == sha(R96 + "/" + t),
    }
out["byte_identity_r97_vs_r96"] = bytecmp

print(json.dumps(out, indent=2))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "c3check.json"), "w") as fh:
    json.dump(out, fh, indent=2, sort_keys=True)
