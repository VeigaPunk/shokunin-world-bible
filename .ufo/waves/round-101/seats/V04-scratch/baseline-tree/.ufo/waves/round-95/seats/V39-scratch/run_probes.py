#!/usr/bin/env python3
"""V39: run the delivered map_obligations on every probe copy; check expectations.

Expectations (pre-registered before seeing P1's revision):
  unmutated r88          -> exit 0, no FINDING lines.
  raw-mut/<slug>         -> exit 1, exactly one finding mentioning the slug's
                            pointer (source-side mismatch), nothing else.
  raw-mut-all            -> exit 1, one finding per enumerated pointer.
  row-drop/<p1..t2>      -> exit 1, exactly one finding mentioning that row's
                            pointer (missing side), nothing else.
  row-drop/s1, s2 and editorial-drop -> OBSERVED (editorial semantics).
Records raw stdout for every run into probes-results.json.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SCRATCH = Path(__file__).resolve().parent
PROBES = SCRATCH / "probes"
TOOL = ROOT / "corpus/tools/map_obligations.py"

OBLIGATIONS = [
    ("entities-0-first", "entities.json#/0/first_appearance"),
    ("entities-0-claim-0", "entities.json#/0/claims/0"),
    ("entities-1-first", "entities.json#/1/first_appearance"),
    ("entities-1-claim-0", "entities.json#/1/claims/0"),
    ("entities-2-first", "entities.json#/2/first_appearance"),
    ("entities-2-claim-0", "entities.json#/2/claims/0"),
    ("entities-3-first", "entities.json#/3/first_appearance"),
    ("entities-3-claim-0", "entities.json#/3/claims/0"),
    ("timeline-0", "timeline.json#/0"),
    ("timeline-1", "timeline.json#/1"),
]
ROW_POINTERS = {
    "p1": "entities.json#/0/first_appearance", "p2": "entities.json#/1/first_appearance",
    "p3": "entities.json#/2/first_appearance", "p4": "entities.json#/3/first_appearance",
    "e1": "entities.json#/0/claims/0", "e2": "entities.json#/1/claims/0",
    "e3": "entities.json#/2/claims/0", "e4": "entities.json#/3/claims/0",
    "t1": "timeline.json#/0", "t2": "timeline.json#/1",
}


def run(tool, target):
    proc = subprocess.run([sys.executable, str(tool), str(target)],
                          cwd=ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def findings(out):
    return [line[len("FINDING "):] for line in out.splitlines() if line.startswith("FINDING ")]


def main():
    results = {"tool_sha256": hashlib.sha256(TOOL.read_bytes()).hexdigest()}
    failures = []

    def record(name, code, out, err):
        entry = {"exit": code, "stdout": out, "stderr": err, "findings": findings(out)}
        results[name] = entry
        return entry

    code, out, err = run(TOOL, "corpus/fixtures/r88-m3-maya-cluster")
    entry = record("r88-unmutated", code, out, err)
    if code != 0 or entry["findings"]:
        failures.append(f"r88-unmutated: expected exit 0 no findings, got exit {code} {entry['findings']}")

    for slug, pointer in OBLIGATIONS:
        code, out, err = run(TOOL, PROBES / "raw-mut" / slug)
        entry = record(f"raw-mut/{slug}", code, out, err)
        if code != 1 or len(entry["findings"]) != 1 or pointer not in entry["findings"][0]:
            failures.append(f"raw-mut/{slug}: expected exit 1 one finding naming {pointer}, "
                            f"got exit {code} {entry['findings']}")

    code, out, err = run(TOOL, PROBES / "raw-mut-all")
    entry = record("raw-mut-all", code, out, err)
    all_pointers = {p for _, p in OBLIGATIONS}
    seen = set()
    for line in entry["findings"]:
        for pointer in all_pointers:
            if pointer in line:
                seen.add(pointer)
    if code != 1 or len(entry["findings"]) != len(all_pointers) or seen != all_pointers:
        failures.append(f"raw-mut-all: expected exit 1 {len(all_pointers)} findings covering all pointers, "
                        f"got exit {code} n={len(entry['findings'])} seen={len(seen)}")

    for slug, pointer in ROW_POINTERS.items():
        code, out, err = run(TOOL, PROBES / "row-drop" / slug)
        entry = record(f"row-drop/{slug}", code, out, err)
        if code != 1 or len(entry["findings"]) != 1 or pointer not in entry["findings"][0]:
            failures.append(f"row-drop/{slug}: expected exit 1 one finding naming {pointer}, "
                            f"got exit {code} {entry['findings']}")

    for name, target in [("row-drop/s1", PROBES / "row-drop" / "s1"),
                         ("row-drop/s2", PROBES / "row-drop" / "s2"),
                         ("editorial-drop", PROBES / "editorial-drop")]:
        code, out, err = run(TOOL, target)
        record(name, code, out, err)

    for name, target in [("control/r87-myth-cluster", ROOT / "corpus/fixtures/r87-myth-cluster"),
                         ("control/r89-inspiration-paraphrase", ROOT / "corpus/fixtures/r89-inspiration-paraphrase"),
                         ("control/r93-m2-kojiki-cluster", ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"),
                         ("control/r94-paired-crossing", ROOT / "corpus/fixtures/r94-paired-crossing")]:
        code, out, err = run(TOOL, target)
        entry = record(name, code, out, err)
        want = 2 if "r87" in name or "r89" in name else 0
        if code != want:
            failures.append(f"{name}: expected exit {want}, got exit {code} {entry['findings']}")

    results["tool_sha256_after"] = hashlib.sha256(TOOL.read_bytes()).hexdigest()
    (SCRATCH / "probes-results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    run_count = len([k for k in results if k.startswith(("r88-", "raw-mut", "row-drop", "editorial", "control/"))])
    print(f"tool sha256={results['tool_sha256']} (after={results['tool_sha256_after']})")
    print(f"probe runs: {run_count}; failures: {len(failures)}")
    for name, entry in results.items():
        if name.startswith("tool_sha256"):
            continue
        print(f"  {name:<30} exit={entry['exit']} findings={entry['findings'] or 'none'}")
    for failure in failures:
        print("FAILURE:", failure)
    print("PROBES " + ("ALL-EXPECTATIONS-MET" if not failures else "MISMATCH"))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
