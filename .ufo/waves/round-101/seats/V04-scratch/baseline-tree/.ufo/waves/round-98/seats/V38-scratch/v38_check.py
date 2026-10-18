#!/usr/bin/env python3
"""V38 anchor-replica-2: independent anchor re-verification for the r98 map.

Own implementation (not support_check.py). For every row of the NEW map:
  - parse the markdown tables with an independent parser
  - resolve the excerpt path inside the fixture
  - find anchor occurrences with a pure-Python scan AND cross-check with
    `grep -nF`
  - in-span iff at least one occurrence and every occurrence line inside the
    declared line span; report outside-span occurrence lines
  - compare inherited rows (same ID in REF map) for anchor/span/path equality
    and resolved line-set equality
  - new rows must occur only beyond the REF excerpt's last line
  - byte-prefix: NEW excerpt file must start with REF excerpt bytes exactly
  - declared inventory must equal parsed counts
  - JSON pointers must resolve in the fixture

Usage: v38_check.py NEW_DIR REF_DIR [--validate]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

SPAN = re.compile(r"^\s*(\d+)(?:\s*[-–]\s*(\d+))?\s*$")
INVENTORY = re.compile(
    r"^\*\*Expected inventory:\*\*\s*(\d+)\s+JSON facts?;\s*(\d+)\s+editorial rows?;\s*"
    r"(\d+)\s+total mapped rows?;\s*(\d+)\s+distinct excerpt anchors?\.\s*$",
    re.IGNORECASE,
)
ROLE_PATTERNS = (
    ("id", re.compile(r"^\s*(?:fact\s+)?id\s*$", re.I)),
    ("pointer", re.compile(r"pointer", re.I)),
    ("source", re.compile(r"^in-world source id$", re.I)),
    ("namespace", re.compile(r"namespace", re.I)),
    ("path", re.compile(r"excerpt path", re.I)),
    ("span", re.compile(r"line span", re.I)),
    ("mode", re.compile(r"delivery mode", re.I)),
    ("anchor", re.compile(r"exact anchor", re.I)),
)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_map(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows, inventory = [], None
    section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            head = line[3:].strip().lower()
            if head.startswith("json facts"):
                section = "json"
            elif head.startswith("editorial rows"):
                section = "editorial"
            else:
                section = None
        m = INVENTORY.match(line)
        if m:
            inventory = tuple(int(x) for x in m.groups())
        if line.lstrip().startswith("|") and "Exact anchor" in line and "Line span" in line:
            header = cells(line)
            roles = {}
            for idx, name in enumerate(header):
                for role, pat in ROLE_PATTERNS:
                    if role not in roles and pat.search(name):
                        roles[role] = idx
                        break
            j = i + 2  # skip separator row
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                row = cells(lines[j])
                if len(row) == len(header):
                    get = lambda r: row[roles[r]].strip().strip("`") if r in roles else ""
                    raw_ptr = get("pointer")
                    tok = re.search(r"`([^`]+)`", row[roles["pointer"]]) if "pointer" in roles else None
                    rows.append({
                        "id": get("id"), "pointer": tok.group(1) if tok else raw_ptr,
                        "source": get("source"),
                        "namespace": get("namespace"), "path": get("path"),
                        "span": get("span"), "mode": get("mode"), "anchor": get("anchor"),
                        "section": section, "mapline": j + 1,
                    })
                j += 1
            i = j
            continue
        i += 1
    return rows, inventory


def parse_span(value):
    m = SPAN.match(value)
    if not m:
        return None
    first = int(m.group(1))
    last = int(m.group(2) or first)
    return (first, last) if first >= 1 and last >= first else None


def occurrences(anchor, text):
    return [n for n, line in enumerate(text.splitlines(), 1) if anchor and anchor in line]


def grep_hits(anchor, filepath):
    r = subprocess.run(["grep", "-nF", "--", anchor, str(filepath)],
                       capture_output=True, text=True)
    hits = []
    if r.returncode == 0:
        for line in r.stdout.splitlines():
            num, sep, _ = line.partition(":")
            if sep and num.isdecimal():
                hits.append(int(num))
    return hits, r.returncode


def resolve_pointer(fixture, pointer):
    m = re.match(r"^([A-Za-z0-9_.-]+\.json)#(.*)$", pointer)
    if not m:
        return None, "pointer shape"
    fname, frag = m.group(1), m.group(2)
    try:
        data = json.loads((fixture / fname).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, f"load {fname}: {e}"
    cur = data
    for raw in frag.split("/"):
        if raw == "":
            continue
        tok = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, list):
            if not tok.isdigit() or int(tok) >= len(cur):
                return None, f"index {tok} out of range in {fname}"
            cur = cur[int(tok)]
        elif isinstance(cur, dict):
            if tok not in cur:
                return None, f"key {tok} missing in {fname}"
            cur = cur[tok]
        else:
            return None, f"walk stopped at {tok} in {fname}"
    return cur, None


def main():
    args = [a for a in sys.argv[1:] if a != "--validate"]
    new_dir, ref_dir = Path(args[0]).resolve(), Path(args[1]).resolve()
    new_map = new_dir / "claim-excerpt-map.md"
    ref_map = ref_dir / "claim-excerpt-map.md"
    new_rows, new_inv = parse_map(new_map)
    ref_rows, _ = parse_map(ref_map)
    ref_by_id = {r["id"]: r for r in ref_rows}
    new_excerpt = new_dir / "fictional-excerpts.md"
    ref_excerpt = ref_dir / "fictional-excerpts.md"
    new_text = new_excerpt.read_text(encoding="utf-8")
    ref_text = ref_excerpt.read_text(encoding="utf-8")
    ref_last = len(ref_text.splitlines())
    prefix_ok = new_text.startswith(ref_text)

    json_rows = [r for r in new_rows if r["section"] == "json"]
    editorial = [r for r in new_rows if r["section"] == "editorial"]
    anchors = {(r["path"], r["anchor"]) for r in new_rows}
    parsed_inv = (len(json_rows), len(editorial), len(new_rows), len(anchors))

    fails, notes = [], []
    print(f"== V38 checker: NEW={new_dir.name} ({len(new_rows)} rows: "
          f"{len(json_rows)} json / {len(editorial)} editorial) vs REF={ref_dir.name} "
          f"({len(ref_rows)} rows) ==")
    print(f"ref excerpt last line={ref_last}; new excerpt prefix-identical={prefix_ok}; "
          f"new excerpt lines={len(new_text.splitlines())}")
    print(f"inventory declared={new_inv} parsed={parsed_inv}")
    if new_inv != parsed_inv:
        fails.append(f"inventory mismatch declared={new_inv} parsed={parsed_inv}")
    if not prefix_ok:
        fails.append("new excerpt is not a byte-prefix-preserving copy of ref excerpt")
    print(f"new rows (vs ref ids): {[r['id'] for r in new_rows if r['id'] not in ref_by_id]}")
    print(f"dropped ref ids: {[r['id'] for r in ref_rows if r['id'] not in {x['id'] for x in new_rows}]}")

    for r in new_rows:
        excerpt = new_dir / r["path"]
        if not excerpt.is_file():
            fails.append(f"{r['id']}: excerpt path missing {r['path']}")
            print(f"{r['id']}  EXCERPT-MISSING {r['path']}")
            continue
        text = excerpt.read_text(encoding="utf-8")
        py = occurrences(r["anchor"], text)
        gr, rc = grep_hits(r["anchor"], excerpt)
        span = parse_span(r["span"])
        in_span = bool(py) and span is not None and all(span[0] <= n <= span[1] for n in py)
        outside = [] if span is None else [n for n in py if not (span[0] <= n <= span[1])]
        py_gr_agree = py == gr
        ref = ref_by_id.get(r["id"])
        if ref:
            anchor_same = ref["anchor"] == r["anchor"]
            span_same = ref["span"] == r["span"]
            path_same = ref["path"] == r["path"]
            ref_lines = occurrences(ref["anchor"], (ref_dir / r["path"]).read_text(encoding="utf-8")
                                   if (ref_dir / r["path"]).is_file() else ref_text)
            lines_same = ref_lines == py
            extra = (f"vs-ref anchor-identical={anchor_same} span-same={span_same} "
                     f"path-same={path_same} lines ref={ref_lines} == this={py} same={lines_same}")
            if not (anchor_same and span_same and path_same and lines_same):
                fails.append(f"{r['id']}: inherited row drift ({extra})")
        else:
            appended_only = bool(py) and all(n > ref_last for n in py)
            extra = f"appended-only={appended_only} (ref file {ref_last} lines)"
            if not appended_only:
                fails.append(f"{r['id']}: new row anchor not confined to appended section")
        if not py:
            fails.append(f"{r['id']}: anchor not found")
        if not in_span:
            fails.append(f"{r['id']}: anchor not in-span span={r['span']} hits={py} outside={outside}")
        if not py_gr_agree:
            fails.append(f"{r['id']}: python scan {py} != grep {gr} (rc={rc})")
        ptr_detail = ""
        if r["pointer"]:
            val, err = resolve_pointer(new_dir, r["pointer"])
            ptr_detail = f" ptr={'OK' if err is None else 'ERR:' + err}"
            if err is not None:
                fails.append(f"{r['id']}: pointer {r['pointer']} unresolved: {err}")
        print(f"{r['id']}  span={r['span']} py={py} grep={gr} agree={py_gr_agree} "
              f"IN-SPAN={in_span} outside={outside} {extra}{ptr_detail}")

    # source_id match for json rows (supplementary): pointed fact's source_id == declared source
    for r in json_rows:
        if not r["pointer"] or not r["source"]:
            continue
        val, err = resolve_pointer(new_dir, r["pointer"])
        if err is not None:
            continue
        if r["pointer"].endswith("first_appearance"):
            fact_src = val
        elif isinstance(val, dict) and "source_id" in val:
            fact_src = val["source_id"]
        else:
            fact_src = None
        if fact_src is not None and fact_src != r["source"]:
            notes.append(f"{r['id']}: pointed source_id={fact_src} != map source={r['source']}")

    print("NOTES:" if notes else "NOTES: none")
    for n in notes:
        print("  " + n)
    if fails:
        print("FAILS:")
        for f in fails:
            print("  " + f)
        print("RESULT FAIL")
        return 1
    print("RESULT ALL-ANCHOR-CHECKS-PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
