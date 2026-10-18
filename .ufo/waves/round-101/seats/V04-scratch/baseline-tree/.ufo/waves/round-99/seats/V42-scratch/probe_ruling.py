#!/usr/bin/env python3
"""Scratch probes: gate-blindness of a ruling/resolution reading. Does not touch corpus."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = ROOT / "corpus/fixtures/r99-window-lapse"
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V42-scratch"
PY = sys.executable


def run(argv, cwd=ROOT):
    result = subprocess.run([PY, *argv], cwd=cwd, capture_output=True, text=True)
    print("$", PY, *argv)
    print(result.stdout, end="" if result.stdout.endswith("\n") or not result.stdout else "\n")
    if result.stderr.strip():
        print("STDERR:", result.stderr.strip())
    print("EXIT", result.returncode)
    print("---")
    return result.returncode


def copy_fix(name):
    dest = SCRATCH / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest)
    return dest


def main():
    print("=== Probe A: appended ruling event + ruling source, tick 16 ===")
    a = copy_fix("probe-a-ruling-row")
    sources = json.loads((a / "sources.json").read_text())
    sources.append({
        "id": "clerk-ruling-note",
        "title": "Maren's Chalk Stair Ruling Note",
        "kind": "fictional first-person note",
        "reliability_note": "The clerk ruled that Aru's account prevails, assigned blame to Evin, and resolved the matter.",
    })
    (a / "sources.json").write_text(json.dumps(sources, indent=2) + "\n")
    timeline = json.loads((a / "timeline.json").read_text())
    timeline.append({
        "id": "clerk-ruling-issued",
        "tick": 16,
        "entity_id": "clerk-maren",
        "place_id": "chalk-stair",
        "depends_on": ["clerk-lapse-recorded"],
        "description": "At tick 16 the clerk issued an official ruling adopting Aru's account, assigning blame to Evin, and closing the matter.",
        "source_id": "clerk-ruling-note",
    })
    (a / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n")
    run(["corpus/fixtures/check_bible.py", str(a)])

    print("=== Probe B: invert delivered lapse description and excerpt denial into a ruling ===")
    b = copy_fix("probe-b-inverted")
    text = (b / "fictional-excerpts.md").read_text()
    text = text.replace(
        "> I record no resolution, assign no blame, and reconcile nothing.",
        "> I record the resolution, assign blame to Evin, and reconcile the accounts.",
    )
    text = text.replace(
        "It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; the crossing-scoped agreement above is unchanged, and the matter stays open.",
        "It asserts a resolution, assigns blame to Evin, and reconciles the accounts; the matter is closed.",
    )
    (b / "fictional-excerpts.md").write_text(text)
    timeline = json.loads((b / "timeline.json").read_text())
    for event in timeline:
        if event["id"] == "clerk-lapse-recorded":
            event["description"] = (
                "At the Chalk Stair at tick 15, the clerk ruled that the agreement was breached by Evin, "
                "assigned blame, resolved the accounts in Aru's favor, and closed the matter."
            )
    (b / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n")
    sources = json.loads((b / "sources.json").read_text())
    for source in sources:
        if source["id"] == "clerk-lapse-note":
            source["reliability_note"] = (
                "The clerk ruled that Evin breached the agreement, assigned blame, and resolved the matter."
            )
    (b / "sources.json").write_text(json.dumps(sources, indent=2) + "\n")
    # map still expects the original anchor sentence, which remains at line 70
    run(["corpus/fixtures/check_bible.py", str(b)])
    run(["corpus/tools/support_check.py", str(b)])
    run(["corpus/tools/map_obligations.py", str(b)])

    print("=== Probe C: tick-15 collision (honesty; not the ruling class) ===")
    c = copy_fix("probe-c-tick-collision")
    timeline = json.loads((c / "timeline.json").read_text())
    timeline.append({
        "id": "clerk-ruling-same-tick",
        "tick": 15,
        "entity_id": "clerk-maren",
        "place_id": "salt-court",
        "depends_on": ["clerk-filing-open"],
        "description": "The clerk rules and closes the matter at tick 15.",
        "source_id": "clerk-lapse-note",
    })
    (c / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n")
    run(["corpus/fixtures/check_bible.py", str(c)])


if __name__ == "__main__":
    main()
