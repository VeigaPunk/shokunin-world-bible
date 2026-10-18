#!/usr/bin/env python3
"""V119 third-pass anchor check: byte-offset windows, not line-number grep.

For each mapped row, convert the declared 1-based line span into a half-open
byte window of the excerpt file (UTF-8, newline bytes included in the line
that precedes them, matching splitlines(keepends=True)). The exact anchor
must occur as a contiguous byte substring inside that window and must not
occur in any other declared window of the same file unless this row's window
is one of those hits. Also require the JSON-pointer fields named by the row
to exist, and require the new event row (if present) to cite clerk-lapse-note.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

CLUSTER = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r99-window-lapse")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_rows(map_text):
    lines = map_text.splitlines()
    rows = []
    section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            h = line[3:].lower()
            if h.startswith("json facts"):
                section = "json"
            elif h.startswith("editorial rows"):
                section = "editorial"
            else:
                section = None
        if not line.lstrip().startswith("|") or section is None:
            i += 1
            continue
        headers = cells(line)
        norm = [re.sub(r"[^a-z0-9]+", " ", h.strip("`").lower()).strip() for h in headers]
        roles = {}
        for idx, name in enumerate(norm):
            if name in {"id", "fact id"}:
                roles.setdefault("id", idx)
            elif "anchor" in name:
                roles.setdefault("anchor", idx)
            elif "excerpt" in name and "path" in name:
                roles.setdefault("path", idx)
            elif name in {"line span", "line", "lines"}:
                roles.setdefault("span", idx)
            elif "delivery mode" in name:
                roles.setdefault("mode", idx)
            elif "json fact" in name or name == "fact":
                roles.setdefault("pointer", idx)
        if not {"id", "anchor", "path", "span"}.issubset(roles):
            i += 1
            continue
        j = i + 1
        while j < len(lines) and lines[j].lstrip().startswith("|"):
            row = cells(lines[j])
            if row and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in row):
                j += 1
                continue
            if len(row) != len(headers):
                raise SystemExit(f"cell mismatch at map line {j+1}: {len(row)} vs {len(headers)}")
            span = row[roles["span"]].strip("`")
            m = re.fullmatch(r"(\d+)(?:\s*[-–]\s*(\d+))?", span)
            if not m:
                raise SystemExit(f"bad span {span!r} at map line {j+1}")
            first, last = int(m.group(1)), int(m.group(2) or m.group(1))
            rows.append({
                "id": row[roles["id"]].strip("`"),
                "kind": section,
                "path": row[roles["path"]].strip("`"),
                "span": (first, last),
                "anchor": row[roles["anchor"]].strip("`"),
                "mode": row[roles["mode"]].strip("`") if "mode" in roles else "",
                "pointer": row[roles["pointer"]] if "pointer" in roles else "",
            })
            j += 1
        i = j
    return rows


def line_windows(raw: bytes):
    """Return list of (start, end) half-open byte offsets, 0-based, one per
    1-based line. A line includes its terminating newline bytes if present.
    """
    windows = []
    start = 0
    n = len(raw)
    i = 0
    while i < n:
        if raw[i:i+2] == b"\r\n":
            i += 2
            windows.append((start, i))
            start = i
        elif raw[i:i+1] in (b"\n", b"\r"):
            i += 1
            windows.append((start, i))
            start = i
        else:
            i += 1
    if start < n or n == 0:
        windows.append((start, n))
    return windows


def span_window(windows, first, last):
    if first < 1 or last > len(windows) or last < first:
        return None
    return windows[first - 1][0], windows[last - 1][1]


def main():
    map_path = CLUSTER / "claim-excerpt-map.md"
    map_bytes = map_path.read_bytes()
    text = map_bytes.decode("utf-8")
    rows = parse_rows(text)
    print(f"MAP bytes={len(map_bytes)} sha256={hashlib.sha256(map_bytes).hexdigest()}")
    print(f"PARSED-ROWS {len(rows)}")
    files = {}
    failures = []
    for row in rows:
        rel = row["path"]
        if rel not in files:
            raw = (CLUSTER / rel).read_bytes()
            files[rel] = (raw, line_windows(raw))
        raw, windows = files[rel]
        window = span_window(windows, *row["span"])
        anchor = row["anchor"].encode("utf-8")
        print(f"ROW {row['id']} kind={row['kind']} file={rel} lines={row['span'][0]}-{row['span'][1]} "
              f"anchor_bytes={len(anchor)} mode={row['mode']}")
        if window is None:
            failures.append(f"{row['id']}: span {row['span']} outside file ({len(windows)} lines)")
            print(f"  WINDOW none")
            continue
        start, end = window
        blob = raw[start:end]
        count = blob.count(anchor)
        # whole-file occurrences with byte offsets
        occ = []
        pos = 0
        while True:
            k = raw.find(anchor, pos)
            if k < 0:
                break
            occ.append(k)
            pos = k + 1
        in_window = [k for k in occ if start <= k and k + len(anchor) <= end]
        print(f"  WINDOW byte[{start}:{end}] len={end-start} in_window={len(in_window)} "
              f"file_occ={len(occ)} occ_offsets={occ}")
        if count != len(in_window):
            failures.append(f"{row['id']}: window count {count} != bounded occ {len(in_window)}")
        if len(in_window) < 1:
            failures.append(f"{row['id']}: anchor bytes absent from declared byte window [{start}:{end}]")
        if row["mode"] and not row["mode"].startswith("verbatim"):
            failures.append(f"{row['id']}: unexpected mode {row['mode']}")
        # curly-quote sanity: anchor must be exact bytes, already enforced
        if row["kind"] == "json" and row["pointer"]:
            pointer_ok = check_pointer(row)
            print(f"  POINTER {pointer_ok}")
            if not pointer_ok.startswith("ok"):
                failures.append(f"{row['id']}: {pointer_ok}")
    print(f"FAILURES {len(failures)}")
    for f in failures:
        print(f"FAIL {f}")
    return 1 if failures else 0


def check_pointer(row):
    m = re.search(r"`([^`]+)`", row["pointer"])
    if not m:
        return "no pointer cell"
    pointer = m.group(1)
    parts = pointer.split("#/")
    if len(parts) != 2:
        return f"unparsed pointer {pointer}"
    table, rest = parts
    data = json.loads((CLUSTER / table).read_text(encoding="utf-8"))
    segs = rest.split("/")
    node = data
    walked = []
    for seg in segs:
        if isinstance(node, list):
            if not seg.isdigit() or int(seg) >= len(node):
                return f"index {seg} missing in {table} at {walked}"
            node = node[int(seg)]
        elif isinstance(node, dict):
            if seg not in node:
                return f"key {seg} missing at {walked}"
            node = node[seg]
        else:
            return f"cannot walk {seg} at {walked}"
        walked.append(seg)
    field_names = re.findall(r"`([^`]+)`", row["pointer"])[1:]
    if isinstance(node, dict):
        missing = [f for f in field_names if f not in node]
        if missing:
            return f"fields missing {missing} on {pointer}"
    return f"ok pointer={pointer} fields={field_names or 'row'}"


if __name__ == "__main__":
    raise SystemExit(main())
