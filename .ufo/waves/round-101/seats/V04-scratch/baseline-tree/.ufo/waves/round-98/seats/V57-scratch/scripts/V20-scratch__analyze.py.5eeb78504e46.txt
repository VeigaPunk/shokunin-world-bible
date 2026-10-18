#!/usr/bin/env python3
"""V20 scope-creep analyzer (round 98). Read-only snapshots under V20-scratch/snap/."""
import json, re, subprocess, sys, os
from pathlib import Path

R = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SNAP = R / ".ufo/waves/round-98/seats/V20-scratch/snap"
SNAP.mkdir(parents=True, exist_ok=True)
label = sys.argv[1] if len(sys.argv) > 1 else "scan"

def run(args, cwd=R):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)

def save(name, text):
    (SNAP / f"{name}-{label}.txt").write_text(text)

# 1. porcelain -uall
por = run(["git", "status", "--porcelain", "-uall"]).stdout
save("porcelain", por)
lines = [l for l in por.splitlines() if l.strip()]

# buckets
def bucket(path):
    p = path
    if p == "LOG.md": return "B0-orchestrator-declaration"
    if p == "corpus/tools/dependency_freeze.py": return "B1a-S1-freeze-tool"
    if p == "corpus/tools/dependency-freeze-contract.json": return "B1a-S1-freeze-contract"
    if p == "corpus/tools/README.md": return "B1b-S2-tools-readme"
    if p == "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md": return "B1c-S3-r95-map-repair"
    if p.startswith("corpus/fixtures/r98-clerk-filing/"): return "B1d-S3S4-r98-fixture"
    if p == "corpus/knowledge/r98-clerk-scope-note.md": return "B1e-S5-r98-note"
    if p in ("corpus/knowledge/r95-aftermath-scope-note.md", "corpus/knowledge/r96-response-scope-note.md"): return "B1e-S5-addenda"
    if p.startswith(".ufo/waves/round-98/"): return "B2-seat-reports-scratch"
    if p.startswith(".ufo/interactive-sessions/"): return "IGN-interactive"
    return "OTHER"

counts = {}
others = []
for l in lines:
    xy, p = l[:2], l[3:]
    if p.endswith("/") and "->" not in p: pass
    if " -> " in p: p = p.split(" -> ")[-1]
    b = bucket(p)
    counts[b] = counts.get(b, 0) + 1
    if b == "OTHER": others.append(l)
save("buckets", json.dumps(counts, indent=2, sort_keys=True) + "\nOTHER:\n" + "\n".join(others))

# 2. tracked diff
save("diff-name-status", run(["git", "diff", "--name-status"]).stdout)
save("diff-cached", run(["git", "diff", "--cached", "--name-status"]).stdout)
save("diff-stat", run(["git", "diff", "--stat"]).stdout)
save("log-head", run(["git", "log", "--oneline", "-4"]).stdout)

# 3. report exclusivity
SEATS = R / ".ufo/waves/round-98/seats"
mds = sorted(SEATS.glob("*.md"))
save("seats-files", "\n".join(p.name for p in sorted(SEATS.iterdir())) + "\n")
pat = re.compile(r"^(S[1-5]|V\d{2})-[A-Za-z0-9._-]+\.md$")
mism = [p.name for p in mds if not pat.match(p.name)]
# content seat-id check
content_mism = []
for p in mds:
    try: head = p.read_text(errors="replace")[:1500]
    except Exception as e: head = f"<read error {e}>"
    m = pat.match(p.name)
    if m:
        sid = m.group(1)
        if sid not in head: content_mism.append(p.name)
save("excl", f"reports={len(mds)}\npattern_mismatch={mism}\nheader_seat_mismatch={content_mism}\n")
# cross-scratch report-pattern files with mismatched owner
cross = []
for d in SEATS.iterdir():
    if not d.is_dir(): continue
    own = re.match(r"^([A-Za-z0-9]+)-", d.name)
    own = own.group(1) if own else None
    for f in d.rglob("*.md"):
        m = pat.match(f.name)
        if m and m.group(1) != own:
            cross.append(f"{d.name}/{f.relative_to(d)}")
save("excl-cross", f"cross_scratch_mismatch={cross}\n")
# report-like md elsewhere in repo (mtime newer than round start), excluding seats/
start = 1792279200  # 2026-10-17 20:20:00 -0300
elsewhere = []
for f in R.rglob("*.md"):
    if "/.git/" in str(f) or str(f).startswith(str(SEATS)): continue
    if str(f).startswith(str(R / ".ufo/interactive-sessions")): continue
    try:
        if f.stat().st_mtime > start: elsewhere.append(f"{f.relative_to(R)}")
    except OSError: pass
save("elsewhere-md", "\n".join(sorted(elsewhere)) + "\n")

# 4. pycache
pyc = run(["find", ".", "-name", "__pycache__", "-type", "d", "-newermt", "2026-10-17 20:20"]).stdout
pyc_all = run(["find", ".", "-name", "__pycache__", "-type", "d"]).stdout
pyc_new = run(["find", ".", "-name", "*.pyc", "-newermt", "2026-10-17 20:20"]).stdout
save("pycache", f"== new dirs (>20:20) ==\n{pyc}\n== all dirs ==\n{pyc_all}\n== new pyc ==\n{pyc_new}")
save("pycache-corpus", run(["find", "corpus", "-name", "*.pyc", "-o", "-name", "__pycache__"]).stdout)

# 5. self-test dirs / transients at repo root
selftest = run(["find", ".", "-maxdepth", "2", "-name", "*-self-test-*"]).stdout
save("selftest", selftest)
trans = run(["find", ".", "-maxdepth", "1", "-newermt", "2026-10-17 20:20", "-not", "-name", ".git"]).stdout
save("root-new", trans)

# 6. parent-tree snapshot + lore-signature scan
par = run(["find", ".", "-maxdepth", "4", "-mindepth", "1", "-not", "-path", "./lore-shokunin*", "-not", "-path", "*/.git/*", "-not", "-name", ".git", "-printf", "%T@ %p\n"], cwd=R.parent).stdout
save("parent-full", par)
sig = run(["find", ".", "-maxdepth", "6", "-not", "-path", "./lore-shokunin*", "-not", "-path", "*/.git/*",
           "(", "-name", "*crossing*", "-o", "-name", "claim-excerpt-map.md", "-o", "-name", "dependency_freeze.py",
           "-o", "-name", "map_obligations.py", "-o", "-name", "*-contract.json", "-o", "-name", "r98-*", "-o", "-name", "clerk-*", ")",
           "-newermt", "2026-10-17 20:20"], cwd=R.parent).stdout
save("parent-sig", sig)
ps = run(["git", "status", "--porcelain", "-uall"], cwd=R.parent).stdout
save("parent-status", ps)

# 7. r98 fixture listing
fix = R / "corpus/fixtures/r98-clerk-filing"
if fix.exists():
    save("fixture-listing", "\n".join(f"{p.name}\t{p.stat().st_size}" for p in sorted(fix.iterdir())) + "\n")
print(f"[{label}] buckets={json.dumps(counts, sort_keys=True)} OTHER={len(others)} reports={len(mds)}")
for o in others[:10]: print("OTHER:", o)
