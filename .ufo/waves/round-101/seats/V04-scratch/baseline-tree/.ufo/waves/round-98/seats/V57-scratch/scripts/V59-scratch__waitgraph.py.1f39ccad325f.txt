#!/usr/bin/env python3
"""r98 wait-graph (maxdepth 2 only): parse seat poll scripts -> edges -> mutual pairs."""
import re, sys
from pathlib import Path
ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SEATS = ROOT / ".ufo/waves/round-98/seats"
files = [p for p in SEATS.glob("*scratch*/*.sh")] + [p for p in SEATS.glob("scratch/*.sh")]
edges = {}
for p in sorted(files):
    seat = p.parent.name.split("-")[0]
    if seat == "scratch": seat = "V02?"  # scratch/V02-poll.sh
    txt = p.read_text(errors="replace")
    waited = sorted(set(re.findall(r'\b(V\d{2}|S[1-5])\b', txt)))
    waited = [w for w in waited if w != seat]
    if waited:
        edges.setdefault(seat, set()).update(waited)
        print(f"{seat:5s} {p.name:18s} waits_on={waited}")
print("\n=== mutual pairs (A->B and B->A) ===")
mut = []
for a, bs in edges.items():
    for b in bs:
        if b in edges and a in edges[b]:
            mut.append(tuple(sorted((a,b))))
mut = sorted(set(mut))
print(mut if mut else "none")

# all-reports waiters: scripts that count seats/*.md (not naming seats)
print("\n=== all-reports waiters (count seats/*.md) ===")
for p in sorted(files):
    txt = p.read_text(errors="replace")
    if re.search(r'seats/\*\.md|\*\.md.*wc -l|nonself', txt) and re.search(r'ge 6[0-9]|-ge 5[0-9]|nonself', txt):
        print(f"  {p.parent.name.split('-')[0]:5s} {p.name}")
