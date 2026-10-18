#!/usr/bin/env python3
"""Relation-type census: baseline git tree vs worktree fixture relations.json files."""
import collections
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = "4265df5"


def load_rows(blob: bytes, label: str):
    data = json.loads(blob.decode("utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"{label}: top-level is {type(data).__name__}, not list")
    types = []
    for i, row in enumerate(data):
        if not isinstance(row, dict) or "type" not in row:
            raise SystemExit(f"{label}[{i}]: missing type or not object")
        types.append(row["type"])
    return types


def baseline_files():
    out = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASE, "corpus/fixtures"],
        cwd=ROOT,
        text=True,
    )
    return [p for p in out.splitlines() if p.endswith("/relations.json")]


def census_from_git():
    counts = collections.Counter()
    files = 0
    rows = 0
    for path in baseline_files():
        blob = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        types = load_rows(blob, path)
        files += 1
        rows += len(types)
        counts.update(types)
    return files, rows, counts


def census_worktree():
    counts = collections.Counter()
    files = 0
    rows = 0
    paths = sorted((ROOT / "corpus/fixtures").glob("*/relations.json"))
    for path in paths:
        types = load_rows(path.read_bytes(), str(path))
        files += 1
        rows += len(types)
        counts.update(types)
    return files, rows, counts, paths


def unchanged():
    moved = []
    checked = 0
    for path in baseline_files():
        blob = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        wt = (ROOT / path).read_bytes()
        checked += 1
        if wt != blob:
            moved.append(path)
    return checked, moved


def main():
    bf, br, bc = census_from_git()
    wf, wr, wc, paths = census_worktree()
    print(f"BASELINE files={bf} rows={br} types={len(bc)}")
    print(f"WORKTREE files={wf} rows={wr} types={len(wc)}")
    keys = sorted(set(bc) | set(wc))
    for k in keys:
        b, w = bc.get(k, 0), wc.get(k, 0)
        mark = "" if b == w else f"  CHANGED {b}->{w}"
        print(f"  {w} {k}{mark}")
    new_types = sorted(set(wc) - set(bc))
    lost_types = sorted(set(bc) - set(wc))
    print("new types:", new_types or "none")
    print("lost types:", lost_types or "none")
    checked, moved = unchanged()
    print(f"baseline relations.json checked={checked} moved={len(moved)}")
    for p in moved:
        print("  MOVED", p)
    if not moved:
        print("all baseline relations.json unchanged in worktree")
    # arc hashes
    import hashlib
    for name in (
        "r94-paired-crossing",
        "r95-crossing-aftermath",
        "r96-crossing-response",
        "r97-crossing-acknowledgment",
        "r98-clerk-filing",
        "r99-window-lapse",
    ):
        p = ROOT / "corpus/fixtures" / name / "relations.json"
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        print(f"arc {name} {p.stat().st_size} {h}")


if __name__ == "__main__":
    main()
