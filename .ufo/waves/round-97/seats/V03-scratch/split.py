#!/usr/bin/env python3
"""Split a V03 battery.txt into per-label section files for cmp."""
import sys, os, hashlib, pathlib
src = pathlib.Path(sys.argv[1])
outdir = src.parent / "sections"
outdir.mkdir(exist_ok=True)
label = None
buf = []
files = []
for line in src.read_text().splitlines(keepends=True):
    if line.startswith("=== ") and line.rstrip().endswith(" ==="):
        if label:
            p = outdir / (label + ".out")
            p.write_text("".join(buf)); files.append(p)
        label = line.strip().strip("= ").strip().replace(" ", "_")
        buf = [line]
    else:
        buf.append(line)
if label:
    p = outdir / (label + ".out")
    p.write_text("".join(buf)); files.append(p)
for p in sorted(files):
    print(hashlib.sha256(p.read_bytes()).hexdigest(), p.name)
