#!/usr/bin/env python3
"""Blob audit: worktree vs 4265df5, excluding .ufo. Writes nothing but stdout."""
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = "4265df5"


def git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return r.stdout


base_files = [
    line
    for line in git("ls-tree", "-r", "--name-only", BASE).splitlines()
    if line and not line.startswith(".ufo/")
]
changed = []
missing = []
for path in base_files:
    p = ROOT / path
    if not p.is_file():
        missing.append(path)
        continue
    work = subprocess.run(
        ["git", "hash-object", str(p)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    base = git("rev-parse", f"{BASE}:{path}").strip()
    if work != base:
        changed.append((path, base, work))

status = subprocess.run(
    ["git", "status", "--porcelain", "-uall"],
    cwd=ROOT,
    check=True,
    capture_output=True,
    text=True,
).stdout
untracked = []
for line in status.splitlines():
    if line.startswith("?? "):
        path = line[3:]
        if not path.startswith(".ufo/"):
            untracked.append(path)

print(f"baseline non-ufo tracked files: {len(base_files)}")
print(f"CHANGED ({len(changed)}):")
for path, base, work in changed:
    print(f"  {path}  {base[:12]} -> {work[:12]}")
print(f"MISSING ({len(missing)}):")
for path in missing:
    print(f"  {path}")
print(f"UNTRACKED non-ufo ({len(untracked)}):")
for path in untracked:
    print(f"  {path}")
