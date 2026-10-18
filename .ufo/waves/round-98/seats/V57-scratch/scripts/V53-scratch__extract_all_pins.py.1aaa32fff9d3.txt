#!/usr/bin/env python3
"""V53: catch ALL hash-like tokens: backticked (with optional trailing U+2026 ellipsis)
plus bare 64-hex tokens (code-block sha256sum output)."""
import re, sys, os, hashlib, json, time

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SKIP = {'.git', '__pycache__'}
BT = re.compile(r'`([0-9a-f]{7,64})(?:\u2026|\.\.\.)?`')
BARE64 = re.compile(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])')

def sha256_path(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 16), b''):
            h.update(c)
    return h.hexdigest()

def walk():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for fn in files:
            p = os.path.join(root, fn)
            try:
                if os.path.getsize(p) > 4 * 1024 * 1024:
                    continue
            except OSError:
                continue
            out.append(os.path.relpath(p, REPO))
    return out

def main():
    files = sys.argv[1:]
    idx = {}
    for rel in walk():
        try:
            h = sha256_path(os.path.join(REPO, rel))
        except OSError:
            continue
        idx.setdefault(h[:8], []).append(rel)
    out = {'run_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'files': []}
    for rel in files:
        p = os.path.join(REPO, rel)
        sh = sha256_path(p)
        e = {'file': rel, 'sha256': sh, 'sha256_8': sh[:8], 'pins': []}
        lines = open(p, encoding='utf-8').read().splitlines()
        for ln, line in enumerate(lines, 1):
            seen = set()
            for rx, kind in ((BT, 'backtick'), (BARE64, 'bare64')):
                for m in rx.finditer(line):
                    t = m.group(1)
                    if (t, m.start()) in seen:
                        continue
                    seen.add((t, m.start()))
                    e['pins'].append({'line': ln, 'token': t, 'width': len(t),
                                      'kind': kind,
                                      'delivered_match': idx.get(t[:8], []),
                                      'line_text': line.strip()[:300]})
        out['files'].append(e)
    print(json.dumps(out, indent=1))

main()
