#!/usr/bin/env python3
"""V24 scope-creep analyzer — round 97. Read-only over the lane repo.
Usage: analyze.py <label>
Writes evidence into V24-scratch/snap/.
"""
import os, re, subprocess, sys, json

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
PARENT = "/home/vgpnk/Projects/shokunin"
SEATS = f"{LANE}/.ufo/waves/round-97/seats"
SNAP = f"{SEATS}/V24-scratch/snap"
label = sys.argv[1] if len(sys.argv) > 1 else "scan"

def sh(cmd, cwd=LANE):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return r.stdout, r.returncode

porc, _ = sh("git status --porcelain -uall")
paths = []
for line in porc.splitlines():
    if len(line) < 4: continue
    xy, p = line[:2], line[3:]
    if " -> " in p: p = p.split(" -> ", 1)[1]
    paths.append((xy, p))

# declared producer paths
R1 = {"corpus/tools/map_obligations.py"}
R2 = {"corpus/tools/map-obligations-contract.json", "corpus/tools/README.md"}
R3 = {"corpus/tools/dependency_freeze.py", "corpus/tools/dependency-freeze-contract.json"}
R4 = {"corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
      "corpus/fixtures/r97-crossing-acknowledgment/entities.json",
      "corpus/fixtures/r97-crossing-acknowledgment/relations.json",
      "corpus/fixtures/r97-crossing-acknowledgment/contradictions.json",
      "corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md",
      "corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md",
      "corpus/fixtures/r97-crossing-acknowledgment/sources.json",
      "corpus/fixtures/r97-crossing-acknowledgment/timeline.json",
      "corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md"}
R5 = {"corpus/fixtures/r97-crossing-acknowledgment/README.md",
      "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"}
R6 = {"corpus/knowledge/r97-acknowledgment-scope-note.md"}
DECL = R1 | R2 | R3 | R4 | R5 | R6

buckets = {"B0_LOG": [], "B1a_tools_mod": [], "B1b_tools_new": [], "B1c_r96_repair": [],
           "B1d_r97_fixture": [], "B1e_knowledge": [], "B2_seats": [], "B2b_wave": [],
           "T_transient": [], "OTHER": []}
for xy, p in paths:
    if p == "LOG.md": buckets["B0_LOG"].append((xy, p))
    elif p in R1 | R2: buckets["B1a_tools_mod"].append((xy, p))
    elif p in R3: buckets["B1b_tools_new"].append((xy, p))
    elif p == "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md": buckets["B1c_r96_repair"].append((xy, p))
    elif p in R4 | R5: buckets["B1d_r97_fixture"].append((xy, p))
    elif p in R6: buckets["B1e_knowledge"].append((xy, p))
    elif p.startswith(".ufo/waves/round-97/seats/"): buckets["B2_seats"].append((xy, p))
    elif p.startswith(".ufo/waves/round-97/"): buckets["B2b_wave"].append((xy, p))
    elif re.match(r"^(map-obligations-self-test-|dependency-freeze-|support-check-|boundary-doc-check-)", p):
        buckets["T_transient"].append((xy, p))
    else: buckets["OTHER"].append((xy, p))
# transient presence at scan time
trans, _ = sh("ls -d map-obligations-self-test-* dependency-freeze-* support-check-* boundary-doc-check-* 2>/dev/null || true")
with open(f"{SNAP}/transients-{label}.txt", "w") as f: f.write(trans)

with open(f"{SNAP}/buckets-{label}.txt", "w") as f:
    for b, items in buckets.items():
        f.write(f"## {b} n={len(items)}\n")
        for xy, p in items: f.write(f"{xy}\t{p}\n")
        f.write("\n")
with open(f"{SNAP}/porcelain-{label}.txt", "w") as f:
    f.write(porc)

# tracked diffs
diff, _ = sh("git diff --name-status")
with open(f"{SNAP}/diff-{label}.txt", "w") as f: f.write(diff)
cached, _ = sh("git diff --cached --name-status")
with open(f"{SNAP}/cached-{label}.txt", "w") as f: f.write(cached)

# seats exclusivity
md = sorted(x for x in os.listdir(SEATS) if x.endswith(".md"))
pat = re.compile(r"^(R[1-6]|V\d{2})-[A-Za-z0-9._-]+\.md$")
bad = [x for x in md if not pat.match(x)]
nonmd = sorted(x for x in os.listdir(SEATS) if not x.endswith(".md"))
with open(f"{SNAP}/excl-{label}.txt", "w") as f:
    f.write(f"report_md_n={len(md)}\n")
    f.write("reports:\n" + "\n".join(md) + "\n")
    f.write("pattern_mismatch:\n" + "\n".join(bad) + "\n")
    f.write("non_md_at_seats_top:\n" + "\n".join(nonmd) + "\n")
    # cross-scratch: report-like md inside a scratch dir owned by another prefix
    cross = []
    for d in nonmd:
        if d.endswith("-scratch"):
            owner = d.split("-")[0]
            for root, _, files in os.walk(os.path.join(SEATS, d)):
                for fn in files:
                    if fn.endswith(".md") and pat.match(fn):
                        o2 = fn.split("-")[0]
                        if o2 != owner:
                            cross.append(os.path.join(root, fn))
    f.write("cross_scratch_mismatch:\n" + "\n".join(cross) + "\n")
    # header spot-check: seat id in filename should appear in first 30 lines
    hdr_bad = []
    for fn in md:
        seat_id = fn.split("-")[0]
        try:
            with open(os.path.join(SEATS, fn), errors="replace") as g:
                head = "".join(g.readline() for _ in range(30))
            if seat_id not in head:
                hdr_bad.append(fn)
        except OSError:
            hdr_bad.append(fn + " (unreadable)")
    f.write("header_seat_mismatch:\n" + "\n".join(hdr_bad) + "\n")
    # duplicate seat-id prefixes (e.g. V40-debt.json + V40-debt.md sidecar pairs)
    from collections import Counter
    pref = Counter(x.split("-")[0] for x in md + nonmd)
    dups = {k: [x for x in md + nonmd if x.split("-")[0] == k] for k, c in pref.items() if c > 1}
    f.write("duplicate_prefixes:\n" + "\n".join(f"{k}: {v}" for k, v in dups.items()) + "\n")

# report-like .md elsewhere in lane repo (mtime >= wave start), outside seats/
elsewhere, _ = sh("find . -path ./.git -prune -o -path ./.ufo/waves/round-97/seats -prune -o -name '*.md' -newermt '2026-10-17 18:41' -print 2>/dev/null | grep -vE '^./.ufo/waves/round-9[0-6]/'")
with open(f"{SNAP}/elsewhere-md-{label}.txt", "w") as f: f.write(elsewhere)

# pycache under corpus
pc, _ = sh("find corpus -name '__pycache__' -o -name '*.pyc'")
with open(f"{SNAP}/pycache-{label}.txt", "w") as f: f.write(pc)
ig, _ = sh("git status --porcelain --ignored -uall")
igc = [l for l in ig.splitlines() if "__pycache__" in l or l.endswith(".pyc")]
with open(f"{SNAP}/pycache-ignored-{label}.txt", "w") as f: f.write("\n".join(igc))

# parent tree
pp, _ = sh("git status --porcelain -uall", cwd=PARENT)
with open(f"{SNAP}/parent-{label}.txt", "w") as f: f.write(pp)
ppc = sh("git status --porcelain --ignored -uall", cwd=PARENT)[0]
with open(f"{SNAP}/parent-ignored-{label}.txt", "w") as f: f.write(ppc)
# parent stray: lore-r97 signature artifacts anywhere in parent outside the lane
sig = ("-name '*crossing-acknowledgment*' -o -name '*crossing-response*' "
       "-o -name 'r97-acknowledgment-scope-note.md' -o -name 'claim-excerpt-map.md' "
       "-o -name 'map_obligations.py' -o -name 'dependency_freeze.py' "
       "-o -name 'map-obligations-contract.json' -o -name 'dependency-freeze-contract.json' "
       "-o -name 'boundary_doc_check.py' -o -name 'support_check.py'")
stray, _ = sh(f"find . -path ./lore-shokunin -prune -o -path ./.git -prune -o -type f \\( {sig} \\) -print 2>/dev/null", cwd=PARENT)
# parent new .md files at repo root (top level) since wave start
rootnew, _ = sh("find . -maxdepth 1 -newermt '2026-10-17 18:41' -type f -print 2>/dev/null", cwd=PARENT)
# parent waves dir listing (round-97 must NOT exist at parent)
pwaves, _ = sh("ls .ufo/waves/ | grep -i 'round-97' || echo 'no round-97 at parent'", cwd=PARENT)
with open(f"{SNAP}/parent-stray-{label}.txt", "w") as f:
    f.write("== signature files outside lore-shokunin ==\n" + stray)
    f.write("\n== parent root new files (18:41+) ==\n" + rootnew)
    f.write("\n== parent .ufo/waves round-97 check ==\n" + pwaves)

print(f"label={label} porcelain={len(paths)}")
for b, items in buckets.items(): print(f"{b}={len(items)}")
print(f"report_md={len(md)} pattern_mismatch={len(bad)} nonmd_top={len(nonmd)}")
print("pycache lines:", len(pc.splitlines()))
print("parent porcelain lines:", len(pp.splitlines()))
print("parent new-files (18:41+, ex .git/reports):", len(stray.splitlines()))
