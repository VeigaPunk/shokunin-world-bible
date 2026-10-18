#!/usr/bin/env python3
"""V46 scratch mutator: copy a fixture, drop one depends_on entry from one event.

Mirrors the r96 self-test reduction_edge_drop mechanics:
  record["depends_on"] = [dep for dep in record["depends_on"] if dep != DEP]
"""
import json
import shutil
import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
event_id = sys.argv[3]
dep = sys.argv[4]

if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst)

timeline_path = dst / "timeline.json"
timeline = json.loads(timeline_path.read_text(encoding="utf-8"))
hits = [r for r in timeline if r.get("id") == event_id]
assert len(hits) == 1, f"expected exactly one event {event_id!r}, found {len(hits)}"
rec = hits[0]
before = list(rec.get("depends_on", []))
rec["depends_on"] = [d for d in before if d != dep]
assert before != rec["depends_on"], f"dep {dep!r} not present in {event_id!r}: {before}"
timeline_path.write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
print(f"event={event_id} before={before} after={rec['depends_on']}")
