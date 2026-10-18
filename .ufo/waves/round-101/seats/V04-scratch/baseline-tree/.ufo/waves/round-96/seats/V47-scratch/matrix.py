#!/usr/bin/env python3
"""V47 independent negative matrix — fresh implementation (r96 C1).

Builds a synthetic base cluster from scratch (no reuse of any other seat's
harness or fixture), then applies one mutation per negative class on a fresh
copy, runs the DELIVERED map_obligations.py via its real CLI, and records
exit code + sorted FINDING IDs + the INVENTORY receipt line.

Classes (nine, from the r94 lineage a-f plus the three r96 C1 targets):
  N1 missing_obligation   (map row deleted, raw claim intact)
  N2 duplicate_mapping    (map row duplicated)
  N3 phantom_obligation   (map row not a raw obligation)
  N4 source_id_mismatch   (map source column differs)
  N5 malformed_json       (entities.json truncated)
  N6 map-path errors      (f1 missing map / f2 foreign map / f3 traversal / f4 dir)
  N7 schema_drift         (claim-shaped records under unexpected entity key)
  N8 inventory_mismatch   (claims key + its map row deleted; declared inventory intact)
  N9 dual_pointer         (legacy-dialect cell naming a second pointer in prose)

Usage: python3 matrix.py <tool-path> <out-dir> [--repeat 2]
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

CANONICAL_MAP = """# V47 synthetic base cluster map

**Expected inventory:** 6 JSON facts; 0 editorial rows; 6 total mapped rows; 2 distinct excerpt anchors.

## JSON facts

| ID | JSON fact pointer and fields | In-world source ID |
|---|---|---|
| F1 | `entities.json#/0/first_appearance` (`alpha`) | `reg-source` |
| F2 | `entities.json#/0/claims/0` | `reg-source` |
| F3 | `entities.json#/1/first_appearance` (`beta`) | `reg-source` |
| F4 | `entities.json#/1/claims/0` | `reg-source` |
| F5 | `relations.json#/0` | `reg-source` |
| F6 | `timeline.json#/0` | `reg-source` |
"""

LEGACY_MAP = """# V47 synthetic legacy-dialect map

**Expected inventory:** 6 JSON facts; 0 editorial rows; 6 total mapped rows; 2 distinct excerpt anchors.

## JSON facts

| ID | JSON fact and fields | `source_id` |
|---|---|---|
| P1 | `entities[0].first_appearance` (alpha) | `reg-source` |
| P2 | `entities[0].claims[0]` (see also `timeline[0]`) | `reg-source` |
| P3 | `entities[1].first_appearance` (beta) | `reg-source` |
| P4 | `entities[1].claims[0]` | `reg-source` |
| P5 | `relations[0]` | `reg-source` |
| P6 | `timeline[0]` | `reg-source` |
"""

LEGACY_MAP_DUAL_CANONICAL = LEGACY_MAP.replace(
    "`entities[0].claims[0]` (see also `timeline[0]`)",
    "`entities[0].claims[0]` (see also `timeline.json#/0`)",
)
LEGACY_MAP_DUAL_COLON = LEGACY_MAP.replace(
    "`entities[0].claims[0]` (see also `timeline[0]`)",
    "`entities[0].claims[0]`: also `timeline[0]`",
)
LEGACY_MAP_DUAL_UNBACKTICKED = LEGACY_MAP.replace(
    "`entities[0].claims[0]` (see also `timeline[0]`)",
    "`entities[0].claims[0]` (see also timeline[0])",
)

ENTITIES = [
    {
        "id": "alpha",
        "first_appearance": "reg-source",
        "claims": [{"statement": "Alpha opens the register.", "source_id": "reg-source"}],
    },
    {
        "id": "beta",
        "first_appearance": "reg-source",
        "claims": [{"statement": "Beta countersigns the register.", "source_id": "reg-source"}],
    },
]
RELATIONS = [{"from": "alpha", "to": "beta", "type": "linked", "source_id": "reg-source"}]
TIMELINE = [{"id": "t-open", "tick": 1, "entity_id": "alpha", "source_id": "reg-source"}]


def build_base(root):
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    (root / "entities.json").write_text(json.dumps(ENTITIES, indent=2) + "\n", encoding="utf-8")
    (root / "relations.json").write_text(json.dumps(RELATIONS, indent=2) + "\n", encoding="utf-8")
    (root / "timeline.json").write_text(json.dumps(TIMELINE, indent=2) + "\n", encoding="utf-8")
    (root / "claim-excerpt-map.md").write_text(CANONICAL_MAP, encoding="utf-8")


def load(name):
    return json.loads((name).read_text(encoding="utf-8"))


def save(name, value):
    name.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def read_map(cluster):
    return (cluster / "claim-excerpt-map.md").read_text(encoding="utf-8")


def write_map(cluster, text):
    (cluster / "claim-excerpt-map.md").write_text(text, encoding="utf-8")


def row_lines(text):
    return [line for line in text.splitlines() if line.startswith("| F")]


def build_cases(work):
    """Return {case_id: (cluster_dir, argv_tail, expected_exit_any)} — mutation applied in place."""
    cases = {}

    def fresh(case_id):
        cluster = work / case_id
        shutil.copytree(work / "base", cluster)
        return cluster

    # N1 missing_obligation: delete the F2 map row only.
    c = fresh("N1_missing_row")
    text = read_map(c)
    write_map(c, text.replace("| F2 | `entities.json#/0/claims/0` | `reg-source` |\n", ""))
    cases["N1_missing_row"] = (c, [str(c)])

    # N2 duplicate_mapping: duplicate the F2 row.
    c = fresh("N2_duplicate_row")
    text = read_map(c)
    write_map(c, text.replace(
        "| F2 | `entities.json#/0/claims/0` | `reg-source` |\n",
        "| F2 | `entities.json#/0/claims/0` | `reg-source` |\n| F2b | `entities.json#/0/claims/0` | `reg-source` |\n"))
    cases["N2_duplicate_row"] = (c, [str(c)])

    # N3 phantom_obligation: add a row naming a non-obligation pointer.
    c = fresh("N3_phantom_row")
    text = read_map(c)
    write_map(c, text.replace(
        "| F6 | `timeline.json#/0` | `reg-source` |\n",
        "| F6 | `timeline.json#/0` | `reg-source` |\n| X1 | `entities.json#/0/name` | `reg-source` |\n"))
    cases["N3_phantom_row"] = (c, [str(c)])

    # N4 source_id_mismatch: change the F1 source column.
    c = fresh("N4_source_mismatch")
    text = read_map(c)
    write_map(c, text.replace(
        "| F1 | `entities.json#/0/first_appearance` (`alpha`) | `reg-source` |",
        "| F1 | `entities.json#/0/first_appearance` (`alpha`) | `other-source` |"))
    cases["N4_source_mismatch"] = (c, [str(c)])

    # N5 malformed_json: truncate entities.json.
    c = fresh("N5_malformed_json")
    (c / "entities.json").write_text("{", encoding="utf-8")
    cases["N5_malformed_json"] = (c, [str(c)])

    # N6 map-path errors (f1-f4).
    c = fresh("N6f1_map_missing")
    cases["N6f1_map_missing"] = (c, [str(c), "--map", "nonexistent-map.md"])

    c = fresh("N6f2_foreign_path")
    outside = work / "outside-map.md"
    outside.write_text(CANONICAL_MAP, encoding="utf-8")
    cases["N6f2_foreign_path"] = (c, [str(c), "--map", str(outside)])

    c = fresh("N6f3_traversal")
    cases["N6f3_traversal"] = (c, [str(c), "--map", "../outside-map.md"])

    c = fresh("N6f4_map_is_dir")
    (c / "mapdir").mkdir()
    cases["N6f4_map_is_dir"] = (c, [str(c), "--map", "mapdir"])

    # N7 schema_drift: claim-shaped records under an unexpected entity key.
    c = fresh("N7_schema_drift")
    entities = load(c / "entities.json")
    entities[0]["notes"] = [{"statement": "Alpha note, claim-shaped.", "source_id": "reg-source"}]
    save(c / "entities.json", entities)
    cases["N7_schema_drift"] = (c, [str(c)])

    # N8 inventory_mismatch (deletion class): drop claims key AND its map row.
    c = fresh("N8_deletion_class")
    entities = load(c / "entities.json")
    del entities[0]["claims"]
    save(c / "entities.json", entities)
    text = read_map(c)
    write_map(c, text.replace("| F2 | `entities.json#/0/claims/0` | `reg-source` |\n", ""))
    cases["N8_deletion_class"] = (c, [str(c)])

    # N8b scope probe (not one of the nine classes): consistent shrink —
    # claims key + map row + declared inventory all shrink together.
    c = fresh("N8b_consistent_shrink")
    entities = load(c / "entities.json")
    del entities[0]["claims"]
    save(c / "entities.json", entities)
    text = read_map(c)
    text = text.replace("| F2 | `entities.json#/0/claims/0` | `reg-source` |\n", "")
    text = text.replace("**Expected inventory:** 6 JSON facts; 0 editorial rows; 6 total mapped rows;",
                        "**Expected inventory:** 5 JSON facts; 0 editorial rows; 5 total mapped rows;")
    write_map(c, text)
    cases["N8b_consistent_shrink"] = (c, [str(c)])

    # N9 dual_pointer: legacy dialect, second pointer in the parenthetical note.
    c = fresh("N9_dual_pointer")
    write_map(c, LEGACY_MAP)
    cases["N9_dual_pointer"] = (c, [str(c)])

    # N9 supplementary variants.
    c = fresh("N9b_dual_canonical")
    write_map(c, LEGACY_MAP_DUAL_CANONICAL)
    cases["N9b_dual_canonical"] = (c, [str(c)])

    c = fresh("N9c_dual_colon")
    write_map(c, LEGACY_MAP_DUAL_COLON)
    cases["N9c_dual_colon"] = (c, [str(c)])

    c = fresh("N9d_dual_unbackticked")
    write_map(c, LEGACY_MAP_DUAL_UNBACKTICKED)
    cases["N9d_dual_unbackticked"] = (c, [str(c)])

    # legacy control: same legacy map without the second pointer must stay PASS.
    c = fresh("N9e_legacy_control")
    write_map(c, LEGACY_MAP.replace(" (see also `timeline[0]`)", ""))
    cases["N9e_legacy_control"] = (c, [str(c)])

    # legacy control: note prose with no pointer token must stay PASS.
    c = fresh("N9f_legacy_prose_control")
    write_map(c, LEGACY_MAP.replace(
        " (see also `timeline[0]`)", " (see also the register margin)"))
    cases["N9f_legacy_prose_control"] = (c, [str(c)])

    # N10 boundary control: canonical header, note naming a second canonical pointer
    # stays unsupported_map exit 2 (pre-existing screening, not dual_pointer).
    c = fresh("N10_canonical_note")
    text = read_map(c)
    write_map(c, text.replace(
        "| F2 | `entities.json#/0/claims/0` | `reg-source` |",
        "| F2 | `entities.json#/0/claims/0` (see `timeline.json#/0`) | `reg-source` |"))
    cases["N10_canonical_note"] = (c, [str(c)])

    # N11 boundary control: legacy header, first token canonical, note pointer
    # stays unsupported_map exit 2 (Q1's documented control).
    c = fresh("N11_legacy_canonical_first")
    write_map(c, LEGACY_MAP.replace(
        "`entities[0].claims[0]` (see also `timeline[0]`)",
        "`entities.json#/0/claims/0` (also `timeline.json#/0`)"))
    cases["N11_legacy_canonical_first"] = (c, [str(c)])

    # N12 fail-closed control: declaration whose counts are unparsable.
    c = fresh("N12_inv_malformed")
    text = read_map(c)
    write_map(c, text.replace(
        "**Expected inventory:** 6 JSON facts; 0 editorial rows; 6 total mapped rows; 2 distinct excerpt anchors.",
        "**Expected inventory:** see the table below."))
    cases["N12_inv_malformed"] = (c, [str(c)])

    return cases


def run(tool, argv_tail):
    command = [sys.executable, str(tool), *argv_tail]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    ids = sorted(
        line[len("FINDING "):].split(":", 1)[0]
        for line in result.stdout.splitlines() if line.startswith("FINDING ")
    )
    inventory = [line for line in result.stdout.splitlines() if line.startswith("INVENTORY ")]
    result_line = [line for line in result.stdout.splitlines() if line.startswith("RESULT ")]
    return {
        "command": " ".join(command),
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
    if work.exists():
        shutil.rmtree(work)
    build_base(work / "base")
    cases = build_cases(work)

    report = {"tool": str(tool), "tool_sha256": None, "cases": {}}
    import hashlib
    report["tool_sha256"] = hashlib.sha256(tool.read_bytes()).hexdigest()

    base_result = run(tool, [str(work / "base")])
    report["base"] = base_result

    for case_id in sorted(cases):
        cluster, argv_tail = cases[case_id]
        runs = [run(tool, argv_tail) for _ in range(args.repeat)]
        stable = all(
            (r["exit"], r["finding_ids"], r["inventory"]) ==
            (runs[0]["exit"], runs[0]["finding_ids"], runs[0]["inventory"])
            for r in runs
        )
        report["cases"][case_id] = {"runs": runs, "stable": stable}

    (outdir / "matrix-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"BASE exit={base_result['exit']} findings={base_result['finding_ids'] or 'none'}")
    for case_id in sorted(report["cases"]):
        entry = report["cases"][case_id]
        first = entry["runs"][0]
        print(f"{case_id:28s} exit={first['exit']} findings={first['finding_ids'] or 'none'} "
              f"inv={first['inventory'] or 'none'} stable={entry['stable']}")
    print("written:", outdir / "matrix-results.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
