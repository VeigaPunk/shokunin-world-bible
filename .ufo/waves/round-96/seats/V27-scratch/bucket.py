#!/usr/bin/env python3
"""V27 r96 scope-creep classifier: bucket every `git status --porcelain -uall` path."""
import subprocess, sys

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
res = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=R,
                     capture_output=True, text=True)
if res.returncode != 0:
    print("git status failed:", res.stderr)
    sys.exit(1)
lines = res.stdout.splitlines()

producer_exact_modified = {
    "corpus/tools/map_obligations.py",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/README.md",
}
producer_tools_new = {
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
}
producer_note_new = {"corpus/knowledge/r96-response-scope-note.md"}
fixture_prefix = "corpus/fixtures/r96-crossing-response/"
allowed_prefix = ".ufo/waves/round-96/"
allowed_exact = {"LOG.md"}

buckets = {
    "B1 producer-modified (tracked)": [],
    "B2a fixture-new": [],
    "B2b tools-new": [],
    "B2c knowledge-note-new": [],
    "B3 seat reports/scratch (.ufo/waves/round-96/)": [],
    "B4 orchestrator LOG.md": [],
    "OTHER": [],
}

for line in lines:
    xy, path = line[:2], line[3:]
    if path in allowed_exact:
        buckets["B4 orchestrator LOG.md"].append((xy, path))
    elif path.startswith(allowed_prefix):
        buckets["B3 seat reports/scratch (.ufo/waves/round-96/)"].append((xy, path))
    elif path in producer_tools_new:
        buckets["B2b tools-new"].append((xy, path))
    elif path in producer_note_new:
        buckets["B2c knowledge-note-new"].append((xy, path))
    elif path.startswith(fixture_prefix):
        buckets["B2a fixture-new"].append((xy, path))
    elif path in producer_exact_modified:
        buckets["B1 producer-modified (tracked)"].append((xy, path))
    else:
        buckets["OTHER"].append((xy, path))

print(f"total porcelain entries: {len(lines)}")
for b, v in buckets.items():
    print(f"{b}: {len(v)}")
print("---OTHER (each line = finding)---")
for xy, p in buckets["OTHER"]:
    print(f"{xy} {p}")
if not buckets["OTHER"]:
    print("(none)")
print("---B1 detail---")
for xy, p in buckets["B1 producer-modified (tracked)"]:
    print(f"{xy} {p}")
print("---B2 detail---")
for b in ("B2a fixture-new", "B2b tools-new", "B2c knowledge-note-new"):
    for xy, p in buckets[b]:
        print(f"{xy} {p}")
