#!/usr/bin/env python3
"""V52 scratch demo builder: r91-hardening vectors vs the delivered support_check.

Reads the live corpus read-only; writes only under .ufo/waves/round-95/seats/V52-scratch/.
Demos:
  demo1-header-rename        r87 copy, JSON facts table header | ID | -> | Row |
  demo2a-mode-flip           r88 copy, Spence declaration mode verbatim -> summary (exact r90 mutation)
  demo2b-unreferenced-flip   r88 copy, S1/S2 rows removed + inventory restated + same flip
                             (reconstructs the r90-era unreferenced-declaration shape)
"""
import shutil
import subprocess
import sys
from pathlib import Path

SCR = Path(__file__).resolve().parent
ROOT = SCR.parents[4]  # V52-scratch -> seats -> round-95 -> waves -> .ufo -> repo root
assert (ROOT / "corpus" / "fixtures").is_dir(), ROOT
FIX = ROOT / "corpus" / "fixtures"
TOOL = ROOT / "corpus" / "tools" / "support_check.py"


def copy_fixture(src_name, dst_name):
    dst = SCR / dst_name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(FIX / src_name, dst)
    return dst


def replace_once(text, old, new, label):
    count = text.count(old)
    assert count == 1, f"{label}: expected exactly 1 occurrence, found {count}"
    return text.replace(old, new, 1)


def flip_spence_mode(map_path):
    lines = map_path.read_text(encoding="utf-8").splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.startswith("| `source-excerpt.md:5` | Lewis Spence")]
    assert len(hits) == 1, f"declaration row hits: {hits}"
    i = hits[0]
    lines[i] = replace_once(lines[i], "`verbatim`", "`summary`", "spence mode cell")
    map_path.write_text("".join(lines), encoding="utf-8")


def run_demo(name, cluster):
    proc = subprocess.run(
        [sys.executable, str(TOOL), str(cluster)],
        cwd=ROOT, capture_output=True, text=True,
    )
    out = proc.stdout + proc.stderr
    (SCR / f"{name}.out").write_text(out, encoding="utf-8")
    print(f"### {name}: exit={proc.returncode}")
    print(out)
    return proc.returncode


def main():
    # demo 1: header rename drops the 14 JSON fact rows (r90 attack #1)
    d1 = copy_fixture("r87-myth-cluster", "demo1-header-rename")
    m1 = d1 / "claim-excerpt-map.md"
    m1.write_text(
        replace_once(m1.read_text(encoding="utf-8"),
                     "| ID | JSON fact and fields |", "| Row | JSON fact and fields |",
                     "r87 JSON facts header"),
        encoding="utf-8",
    )
    rc1 = run_demo("demo1-header-rename", d1)

    # demo 2a: exact r90 mutation on the current r88 map
    d2a = copy_fixture("r88-m3-maya-cluster", "demo2a-mode-flip")
    flip_spence_mode(d2a / "claim-excerpt-map.md")
    rc2a = run_demo("demo2a-mode-flip", d2a)

    # demo 2b: r90-era unreferenced-declaration shape
    d2b = copy_fixture("r88-m3-maya-cluster", "demo2b-unreferenced-flip")
    m2b = d2b / "claim-excerpt-map.md"
    text = m2b.read_text(encoding="utf-8")
    for row_id in ("S1", "S2"):
        line = next(l for l in text.splitlines() if l.startswith(f"| {row_id} |"))
        text = replace_once(text, line + "\n", "", f"drop {row_id} row")
    text = replace_once(
        text,
        "**Expected inventory:** 10 JSON facts; 2 editorial rows; 12 total mapped rows; 8 distinct excerpt anchors.",
        "**Expected inventory:** 10 JSON facts; 0 editorial rows; 10 total mapped rows; 6 distinct excerpt anchors.",
        "r88 inventory restated",
    )
    m2b.write_text(text, encoding="utf-8")
    flip_spence_mode(m2b)
    rc2b = run_demo("demo2b-unreferenced-flip", d2b)

    print(f"SUMMARY demo1={rc1} demo2a={rc2a} demo2b={rc2b}")


if __name__ == "__main__":
    main()
