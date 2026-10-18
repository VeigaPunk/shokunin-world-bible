#!/usr/bin/env python3
"""F23 independent before/after + honesty probes for the C2 mapping checker.

Writes only inside this scratch directory (temp dirs removed at exit).
"""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SCRATCH = Path(__file__).resolve().parent
SUPPORT = ROOT / "corpus/tools/support_check.py"
MAPOBL = ROOT / "corpus/tools/map_obligations.py"
BASELINE_COMMIT = "9c2eea3"


def run(cmd, cwd=ROOT):
    proc = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout, proc.stderr


def terminal(stdout):
    return [line for line in stdout.splitlines() if line.startswith("RESULT ")]


def findings(stdout):
    return [line for line in stdout.splitlines() if line.startswith("FINDING ")]


def report(label, code, stdout, stderr, expect_code, expect_terminal=None, expect_findings=None):
    term = terminal(stdout)
    found = findings(stdout)
    ok = code == expect_code and not stderr and len(term) == 1
    if expect_terminal is not None:
        ok = ok and term == [f"RESULT {expect_terminal}"]
    if expect_findings is not None:
        ok = ok and found == expect_findings
    print(f"[{'PASS' if ok else 'CHECK'}] {label}: exit={code} terminal={term} findings={found}")
    if stderr.strip():
        print(f"        stderr: {stderr.strip()[:300]}")
    if not ok:
        print("        --- full stdout ---")
        print("        " + stdout.replace("\n", "\n        ")[:1200])
    return ok


def clone(src, dst):
    shutil.copytree(src, dst)
    return dst


def append_unmapped_claim(cluster, source_id):
    path = cluster / "entities.json"
    entities = json.loads(path.read_text(encoding="utf-8"))
    entities[0]["claims"].append({"statement": "F23 isolated unmapped raw claim", "source_id": source_id})
    path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    return len(entities[0]["claims"]) - 1


results = []

with tempfile.TemporaryDirectory(prefix="f23-", dir=SCRATCH) as tmp:
    tmp = Path(tmp)

    # ---- 0. baseline support_check.py byte identity ----
    baseline_bytes = subprocess.run(
        ["git", "show", f"{BASELINE_COMMIT}:corpus/tools/support_check.py"],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout
    head_bytes = SUPPORT.read_bytes()
    same = hashlib.sha256(baseline_bytes).hexdigest() == hashlib.sha256(head_bytes).hexdigest()
    print(f"[{'PASS' if same else 'FAIL'}] support_check.py bytes identical baseline->HEAD "
          f"sha256={hashlib.sha256(head_bytes).hexdigest()[:16]}")
    baseline_support = tmp / "support_check_baseline.py"
    baseline_support.write_bytes(baseline_bytes)
    results.append(same)

    # ---- 1. before/after on r93 clone ----
    for fixture in ("r93-m2-kojiki-cluster", "r94-paired-crossing"):
        cluster = clone(ROOT / f"corpus/fixtures/{fixture}", tmp / fixture)
        claim_index = append_unmapped_claim(cluster, "f23-injected-source")
        print(f"--- {fixture}: appended entities.json#/0/claims/{claim_index} "
              f"(source_id=f23-injected-source), no map row added ---")
        code, out, err = run([sys.executable, "-B", SUPPORT, cluster])
        results.append(report(f"{fixture} BEFORE lexical support_check (HEAD==baseline)", code, out, err, 0, "PASS"))
        code, out, err = run([sys.executable, "-B", baseline_support, cluster])
        results.append(report(f"{fixture} BEFORE lexical support_check (git {BASELINE_COMMIT} copy)",
                              code, out, err, 0, "PASS"))
        code, out, err = run([sys.executable, "-B", MAPOBL, cluster])
        results.append(report(f"{fixture} AFTER map_obligations", code, out, err, 1, "FAIL",
                              [f"FINDING missing_obligation: entities.json#/0/claims/{claim_index} has no map row"]))

    # ---- 2. clean runs on unmodified fixtures ----
    for fixture, raw in (("r93-m2-kojiki-cluster", 12), ("r94-paired-crossing", 14)):
        code, out, err = run([sys.executable, "-B", MAPOBL, ROOT / f"corpus/fixtures/{fixture}"])
        expected_line = f"OBLIGATIONS raw={raw} mapped={raw}"
        ok = report(f"{fixture} clean run", code, out, err, 0, "PASS")
        ok = ok and expected_line in out
        print(f"        count line present ({expected_line}): {expected_line in out}")
        results.append(ok)

    # ---- 3. honesty probes: could-not-evaluate must never be empty-success ----
    probe = clone(ROOT / "corpus/fixtures/r93-m2-kojiki-cluster", tmp / "probe")

    # 3a. zero-row JSON facts table
    p = clone(probe, tmp / "p_zero_rows")
    map_path = p / "claim-excerpt-map.md"
    text = map_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    head = [ln for ln in lines if ln.startswith("## JSON facts")]
    new = []
    in_json = False
    for ln in lines:
        if ln.startswith("## "):
            in_json = ln.startswith("## JSON facts")
            new.append(ln)
            continue
        if in_json and ln.lstrip().startswith("|"):
            continue
        new.append(ln)
    map_path.write_text("\n".join(new) + "\n", encoding="utf-8")
    code, out, err = run([sys.executable, "-B", MAPOBL, p])
    results.append(report("probe zero-row JSON facts table", code, out, err, 2, "ERROR"))

    # 3b. JSON facts section absent entirely
    p = clone(probe, tmp / "p_no_section")
    map_path = p / "claim-excerpt-map.md"
    text = map_path.read_text(encoding="utf-8").replace("## JSON facts", "## Some other facts")
    map_path.write_text(text, encoding="utf-8")
    code, out, err = run([sys.executable, "-B", MAPOBL, p])
    results.append(report("probe JSON facts section absent", code, out, err, 2, "ERROR"))

    # 3c. raw claim with a renamed source field (unknown shape must not silently vanish)
    p = clone(probe, tmp / "p_renamed_field")
    path = p / "entities.json"
    entities = json.loads(path.read_text(encoding="utf-8"))
    entities[0]["claims"].append({"statement": "renamed field", "source": "m2-record-archive"})
    path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    code, out, err = run([sys.executable, "-B", MAPOBL, p])
    results.append(report("probe raw claim without source_id (renamed field)", code, out, err, 2, "ERROR"))

    # 3d. empty raw arrays + empty map table -> must not be PASS
    p = clone(probe, tmp / "p_empty_raw")
    for name in ("entities.json", "relations.json", "timeline.json"):
        (p / name).write_text("[]\n", encoding="utf-8")
    code, out, err = run([sys.executable, "-B", MAPOBL, p])
    results.append(report("probe empty raw arrays vs non-empty map", code, out, err, 1, "FAIL"))

    # 3e. unmapped raw relation and timeline record (not just claims)
    p = clone(probe, tmp / "p_rel_timeline")
    relations = json.loads((p / "relations.json").read_text(encoding="utf-8"))
    relations.append({"from": "a", "to": "b", "type": "linked", "source_id": "f23-injected-source"})
    (p / "relations.json").write_text(json.dumps(relations, indent=2) + "\n", encoding="utf-8")
    code, out, err = run([sys.executable, "-B", MAPOBL, p])
    results.append(report("probe unmapped raw relation", code, out, err, 1, "FAIL",
                          [f"FINDING missing_obligation: relations.json#/{len(relations) - 1} has no map row"]))

    # ---- 4. self-test ----
    code, out, err = run([sys.executable, "-B", MAPOBL, "--self-test"])
    ok = report("map_obligations --self-test", code, out, err, 0, "PASS")
    n = out.count("SELF-TEST PASS")
    print(f"        SELF-TEST PASS lines: {n}")
    results.append(ok and n == 20)

print(f"\nF23 demo overall: {'PASS' if all(results) else 'FAIL'} ({sum(results)}/{len(results)} checks)")
raise SystemExit(0 if all(results) else 1)
