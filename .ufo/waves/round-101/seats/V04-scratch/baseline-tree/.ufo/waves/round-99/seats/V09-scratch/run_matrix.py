#!/usr/bin/env python3
"""Run the five-gate matrix on the scratch r96 mutants. Does not write corpus."""

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V09-scratch"
BASE = SCRATCH / "base" / "r96-crossing-response"
MUTANTS = SCRATCH / "mutants"
TOOL = LANE / "corpus/tools/dependency_freeze.py"
CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"
TRANS = SCRATCH / "transcripts"

CASES = (
    "control-base",
    "edge-reduction",
    "prose-word",
    "map-row-drop",
    "span-break",
    "source-id",
    "prose-word-nonanchor",
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def fixture_for(name):
    if name == "control-base":
        return BASE
    return MUTANTS / name / "r96-crossing-response"


def make_mirror(name, fixture):
    root = SCRATCH / "mirrors" / name
    if root.exists():
        shutil.rmtree(root)
    tools = root / "corpus/tools"
    dest = root / "corpus/fixtures/r96-crossing-response"
    tools.mkdir(parents=True)
    shutil.copy2(TOOL, tools / "dependency_freeze.py")
    shutil.copy2(CONTRACT, tools / "dependency-freeze-contract.json")
    shutil.copytree(fixture, dest)
    if sha256(tools / "dependency_freeze.py") != sha256(TOOL):
        raise SystemExit(f"mirror tool hash mismatch for {name}")
    if sha256(tools / "dependency-freeze-contract.json") != sha256(CONTRACT):
        raise SystemExit(f"mirror contract hash mismatch for {name}")
    return root, dest


def quote_block(cmd, code, stdout, stderr):
    lines = [f"$ {' '.join(cmd)}", f"cwd={LANE}"]
    if stdout:
        lines.append(stdout.rstrip("\n"))
    if stderr:
        lines.append("--- stderr ---")
        lines.append(stderr.rstrip("\n"))
    lines.append(f"EXIT={code}")
    return "\n".join(lines) + "\n"


def main():
    TRANS.mkdir(parents=True, exist_ok=True)
    summary = []
    live_cmd = [sys.executable, str(TOOL), str(LANE / "corpus/fixtures/r96-crossing-response")]
    code, out, err = run(live_cmd, LANE)
    (TRANS / "live-r96-freeze.txt").write_text(quote_block(live_cmd, code, out, err), encoding="utf-8")
    print(f"LIVE freeze exit={code}")
    print(out.rstrip())

    for name in CASES:
        fixture = fixture_for(name)
        if not fixture.is_dir():
            raise SystemExit(f"missing fixture {fixture}")
        mirror, mirror_fix = make_mirror(name, fixture)
        mirror_tool = mirror / "corpus/tools/dependency_freeze.py"
        commands = {
            "check_bible": [sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fixture)],
            "support_check": [sys.executable, str(LANE / "corpus/tools/support_check.py"), str(fixture)],
            "map_obligations": [sys.executable, str(LANE / "corpus/tools/map_obligations.py"), str(fixture)],
            "dependency_freeze": [sys.executable, str(mirror_tool), str(mirror_fix)],
            "boundary_default": [sys.executable, str(LANE / "corpus/tools/boundary_doc_check.py")],
        }
        exits = {}
        parts = [f"# {name}\nfixture={fixture}\nmirror_fixture={mirror_fix}\n"]
        for gate, cmd in commands.items():
            code, out, err = run(cmd, LANE)
            exits[gate] = code
            block = quote_block(cmd, code, out, err)
            parts.append(f"## {gate}\n{block}")
            print(f"{name} {gate} EXIT={code}")
        (TRANS / f"{name}.txt").write_text("\n".join(parts), encoding="utf-8")
        summary.append((name, exits))

    lines = ["case\tcheck_bible\tsupport_check\tmap_obligations\tdependency_freeze\tboundary_default"]
    for name, exits in summary:
        lines.append("\t".join([
            name,
            str(exits["check_bible"]),
            str(exits["support_check"]),
            str(exits["map_obligations"]),
            str(exits["dependency_freeze"]),
            str(exits["boundary_default"]),
        ]))
    table = "\n".join(lines) + "\n"
    (TRANS / "summary.tsv").write_text(table, encoding="utf-8")
    print(table)
    return 0


if __name__ == "__main__":
    sys.exit(main())
