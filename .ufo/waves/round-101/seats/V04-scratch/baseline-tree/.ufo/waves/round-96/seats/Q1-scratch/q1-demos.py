#!/usr/bin/env python3
"""Q1 r96 demos: gating inventory_mismatch, dual_pointer, schema_drift, usage probes.

Every mutation is applied to a scratch copy; the corpus tree is never written.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = ROOT / "corpus/tools/map_obligations.py"
FIXTURES = ROOT / "corpus/fixtures"
SCRATCH = ROOT / ".ufo/waves/round-96/seats/Q1-scratch/work"

if SCRATCH.exists():
    shutil.rmtree(SCRATCH)
SCRATCH.mkdir(parents=True)


def copy(fixture, name):
    target = SCRATCH / name
    shutil.copytree(FIXTURES / fixture, target)
    return target


def map_text(cluster):
    return (cluster / "claim-excerpt-map.md").read_text(encoding="utf-8")


def write_map(cluster, text):
    (cluster / "claim-excerpt-map.md").write_text(text, encoding="utf-8")


def replace_cell(cluster, row_id, new_cell):
    lines = map_text(cluster).splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| {row_id} |"):
            cells = line.split("|")
            cells[2] = f" {new_cell} "
            lines[index] = "|".join(cells)
            break
    else:
        raise SystemExit(f"row {row_id} not found")
    write_map(cluster, "\n".join(lines) + "\n")


def drop_row(cluster, row_id):
    lines = [line for line in map_text(cluster).splitlines() if not line.startswith(f"| {row_id} |")]
    write_map(cluster, "\n".join(lines) + "\n")


def rename_claims(cluster, index, key):
    path = cluster / "entities.json"
    entities = json.loads(path.read_text(encoding="utf-8"))
    entities[index][key] = entities[index].pop("claims")
    path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")


def run(label, args, expect):
    result = subprocess.run(
        [sys.executable, str(TOOL), *args], cwd=ROOT, capture_output=True, text=True, check=False
    )
    print(f"### {label}")
    print(f"$ python3 corpus/tools/map_obligations.py {' '.join(str(a) for a in args)}")
    for line in result.stdout.splitlines():
        print(f"    {line}")
    if result.stderr:
        print(f"    STDERR {result.stderr.strip()}")
    print(f"    exit={result.returncode} (expected {expect})")
    print()


# A. deletion class: claims key and its map row both removed (r95-carry)
cluster = copy("r95-crossing-aftermath", "deletion-class")
rename_claims(cluster, 0, "kept-claims-under-other-key")  # placeholder replaced below
path = cluster / "entities.json"
entities = json.loads(path.read_text(encoding="utf-8"))
del entities[0]["kept-claims-under-other-key"]
path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
drop_row(cluster, "J06")
run("A deletion class (claims key + map row removed, r95 copy)", [cluster], "exit 1 inventory_mismatch")

# B. dual pointer in the legacy parenthetical (canonical second token)
cluster = copy("r88-m3-maya-cluster", "dual-pointer-paren-canonical")
replace_cell(cluster, "P1", "`entities[0].first_appearance` (also `relations.json#/0`)")
run("B dual_pointer legacy parenthetical, canonical second token", [cluster], "exit 1 dual_pointer")

# C. dual pointer in the legacy parenthetical (legacy second token)
cluster = copy("r88-m3-maya-cluster", "dual-pointer-paren-legacy")
replace_cell(cluster, "P2", "`entities[1].first_appearance` (also `entities[9].claims[0]`)")
run("C dual_pointer legacy parenthetical, legacy second token", [cluster], "exit 1 dual_pointer")

# D. dual pointer in the legacy colon-prose
cluster = copy("r88-m3-maya-cluster", "dual-pointer-colon-prose")
replace_cell(cluster, "T2", "`timeline[1]`: also `entities[9].claims[0]`")
run("D dual_pointer legacy colon-prose", [cluster], "exit 1 dual_pointer")

# E. control: undocumented legacy tail prose stays fail-closed exit 2 (unchanged grammar)
cluster = copy("r88-m3-maya-cluster", "legacy-tail-prose-control")
replace_cell(cluster, "P1", "`entities[0].first_appearance` extra prose")
run("E control legacy tail prose (grammar unchanged)", [cluster], "exit 2 unsupported_map")

# F. schema_drift with the map row removed
cluster = copy("r95-crossing-aftermath", "schema-drift-row-removed")
rename_claims(cluster, 0, "assertions")
drop_row(cluster, "J06")
run("F schema_drift (claims renamed, row removed)", [cluster], "exit 1 schema_drift + inventory_mismatch")

# G. schema_drift with the map row kept
cluster = copy("r95-crossing-aftermath", "schema-drift-row-kept")
rename_claims(cluster, 0, "assertions")
run("G schema_drift (claims renamed, row kept)", [cluster], "exit 1 phantom_obligation + schema_drift")

# H. malformed declaration line is gating (fail-closed)
cluster = copy("r93-m2-kojiki-cluster", "declaration-malformed")
lines = map_text(cluster).splitlines()
lines = [
    "**Expected inventory:** see the table below." if line.startswith("**Expected inventory:**") else line
    for line in lines
]
write_map(cluster, "\n".join(lines) + "\n")
run("H malformed declaration (fail-closed)", [cluster], "exit 1 inventory_mismatch")

# I. declaration undercounts the parsed rows
cluster = copy("r93-m2-kojiki-cluster", "declaration-undercount")
lines = map_text(cluster).splitlines()
lines = [
    "**Expected inventory:** 11 JSON facts; 3 editorial rows; 14 total mapped rows; 15 distinct excerpt anchors."
    if line.startswith("**Expected inventory:**") else line
    for line in lines
]
write_map(cluster, "\n".join(lines) + "\n")
run("I declaration undercount", [cluster], "exit 1 inventory_mismatch")

# J. control: no declaration line is not a gate
cluster = copy("r88-m3-maya-cluster", "no-declaration-control")
lines = [line for line in map_text(cluster).splitlines() if not line.startswith("**Expected inventory:**")]
write_map(cluster, "\n".join(lines) + "\n")
run("J control no declaration line", [cluster], "exit 0 PASS")

# K. usage probes
run("K1 usage: no arguments", [], "exit 2 invalid_arguments")
run("K2 usage: --self-test with a cluster", ["--self-test", FIXTURES / "r93-m2-kojiki-cluster"], "exit 2 invalid_arguments")
run("K3 usage: --frozen with a cluster", ["--frozen", ROOT / ".ufo/waves/round-94/frozen/map-obligations-r93", FIXTURES / "r93-m2-kojiki-cluster"], "exit 2 invalid_arguments")
run("K4 usage: --frozen with --map", ["--frozen", ROOT / ".ufo/waves/round-94/frozen/map-obligations-r93", "--map", "claim-excerpt-map.md"], "exit 2 invalid_arguments")
run("K5 usage: --map outside the cluster", [FIXTURES / "r93-m2-kojiki-cluster", "--map", "/etc/hosts"], "exit 2 foreign_path")
run("K6 usage: unknown flag", ["--bogus"], "exit 2 invalid_arguments")
