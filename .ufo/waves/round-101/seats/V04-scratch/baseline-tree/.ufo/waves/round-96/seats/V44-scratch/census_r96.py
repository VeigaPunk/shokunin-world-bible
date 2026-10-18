#!/usr/bin/env python3
"""V44 (round 96) independent census replica.

Fresh implementation (not V34's r95 script, not V24's method as far as known):
materialize `git archive --format=tar <ref> <root>` into a temp dir, then compare
the extracted tree against the working tree by SHA-256 of file bytes.

Usage:
  python3 census_r96.py --ref <commit> [--root corpus/fixtures]
                        [--expected-dirs N] [--allow-new PREFIX ...]

Exit 0 when PASS (expected dir count, zero modified/deleted inherited, every new
path under an allow-new prefix), exit 1 otherwise. Prints a JSON receipt.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk_files(root):
    out = {}
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            out[os.path.relpath(full, root)] = sha256(full)
    return out


def walk_dirs(root):
    """Immediate subdirectories and all subdirectories (relative paths)."""
    top = []
    all_d = []
    for dirpath, dirnames, _filenames in os.walk(root):
        for name in dirnames:
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            all_d.append(rel)
            if os.sep not in rel:
                top.append(rel)
    return sorted(top), sorted(all_d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("--root", default="corpus/fixtures")
    ap.add_argument("--expected-dirs", type=int, default=None)
    ap.add_argument("--allow-new", action="append", default=[])
    args = ap.parse_args()

    work_root = os.path.join(REPO, args.root)
    tmp = tempfile.mkdtemp(prefix="v44-census-")
    tar_path = os.path.join(tmp, "snap.tar")
    with open(tar_path, "wb") as fh:
        proc = subprocess.run(
            ["git", "archive", "--format=tar", args.ref, args.root],
            cwd=REPO, stdout=fh, stderr=subprocess.PIPE,
        )
    if proc.returncode != 0:
        print("git archive failed:", proc.stderr.decode())
        sys.exit(2)
    with tarfile.open(tar_path) as tf:
        tf.extractall(tmp)
    base_root = os.path.join(tmp, args.root)

    base_files = walk_files(base_root)
    work_files = walk_files(work_root)
    base_top, base_all = walk_dirs(base_root)
    work_top, work_all = walk_dirs(work_root)

    inherited = sorted(set(base_files) & set(work_files))
    modified = [p for p in inherited if base_files[p] != work_files[p]]
    deleted = sorted(set(base_files) - set(work_files))
    new = sorted(set(work_files) - set(base_files))
    new_top_dirs = sorted(set(work_top) - set(base_top))
    gone_top_dirs = sorted(set(base_top) - set(work_top))

    def allowed(p):
        return any(p == a or p.startswith(a + os.sep) for a in args.allow_new)

    unexpected_new_files = [p for p in new if not allowed(p)]
    unexpected_new_dirs = [p for p in new_top_dirs if not allowed(p)]

    reasons = []
    if args.expected_dirs is not None and len(work_top) != args.expected_dirs:
        reasons.append(
            "dir count %d != expected %d" % (len(work_top), args.expected_dirs)
        )
    if modified:
        reasons.append("modified inherited: %d" % len(modified))
    if deleted:
        reasons.append("deleted inherited: %d" % len(deleted))
    if unexpected_new_files:
        reasons.append("unexpected new files: %d" % len(unexpected_new_files))
    if unexpected_new_dirs:
        reasons.append("unexpected new dirs: %d" % len(unexpected_new_dirs))
    if gone_top_dirs:
        reasons.append("gone top dirs: %d" % len(gone_top_dirs))

    receipt = {
        "ref": args.ref,
        "root": args.root,
        "baseline_top_dirs": len(base_top),
        "work_top_dirs": len(work_top),
        "baseline_all_dirs": len(base_all),
        "work_all_dirs": len(work_all),
        "baseline_files": len(base_files),
        "work_files": len(work_files),
        "inherited_files": len(inherited),
        "modified_inherited": modified,
        "deleted_inherited": deleted,
        "new_top_dirs": new_top_dirs,
        "gone_top_dirs": gone_top_dirs,
        "new_files_count": len(new),
        "new_files": new,
        "unexpected_new_files": unexpected_new_files,
        "unexpected_new_dirs": unexpected_new_dirs,
        "verdict": "PASS" if not reasons else "FAIL",
        "reasons": reasons,
    }
    print(json.dumps(receipt, indent=1))
    if reasons:
        print("CENSUS FAIL: " + "; ".join(reasons))
        sys.exit(1)
    print(
        "CENSUS PASS: dirs=%d files=%d modified=0 deleted=0 new=%d"
        % (len(work_top), len(work_files), len(new))
    )


if __name__ == "__main__":
    main()
