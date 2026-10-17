#!/usr/bin/env python3
"""Independent extraction of dependency edges + relation endpoints for V20 review."""
import json
import sys
from pathlib import Path

for fixture in sys.argv[1:]:
    root = Path(fixture)
    timeline = json.loads((root / "timeline.json").read_text())
    relations = json.loads((root / "relations.json").read_text())
    print(f"== {root.name}")
    for event in timeline:
        deps = event.get("depends_on")
        print(f"  EV {event['id']} tick={event.get('tick')} deps={sorted(deps) if isinstance(deps, list) else deps}")
    for i, rel in enumerate(relations):
        print(f"  REL#{i} {rel.get('left_id')}->{rel.get('right_id')} type={rel.get('type')}")
