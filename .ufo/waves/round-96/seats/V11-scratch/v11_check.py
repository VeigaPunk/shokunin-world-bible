#!/usr/bin/env python3
"""V11 r96 c2-anchors independent checker.

Verifies claim-excerpt-map rows: every anchor resolves via grep -nF AND a pure
Python substring scan at identical line sets; all occurrences inside the
declared span; inherited rows byte-identical anchor/span and same resolved
lines as the r95 map; new rows only inside the appended section; declared
inventory matches parse; byte-prefix discipline for the excerpt file.

Usage:
  v11_check.py validate            # r95 map vs r95 files, ref r94 (parser self-validation)
  v11_check.py run                 # r96 map vs r96 files, ref r95 (the real check)
"""
import hashlib
import os
import re
import subprocess
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
R96 = f"{ROOT}/corpus/fixtures/r96-crossing-response"
R95 = f"{ROOT}/corpus/fixtures/r95-crossing-aftermath"
R94 = f"{ROOT}/corpus/fixtures/r94-paired-crossing"


def parse_map(path):
    rows = {}
    declared = None
    for ln in open(path, encoding="utf-8"):
        if "Expected inventory" in ln:
            declared = ln.strip()
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells[0] in ("ID",) or set(cells[0]) <= set("-: "):
            continue
        rid = cells[0].strip("` ")
        if not (rid.startswith("J") or rid.startswith("S")):
            continue
        if len(cells) < 7:
            raise SystemExit(f"row {rid}: too few cells ({len(cells)}): {cells}")
        if len(cells) >= 8:
            path_i, span_i = 4, 5
        else:
            path_i, span_i = 3, 4
        rows[rid] = {
            "kind": rid[0],
            "excerpt": cells[path_i].strip("` "),
            "span": cells[span_i].strip("` "),
            "mode": cells[-2].strip("` "),
            "anchor": cells[-1].strip("` "),
            "cells": cells,
        }
    return rows, declared


def parse_span(s):
    s = s.strip().strip("`")
    m = re.fullmatch(r"(\d+)(?:-(\d+))?", s)
    if not m:
        raise SystemExit(f"bad span: {s!r}")
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return a, b


def grep_nF(anchor, path):
    p = subprocess.run(["grep", "-nF", "-e", anchor, "--", path],
                       capture_output=True, text=True)
    lines = sorted(int(o.split(":", 1)[0]) for o in p.stdout.splitlines())
    return lines, p.returncode


def py_scan(anchor, path):
    lines, total = [], 0
    for i, ln in enumerate(open(path, encoding="utf-8"), 1):
        c = ln.count(anchor)
        if c:
            lines.append(i)
            total += c
    return sorted(lines), total


def check(mdir, map_path, ref_map=None, ref_mdir=None, new_ids=(), label="", prefix_ref=None):
    rows, declared = parse_map(map_path)
    ref_rows = {}
    if ref_map and os.path.exists(ref_map):
        ref_rows, _ = parse_map(ref_map)
    ok = True
    print(f"== {label}: parsed {sum(1 for r in rows.values() if r['kind']=='J')} json rows, "
          f"{sum(1 for r in rows.values() if r['kind']=='S')} editorial rows ==")
    for rid in sorted(rows):
        r = rows[rid]
        exp = os.path.join(mdir, r["excerpt"])
        if not os.path.exists(exp):
            print(f"{rid}: EXCERPT-MISSING {r['excerpt']}")
            ok = False
            continue
        g, grc = grep_nF(r["anchor"], exp)
        p, total = py_scan(r["anchor"], exp)
        span = parse_span(r["span"])
        outside = [x for x in p if not (span[0] <= x <= span[1])]
        agree = g == p
        in_span = bool(g) and not outside and agree
        flag = "IN-SPAN" if in_span else "DRIFT"
        if not in_span or not agree:
            ok = False
        extra = ""
        if rid in new_ids:
            r95file = os.path.join(prefix_ref, r["excerpt"]) if prefix_ref else None
            pre = []
            if r95file and os.path.exists(r95file):
                pre, _ = py_scan(r["anchor"], r95file)
            appended_only = not pre and all(x > prefix_lines for x in p)
            extra = f" pre95={pre} appended-only={appended_only}"
            if pre or not all(x > prefix_lines for x in p):
                ok = False
        print(f"{rid}  excerpt={r['excerpt']} span={span[0]}-{span[1]} grep={g} py={p} "
              f"occ={total} {flag} outside-span={outside}{extra}")
        if rid in ref_rows:
            rr = ref_rows[rid]
            same_anchor = rr["anchor"] == r["anchor"]
            same_span = rr["span"] == r["span"]
            ref_lines, _ = py_scan(rr["anchor"], os.path.join(ref_mdir, rr["excerpt"]))
            same_lines = ref_lines == p
            if not (same_anchor and same_span and same_lines):
                ok = False
            print(f"     vs-ref({rid}): anchor-identical={same_anchor} span-same={same_span} "
                  f"lines ref={ref_lines} == this={p} same={same_lines}")
    newrows = sorted(set(rows) - set(ref_rows)) if ref_rows else sorted(rows)
    print(f"new row ids (vs ref): {newrows}")
    # inventory
    if declared:
        nums = [int(x) for x in re.findall(r"(\d+)", declared)]
        parsed_j = sum(1 for r in rows.values() if r["kind"] == "J")
        parsed_s = sum(1 for r in rows.values() if r["kind"] == "S")
        parsed_total = len(rows)
        distinct = len({(r["excerpt"], r["anchor"]) for r in rows.values()})
        parsed = [parsed_j, parsed_s, parsed_total, distinct]
        match = nums == parsed
        if not match:
            ok = False
        print(f"inventory declared={nums} parsed={parsed} match={match}")
        print(f"declared-line: {declared}")
    # byte prefix discipline
    if prefix_ref:
        rf = os.path.join(prefix_ref, "fictional-excerpts.md")
        nf = os.path.join(mdir, "fictional-excerpts.md")
        if os.path.exists(rf) and os.path.exists(nf):
            rb = open(rf, "rb").read()
            nb = open(nf, "rb").read()
            print(f"fictional-excerpts.md: ref={len(rb)}B this={len(nb)}B "
                  f"byte-prefix-ok={nb[:len(rb)] == rb}")
            if nb[:len(rb)] != rb:
                ok = False
    return ok


def main():
    global prefix_lines
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if mode == "validate":
        prefix_lines = sum(1 for _ in open(f"{R94}/fictional-excerpts.md"))
        ok = check(R95, f"{R95}/claim-excerpt-map.md", ref_map=f"{R94}/claim-excerpt-map.md",
                   ref_mdir=R94, new_ids=("J15",), label="VALIDATE r95 vs r94", prefix_ref=R94)
    else:
        prefix_lines = sum(1 for _ in open(f"{R95}/fictional-excerpts.md"))
        rows, _ = parse_map(f"{R96}/claim-excerpt-map.md")
        ref_rows, _ = parse_map(f"{R95}/claim-excerpt-map.md")
        new_ids = tuple(sorted(set(rows) - set(ref_rows)))
        ok = check(R96, f"{R96}/claim-excerpt-map.md", ref_map=f"{R95}/claim-excerpt-map.md",
                   ref_mdir=R95, new_ids=new_ids, label="RUN r96 vs r95", prefix_ref=R95)
    print("ALL-ANCHOR-CHECKS-PASS" if ok else "ANCHOR-CHECKS-FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
