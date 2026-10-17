#!/usr/bin/env python3
"""V16 c3-anchors (round 97) — independent anchor/span/line checker.

Own implementation: parses the map tables, resolves every anchor via
`grep -nF` subprocess AND a pure-Python substring scan, cross-checks the two,
checks in-span containment / outside-span occurrences, inherited-row
equality vs a reference map, and new-row placement in the appended section.

Usage:
  v16_check.py --new <fixture-dir> --ref <fixture-dir> [--expect-new IDS]
  v16_check.py --validate            # r96 vs r95 parser validation
Exit 0 iff all checks pass; prints per-row evidence lines.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
ROW_ID = re.compile(r"^[JS]\d{2}$")


def parse_map(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = {}
    section = None
    inventory = None
    for raw in lines:
        s = raw.strip()
        if s.startswith("## "):
            h = s[3:].strip().lower()
            section = "json" if h.startswith("json facts") else (
                "editorial" if h.startswith("editorial rows") else None)
        m = re.match(r"^\*\*Expected inventory:\*\*\s*(.+)$", s)
        if m:
            inventory = m.group(1)
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        cid = cells[0].strip("`")
        if not ROW_ID.match(cid):
            continue
        paths = [c.strip("`") for c in cells if re.fullmatch(r"[\w.-]+\.md", c.strip("`"))]
        spans = []
        for c in cells:
            cc = c.strip("`").replace("\u2013", "-").strip()
            mm = re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?", cc)
            if mm:
                spans.append((int(mm.group(1)), int(mm.group(2) or mm.group(1))))
        anchor = cells[-1].strip("`")
        if len(paths) != 1 or len(spans) != 1 or not anchor:
            raise SystemExit(f"PARSE-FAIL {path}: row {cid} paths={paths} spans={spans} anchor={anchor!r}")
        rows[cid] = dict(section=section, path=paths[0], span=spans[0], anchor=anchor)
    return rows, inventory


def resolve(fixture, row):
    p = fixture / row["path"]
    if not p.exists():
        return p, None, None, None
    text = p.read_text(encoding="utf-8")
    py_lines = [i + 1 for i, t in enumerate(text.splitlines()) if row["anchor"] in t]
    cp = subprocess.run(["grep", "-nF", "-e", row["anchor"], "--", str(p)],
                        capture_output=True, text=True)
    grep_lines = sorted(int(l.split(":", 1)[0]) for l in cp.stdout.splitlines() if l.strip())
    return p, grep_lines, py_lines, len(text.splitlines())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new")
    ap.add_argument("--ref")
    ap.add_argument("--ref2")
    ap.add_argument("--expect-new", default="")
    ap.add_argument("--validate", action="store_true")
    args = ap.parse_args()

    if args.validate:
        new_dir = ROOT / "corpus/fixtures/r96-crossing-response"
        ref_dir = ROOT / "corpus/fixtures/r95-crossing-aftermath"
        args.new, args.ref = str(new_dir), str(ref_dir)
        args.expect_new = "J16"
    new_dir, ref_dir = Path(args.new), Path(args.ref)
    ref2_dir = Path(args.ref2) if args.ref2 else None
    expect_new = set(args.expect_new.split()) if args.expect_new else None

    new_rows, new_inv = parse_map(new_dir / "claim-excerpt-map.md")
    ref_rows, ref_inv = parse_map(ref_dir / "claim-excerpt-map.md")
    ref2_rows = parse_map(ref2_dir / "claim-excerpt-map.md")[0] if ref2_dir else None

    fails = []
    print(f"== V16 checker: NEW={new_dir.name} ({len(new_rows)} rows) vs REF={ref_dir.name} ({len(ref_rows)} rows) ==")
    ref_fx_lines = len((ref_dir / "fictional-excerpts.md").read_text(encoding="utf-8").splitlines())

    # resolve ref rows once (for inherited equality)
    ref_res = {}
    for rid, row in ref_rows.items():
        p, g, py, n = resolve(ref_dir, row)
        ref_res[rid] = (g, py)
    ref2_res = {}
    if ref2_rows is not None:
        for rid, row in ref2_rows.items():
            p, g, py, n = resolve(ref2_dir, row)
            ref2_res[rid] = (g, py)

    new_ids = sorted(set(new_rows) - set(ref_rows))
    if expect_new is not None and set(new_ids) != expect_new:
        fails.append(f"new-row set {new_ids} != expected {sorted(expect_new)}")
    print(f"new rows (vs ref): {new_ids}")

    for rid in sorted(new_rows):
        row = new_rows[rid]
        p, grep_lines, py_lines, nlines = resolve(new_dir, row)
        if grep_lines is None:
            fails.append(f"{rid}: excerpt path missing {p}")
            print(f"{rid}  MISSING-PATH {p}")
            continue
        lo, hi = row["span"]
        ok = (grep_lines == py_lines) and len(grep_lines) > 0
        outside = [l for l in grep_lines if not (lo <= l <= hi)]
        in_span = len(grep_lines) > 0 and not outside
        if not ok:
            fails.append(f"{rid}: grep {grep_lines} != py {py_lines}")
        if not in_span:
            fails.append(f"{rid}: occurrences outside span {lo}-{hi}: {outside} (grep={grep_lines})")
        if rid in ref_rows:
            ra, rs = ref_rows[rid]["anchor"], ref_rows[rid]["span"]
            rg, rpy = ref_res[rid]
            anchor_same = (ra == row["anchor"])
            span_same = (rs == row["span"])
            lines_same = (rg == grep_lines)
            if not (anchor_same and span_same and lines_same):
                fails.append(f"{rid}: inherited mismatch anchor={anchor_same} span={span_same} lines={lines_same}")
            extra = ""
            if ref2_rows is not None and rid in ref2_rows:
                r2g, _ = ref2_res[rid]
                extra = f" ref2({ref2_dir.name})={r2g} same2={r2g == grep_lines}"
            print(f"{rid}  span={lo}-{hi}  grep={grep_lines} py={py_lines} occ={len(grep_lines)} "
                  f"IN-SPAN={in_span} outside-span={outside}  vs-ref: anchor-identical={anchor_same} "
                  f"span-same={span_same} lines ref={rg} == this={grep_lines} same={lines_same}{extra}")
        else:
            # new row: must occur only in appended section
            all_appended = all(l > ref_fx_lines for l in grep_lines)
            if not all_appended:
                fails.append(f"{rid}: new-row occurrences not all beyond line {ref_fx_lines}: {grep_lines}")
            ref_p = ref_dir / row["path"]
            ref_has = False
            if ref_p.exists():
                ref_has = any(row["anchor"] in t for t in ref_p.read_text(encoding="utf-8").splitlines())
            if ref_has:
                fails.append(f"{rid}: new anchor already present in ref file")
            if lo <= ref_fx_lines:
                fails.append(f"{rid}: new span {lo}-{hi} starts before/at ref line count {ref_fx_lines}")
            print(f"{rid}  span={lo}-{hi}  grep={grep_lines} py={py_lines} occ={len(grep_lines)} "
                  f"IN-SPAN={in_span} outside-span={outside}  appended-only={all_appended} "
                  f"(ref file {ref_fx_lines} lines; ref-has-anchor={ref_has}; file has {nlines} lines)")

    # inventory
    inv_counts = {"json": sum(1 for r in new_rows.values() if r["section"] == "json"),
                  "editorial": sum(1 for r in new_rows.values() if r["section"] == "editorial"),
                  "total": len(new_rows),
                  "distinct": len({(r["path"], r["anchor"]) for r in new_rows.values()})}
    print(f"inventory declared={new_inv!r}")
    print(f"inventory parsed={inv_counts}")
    m = re.match(r"(\d+) JSON facts?;\s*(\d+) editorial rows?;\s*(\d+) total mapped rows?;\s*(\d+) distinct excerpt anchors?",
                 new_inv or "")
    if not m:
        fails.append("inventory declaration unparseable")
    else:
        declared = tuple(int(x) for x in m.groups())
        parsed = (inv_counts["json"], inv_counts["editorial"], inv_counts["total"], inv_counts["distinct"])
        if declared != parsed:
            fails.append(f"inventory declared {declared} != parsed {parsed}")
        print(f"inventory match={declared == parsed} declared={declared} parsed={parsed}")

    # byte-prefix discipline for fictional-excerpts.md
    ref_fx = (ref_dir / "fictional-excerpts.md").read_bytes()
    new_fx = (new_dir / "fictional-excerpts.md").read_bytes()
    prefix_ok = new_fx[:len(ref_fx)] == ref_fx
    print(f"fictional-excerpts.md: ref={len(ref_fx)}B this={len(new_fx)}B byte-prefix-ok={prefix_ok}")
    if not prefix_ok:
        fails.append("fictional-excerpts.md is not a byte-prefix extension of ref")

    print("FAILURES:", fails if fails else "none")
    print("RESULT:", "ALL-ANCHOR-CHECKS-PASS" if not fails else "CHECKS-FAILED")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
