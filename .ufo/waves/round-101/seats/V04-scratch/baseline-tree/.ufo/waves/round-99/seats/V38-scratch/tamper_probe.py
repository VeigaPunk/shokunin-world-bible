#!/usr/bin/env python3
"""Per-file DIGEST-MISMATCH probe on a private mirror of the delivered tool.

Does not write lane corpus files. Copies tool+contract+r98 fixture into scratch.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
MIRROR = LANE / ".ufo/waves/round-99/seats/V38-scratch/tamper-mirror"
PINNED = (
    "entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json",
    "README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md", "source-excerpt.md",
)


def run(tool, fixture):
    r = subprocess.run([sys.executable, str(tool), str(fixture)], cwd=MIRROR, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def main():
    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    tool_dir = MIRROR / "corpus/tools"
    tool_dir.mkdir(parents=True)
    tool = tool_dir / "dependency_freeze.py"
    contract = tool_dir / "dependency-freeze-contract.json"
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", tool)
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json", contract)
    src = LANE / "corpus/fixtures/r98-clerk-filing"
    fix = MIRROR / "corpus/fixtures/r98-clerk-filing"
    shutil.copytree(src, fix)
    print("tool", hashlib.sha256(tool.read_bytes()).hexdigest())
    print("contract", hashlib.sha256(contract.read_bytes()).hexdigest())
    code, out, err = run(tool, fix)
    print("--- control ---")
    print(out.rstrip())
    print("EXIT", code)
    if err.strip():
        print("STDERR", err)

    # exact before-mutation: drop first line containing 'depends'
    raw = (fix / "fictional-excerpts.md").read_text(encoding="utf-8")
    lines = raw.splitlines(keepends=True)
    dropped = None
    out_lines = []
    for line in lines:
        if dropped is None and "depends" in line.lower():
            dropped = line
            continue
        out_lines.append(line)
    (fix / "fictional-excerpts.md").write_text("".join(out_lines), encoding="utf-8")
    print("--- prose drop ---")
    print("DROPPED", json.dumps(dropped))
    code, out, err = run(tool, fix)
    print(out.rstrip())
    print("EXIT", code)
    shutil.copytree(src, fix) if False else None
    shutil.rmtree(fix)
    shutil.copytree(src, fix)

    print("--- per-file newline append ---")
    for name in PINNED:
        target = fix / name
        before = target.read_bytes()
        target.write_bytes(before + b"\n")
        code, out, err = run(tool, fix)
        named = name in out
        finding = [ln for ln in out.splitlines() if ln.startswith("FINDING") or ln.startswith("RESULT")]
        print(f"{name}: exit={code} names_file={named} {' | '.join(finding)}")
        target.write_bytes(before)

    print("--- semantic edge drop still exit 1 ---")
    timeline = json.loads((fix / "timeline.json").read_text(encoding="utf-8"))
    for rec in timeline:
        if rec["id"] == "clerk-filing-open":
            rec["depends_on"] = []
    (fix / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    code, out, err = run(tool, fix)
    print(out.rstrip())
    print("EXIT", code)


if __name__ == "__main__":
    main()
