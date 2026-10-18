#!/usr/bin/env python3
"""Copy a fixture dir and drop one depends_on member from one event (BR-01 class).

Usage: mutate.py <src_fixture> <dst_fixture> <event_id> <dep_id>
Keeps the depends_on key present (empty list), mirroring the r96/r97 self-test mechanics.
"""
import json
import shutil
import sys
from pathlib import Path


def main():
    src, dst, event_id, dep_id = sys.argv[1:5]
    shutil.copytree(src, dst)
    path = Path(dst) / "timeline.json"
    rows = json.loads(path.read_text())
    hit = False
    for row in rows:
        if row.get("id") == event_id:
            before = list(row["depends_on"])
            row["depends_on"] = [d for d in row["depends_on"] if d != dep_id]
            after = list(row["depends_on"])
            hit = True
            print(f"event={event_id} before={before} after={after}")
    if not hit:
        sys.exit(f"event {event_id!r} not found in {path}")
    path.write_text(json.dumps(rows, indent=2) + "\n")


if __name__ == "__main__":
    main()
