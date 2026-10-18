#!/usr/bin/env python3
"""Definitive: hash every blob reachable from all refs; report which of the target
prefixes ever existed as committed content anywhere in the repo."""
import subprocess, hashlib, sys, collections

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
targets = sys.argv[1:]

def git(*a):
    return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True)

oids = git('rev-list', '--all', '--objects').stdout.decode().splitlines()
blob_oids = []
for line in oids:
    parts = line.split(' ', 1)
    if len(parts) == 2:
        blob_oids.append((parts[0], parts[1]))

# batch-check types
p = subprocess.run(['git', 'cat-file', '--batch-check=%(objectname) %(objecttype)'],
                   cwd=REPO, input='\n'.join(o for o, _ in blob_oids).encode(),
                   capture_output=True)
types = {}
for line in p.stdout.decode().splitlines():
    oid, t = line.split()
    types[oid] = t

hits = collections.defaultdict(list)
nblobs = 0
for oid, path in blob_oids:
    if types.get(oid) != 'blob':
        continue
    nblobs += 1
    content = git('cat-file', '-p', oid).stdout
    h = hashlib.sha256(content).hexdigest()
    for t in targets:
        if h.startswith(t):
            hits[t].append({'path': path, 'oid': oid[:12], 'sha256': h[:16]})

print('blobs scanned:', nblobs)
for t in targets:
    print(f'{t}: {len(hits[t])} hit(s)')
    for h in hits[t][:5]:
        print('   ', h)
