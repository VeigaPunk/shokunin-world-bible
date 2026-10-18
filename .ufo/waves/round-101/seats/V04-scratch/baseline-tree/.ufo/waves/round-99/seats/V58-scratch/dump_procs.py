#!/usr/bin/env python3
"""Dump round-99 poller cmdlines into V58-scratch/procs/ for offline classification.

Read-only of /proc. Writes only under V58-scratch.
"""
import os
import re

OUT = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V58-scratch/procs"
os.makedirs(OUT, exist_ok=True)
# clear previous dumps
for name in os.listdir(OUT):
    os.remove(os.path.join(OUT, name))

n = 0
for pid in os.listdir("/proc"):
    if not pid.isdigit():
        continue
    try:
        raw = open(f"/proc/{pid}/cmdline", "rb").read()
    except OSError:
        continue
    if b"round-99" not in raw:
        continue
    text = raw.replace(b"\x00", b"\n").decode("utf-8", "replace")
    # skip this dumper and the sampler if we only want others? keep all, tag them.
    seat = "?"
    m = re.search(r"round-99/seats/(S[1-5]|V\d{2,3})-scratch", text)
    if m:
        seat = m.group(1)
    else:
        m = re.search(r"\b(V\d{2,3}|S[1-5])\b", text)
        if m:
            seat = m.group(1)
    # skip kernel-short sleepers that are just `sleep 20` children? keep if round-99
    path = os.path.join(OUT, f"{seat}__{pid}.txt")
    # avoid clobber if two
    i = 0
    while os.path.exists(path):
        i += 1
        path = os.path.join(OUT, f"{seat}__{pid}_{i}.txt")
    with open(path, "w") as f:
        f.write(text)
    n += 1
print(f"dumped={n} dir={OUT}")
