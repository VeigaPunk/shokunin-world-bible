#!/usr/bin/env python3
"""V53: extract hash-like pins from S5 note files and verify against delivered bytes."""
import re, sys, subprocess, hashlib, os, json

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "9a3d648"
HEX = re.compile(r'\b([0-9a-f]{7,64})\b')
# hash pin forms: `sha256 ` + hex, or bare `abcdef12…`
FILES = sys.argv[1:]

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()

def sha256_git(rev, path):
    p = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=REPO,
                       capture_output=True)
    if p.returncode != 0:
        return None
    return hashlib.sha256(p.stdout).hexdigest()

# Known tool/corpus file names that pins typically refer to
TOOLS = {}
for d in ['corpus/tools', 'corpus/fixtures', 'corpus']:
    full = os.path.join(REPO, d)
    if not os.path.isdir(full):
        continue
    for name in os.listdir(full):
        p = os.path.join(full, name)
        if os.path.isfile(p) and (name.endswith('.py') or name.endswith('.json') or name.endswith('.md')):
            TOOLS.setdefault(name, []).append(os.path.relpath(p, REPO))

out = []
for rel in FILES:
    path = os.path.join(REPO, rel)
    if not os.path.exists(path):
        out.append({'file': rel, 'status': 'MISSING'})
        continue
    text = open(path, encoding='utf-8').read()
    lines = text.splitlines()
    hits = []
    for ln, line in enumerate(lines, 1):
        # find lines that look like they carry a hash pin
        for m in re.finditer(r'`?([0-9a-f]{7,8})…?`?', line):
            tok = m.group(1)
            if len(tok) < 7:
                continue
            ctx = line
            hits.append({'line': ln, 'token': tok, 'context': ctx.strip()})
    out.append({'file': rel, 'sha256': sha256_of(path),
                'git_base_sha256': sha256_git(BASE, rel),
                'hits': hits, 'n_hits': len(hits)})
print(json.dumps(out, indent=1))
