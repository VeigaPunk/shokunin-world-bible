#!/usr/bin/env python3
"""V56 mutual-wait watcher: sample round-97 seat activity every 20s.

Writes to V56-scratch/watch.log a periodic snapshot:
- report counts (R/V) and which R seats are absent
- tail of every poll log under seats/*scratch*/
- sha of every poll script (new/changed scripts get copied to V56-scratch/scripts/)
"""
import hashlib
import json
import shutil
import subprocess
import time
from datetime import datetime
from pathlib import Path

SEATS = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats")
SCRATCH = SEATS / "V56-scratch"
LOG = SCRATCH / "watch.log"
SCRIPTS = SCRATCH / "scripts"
SCRIPTS.mkdir(parents=True, exist_ok=True)

MAX_ITERS = 180  # 180 * 20s = 60 min
seen = {}


def now():
    return datetime.now().strftime("%H:%M:%S")


def sample(i):
    lines = [f"== t={now()} iter={i} =="]
    md = sorted(p.name for p in SEATS.glob("*.md"))
    r = [m for m in md if m.startswith("R") and m[1].isdigit()]
    v = [m for m in md if m.startswith("V")]
    lines.append(f"reports R={len(r)} V={len(v)} total={len(md)}")
    absent_r = [f"R{k}" for k in range(1, 7) if not any(m.startswith(f"R{k}-") for m in r)]
    lines.append(f"absent_producers={absent_r}")
    for d in sorted(SEATS.glob("*scratch*")):
        if d.name == "V56-scratch" or not d.is_dir():
            continue
        for f in sorted(d.glob("poll*.log")) + sorted(d.glob("*poll*.log")):
            try:
                tail = f.read_text(errors="replace").strip().splitlines()
                lines.append(f"  [{d.name}/{f.name}] last={tail[-1] if tail else '<empty>'}")
            except OSError:
                pass
        for f in sorted(d.glob("*.sh")):
            try:
                h = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
            except OSError:
                continue
            key = str(f)
            if seen.get(key) != h:
                seen[key] = h
                dest = SCRIPTS / f"{d.name}__{f.name}.{h}.txt"
                try:
                    shutil.copyfile(f, dest)
                    lines.append(f"  [new/changed script] {d.name}/{f.name} sha={h}")
                except OSError:
                    pass
    # artifact presence
    root = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
    fx = root / "corpus/fixtures/r97-crossing-acknowledgment"
    have = [f.name for f in sorted(fx.glob("*"))] if fx.is_dir() else []
    lines.append(f"r97_fixture_files={len(have)} {have}")
    lines.append("")
    with LOG.open("a") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    for i in range(MAX_ITERS):
        try:
            sample(i)
        except Exception as e:  # keep the watcher alive
            with LOG.open("a") as fh:
                fh.write(f"== t={now()} iter={i} ERROR {e!r} ==\n")
        time.sleep(20)
