#!/usr/bin/env python3
"""V33 adjacency audit — read-only. Writes only under V33-scratch/."""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V33-scratch"
OUT = SCRATCH / "audit-out"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "4265df5"
os.chdir(ROOT)

def run(cmd, timeout=120):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def blob(path: str) -> str:
    rc, out, err = run(f"git hash-object -- {path}")
    return out.strip()

lines = []
def emit(s=""):
    lines.append(s)
    print(s, flush=True)

emit(f"AUDIT_START")
rc, out, err = run("date '+%Y-%m-%d %H:%M:%S %z'")
emit(out.strip())
rc, out, err = run("git rev-parse HEAD")
emit(f"HEAD {out.strip()}")
rc, out, err = run("git log -1 --oneline")
emit(out.strip())

# A1 charter identity
emit("\n=== A1 CHARTER ===")
for f in ["PROVINCE.md", "SHONEN.md", "SKILL.md", "README.md", "l0-questions.md", "SCORECARD.md", ".gitignore"]:
    rc, bout, _ = run(f"git rev-parse {BASE}:{f}")
    base_blob = bout.strip()
    live = blob(f)
    rc, dout, _ = run(f"git diff {BASE} -- {f} | wc -c")
    same = "IDENTICAL" if live == base_blob else "CHANGED"
    emit(f"{f} {same} live={live} base={base_blob} diff_bytes={dout.strip()} sha={sha256_file(ROOT/f)}")

# A2 tracked diff vs baseline and vs HEAD
emit("\n=== A2 DIFF NAME-STATUS vs 4265df5 ===")
rc, out, err = run(f"git diff --name-status {BASE}")
emit(out.rstrip())
emit("\n=== A2 DIFF NAME-STATUS vs HEAD ===")
rc, out, err = run("git diff --name-status HEAD")
emit(out.rstrip() or "(empty)")
emit("\n=== A2 NUMSTAT vs HEAD ===")
rc, out, err = run("git diff --numstat HEAD")
emit(out.rstrip() or "(empty)")
emit("\n=== A2 NUMSTAT vs BASE (selected) ===")
rc, out, err = run(f"git diff --numstat {BASE} -- LOG.md SCORECARD.md SKILL.md corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json")
emit(out.rstrip())

# untracked outside wave
emit("\n=== A2 UNTRACKED OUTSIDE WAVE ===")
rc, out, err = run("git status --porcelain -uall")
outside = []
wave = []
for line in out.splitlines():
    if line.startswith("?? "):
        path = line[3:]
        if path.startswith(".ufo/waves/round-99/"):
            wave.append(path)
        else:
            outside.append(path)
    else:
        outside.append("NON-UNTRACKED " + line)
emit(f"wave_untracked_count={len(wave)}")
emit(f"outside_count={len(outside)}")
for p in outside:
    emit(p)

# corpus blob audit vs baseline (tracked files only, skip .ufo)
emit("\n=== A2 CORPUS BLOB AUDIT ===")
rc, out, err = run(f"git ls-tree -r --name-only {BASE}")
base_files = [p for p in out.splitlines() if not p.startswith(".ufo/")]
changed = []
missing = []
for p in base_files:
    live_path = ROOT / p
    if not live_path.exists():
        missing.append(p)
        continue
    rc, bout, _ = run(f"git rev-parse {BASE}:{p}")
    if blob(p) != bout.strip():
        changed.append(p)
emit(f"base_non_ufo={len(base_files)} changed={len(changed)} missing={len(missing)}")
for p in changed:
    emit(f"CHANGED {p}")
for p in missing:
    emit(f"MISSING {p}")

# fixture census
emit("\n=== CENSUS ===")
rc, out, err = run("ls -d corpus/fixtures/*/ | wc -l")
emit(f"fixture_dirs={out.strip()}")

# modes / symlinks of new corpus
emit("\n=== NEW FILE MODES ===")
rc, out, err = run("find corpus/fixtures/r99-window-lapse corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md -printf '%y %m %s %p\\n' 2>/dev/null | sort")
emit(out.rstrip())

# inheritance cmp
emit("\n=== INHERITANCE vs r98 ===")
r98 = ROOT / "corpus/fixtures/r98-clerk-filing"
r99 = ROOT / "corpus/fixtures/r99-window-lapse"
for name in ["entities.json", "relations.json", "contradictions.json", "inspiration-note.md", "source-excerpt.md", "timeline.json", "sources.json", "fictional-excerpts.md", "README.md", "claim-excerpt-map.md"]:
    a = r98 / name
    b = r99 / name
    if not b.exists():
        emit(f"ABSENT {name}")
        continue
    ab, bb = a.read_bytes(), b.read_bytes()
    if ab == bb:
        emit(f"IDENTICAL {name} {len(ab)}")
    elif bb.startswith(ab):
        emit(f"PREFIX {name} {len(ab)} -> {len(bb)} appended={len(bb)-len(ab)}")
    else:
        # json prefix?
        emit(f"DIFF {name} {len(ab)} -> {len(bb)}")

# json counts
emit("\n=== JSON COUNTS r99 ===")
for name in ["entities.json", "relations.json", "contradictions.json", "timeline.json", "sources.json"]:
    data = json.loads((r99 / name).read_text())
    emit(f"{name} len={len(data)}")

# external names in json
emit("\n=== EXTERNAL NAMES IN r99 JSON ===")
import re
pat = re.compile(r"spence|kojiki|chamberlain|gutenberg|etcs|inana|ovid|maya|kiche|k'iche", re.I)
for p in sorted(r99.glob("*.json")):
    text = p.read_text()
    hits = [(i+1, line) for i, line in enumerate(text.splitlines()) if pat.search(line)]
    emit(f"{p.name} hits={len(hits)}")
    for n, line in hits[:20]:
        emit(f"  {n}: {line[:200]}")

# language scan over new/changed bytes
emit("\n=== LANGUAGE SCAN ===")
scan_files = []
# diffs of tracked producer files vs BASE
rc, diff, err = run(f"git diff {BASE} -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md LOG.md")
(OUT / "tracked.diff").write_text(diff)
scan_files.append(("tracked.diff", diff))
for p in sorted(r99.iterdir()):
    if p.is_file():
        scan_files.append((str(p.relative_to(ROOT)), p.read_text(errors="replace")))
for kn in ["corpus/knowledge/r99-gate-blind-spot-table.md", "corpus/knowledge/r99-lapse-scope-note.md"]:
    kp = ROOT / kn
    if kp.exists():
        scan_files.append((kn, kp.read_text(errors="replace")))

mech = re.compile(r"mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|\bdice\b|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)|licensed under|permission is granted", re.I)
rights = re.compile(r"rights|licen[cs]e|copyright|permission|canon|training|attribut", re.I)
pathpat = re.compile(r"/home/|\.\./|/tmp/|kotodama|game-dev|art-east|kengaku|mado-shokunin|tabi-shokunin")
emit("--- mechanics / rights-grant / path hits ---")
for label, text in scan_files:
    for i, line in enumerate(text.splitlines(), 1):
        if mech.search(line) or pathpat.search(line):
            emit(f"HIT {label}:{i}: {line[:240]}")
emit("--- rights/canon context hits (for classification) ---")
# only new corpus + tool diff, not whole LOG
for label, text in scan_files:
    if label == "tracked.diff" and "LOG.md" in text:
        pass
    for i, line in enumerate(text.splitlines(), 1):
        if rights.search(line):
            # skip huge LOG body noise by filtering later
            if label.endswith("LOG.md") or (label == "tracked.diff" and line.startswith((" ", "\\"))):
                continue
            emit(f"CTX {label}:{i}: {line[:220]}")

(OUT / "audit.txt").write_text("\n".join(lines) + "\n")
emit("\nAUDIT_WRITTEN")
