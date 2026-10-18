#!/usr/bin/env python3
"""V58 presence-final: gather liveness evidence for seats whose reports are absent
at the escape snapshot. Read-only. Prints a compact report."""
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta

SEATS = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats"
EXPECTED = [f"S{i}" for i in range(1, 6)] + [f"V{i:02d}" for i in range(1, 60)]

def main():
    missing = sys.argv[1:] or []
    if not missing:
        present = set()
        for n in os.listdir(SEATS):
            if n.endswith(".md"):
                present.add(n.split("-", 1)[0])
        missing = [s for s in EXPECTED if s not in present]
    print("MISSING:", " ".join(missing) if missing else "(none)")
    for s in missing:
        scratch = os.path.join(SEATS, f"{s}-scratch")
        print(f"--- {s} ---")
        if not os.path.isdir(scratch):
            print(f"  scratch dir: ABSENT ({scratch})")
            continue
        entries = []
        for root, dirs, files in os.walk(scratch):
            for fn in files:
                p = os.path.join(root, fn)
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                entries.append((st.st_mtime, st.st_size, p))
        entries.sort(reverse=True)
        for mt, sz, p in entries[:6]:
            t = datetime.fromtimestamp(mt, timezone(timedelta(hours=-3))).strftime("%H:%M:%S")
            print(f"  {t} {sz:>8} {os.path.relpath(p, SEATS)}")
        # poll logs: last 2 lines of any *poll*.log / *poll*.txt
        for root, dirs, files in os.walk(scratch):
            for fn in files:
                if "poll" in fn and fn.endswith((".log", ".txt")):
                    p = os.path.join(root, fn)
                    try:
                        with open(p, encoding="utf-8", errors="replace") as f:
                            lines = f.read().splitlines()
                    except OSError:
                        continue
                    tail = lines[-2:] if lines else []
                    print(f"  tail[{os.path.relpath(p, SEATS)}]: {' | '.join(tail)}")

if __name__ == "__main__":
    main()
