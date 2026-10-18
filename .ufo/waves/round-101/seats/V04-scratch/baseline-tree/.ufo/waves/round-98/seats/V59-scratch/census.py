#!/usr/bin/env python3
"""V59 census replica (r94-r97 convention): fixture dirs, clean/negative, VIOLATION lines."""
import subprocess, sys
from pathlib import Path
ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX = ROOT / "corpus/fixtures"
dirs = sorted(p for p in FIX.iterdir() if p.is_dir())
clean = neg = viol = 0
non01 = []
for d in dirs:
    r = subprocess.run([sys.executable, str(FIX / "check_bible.py"), str(d)],
                       capture_output=True, text=True, env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    v = sum(1 for l in r.stdout.splitlines() if "VIOLATION" in l)
    viol += v
    if r.returncode == 0: clean += 1
    elif r.returncode == 1: neg += 1
    else: non01.append((d.name, r.returncode))
print(f"fixture_dirs={len(dirs)} clean_exit0={clean} negative_exit1={neg} violation_lines={viol} non_0_1={non01}")
