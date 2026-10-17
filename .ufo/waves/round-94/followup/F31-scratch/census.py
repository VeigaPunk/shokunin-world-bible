#!/usr/bin/env python3
"""F31 census-replica-2: independent preservation census of corpus/ vs git archive of 9c2eea3.

Fresh script (no reuse of F13 artifacts). Stdlib only, read-only on the live tree.
Extracts `git archive 9c2eea3 corpus` into F31-scratch/baseline/ and compares
byte-for-byte (sha256) against the live working tree.

Primary scope: corpus/fixtures. Secondary scope: whole corpus/.
Exit 0 iff 0 missing and 0 modified inherited paths (new paths are expected).
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tarfile

BASE_COMMIT = "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b"
ARCHIVE_PATH = "corpus"
PRIMARY = "corpus/fixtures"

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

def walk(root):
    """rel -> digest. Symlinks hashed as 'link:<target>'."""
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            if os.path.islink(full):
                out[rel] = "link:" + os.readlink(full)
            else:
                out[rel] = sha256_file(full)
    return out

def top_dirs(root):
    return sorted(
        n for n in os.listdir(root)
        if os.path.isdir(os.path.join(root, n))
    )

def main():
    repo = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    scratch = os.path.join(repo, ".ufo/waves/round-94/followup/F31-scratch")
    base_dir = os.path.join(scratch, "baseline")
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)

    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True,
    ).stdout.strip()
    tar_bytes = subprocess.run(
        ["git", "archive", BASE_COMMIT, ARCHIVE_PATH],
        capture_output=True, check=True,
    ).stdout
    with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tf:
        tf.extractall(base_dir)
    print(f"repo={repo}")
    print(f"baseline_commit={BASE_COMMIT}")
    print(f"live_HEAD={head}")

    live_root = os.path.join(repo, ARCHIVE_PATH)
    base_root = os.path.join(base_dir, ARCHIVE_PATH)
    live = walk(live_root)   # keys are relative to corpus/
    base = walk(base_root)

    base_keys = set(base)
    live_keys = set(live)
    new = sorted(live_keys - base_keys)
    missing = sorted(base_keys - live_keys)
    modified = sorted(k for k in (base_keys & live_keys) if base[k] != live[k])

    print(f"archive_bytes={len(tar_bytes)}")
    print(f"baseline_files_total={len(base)} live_files_total={len(live)}")

    def path_status(rel):
        if subprocess.run(["git", "ls-files", "--error-unmatch", "--", rel],
                          cwd=repo, capture_output=True).returncode == 0:
            return "tracked@HEAD"
        if subprocess.run(["git", "check-ignore", "-q", "--", rel],
                          cwd=repo, capture_output=True).returncode == 0:
            return "ignored"
        return "untracked"

    # ---- primary scope: corpus/fixtures ----
    def sub(d, prefix):
        return {k: v for k, v in d.items() if k == prefix or k.startswith(prefix + "/")}

    fx_rel = PRIMARY.split("/", 1)[1]          # "fixtures"; walk keys are corpus-relative
    p = fx_rel + "/"
    live_fx = sub(live, fx_rel)
    base_fx = sub(base, fx_rel)
    new_fx = sorted(k[len(p):] for k in new if k.startswith(p))
    missing_fx = sorted(k[len(p):] for k in missing if k.startswith(p))
    mod_fx = sorted(k[len(p):] for k in modified if k.startswith(p))

    live_dirs = top_dirs(os.path.join(live_root, fx_rel))
    base_dirs = top_dirs(os.path.join(base_root, fx_rel))
    print(f"fixtures_baseline_topdirs={len(base_dirs)}")
    print(f"fixtures_live_topdirs={len(live_dirs)}")
    print(f"fixtures_new_topdirs={sorted(set(live_dirs) - set(base_dirs))}")
    print(f"fixtures_lost_topdirs={sorted(set(base_dirs) - set(live_dirs))}")
    print(f"fixtures_baseline_files={len(base_fx)}")
    print(f"fixtures_live_files={len(live_fx)}")
    print(f"fixtures_inherited_modified={len(mod_fx)}")
    print(f"fixtures_inherited_missing={len(missing_fx)}")
    print(f"fixtures_new_files={len(new_fx)}")
    print("--- NEW fixture paths (relative to corpus/fixtures) ---")
    for k in new_fx:
        print(f"NEW  {k} [{path_status(ARCHIVE_PATH + '/' + fx_rel + '/' + k)}]")
    print("--- MISSING fixture paths ---")
    for k in missing_fx:
        print(f"MISS {k}")
    print("--- MODIFIED fixture paths ---")
    for k in mod_fx:
        print(f"MOD  {k}")

    # ---- secondary scope: whole corpus/ ----
    new_c = sorted(new)
    missing_c = sorted(missing)
    mod_c = sorted(modified)
    print(f"corpus_inherited_modified={len(mod_c)}")
    print(f"corpus_inherited_missing={len(missing_c)}")
    print(f"corpus_new_files={len(new_c)}")
    print("--- NEW corpus paths (relative to corpus/) ---")
    for k in new_c:
        print(f"NEW  {k} [{path_status(ARCHIVE_PATH + '/' + k)}]")
    print("--- MODIFIED corpus paths ---")
    for k in mod_c:
        print(f"MOD  {k}")
    print("--- MISSING corpus paths ---")
    for k in missing_c:
        print(f"MISS {k}")

    # dir counts
    def count_dirs(root):
        n = 0
        for _, dirnames, _ in os.walk(root):
            n += len(dirnames)
        return n

    print(f"fixtures_live_dirs_recursive={count_dirs(os.path.join(live_root, fx_rel))}")
    print(f"fixtures_baseline_dirs_recursive={count_dirs(os.path.join(base_root, fx_rel))}")
    print(f"corpus_live_dirs_recursive={count_dirs(live_root)}")
    print(f"corpus_baseline_dirs_recursive={count_dirs(base_root)}")

    verdict = "CLEAN" if not missing_fx and not mod_fx and not missing_c and not mod_c else "FAILED"
    print(f"RESULT {verdict}")
    sys.exit(0 if verdict == "CLEAN" else 1)

if __name__ == "__main__":
    main()
