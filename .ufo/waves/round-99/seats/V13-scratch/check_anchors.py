#!/usr/bin/env python3
"""V13 independent anchor check for r99-window-lapse claim-excerpt-map.

Own implementation. Does not import corpus/tools/support_check.py.
Checks, on the delivered fixture:
  A. Every mapped row's exact anchor is a fixed substring of its declared
     line span (window join), and every grep -nF hit line lies inside that span.
  B. The 20 inherited JSON-fact rows match the r98 baseline map on pointer,
     in-world source ID, excerpt path, span, mode, and exact anchor.
  C. Inherited excerpt line numbers are preserved: fictional-excerpts.md
     lines 1-64 are byte-identical to the r98 baseline, and no inherited
     span reaches into the appended lapse section.
  D. Exactly one new JSON-fact anchor, and it occurs only in the lapse
     section (lines after the preserved r98 prefix).
  E. Declared inventory matches parsed counts.
  F. JSON pointers resolve in the fixture; string nodes equal the row's
     in-world source ID; object nodes' source_id equals the row source ID.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX_NAME = "r99-window-lapse"
REF_NAME = "r98-clerk-filing"
FIX = REPO / "corpus/fixtures" / FIX_NAME
REF = REPO / "corpus/fixtures" / REF_NAME
MAP = FIX / "claim-excerpt-map.md"
REF_MAP = REF / "claim-excerpt-map.md"
EXCERPT = "fictional-excerpts.md"

problems = []


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
    if start < 1 or end < start:
        raise ValueError(f"bad span bounds {value!r}")
    return start, end


def resolve_pointer(fixture, pointer):
    file_part, frag = pointer.split("#", 1)
    data = json.loads((fixture / file_part).read_text(encoding="utf-8"))
    if frag in ("", "/"):
        return data
    node = data
    for tok in frag.lstrip("/").split("/"):
        tok = tok.replace("~1", "/").replace("~0", "~")
        if isinstance(node, list):
            node = node[int(tok)]
        elif isinstance(node, dict):
            node = node[tok]
        else:
            raise KeyError(f"cannot index {type(node).__name__} with {tok!r}")
    return node


def parse_map(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    inventory = None
    section = None
    inventory_line = None
    i = 0
    while i < len(lines):
        line = lines[i]
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
            inventory_line = i + 1
        if not line.lstrip().startswith("|"):
            i += 1
            continue
        header = cells(line)
        role = {}
        for idx, h in enumerate(header):
            n = norm(h)
            if n in {"id", "fact", "fact id"}:
                role.setdefault("id", idx)
            elif "json fact pointer" in n or n == "pointer" or "pointer" in n:
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
            i += 1
            continue
        j = i + 1
        while j < len(lines) and lines[j].lstrip().startswith("|"):
            row = cells(lines[j])
            if row and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in row):
                j += 1
                continue
            if len(row) != len(header):
                problems.append(
                    f"{path.name}:{j+1}: cell count {len(row)} != header {len(header)}")
                j += 1
                continue
            ptr_cell = row[role["ptr"]] if "ptr" in role else ""
            m_ptr = re.search(r"`([^`]+#[^`]+)`", ptr_cell)
            rows.append({
                "id": row[role["id"]].strip("`"),
                "section": section,
                "ptr": m_ptr.group(1) if m_ptr else None,
                "ptr_cell": ptr_cell,
                "src": row[role["src"]].strip("`") if "src" in role else None,
                "path": row[role["path"]].strip("`") if "path" in role else None,
                "span": row[role["span"]].strip("`"),
                "mode": row[role["mode"]].strip("`"),
                "anchor": row[role["anchor"]].strip("`"),
                "map_line": j + 1,
            })
            j += 1
        i = j
    return rows, inventory, inventory_line


def excerpt_lines(fixture, name):
    return (fixture / name).read_text(encoding="utf-8").splitlines()


def grep_hits(anchor, path):
    result = subprocess.run(
        ["grep", "-nF", "--", anchor, str(path)],
        check=False, capture_output=True, text=True,
    )
    if result.returncode == 1:
        return []
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"grep exited {result.returncode}")
    hits = []
    for line in result.stdout.splitlines():
        number, sep, _rest = line.partition(":")
        if not sep or not number.isdecimal():
            raise RuntimeError(f"unparsed grep line {line!r}")
        hits.append(int(number))
    return hits


def main():
    if not MAP.exists():
        print("ABSENT: map missing")
        return 3
    if not REF_MAP.exists():
        print("ABSENT: r98 baseline map missing")
        return 3

    rows, inventory, inventory_line = parse_map(MAP)
    facts = [r for r in rows if r["section"] == "json"]
    editorial = [r for r in rows if r["section"] == "editorial"]
    print(f"parsed rows: {len(facts)} JSON facts, {len(editorial)} editorial")
    print(f"declared inventory: {inventory} (map line {inventory_line})")

    distinct = len({(r["path"], r["anchor"]) for r in rows})
    actual = (len(facts), len(editorial), len(facts) + len(editorial), distinct)
    if inventory != actual:
        problems.append(f"INVENTORY mismatch declared={inventory} actual={actual}")
    else:
        print(f"INVENTORY OK: {actual}")

    for r in rows:
        if not r["path"]:
            problems.append(f"{r['id']}: excerpt path missing")
            continue
        excerpt_path = FIX / r["path"]
        if not excerpt_path.is_file():
            problems.append(f"{r['id']}: excerpt path missing {r['path']!r}")
            continue
        src_lines = excerpt_lines(FIX, r["path"])
        try:
            start, end = parse_span(r["span"])
        except ValueError as exc:
            problems.append(f"{r['id']}: {exc}")
            continue
        if end > len(src_lines):
            problems.append(
                f"{r['id']}: span {start}-{end} out of file range 1-{len(src_lines)}")
            continue
        window = "\n".join(src_lines[start - 1:end])
        in_window = r["anchor"] in window
        hits = grep_hits(r["anchor"], excerpt_path)
        outside = [n for n in hits if not (start <= n <= end)]
        own_line = next((n for n in hits if start <= n <= end), None)
        print(
            f"ROW {r['id']} map_line={r['map_line']} span={start}-{end} "
            f"window={in_window} grep={hits} outside={outside} own_line={own_line} "
            f"ptr={r['ptr']} src={r['src']}"
        )
        if not in_window:
            problems.append(f"{r['id']}: anchor NOT in span window {r['path']}:{start}-{end}")
        if not hits:
            problems.append(f"{r['id']}: anchor has zero grep -nF hits in {r['path']}")
        if outside:
            problems.append(
                f"{r['id']}: grep hit outside declared span {start}-{end}: {outside}")
        if r["mode"] != "verbatim":
            problems.append(f"{r['id']}: mode {r['mode']!r} not verbatim")
        if r["section"] == "json":
            if not r["ptr"]:
                problems.append(f"{r['id']}: no JSON pointer token")
                continue
            try:
                node = resolve_pointer(FIX, r["ptr"])
            except Exception as exc:  # noqa: BLE001
                problems.append(f"{r['id']}: pointer {r['ptr']} unresolved: {exc}")
                continue
            if isinstance(node, str):
                if r["src"] and node != r["src"]:
                    problems.append(
                        f"{r['id']}: first_appearance {node!r} != row src {r['src']!r}")
            elif isinstance(node, dict):
                if "source_id" in node and r["src"] and node["source_id"] != r["src"]:
                    problems.append(
                        f"{r['id']}: JSON source_id {node['source_id']!r} != row src {r['src']!r}")
            else:
                problems.append(f"{r['id']}: pointer node type {type(node).__name__}")

    ref_rows, _, _ = parse_map(REF_MAP)
    ref_facts = {r["id"]: r for r in ref_rows if r["section"] == "json"}
    inherited = [r for r in facts if r["id"] in ref_facts]
    new_rows = [r for r in facts if r["id"] not in ref_facts]
    dropped = sorted(set(ref_facts) - {r["id"] for r in facts})
    print(f"inherited-matched rows: {len(inherited)}; new rows: {[r['id'] for r in new_rows]}; dropped: {dropped}")
    if dropped:
        problems.append(f"inherited IDs dropped: {dropped}")
    if len(inherited) != 20:
        problems.append(f"expected 20 inherited JSON rows, matched {len(inherited)}")
    if len(new_rows) != 1:
        problems.append(f"expected exactly 1 new JSON row, found {len(new_rows)}: {[r['id'] for r in new_rows]}")

    for r in inherited:
        b = ref_facts[r["id"]]
        for field in ("ptr", "src", "path", "span", "anchor", "mode"):
            if r[field] != b[field]:
                problems.append(
                    f"{r['id']}: inherited {field} changed: r99={r[field]!r} r98={b[field]!r}")
        if r["map_line"] != b["map_line"]:
            problems.append(
                f"{r['id']}: inherited map line moved: r99={r['map_line']} r98={b['map_line']}")

    ref_exc = excerpt_lines(REF, EXCERPT)
    new_exc = excerpt_lines(FIX, EXCERPT)
    if new_exc[:len(ref_exc)] != ref_exc:
        # locate first differing line for the receipt
        first = None
        for n, (a, b) in enumerate(zip(new_exc, ref_exc), start=1):
            if a != b:
                first = n
                break
        if first is None and len(new_exc) < len(ref_exc):
            first = len(new_exc) + 1
        problems.append(
            f"preserved prefix: r99 fictional-excerpts.md first {len(ref_exc)} "
            f"lines differ from r98 baseline (first diff line {first})")
    else:
        print(f"PRESERVED PREFIX OK: lines 1-{len(ref_exc)} byte-identical to r98")
    section_start = len(ref_exc) + 1
    headings = [(i + 1, line) for i, line in enumerate(new_exc) if line.startswith("## ")]
    new_heads = [h for h in headings if h[0] >= section_start]
    print(f"lapse section starts at line {section_start}; new headings: {new_heads}")
    print(f"r99 excerpt lines: {len(new_exc)}")

    prefix_text = "\n".join(new_exc[:len(ref_exc)])
    for r in new_rows:
        if r["path"] != EXCERPT:
            problems.append(f"{r['id']}: new row path {r['path']!r} is not {EXCERPT}")
            continue
        start, end = parse_span(r["span"])
        if start < section_start:
            problems.append(
                f"{r['id']}: new anchor span {start}-{end} starts before lapse section "
                f"(line {section_start})")
        if end < section_start:
            problems.append(f"{r['id']}: new anchor span ends before lapse section")
        if r["anchor"] in prefix_text:
            problems.append(
                f"{r['id']}: new anchor literal also present in preserved prefix")
        # also require the new row's map line to be after every inherited JSON row
        inherited_lines = [x["map_line"] for x in inherited]
        if inherited_lines and r["map_line"] <= max(inherited_lines):
            problems.append(
                f"{r['id']}: new row map line {r['map_line']} is not after inherited rows "
                f"(max inherited map line {max(inherited_lines)})")

    for r in inherited:
        if r["path"] != EXCERPT:
            continue
        start, end = parse_span(r["span"])
        if end >= section_start:
            problems.append(
                f"{r['id']}: inherited span {start}-{end} reaches into lapse section")

    # editorial rows must also match r98 on span/anchor/path/mode
    ref_ed = {r["id"]: r for r in ref_rows if r["section"] == "editorial"}
    got_ed = {r["id"]: r for r in editorial}
    if set(ref_ed) != set(got_ed):
        problems.append(f"editorial ID set changed: r99={sorted(got_ed)} r98={sorted(ref_ed)}")
    for eid, r in got_ed.items():
        if eid not in ref_ed:
            continue
        b = ref_ed[eid]
        for field in ("path", "span", "anchor", "mode"):
            if r[field] != b[field]:
                problems.append(
                    f"{eid}: editorial {field} changed: r99={r[field]!r} r98={b[field]!r}")

    print()
    if problems:
        print(f"PROBLEMS ({len(problems)}):")
        for p in problems:
            print(" -", p)
        print("RESULT FAIL")
        return 1
    print("ALL CHECKS PASS")
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
