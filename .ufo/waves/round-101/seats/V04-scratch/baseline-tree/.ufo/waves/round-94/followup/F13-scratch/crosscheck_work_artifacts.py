#!/usr/bin/env python3
"""F13 cross-check: my census vs WORK-wave baseline artifacts (W04, W05).

Recomputes sha256 for every corpus/fixtures path at 9c2eea3 from git blobs and
compares to W05-baseline-corpus.sha256; compares W04's per-directory exits to
the baseline exits observed by census_tuples.py.
"""
import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = "9c2eea3"
W05 = REPO / ".ufo/waves/round-94/work/W05-baseline-corpus.sha256"
W04 = REPO / ".ufo/waves/round-94/work/W04-baseline.json"
TUP = REPO / ".ufo/waves/round-94/followup/F13-scratch/census-tuples.json"

# 1. baseline blobs -> sha256
raw = subprocess.run(["git", "ls-tree", "-r", "-z", BASE, "--", "corpus/fixtures"],
                     cwd=REPO, capture_output=True, check=True).stdout
blobs = {}
for rec in raw.split(b"\0"):
    if not rec:
        continue
    meta, path = rec.split(b"\t", 1)
    blobs[path.decode()] = meta.split()[2].decode()
sha256_of = {}
for path, oid in blobs.items():
    data = subprocess.run(["git", "cat-file", "blob", oid], cwd=REPO, capture_output=True, check=True).stdout
    sha256_of[path] = hashlib.sha256(data).hexdigest()

# 2. W05 manifest
manifest = {}
for line in W05.read_text(encoding="utf-8").splitlines():
    digest, path = line.split("  ", 1)
    manifest[path] = digest
fixture_rows = {p: d for p, d in manifest.items() if p.startswith("corpus/fixtures/")}
mismatch = sorted(p for p in fixture_rows if p not in sha256_of or sha256_of[p] != fixture_rows[p])
not_in_manifest = sorted(p for p in sha256_of if p not in fixture_rows)
new_dir_rows = sorted(p for p in manifest if "r94-paired-crossing" in p)

# 3. W04 exits/violations vs my baseline exits
w04 = json.loads(W04.read_text(encoding="utf-8"))["tuples"]
tup = json.loads(TUP.read_text(encoding="utf-8"))
per = tup["per_dir"]

w04_dirs = sorted(k.split("/")[-1] for k in w04)
my_base_dirs = sorted(n for n, v in per.items() if v["baseline"])
exit_violation_mismatch = []
for k, row in w04.items():
    name = k.split("/")[-1]
    mine = per[name]["baseline"]
    if row["exit"] != mine["exit"] or row["violation_count"] != mine["violations"]:
        exit_violation_mismatch.append({"dir": name, "w04": row, "mine": mine})

print(f"W04 dirs: {len(w04)}  my baseline dirs: {len(my_base_dirs)}  dir sets equal: {w04_dirs == my_base_dirs}")
print(f"W04 exit/violation mismatches: {len(exit_violation_mismatch)}")
for m in exit_violation_mismatch[:10]:
    print(f"  MISMATCH {m}")

print(f"baseline tracked fixture blobs (mine): {len(sha256_of)}")
print(f"W05 fixture rows: {len(fixture_rows)}  mismatches vs recomputed: {len(mismatch)}  missing-from-manifest: {len(not_in_manifest)}")
print(f"W05 rows mentioning r94-paired-crossing: {len(new_dir_rows)}")
if mismatch:
    for p in mismatch[:10]:
        print(f"  MISMATCH {p}: w05={fixture_rows.get(p)} recomputed={sha256_of.get(p)}")
if not_in_manifest:
    for p in not_in_manifest[:10]:
        print(f"  NOT IN MANIFEST {p}")
