#!/usr/bin/env python3
"""V27 r99 adjacency — whole-tree blob audit vs baseline 4265df5 (batched).

Tracked files outside .ufo/: worktree blob hash vs baseline blob hash.
Usage: audit_tree.py <outdir>
"""
import subprocess, sys, os

BASE = "4265df5"
REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)

def run(args, **kw):
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True, **kw)

# baseline blob map: one ls-tree call
base = {}
for line in run(["git", "ls-tree", "-r", BASE]).stdout.splitlines():
    meta, path = line.split("\t", 1)
    mode, typ, blob = meta.split()
    if not path.startswith(".ufo/"):
        base[path] = blob

paths = sorted(base)
existing = [p for p in paths if os.path.exists(os.path.join(REPO, p))]
missing = [p for p in paths if p not in set(existing)]
# batch hash-object for worktree files
hashes = {}
if existing:
    proc = run(["git", "hash-object", "--stdin-paths"], input="\n".join(existing) + "\n")
    out = proc.stdout.splitlines()
    hashes = dict(zip(existing, out))

changed = [(p, base[p], hashes[p]) for p in existing if hashes.get(p) != base[p]]

por = run(["git", "status", "--porcelain", "-uall"]).stdout
untracked = [l[3:] for l in por.splitlines() if l.startswith("?? ") and not l.startswith("?? .ufo/")]
staged = [l for l in por.splitlines() if l[:1] not in (" ", "?")]
deleted = [l[3:] for l in por.splitlines() if l.startswith(" D ")]
modified_ufo = [l[3:] for l in por.splitlines() if l.startswith(" M ") and l[3:].startswith(".ufo/")]

with open(os.path.join(outdir, "tree-audit.txt"), "w") as f:
    f.write(f"baseline non-ufo tracked files: {len(paths)}\n")
    f.write(f"CHANGED ({len(changed)}):\n")
    for p, b, w in changed:
        f.write(f"  {p}  base={b[:12]} work={w[:12]}\n")
    f.write(f"ADDED-UNTRACKED non-ufo ({len(untracked)}):\n")
    for p in untracked:
        f.write(f"  {p}\n")
    f.write(f"MISSING ({len(missing)}): {missing}\n")
    f.write(f"STAGED: {staged}\nWORKTREE-DELETED: {deleted}\nMODIFIED-.ufo-tracked: {modified_ufo}\n")
print(f"changed={len(changed)} untracked_nonufo={len(untracked)} missing={len(missing)} staged={len(staged)} deleted={len(deleted)}")
for p, b, w in changed:
    print("  CHANGED", p, b[:12], "->", w[:12])
for p in untracked:
    print("  UNTRACKED", p)
