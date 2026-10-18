#!/usr/bin/env python3
"""V12 independent anchor check for r98-clerk-filing claim-excerpt-map.

Own implementation (does not import corpus/tools/support_check.py).
Checks:
  A. Every mapped JSON fact row's exact anchor is an in-span substring of the
     declared excerpt file lines.
  B. The 17 inherited rows (J01-J17) carry spans/anchors/modes identical to the
     r97 baseline map (git 9a3d648).
  C. The 3 new anchors point into the appended filing-note section only.
  D. Declared inventory matches actual parsed counts.
  E. JSON pointers resolve in the fixture and their source_id matches the row.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX = REPO / "corpus/fixtures/r98-clerk-filing"
MAP = FIX / "claim-excerpt-map.md"
BASE = "9a3d648"
R97_MAP = "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"
R97_EXC = "corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md"

problems = []
notes = []


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def norm(h):
    return re.sub(r"[^a-z0-9]+", " ", h.strip().strip("`").lower()).strip()


def parse_span(value):
    m = re.fullmatch(r"(\d+)(?:\s*[-–]\s*(\d+))?", value.strip().strip("`"))
    if not m:
        raise ValueError(f"bad span {value!r}")
    start = int(m.group(1))
    end = int(m.group(2)) if m.group(2) else start
    return start, end


def resolve_pointer(root, pointer):
    # root like "entities.json#/0/first_appearance"
    file_part, frag = pointer.split("#", 1)
    data = json.loads((FIX / file_part).read_text(encoding="utf-8"))
    if frag in ("", "/"):
        return data
    node = data
    for tok in frag.lstrip("/").split("/"):
        tok = tok.replace("~1", "/").replace("~0", "~")
        if isinstance(node, list):
            node = node[int(tok)]
        else:
            node = node[tok]
    return node


def parse_map(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    inventory = None
    section = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            h = norm(line[3:])
            section = "json" if h.startswith("json facts") else (
                "editorial" if h.startswith("editorial rows") else None)
        m = re.fullmatch(
            r"\*\*Expected inventory:\*\*\s*(\d+) JSON fact(?:s)?;\s*"
            r"(\d+) editorial row(?:s)?;\s*(\d+) total mapped row(?:s)?;\s*"
            r"(\d+) distinct excerpt anchor(?:s)?\.\s*", line)
        if m:
            inventory = tuple(int(x) for x in m.groups())
        if not line.lstrip().startswith("|"):
            continue
        header = cells(line)
        role = {}
        for idx, h in enumerate(header):
            n = norm(h)
            if n in {"id", "fact", "fact id"}:
                role.setdefault("id", idx)
            elif "json fact pointer" in n or "pointer" in n:
                role.setdefault("ptr", idx)
            elif n == "in world source id":
                role.setdefault("src", idx)
            elif "excerpt" in n and ("path" in n or n == "excerpt"):
                role.setdefault("path", idx)
            elif n in {"line span", "lines", "line"}:
                role.setdefault("span", idx)
            elif "delivery mode" in n or n.endswith(" mode"):
                role.setdefault("mode", idx)
            elif "anchor" in n:
                role.setdefault("anchor", idx)
        if not {"id", "anchor", "span", "mode"}.issubset(role):
            continue
        j = i + 1
        while j < len(lines) and lines[j].lstrip().startswith("|"):
            row = cells(lines[j])
            if row and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in row):
                j += 1
                continue
            if len(row) == len(header):
                ptr_cell = row[role["ptr"]] if "ptr" in role else ""
                m_ptr = re.search(r"`([^`]+#[^`]+)`", ptr_cell)
                rows.append({
                    "id": row[role["id"]].strip("`"),
                    "section": section,
                    "ptr": m_ptr.group(1) if m_ptr else None,
                    "src": row[role["src"]].strip("`") if "src" in role else None,
                    "path": row[role["path"]].strip("`") if "path" in role else None,
                    "span": row[role["span"]],
                    "mode": row[role["mode"]].strip("`"),
                    "anchor": row[role["anchor"]].strip("`"),
                })
            j += 1
    return rows, inventory


def excerpt_lines(fixture, name):
    return (fixture / name).read_text(encoding="utf-8").splitlines()


def main():
    if not MAP.exists():
        print("ABSENT: map missing")
        sys.exit(3)
    rows, inventory = parse_map(MAP)
    facts = [r for r in rows if r["section"] == "json"]
    editorial = [r for r in rows if r["section"] == "editorial"]
    print(f"parsed rows: {len(facts)} JSON facts, {len(editorial)} editorial")
    print(f"declared inventory: {inventory}")

    # D. inventory
    distinct = len({(r["path"], r["anchor"]) for r in rows})
    actual = (len(facts), len(editorial), len(facts) + len(editorial), distinct)
    if inventory != actual:
        problems.append(f"INVENTORY mismatch declared={inventory} actual={actual}")
    else:
        print(f"INVENTORY OK: {actual}")

    # A. in-span anchors + E. pointer resolution
    for r in rows:
        f = FIX / r["path"] if r["path"] else None
        if f is None or not f.exists():
            problems.append(f"{r['id']}: excerpt path missing {r['path']!r}")
            continue
        src_lines = excerpt_lines(FIX, r["path"])
        start, end = parse_span(r["span"])
        if start < 1 or end > len(src_lines):
            problems.append(f"{r['id']}: span {start}-{end} out of file range 1-{len(src_lines)}")
            continue
        window = "\n".join(src_lines[start - 1:end])
        if r["anchor"] not in window:
            problems.append(f"{r['id']}: anchor NOT in span {r['path']}:{start}-{end}")
        if r["mode"] != "verbatim":
            problems.append(f"{r['id']}: mode {r['mode']!r} not verbatim")
        if r["section"] == "json" and r["ptr"]:
            try:
                node = resolve_pointer(REPO, r["ptr"]) if False else resolve_pointer(None, r["ptr"])
            except Exception as e:  # noqa: BLE001
                problems.append(f"{r['id']}: pointer {r['ptr']} unresolved: {e}")
                continue
            if isinstance(node, str):
                if r["src"] and node != r["src"]:
                    problems.append(f"{r['id']}: first_appearance {node!r} != row src {r['src']!r}")
            elif isinstance(node, dict):
                if "source_id" in node and r["src"] and node["source_id"] != r["src"]:
                    problems.append(f"{r['id']}: JSON source_id {node['source_id']!r} != row src {r['src']!r}")
            else:
                problems.append(f"{r['id']}: pointer node type {type(node).__name__}")

    # B. inherited rows identical to r97 baseline map
    base_text = subprocess.run(["git", "show", f"{BASE}:{R97_MAP}"], cwd=REPO,
                               capture_output=True, text=True, check=True).stdout
    base_tmp = Path("/tmp/v12-r97map.md")
    base_tmp.write_text(base_text, encoding="utf-8")
    base_rows, _ = parse_map(base_tmp)
    base_facts = {r["id"]: r for r in base_rows if r["section"] == "json"}
    inherited = [r for r in facts if r["id"].startswith("J") and r["id"] in base_facts]
    new_rows = [r for r in facts if r["id"] not in base_facts]
    print(f"inherited-matched rows: {len(inherited)}; new rows: {[r['id'] for r in new_rows]}")
    for r in inherited:
        b = base_facts[r["id"]]
        for field in ("path", "span", "anchor", "mode"):
            if r[field] != b[field]:
                problems.append(f"{r['id']}: inherited {field} changed: r98={r[field]!r} r97={b[field]!r}")
    if len(inherited) != 17:
        problems.append(f"expected 17 inherited rows, matched {len(inherited)}")

    # C. new anchors only in the appended filing-note section
    r97_exc = subprocess.run(["git", "show", f"{BASE}:{R97_EXC}"], cwd=REPO,
                             capture_output=True, text=True, check=True).stdout.splitlines()
    r98_exc = excerpt_lines(FIX, "fictional-excerpts.md")
    if r98_exc[:len(r97_exc)] != r97_exc:
        problems.append("preserved prefix: r98 fictional-excerpts.md first "
                        f"{len(r97_exc)} lines differ from r97 baseline")
    else:
        print(f"PRESERVED PREFIX OK: lines 1-{len(r97_exc)} byte-identical to r97")
    section_start = len(r97_exc) + 1
    headings = [(i + 1, l) for i, l in enumerate(r98_exc) if l.startswith("## ")]
    new_heads = [h for h in headings if h[0] >= section_start]
    print(f"filing section starts at line {section_start}; new headings: {new_heads}")
    prefix_text = "\n".join(r98_exc[:len(r97_exc)])
    for r in new_rows:
        start, end = parse_span(r["span"])
        if start < section_start:
            problems.append(f"{r['id']}: new anchor span {start}-{end} starts before filing section (line {section_start})")
        if r["anchor"] in prefix_text:
            problems.append(f"{r['id']}: new anchor literal also present in preserved prefix (not filing-only)")
    # inherited anchors must stay out of the filing section
    for r in inherited:
        start, end = parse_span(r["span"])
        if end >= section_start:
            problems.append(f"{r['id']}: inherited span {start}-{end} reaches into filing section")

    print()
    if problems:
        print(f"PROBLEMS ({len(problems)}):")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
