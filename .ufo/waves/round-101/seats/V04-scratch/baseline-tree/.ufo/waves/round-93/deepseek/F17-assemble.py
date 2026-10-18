#!/usr/bin/env python3
"""F17 seat: assemble the machine-readable support-receipt record.

Reads the persisted F17-receipts/*.txt stdout/stderr captures plus the
cluster inputs at the judged candidate, and writes F17-support-receipts.json.
Read-only over product/source; stdlib only.
"""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEEPSEEK = Path(__file__).resolve().parent
RECEIPTS = DEEPSEEK / "F17-receipts"

FAMILIES = {
    "r87": dict(cluster="corpus/fixtures/r87-myth-cluster", expect_json=14, expect_editorial=8,
                expect_source="14/14", expect_editorial_hits="8/8", expect_retelling="0 entries"),
    "r88": dict(cluster="corpus/fixtures/r88-m3-maya-cluster", expect_json=10, expect_editorial=2,
                expect_source="10/10", expect_editorial_hits="2/2", expect_retelling="0 entries"),
    "r89": dict(cluster="corpus/fixtures/r89-inspiration-paraphrase", expect_json=1, expect_editorial=0,
                expect_source="0/0", expect_editorial_hits="0/0", expect_retelling="1 entries"),
    "r93": dict(cluster="corpus/fixtures/r93-m2-kojiki-cluster", expect_json=12, expect_editorial=3,
                expect_source="12/12", expect_editorial_hits="3/3", expect_retelling="0 entries"),
}

RECEIPT_LINE = re.compile(r"^SOURCE-SUPPORT (\d+/\d+); EDITORIAL-ANCHORS (\d+/\d+); "
                          r"RETELLING-SUPPORT-ONLY (\d+ entries \([^)]*\)); MODES (\d+/\d+); "
                          r"VALIDATED-ROWS (\d+/\d+)$", re.MULTILINE)
INVENTORY_LINE = re.compile(r"^INVENTORY JSON-FACTS (\d+)/(\d+); EDITORIAL-ROWS (\d+)/(\d+); "
                            r"TOTAL-ROWS (\d+)/(\d+); DISTINCT-ANCHORS (\d+)/(\d+)$", re.MULTILINE)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(cluster_rel):
    cluster = ROOT / cluster_rel
    files = sorted(p for p in cluster.rglob("*") if p.is_file())
    return {str(p.relative_to(ROOT)): sha256(p) for p in files}


def main():
    checker = ROOT / "corpus/tools/support_check.py"
    payload = {
        "seat": "F17",
        "role": "receipts judge",
        "candidate_commit": "4780cf088ab338f42b85739517aa237c968c4aea",
        "pre_round_baseline": "87779a00f25bd1855ede479e490123843e5f056e",
        "original_work_commit": "65838f867d6ece8e7b8bdcc4ffc667a08a1b785e",
        "checker": {
            "path": "corpus/tools/support_check.py",
            "sha256": sha256(checker),
            "git_blob": "a69ae9d27ad1e848c3188fa832352d00b7c0ffc7",
            "blob_identical_at": ["87779a00f25bd1855ede479e490123843e5f056e",
                                  "65838f867d6ece8e7b8bdcc4ffc667a08a1b785e",
                                  "4780cf088ab338f42b85739517aa237c968c4aea"],
            "last_change_commit": "c4d4823",
        },
        "families": {},
        "all_pass": True,
        "all_expectations_met": True,
    }
    for name, spec in FAMILIES.items():
        stdout = (RECEIPTS / f"F17-{name}.stdout.txt").read_text(encoding="utf-8")
        stderr = (RECEIPTS / f"F17-{name}.stderr.txt").read_text(encoding="utf-8")
        receipt = RECEIPT_LINE.search(stdout)
        inventory = INVENTORY_LINE.search(stdout)
        if receipt is None or inventory is None:
            raise SystemExit(f"{name}: could not parse receipt lines")
        observed = dict(source=receipt.group(1), editorial=receipt.group(2),
                        retelling=receipt.group(3), modes=receipt.group(4),
                        validated=receipt.group(5))
        json_facts, json_declared = int(inventory.group(1)), int(inventory.group(2))
        editorial_rows, editorial_declared = int(inventory.group(3)), int(inventory.group(4))
        result_line = [line for line in stdout.splitlines()
                       if line.startswith("RESULT ")][-1]
        entry = {
            "cluster": spec["cluster"],
            "command": f"python3 corpus/tools/support_check.py {spec['cluster']}",
            "observed_exit": 0 if result_line == "RESULT PASS" else 1,
            "stderr": stderr,
            "stdout_sha256": hashlib.sha256(stdout.encode("utf-8")).hexdigest(),
            "result_line": result_line,
            "inventory_observed": {"json_facts": json_facts, "declared_json_facts": json_declared,
                                   "editorial_rows": editorial_rows,
                                   "declared_editorial_rows": editorial_declared},
            "receipt_observed": observed,
            "declared_expectation": {"json_facts": spec["expect_json"],
                                     "editorial_rows": spec["expect_editorial"],
                                     "source_support": spec["expect_source"],
                                     "editorial_anchors": spec["expect_editorial_hits"],
                                     "retelling": spec["expect_retelling"]},
            "matches_declared_expectation": (
                json_facts == spec["expect_json"]
                and editorial_rows == spec["expect_editorial"]
                and observed["source"] == spec["expect_source"]
                and observed["editorial"] == spec["expect_editorial_hits"]
                and observed["retelling"].startswith(spec["expect_retelling"])
                and stderr == ""
                and result_line in {"RESULT PASS", "RESULT PASS WITH WARNINGS"}
            ),
            "input_sha256": inputs(spec["cluster"]),
            "stdout_full": stdout,
        }
        payload["families"][name] = entry
        payload["all_pass"] = payload["all_pass"] and entry["observed_exit"] == 0
        payload["all_expectations_met"] = payload["all_expectations_met"] and entry["matches_declared_expectation"]
    (DEEPSEEK / "F17-support-receipts.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("all_pass", payload["all_pass"], "all_expectations_met", payload["all_expectations_met"])
    for name, entry in payload["families"].items():
        print(name, entry["result_line"], "exit", entry["observed_exit"],
              "source", entry["receipt_observed"]["source"],
              "editorial", entry["receipt_observed"]["editorial"],
              "retelling", entry["receipt_observed"]["retelling"],
              "match", entry["matches_declared_expectation"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
