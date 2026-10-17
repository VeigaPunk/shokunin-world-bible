#!/usr/bin/env python3
"""Check fixed-string anchors and R9 delivery modes in a cluster map."""

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

MODES = {"verbatim", "translation", "paraphrase", "summary"}
RETELLING_MODES = {"paraphrase", "summary"}
MODE_DECLARATION = re.compile(
    r"^\s*(?:\*\*)?Delivery\s+mode(?:\s*\(R9\))?(?:\*\*)?\s*:\s*(?:\*\*)?\s*`?"
    r"(verbatim|translation|paraphrase|summary)\b",
    re.IGNORECASE,
)
LOCATOR_SUFFIX = re.compile(
    r"^(.*?):\s*(?:lines?\s*)?(\d+)(?:\s*[-–]\s*(\d+))?$",
    re.IGNORECASE,
)
EXPECTED_INVENTORY = re.compile(
    r"^\*\*Expected inventory:\*\*\s*(\d+) JSON fact(?:s)?;\s*"
    r"(\d+) editorial row(?:s)?;\s*(\d+) total mapped row(?:s)?;\s*"
    r"(\d+) distinct excerpt anchor(?:s)?\.\s*$",
    re.IGNORECASE,
)


class InventoryError(ValueError):
    pass


def cells(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def normalized_header(value):
    value = value.strip().strip("`").lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def header_roles(headers):
    roles = {}
    for index, header in enumerate(headers):
        name = normalized_header(header)
        if name in {"fact", "fact id", "fact identifier", "id", "claim pointer", "claim id"}:
            roles.setdefault("id", index)
        elif "delivery mode" in name or name.endswith(" mode") or name in {"mode", "mode author"}:
            roles.setdefault("mode", index)
        elif "anchor" in name:
            roles.setdefault("anchor", index)
        elif "excerpt" in name and ("path" in name or name == "excerpt"):
            roles.setdefault("path", index)
        elif name in {"line", "lines", "line span", "excerpt lines", "line numbers"}:
            roles.setdefault("span", index)
    return roles


def locator_path(value):
    value = value.strip().strip("`")
    match = LOCATOR_SUFFIX.match(value)
    return match.group(1).strip() if match else value


def parse_mode(value):
    match = re.match(r"^\s*(verbatim|translation|paraphrase|summary)\b", value, re.IGNORECASE)
    return match.group(1).lower() if match else None


def parse_map(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    facts = []
    excerpt_modes = {}
    expected_inventory = None
    current_section = None
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("## "):
            heading = normalized_header(line[3:])
            if re.match(r"json facts(?:$| )", heading):
                current_section = "json"
            elif re.match(r"editorial rows(?:$| )", heading):
                current_section = "editorial"
            else:
                current_section = None
        inventory_match = EXPECTED_INVENTORY.fullmatch(line)
        if line.lstrip().startswith("**Expected inventory:**") and not inventory_match:
            raise InventoryError("expected inventory declaration is malformed")
        if inventory_match:
            if expected_inventory is not None:
                raise InventoryError("map must contain exactly one expected inventory declaration")
            expected_inventory = tuple(int(value) for value in inventory_match.groups())
        if not line.lstrip().startswith("|"):
            index += 1
            continue
        headers = cells(line)
        roles = header_roles(headers)
        if not {"mode", "path"}.issubset(roles):
            index += 1
            continue
        is_fact_table = {"id", "anchor"}.issubset(roles)
        row_index = index + 1
        while row_index < len(lines) and lines[row_index].lstrip().startswith("|"):
            row = cells(lines[row_index])
            if row and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in row):
                row_index += 1
                continue
            if len(row) != len(headers):
                raise ValueError("map table row has a different number of cells than its header")
            mode = row[roles["mode"]].strip().strip("`")
            excerpt_path = locator_path(row[roles["path"]])
            declared = parse_mode(mode)
            if not is_fact_table:
                previous = excerpt_modes.get(excerpt_path, declared)
                excerpt_modes[excerpt_path] = declared if previous == declared else None
            if is_fact_table:
                if current_section is None:
                    raise ValueError("fact table must be under a JSON facts or Editorial rows heading")
                fact_id = row[roles["id"]].strip().strip("`")
                anchor = row[roles["anchor"]].strip().strip("`")
                locator = row[roles["path"]].strip().strip("`")
                span = row[roles["span"]].strip().strip("`") if "span" in roles else ""
                if not span:
                    match = LOCATOR_SUFFIX.match(locator)
                    if match:
                        locator, first, last = match.groups()
                        span = first if last is None else f"{first}-{last}"
                if not fact_id or not excerpt_path or not anchor:
                    raise ValueError("map rows require a fact id, excerpt path, and non-empty anchor")
                facts.append({"id": fact_id, "kind": current_section, "mode": mode, "anchor": anchor, "path": excerpt_path, "span": span})
            row_index += 1
        index = row_index
    if expected_inventory is None:
        raise InventoryError("map must contain exactly one expected inventory declaration")
    if expected_inventory[2] != expected_inventory[0] + expected_inventory[1]:
        raise InventoryError("expected JSON facts and editorial rows must sum to total mapped rows")
    return facts, excerpt_modes, expected_inventory


def find_repo_root(cluster):
    for ancestor in (cluster, *cluster.parents):
        if (ancestor / "corpus").is_dir():
            return ancestor
    return None


def resolve_excerpt(cluster, raw_path):
    cluster = cluster.resolve()
    path = Path(raw_path)
    if path.is_absolute():
        candidates = [path]
    else:
        candidates = [cluster / path]
        if path.parts and path.parts[0] == cluster.name:
            candidates.append(cluster.joinpath(*path.parts[1:]))
        root = find_repo_root(cluster)
        if root is not None:
            candidates.extend([root / path, root / "corpus" / path])
    for candidate in candidates:
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(cluster)
        except (OSError, ValueError):
            continue
        if resolved.is_file():
            return resolved
    return None


def excerpt_modes(path):
    declarations = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MODE_DECLARATION.match(line)
        if match:
            declarations.append(match.group(1).lower())
    return declarations


def parse_line_span(value):
    match = re.fullmatch(r"\s*(\d+)(?:\s*[-–]\s*(\d+))?\s*", value)
    if match is None:
        return None
    first = int(match.group(1))
    last = int(match.group(2) or first)
    if first < 1 or last < first:
        return None
    return first, last


def grep_anchor(anchor, excerpt):
    try:
        result = subprocess.run(
            ["grep", "-nF", "--", anchor, str(excerpt)],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as error:
        return [], str(error)
    if result.returncode == 0:
        hits = []
        for line in result.stdout.splitlines():
            line_number, separator, _ = line.partition(":")
            if not separator or not line_number.isdecimal():
                return [], f"could not parse grep hit line: {line!r}"
            hits.append((int(line_number), line))
        return hits, ""
    if result.returncode == 1:
        return [], ""
    return [], result.stderr.strip() or f"grep exited {result.returncode}"


def run(cluster, map_path):
    facts, map_excerpt_modes, expected_inventory = parse_map(map_path)
    expected_json, expected_editorial, expected_total, expected_distinct = expected_inventory
    json_facts = [fact for fact in facts if fact["kind"] == "json"]
    editorial_rows = [fact for fact in facts if fact["kind"] == "editorial"]
    anchor_counts = Counter((fact["path"], fact["anchor"]) for fact in facts)
    duplicate_rows = Counter(
        (fact["kind"], fact["id"], fact["path"], fact["span"], fact["mode"], fact["anchor"])
        for fact in facts
    )
    duplicate_row_count = sum(count - 1 for count in duplicate_rows.values())
    repeated_anchor_refs = sum(count - 1 for count in anchor_counts.values())
    source_total = 0
    source_hits = 0
    editorial_total = 0
    editorial_hits = 0
    retelling_total = 0
    retelling_hits = 0
    declared_modes = 0
    validated_rows = 0
    failures = []
    warnings = []

    observed_inventory = (
        len(json_facts), len(editorial_rows), len(facts), len(anchor_counts)
    )
    labels = ("JSON facts", "editorial rows", "total mapped rows", "distinct excerpt anchors")
    for label, observed, expected in zip(labels, observed_inventory, expected_inventory):
        if observed != expected:
            failures.append(f"inventory {label} mismatch: expected={expected} parsed={observed}")
    print(
        f"INVENTORY JSON-FACTS {len(json_facts)}/{expected_json}; "
        f"EDITORIAL-ROWS {len(editorial_rows)}/{expected_editorial}; "
        f"TOTAL-ROWS {len(facts)}/{expected_total}; "
        f"DISTINCT-ANCHORS {len(anchor_counts)}/{expected_distinct}"
    )
    print(f"ANCHORS repeated-references={repeated_anchor_refs}; DUPLICATE-ROWS {duplicate_row_count}")
    for row, count in duplicate_rows.items():
        if count > 1:
            failures.append(f"duplicate mapped row {row[1]} appears {count} times")

    referenced_paths = {locator_path(fact["path"]) for fact in facts}
    for path, mode in sorted(map_excerpt_modes.items()):
        if path not in referenced_paths:
            warnings.append(
                f"unreferenced excerpt declaration: {path} (mode={mode or 'undeclared'})"
            )

    for fact in facts:
        map_mode_value = parse_mode(fact["mode"])
        excerpt = resolve_excerpt(cluster, fact["path"])
        path_key = locator_path(fact["path"])
        inline_modes = excerpt_modes(excerpt) if excerpt is not None else []
        excerpt_declared_mode = map_excerpt_modes.get(path_key)
        if inline_modes:
            actual_mode = inline_modes[0] if len(inline_modes) == 1 else None
            mode_ok = (
                map_mode_value is not None
                and len(inline_modes) == 1
                and actual_mode == map_mode_value
                and (path_key not in map_excerpt_modes or excerpt_declared_mode == map_mode_value)
            )
        else:
            actual_mode = excerpt_declared_mode
            mode_ok = map_mode_value is not None and actual_mode == map_mode_value
        if mode_ok:
            declared_modes += 1

        line_span = parse_line_span(fact["span"])
        hits = []
        grep_error = ""
        if excerpt is not None and fact["anchor"]:
            hits, grep_error = grep_anchor(fact["anchor"], excerpt)
        anchor_found = bool(hits)
        anchor_output = "; ".join(output for _, output in hits)
        outside_hits = [
            number for number, _ in hits
            if line_span is None or not line_span[0] <= number <= line_span[1]
        ]
        span_ok = line_span is not None and not outside_hits
        is_retelling = map_mode_value in RETELLING_MODES
        row_valid = mode_ok and span_ok and anchor_found
        if row_valid:
            validated_rows += 1

        if is_retelling:
            retelling_total += 1
            if anchor_found:
                retelling_hits += 1
            else:
                warnings.append(
                    f"retelling anchor not found for {fact['id']}; excluded from source support"
                )
            detail = "retelling-support-only"
            detail += "; anchor=" + ("found" if anchor_found else "not-found")
            detail += f"; mode={map_mode_value or 'undeclared'}"
            if actual_mode is None:
                detail += "; excerpt-mode=undeclared"
            elif actual_mode != map_mode_value:
                detail += f"; excerpt-mode={actual_mode}"
            if anchor_output:
                detail += f"; {anchor_output}"
        else:
            if fact["kind"] == "json":
                source_total += 1
                if row_valid:
                    source_hits += 1
                detail = f"source-support; mode={map_mode_value or 'undeclared'}"
            else:
                editorial_total += 1
                if row_valid:
                    editorial_hits += 1
                detail = f"editorial-row; mode={map_mode_value or 'undeclared'}"
            if actual_mode is None:
                detail += "; excerpt-mode=undeclared"
            elif actual_mode != map_mode_value:
                detail += f"; excerpt-mode={actual_mode}"
            detail += "; anchor=" + ("found" if anchor_found else "not-found")
            if anchor_output:
                detail += f"; {anchor_output}"

        if line_span is None:
            detail += f"; span={fact['span'] or 'undeclared'}"
        elif outside_hits:
            detail += f"; span={fact['span']}; outside-span={','.join(map(str, outside_hits))}"

        if line_span is None:
            failures.append(fact["id"] + ": missing or invalid declared line span")
        elif outside_hits:
            failures.append(
                f"{fact['id']}: anchor hit outside declared line span "
                f"{fact['span']} (hit lines: {', '.join(map(str, outside_hits))})"
            )
        if not mode_ok:
            failures.append(fact["id"] + ": delivery mode missing or mismatched")
        if not is_retelling and not anchor_found:
            failures.append(fact["id"] + ": source-support anchor missing")
        if excerpt is None:
            failures.append(fact["id"] + ": excerpt path missing or outside cluster")
        if grep_error:
            failures.append(fact["id"] + ": " + grep_error)
        row_status = "WARN" if is_retelling and not anchor_found else "PASS" if row_valid else "FAIL"
        print(f"{row_status} {fact['id']}: {detail}")

    print(
        f"RECEIPT JSON-FACTS {len(json_facts)}; EDITORIAL-ROWS {len(editorial_rows)}; "
        f"TOTAL-ROWS {len(facts)}"
    )
    print(
        f"SOURCE-SUPPORT {source_hits}/{source_total}; EDITORIAL-ANCHORS {editorial_hits}/{editorial_total}; "
        f"RETELLING-SUPPORT-ONLY {retelling_total} entries "
        f"({retelling_hits}/{retelling_total} anchors); MODES {declared_modes}/{len(facts)}; "
        f"VALIDATED-ROWS {validated_rows}/{len(facts)}"
    )
    for warning in warnings:
        print(f"WARN: {warning}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("RESULT FAIL")
        return 1
    print("RESULT PASS WITH WARNINGS" if warnings else "RESULT PASS")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Check fixed-string anchors and R9 modes in a cluster map")
    parser.add_argument("cluster", type=Path, help="cluster directory containing the claim-to-excerpt map")
    parser.add_argument("--map", type=Path, help="map path; defaults to a conventional map in the cluster")
    try:
        args = parser.parse_args()
    except SystemExit as error:
        exit_code = error.code if isinstance(error.code, int) else 1 if error.code else 0
        if exit_code:
            print("RESULT ERROR")
        return exit_code

    try:
        cluster = args.cluster.resolve()
        if not cluster.is_dir():
            print(f"FAIL: cluster directory not found: {args.cluster}", file=sys.stderr)
            print("RESULT ERROR")
            return 2
        map_path = args.map
        if map_path is None:
            candidates = [cluster / "claim-to-excerpt-map.md", cluster / "claim-excerpt-map.md"]
            map_path = next((candidate for candidate in candidates if candidate.is_file()), None)
        elif not map_path.is_absolute():
            map_path = Path.cwd() / map_path
        if map_path is None or not map_path.is_file():
            print("FAIL: claim-to-excerpt map not found", file=sys.stderr)
            print("RESULT ERROR")
            return 2
        return run(cluster, map_path)
    except InventoryError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        print("RESULT FAIL")
        return 1
    except (OSError, UnicodeError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        print("RESULT ERROR")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
