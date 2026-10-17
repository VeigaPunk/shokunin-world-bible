#!/usr/bin/env python3
"""V37 adjacency freeze battery — read-only. Run from lane root."""
import hashlib, json, os, subprocess, sys

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "dcb2d92"
HEAD = "60dba0c"
os.chdir(LANE)

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

print("== 1. PROVINCE vs baseline ==")
for cmd in ["git hash-object PROVINCE.md", f"git rev-parse {BASE}:PROVINCE.md",
            "sha256sum PROVINCE.md", f"git show {BASE}:PROVINCE.md | sha256sum",
            f"git diff {BASE} -- PROVINCE.md | wc -c"]:
    r = sh(cmd); print(f"$ {cmd}\n{r.stdout.rstrip()}")

print("\n== 2. tracked diff vs HEAD and vs baseline ==")
print(sh(f"git diff --name-status {HEAD}").stdout)
print(sh(f"git diff --name-status {BASE}").stdout)

print("\n== 3. corpus blob-level comparison vs HEAD ==")
base = sh("git ls-tree -r HEAD --name-only corpus/").stdout.split()
changed, added, missing = [], [], []
for p in base:
    if not os.path.exists(p):
        missing.append(p); continue
    wt = sh(f"git hash-object -- {p}").stdout.strip()
    tr = sh(f"git rev-parse HEAD:{p}").stdout.strip()
    if wt != tr:
        changed.append(p)
# untracked corpus files
unt = sh("git status --porcelain --untracked-files=all").stdout.splitlines()
for line in unt:
    if line.startswith("?? ") and line[3:].startswith("corpus/"):
        added.append(line[3:])
print(f"base corpus files: {len(base)}")
print("CHANGED:", changed)
print("ADDED:", sorted(added))
print("MISSING:", missing)

print("\n== 4. untracked paths outside round dir ==")
roots = {}
for line in unt:
    if line.startswith("?? "):
        p = line[3:]
        roots.setdefault(p.split("/")[0], 0)
        roots[p.split("/")[0]] += 1
print("untracked roots:", roots)
outside = [l for l in unt if l.startswith("?? ") and not l[3:].startswith((".ufo/waves/round-96/", "corpus/"))]
print("outside corpus/ and round-96 wave dir:", outside)

print("\n== 5. hashes of round-96 byte-owned files ==")
for p in ["corpus/tools/map_obligations.py", "corpus/tools/map-obligations-contract.json",
          "corpus/tools/README.md", "corpus/tools/dependency_freeze.py",
          "corpus/tools/dependency-freeze-contract.json",
          "corpus/knowledge/r96-response-scope-note.md",
          "corpus/fixtures/r96-crossing-response/README.md",
          "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
          "corpus/fixtures/r96-crossing-response/sources.json",
          "corpus/fixtures/r96-crossing-response/timeline.json",
          "corpus/fixtures/r96-crossing-response/fictional-excerpts.md"]:
    if os.path.exists(p):
        h = sh(f"sha256sum {p}").stdout.split()[0]
        print(f"{h}  {p}")
    else:
        print(f"ABSENT  {p}")

print("\n== 6. inherited byte copies r95 -> r96 ==")
for f in ["entities.json", "relations.json", "contradictions.json",
          "inspiration-note.md", "source-excerpt.md"]:
    a = f"corpus/fixtures/r95-crossing-aftermath/{f}"
    b = f"corpus/fixtures/r96-crossing-response/{f}"
    if os.path.exists(b):
        print(("IDENTICAL " if open(a,'rb').read() == open(b,'rb').read() else "DIFFER    ") + f)
    else:
        print("ABSENT    " + f)

print("\n== 7. r95 fixture unchanged vs HEAD ==")
r = sh("git diff --stat HEAD -- corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r87-myth-cluster")
print(repr(r.stdout.strip()))

print("\n== 8. rights/canon/mechanics scan over new r96 bytes ==")
import re
pat = re.compile(r"public domain|licen[cs]e|copyright|permission|rights|canon|mechanic|gameplay|ruleset|damage|stats|balancing", re.I)
targets = []
for root, dirs, files in os.walk("corpus/fixtures/r96-crossing-response"):
    for f in files: targets.append(os.path.join(root, f))
targets.append("corpus/knowledge/r96-response-scope-note.md")
hits = 0
for t in targets:
    if not os.path.exists(t): continue
    for i, line in enumerate(open(t, encoding="utf-8"), 1):
        if pat.search(line):
            hits += 1
            print(f"{t}:{i}: {line.rstrip()[:160]}")
print(f"total hits: {hits}")
