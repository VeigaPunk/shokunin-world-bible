#!/bin/sh
# Counts for a lore fixture directory
D="$1"
python3 - "$D" <<'PY'
import json, sys, re
from pathlib import Path
d = Path(sys.argv[1])
for name in ("entities", "relations", "timeline", "sources", "contradictions"):
    p = d / (name + ".json")
    try:
        rows = json.loads(p.read_text(encoding="utf-8"))
        print(f"{name}: {len(rows)}")
    except Exception as e:
        print(f"{name}: ERROR {e}")
mp = d / "claim-excerpt-map.md"
if mp.exists():
    text = mp.read_text(encoding="utf-8")
    m = re.search(r"\*\*Expected inventory:\*\*\s*(.*)", text)
    print("inventory line:", m.group(1) if m else "MISSING")
PY
