#!/usr/bin/env python3
"""V44 secondary C1 probes on a DELIVERED tool+contract pair (read-only copies).

Runs in a scratch probe tree; never touches corpus/tools.

  A. baseline: `--self-test` on the delivered pair           -> expect PASS 25/25
  B. drop-pin: remove `dual_pointer` from the copied contract -> expect ERROR
     self_test_contract ("contract drops implemented self-test cases: dual_pointer")
  C. load-bearing: neutralize dual_pointer emission in the copied tool
     (parse_pointer_cell returns mention None) then `--self-test` -> expect ERROR
     self_test_mismatch (dual_pointer case now exits 0).

Usage: python3 pin-probes-v44.py <delivered-tool> <delivered-contract> <probe-root>
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path


def run_self_test(tool):
    result = subprocess.run(
        [sys.executable, str(tool), "--self-test"],
        capture_output=True, text=True, check=False,
    )
    return result.returncode, result.stdout, result.stderr


def main():
    tool_src = Path(sys.argv[1]).resolve()
    contract_src = Path(sys.argv[2]).resolve()
    root = Path(sys.argv[3]).resolve()
    if root.exists():
        shutil.rmtree(root)

    def stage(name, tool_bytes=None, contract_obj=None):
        d = root / name
        d.mkdir(parents=True)
        tool = d / "map_obligations.py"
        tool.write_bytes(tool_bytes if tool_bytes is not None else tool_src.read_bytes())
        contract = d / "map-obligations-contract.json"
        if contract_obj is None:
            contract.write_bytes(contract_src.read_bytes())
        else:
            contract.write_text(json.dumps(contract_obj, indent=2) + "\n", encoding="utf-8")
        return tool

    # A. baseline.
    tool_a = stage("A_baseline")
    code_a, out_a, err_a = run_self_test(tool_a)
    last_a = [line for line in out_a.splitlines() if line.startswith(("SELF-TEST CASES", "RESULT", "FINDING"))]
    print("A_baseline", "exit=", code_a)
    for line in last_a[-4:]:
        print("   ", line)

    # B. drop-pin.
    contract_obj = json.loads(contract_src.read_text(encoding="utf-8"))
    contract_obj["self_test"]["cases"] = [
        c for c in contract_obj["self_test"]["cases"] if c["id"] != "dual_pointer"
    ]
    tool_b = stage("B_drop_pin", contract_obj=contract_obj)
    code_b, out_b, err_b = run_self_test(tool_b)
    print("B_drop_pin", "exit=", code_b)
    for line in out_b.splitlines()[-3:]:
        print("   ", line)

    # C. load-bearing: neutralize the emission.
    tool_bytes = tool_src.read_bytes()
    marker = b"return translated, second_pointer_mention(tail)"
    if tool_bytes.count(marker) != 1:
        print("C_load_bearing SKIP marker count", tool_bytes.count(marker))
    else:
        neutralized = tool_bytes.replace(marker, b"return translated, None")
        tool_c = stage("C_load_bearing", tool_bytes=neutralized)
        code_c, out_c, err_c = run_self_test(tool_c)
        print("C_load_bearing", "exit=", code_c)
        for line in out_c.splitlines()[-6:]:
            print("   ", line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
