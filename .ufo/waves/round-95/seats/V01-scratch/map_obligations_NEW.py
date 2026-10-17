#!/usr/bin/env python3
"""Compare raw source-attributed JSON obligations with a canonical map."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

RAW_FILES = ("entities.json", "relations.json", "timeline.json")
MAP_CANDIDATES = ("claim-to-excerpt-map.md", "claim-excerpt-map.md")
FROZEN_MAP = "claim-excerpt-map.md"
FROZEN_INPUTS = (*RAW_FILES, FROZEN_MAP)
POINTER_COLUMN_ROLES = ("json fact pointer", "json fact pointer and fields", "json fact and fields")
LEGACY_POINTER_COLUMN = "json fact and fields"
LEGACY_POINTER = re.compile(
    r"^(entities|relations|timeline)\[([0-9]+)\]"
    r"(?:\.first_appearance|\.claims\[([0-9]+)\])?$"
)
LEGACY_CELL = re.compile(r"\s*`([^`]+)`(?:\s*\([^()]*\))?(?:\s*:\s*.*)?\s*")
EXPECTED_INVENTORY = re.compile(
    r"^\*\*Expected inventory:\*\*\s*([0-9]+)\s+JSON facts?;\s*([0-9]+)\s+editorial rows?;\s*"
    r"([0-9]+)\s+total mapped rows?;\s*([0-9]+)\s+distinct excerpt anchors?\.\s*$",
    re.IGNORECASE,
)
SELF_TEST_CASES = (
    "complete",
    "missing",
    "duplicate",
    "phantom",
    "source_id_mismatch",
    "malformed_json",
    "map_missing",
    "co_mapped_grammar",
    "legacy_grammar",
    "invalid_pointer",
    "empty_segment",
    "noncanonical_index",
    "noncanonical_claim_index",
    "foreign_path",
    "traversal_path",
    "symlink_path",
    "invalid_arguments",
    "frozen_complete",
    "frozen_tampered",
    "frozen_missing_digests",
    "frozen_expected_failure",
    "frozen_verdict_mismatch",
)
RESULTS = {0: "PASS", 1: "FAIL", 2: "ERROR"}
ROOT = Path(__file__).resolve().parents[2]
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ARRAY_INDEX = re.compile(r"^(?:0|[1-9][0-9]*)$")


class ToolError(Exception):
    def __init__(self, finding_id, detail):
        super().__init__(detail)
        self.finding_id = finding_id
        self.detail = detail


class CliParser(argparse.ArgumentParser):
    def error(self, message):
        raise ToolError("invalid_arguments", message)


def fail(finding_id, detail):
    raise ToolError(finding_id, detail)


def emit(code, findings=()):
    for finding_id, detail in sorted(findings):
        print(f"FINDING {finding_id}: {detail}")
    print(f"RESULT {RESULTS[code]}")
    return code


def path_has_symlink(path):
    path = Path(os.path.abspath(path))
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current = current / part
        if current.is_symlink():
            return True
    return False


def resolve_cluster(value):
    candidate = Path(value).expanduser()
    if not candidate.is_absolute():
        candidate = Path.cwd() / candidate
    candidate = Path(os.path.abspath(candidate))
    if path_has_symlink(candidate):
        fail("unsafe_path", "cluster path contains a symlink")
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as error:
        fail("cluster_missing", f"cannot resolve cluster: {error}")
    if not resolved.is_dir():
        fail("cluster_missing", "cluster is not a directory")
    return resolved


def resolve_map(cluster, value):
    if value is None:
        candidates = [cluster / name for name in MAP_CANDIDATES if (cluster / name).exists()]
        if len(candidates) != 1:
            fail("map_missing" if not candidates else "unsupported_map",
                 "expected exactly one conventional claim-to-excerpt map")
        candidate = candidates[0]
    else:
        candidate = Path(value).expanduser()
        if not candidate.is_absolute():
            if ".." in candidate.parts:
                fail("unsafe_path", "map path contains traversal")
            candidate = cluster / candidate
    candidate = Path(os.path.abspath(candidate))
    if path_has_symlink(candidate):
        fail("unsafe_path", "map path contains a symlink")
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as error:
        fail("map_missing", f"cannot resolve map: {error}")
    try:
        resolved.relative_to(cluster)
    except ValueError:
        fail("foreign_path", "map path is outside the cluster")
    if not resolved.is_file():
        fail("map_missing", "map path is not a file")
    return resolved


def markdown_cells(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def normalized_header(value):
    value = value.strip().strip("`").casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def is_separator(row):
    return bool(row) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in row
    )


def legacy_pointer(token):
    """Translate one legacy field-path token (entities[0].first_appearance) into a canonical pointer."""
    match = LEGACY_POINTER.fullmatch(token)
    if match is None:
        return None
    filename, record_index, claim_index = match.groups()
    if not ARRAY_INDEX.fullmatch(record_index):
        return None
    if token != f"{filename}[{record_index}]":
        if filename != "entities":
            return None
        if token.endswith(".first_appearance"):
            return f"entities.json#/{record_index}/first_appearance"
        if claim_index is None or not ARRAY_INDEX.fullmatch(claim_index):
            return None
        return f"entities.json#/{record_index}/claims/{claim_index}"
    return None if filename == "entities" else f"{filename}.json#/{record_index}"


def parse_pointer_cell(cell, legacy=False):
    if legacy:
        legacy_match = LEGACY_CELL.fullmatch(cell)
        if legacy_match is not None:
            translated = legacy_pointer(legacy_match.group(1))
            if translated is not None:
                return translated
    match = re.fullmatch(r"\s*`([^`]+)`(?:\s+\((.*)\))?\s*", cell)
    if match is None:
        fail("unsupported_map", "pointer cells must contain one canonical inline-code pointer")
    token, note = match.groups()
    if len(re.findall(r"[A-Za-z0-9_.-]+\.json#", token)) != 1:
        fail("unsupported_map", "co-mapped or unsupported pointer grammar")
    if note and re.search(r"[A-Za-z0-9_.-]+\.json#", note):
        fail("unsupported_map", "co-mapped or unsupported pointer grammar")
    if token.count("#") != 1:
        fail("invalid_pointer", "pointer must have one file.json#/pointer separator")
    filename, pointer = token.split("#", 1)
    if (not filename or filename.startswith("/") or "/" in filename
            or "\\" in filename or filename in {".", ".."}):
        fail("unsafe_path", "pointer file path must be a cluster-local JSON filename")
    if filename not in RAW_FILES:
        fail("foreign_path", f"pointer names unsupported input file {filename!r}")
    if not pointer.startswith("/"):
        fail("invalid_pointer", "pointer is not a canonical JSON Pointer")
    segments = pointer[1:].split("/")
    if (not segments or any(not segment for segment in segments)
            or any(re.search(r"~(?![01])", segment) for segment in segments)):
        fail("invalid_pointer", "pointer contains an empty or invalid escape segment")
    if not ARRAY_INDEX.fullmatch(segments[0]):
        fail("invalid_pointer", "top-level array index must be canonical decimal")
    if any(re.fullmatch(r"[0-9]+", segment) and not ARRAY_INDEX.fullmatch(segment)
           for segment in segments):
        fail("invalid_pointer", "array indices must not contain leading zeroes")
    decoded = [segment.replace("~1", "/").replace("~0", "~") for segment in segments]
    if (filename == "entities.json" and len(decoded) > 1 and decoded[1] == "claims"
            and len(segments) > 2 and not ARRAY_INDEX.fullmatch(segments[2])):
        fail("invalid_pointer", "entity claim index must be canonical decimal")
    return token


def parse_source_id(value):
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", value):
        fail("unsupported_map", "source-ID cells must contain one unadorned source ID")
    return value


def declared_inventory(lines):
    """Return the map's declared (facts, editorial, total, anchors) inventory and a malformed flag."""
    declared = None
    malformed = False
    for line in lines:
        if not line.lstrip().startswith("**Expected inventory:**"):
            continue
        match = EXPECTED_INVENTORY.fullmatch(line.strip())
        if match is None:
            malformed = True
        elif declared is None:
            declared = tuple(int(value) for value in match.groups())
    return declared, malformed


def editorial_row_count(lines):
    heading = next((index for index, line in enumerate(lines)
                    if re.match(r"^##\s+Editorial rows(?:\s|$|\()", line, re.IGNORECASE)), None)
    if heading is None:
        return 0
    end = next((index for index in range(heading + 1, len(lines))
                if re.match(r"^#{1,6}\s+", lines[index])), len(lines))
    table_start = next((index for index in range(heading + 1, end)
                        if lines[index].lstrip().startswith("|")), None)
    if table_start is None:
        return 0
    count = 0
    index = table_start + 1
    while index < end and lines[index].lstrip().startswith("|"):
        if not is_separator(markdown_cells(lines[index])):
            count += 1
        index += 1
    return count


def print_inventory_receipt(declared, malformed, parsed_facts, parsed_editorial):
    if declared is None and not malformed:
        return
    if declared is None:
        print("INVENTORY declaration-malformed")
        return
    facts, editorial, total, _anchors = declared
    observed = (parsed_facts, parsed_editorial, parsed_facts + parsed_editorial)
    status = "" if observed == (facts, editorial, total) else " MISMATCH"
    print(
        f"INVENTORY JSON-FACTS {parsed_facts}/{facts}; EDITORIAL-ROWS {parsed_editorial}/{editorial}; "
        f"TOTAL-ROWS {parsed_facts + parsed_editorial}/{total}{status}"
    )


def parse_map_text(text):
    lines = text.splitlines()
    headings = [
        index for index, line in enumerate(lines)
        if re.match(r"^##\s+JSON facts(?:\s|$|\()", line, re.IGNORECASE)
    ]
    if len(headings) != 1:
        fail("unsupported_map", "map must contain exactly one JSON facts section")
    start = headings[0] + 1
    end = next((index for index in range(start, len(lines))
                if re.match(r"^#{1,6}\s+", lines[index])), len(lines))
    table_start = next((index for index in range(start, end)
                        if lines[index].lstrip().startswith("|")), None)
    if table_start is None:
        fail("unsupported_map", "JSON facts section has no supported table")
    headers = markdown_cells(lines[table_start])
    pointer_columns = []
    pointer_roles = []
    source_columns = []
    for index, header in enumerate(headers):
        role = normalized_header(header)
        if role in POINTER_COLUMN_ROLES:
            pointer_columns.append(index)
            pointer_roles.append(role)
        if role in {"in world source id", "source id"}:
            source_columns.append(index)
    if len(pointer_columns) != 1 or len(source_columns) != 1:
        fail("unsupported_map", "table needs one JSON fact pointer and one source-ID column")
    legacy = pointer_roles[0] == LEGACY_POINTER_COLUMN
    rows = []
    index = table_start + 1
    while index < end and lines[index].lstrip().startswith("|"):
        row = markdown_cells(lines[index])
        if not is_separator(row):
            if len(row) != len(headers):
                fail("unsupported_map", "map row cell count differs from its header")
            rows.append((
                parse_pointer_cell(row[pointer_columns[0]], legacy),
                parse_source_id(row[source_columns[0]]),
            ))
        index += 1
    if any(lines[line].lstrip().startswith("|") for line in range(index, end)):
        fail("unsupported_map", "JSON facts section has multiple or non-contiguous tables")
    if not rows:
        fail("unsupported_map", "JSON facts table has no obligation rows")
    declared, malformed = declared_inventory(lines)
    return rows, declared, malformed, editorial_row_count(lines)


def parse_map(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        fail("map_unreadable", f"cannot read UTF-8 map: {error}")
    return parse_map_text(text)


def read_raw(cluster, filename):
    path = cluster / filename
    if path.is_symlink():
        fail("unsafe_path", f"raw input is a symlink: {filename}")
    try:
        resolved = path.resolve(strict=True)
    except OSError as error:
        fail("raw_input_missing", f"cannot resolve {filename}: {error}")
    try:
        resolved.relative_to(cluster)
    except ValueError:
        fail("unsafe_path", f"raw input escapes cluster: {filename}")
    if not resolved.is_file():
        fail("raw_input_missing", f"raw input is not a file: {filename}")
    try:
        text = resolved.read_text(encoding="utf-8")
        return json.loads(text)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail("malformed_json", f"cannot parse {filename}: {error}")


def source_value(value, context):
    if not isinstance(value, str) or not value or value != value.strip():
        fail("invalid_raw_data", f"{context} must contain a non-empty source ID")
    return value


def claim_shaped(record):
    return (
        isinstance(record, dict)
        and isinstance(record.get("statement"), str) and record["statement"] != ""
        and isinstance(record.get("source_id"), str) and record["source_id"] != ""
    )


def raw_obligations_values(entities, relations, timeline):
    if not isinstance(entities, list) or not isinstance(relations, list) or not isinstance(timeline, list):
        fail("invalid_raw_data", "entities, relations, and timeline roots must be arrays")
    obligations = {}
    findings = []

    def add(pointer, source_id):
        if pointer in obligations:
            fail("invalid_raw_data", f"raw obligation repeated at {pointer}")
        obligations[pointer] = source_id

    for entity_index, entity in enumerate(entities):
        if not isinstance(entity, dict):
            fail("invalid_raw_data", f"entities/{entity_index} must be an object")
        prefix = f"entities.json#/{entity_index}"
        for key, value in entity.items():
            if key == "claims" or not isinstance(value, list) or not value:
                continue
            shaped = sum(1 for record in value if claim_shaped(record))
            if shaped:
                findings.append((
                    "schema_drift",
                    f"{prefix}: {shaped} sourced-claim-shaped record(s) under unexpected key {key!r}",
                ))
        add(prefix + "/first_appearance",
            source_value(entity.get("first_appearance"), prefix + "/first_appearance"))
        claims = entity.get("claims", [])
        if not isinstance(claims, list):
            fail("invalid_raw_data", f"{prefix}/claims must be an array")
        for claim_index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                fail("invalid_raw_data", f"{prefix}/claims/{claim_index} must be an object")
            pointer = f"{prefix}/claims/{claim_index}"
            add(pointer, source_value(claim.get("source_id"), pointer + "/source_id"))
    for filename, records in (("relations.json", relations), ("timeline.json", timeline)):
        for record_index, record in enumerate(records):
            if not isinstance(record, dict):
                fail("invalid_raw_data", f"{filename}/{record_index} must be an object")
            pointer = f"{filename}#/{record_index}"
            add(pointer, source_value(record.get("source_id"), pointer + "/source_id"))
    return obligations, findings


def raw_obligations(cluster):
    return raw_obligations_values(
        read_raw(cluster, "entities.json"),
        read_raw(cluster, "relations.json"),
        read_raw(cluster, "timeline.json"),
    )


def compare(obligations, rows):
    findings = []
    counts = Counter(pointer for pointer, _ in rows)
    by_pointer = {}
    for pointer, source_id in rows:
        by_pointer.setdefault(pointer, []).append(source_id)
    for pointer, count in sorted(counts.items()):
        if count > 1:
            findings.append(("duplicate_mapping", f"{pointer} appears {count} times"))
        if pointer not in obligations:
            findings.append(("phantom_obligation", f"{pointer} is not a raw source-attributed obligation"))
        elif any(source_id != obligations[pointer] for source_id in by_pointer[pointer]):
            findings.append(("source_id_mismatch", f"{pointer} does not bind to {obligations[pointer]!r}"))
    for pointer in sorted(obligations):
        if pointer not in counts:
            findings.append(("missing_obligation", f"{pointer} has no map row"))
    return findings


def run_cluster(cluster_value, map_value=None):
    cluster = resolve_cluster(cluster_value)
    map_path = resolve_map(cluster, map_value)
    rows, declared, malformed, editorial_rows = parse_map(map_path)
    obligations, drift_findings = raw_obligations(cluster)
    findings = [*drift_findings, *compare(obligations, rows)]
    print(f"OBLIGATIONS raw={len(obligations)} mapped={len(rows)}")
    print_inventory_receipt(declared, malformed, len(rows), editorial_rows)
    return emit(1 if findings else 0, findings)


def resolve_frozen(value):
    candidate = Path(value).expanduser()
    if ".." in candidate.parts:
        fail("unsafe_path", "frozen snapshot path contains traversal")
    if not candidate.is_absolute():
        candidate = Path.cwd() / candidate
    candidate = Path(os.path.abspath(candidate))
    if path_has_symlink(candidate):
        fail("snapshot_tampered", "frozen snapshot path contains a symlink")
    try:
        resolved = candidate.resolve(strict=True)
    except OSError:
        fail("snapshot_tampered", "frozen snapshot directory is missing or unreadable")
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        fail("unsafe_path", "frozen snapshot must be inside the owning repository")
    if not resolved.is_dir():
        fail("snapshot_tampered", "frozen snapshot path is not a directory")
    return resolved


def load_frozen_expected(snapshot):
    path = snapshot / "expected.json"
    if path.is_symlink():
        fail("unpinned", "expected.json must be a regular snapshot file")
    try:
        expected = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail("unpinned", f"cannot load frozen expectations: {error}")
    if not isinstance(expected, dict) or expected.get("schema_version") != 1:
        fail("unpinned", "expected.json has an unsupported schema")
    inputs = expected.get("inputs")
    if not isinstance(inputs, dict) or set(inputs) != set(FROZEN_INPUTS):
        fail("unpinned", "expected.json must pin every frozen input exactly once")
    if any(not isinstance(inputs[name], str) or SHA256.fullmatch(inputs[name]) is None
           for name in FROZEN_INPUTS):
        fail("unpinned", "expected.json contains a missing or invalid input digest")
    verdict = expected.get("expected")
    if not isinstance(verdict, dict):
        fail("unpinned", "expected.json has no expected verdict")
    code = verdict.get("exit_code")
    ids = verdict.get("finding_ids")
    if (type(code) is not int or code not in (0, 1)
            or verdict.get("result") != RESULTS[code]
            or not isinstance(ids, list)
            or any(not isinstance(value, str) for value in ids)):
        fail("unpinned", "expected verdict must pin exit 0/PASS or 1/FAIL and finding IDs")
    return inputs, code, sorted(ids)


def verify_frozen_inputs(snapshot, expected_digests):
    contents = {}
    problems = []
    for name in FROZEN_INPUTS:
        path = snapshot / name
        if path.is_symlink() or not path.is_file():
            problems.append(name)
            continue
        try:
            data = path.read_bytes()
        except OSError:
            problems.append(name)
            continue
        contents[name] = data
        if hashlib.sha256(data).hexdigest() != expected_digests[name]:
            problems.append(name)
    if problems:
        fail("snapshot_tampered", "missing, unsafe, or digest-mismatched inputs: " + ", ".join(problems))
    return contents


def parse_frozen_json(contents, filename):
    try:
        return json.loads(contents[filename].decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as error:
        fail("malformed_json", f"cannot parse frozen {filename}: {error}")


def run_frozen(value):
    snapshot = resolve_frozen(value)
    input_digests, expected_code, expected_ids = load_frozen_expected(snapshot)
    contents = verify_frozen_inputs(snapshot, input_digests)
    print(f"SNAPSHOT inputs={len(FROZEN_INPUTS)} digests=verified")
    try:
        map_text = contents[FROZEN_MAP].decode("utf-8")
        rows, declared, malformed, editorial_rows = parse_map_text(map_text)
        obligations, drift_findings = raw_obligations_values(
            parse_frozen_json(contents, "entities.json"),
            parse_frozen_json(contents, "relations.json"),
            parse_frozen_json(contents, "timeline.json"),
        )
        findings = [*drift_findings, *compare(obligations, rows)]
        code = 1 if findings else 0
    except UnicodeError as error:
        findings = [("map_unreadable", f"frozen map is not UTF-8: {error}")]
        code = 2
    except ToolError as error:
        findings = [(error.finding_id, error.detail)]
        code = 2
    actual_ids = sorted(finding_id for finding_id, _ in findings)
    if code != expected_code or actual_ids != expected_ids:
        mismatch = ("frozen_verdict_mismatch",
                    f"expected {RESULTS[expected_code]}/{expected_code} {expected_ids}; "
                    f"observed {RESULTS[code]}/{code} {actual_ids}")
        if code == 2:
            return emit(2, [*findings, mismatch])
        return emit(2, [mismatch])
    if code != 2:
        print(f"OBLIGATIONS raw={len(obligations)} mapped={len(rows)}")
        print_inventory_receipt(declared, malformed, len(rows), editorial_rows)
    print(f"FROZEN expected={RESULTS[expected_code]}/{expected_code} findings={expected_ids or 'none'} matched")
    return emit(code, findings)


def test_rows():
    return [
        ("E1", "entities.json#/0/first_appearance", "fixture-source"),
        ("E2", "entities.json#/0/claims/0", "fixture-source"),
        ("R1", "relations.json#/0", "fixture-source"),
        ("T1", "timeline.json#/0", "fixture-source"),
    ]


def write_test_fixture(cluster, rows, pointer_overrides=None):
    cluster.mkdir(parents=True, exist_ok=True)
    files = {
        "entities.json": [{
            "id": "test-entity",
            "first_appearance": "fixture-source",
            "claims": [{"statement": "test claim", "source_id": "fixture-source"}],
        }],
        "relations.json": [{
            "from": "test-entity", "to": "other", "type": "linked", "source_id": "fixture-source",
        }],
        "timeline.json": [{"id": "test-event", "source_id": "fixture-source"}],
    }
    for filename, value in files.items():
        (cluster / filename).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    pointer_overrides = pointer_overrides or {}
    map_lines = [
        "# Isolated mapping fixture",
        "",
        "## JSON facts",
        "",
        "| ID | JSON fact pointer and fields | In-world source ID |",
        "|---|---|---|",
    ]
    for row_index, (row_id, pointer, source_id) in enumerate(rows):
        pointer_cell = pointer_overrides.get(row_index, f"`{pointer}`")
        map_lines.append(f"| {row_id} | {pointer_cell} | `{source_id}` |")
    (cluster / "claim-excerpt-map.md").write_text("\n".join(map_lines) + "\n", encoding="utf-8")


def prepare_test_frozen(case_name, snapshot):
    rows = test_rows()
    expected_code = 0
    expected_ids = []
    if case_name in {"frozen_expected_failure", "frozen_verdict_mismatch"}:
        rows = rows[:-1]
    if case_name == "frozen_expected_failure":
        expected_code = 1
        expected_ids = ["missing_obligation"]
    write_test_fixture(snapshot, rows)
    inputs = {
        name: hashlib.sha256((snapshot / name).read_bytes()).hexdigest()
        for name in FROZEN_INPUTS
    }
    if case_name == "frozen_missing_digests":
        inputs.pop(FROZEN_MAP)
    expected = {
        "schema_version": 1,
        "inputs": inputs,
        "expected": {
            "exit_code": expected_code,
            "result": RESULTS[expected_code],
            "finding_ids": expected_ids,
        },
    }
    (snapshot / "expected.json").write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")
    if case_name == "frozen_tampered":
        path = snapshot / "entities.json"
        path.write_bytes(path.read_bytes() + b"\n")


def prepare_test_case(case_name, cluster):
    if case_name.startswith("frozen_"):
        prepare_test_frozen(case_name, cluster)
        return
    rows = test_rows()
    pointer_overrides = {}
    write_test_fixture(cluster, rows)
    if case_name == "complete":
        return
    if case_name == "missing":
        rows = rows[:-1]
    elif case_name == "duplicate":
        rows.append(rows[0])
    elif case_name == "phantom":
        rows.append(("X1", "entities.json#/0/name", "fixture-source"))
    elif case_name == "source_id_mismatch":
        rows[0] = (rows[0][0], rows[0][1], "wrong-source")
    elif case_name == "malformed_json":
        (cluster / "entities.json").write_text("{", encoding="utf-8")
        return
    elif case_name == "map_missing":
        (cluster / "claim-excerpt-map.md").unlink()
        return
    elif case_name == "co_mapped_grammar":
        pointer_overrides[0] = "`entities.json#/0/first_appearance; relations.json#/0`"
    elif case_name == "legacy_grammar":
        pointer_overrides[0] = "`entities[0].claims[0]`"
    elif case_name == "invalid_pointer":
        rows[0] = (rows[0][0], "entities.json#0/first_appearance", rows[0][2])
    elif case_name == "empty_segment":
        rows[0] = (rows[0][0], "entities.json#/0//name", rows[0][2])
    elif case_name == "noncanonical_index":
        rows[0] = (rows[0][0], "entities.json#/00/name", rows[0][2])
    elif case_name == "noncanonical_claim_index":
        rows[0] = (rows[0][0], "entities.json#/0/claims/01", rows[0][2])
    elif case_name == "foreign_path":
        rows[0] = (rows[0][0], "sources.json#/0", rows[0][2])
    elif case_name == "traversal_path":
        rows[0] = (rows[0][0], "../entities.json#/0/first_appearance", rows[0][2])
    elif case_name == "symlink_path":
        source = cluster / "entities.json"
        target = cluster / "entities-data.json"
        target.write_bytes(source.read_bytes())
        source.unlink()
        source.symlink_to(target.name)
        return
    else:
        fail("self_test_contract", f"unknown self-test case {case_name!r}")
    write_test_fixture(cluster, rows, pointer_overrides)


def finding_ids(output):
    found = []
    for line in output.splitlines():
        if line.startswith("FINDING "):
            found.append(line[len("FINDING "):].split(":", 1)[0])
    return sorted(found)


def load_test_expectations():
    contract_path = Path(__file__).resolve().with_name("map-obligations-contract.json")
    if contract_path.is_symlink():
        fail("self_test_contract", "self-test contract must not be a symlink")
    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail("self_test_contract", f"cannot load self-test contract: {error}")
    cases = contract.get("self_test", {}).get("cases") if isinstance(contract, dict) else None
    if not isinstance(cases, list):
        fail("self_test_contract", "contract self_test.cases must be an array")
    expected = {}
    for item in cases:
        if (not isinstance(item, dict) or not isinstance(item.get("id"), str)
                or item.get("exit") not in RESULTS
                or not isinstance(item.get("finding_ids"), list)
                or any(not isinstance(value, str) for value in item["finding_ids"])):
            fail("self_test_contract", "contract contains an invalid self-test expectation")
        if item["id"] in expected:
            fail("self_test_contract", "contract repeats a self-test case ID")
        expected[item["id"]] = item
    if set(expected) != set(SELF_TEST_CASES):
        fail("self_test_contract", "contract self-test cases do not match the implemented cases")
    return expected


def run_self_test():
    try:
        expected = load_test_expectations()
        passed = True
        with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT) as temporary:
            scratch = Path(temporary)
            for case_name in SELF_TEST_CASES:
                cluster = scratch / case_name
                prepare_test_case(case_name, cluster)
                command = [sys.executable, str(Path(__file__).resolve())]
                if case_name.startswith("frozen_"):
                    command.extend(["--frozen", str(cluster)])
                elif case_name == "invalid_arguments":
                    pass
                else:
                    command.append(str(cluster))
                try:
                    result = subprocess.run(
                        command,
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                except OSError as error:
                    fail("self_test_execution", f"cannot invoke real CLI for {case_name}: {error}")
                actual_findings = finding_ids(result.stdout)
                result_lines = [line for line in result.stdout.splitlines() if line.startswith("RESULT ")]
                expectation = expected[case_name]
                wanted = sorted(expectation["finding_ids"])
                ok = (
                    result.returncode == expectation["exit"]
                    and actual_findings == wanted
                    and len(result_lines) == 1
                    and result_lines[0] == f"RESULT {RESULTS[expectation['exit']]}"
                    and not result.stderr
                    and "Traceback" not in result.stdout
                )
                print(f"SELF-TEST {'PASS' if ok else 'FAIL'} {case_name} exit={result.returncode} findings={actual_findings or 'none'}")
                if not ok:
                    passed = False
                    if result.stdout:
                        print(result.stdout.rstrip())
                    if result.stderr:
                        print(result.stderr.rstrip())
        if passed:
            print("RESULT PASS")
            return 0
        print("FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations")
        print("RESULT ERROR")
        return 2
    except ToolError as error:
        print(f"FINDING {error.finding_id}: {error.detail}")
        print("RESULT ERROR")
        return 2
    except OSError as error:
        print(f"FINDING self_test_error: {error}")
        print("RESULT ERROR")
        return 2


def main(argv=None):
    parser = CliParser(description="Compare raw source-attributed JSON obligations with a canonical map")
    parser.add_argument("cluster", nargs="?", type=Path, help="cluster directory")
    parser.add_argument("--map", type=Path, help="map path within the cluster")
    parser.add_argument("--frozen", type=Path, help="verify input SHA-256 pins and replay expected.json from this directory")
    parser.add_argument("--self-test", action="store_true", help="exercise isolated CLI cases")
    try:
        args = parser.parse_args(argv)
    except ToolError as error:
        return emit(2, [(error.finding_id, error.detail)])
    except SystemExit as error:
        return error.code if isinstance(error.code, int) else 2
    if args.self_test:
        if args.cluster is not None or args.map is not None or args.frozen is not None:
            return emit(2, [("invalid_arguments", "--self-test cannot be combined with cluster, --map, or --frozen")])
        return run_self_test()
    if args.frozen is not None:
        if args.cluster is not None or args.map is not None:
            return emit(2, [("invalid_arguments", "--frozen cannot be combined with cluster or --map")])
        try:
            return run_frozen(args.frozen)
        except ToolError as error:
            return emit(2, [(error.finding_id, error.detail)])
    if args.cluster is None:
        return emit(2, [("invalid_arguments", "cluster directory is required")])
    try:
        return run_cluster(args.cluster, args.map)
    except ToolError as error:
        return emit(2, [(error.finding_id, error.detail)])


if __name__ == "__main__":
    raise SystemExit(main())
