#!/usr/bin/env python3
"""V15 c2-ordering: report tick sequence and depends_on backward-ness for a fixture."""
import json
import sys
from pathlib import Path

for arg in sys.argv[1:]:
    d = Path(arg)
    tl = json.loads((d / 'timeline.json').read_text(encoding='utf-8'))
    by_id = {r['id']: r for r in tl}
    print(f"--- {d}")
    print("ids/tick:", ", ".join(f"{r['id']}={r['tick']}" for r in tl))
    print("tick-sequence:", [r['tick'] for r in tl])
    bad = []
    for r in tl:
        for dep in r['depends_on']:
            if dep not in by_id:
                bad.append(f"{r['id']}: unknown dep {dep}")
                continue
            dt, rt = by_id[dep]['tick'], r['tick']
            if not (dt < rt):
                bad.append(f"{r['id']}(tick {rt}): dep {dep}(tick {dt}) NOT strictly backward")
    print("backward-check:", "OK all deps strictly backward" if not bad else "; ".join(bad))
    print("edges:", ", ".join(f"{dep}->{r['id']}" for r in tl for dep in r['depends_on']))
