"""Summarize V32 poll.log: first non-baseline + last-change + final value per tracked var."""
import re, sys

BASELINE = {
    "s1t": "b06275f3", "s1c": "27273be2", "s2": "8678abc1", "s3m": "30281ff1",
    "s5a": "ABSENT", "s5b": "f87ed42a", "s5c": "6db32ca2",
    "fxh": "NA", "prods": "0", "seats": "0", "fleet": "no", "fx": "0",
}

path = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V32-scratch/poll.log"
rows = []
for line in open(path):
    parts = line.split()
    if len(parts) < 4 or parts[0] == "POLL":
        continue
    i, ts = int(parts[0]), parts[1]
    d = {}
    for kv in parts[2:]:
        if "=" in kv:
            k, v = kv.split("=", 1)
            d[k] = v
    rows.append((i, ts, d))

print(f"samples: {len(rows)}; first {rows[0][1]}; last {rows[-1][1]}")
for var, base in BASELINE.items():
    first = None
    last_change = None
    prev = None
    for i, ts, d in rows:
        v = d.get(var)
        if first is None and v != base:
            first = (i, ts, v)
        if prev is not None and v != prev:
            last_change = (i, ts, v)
        prev = v
    final = rows[-1][2].get(var)
    fc = f"{last_change[2]} @s{last_change[0]} {last_change[1]}" if last_change else "n/a"
    fi = f"{first[2]} @s{first[0]} {first[1]}" if first else f"baseline through s{rows[-1][0]}"
    print(f"{var:6s} base={base:8s} first={fi:28s} lastchange={fc:28s} final={final}")
