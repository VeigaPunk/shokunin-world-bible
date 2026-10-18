#!/usr/bin/env python3
"""Live r99 wait edges only. Archives, mirrors, and baseline copies excluded."""
import re
from pathlib import Path

root = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats")
SKIP_PARTS = {
    "archive", "mirror", "work", "base", "baseline", "baseline-r98",
    "negctl", "snap", "__pycache__", "midwrite", "before", "pre",
    "r98-tools", "scripts",
}

def skip(path: Path) -> bool:
    for part in path.parts:
        low = part.lower()
        if part in SKIP_PARTS or low.startswith("baseline") or "mirror" in low or "archive" in low:
            return True
    return False

def owner_of(path: Path) -> str | None:
    for part in path.relative_to(root).parts:
        m = re.match(r"^(S[1-5]|V\d{1,3})(?:-|$)", part)
        if m:
            return m.group(1)
    return None

scripts = []
for p in root.rglob("*"):
    if not p.is_file():
        continue
    if skip(p):
        continue
    if p.suffix not in {".sh", ".py"}:
        continue
    name = p.name.lower()
    if not any(k in name for k in ("poll", "wait", "watch", "audit", "sampler")):
        continue
    scripts.append(p)

SEAT = re.compile(r"\b(S[1-5]|V\d{2,3})\b")
owner_waits = {}
rows = []
allrep = []

for p in sorted(scripts):
    owner = owner_of(p)
    text = p.read_text(errors="replace")
    low = text.lower()
    awaited = set()
    # explicit report-path waits
    for m in re.finditer(r"(S[1-5]|V\d{2,3})(?:-[A-Za-z0-9_-]+)?\.md", text):
        sid = m.group(1)
        if sid != owner:
            awaited.add(sid)
    for m in re.finditer(r"\$\{?SEATS\}?/(S[1-5]|V\d{2,3})", text):
        sid = m.group(1)
        if sid != owner:
            awaited.add(sid)
    for m in re.finditer(r"name ['\"](S[1-5]|V\d{2,3})", text):
        sid = m.group(1)
        if sid != owner:
            awaited.add(sid)
    # numeric all-reports threshold
    thresh = re.findall(r"(?:-ge|-gt|>=)\s*(\d+)", text)
    thresh += re.findall(r"\b(12[0-8]|11[0-9])\b", text)
    is_all = False
    if any(int(t) >= 100 for t in thresh if t.isdigit()):
        if "report" in low or ".md" in low:
            is_all = True
    if "nonself" in low or "subtract self" in low or "subtract-self" in low:
        is_all = True
    # producer-all is not all-reports
    rel = str(p.relative_to(root))
    rows.append((owner, sorted(awaited), is_all, rel, sorted(set(thresh))[:8]))
    owner_waits.setdefault(owner, set()).update(awaited)
    if is_all:
        allrep.append((owner, rel, sorted(set(thresh))[:8]))

print(f"live_scripts={len(scripts)}")
print("--- WAITS ---")
for owner, awaited, is_all, rel, thresh in rows:
    if awaited or is_all:
        print(f"{owner} allrep={is_all} thresh={thresh} waits={awaited} :: {rel}")
print("--- MUTUAL (direct, live scripts only) ---")
owners = sorted(k for k in owner_waits if k)
mutual = []
for i, a in enumerate(owners):
    for b in owners[i+1:]:
        if b in owner_waits.get(a, ()) and a in owner_waits.get(b, ()):
            mutual.append((a, b))
            print(f"MUTUAL {a} <-> {b}")
if not mutual:
    print("NONE")
print("--- ALL-REPORTS ---")
for owner, rel, thresh in allrep:
    print(f"{owner} thresh={thresh} {rel}")
