#!/usr/bin/env python3
"""F17 seat: negative/positive controls for corpus/tools/support_check.py.

Builds tiny own copies under F17-scratch/ and runs the unchanged delivered
checker against each, recording exact exit/stdout/stderr. Stdlib only.
"""

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CHECKER = ROOT / "corpus/tools/support_check.py"
SCRATCH = Path(__file__).resolve().parent / "F17-scratch"

EXCERPT = """# Tiny control excerpt

Delivery mode (R9): {mode}

The bell rang once at the west stair.
"""

MAP = """# Tiny control map

**Expected inventory:** {json_facts} JSON facts; 0 editorial rows; {total} total mapped rows; {anchors} distinct excerpt anchors.

## JSON facts (1 row)

| ID | JSON fact pointer | In-world source | Excerpt path | R9 delivery mode | Exact anchor |
|---|---|---|---|---|---|
| E1 | `entities.json#/0/claims/0` | `tiny-source` | `tiny-excerpt.md:{span}` | `{map_mode}` | `{anchor}` |
"""

CASES = {
    "positive": dict(excerpt_mode="verbatim", map_mode="verbatim", span=5,
                     anchor="The bell rang once at the west stair",
                     json_facts=1, total=1, anchors=1, expect=0),
    "anchor_missing": dict(excerpt_mode="verbatim", map_mode="verbatim", span=5,
                           anchor="The bell rang twice at the west stair",
                           json_facts=1, total=1, anchors=1, expect=1),
    "mode_mismatch": dict(excerpt_mode="paraphrase", map_mode="verbatim", span=5,
                          anchor="The bell rang once at the west stair",
                          json_facts=1, total=1, anchors=1, expect=1),
    "inventory_mismatch": dict(excerpt_mode="verbatim", map_mode="verbatim", span=5,
                               anchor="The bell rang once at the west stair",
                               json_facts=2, total=2, anchors=2, expect=1),
    "span_outside": dict(excerpt_mode="verbatim", map_mode="verbatim", span=2,
                         anchor="The bell rang once at the west stair",
                         json_facts=1, total=1, anchors=1, expect=1),
    "retelling_missing": dict(excerpt_mode="paraphrase", map_mode="paraphrase", span=5,
                              anchor="The bell rang twice at the west stair",
                              json_facts=1, total=1, anchors=1, expect=0),
}

DELIVERED_COPY = dict(
    source=ROOT / "corpus/fixtures/r93-m2-kojiki-cluster",
    old_anchor="M-17 identifies Teva as the initial recorder",
    new_anchor="M-17 identifies Teva as the final recorder",
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(name, case, checker_hash_before):
    case_dir = SCRATCH / ("F17-case-" + name)
    if case_dir.exists():
        shutil.rmtree(case_dir)
    case_dir.mkdir(parents=True)
    (case_dir / "tiny-excerpt.md").write_text(EXCERPT.format(mode=case["excerpt_mode"]), encoding="utf-8")
    (case_dir / "claim-to-excerpt-map.md").write_text(MAP.format(**case), encoding="utf-8")
    result = subprocess.run([sys.executable, str(CHECKER), str(case_dir)],
                            capture_output=True, text=True)
    checker_hash_after = sha256(CHECKER)
    record = {
        "case": name,
        "command": f"python3 corpus/tools/support_check.py {case_dir.relative_to(ROOT)}",
        "checker_sha256_before": checker_hash_before,
        "checker_sha256_after": checker_hash_after,
        "checker_unchanged": checker_hash_before == checker_hash_after,
        "expected_exit": case["expect"],
        "observed_exit": result.returncode,
        "exit_matches_expectation": result.returncode == case["expect"],
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    (SCRATCH / f"F17-{name}.stdout.txt").write_text(result.stdout, encoding="utf-8")
    (SCRATCH / f"F17-{name}.stderr.txt").write_text(result.stderr, encoding="utf-8")
    return record


def run_delivered_copy(checker_hash_before):
    case_dir = SCRATCH / "F17-case-delivered-r93-copy"
    if case_dir.exists():
        shutil.rmtree(case_dir)
    shutil.copytree(DELIVERED_COPY["source"], case_dir)
    map_path = case_dir / "claim-excerpt-map.md"
    text = map_path.read_text(encoding="utf-8")
    assert DELIVERED_COPY["old_anchor"] in text
    map_path.write_text(text.replace(DELIVERED_COPY["old_anchor"], DELIVERED_COPY["new_anchor"]), encoding="utf-8")
    result = subprocess.run([sys.executable, str(CHECKER), str(case_dir)],
                            capture_output=True, text=True)
    record = {
        "case": "delivered_r93_copy_anchor_mutated",
        "command": f"python3 corpus/tools/support_check.py {case_dir.relative_to(ROOT)}",
        "note": "copy of the delivered r93 cluster with one anchor string changed; excerpt untouched",
        "checker_sha256_before": checker_hash_before,
        "checker_sha256_after": sha256(CHECKER),
        "checker_unchanged": checker_hash_before == sha256(CHECKER),
        "expected_exit": 1,
        "observed_exit": result.returncode,
        "exit_matches_expectation": result.returncode == 1,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    (SCRATCH / "F17-delivered-copy.stdout.txt").write_text(result.stdout, encoding="utf-8")
    (SCRATCH / "F17-delivered-copy.stderr.txt").write_text(result.stderr, encoding="utf-8")
    return record


def main():
    SCRATCH.mkdir(exist_ok=True)
    before = sha256(CHECKER)
    records = [run_case(name, case, before) for name, case in CASES.items()]
    records.append(run_delivered_copy(before))
    payload = {
        "seat": "F17",
        "checker_path": "corpus/tools/support_check.py",
        "checker_sha256": before,
        "all_exit_matches_expectation": all(r["exit_matches_expectation"] for r in records),
        "all_checker_unchanged": all(r["checker_unchanged"] for r in records),
        "controls": records,
    }
    (SCRATCH / "F17-negative-controls.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for record in records:
        print(f"{record['case']}: expected_exit={record['expected_exit']} "
              f"observed_exit={record['observed_exit']} "
              f"match={record['exit_matches_expectation']}")
    print("ALL_MATCH", payload["all_exit_matches_expectation"])
    return 0 if payload["all_exit_matches_expectation"] and payload["all_checker_unchanged"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
