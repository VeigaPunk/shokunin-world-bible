#!/usr/bin/env python3
"""V49 inherited-tools scope check: classify every corpus-scope path that differs
from f3e09f9 into {owned-expected, allowed-exception, VIOLATION}."""
import hashlib
import os
import subprocess

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "f3e09f9"
SCOPE = ["corpus/tools", "corpus/fixtures", "corpus/knowledge", "corpus/live"]

OWNED = {  # declared producer byte-ownership for r97
    "corpus/tools/map_obligations.py": "R1",
    "corpus/tools/map-obligations-contract.json": "R2",
    "corpus/tools/README.md": "R2",
    "corpus/tools/dependency_freeze.py": "R3",
    "corpus/tools/dependency-freeze-contract.json": "R3",
    "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md": "R4 (cosmetic repair)",
}
NEW_FIXTURE = "corpus/fixtures/r97-crossing-acknowledgment/"
NEW_NOTE = "corpus/knowledge/r97-acknowledgment-scope-note.md"

INHERITED_TOOLS = [
    "corpus/fixtures/check_bible.py",
    "corpus/tools/support_check.py",
    "corpus/tools/boundary_doc_check.py",
    "corpus/tools/boundary-doc-contract.json",
    "corpus/tools/discriminate_check.py",
]


def run(*a, **kw):
    return subprocess.run(a, cwd=REPO, capture_output=True, text=True, **kw)


def rev_files(rev):
    out = run("git", "ls-tree", "-r", rev, "--name-only", "--", *SCOPE)
    return [p for p in out.stdout.splitlines() if p]


def rev_hash(rev, path):
    out = run("git", "cat-file", "-p", f"{rev}:{path}")
    return hashlib.sha256(out.stdout.encode("utf-8", "surrogateescape")).hexdigest() if out.returncode == 0 else None


def wt_hash(rel):
    try:
        with open(os.path.join(REPO, rel), "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        return None


def classify(p):
    if p in OWNED:
        return f"OWNED({OWNED[p]})"
    if p.startswith(NEW_FIXTURE) or p == NEW_NOTE:
        return "NEW(r97 declared)"
    return "VIOLATION"


def main():
    base = {p: rev_hash(BASE, p) for p in rev_files(BASE)}
    wt = {}
    for root in SCOPE:
        for dirpath, _d, files in os.walk(os.path.join(REPO, root)):
            if "__pycache__" in dirpath:
                continue
            for fn in files:
                rel = os.path.relpath(os.path.join(dirpath, fn), REPO)
                wt[rel] = wt_hash(rel)

    changed = sorted(p for p in base if wt.get(p) not in (None, base[p]))
    deleted = sorted(p for p in base if p not in wt)
    added = sorted(p for p in wt if p not in base)

    print(f"## rev={BASE} tracked={len(base)} worktree={len(wt)}")
    print(f"## INHERITED TOOL PINS (must be unchanged):")
    for p in INHERITED_TOOLS:
        state = "UNCHANGED" if wt.get(p) == base.get(p) else "CHANGED"
        print(f"  {state:9s} {p}  base={base.get(p, '')[:12]} wt={(wt.get(p) or '')[:12]}")
    print(f"## CHANGED ({len(changed)}) -> classification:")
    for p in changed:
        print(f"  {classify(p):28s} {p}")
    print(f"## DELETED ({len(deleted)}):")
    for p in deleted:
        print(f"  {classify(p):28s} {p}")
    print(f"## ADDED ({len(added)}):")
    for p in added:
        print(f"  {classify(p):28s} {p}")
    viol = [p for p in changed + deleted + added if classify(p) == "VIOLATION"]
    print(f"## VIOLATIONS={len(viol)}")
    for p in viol:
        print(f"  VIOLATION {p}")


if __name__ == "__main__":
    main()
