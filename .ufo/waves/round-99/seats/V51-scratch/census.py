#!/usr/bin/env python3
"""V51 census: repo-relative check_bible over every fixture dir. Read-only."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
checker = ROOT / "corpus/fixtures/check_bible.py"
dirs = sorted(p for p in (ROOT / "corpus/fixtures").iterdir() if p.is_dir())
clean = neg = 0
viol = 0
other = []
for d in dirs:
    r = subprocess.run(
        [sys.executable, str(checker), str(d.relative_to(ROOT))],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    text = r.stdout + r.stderr
    vlines = [ln for ln in text.splitlines() if "VIOLATION" in ln]
    viol += len(vlines)
    if r.returncode == 0:
        clean += 1
    elif r.returncode == 1:
        neg += 1
    else:
        other.append((d.name, r.returncode, text[:200]))
out = {
    "fixture_dirs": len(dirs),
    "clean_exit0": clean,
    "negative_exit1": neg,
    "violation_lines": viol,
    "non_0_1_exits": other,
}
print(json.dumps(out, indent=2))
sys.exit(0 if not other else 3)
