#!/usr/bin/env python3
"""V24 scratch: byte-compare r96-crossing-response against r95-crossing-aftermath blobs at dcb2d92."""
import hashlib
import subprocess
from pathlib import Path

BASE = "dcb2d92"
OLD = "corpus/fixtures/r95-crossing-aftermath"
NEW = "corpus/fixtures/r96-crossing-response"

old_files = sorted(
    p for p in subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASE, OLD + "/"], text=True
    ).splitlines()
)
new_files = sorted(p.name for p in Path(NEW).iterdir() if p.is_file())

print(f"baseline files ({OLD}): {len(old_files)}")
print(f"new files ({NEW}): {len(new_files)}")
print("only_in_new:", sorted(set(new_files) - {Path(p).name for p in old_files}))
print("only_in_old:", sorted({Path(p).name for p in old_files} - set(new_files)))
print()

for name in sorted(set(new_files) & {Path(p).name for p in old_files}):
    blob = subprocess.check_output(["git", "cat-file", "blob", f"{BASE}:{OLD}/{name}"])
    old_sha = hashlib.sha256(blob).hexdigest()
    new_sha = hashlib.sha256(Path(f"{NEW}/{name}").read_bytes()).hexdigest()
    verdict = "IDENTICAL" if old_sha == new_sha else "DIFFERS"
    print(f"{verdict:9} {name}")
    print(f"  old {old_sha}")
    print(f"  new {new_sha}")
