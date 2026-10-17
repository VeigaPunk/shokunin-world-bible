#!/usr/bin/env python3
"""V48 scratch mutations (v2) for dependency_freeze direct demos.
Targets preserve the pinned basename so pin lookup reaches comparison."""
import json
import shutil
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
MUT = SCRATCH / "mutations"
CORPUS = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures")


def load(p):
    return json.loads(p.read_text())


def save(p, obj):
    p.write_text(json.dumps(obj, indent=2) + "\n")


def copy(fixture, case):
    target = MUT / case / fixture
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(CORPUS / fixture, target)
    return target


def set_deps(path, event_id, deps):
    tl = load(path)
    for ev in tl:
        if ev["id"] == event_id:
            ev["depends_on"] = deps
    save(path, tl)


# reduction: drop evin-ninth-bell from the tick-10 decision
t = copy("r94-paired-crossing", "reduction-r94")
tl = load(t / "timeline.json")
for ev in tl:
    if ev["id"] == "paired-crossing-decision":
        ev["depends_on"] = [d for d in ev["depends_on"] if d != "evin-ninth-bell"]
save(t / "timeline.json", tl)

t = copy("r95-crossing-aftermath", "reduction-r95")
tl = load(t / "timeline.json")
for ev in tl:
    if ev["id"] == "paired-crossing-decision":
        ev["depends_on"] = [d for d in ev["depends_on"] if d != "evin-ninth-bell"]
save(t / "timeline.json", tl)

# addition: add an edge not in the pin
t = copy("r94-paired-crossing", "addition-r94")
set_deps(t / "timeline.json", "aru-ninth-bell", ["evin-ninth-bell"])

t = copy("r95-crossing-aftermath", "addition-r95")
tl = load(t / "timeline.json")
for ev in tl:
    if ev["id"] == "aftermath-missing-evin":
        ev["depends_on"] = ev["depends_on"] + ["phantom-ninth-bell"]
save(t / "timeline.json", tl)

# relation endpoint flip
t = copy("r96-crossing-response", "endpoint-rel-r96")
rel = load(t / "relations.json")
rel[0]["from"], rel[0]["to"] = rel[0]["to"], rel[0]["from"]
save(t / "relations.json", rel)

# event endpoint change (place_id)
t = copy("r95-crossing-aftermath", "endpoint-event-r95")
tl = load(t / "timeline.json")
for ev in tl:
    if ev["id"] == "paired-crossing-decision":
        ev["place_id"] = "salt-court"
save(t / "timeline.json", tl)

# text-only tamper (inventory unchanged, digest changed)
t = copy("r94-paired-crossing", "tamper-text-r94")
tl = load(t / "timeline.json")
for ev in tl:
    if ev["id"] == "aru-ninth-bell":
        ev["description"] += " [tampered text, edges unchanged]"
save(t / "timeline.json", tl)

# digest tamper matching the tool's own case
t = copy("r95-crossing-aftermath", "tamper-digest-r95")
txt = (t / "timeline.json").read_text()
(t / "timeline.json").write_text(txt.replace("south bell at Salt Court", "South bell at Salt Court", 1))

# missing timeline
t = copy("r95-crossing-aftermath", "missing-timeline")
(t / "timeline.json").unlink()

# malformed json
t = copy("r95-crossing-aftermath", "malformed")
(t / "timeline.json").write_text("[{\n")

# unpinned basename
copy("r95-crossing-aftermath", "unpinned")
t = MUT / "unpinned" / "r95-crossing-aftermath"
t.rename(MUT / "unpinned" / "not-a-pinned-fixture")

print("mutations v2 applied")
for p in sorted(MUT.rglob("timeline.json")):
    tl = json.loads(p.read_text())
    print(p.relative_to(SCRATCH), {e["id"]: e["depends_on"] for e in tl})
