#!/usr/bin/env python3
"""V45 anchor-replica-2 checker (round 96).

Independent pure-Python line-slice method (no grep, no support_check, no
map_obligations import). Parses a claim-excerpt-map.md table itself, reads each
excerpt file with Path.read_text().split("\n"), and resolves every anchor by
line index. Verifies:
  - every JSON-fact row's anchor occurs in-span
  - inherited rows (J01..J15) vs the r95 map: span/anchor/excerpt identical,
    resolved physical line numbers preserved
  - new row anchor only inside the appended section
  - declared inventory numbers
  - byte-prefix discipline of fictional-excerpts.md vs r95
Calibration: --control shifts one span by +1 and must report a miss.
Usage: v45_check.py <map-path> [--ref-map <r95 map>] [--control]
"""
import argparse
import re
import sys
from pathlib import Path

CELL = re.compile(r"^\s*\|(.+)\|\s*$")


def split_cells(line):
    body = CELL.match(line)
    if not body:
        return None
    return [c.strip() for c in body.group(1).split("|")]


def code_cell(cell):
    """Return the content of the first backtick span in a cell, or None."""
    m = re.search(r"`([^`]*)`", cell)
    return m.group(1) if m else None


def parse_span(cell):
    m = re.match(r"^(\d+)(?:\s*-\s*(\d+))?$", cell.strip())
    if not m:
        return None
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return (a, b)


def parse_map(path):
    """Return dict: rows {id: {pointer, source, ns, excerpt, span, mode, anchor}},
    json_count, editorial_count, declared_numbers."""
    text = Path(path).read_text()
    rows = {}
    json_ids, ed_ids = [], []
    for line in text.split("\n"):
        cells = split_cells(line)
        if not cells:
            continue
        rid = cells[0]
        if re.fullmatch(r"J\d+", rid) and len(cells) == 8:
            json_ids.append(rid)
            rows[rid] = {
                "pointer": code_cell(cells[1]),
                "source": cells[2].strip("`"),
                "ns": cells[3].strip("`"),
                "excerpt": code_cell(cells[4]),
                "span": parse_span(cells[5]),
                "mode": cells[6].strip("`"),
                "anchor": code_cell(cells[7]),
            }
        elif re.fullmatch(r"S\d+", rid) and len(cells) == 7:
            ed_ids.append(rid)
            rows[rid] = {
                "excerpt": code_cell(cells[3]),
                "span": parse_span(cells[4]),
                "mode": cells[5].strip("`"),
                "anchor": code_cell(cells[6]),
            }
    declared = None
    m = re.search(
        r"\*\*Expected inventory:\*\*\s*(\d+)\s*JSON facts;\s*(\d+)\s*editorial rows;\s*"
        r"(\d+)\s*total mapped rows;\s*(\d+)\s*distinct excerpt anchors",
        text,
    )
    if m:
        declared = tuple(int(g) for g in m.groups())
    return {
        "rows": rows,
        "json_ids": json_ids,
        "ed_ids": ed_ids,
        "declared": declared,
        "text": text,
    }


def lines_of(path):
    return Path(path).read_text().split("\n")


def resolve(anchor, lines):
    """Pure-Python line-index resolution: 1-based line numbers containing anchor."""
    return [i + 1 for i, l in enumerate(lines) if anchor in l]


def run(map_path, ref_map_path, control=False, json_expect=None):
    base = Path(map_path).resolve().parent
    m = parse_map(map_path)
    print(f"PARSED {map_path}")
    print(f"  JSON-fact rows: {len(m['json_ids'])} ({', '.join(m['json_ids'])})")
    print(f"  editorial rows: {len(m['ed_ids'])} ({', '.join(m['ed_ids'])})")
    print(f"  declared inventory: {m['declared']}")

    cache = {}

    def get_lines(rel):
        if rel not in cache:
            p = base / rel
            cache[rel] = (p, lines_of(p))
        return cache[rel]

    ok = 0
    misses = []
    outside = []
    json_ids = m["json_ids"]
    for rid in json_ids:
        row = m["rows"][rid]
        p, lines = get_lines(row["excerpt"])
        hits = resolve(row["anchor"], lines)
        span = row["span"]
        if control and rid == json_ids[0]:
            span = (span[0] + 1, span[1] + 1)
            print(f"  CONTROL: {rid} span shifted {row['span']} -> {span}")
        in_span = [h for h in hits if span[0] <= h <= span[1]]
        out = [h for h in hits if not (span[0] <= h <= span[1])]
        if in_span:
            ok += 1
        else:
            misses.append(rid)
        if out:
            outside.append((rid, out))
        extra = f"  [also outside span: {out}]" if out else ""
        print(f"  {'OK  ' if in_span else 'MISS'} {rid} span {span[0]}-{span[1]} anchor found at line(s) {hits}{extra}")

    print(f"ANCHOR CHECK: {ok}/{len(json_ids)} in-span; misses={misses}; outside-span={outside}")

    for rid in m["ed_ids"]:
        row = m["rows"][rid]
        p, lines = get_lines(row["excerpt"])
        hits = resolve(row["anchor"], lines)
        span = row["span"]
        in_span = [h for h in hits if span[0] <= h <= span[1]]
        print(f"  EDITORIAL {rid} span {span[0]}-{span[1]} anchor found at line(s) {hits} "
              f"in-span={in_span} {'OK' if in_span else 'MISS'}")

    if ref_map_path and not control:
        ref = parse_map(ref_map_path)
        refbase = Path(ref_map_path).resolve().parent
        print("\n== inherited rows vs r95 map ==")
        mism = []
        changed_lines = []
        for rid in ref["json_ids"]:
            if rid not in m["rows"]:
                mism.append((rid, "absent in r96"))
                print(f"  {rid}: ABSENT in r96 map")
                continue
            a, b = ref["rows"][rid], m["rows"][rid]
            same = (
                a["span"] == b["span"]
                and a["anchor"] == b["anchor"]
                and a["excerpt"] == b["excerpt"]
                and a["pointer"] == b["pointer"]
                and a["mode"] == b["mode"]
            )
            if not same:
                mism.append((rid, "cell diff"))
            l95 = resolve(a["anchor"], lines_of(refbase / a["excerpt"]))
            l96 = resolve(b["anchor"], lines_of(base / b["excerpt"]))
            if l95 != l96:
                changed_lines.append((rid, l95, l96))
            print(f"  {rid} span {a['span']}=={b['span']} anchor-identical={a['anchor']==b['anchor']} "
                  f"lines r95={l95} r96={l96} {'PRESERVED' if l95 == l96 else 'CHANGED'}")
        print(f"INHERITED: {len(ref['json_ids'])} rows; cell mismatches={mism}; changed physical lines={changed_lines}")

        new_ids = [r for r in json_ids if r not in ref["rows"]]
        print(f"\n== new rows vs r95 map ==\nnew row ids: {new_ids}")
        r95_file_lines = len(lines_of(refbase / "fictional-excerpts.md"))
        for rid in new_ids:
            row = m["rows"][rid]
            hits = resolve(row["anchor"], lines_of(base / row["excerpt"]))
            pre = [h for h in hits if h <= r95_file_lines]
            post = [h for h in hits if h > r95_file_lines]
            print(f"  {rid}: excerpt={row['excerpt']} span={row['span']} hits={hits} "
                  f"pre-appended(<= {r95_file_lines})={pre} appended={post}")

    # byte-prefix discipline
    if ref_map_path and not control:
        refbase = Path(ref_map_path).resolve().parent
        a = (refbase / "fictional-excerpts.md").read_bytes()
        b = (base / "fictional-excerpts.md").read_bytes()
        print(f"\n== byte-prefix ==\nfictional-excerpts.md r95={len(a)}B r96={len(b)}B "
              f"prefix-ok={b[:len(a)] == a}")
        a2 = (refbase / "source-excerpt.md").read_bytes()
        b2 = (base / "source-excerpt.md").read_bytes()
        print(f"source-excerpt.md identical={a2 == b2} ({len(b2)}B)")

    # declared inventory vs parsed
    if m["declared"]:
        parsed = (len(json_ids), len(m["ed_ids"]), len(json_ids) + len(m["ed_ids"]),
                  len({m["rows"][r]["anchor"] for r in m["rows"]}))
        print(f"\n== inventory ==\ndeclared={m['declared']} parsed={parsed} "
              f"match={m['declared'] == parsed}")

    if json_expect is not None and len(json_ids) != json_expect:
        print(f"COUNT CHECK: FAIL expected {json_expect} JSON rows, parsed {len(json_ids)}")
        return 1
    if json_expect is not None:
        print(f"COUNT CHECK: {len(json_ids)} JSON rows == expected {json_expect}")

    verdict = (not misses) and (not outside)
    print(f"\nV45 VERDICT: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("map")
    ap.add_argument("--ref-map")
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--json-expect", type=int, default=None)
    a = ap.parse_args()
    return run(a.map, a.ref_map, a.control, a.json_expect)


if __name__ == "__main__":
    sys.exit(main())
