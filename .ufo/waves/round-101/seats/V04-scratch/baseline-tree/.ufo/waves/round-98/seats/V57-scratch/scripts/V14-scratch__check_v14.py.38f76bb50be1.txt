#!/usr/bin/env python3
"""V14 anti-overclaim / inheritance harness for r98 clerk-filing."""
import json, os, subprocess, sys, hashlib, re

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
F98 = os.path.join(R, "corpus/fixtures/r98-clerk-filing")
F97 = os.path.join(R, "corpus/fixtures/r97-crossing-acknowledgment")
BASE97 = os.path.join(R, ".ufo/waves/round-98/seats/V14-scratch/base/r97")
BASE95 = os.path.join(R, ".ufo/waves/round-98/seats/V14-scratch/base/r95")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def jload(p):
    return json.load(open(p))

print("== A. byte inheritance r98 vs r97@9a3d648 ==")
for f in ["contradictions.json", "inspiration-note.md", "relations.json", "source-excerpt.md"]:
    a, b = os.path.join(F98, f), os.path.join(BASE97, f)
    same = os.path.exists(a) and open(a, "rb").read() == open(b, "rb").read()
    print(f"  {f}: byte-identical={same}")
    if f == "relations.json":
        print(f"    relations sha r98={sha(a)[:12]} base={sha(b)[:12]}")

print("== A2. all r98 files vs r97 baseline byte status ==")
for f in sorted(os.listdir(BASE97)):
    a = os.path.join(F98, f)
    if not os.path.exists(a):
        print(f"  {f}: MISSING in r98")
        continue
    same = open(a, "rb").read() == open(os.path.join(BASE97, f), "rb").read()
    print(f"  {f}: identical={same}")

print("== B. prefix parsed-equal (inherited rows) ==")
for f, n in [("entities.json", 5), ("sources.json", 6), ("timeline.json", 6)]:
    a, b = jload(os.path.join(F98, f)), jload(os.path.join(BASE97, f))
    print(f"  {f}: r98 len={len(a)} base len={len(b)}; prefix[{n}] parsed-equal={a[:n] == b[:n]}")
    if len(a) > n:
        print(f"    new row(s): {json.dumps(a[n:], ensure_ascii=False)[:600]}")

print("== C. fictional-excerpts append-only ==")
b = open(os.path.join(BASE97, "fictional-excerpts.md"), "rb").read()
a = open(os.path.join(F98, "fictional-excerpts.md"), "rb").read()
print(f"  r98 startswith base bytes: {a.startswith(b)}; base={len(b)}B r98={len(a)}B")
print(f"  appended bytes:\n{a[len(b):].decode('utf-8', 'replace')[:900]}")

print("== D. claim-excerpt-map rows ==")
def rows(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\|\s*(J\d+|S\d+)\s*\|", line)
        if m:
            cells = [c.strip() for c in line.rstrip("\n").strip("|").split("|")]
            out[m.group(1)] = cells
    return out
try:
    m98, m97 = rows(os.path.join(F98, "claim-excerpt-map.md")), rows(os.path.join(BASE97, "claim-excerpt-map.md"))
    print(f"  r97 rows={len(m97)} r98 rows={len(m98)}")
    diffs = []
    for k in sorted(m97):
        if k not in m98:
            diffs.append((k, "MISSING"))
            continue
        c98, c97 = m98[k], m97[k]
        if len(c98) != len(c97):
            diffs.append((k, f"cellcount {len(c97)}->{len(c98)}"))
            continue
        for i, (x, y) in enumerate(zip(c98, c97)):
            if i == 3:  # namespace column may be re-qualified
                continue
            if x != y:
                diffs.append((k, f"col{i}: {y!r} -> {x!r}"))
    print(f"  inherited-row diffs (cols except namespace): {diffs if diffs else 'NONE'}")
    print(f"  new rows: {[k for k in sorted(m98) if k not in m97]}")
    for k in sorted(m98):
        if k not in m97:
            print(f"    {k}: {m98[k]}")
except Exception as e:
    print(f"  map check error: {e}")

print("== E. README counts (r98) ==")
try:
    rd = open(os.path.join(F98, "README.md"), encoding="utf-8").read()
    for pat in ["entities", "relation", "events", "sources", "obligation"]:
        for line in rd.splitlines():
            if pat in line and re.search(r"\d", line):
                print(f"  [{pat}] {line.strip()[:200]}")
                break
except Exception as e:
    print(f"  readme error: {e}")

print("== F. census ==")
n = subprocess.run("ls -d %s/corpus/fixtures/*/ | wc -l" % R, shell=True, capture_output=True, text=True).stdout.strip()
print(f"  fixture dirs: {n}")

print("== G. overclaim grep on new bytes ==")
terms = ["verdict", "ruling", "findings", "finding", "resolution", "resolv", "canon", "rights",
         "permission", "identity", "official", "adjudicat", "authoritativ", "authentic",
         "guilt", "fault", "breach", "winner", "settle", "determin", "declar", "true", "false",
         "binding", "judgment", "judgement", "instituti", "registrar", "certif"]
targets = []
for root, dirs, files in os.walk(F98):
    for f in files:
        targets.append(os.path.join(root, f))
targets += [os.path.join(R, "corpus/knowledge/r98-clerk-scope-note.md"),
            os.path.join(R, "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md"),
            os.path.join(R, "corpus/knowledge/r95-aftermath-scope-note.md"),
            os.path.join(R, "corpus/knowledge/r96-response-scope-note.md")]
for t in targets:
    if not os.path.exists(t):
        print(f"  [absent] {os.path.relpath(t, R)}")
        continue
    lines = open(t, encoding="utf-8").read().splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        for term in terms:
            if term in low:
                hits.append((i, term, line.strip()[:220]))
                break
    print(f"  {os.path.relpath(t, R)}: {len(hits)} lines with flagged terms")
    for h in hits[:40]:
        print(f"    :{h[0]} [{h[1]}] {h[2]}")

print("== H. r95 map repair scope ==")
try:
    b95 = open(os.path.join(BASE95, "claim-excerpt-map.md"), encoding="utf-8").read().splitlines()
    a95 = open(os.path.join(R, "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md"), encoding="utf-8").read().splitlines()
    import difflib
    d = list(difflib.unified_diff(b95, a95, "base", "now", lineterm="", n=1))
    print(f"  diff lines={len(d)}")
    for line in d:
        print(f"    {line[:260]}")
    m95a, m95b = rows(os.path.join(R, "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md")), rows(os.path.join(BASE95, "claim-excerpt-map.md"))
    print(f"  r95 data rows equal: {m95a == m95b} (n={len(m95a)})")
except Exception as e:
    print(f"  r95 error: {e}")
