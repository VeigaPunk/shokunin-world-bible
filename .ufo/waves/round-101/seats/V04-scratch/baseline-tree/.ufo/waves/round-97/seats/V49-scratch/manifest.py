#!/usr/bin/env python3
"""V49 manifest: sha256 of every corpus/{tools,fixtures,knowledge} file at a git rev,
plus the same for the working tree, and a path-level delta."""
import hashlib
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "f3e09f9"
SCOPE = ["corpus/tools", "corpus/fixtures", "corpus/knowledge", "corpus/live"]


def run(*args, **kw):
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True, **kw)


def rev_files(rev):
    out = run("git", "ls-tree", "-r", rev, "--name-only", "--", *SCOPE)
    return [p for p in out.stdout.splitlines() if p]


def rev_hash(rev, path):
    out = run("git", "cat-file", "-p", f"{rev}:{path}")
    if out.returncode != 0:
        return None
    return hashlib.sha256(out.stdout.encode("utf-8", "surrogateescape")).hexdigest()


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else BASE
    base = {p: rev_hash(rev, p) for p in rev_files(rev)}
    import os

    wt = {}
    for root in SCOPE:
        d = os.path.join(REPO, root)
        for dirpath, _dirnames, filenames in os.walk(d):
            if "__pycache__" in dirpath:
                continue
            for fn in filenames:
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, REPO)
                try:
                    with open(full, "rb") as fh:
                        wt[rel] = hashlib.sha256(fh.read()).hexdigest()
                except OSError:
                    pass
    changed = sorted(p for p in base if p in wt and wt[p] != base[p])
    deleted = sorted(p for p in base if p not in wt)
    added = sorted(p for p in wt if p not in base)
    print(f"# rev={rev} tracked={len(base)} worktree={len(wt)}")
    print(f"# CHANGED ({len(changed)}):")
    for p in changed:
        print(f"  M {p}")
    print(f"# DELETED ({len(deleted)}):")
    for p in deleted:
        print(f"  D {p}")
    print(f"# ADDED ({len(added)}):")
    for p in added:
        print(f"  A {p}")


if __name__ == "__main__":
    main()
