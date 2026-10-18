#!/usr/bin/env python3
"""Non-mutating usage-surface probe for dependency_freeze.py.

Runs from the lane root. Does not call --freeze on a real fixture directory.
Records exit, stdout, stderr, RESULT-line counts for each case.
"""
import hashlib
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = ROOT / "corpus/tools/dependency_freeze.py"
CONTRACT = ROOT / "corpus/tools/dependency-freeze-contract.json"
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V76-scratch"
OUT = SCRATCH / "usage-probe-final.txt"
FX = ROOT / "corpus/fixtures/r95-crossing-aftermath"
FILE = FX / "timeline.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(name, args):
    proc = subprocess.run(
        [sys.executable, str(TOOL), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    stdout_lines = proc.stdout.splitlines()
    stderr_lines = proc.stderr.splitlines()
    result_out = [ln for ln in stdout_lines if ln.startswith("RESULT ")]
    result_err = [ln for ln in stderr_lines if ln.startswith("RESULT ")]
    findings = [ln for ln in stdout_lines if ln.startswith("FINDING ")]
    tb = sum(1 for ln in stdout_lines + stderr_lines if "Traceback" in ln)
    return {
        "name": name,
        "args": args,
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "result_out": result_out,
        "result_err": result_err,
        "findings": findings,
        "traceback": tb,
    }


def main():
    fake = SCRATCH / "r95-crossing-aftermath"
    fake.write_text("not a directory\n", encoding="utf-8")
    missing_named = SCRATCH / "does-not-exist" / "r95-crossing-aftermath"
    cases = [
        ("no-args", []),
        ("help", ["--help"]),
        ("help-short", ["-h"]),
        ("unknown-long", ["--not-a-flag"]),
        ("unknown-short", ["-z"]),
        ("freeze-missing-arg", ["--freeze"]),
        ("freeze-empty-eq", ["--freeze="]),
        ("verify-file", [str(FILE)]),
        ("verify-file-rel", ["corpus/fixtures/r95-crossing-aftermath/timeline.json"]),
        ("verify-file-pin-basename", [str(fake)]),
        ("verify-missing-pin-basename", [str(missing_named)]),
        ("unknown-then-fixture", ["--bogus", str(FX)]),
        ("fixture-then-unknown", [str(FX), "--bogus"]),
        ("freeze-and-fixture", ["--freeze", str(FX), str(FX)]),
        ("double-dash", ["--"]),
        ("freeze-double-dash", ["--freeze", "--"]),
        ("self-test-plus-fixture", ["--self-test", str(FX)]),
        ("self-test-plus-freeze", ["--self-test", "--freeze", str(FX)]),
        ("freeze-file", ["--freeze", str(FILE)]),
        ("freeze-missing-dir", ["--freeze", str(ROOT / "corpus/fixtures/r99-does-not-exist")]),
        ("two-positionals", [str(FX), str(ROOT / "corpus/fixtures/r94-paired-crossing")]),
        ("help-with-extra", ["--help", "--freeze"]),
        ("unknown-equals", ["--nope=1"]),
        ("verify-missing-plain", [str(SCRATCH / "no-such-fixture")]),
    ]
    before_tool = sha(TOOL)
    before_contract = sha(CONTRACT)
    lines = []
    lines.append(f"TOOL {TOOL}")
    lines.append(f"TOOL_SHA_BEFORE {before_tool}")
    lines.append(f"CONTRACT_SHA_BEFORE {before_contract}")
    lines.append(f"TOOL_BYTES {TOOL.stat().st_size}")
    lines.append(f"CONTRACT_BYTES {CONTRACT.stat().st_size}")
    results = []
    for name, args in cases:
        results.append(run(name, args))
    after_tool = sha(TOOL)
    after_contract = sha(CONTRACT)
    lines.append(f"TOOL_SHA_AFTER {after_tool}")
    lines.append(f"CONTRACT_SHA_AFTER {after_contract}")
    lines.append(f"TOOL_UNCHANGED {before_tool == after_tool}")
    lines.append(f"CONTRACT_UNCHANGED {before_contract == after_contract}")
    lines.append("")
    for item in results:
        lines.append(f"===== CASE {item['name']} =====")
        shown = " ".join(item["args"]) if item["args"] else "(no args)"
        lines.append(f"CMD: python3 corpus/tools/dependency_freeze.py {shown}")
        lines.append(f"EXIT {item['exit']}")
        lines.append("--- stdout ---")
        lines.append(item["stdout"].rstrip("\n"))
        lines.append("--- stderr ---")
        lines.append(item["stderr"].rstrip("\n"))
        lines.append(f"RESULT_STDOUT_COUNT {len(item['result_out'])}")
        lines.append(f"RESULT_STDERR_COUNT {len(item['result_err'])}")
        lines.append(f"RESULT_STDOUT {item['result_out']}")
        lines.append(f"FINDING_COUNT {len(item['findings'])}")
        lines.append(f"TRACEBACK {item['traceback']}")
        lines.append("")
    # summary table
    lines.append("===== SUMMARY =====")
    for item in results:
        finding = item["findings"][0].split(":", 1)[0].replace("FINDING ", "") if item["findings"] else "-"
        nres = len(item["result_out"]) + len(item["result_err"])
        lines.append(
            f"{item['name']}\texit={item['exit']}\tresult_lines={nres}\tfinding={finding}\ttb={item['traceback']}"
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {OUT}")
    print(f"TOOL_UNCHANGED {before_tool == after_tool} CONTRACT_UNCHANGED {before_contract == after_contract}")
    if before_contract != after_contract or before_tool != after_tool:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
