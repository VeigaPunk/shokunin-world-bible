#!/usr/bin/env python3
"""Audit the exit/RESULT contract over a battery TSV produced by the V07 runner.

Each line: "<path> rc=<n> | <stdout+stderr with ~ separators>"
Checks: no stderr text, exactly one RESULT line, exit in {0,1,2},
no PASS with FINDING lines, no exit 2 without a FINDING line.
"""

import sys

VALID = {0, 1, 2}
problems = []
checked = 0
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line:
        continue
    path, _, rest = line.partition(" rc=")
    code, _, payload = rest.partition(" | ")
    lines = [part for part in payload.split("~") if part != ""]
    checked += 1
    results = [item for item in lines if item.startswith("RESULT ")]
    findings = [item for item in lines if item.startswith("FINDING ")]
    if int(code) not in VALID:
        problems.append(f"{path}: exit {code} outside 0/1/2")
    if len(results) != 1:
        problems.append(f"{path}: {len(results)} RESULT lines")
    elif results[0] not in {"RESULT PASS", "RESULT FAIL", "RESULT ERROR"}:
        problems.append(f"{path}: malformed RESULT line {results[0]!r}")
    if int(code) == 0 and findings:
        problems.append(f"{path}: exit 0 with findings {findings}")
    if int(code) == 2 and not findings:
        problems.append(f"{path}: exit 2 without a FINDING line")
    if int(code) == 1 and not findings:
        problems.append(f"{path}: exit 1 without a FINDING line")
print(f"checked {checked} runs; violations {len(problems)}")
for item in problems:
    print("VIOLATION", item)
