#!/usr/bin/env python3
"""Compare V03 baseline vs delivered battery sections + extract key counts/exits."""
import pathlib, hashlib, sys, re

S = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V03-scratch')
base = S / 'baseline' / 'sections'
deliv = S / 'delivered' / 'sections'

def parse(p):
    t = p.read_text()
    lines = t.splitlines(keepends=True)
    body = "".join(lines[2:])
    m = re.search(r'EXIT=(\d+)\s*$', body)
    exit_code = m.group(1) if m else '?'
    return body.rsplit("EXIT=", 1)[0], exit_code

names = sorted({p.name for p in base.glob('*.out')} | {p.name for p in deliv.glob('*.out')})
for n in names:
    bp, dp = base / n, deliv / n
    if not bp.exists():
        print(f"NEW      {n}"); continue
    if not dp.exists():
        print(f"MISSING  {n}"); continue
    bb, be = parse(bp)
    db, de = parse(dp)
    same = "SAME" if bb == db else "DIFF"
    print(f"{same}  {n:48s} exit {be}->{de}  sha {hashlib.sha256(bb.encode()).hexdigest()[:12]} -> {hashlib.sha256(db.encode()).hexdigest()[:12]}")

print("\n--- key receipts (delivered) ---")
for n in names:
    dp = deliv / n
    if not dp.exists():
        continue
    body, exit_code = parse(dp)
    if n.startswith('map-') and not n.startswith('map-frozen'):
        obl = re.search(r'OBLIGATIONS raw=(\d+) mapped=(\d+)', body)
        inv = re.search(r'INVENTORY JSON-FACTS (\S+); EDITORIAL-ROWS (\S+); TOTAL-ROWS (\S+)', body)
        res = re.search(r'RESULT (\w+)', body)
        print(f"{n:48s} raw/mapped={obl.groups() if obl else None} inv={inv.groups() if inv else None} {res.group(1) if res else '?'} exit={exit_code}")
