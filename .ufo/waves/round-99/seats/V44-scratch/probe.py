#!/usr/bin/env python3
"""V44 independent re-derivation of three check_bible blind spots on r99-window-lapse.

Mutations run only on scratch copies. Live fixture is never written.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = REPO / "corpus/fixtures/r99-window-lapse"
CHECKER = REPO / "corpus/fixtures/check_bible.py"
SCRATCH = REPO / ".ufo/waves/round-99/seats/V44-scratch/copies"
GATES = [
    ("check_bible", [sys.executable, str(CHECKER)]),
    ("map_obligations", [sys.executable, str(REPO / "corpus/tools/map_obligations.py")]),
    ("support_check", [sys.executable, str(REPO / "corpus/tools/support_check.py")]),
    ("dependency_freeze", [sys.executable, str(REPO / "corpus/tools/dependency_freeze.py")]),
]
EVENT = "clerk-lapse-recorded"
WRONG_EARLIER = "acknowledgment-aru-records"


def run(cmd, directory):
    proc = subprocess.run(cmd + [str(directory)], cwd=REPO, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def dump(label, code, out, err):
    print(f"===== {label} exit={code} =====")
    print(out, end="" if out.endswith("\n") or not out else "\n")
    if err.strip():
        print("--- stderr ---")
        print(err, end="" if err.endswith("\n") else "\n")


def mutate_empty(tl):
    for row in tl:
        if row.get("id") == EVENT:
            row["depends_on"] = []
            return
    raise SystemExit(f"missing {EVENT}")


def mutate_wrong(tl):
    for row in tl:
        if row.get("id") == EVENT:
            row["depends_on"] = [WRONG_EARLIER]
            return
    raise SystemExit(f"missing {EVENT}")


def mutate_delete(tl):
    before = len(tl)
    tl[:] = [row for row in tl if row.get("id") != EVENT]
    if len(tl) != before - 1:
        raise SystemExit(f"delete missed {EVENT}")


def main():
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir(parents=True)
    cases = [
        ("baseline", None),
        ("empty-depends_on", mutate_empty),
        ("wrong-earlier-edge", mutate_wrong),
        ("deleted-terminal", mutate_delete),
    ]
    for name, mutate in cases:
        dest = SCRATCH / name
        shutil.copytree(SRC, dest)
        if mutate is not None:
            path = dest / "timeline.json"
            rows = json.loads(path.read_text(encoding="utf-8"))
            mutate(rows)
            path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
        print(f"\n########## CASE {name} ##########")
        for gate, cmd in GATES:
            code, out, err = run(cmd, dest)
            dump(f"{name}/{gate}", code, out, err)
    return 0


if __name__ == "__main__":
    sys.exit(main())
