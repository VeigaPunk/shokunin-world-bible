#!/usr/bin/env python3
"""V21 (round 97) census + preservation receipt: repo-relative check_bible run
over every fixture directory; violation lines counted as "- " lines (r94-r96
definition, matching V13). Emits per-dir exit + output hash receipt."""
import hashlib, json, os, subprocess, sys
REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
tag = sys.argv[1] if len(sys.argv) > 1 else "pre"
dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
clean = negative = violation_lines = 0
odd = []
receipts = {}
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", rel],
                       cwd=REPO, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    receipts[rel] = {"exit": p.returncode, "stdout_sha256": hashlib.sha256(out.encode()).hexdigest()}
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        violation_lines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else:
        odd.append((rel, p.returncode, out))
res = {"fixture_dirs": len(dirs), "clean_exit0": clean, "negative_exit1": negative,
       "violation_lines": violation_lines, "non_0_1_exits": odd}
print(json.dumps(res))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "census_%s_receipts.json" % tag), "w") as fh:
    json.dump(receipts, fh, indent=1, sort_keys=True)
