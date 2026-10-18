#!/usr/bin/env python3
"""V44 independent nine-class negative matrix for map_obligations (r97 C1).

Fresh implementation (no reuse of V47/V06/V04 harnesses). Builds a synthetic
8-obligation cluster (arden/borin, 2 entities x claims + 1 relation + 2 timeline
records) from scratch, applies one mutation per negative class on a fresh copy,
invokes the subject tool's real CLI, and records exit code + sorted FINDING IDs
+ INVENTORY receipt lines. Every case runs twice; byte-stability is checked.

Classes (nine, r94 lineage + r96/r97 C1 targets):
  N1 missing_obligation  (map row deleted, raw intact)
  N2 duplicate_mapping   (second row re-mapping a pointer)
  N3 phantom_obligation  (row naming a non-obligation pointer)
  N4 source_id_mismatch  (map source column differs from raw)
  N5 malformed_json      (timeline.json truncated)
  N6 map-path errors     (f1 missing / f2 foreign / f3 traversal / f4 dir)
  N7 schema_drift        (claim-shaped records under unexpected key)
  N8 inventory_mismatch  (claims key + its map rows deleted, declaration intact)
  N9 dual_pointer        (legacy cell naming a second pointer token)
Controls: clean base, legacy-clean, legacy-prose, canonical-note, malformed declaration.

Usage: python3 matrix-v44.py <tool-path> <out-dir> [--repeat 2]
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

SRC = "marginalia"

ENTITIES = [
    {"id": "arden", "first_appearance": SRC, "claims": [
        {"statement": "Arden keeps the tally.", "source_id": SRC},
        {"statement": "Arden dates the tally twice.", "source_id": SRC},
    ]},
    {"id": "borin", "first_appearance": SRC, "claims": [
        {"statement": "Borin countersigns the tally.", "source_id": SRC},
    ]},
]
RELATIONS = [{"from": "arden", "to": "borin", "type": "witnesses", "source_id": SRC}]
TIMELINE = [
    {"id": "t-open", "tick": 1, "entity_id": "arden", "source_id": SRC},
    {"id": "t-close", "tick": 2, "entity_id": "borin", "source_id": SRC},
]

CANON_MAP = """# V44 synthetic base cluster map

**Expected inventory:** 8 JSON facts; 0 editorial rows; 8 total mapped rows; 2 distinct excerpt anchors.

## JSON facts

| ID | JSON fact pointer and fields | In-world source ID |
|---|---|---|
| R01 | `entities.json#/0/first_appearance` (arden) | `marginalia` |
| R02 | `entities.json#/0/claims/0` | `marginalia` |
| R03 | `entities.json#/0/claims/1` | `marginalia` |
| R04 | `entities.json#/1/first_appearance` (borin) | `marginalia` |
| R05 | `entities.json#/1/claims/0` | `marginalia` |
| R06 | `relations.json#/0` | `marginalia` |
| R07 | `timeline.json#/0` | `marginalia` |
| R08 | `timeline.json#/1` | `marginalia` |
"""

LEGACY_MAP = """# V44 synthetic legacy-dialect map

**Expected inventory:** 8 JSON facts; 0 editorial rows; 8 total mapped rows; 2 distinct excerpt anchors.

## JSON facts

| ID | JSON fact and fields | In-world source ID |
|---|---|---|
| P01 | `entities[0].first_appearance` (arden) | `marginalia` |
| P02 | `entities[0].claims[0]` | `marginalia` |
| P03 | `entities[0].claims[1]` (see also `timeline[1]`) | `marginalia` |
| P04 | `entities[1].first_appearance` (borin) | `marginalia` |
| P05 | `entities[1].claims[0]` | `marginalia` |
| P06 | `relations[0]` | `marginalia` |
| P07 | `timeline[0]` | `marginalia` |
| P08 | `timeline[1]` | `marginalia` |
"""

LEGACY_DUAL_COLON = LEGACY_MAP.replace(
    "`entities[0].claims[1]` (see also `timeline[1]`)",
    "`entities[0].claims[1]`: see also `timeline[1]`",
)


def write_base(root):
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    (root / "entities.json").write_text(json.dumps(ENTITIES, indent=2) + "\n", encoding="utf-8")
    (root / "relations.json").write_text(json.dumps(RELATIONS, indent=2) + "\n", encoding="utf-8")
    (root / "timeline.json").write_text(json.dumps(TIMELINE, indent=2) + "\n", encoding="utf-8")
    (root / "claim-excerpt-map.md").write_text(CANON_MAP, encoding="utf-8")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def read_map(cluster):
    return (cluster / "claim-excerpt-map.md").read_text(encoding="utf-8")


def write_map(cluster, text):
    (cluster / "claim-excerpt-map.md").write_text(text, encoding="utf-8")


def build_cases(work):
    """Return {case_id: (cluster_dir, argv_tail)} with mutations applied in place."""
    cases = {}

    def fresh(case_id):
        cluster = work / case_id
        shutil.copytree(work / "base", cluster)
        return cluster

    # N1 missing_obligation: drop the R03 map row, raw claim intact.
    c = fresh("N1_missing_row")
    write_map(c, read_map(c).replace("| R03 | `entities.json#/0/claims/1` | `marginalia` |\n", ""))
    cases["N1_missing_row"] = (c, [str(c)])

    # N2 duplicate_mapping: second row re-mapping relations.json#/0.
    c = fresh("N2_duplicate_row")
    write_map(c, read_map(c).replace(
        "| R06 | `relations.json#/0` | `marginalia` |\n",
        "| R06 | `relations.json#/0` | `marginalia` |\n"
        "| R09 | `relations.json#/0` | `marginalia` |\n"))
    cases["N2_duplicate_row"] = (c, [str(c)])

    # N3 phantom_obligation: row naming a non-obligation pointer.
    c = fresh("N3_phantom_row")
    write_map(c, read_map(c).replace(
        "| R08 | `timeline.json#/1` | `marginalia` |\n",
        "| R08 | `timeline.json#/1` | `marginalia` |\n"
        "| X01 | `entities.json#/0/name` | `marginalia` |\n"))
    cases["N3_phantom_row"] = (c, [str(c)])

    # N4 source_id_mismatch: R01 source column differs from raw.
    c = fresh("N4_source_id_mismatch")
    write_map(c, read_map(c).replace(
        "| R01 | `entities.json#/0/first_appearance` (arden) | `marginalia` |",
        "| R01 | `entities.json#/0/first_appearance` (arden) | `ledger` |"))
    cases["N4_source_id_mismatch"] = (c, [str(c)])

    # N5 malformed_json: truncate timeline.json.
    c = fresh("N5_malformed_json")
    (c / "timeline.json").write_text("[", encoding="utf-8")
    cases["N5_malformed_json"] = (c, [str(c)])

    # N6 map-path errors.
    c = fresh("N6f1_map_missing")
    cases["N6f1_map_missing"] = (c, [str(c), "--map", "no-such-map.md"])

    outside = work / "outside"
    outside.mkdir(exist_ok=True)
    (outside / "foreign-map.md").write_text(CANON_MAP, encoding="utf-8")
    c = fresh("N6f2_foreign_path")
    cases["N6f2_foreign_path"] = (c, [str(c), "--map", str(outside / "foreign-map.md")])

    c = fresh("N6f3_traversal")
    cases["N6f3_traversal"] = (c, [str(c), "--map", "../outside/foreign-map.md"])

    c = fresh("N6f4_map_is_dir")
    (c / "mapdir").mkdir()
    cases["N6f4_map_is_dir"] = (c, [str(c), "--map", "mapdir"])

    # N7 schema_drift: claim-shaped records under an unexpected entity key.
    c = fresh("N7_schema_drift")
    entities = load_json(c / "entities.json")
    entities[0]["annotations"] = [{"statement": "Arden annotates the tally.", "source_id": SRC}]
    save_json(c / "entities.json", entities)
    cases["N7_schema_drift"] = (c, [str(c)])

    # N8 inventory_mismatch (deletion class): claims key + its rows deleted,
    # declaration untouched.
    c = fresh("N8_deletion_class")
    entities = load_json(c / "entities.json")
    del entities[0]["claims"]
    save_json(c / "entities.json", entities)
    text = read_map(c)
    text = text.replace("| R02 | `entities.json#/0/claims/0` | `marginalia` |\n", "")
    text = text.replace("| R03 | `entities.json#/0/claims/1` | `marginalia` |\n", "")
    write_map(c, text)
    cases["N8_deletion_class"] = (c, [str(c)])

    # N9 dual_pointer: legacy dialect, second token in the parenthetical note.
    c = fresh("N9_dual_pointer")
    write_map(c, LEGACY_MAP)
    cases["N9_dual_pointer"] = (c, [str(c)])

    c = fresh("N9b_dual_colon")
    write_map(c, LEGACY_DUAL_COLON)
    cases["N9b_dual_colon"] = (c, [str(c)])

    # Controls.
    c = fresh("K1_legacy_clean")
    write_map(c, LEGACY_MAP.replace(" (see also `timeline[1]`)", ""))
    cases["K1_legacy_clean"] = (c, [str(c)])

    c = fresh("K2_legacy_prose")
    write_map(c, LEGACY_MAP.replace(" (see also `timeline[1]`)", " (see the margin)"))
    cases["K2_legacy_prose"] = (c, [str(c)])

    c = fresh("K3_canonical_note")
    write_map(c, read_map(c).replace(
        "| R02 | `entities.json#/0/claims/0` | `marginalia` |",
        "| R02 | `entities.json#/0/claims/0` (see `timeline.json#/1`) | `marginalia` |"))
    cases["K3_canonical_note"] = (c, [str(c)])

    c = fresh("K4_inv_malformed")
    write_map(c, read_map(c).replace(
        "**Expected inventory:** 8 JSON facts; 0 editorial rows; 8 total mapped rows; 2 distinct excerpt anchors.",
        "**Expected inventory:** see the table below."))
    cases["K4_inv_malformed"] = (c, [str(c)])

    return cases


def run_once(tool, argv_tail):
    command = [sys.executable, str(tool), *argv_tail]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    ids = sorted(
        line[len("FINDING "):].split(":", 1)[0]
        for line in result.stdout.splitlines() if line.startswith("FINDING ")
    )
    inventory = [line for line in result.stdout.splitlines() if line.startswith("INVENTORY ")]
    result_line = [line for line in result.stdout.splitlines() if line.startswith("RESULT ")]
    return {
        "exit": result.returncode,
        "result": result_line[0] if result_line else None,
        "finding_ids": ids,
        "inventory": inventory,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tool")
    parser.add_argument("outdir")
    parser.add_argument("--repeat", type=int, default=2)
    args = parser.parse_args()

    tool = Path(args.tool).resolve()
    outdir = Path(args.outdir).resolve()
    work = outdir / "work"
    write_base(work / "base")
    cases = build_cases(work)

    report = {
        "tool": str(tool),
        "tool_sha256": hashlib.sha256(tool.read_bytes()).hexdigest(),
        "cases": {},
    }
    base_runs = [run_once(tool, [str(work / "base")]) for _ in range(args.repeat)]
    report["base"] = {
        "runs": base_runs,
        "stable": all(
            (r["exit"], r["finding_ids"]) == (base_runs[0]["exit"], base_runs[0]["finding_ids"])
            for r in base_runs
        ),
    }

    for case_id in sorted(cases):
        cluster, argv_tail = cases[case_id]
        runs = [run_once(tool, argv_tail) for _ in range(args.repeat)]
        report["cases"][case_id] = {
            "runs": runs,
            "stable": all(
                (r["exit"], r["finding_ids"], r["inventory"]) ==
                (runs[0]["exit"], runs[0]["finding_ids"], runs[0]["inventory"])
                for r in runs
            ),
        }

    report["tool_sha256_after"] = hashlib.sha256(tool.read_bytes()).hexdigest()
    (outdir / "matrix-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"TOOL {report['tool_sha256']} stable_after={report['tool_sha256'] == report['tool_sha256_after']}")
    first = base_runs[0]
    print(f"{'BASE':24s} exit={first['exit']} findings={first['finding_ids'] or 'none'} stable={report['base']['stable']}")
    for case_id in sorted(report["cases"]):
        entry = report["cases"][case_id]
        run = entry["runs"][0]
        print(f"{case_id:24s} exit={run['exit']} findings={run['finding_ids'] or 'none'} "
              f"inv={run['inventory'] or 'none'} stable={entry['stable']}")
    print("written:", outdir / "matrix-results.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
