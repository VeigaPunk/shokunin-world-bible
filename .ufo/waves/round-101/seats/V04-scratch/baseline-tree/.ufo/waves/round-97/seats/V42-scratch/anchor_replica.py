#!/usr/bin/env python3
"""V42 independent anchor replica verifier.

Parses a claim-excerpt map with a from-scratch parser (no project tool is
invoked) and re-verifies:
  (a) in-span: every occurrence of each JSON-fact anchor in the referenced
      excerpt file falls inside the row's declared line span;
  (b) line numbers preserved: for rows shared with a baseline map+cluster,
      the row's pointer/path/span/mode/anchor cells are identical and the
      anchor resolves to the same line numbers in both clusters.

Exit 0 = all checks pass; 1 = at least one failure; 2 = input error.
"""

import argparse
import re
import sys
from pathlib import Path


def cells(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(row):
    return bool(row) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in row
    )


def normalized(value):
    return re.sub(r"[^a-z0-9]+", " ", value.strip().strip("`").casefold()).strip()


def parse_facts_table(map_path):
    lines = map_path.read_text(encoding="utf-8").splitlines()
    starts = [
        index for index, line in enumerate(lines)
        if re.match(r"^##\s+JSON facts(?:\s|$|\()", line, re.IGNORECASE)
    ]
    if len(starts) != 1:
        raise SystemExit(f"INPUT-ERROR: {map_path}: expected one '## JSON facts' heading, found {len(starts)}")
    start = starts[0]
    end = next(
        (index for index in range(start + 1, len(lines)) if re.match(r"^#{1,6}\s+", lines[index])),
        len(lines),
    )
    table_start = next(
        (index for index in range(start + 1, end) if lines[index].lstrip().startswith("|")),
        None,
    )
    if table_start is None:
        raise SystemExit(f"INPUT-ERROR: {map_path}: no table under JSON facts")
    headers = cells(lines[table_start])
    roles = {}
    for index, header in enumerate(headers):
        name = normalized(header)
        if name == "id":
            roles["id"] = index
        elif "pointer" in name or "fact" in name and "field" in name:
            roles.setdefault("pointer", index)
        elif "excerpt" in name or name == "path":
            roles.setdefault("path", index)
        elif name in {"line", "lines", "line span", "span"}:
            roles.setdefault("span", index)
        elif "delivery mode" in name or name == "mode":
            roles.setdefault("mode", index)
        elif "anchor" in name:
            roles.setdefault("anchor", index)
    missing = {"id", "pointer", "path", "span", "mode", "anchor"} - set(roles)
    if missing:
        raise SystemExit(f"INPUT-ERROR: {map_path}: header roles missing {sorted(missing)}; headers={headers}")
    rows = []
    for index in range(table_start + 1, end):
        if not lines[index].lstrip().startswith("|"):
            break
        row = cells(lines[index])
        if is_separator(row):
            continue
        if len(row) != len(headers):
            raise SystemExit(
                f"INPUT-ERROR: {map_path}: line {index + 1}: {len(row)} cells vs {len(headers)} headers"
            )
        rows.append({
            "line": index + 1,
            "id": row[roles["id"]].strip().strip("`"),
            "pointer": row[roles["pointer"]].strip(),
            "path": row[roles["path"]].strip().strip("`"),
            "span": row[roles["span"]].strip().strip("`"),
            "mode": row[roles["mode"]].strip().strip("`"),
            "anchor": row[roles["anchor"]].strip().strip("`"),
        })
    if not rows:
        raise SystemExit(f"INPUT-ERROR: {map_path}: no fact rows")
    return rows


def parse_span(value):
    match = re.fullmatch(r"\s*(\d+)(?:\s*[-\u2013]\s*(\d+))?\s*", value)
    if match is None:
        return None
    first = int(match.group(1))
    last = int(match.group(2) or match.group(1))
    return (first, last)


def anchor_hits(anchor, excerpt_path):
    if "\n" in anchor:
        raise SystemExit(f"INPUT-ERROR: anchor contains a newline: {anchor!r}")
    hits = []
    for number, line in enumerate(excerpt_path.read_text(encoding="utf-8").splitlines(), 1):
        if anchor in line:
            hits.append(number)
    return hits


def verify_rows(rows, cluster, label):
    results = []
    failures = 0
    for row in rows:
        excerpt = cluster / row["path"]
        if not excerpt.is_file():
            results.append((row, None, None, f"excerpt-missing {excerpt}"))
            failures += 1
            continue
        span = parse_span(row["span"])
        if span is None:
            results.append((row, None, None, f"span-unparsable {row['span']!r}"))
            failures += 1
            continue
        hits = anchor_hits(row["anchor"], excerpt)
        outside = [number for number in hits if not (span[0] <= number <= span[1])]
        if not hits:
            note = "anchor-not-found"
            failures += 1
        elif outside:
            note = f"outside-span hits={','.join(map(str, outside))}"
            failures += 1
        else:
            note = "in-span"
        results.append((row, span, hits, note))
    print(f"== {label}: {len(rows)} rows, in-span "
          f"{sum(1 for _, _, _, note in results if note == 'in-span')}/{len(rows)} ==")
    for row, span, hits, note in results:
        print(
            f"ROW {row['id']:>4} line={row['line']:>3} path={row['path']:<24} "
            f"span={row['span']:<8} hits={','.join(map(str, hits)) or '-':<8} {note}"
        )
    return results, failures


def compare_baseline(new_results, baseline_map, baseline_cluster):
    baseline_rows = parse_facts_table(baseline_map)
    by_id = {row["id"]: row for row in baseline_rows}
    by_pointer = {row["pointer"]: row for row in baseline_rows}
    print(f"== preservation vs {baseline_map}: baseline rows={len(baseline_rows)} ==")
    matched = 0
    mismatches = 0
    unmatched_new = []
    used = set()
    for row, span, hits, note in new_results:
        base = by_id.get(row["id"]) or by_pointer.get(row["pointer"])
        if base is None:
            unmatched_new.append(row["id"])
            continue
        matched += 1
        used.add(base["id"])
        diffs = []
        for field in ("pointer", "path", "span", "mode", "anchor"):
            if row[field] != base[field]:
                diffs.append(f"{field}: {base[field]!r} -> {row[field]!r}")
        base_excerpt = baseline_cluster / base["path"]
        base_hits = anchor_hits(base["anchor"], base_excerpt) if base_excerpt.is_file() else None
        if base_hits != hits:
            diffs.append(f"line numbers: baseline hits={base_hits} new hits={hits}")
        if diffs:
            mismatches += 1
            print(f"PRESERVED-FAIL {row['id']}: " + "; ".join(diffs))
        else:
            print(f"PRESERVED-OK {row['id']} hits={','.join(map(str, hits))}")
    baseline_only = [row["id"] for row in baseline_rows if row["id"] not in used]
    if baseline_only:
        mismatches += len(baseline_only)
        print(f"PRESERVED-FAIL baseline rows missing from new map: {baseline_only}")
    if unmatched_new:
        print(f"NOTE new rows without baseline match: {unmatched_new}")
    print(f"== preservation: matched={matched} mismatches={mismatches} ==")
    return mismatches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", required=True, type=Path)
    parser.add_argument("--cluster", required=True, type=Path)
    parser.add_argument("--baseline-map", type=Path)
    parser.add_argument("--baseline-cluster", type=Path)
    parser.add_argument("--label", default="new")
    args = parser.parse_args()

    rows = parse_facts_table(args.map)
    results, failures = verify_rows(rows, args.cluster, args.label)
    if (args.baseline_map is None) != (args.baseline_cluster is None):
        raise SystemExit("INPUT-ERROR: --baseline-map and --baseline-cluster go together")
    if args.baseline_map is not None:
        failures += compare_baseline(results, args.baseline_map, args.baseline_cluster)
    print(f"VERDICT {'PASS' if failures == 0 else 'FAIL'} failures={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
