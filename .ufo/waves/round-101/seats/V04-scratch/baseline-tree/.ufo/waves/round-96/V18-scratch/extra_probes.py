#!/usr/bin/env python3
"""V18 extra addition-class probes on scratch copies of r96-crossing-response.

A: new event row WITH depends_on      -> expect exit 1 ADDITION-DETECTED
B: new event row WITHOUT depends_on   -> inventory-neutral; expect exit 2 DIGEST-MISMATCH
C: new relation triple                -> expect exit 1 ADDITION-DETECTED
Each case runs twice; outputs captured verbatim.
"""
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = ROOT / "corpus/tools/dependency_freeze.py"
S = ROOT / ".ufo/waves/round-96/V18-scratch/scratch-root"
FIX = "r96-crossing-response"


def fresh(tag):
    d = S / f"extra-{tag}" / FIX
    if d.parent.exists():
        shutil.rmtree(d.parent)
    d.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures" / FIX, d)
    return d


def run(d):
    r = subprocess.run(["python3", str(TOOL), str(d)], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, (r.stdout + r.stderr).strip()


def report(tag, d):
    print(f"=== {tag} dir={d}")
    outs = []
    for i in (1, 2):
        code, out = run(d)
        outs.append(out)
        print(f"--- run{i} exit={code}")
        print(out)
    print(f"=== SUMMARY {tag} exits_identical={outs[0] == outs[1]}")


# A: new event with a dependency
d = fresh("addevent")
tl = json.loads((d / "timeline.json").read_text())
tl.append({"id": "intruder-tick-13", "tick": 13, "entity_id": "aru", "place_id": "quiet-rise",
           "depends_on": ["response-evin-salt-court"], "description": "Intruder event.",
           "source_id": "paired-clock"})
(d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
report("A-new-event-with-deps", d)

# B: new event with no dependency (inventory-neutral)
d = fresh("addempty")
tl = json.loads((d / "timeline.json").read_text())
tl.append({"id": "silent-tick-14", "tick": 14, "entity_id": "aru", "place_id": "quiet-rise",
           "depends_on": [], "description": "Unlinked event.", "source_id": "paired-clock"})
(d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
report("B-new-event-no-deps", d)

# C: new relation triple
d = fresh("addrel")
rels = json.loads((d / "relations.json").read_text())
rels.append({"from": "evin", "to": "aru", "type": "second_account_same_occasion",
             "source_id": "evin-response-note"})
(d / "relations.json").write_text(json.dumps(rels, indent=2) + "\n")
report("C-new-relation", d)
