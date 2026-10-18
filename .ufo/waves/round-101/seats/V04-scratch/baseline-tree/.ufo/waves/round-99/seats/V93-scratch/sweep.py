#!/usr/bin/env python3
"""V93 census-4: python hashlib full inherited sweep vs a git-archive tree.

Compares every blob path listed by `git ls-tree -r <base> -- corpus` between
the worktree and an extracted archive of that commit. Does not use
git hash-object. Also records tracked non-corpus paths that the round may
touch (SKILL.md, LOG.md, SCORECARD.md) when those archive copies exist.
"""
import hashlib
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "4265df5"
EXTRA = ("SKILL.md", "LOG.md", "SCORECARD.md")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    arch = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    raw = subprocess.check_output(
        ["git", "ls-tree", "-r", BASE, "--", "corpus"], text=True, cwd=REPO
    )
    rows = []
    for line in raw.splitlines():
        meta, path = line.split("\t", 1)
        mode, typ, blob = meta.split()
        if typ == "blob":
            rows.append((path, blob, mode))
    identical = []
    mismatch = []
    missing = []
    for path, blob, mode in rows:
        wt = os.path.join(REPO, path)
        ar = os.path.join(arch, path)
        if not os.path.isfile(wt):
            missing.append({"path": path, "where": "worktree", "git_blob": blob})
            continue
        if not os.path.isfile(ar):
            missing.append({"path": path, "where": "archive", "git_blob": blob})
            continue
        a, b = sha256(wt), sha256(ar)
        rec = {
            "path": path,
            "worktree_sha256": a,
            "archive_sha256": b,
            "git_blob": blob,
            "wt_size": os.path.getsize(wt),
            "ar_size": os.path.getsize(ar),
        }
        if a == b:
            identical.append(path)
        else:
            mismatch.append(rec)
    extras = []
    for rel in EXTRA:
        wt = os.path.join(REPO, rel)
        ar = os.path.join(arch, rel)
        if os.path.isfile(wt) and os.path.isfile(ar):
            a, b = sha256(wt), sha256(ar)
            extras.append(
                {
                    "path": rel,
                    "identical": a == b,
                    "worktree_sha256": a,
                    "archive_sha256": b,
                    "wt_size": os.path.getsize(wt),
                    "ar_size": os.path.getsize(ar),
                }
            )
    # untracked corpus paths (new files), excluding seat scratch
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "corpus", "SKILL.md"],
        text=True,
        cwd=REPO,
    ).splitlines()
    summary = {
        "baseline": subprocess.check_output(
            ["git", "rev-parse", BASE], text=True, cwd=REPO
        ).strip(),
        "head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, cwd=REPO
        ).strip(),
        "baseline_corpus_blobs": len(rows),
        "identical": len(identical),
        "mismatch_count": len(mismatch),
        "missing_count": len(missing),
        "mismatch": mismatch,
        "missing": missing,
        "extras": extras,
        "untracked_corpus_or_skill": untracked,
    }
    text = json.dumps(summary, indent=1) + "\n"
    if out:
        with open(out, "w") as fh:
            fh.write(text)
    print(
        json.dumps(
            {
                "baseline_corpus_blobs": summary["baseline_corpus_blobs"],
                "identical": summary["identical"],
                "mismatch_count": summary["mismatch_count"],
                "missing_count": summary["missing_count"],
                "mismatch_paths": [m["path"] for m in mismatch],
                "missing_paths": [m["path"] for m in missing],
                "extras": [
                    {"path": e["path"], "identical": e["identical"]} for e in extras
                ],
                "untracked": untracked,
            },
            indent=1,
        )
    )


if __name__ == "__main__":
    main()
