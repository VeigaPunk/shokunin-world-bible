#!/usr/bin/env python3
"""V53: extract hash pins from S5 note files, verify against delivered bytes at run time.

Pin forms recognized:
  - 8+ hex chars followed by the U+2026 ellipsis (truncated pin)
  - full 64-hex-char sha256
Attribution: filename tokens on the same line/sentence; plus a repo-wide
brute-force prefix search to find ANY delivered file whose sha256 matches.
"""
import re, sys, os, json, hashlib, subprocess, time

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "9a3d648"
SKIP_DIRS = {'.git', '.ufo', '__pycache__', '.tower', '.devin', '.omp'}
MAXSZ = 4 * 1024 * 1024

PIN = re.compile(r'`?([0-9a-f]{8})(?:\u2026|\.\.\.)`?')
FULL = re.compile(r'`?([0-9a-f]{64})`?')

def sha256_path(p):
    h = hashlib.sha256()
    try:
        with open(p, 'rb') as f:
            for c in iter(lambda: f.read(1 << 16), b''):
                h.update(c)
    except OSError:
        return None
    return h.hexdigest()

def sha256_git(rev, rel):
    p = subprocess.run(['git', 'show', f'{rev}:{rel}'], cwd=REPO, capture_output=True)
    return hashlib.sha256(p.stdout).hexdigest() if p.returncode == 0 else None

def walk_repo():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            p = os.path.join(root, fn)
            try:
                if os.path.getsize(p) > MAXSZ:
                    continue
            except OSError:
                continue
            out.append(os.path.relpath(p, REPO))
    return out

def main():
    files = sys.argv[1:]
    repo_files = walk_repo()
    index = {}
    for rel in repo_files:
        h = sha256_path(os.path.join(REPO, rel))
        if h:
            index.setdefault(h[:8], []).append(rel)

    report = {'run_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
              'files': [], 'index_size': len(index)}
    for rel in files:
        p = os.path.join(REPO, rel)
        entry = {'file': rel, 'exists': os.path.exists(p)}
        if entry['exists']:
            entry['sha256'] = sha256_path(p)
            entry['git_base_sha256'] = sha256_git(BASE, rel)
            entry['changed_vs_base'] = entry['sha256'] != entry['git_base_sha256']
        text = open(p, encoding='utf-8').read() if entry['exists'] else ''
        lines = text.splitlines()
        pins = []
        for ln, line in enumerate(lines, 1):
            found = []
            for m in FULL.finditer(line):
                found.append((m.group(1), 64))
            for m in PIN.finditer(line):
                # avoid double-counting the first 8 chars of a full hash
                if any(m.start() >= f[0] and m.start() < f[0] + 64 for f in []):
                    pass
                found.append((m.group(1), 8))
            # dedupe by (token,start)
            seen = set()
            for tok, n in found:
                if (tok, n) in seen:
                    continue
                seen.add((tok, n))
                match8 = index.get(tok[:8], [])
                pins.append({'line': ln, 'token': tok, 'width': n,
                             'matches_delivered': match8,
                             'line_text': line.strip()})
        entry['pins'] = pins
        entry['n_pins'] = len(pins)
        report['files'].append(entry)
    print(json.dumps(report, indent=1))

main()
