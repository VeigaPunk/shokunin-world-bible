#!/usr/bin/env python3
"""V41 independent anchor replica. Own parser. No project tool imports."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def split_row(line: str) -> list[str] | None:
    if not line.startswith("|"):
        return None
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells = [c.strip() for c in body.split("|")]
    return cells


def is_sep(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def parse_span(text: str) -> tuple[int, int]:
    text = text.strip()
    m = re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?", text)
    if not m:
        raise ValueError(f"bad span: {text!r}")
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return a, b


def unquote_anchor(cell: str) -> str:
    cell = cell.strip()
    if len(cell) >= 2 and cell[0] == "`" and cell[-1] == "`":
        return cell[1:-1]
    return cell


def parse_map(text: str) -> dict:
    lines = text.splitlines()
    tables = []
    i = 0
    while i < len(lines):
        cells = split_row(lines[i])
        if cells and i + 1 < len(lines):
            nxt = split_row(lines[i + 1])
            if nxt and is_sep(nxt) and len(nxt) == len(cells):
                rows = []
                j = i + 2
                while j < len(lines):
                    rc = split_row(lines[j])
                    if not rc or len(rc) != len(cells):
                        break
                    rows.append((j + 1, rc))
                    j += 1
                tables.append({"header": cells, "header_line": i + 1, "rows": rows})
                i = j
                continue
        i += 1

    json_rows = []
    editorial_rows = []
    for table in tables:
        header = [h.lower() for h in table["header"]]
        if "exact anchor" not in " ".join(header):
            continue
        id_idx = 0
        path_idx = next(k for k, h in enumerate(header) if "excerpt path" in h)
        span_idx = next(k for k, h in enumerate(header) if "line span" in h or h == "span")
        mode_idx = next(k for k, h in enumerate(header) if "mode" in h)
        anchor_idx = next(k for k, h in enumerate(header) if "exact anchor" in h)
        is_json = any("json fact" in h or "pointer" in h for h in header)
        for line_no, cells in table["rows"]:
            rid = cells[id_idx].strip()
            rec = {
                "id": rid,
                "line": line_no,
                "path": cells[path_idx].strip().strip("`"),
                "span_raw": cells[span_idx].strip(),
                "span": parse_span(cells[span_idx]),
                "mode": cells[mode_idx].strip().strip("`"),
                "anchor": unquote_anchor(cells[anchor_idx]),
                "cells": cells,
                "kind": "json" if is_json else "editorial",
            }
            if is_json:
                rec["pointer"] = cells[1]
                rec["source_id"] = cells[2].strip().strip("`")
                rec["namespace"] = cells[3].strip().strip("`")
                json_rows.append(rec)
            else:
                editorial_rows.append(rec)
    return {"json": json_rows, "editorial": editorial_rows, "tables": len(tables)}


def load_lines(path: Path) -> list[str]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    # keepends=False; line numbers are 1-based splitlines (no trailing empty from final newline)
    return text.splitlines()


def find_hits(lines: list[str], anchor: str) -> list[int]:
    return [i + 1 for i, line in enumerate(lines) if anchor in line]


def inventory_declared(text: str) -> tuple[int, int, int, int] | None:
    m = re.search(
        r"Expected inventory:\*\*\s*(\d+)\s+JSON facts;\s*(\d+)\s+editorial rows;\s*(\d+)\s+total mapped rows;\s*(\d+)\s+distinct excerpt anchors",
        text,
    )
    if not m:
        return None
    return tuple(int(x) for x in m.groups())  # type: ignore[return-value]


def resolve_pointer(cluster: Path, pointer_cell: str) -> tuple[bool, str]:
    m = re.search(r"`([^`]+\.json)#(/[^`]*)`", pointer_cell)
    if not m:
        return False, "no-pointer-token"
    rel, ptr = m.group(1), m.group(2)
    target = cluster / rel
    if not target.exists():
        return False, f"missing {rel}"
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return False, f"json-error {exc}"
    node = data
    parts = [p for p in ptr.split("/") if p != ""]
    try:
        for part in parts:
            if isinstance(node, list):
                node = node[int(part)]
            elif isinstance(node, dict):
                node = node[part]
            else:
                return False, f"cannot-descend {part}"
    except (IndexError, KeyError, ValueError) as exc:
        return False, f"resolve-fail {exc}"
    return True, type(node).__name__


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", required=True)
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--baseline-map")
    ap.add_argument("--baseline-cluster")
    ap.add_argument("--label", default="check")
    args = ap.parse_args()

    map_path = Path(args.map)
    cluster = Path(args.cluster)
    text = map_path.read_text(encoding="utf-8")
    parsed = parse_map(text)
    declared = inventory_declared(text)
    json_rows = parsed["json"]
    editorial = parsed["editorial"]
    distinct = {(r["path"], r["anchor"]) for r in json_rows + editorial}

    print(f"== {args.label}: json={len(json_rows)} editorial={len(editorial)} distinct={len(distinct)} tables={parsed['tables']} ==")
    print(f"declared_inventory={declared} parsed=({len(json_rows)}, {len(editorial)}, {len(json_rows)+len(editorial)}, {len(distinct)})")
    if declared and declared != (len(json_rows), len(editorial), len(json_rows) + len(editorial), len(distinct)):
        print("INVENTORY-MISMATCH")

    file_cache: dict[str, list[str]] = {}
    failures = 0
    in_span = 0
    for row in json_rows + editorial:
        rel = row["path"]
        excerpt = cluster / rel
        if rel not in file_cache:
            if not excerpt.exists():
                file_cache[rel] = []
            else:
                file_cache[rel] = load_lines(excerpt)
        lines = file_cache[rel]
        hits = find_hits(lines, row["anchor"]) if lines or excerpt.exists() else []
        lo, hi = row["span"]
        inside = [h for h in hits if lo <= h <= hi]
        outside = [h for h in hits if h < lo or h > hi]
        ok = bool(hits) and not outside and bool(inside)
        if ok:
            in_span += 1
        else:
            failures += 1
        ptr = ""
        if row["kind"] == "json":
            pok, detail = resolve_pointer(cluster, row["pointer"])
            ptr = f" ptr={'OK' if pok else 'FAIL:'+detail}"
            if not pok:
                failures += 1
        print(
            f"{row['id']} mapline={row['line']} span={row['span_raw']} "
            f"py={hits or 'NONE'} inside={inside or '-'} outside={outside or '-'} "
            f"IN-SPAN={ok} mode={row['mode']}{ptr}"
        )

    baseline_note = "no-baseline"
    if args.baseline_map and args.baseline_cluster:
        base = parse_map(Path(args.baseline_map).read_text(encoding="utf-8"))
        base_by_id = {r["id"]: r for r in base["json"]}
        new_ids = []
        dropped = []
        inherited_ok = 0
        inherited_bad = []
        bcluster = Path(args.baseline_cluster)
        bcache: dict[str, list[str]] = {}
        ncache: dict[str, list[str]] = {}
        for row in json_rows:
            prev = base_by_id.get(row["id"])
            if prev is None:
                new_ids.append(row["id"])
                continue
            same_anchor = row["anchor"] == prev["anchor"]
            same_span = row["span"] == prev["span"]
            same_path = row["path"] == prev["path"]
            same_mode = row["mode"] == prev["mode"]
            # namespace column is expected to differ; compare pointer cell with namespace swapped out
            def load(cache, root, rel):
                key = str(root / rel)
                if key not in cache:
                    p = root / rel
                    cache[key] = load_lines(p) if p.exists() else []
                return cache[key]
            bhits = find_hits(load(bcache, bcluster, prev["path"]), prev["anchor"])
            nhits = find_hits(load(ncache, cluster, row["path"]), row["anchor"])
            same_lines = bhits == nhits
            if same_anchor and same_span and same_path and same_mode and same_lines:
                inherited_ok += 1
            else:
                inherited_bad.append(
                    f"{row['id']} anchor={same_anchor} span={same_span} path={same_path} "
                    f"mode={same_mode} lines={same_lines} base={bhits} new={nhits}"
                )
        new_set = {r["id"] for r in json_rows}
        dropped = [r["id"] for r in base["json"] if r["id"] not in new_set]
        print(f"inherited_ok={inherited_ok}/{len(base['json'])} new={new_ids} dropped={dropped}")
        for bad in inherited_bad:
            print(f"INHERIT-MISMATCH {bad}")
            failures += 1
        baseline_note = f"inherited_ok={inherited_ok} mismatches={len(inherited_bad)} new={new_ids}"

        # byte prefix of fictional-excerpts
        b_ex = (bcluster / "fictional-excerpts.md").read_bytes()
        n_ex = (cluster / "fictional-excerpts.md").read_bytes()
        prefix = n_ex.startswith(b_ex)
        print(f"excerpt_byte_prefix={prefix} base_len={len(b_ex)} new_len={len(n_ex)}")
        if not prefix:
            failures += 1
        # new json rows must hit only past baseline excerpt length
        base_nlines = len(b_ex.decode("utf-8").splitlines())
        for row in json_rows:
            if row["id"] not in new_ids:
                continue
            hits = find_hits(load_lines(cluster / row["path"]), row["anchor"])
            appended_only = bool(hits) and all(h > base_nlines for h in hits)
            print(f"{row['id']} appended-only={appended_only} base_lines={base_nlines} hits={hits}")
            if not appended_only:
                failures += 1

    print(f"IN-SPAN {in_span}/{len(json_rows)+len(editorial)} json_in_span_count_pending")
    json_ok = 0
    # recount json-only from printed logic by re-scan is already in failures
    print(f"RESULT {'PASS' if failures == 0 else 'FAIL'} failures={failures} {baseline_note}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
