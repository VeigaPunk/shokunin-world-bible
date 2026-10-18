#!/usr/bin/env python3
"""V01 scratch harness: build mirrors and run the SELF-TEST-MISMATCH probes.

Usage:
  python3 harness.py build <mirror> <tool_src> <contract_src> [fixture_src]
  python3 harness.py perturb-exit <mirror> <case> <new_exit>
  python3 harness.py drop-case <mirror> <case>
  python3 harness.py neutralize-exit <mirror>
  python3 harness.py run <mirror>            # runs --self-test, prints exit
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE16 = [
    "clean", "reduction_edge_drop", "addition_edge_phantom", "event_removed",
    "event_endpoint_change", "relation_endpoint_flip", "relation_removed",
    "relation_added", "digest_tamper", "malformed_json", "missing_timeline",
    "unpinned_fixture", "missing_fixture", "invalid_arguments", "scope_refused",
    "path_mismatch",
]


def build(mirror, tool_src, contract_src, fixture_src=None):
    mirror = Path(mirror)
    if mirror.exists():
        shutil.rmtree(mirror)
    (mirror / "corpus/tools").mkdir(parents=True)
    (mirror / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(tool_src, mirror / "corpus/tools/dependency_freeze.py")
    shutil.copy2(contract_src, mirror / "corpus/tools/dependency-freeze-contract.json")
    src = Path(fixture_src) if fixture_src else REPO / "corpus/fixtures/r95-crossing-aftermath"
    shutil.copytree(src, mirror / "corpus/fixtures/r95-crossing-aftermath")
    print(f"BUILT {mirror}")
    return 0


def load_contract(mirror):
    p = Path(mirror) / "corpus/tools/dependency-freeze-contract.json"
    return p, json.loads(p.read_text(encoding="utf-8"))


def save_contract(p, data):
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def perturb_exit(mirror, case, new_exit):
    p, data = load_contract(mirror)
    old = data["self_test"]["expected"][case]["exit"]
    data["self_test"]["expected"][case]["exit"] = int(new_exit)
    save_contract(p, data)
    print(f"PERTURBED {case}: exit {old} -> {new_exit}")
    return 0


def drop_case(mirror, case):
    p, data = load_contract(mirror)
    if case == "NEW":
        keys = sorted(set(data["self_test"]["expected"]) - set(BASE16))
        if len(keys) != 1:
            print(f"NEW-CASE-DISCOVERY n={len(keys)} keys={keys}")
            return 3
        case = keys[0]
    removed = data["self_test"]["expected"].pop(case, None)
    save_contract(p, data)
    print(f"DROPPED {case} (was {removed is not None})")
    return 0


def neutralize_exit(mirror):
    """Revert the SELF-TEST-MISMATCH emit+return to the r97 exit-1 convention."""
    p = Path(mirror) / "corpus/tools/dependency_freeze.py"
    text = p.read_text(encoding="utf-8")
    block = ('        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])\n'
             '        return 2\n')
    r97 = ('        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])\n'
           '        return 1\n')
    if block not in text:
        print("NEUTRALIZE: block not found")
        return 3
    text = text.replace(block, r97, 1)
    p.write_text(text, encoding="utf-8")
    print("NEUTRALIZED emit(2->1)+return(2->1) for SELF-TEST-MISMATCH (r97 form)")
    return 0


def run(mirror):
    tool = Path(mirror) / "corpus/tools/dependency_freeze.py"
    r = subprocess.run([sys.executable, str(tool), "--self-test"],
                       cwd=REPO, capture_output=True, text=True)
    print(f"EXIT={r.returncode}")
    print("--- stdout ---")
    print(r.stdout.rstrip())
    if r.stderr.strip():
        print("--- stderr ---")
        print(r.stderr.rstrip())
    return 0


def parity(mirror):
    p, data = load_contract(mirror)
    exp = set(data["self_test"]["expected"])
    tool_text = (Path(mirror) / "corpus/tools/dependency_freeze.py").read_text(encoding="utf-8")
    start = tool_text.index("FROZEN_CASES = (")
    end = tool_text.index(")", start)
    frozen = set()
    for line in tool_text[start:end].splitlines()[1:]:
        line = line.strip().strip(',').strip('"')
        if line:
            frozen.add(line)
    new = sorted(exp - set(BASE16))
    print(f"FROZEN_CASES n={len(frozen)} contract expected n={len(exp)} identical={frozen == exp}")
    print(f"NEW case(s): {new}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1]
    args = sys.argv[2:]
    rc = {"build": build, "perturb-exit": perturb_exit, "drop-case": drop_case,
          "neutralize-exit": neutralize_exit, "run": run, "parity": parity}[cmd](*args)
    sys.exit(rc)
