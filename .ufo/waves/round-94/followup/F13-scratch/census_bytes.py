#!/usr/bin/env python3
"""F13 byte/path preservation census: corpus/fixtures 9c2eea3 vs HEAD vs worktree.

Own script (F13 seat). Classifies every path under corpus/fixtures/ into
added / modified / deleted by git blob hash, then verifies the on-disk worktree
against the HEAD blobs. Also counts top-level fixture directories at both
revisions and on disk.
"""
import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = "9c2eea3"
PREFIX = "corpus/fixtures/"
OUT = Path(__file__).resolve().parent / "census-bytes.json"


def ls_tree(rev):
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "-z", rev, "--", PREFIX],
        cwd=REPO, capture_output=True, check=True,
    )
    entries = {}
    for rec in proc.stdout.split(b"\0"):
        if not rec:
            continue
        meta, path = rec.split(b"\t", 1)
        mode, typ, sha = meta.split()
        entries[path.decode()] = {"mode": mode.decode(), "type": typ.decode(), "blob": sha.decode()}
    return entries


def git_blob_sha(data: bytes) -> str:
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(data))
    h.update(data)
    return h.hexdigest()


def top_dirs(paths):
    dirs = set()
    for p in paths:
        rel = p[len(PREFIX):]
        head = rel.split("/", 1)[0]
        if "/" in rel:
            dirs.add(head)
    return dirs


base = ls_tree(BASE)
head = ls_tree("HEAD")

added = sorted(set(head) - set(base))
deleted = sorted(set(base) - set(head))
modified = sorted(p for p in set(base) & set(head) if base[p]["blob"] != head[p]["blob"])

# on-disk census
disk = {}
for f in sorted((REPO / PREFIX).rglob("*")):
    if f.is_file():
        disk[str(f.relative_to(REPO))] = git_blob_sha(f.read_bytes())
disk_untracked = sorted(p for p in disk if p not in head)
disk_missing = sorted(p for p in head if p not in disk)
disk_dirty = sorted(p for p in set(disk) & set(head) if disk[p] != head[p]["blob"])

base_dirs = top_dirs(base)
head_dirs = top_dirs(head)
disk_dirs = sorted(
    str(d.relative_to(REPO / PREFIX))
    for d in (REPO / PREFIX).iterdir()
    if d.is_dir()
)

result = {
    "baseline_rev": subprocess.run(
        ["git", "rev-parse", BASE], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout.strip(),
    "head_rev": subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout.strip(),
    "tracked_files_baseline": len(base),
    "tracked_files_head": len(head),
    "top_level_dirs_baseline": sorted(base_dirs),
    "top_level_dirs_baseline_count": len(base_dirs),
    "top_level_dirs_head_count": len(head_dirs),
    "top_level_dirs_disk_count": len(disk_dirs),
    "dirs_added": sorted(head_dirs - base_dirs),
    "dirs_removed": sorted(base_dirs - head_dirs),
    "paths_added": added,
    "paths_modified": modified,
    "paths_deleted": deleted,
    "disk_files": len(disk),
    "disk_untracked_under_fixtures": disk_untracked,
    "disk_missing_vs_head": disk_missing,
    "disk_dirty_vs_head": disk_dirty,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

print(f"baseline {result['baseline_rev'][:7]} tracked files: {len(base)}")
print(f"HEAD {result['head_rev'][:7]} tracked files: {len(head)}")
print(f"top-level fixture dirs: baseline {len(base_dirs)} -> HEAD {len(head_dirs)} -> disk {len(disk_dirs)}")
print(f"dirs added: {result['dirs_added']}")
print(f"dirs removed: {result['dirs_removed']}")
print(f"paths added ({len(added)}):")
for p in added:
    print(f"  + {p}")
print(f"paths modified ({len(modified)}): {modified}")
print(f"paths deleted ({len(deleted)}): {deleted}")
print(f"disk files: {len(disk)}; untracked={disk_untracked}; missing={disk_missing}; dirty={disk_dirty}")
print(f"wrote {OUT}")
