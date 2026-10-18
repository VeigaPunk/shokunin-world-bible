#!/usr/bin/env python3
"""R1 scratch probe: build legacy-dialect clusters (dual-pointer + single control)."""
import json
import pathlib
import sys

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
OUT = ROOT / ".ufo/waves/round-97/seats/scratch-R1"

FILES = {
    "entities.json": [{
        "id": "test-entity",
        "first_appearance": "fixture-source",
        "claims": [{"statement": "test claim", "source_id": "fixture-source"}],
    }],
    "relations.json": [{
        "from": "test-entity", "to": "other", "type": "linked", "source_id": "fixture-source",
    }],
    "timeline.json": [{"id": "test-event", "source_id": "fixture-source"}],
}


def build(name, e1_cell):
    cluster = OUT / name
    cluster.mkdir(parents=True, exist_ok=True)
    for filename, value in FILES.items():
        (cluster / filename).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    rows = [
        ("E1", e1_cell),
        ("E2", "`entities[0].claims[0]`"),
        ("R1", "`relations[0]`"),
        ("T1", "`timeline[0]`"),
    ]
    lines = [
        "# Isolated mapping fixture",
        "",
        "## JSON facts",
        "",
        "| ID | JSON fact and fields | In-world source ID |",
        "|---|---|---|",
    ]
    for row_id, cell in rows:
        lines.append(f"| {row_id} | {cell} | `fixture-source` |")
    (cluster / "claim-excerpt-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"built {cluster}")


build("probe-legacy-dual", "`entities[0].first_appearance` (also named `entities[1].first_appearance`)")
build("probe-legacy-single", "`entities[0].first_appearance`")
sys.exit(0)
