#!/usr/bin/env python3
"""Positive control on the delivered fixture: mutate copies of the r96 fixture
and confirm compare_inherited.py reports FAIL (exit 1) for each mutation."""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
R95 = os.path.join(REPO, "corpus/fixtures/r95-crossing-aftermath")
R96 = os.path.join(REPO, "corpus/fixtures/r96-crossing-response")
COMPARATOR = os.path.join(HERE, "compare_inherited.py")


def run(r96_dir):
    p = subprocess.run([sys.executable, COMPARATOR, R95, r96_dir],
                       capture_output=True, text=True, cwd=REPO)
    return p.returncode, p.stdout


def mutate(name, fn):
    work = os.path.join(HERE, "mut-" + name)
    if os.path.exists(work):
        shutil.rmtree(work)
    shutil.copytree(R96, work)
    fn(work)
    rc, out = run(work)
    verdict = [l for l in out.splitlines() if l.startswith("VERDICT:")]
    print("MUTATION %-28s exit=%d %s" % (name, rc, verdict[0] if verdict else "?"))
    for l in out.splitlines():
        if l.strip().startswith("FAIL"):
            print("      " + l.strip()[:150])
    return rc


def swap_keys(path):
    with open(path) as fh:
        rows = json.load(fh)
    r = rows[0]
    keys = list(r.keys())
    keys[0], keys[1] = keys[1], keys[0]
    rows[0] = {k: r[k] for k in keys}
    with open(path, "w") as fh:
        json.dump(rows, fh, indent=2)


def change_value(path):
    with open(path) as fh:
        rows = json.load(fh)
    rows[3]["description"] = rows[3]["description"] + " (mutated)"
    with open(path, "w") as fh:
        json.dump(rows, fh, indent=2)


def drop_inherited_row(path):
    with open(path) as fh:
        rows = json.load(fh)
    del rows[2]
    with open(path, "w") as fh:
        json.dump(rows, fh, indent=2)


print("CONTROL 0: unmutated delivered fixture")
rc0, out0 = run(R96)
print("  exit=%d %s" % (rc0, [l for l in out0.splitlines() if l.startswith("VERDICT:")][0]))

rc1 = mutate("entities-key-order", lambda w: swap_keys(os.path.join(w, "entities.json")))
rc2 = mutate("timeline-value", lambda w: change_value(os.path.join(w, "timeline.json")))
rc3 = mutate("sources-drop-row", lambda w: drop_inherited_row(os.path.join(w, "sources.json")))

ok = (rc0 == 0 and rc1 == 1 and rc2 == 1 and rc3 == 1)
print("CONTROL:", "PASS" if ok else "FAIL", "(clean exit 0; each mutation exit 1)")
sys.exit(0 if ok else 1)
