#!/usr/bin/env python3
"""Demonstrate BR-01 prose half against r98 baseline bytes, in a private mirror.

Does not touch lane files. Tool ROOT is parents[2] of the script, so the
mirror root must contain corpus/tools/dependency_freeze.py and the fixture
at the pin's repo-relative path.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = LANE / ".ufo/waves/round-99/seats/V38-scratch"
BASE = "4265df5"
MIRROR = SCR / "prose-before-mirror"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def main():
    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    tool_dir = MIRROR / "corpus/tools"
    tool_dir.mkdir(parents=True)
    tool = tool_dir / "dependency_freeze.py"
    contract = tool_dir / "dependency-freeze-contract.json"
    tool.write_bytes(subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency_freeze.py"], cwd=LANE))
    contract.write_bytes(subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"], cwd=LANE))
    fix = MIRROR / "corpus/fixtures/r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", fix)
    excerpt = fix / "fictional-excerpts.md"
    raw = excerpt.read_text(encoding="utf-8")
    # Remove a dependency-ish prose token if present; otherwise append-delete a clause.
    needle = "depends"
    if needle in raw.lower():
        # drop the first line containing the word
        lines = raw.splitlines(keepends=True)
        dropped = False
        out = []
        for line in lines:
            if not dropped and needle in line.lower():
                dropped = True
                continue
            out.append(line)
        excerpt.write_text("".join(out), encoding="utf-8")
        how = "dropped first line containing 'depends'"
    else:
        excerpt.write_text(raw.replace("open", "OPEN", 1) if "open" in raw else raw + "\n<!-- tamper -->\n", encoding="utf-8")
        how = "token replace or trailing comment"
    print("TAMPER", how)
    print("excerpt sha before/after recorded in mirror only")
    code, out, err = run([sys.executable, str(tool), str(fix)], MIRROR)
    print("--- baseline verify after prose tamper ---")
    print(out)
    if err.strip():
        print("STDERR", err)
    print("EXIT", code)
    # also show clean control
    shutil.rmtree(fix)
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", fix)
    code2, out2, err2 = run([sys.executable, str(tool), str(fix)], MIRROR)
    print("--- baseline verify control ---")
    print(out2)
    print("EXIT", code2)


if __name__ == "__main__":
    main()
