#!/usr/bin/env python3
"""V27 r96 report-path exclusivity checks (lane repo + parent tree)."""
import os, re, subprocess, glob, time

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(R, ".ufo/waves/round-96/seats")

print("=== 1. report files directly under seats/ (non-dir) ===")
entries = sorted(os.listdir(SEATS))
reports = [e for e in entries if os.path.isfile(os.path.join(SEATS, e))]
dirs = [e for e in entries if os.path.isdir(os.path.join(SEATS, e))]
print(f"files: {len(reports)}")
for e in reports:
    print("  ", e)
print(f"dirs: {len(dirs)}")
for e in dirs:
    print("  ", e, "(dir)")

print("=== 2. name pattern + duplicate seat-id prefixes ===")
pat = re.compile(r"^(Q[1-6]|V\d{1,2})")
seatids = {}
bad = []
for e in reports:
    m = pat.match(e)
    if not m:
        bad.append(e)
        continue
    seatids.setdefault(m.group(1), []).append(e)
dups = {k: v for k, v in seatids.items() if len(v) > 1}
print("unmatched names:", bad if bad else "(none)")
print("duplicate seat-id prefixes:", dups if dups else "(none)")

print("=== 3. content spot-check: filename seat-id appears in first 30 lines ===")
mismatch = []
for e in reports:
    m = pat.match(e)
    if not m:
        continue
    sid = m.group(1)
    with open(os.path.join(SEATS, e), encoding="utf-8", errors="replace") as fh:
        head = "".join(fh.readlines()[:30])
    if sid not in head:
        mismatch.append(e)
print("files whose seat-id missing from first 30 lines:", mismatch if mismatch else "(none)")

print("=== 4. report-like files elsewhere in lane repo (mtime >= wave start 17:37) ===")
wave_start = time.mktime(time.strptime("2026-10-17 17:37", "%Y-%m-%d %H:%M"))
hits = []
for root, dirs, files in os.walk(R):
    if ".git" in root.split(os.sep):
        continue
    for f in files:
        if re.match(r"^(Q[1-6]|V\d{1,2})[a-z0-9._-]*\.(md|json)$", f):
            p = os.path.join(root, f)
            if os.path.getmtime(p) >= wave_start and not p.startswith(SEATS + os.sep):
                hits.append(p)
print("hits:", hits if hits else "(none)")

print("=== 5. round-96 dir: files at round-96/ top level and scratch listing ===")
RD = os.path.join(R, ".ufo/waves/round-96")
for e in sorted(os.listdir(RD)):
    p = os.path.join(RD, e)
    kind = "dir" if os.path.isdir(p) else "file"
    print(f"  {kind} {e}")

print("=== 6. parent tree: git status + recent loose files (mtime >= 17:37) ===")
P = "/home/vgpnk/Projects/shokunin"
res = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=P,
                     capture_output=True, text=True)
print("parent git status lines:", len(res.stdout.splitlines()))
print(res.stdout)
print("parent loose files newer than wave start (depth<=2, excl. lane repo/.git):")
for root, dirs, files in os.walk(P):
    depth = root[len(P):].count(os.sep)
    if depth >= 2:
        dirs[:] = []
    if "/lore-shokunin" in root or "/.git" in root:
        dirs[:] = []
        continue
    for f in files:
        p = os.path.join(root, f)
        try:
            if os.path.getmtime(p) >= wave_start:
                print("  ", p)
        except OSError:
            pass
