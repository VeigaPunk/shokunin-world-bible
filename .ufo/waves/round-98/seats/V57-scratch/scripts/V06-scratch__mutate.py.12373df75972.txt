#!/usr/bin/env python3
"""V06 scratch mutator — V46's exact r97 class: drop one depends_on edge, key stays []."""
import json
import sys

fixture, dep, target = sys.argv[1], sys.argv[2], sys.argv[3]
path = f"{fixture}/timeline.json"
records = json.load(open(path))
for record in records:
    if record.get("id") == target:
        before = list(record.get("depends_on", []))
        record["depends_on"] = [d for d in record["depends_on"] if d != dep]
        after = list(record["depends_on"])
        print(f"event={target} before={before} after={after}")
        break
else:
    sys.exit(f"event {target} not found")
with open(path, "w") as fh:
    json.dump(records, fh, indent=2)
    fh.write("\n")
