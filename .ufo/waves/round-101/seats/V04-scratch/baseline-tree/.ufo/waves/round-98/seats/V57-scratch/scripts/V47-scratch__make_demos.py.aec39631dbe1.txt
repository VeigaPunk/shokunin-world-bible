#!/usr/bin/env python3
"""V47 (r98) support-regression: rebuild the r94-round silent-failure vectors on scratch copies.

Reads the live corpus read-only; writes only under V47-scratch/demos/.
Every replacement asserts an exact single occurrence so a drifted source fails loudly.
Mutation definitions mirror the r97 V52 seat's builder (same vectors, same anchors).
"""
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = REPO / ".ufo/waves/round-98/seats/V47-scratch"
DEMOS = SCRATCH / "demos"


def sub_once(text, old, new, tag):
    n = text.count(old)
    assert n == 1, f"{tag}: expected 1 occurrence, found {n}: {old[:60]!r}"
    return text.replace(old, new)


def copy_fixture(name, tag):
    src = REPO / "corpus/fixtures" / name
    dst = DEMOS / tag
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return dst


def main():
    DEMOS.mkdir(parents=True, exist_ok=True)

    d = copy_fixture("r87-myth-cluster", "T1-header-rename")
    p = d / "claim-excerpt-map.md"
    p.write_text(sub_once(p.read_text(encoding="utf-8"),
                          "| ID | JSON fact and fields |",
                          "| Ref | JSON fact and fields |", "T1"))

    d = copy_fixture("r87-myth-cluster", "T2-editorial-drop")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    start = text.index("## Editorial rows")
    end = text.index("## Scope and review notes")
    p.write_text(text[:start] + text[end:], encoding="utf-8")

    d = copy_fixture("r87-myth-cluster", "T3-duplicate-row")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    e1 = [l for l in text.split("\n") if l.startswith("| E1 |")][0]
    p.write_text(text.replace(e1, e1 + "\n" + e1, 1), encoding="utf-8")

    d = copy_fixture("r87-myth-cluster", "T4-referenced-mode-flip")
    p = d / "claim-excerpt-map.md"
    p.write_text(sub_once(p.read_text(encoding="utf-8"),
                          "| `lowwater-hymn-excerpt.md` | `lowwater-hymn` | `verbatim` |",
                          "| `lowwater-hymn-excerpt.md` | `lowwater-hymn` | `summary` |", "T4"))

    d = copy_fixture("r88-m3-maya-cluster", "T5a-current-map-mode-flip")
    p = d / "claim-excerpt-map.md"
    p.write_text(sub_once(p.read_text(encoding="utf-8"),
                          "English prose | `verbatim` |",
                          "English prose | `summary` |", "T5a"))

    d = copy_fixture("r88-m3-maya-cluster", "T5b-r90shape-unreferenced-flip")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    start = text.index("## Editorial rows")
    end = text.index("## Scope and review notes")
    text = text[:start] + text[end:]
    text = sub_once(text,
                    "**Expected inventory:** 10 JSON facts; 2 editorial rows; 12 total mapped rows; 8 distinct excerpt anchors.",
                    "**Expected inventory:** 10 JSON facts; 0 editorial rows; 10 total mapped rows; 6 distinct excerpt anchors.",
                    "T5b-inventory")
    text = sub_once(text, "English prose | `verbatim` |", "English prose | `summary` |", "T5b-flip")
    p.write_text(text, encoding="utf-8")

    d = copy_fixture("r89-inspiration-paraphrase", "T6-paraphrase-anchor-absent")
    p = d / "ash-ledger-excerpt.md"
    p.write_text(sub_once(p.read_text(encoding="utf-8"),
                          "moved to the west stair", "moved to the east stair", "T6"))

    d = copy_fixture("r87-myth-cluster", "T7-no-inventory")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    p.write_text(sub_once(text,
                          "**Expected inventory:** 14 JSON facts; 8 editorial rows; 22 total mapped rows; 22 distinct excerpt anchors.\n",
                          "", "T7"), encoding="utf-8")

    d = copy_fixture("r87-myth-cluster", "T8-anchor-count-offby1")
    p = d / "claim-excerpt-map.md"
    p.write_text(sub_once(p.read_text(encoding="utf-8"),
                          "22 total mapped rows; 22 distinct excerpt anchors.",
                          "22 total mapped rows; 21 distinct excerpt anchors.", "T8"))

    d = copy_fixture("r94-paired-crossing", "F15-b2-rowdrop-counts-updated")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    j05 = [l for l in text.split("\n") if l.startswith("| J05 |")][0]
    text = text.replace(j05 + "\n", "", 1)
    text = sub_once(text,
                    "**Expected inventory:** 14 JSON facts; 2 editorial rows; 16 total mapped rows; 12 distinct excerpt anchors.",
                    "**Expected inventory:** 13 JSON facts; 2 editorial rows; 15 total mapped rows; 11 distinct excerpt anchors.",
                    "b2-inventory")
    p.write_text(text, encoding="utf-8")

    d = copy_fixture("r94-paired-crossing", "F15-b3-rowdrop-stale-counts")
    p = d / "claim-excerpt-map.md"
    text = p.read_text(encoding="utf-8")
    j05 = [l for l in text.split("\n") if l.startswith("| J05 |")][0]
    p.write_text(text.replace(j05 + "\n", "", 1), encoding="utf-8")

    d = copy_fixture("r94-paired-crossing", "F15-a-dependency-reduced")
    p = d / "timeline.json"
    text = p.read_text(encoding="utf-8")
    p.write_text(sub_once(text,
                          '      "aru-ninth-bell",\n      "evin-ninth-bell"\n',
                          '      "aru-ninth-bell"\n', "F15-a"), encoding="utf-8")

    old = subprocess.run(["git", "show", "a7c6a17:corpus/tools/support_check.py"],
                         cwd=REPO, capture_output=True, text=True, check=True).stdout
    (SCRATCH / "support_check_r90.py").write_text(old, encoding="utf-8")
    mid = subprocess.run(["git", "show", "6332115:corpus/tools/support_check.py"],
                         cwd=REPO, capture_output=True, text=True, check=True).stdout
    (SCRATCH / "support_check_r91.py").write_text(mid, encoding="utf-8")
    print("demos built:", sorted(p.name for p in DEMOS.iterdir()))


if __name__ == "__main__":
    sys.exit(main())
