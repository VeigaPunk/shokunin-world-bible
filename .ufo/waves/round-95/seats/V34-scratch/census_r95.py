#!/usr/bin/env python3
"""V34 independent census replica: corpus/fixtures working tree vs git archive of a ref.

Fresh implementation (does not reuse any prior census script).
Usage: census_r95.py [--ref fb118c4] [--root corpus/fixtures] [--expected-dirs 169]
Exit 0 iff: dir count == expected, 0 modified/deleted inherited files,
and every new path is under an expected new top-level dir (--allow-new).
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))
while not os.path.isdir(os.path.join(REPO, ".git")):
    REPO = os.path.dirname(REPO)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def materialize(ref, root, dest):
    proc = subprocess.run(
        ["git", "archive", "--format=tar", ref, root],
        cwd=REPO, capture_output=True,
    )
    if proc.returncode != 0:
        raise SystemExit("git archive failed: %s" % proc.stderr.decode())
    with tempfile.NamedTemporaryFile(suffix=".tar", delete=False) as tmp:
        tmp.write(proc.stdout)
        tar_path = tmp.name
    with tarfile.open(tar_path) as tf:
        tf.extractall(dest)
    os.unlink(tar_path)
    return os.path.join(dest, root)


def walk_files(base):
    out = {}
    for dirpath, _dirnames, filenames in os.walk(base):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            out[os.path.relpath(full, base)] = full
    return out


def walk_dirs(base, top_only):
    out = []
    if top_only:
        for name in sorted(os.listdir(base)):
            if os.path.isdir(os.path.join(base, name)):
                out.append(name)
        return out
    for dirpath, dirnames, _fn in os.walk(base):
        for d in dirnames:
            out.append(os.path.relpath(os.path.join(dirpath, d), base))
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="fb118c4")
    ap.add_argument("--root", default="corpus/fixtures")
    ap.add_argument("--expected-dirs", type=int, default=None)
    ap.add_argument("--allow-new", action="append", default=[])
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    work = os.path.join(REPO, args.root)
    with tempfile.TemporaryDirectory() as td:
        baseline = materialize(args.ref, args.root, td)
        b_files = walk_files(baseline)
        w_files = walk_files(work)

        inherited = sorted(set(b_files) & set(w_files))
        modified = sorted(p for p in inherited if sha256(b_files[p]) != sha256(w_files[p]))
        deleted = sorted(set(b_files) - set(w_files))
        new = sorted(set(w_files) - set(b_files))

        b_dirs_top = walk_dirs(baseline, True)
        w_dirs_top = walk_dirs(work, True)
        b_dirs_all = walk_dirs(baseline, False)
        w_dirs_all = walk_dirs(work, False)

        new_top_dirs = sorted(set(w_dirs_top) - set(b_dirs_top))
        gone_top_dirs = sorted(set(b_dirs_top) - set(w_dirs_top))

    allow = args.allow_new or []
    unexpected_new = []
    for p in new:
        if not any(p == a or p.startswith(a.rstrip("/") + "/") for a in allow):
            unexpected_new.append(p)
    unexpected_new_dirs = [d for d in new_top_dirs
                           if not any(d == a.rstrip("/") or d.startswith(a.rstrip("/") + "/")
                                      for a in allow)]

    ok = True
    reasons = []
    if args.expected_dirs is not None and len(w_dirs_top) != args.expected_dirs:
        ok = False
        reasons.append("top-level dir count %d != expected %d" % (len(w_dirs_top), args.expected_dirs))
    if modified:
        ok = False
        reasons.append("%d inherited file(s) modified" % len(modified))
    if deleted:
        ok = False
        reasons.append("%d inherited file(s) deleted" % len(deleted))
    if unexpected_new:
        ok = False
        reasons.append("%d unexpected new file(s)" % len(unexpected_new))
    if unexpected_new_dirs:
        ok = False
        reasons.append("%d unexpected new dir(s)" % len(unexpected_new_dirs))

    report = {
        "ref": args.ref,
        "root": args.root,
        "work_head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                                    capture_output=True).stdout.decode().strip(),
        "baseline_top_dirs": len(b_dirs_top),
        "work_top_dirs": len(w_dirs_top),
        "baseline_all_dirs": len(b_dirs_all),
        "work_all_dirs": len(w_dirs_all),
        "baseline_files": len(b_files),
        "work_files": len(w_files),
        "inherited_files": len(inherited),
        "modified_inherited": modified,
        "deleted_inherited": deleted,
        "new_files": new,
        "new_top_dirs": new_top_dirs,
        "gone_top_dirs": gone_top_dirs,
        "unexpected_new_files": unexpected_new,
        "unexpected_new_dirs": unexpected_new_dirs,
        "verdict": "PASS" if ok else "FAIL",
        "reasons": reasons,
    }
    print(json.dumps(report, indent=2))
    if args.json_out:
        with open(args.json_out, "w") as fh:
            json.dump(report, fh, indent=2)
    print("CENSUS %s: dirs=%d files=%d modified=%d deleted=%d new=%d %s"
          % (report["verdict"], len(w_dirs_top), len(w_files), len(modified),
             len(deleted), len(new), "; ".join(reasons)))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
