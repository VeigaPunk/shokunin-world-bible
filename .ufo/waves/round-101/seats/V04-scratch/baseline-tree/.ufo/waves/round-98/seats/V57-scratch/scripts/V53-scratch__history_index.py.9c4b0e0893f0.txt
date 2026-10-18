#!/usr/bin/env python3
"""Build a prefix->(rev,path) index over ALL blobs ever committed for a set of paths,
so a non-matching pin can be classified as historical (matched a prior revision)
vs. fabricated/never-delivered."""
import subprocess, hashlib, json, sys, os

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"

def git(*args):
    return subprocess.run(['git'] + list(args), cwd=REPO, capture_output=True)

def blobs_for(path):
    """All distinct blob hashes for a path across all commits."""
    p = git('log', '--all', '--pretty=format:%H', '--', path)
    revs = [r for r in p.stdout.decode().splitlines() if r]
    seen = {}
    for rev in revs:
        ls = git('ls-tree', rev, path)
        if ls.returncode != 0 or not ls.stdout.strip():
            continue
        blob = ls.stdout.decode().split()[2]
        if blob in seen:
            continue
        cat = git('cat-file', '-p', blob)
        if cat.returncode != 0:
            continue
        h = hashlib.sha256(cat.stdout).hexdigest()
        seen[blob] = {'sha256': h, 'rev': rev[:8]}
    return seen

paths = sys.argv[1:]
idx = {}
for path in paths:
    for blob, meta in blobs_for(path).items():
        idx.setdefault(meta['sha256'][:8], []).append(
            {'path': path, 'rev': meta['rev'], 'sha256': meta['sha256'][:16]})
print(json.dumps(idx, indent=1, sort_keys=True))
