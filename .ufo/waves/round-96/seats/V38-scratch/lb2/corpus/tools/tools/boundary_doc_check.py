#!/usr/bin/env python3
"""Check a pinned boundary document, its receipts, anchors, and structure."""

import argparse
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath


SCRIPT_PATH = Path(__file__).resolve()
DEFAULT_ROOT = SCRIPT_PATH.parents[2]
CONTRACT_PATH = "corpus/tools/boundary-doc-contract.json"
CHECKER_PATH = "corpus/fixtures/check_bible.py"
DEFAULT_DOC = "corpus/knowledge/holder-assessment-boundary.md"
FENCE_OPEN = re.compile(r"^[ \t]*(?P<mark>`{3,}|~{3,})(?P<info>[^\r\n]*)[ \t]*(?:\r?\n)?$")
RECEIPT_MARKERS = (
    b"VIOLATION:",
    b"CLEAN:",
    b" violation(s); no canon changed",
)
INSTRUCTION_MARKERS = re.compile(
    r"\bTODO\b|\bTBD\b|\bFIXME\b|\bREPLACE:|\bINSERT HERE\b|"
    r"\bPASTE HERE\b|\bAPPLY ORDER\b|\bOLD TEXT\b|\bNEW TEXT\b|"
    r"\bINSTRUCTION SHEET\b|\bSECTION-REPLACEMENT INSTRUCTIONS\b|"
    r"\bSKIPPED AS NAMED DEBT\b",
    re.IGNORECASE,
)
ANCHOR = re.compile(r"\bcheck_bible\.py:(\d+)(?:-(\d+))?\b")
DIRECT_REPLAY = re.compile(
    r"python3[ \t]+corpus/fixtures/check_bible\.py[ \t]+"
    r"(?P<path>corpus/(?:fixtures|live/runs/round-85/probe-inputs)/[A-Za-z0-9_-]+)"
    r"[ \t]*;[ \t]*echo[ \t]+\"\[rc=\$\?\]\""
)
LOOP_REPLAY = re.compile(
    r"for[ \t]+(?P<var>[A-Za-z_][A-Za-z0-9_]*)[ \t]+in[ \t]+"
    r"(?P<names>[A-Za-z0-9_-]+(?:[ \t]+[A-Za-z0-9_-]+)*)[ \t]*;[ \t]*do\n"
    r"[ \t]*echo[ \t]+\"===[ \t]*\$(?P=var)[ \t]*===\";[ \t]*"
    r"python3[ \t]+corpus/fixtures/check_bible\.py[ \t]+"
    r"(?P<base>corpus/fixtures/|corpus/live/runs/round-85/probe-inputs/)"
    r"(?:\"\$(?P=var)\"|\$(?P=var));[ \t]*"
    r"echo[ \t]+\"\[rc=\$\?\]\"\n"
    r"done"
)
HEX_64 = re.compile(r"^[0-9a-f]{64}$")
HEX_40 = re.compile(r"^[0-9a-f]{40}$")


class CheckResult:
    def __init__(self, returncode, lines, findings=None, metrics=None):
        self.returncode = returncode
        self.lines = lines
        self.findings = findings or []
        self.metrics = metrics or {}


def add_finding(findings, finding_id, detail):
    findings.append((finding_id, detail))


def read_utf8(path, kind):
    try:
        data = path.read_bytes()
    except FileNotFoundError:
        return None, None, (f"{kind}_missing", f"{kind} not found: {path}")
    except OSError as error:
        return None, None, (f"{kind}_unreadable", f"cannot read {kind} {path}: {error}")
    try:
        return data, data.decode("utf-8"), None
    except UnicodeError as error:
        return data, None, (f"{kind}_invalid_utf8", f"{kind} is not UTF-8: {path}: {error}")


def load_contract(root):
    data, text, failure = read_utf8(root / CONTRACT_PATH, "contract")
    if failure:
        return None, None, [failure]
    try:
        contract = json.loads(text)
    except (json.JSONDecodeError, TypeError) as error:
        return None, data, [("contract_invalid", f"invalid contract JSON: {error}")]
    errors = []
    if not isinstance(contract, dict):
        return None, data, [("contract_invalid", "contract root must be an object")]
    document = contract.get("document")
    checker = contract.get("checker")
    expected = contract.get("self_test", {}).get("expected") if isinstance(contract.get("self_test"), dict) else None
    if not isinstance(document, dict) or not isinstance(checker, dict):
        errors.append(("contract_invalid", "document and checker pins must be objects"))
    else:
        if document.get("path") != DEFAULT_DOC or checker.get("path") != CHECKER_PATH:
            errors.append(("contract_invalid", "contract paths do not match the fixed inputs"))
        for label, value in (("document sha256", document.get("sha256")),
                             ("checker sha256", checker.get("sha256")),
                             ("baseline checker sha256", checker.get("legacy_baseline_sha256"))):
            if not isinstance(value, str) or HEX_64.fullmatch(value) is None:
                errors.append(("contract_invalid", f"invalid {label} pin"))
        for label, value in (("document revision", document.get("revision")),
                             ("checker revision", checker.get("revision")),
                             ("legacy baseline revision", checker.get("legacy_baseline_revision"))):
            if not isinstance(value, str) or HEX_40.fullmatch(value) is None:
                errors.append(("contract_invalid", f"invalid {label}"))
        legacy_anchors = checker.get("legacy_anchor_revisions")
        if not isinstance(legacy_anchors, dict):
            errors.append(("contract_invalid", "legacy_anchor_revisions must be an object"))
        else:
            baseline_revision = checker.get("legacy_baseline_revision")
            for anchor, revision in legacy_anchors.items():
                if not isinstance(anchor, str) or ANCHOR.fullmatch(anchor) is None or revision != baseline_revision:
                    errors.append(("contract_invalid", "invalid legacy anchor revision mapping"))
    if not isinstance(contract.get("scope"), str) or not contract.get("scope"):
        errors.append(("contract_invalid", "scope must be a nonempty string"))
    if not isinstance(expected, dict):
        errors.append(("contract_invalid", "self_test.expected must be an object"))
    else:
        for case, result in expected.items():
            if (not isinstance(case, str) or not isinstance(result, dict)
                    or result.get("exit") not in (0, 1)
                    or not isinstance(result.get("finding_ids"), list)
                    or any(not isinstance(item, str) for item in result.get("finding_ids", []))):
                errors.append(("contract_invalid", "invalid self-test expected result"))
                break
    return (contract if not errors else None), data, errors


def markdown_fences(text):
    lines = text.splitlines(keepends=True)
    fences = []
    fenced_lines = set()
    errors = []
    index = 0
    while index < len(lines):
        opening = FENCE_OPEN.match(lines[index])
        if opening is None:
            index += 1
            continue
        marker = opening.group("mark")
        language = opening.group("info").strip().split(maxsplit=1)
        language = language[0].lower() if language else ""
        start = index + 1
        close_re = re.compile(r"^[ \t]*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}[ \t]*(?:\r?\n)?$")
        end = index + 1
        while end < len(lines) and close_re.match(lines[end]) is None:
            end += 1
        if end == len(lines):
            errors.append(f"unclosed fenced block at line {start}")
            fenced_lines.update(range(start, len(lines) + 1))
            break
        fences.append({
            "language": language,
            "body": "".join(lines[index + 1:end]).encode("utf-8"),
            "line": start,
        })
        fenced_lines.update(range(start, end + 2))
        index = end + 1
    return fences, fenced_lines, errors


def looks_like_receipt(body):
    return any(marker in body for marker in RECEIPT_MARKERS)


def is_safe_fixture_path(value):
    path = PurePosixPath(value)
    allowed = (
        value.startswith("corpus/fixtures/"),
        value.startswith("corpus/live/runs/round-85/probe-inputs/"),
    )
    return not path.is_absolute() and ".." not in path.parts and any(allowed)


def parse_checker_command(block):
    try:
        command = block["body"].decode("utf-8").replace("\r\n", "\n").strip()
    except UnicodeDecodeError:
        return None, [f"command block at line {block['line']} is not UTF-8"]
    loop = LOOP_REPLAY.fullmatch(command)
    if loop:
        names = loop.group("names").split()
        paths = [loop.group("base") + name for name in names]
        if any(not is_safe_fixture_path(path) for path in paths):
            return None, [f"unsafe fixture path in command block at line {block['line']}"]
        return {"paths": paths, "names": names, "wrapped": True}, []
    direct = DIRECT_REPLAY.fullmatch(command)
    if direct:
        path = direct.group("path")
        if not is_safe_fixture_path(path):
            return None, [f"unsafe fixture path in command block at line {block['line']}"]
        return {"paths": [path], "names": [None], "wrapped": False}, []
    return None, [f"unsupported checker command grammar at line {block['line']}"]


def parse_wrapped_receipt(body, names, line):
    lines = body.splitlines(keepends=True)
    cases = []
    failures = []
    index = 0
    for expected_name in names:
        if index >= len(lines):
            failures.append(f"receipt at line {line} is missing case {expected_name}")
            break
        wrapper = lines[index].rstrip(b"\r\n")
        if not wrapper.startswith(b"=== ") or not wrapper.endswith(b" ==="):
            failures.append(f"receipt at line {line} expected a case wrapper, got {wrapper!r}")
            break
        actual_name = wrapper[4:-4].decode("utf-8", errors="replace")
        if actual_name != expected_name:
            failures.append(f"receipt at line {line} case order/name mismatch: expected={expected_name!r} observed={actual_name!r}")
        index += 1
        output = []
        while index < len(lines) and not re.fullmatch(rb"\[rc=-?\d+\](?:\r?\n)?", lines[index]):
            if lines[index].startswith(b"=== "):
                break
            output.append(lines[index])
            index += 1
        if index >= len(lines) or not re.fullmatch(rb"\[rc=-?\d+\](?:\r?\n)?", lines[index]):
            failures.append(f"receipt at line {line} case {expected_name} has no return-code wrapper")
            break
        raw_code = lines[index].strip()[4:-1]
        try:
            return_code = int(raw_code)
        except ValueError:
            failures.append(f"receipt at line {line} case {expected_name} has invalid return code")
            return_code = None
        cases.append({"name": expected_name, "stdout": b"".join(output), "returncode": return_code})
        index += 1
    if index != len(lines):
        failures.append(f"receipt at line {line} has unparsed trailing output")
    return cases, failures


def parse_direct_receipt(body, line):
    lines = body.splitlines(keepends=True)
    if not lines or re.fullmatch(rb"\[rc=-?\d+\](?:\r?\n)?", lines[-1]) is None:
        return None, [f"receipt at line {line} has no final return-code wrapper"]
    try:
        return_code = int(lines[-1].strip()[4:-1])
    except ValueError:
        return None, [f"receipt at line {line} has invalid return-code wrapper"]
    return {"stdout": b"".join(lines[:-1]), "returncode": return_code}, []


def replay_receipts(root, checker_path, fences):
    failures = []
    commands = {
        index: block for index, block in enumerate(fences)
        if block["language"] in {"sh", "bash"} and CHECKER_PATH.encode() in block["body"]
    }
    receipts = [(index, block) for index, block in enumerate(fences) if looks_like_receipt(block["body"])]
    paired = set()
    matched_receipts = 0
    matched_cases = 0
    total_cases = 0
    if not receipts:
        add_finding(failures, "receipt_structure", "no checker output receipt blocks found")
    for index, receipt in receipts:
        command_index = index - 1
        if command_index not in commands:
            add_finding(failures, "receipt_structure", f"checker receipt at line {receipt['line']} has no immediately preceding checker command block")
            continue
        if command_index in paired:
            add_finding(failures, "receipt_structure", f"checker command at line {commands[command_index]['line']} has multiple receipt blocks")
            continue
        paired.add(command_index)
        command, command_failures = parse_checker_command(commands[command_index])
        for detail in command_failures:
            add_finding(failures, "receipt_grammar", detail)
        if command is None:
            continue
        if command["wrapped"]:
            expected, parse_failures = parse_wrapped_receipt(receipt["body"], command["names"], receipt["line"])
        else:
            expected_one, parse_failures = parse_direct_receipt(receipt["body"], receipt["line"])
            expected = [expected_one] if expected_one is not None else []
        for detail in parse_failures:
            add_finding(failures, "receipt_structure", detail)
        total_cases += len(command["paths"])
        if len(expected) != len(command["paths"]):
            add_finding(failures, "receipt_structure", f"receipt at line {receipt['line']} case count mismatch: commands={len(command['paths'])} receipts={len(expected)}")
        receipt_ok = len(expected) == len(command["paths"]) and not parse_failures
        for case_index, path in enumerate(command["paths"]):
            case_name = command["names"][case_index]
            fixture = root / path
            if not fixture.is_dir():
                add_finding(failures, "receipt_input_missing", f"replay fixture missing for {case_name or path}: {path}")
                receipt_ok = False
                continue
            try:
                result = subprocess.run(
                    [sys.executable, str(checker_path), path],
                    cwd=root,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )
            except OSError as error:
                add_finding(failures, "receipt_execution", f"replay could not start for {case_name or path}: {error}")
                receipt_ok = False
                continue
            item = expected[case_index] if case_index < len(expected) else None
            if item is None:
                continue
            case_ok = True
            if item["stdout"] != result.stdout:
                add_finding(failures, "receipt_drift", f"stdout mismatch for {case_name or path} (receipt line {receipt['line']})")
                case_ok = False
            if item["returncode"] != result.returncode:
                add_finding(failures, "receipt_drift", f"return-code mismatch for {case_name or path}: receipt={item['returncode']} observed={result.returncode}")
                case_ok = False
            if result.stderr:
                add_finding(failures, "receipt_drift", f"unexpected stderr for {case_name or path}: {result.stderr.decode('utf-8', errors='replace').rstrip()!r}")
                case_ok = False
            if case_ok:
                matched_cases += 1
            else:
                receipt_ok = False
        if receipt_ok:
            matched_receipts += 1
    for index, block in commands.items():
        if index not in paired:
            add_finding(failures, "receipt_structure", f"checker command block at line {block['line']} has no receipt block")
    return matched_receipts, len(receipts), matched_cases, total_cases, failures


def check_anchors(doc_text, checker_bytes, baseline_bytes, checker_spec):
    matches = list(ANCHOR.finditer(doc_text))
    failures = []
    resolved = 0
    baseline_revision = checker_spec["legacy_baseline_revision"]
    legacy_anchors = checker_spec["legacy_anchor_revisions"]
    found_legacy = set()
    for match in matches:
        citation = match.group(0)
        revision = legacy_anchors.get(citation)
        if revision is not None:
            found_legacy.add(citation)
            source = baseline_bytes if revision == baseline_revision else None
            source_name = f"baseline {revision}"
        else:
            source = checker_bytes
            source_name = "delivered checker"
        if source is None:
            add_finding(failures, "anchor_range", f"unavailable revision for anchor {citation}")
            continue
        line_count = len(source.splitlines())
        first = int(match.group(1))
        last = int(match.group(2) or first)
        if first < 1 or last < first or last > line_count:
            add_finding(failures, "anchor_range", f"unresolved anchor {citation} against {source_name}: checker has {line_count} lines")
        else:
            resolved += 1
    for citation in set(legacy_anchors) - found_legacy:
        add_finding(failures, "anchor_range", f"declared legacy anchor not found: {citation}")
    return len(matches), resolved, failures


def check_structure(doc_text, fenced_lines, fence_errors):
    failures = []
    for detail in fence_errors:
        add_finding(failures, "document_structure", detail)
    original_lines = doc_text.splitlines()
    prose_lines = ["" if number in fenced_lines else line for number, line in enumerate(original_lines, 1)]
    marker_count = 0
    for line_number, line in enumerate(prose_lines, 1):
        if line_number in fenced_lines:
            continue
        for match in INSTRUCTION_MARKERS.finditer(line):
            marker_count += 1
            add_finding(failures, "document_structure", f"instruction marker {match.group(0)!r} at non-fenced line {line_number}")
    prose = "\n".join(prose_lines)
    without_comments = re.sub(r"<!--.*?-->", lambda match: "\n" * match.group(0).count("\n"), prose, flags=re.DOTALL)
    headings = []
    for line_number, line in enumerate(without_comments.splitlines(), 1):
        match = re.match(r"^[ \t]*(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", line)
        if match is None:
            continue
        title = re.sub(r"[`*_~]", "", match.group(2))
        title = re.sub(r"\s+", " ", title).strip().casefold()
        headings.append((len(match.group(1)), title, line_number))
    h1_count = sum(level == 1 for level, _, _ in headings)
    if h1_count != 1:
        add_finding(failures, "document_structure", f"expected exactly one level-one heading; observed {h1_count}")
    by_title = {}
    for _, title, line_number in headings:
        by_title.setdefault(title, []).append(line_number)
    duplicates = [(title, lines) for title, lines in by_title.items() if len(lines) > 1]
    for title, lines in duplicates:
        add_finding(failures, "document_structure", f"duplicate heading {title!r} at lines {lines}")
    return h1_count, len(duplicates), marker_count, failures


def fail_result(findings, heading="CHECK pinned inputs: FAIL"):
    lines = [heading]
    lines.extend(f"FINDING {finding_id}: {detail}" for finding_id, detail in findings)
    lines.append("CERTIFICATION FAIL")
    return CheckResult(1, lines, findings)


def resolve_path(root, value):
    path = Path(value)
    return path if path.is_absolute() else root / path


def read_baseline_checker(root, checker_spec, override=None):
    if override is not None:
        return override, None
    revision = checker_spec["legacy_baseline_revision"]
    try:
        result = subprocess.run(
            ["git", "show", f"{revision}:{CHECKER_PATH}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as error:
        return None, ("baseline_checker_unavailable", f"could not read baseline checker {revision}: {error}")
    if result.returncode != 0:
        return None, ("baseline_checker_unavailable", f"could not read baseline checker at {revision}")
    if hashlib.sha256(result.stdout).hexdigest() != checker_spec["legacy_baseline_sha256"]:
        return None, ("baseline_checker_drift", f"baseline checker digest differs for revision {revision}")
    try:
        result.stdout.decode("utf-8")
    except UnicodeError as error:
        return None, ("baseline_checker_invalid_utf8", f"baseline checker is not UTF-8: {error}")
    return result.stdout, None


def audit(root, doc_arg=None, checker_arg=None, baseline_override=None):
    root = Path(root).resolve()
    contract, _, contract_failures = load_contract(root)
    if contract_failures:
        return fail_result(contract_failures)
    document_spec = contract["document"]
    checker_spec = contract["checker"]
    document_path = resolve_path(root, doc_arg if doc_arg is not None else document_spec["path"])
    checker_path = resolve_path(root, checker_arg if checker_arg is not None else checker_spec["path"])
    failures = []
    document_bytes, doc_text, document_failure = read_utf8(document_path, "document")
    checker_bytes, checker_text, checker_failure = read_utf8(checker_path, "checker")
    if document_failure:
        failures.append(document_failure)
    if checker_failure:
        failures.append(checker_failure)
    if doc_text is not None and hashlib.sha256(document_bytes).hexdigest() != document_spec["sha256"]:
        add_finding(failures, "document_drift", f"document digest differs from pinned {document_spec['revision']} bytes")
    if checker_text is not None and hashlib.sha256(checker_bytes).hexdigest() != checker_spec["sha256"]:
        add_finding(failures, "checker_drift", "delivered checker digest differs from the committed pin")
    if failures:
        return fail_result(failures)
    baseline_bytes, baseline_failure = read_baseline_checker(root, checker_spec, baseline_override)
    if baseline_failure:
        return fail_result([baseline_failure])
    fences, fenced_lines, fence_errors = markdown_fences(doc_text)
    receipt_counts = replay_receipts(root, checker_path, fences)
    matched_receipts, found_receipts, matched_cases, total_cases, replay_failures = receipt_counts
    anchor_total, anchor_resolved, anchor_failures = check_anchors(doc_text, checker_bytes, baseline_bytes, checker_spec)
    h1_count, duplicate_count, marker_count, structure_failures = check_structure(doc_text, fenced_lines, fence_errors)
    failures.extend(replay_failures)
    failures.extend(anchor_failures)
    failures.extend(structure_failures)
    replay_ok = not replay_failures and found_receipts > 0 and matched_receipts == found_receipts
    anchors_ok = not anchor_failures and anchor_resolved == anchor_total
    structure_ok = not structure_failures and h1_count == 1 and duplicate_count == 0 and marker_count == 0
    lines = [
        "CHECK pinned inputs: PASS",
        f"CHECK receipt replay: {'PASS' if replay_ok else 'FAIL'}",
        f"CHECK explicit anchor ranges: {'PASS' if anchors_ok else 'FAIL'}",
        f"CHECK document structure: {'PASS' if structure_ok else 'FAIL'}",
        f"scope={contract['scope']}",
        f"replay_receipts={matched_receipts}/{found_receipts}",
        f"replay_cases={matched_cases}/{total_cases}",
        f"anchors={anchor_resolved}/{anchor_total}",
        f"h1_count={h1_count}",
        f"duplicate_headings={duplicate_count}",
        f"instruction_markers={marker_count}",
    ]
    lines.extend(f"FINDING {finding_id}: {detail}" for finding_id, detail in failures)
    if failures:
        lines.append("CERTIFICATION FAIL")
        return CheckResult(1, lines, failures, {"replay_cases": f"{matched_cases}/{total_cases}"})
    lines.append("CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)")
    return CheckResult(0, lines, [], {"replay_cases": f"{matched_cases}/{total_cases}"})


def git_blob(root, revision, path):
    try:
        result = subprocess.run(
            ["git", "show", f"{revision}:{path}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as error:
        raise RuntimeError(f"cannot read committed input {revision}:{path}: {error}") from error
    if result.returncode != 0:
        raise RuntimeError(f"cannot read committed input {revision}:{path}")
    return result.stdout


def checker_fixture_paths(doc_text):
    fences, _, errors = markdown_fences(doc_text)
    if errors:
        raise RuntimeError("committed document has an unclosed fenced block")
    paths = []
    for block in fences:
        if block["language"] in {"sh", "bash"} and CHECKER_PATH.encode() in block["body"]:
            command, failures = parse_checker_command(block)
            if failures or command is None:
                raise RuntimeError("committed document has an unsupported replay command")
            paths.extend(command["paths"])
    if not paths:
        raise RuntimeError("committed document has no replay fixtures")
    return sorted(set(paths))


def committed_fixture_files(root, revision, fixture_paths):
    try:
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", revision, "--", *fixture_paths],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as error:
        raise RuntimeError(f"cannot list committed fixture files: {error}") from error
    if listing.returncode != 0:
        raise RuntimeError("cannot list committed fixture files")
    files = [line for line in listing.stdout.decode("utf-8").splitlines() if line]
    if not files:
        raise RuntimeError("no committed fixture files found")
    return files


def parse_finding_ids(output):
    ids = set()
    for line in output.splitlines():
        if line.startswith("FINDING "):
            ids.add(line[len("FINDING "):].split(":", 1)[0])
    return sorted(ids)


def run_anchor_range_control(baseline_checker, checker_spec, expected):
    legacy_anchor = expected["legacy_anchor"]
    out_of_range_anchor = expected["out_of_range_anchor"]
    legacy_revision = expected["legacy_revision"]
    delivered_checker = b"control line\n" * expected["delivered_line_count"]
    control_doc = f"legacy {legacy_anchor}; delivered {out_of_range_anchor}"
    total, resolved, findings = check_anchors(control_doc, delivered_checker, baseline_checker, checker_spec)
    finding_ids = sorted({finding_id for finding_id, _ in findings})
    details = [detail for _, detail in findings]
    baseline_lines = len(baseline_checker.splitlines())
    actual_exit = 1 if findings else 0
    legacy_revision_ok = checker_spec["legacy_anchor_revisions"].get(legacy_anchor) == legacy_revision
    passed = (
        legacy_revision_ok
        and baseline_lines == expected["legacy_line_count"]
        and actual_exit == expected["exit"]
        and finding_ids == sorted(set(expected["finding_ids"]))
        and total == expected["anchor_total"]
        and resolved == expected["anchor_resolved"]
        and details == expected["finding_details"]
    )
    if passed:
        print(
            f"SELF-TEST PASS anchor_range_control exit={actual_exit} findings={finding_ids} "
            f"anchors={resolved}/{total} legacy_anchor={legacy_anchor}@{legacy_revision} "
            f"baseline_lines={baseline_lines}"
        )
        return True
    print(
        f"SELF-TEST FAIL anchor_range_control exit={actual_exit} findings={finding_ids} "
        f"anchors={resolved}/{total} legacy_revision_ok={legacy_revision_ok} "
        f"baseline_lines={baseline_lines} details={details}"
    )
    return False


def run_self_test():
    root = DEFAULT_ROOT
    contract, contract_bytes, contract_failures = load_contract(root)
    if contract_failures:
        for finding_id, detail in contract_failures:
            print(f"SELF-TEST FAIL {finding_id}: {detail}")
        return 1
    try:
        document_revision = contract["document"]["revision"]
        checker_revision = contract["checker"]["revision"]
        baseline_revision = contract["checker"]["legacy_baseline_revision"]
        committed_doc = git_blob(root, document_revision, DEFAULT_DOC)
        committed_checker = git_blob(root, checker_revision, CHECKER_PATH)
        baseline_checker = git_blob(root, baseline_revision, CHECKER_PATH)
        if hashlib.sha256(committed_doc).hexdigest() != contract["document"]["sha256"]:
            raise RuntimeError("committed default document does not match its persisted pin")
        if hashlib.sha256(committed_checker).hexdigest() != contract["checker"]["sha256"]:
            raise RuntimeError("committed delivered checker does not match its persisted pin")
        if hashlib.sha256(baseline_checker).hexdigest() != contract["checker"]["legacy_baseline_sha256"]:
            raise RuntimeError("committed legacy checker does not match its persisted pin")
        fixture_paths = checker_fixture_paths(committed_doc.decode("utf-8"))
        fixture_files = committed_fixture_files(root, document_revision, fixture_paths)
        baseline_file_data = baseline_checker
    except (RuntimeError, UnicodeError, OSError) as error:
        print(f"SELF-TEST FAIL committed inputs: {error}")
        return 1
    expected = contract["self_test"]["expected"]
    cases = (
        "committed_default",
        "comment_parked_c9",
        "wrong_bare_anchor",
        "checker_drift",
        "missing_document",
        "missing_checker",
        "receipt_drift",
    )
    anchor_control = expected.get("anchor_range_control")
    control_fields = (
        "exit", "finding_ids", "anchor_total", "anchor_resolved", "delivered_line_count",
        "legacy_line_count", "legacy_anchor", "legacy_revision", "out_of_range_anchor", "finding_details",
    )
    if (any(name not in expected for name in cases)
            or not isinstance(anchor_control, dict)
            or any(field not in anchor_control for field in control_fields)):
        print("SELF-TEST FAIL contract_invalid: expected outcomes are incomplete")
        return 1
    with tempfile.TemporaryDirectory(prefix="boundary-doc-self-test-") as scratch:
        scratch_root = Path(scratch)
        base_root = scratch_root / "committed"
        (base_root / "corpus/tools").mkdir(parents=True)
        (base_root / DEFAULT_DOC).parent.mkdir(parents=True, exist_ok=True)
        (base_root / CHECKER_PATH).parent.mkdir(parents=True, exist_ok=True)
        (base_root / CONTRACT_PATH).parent.mkdir(parents=True, exist_ok=True)
        (base_root / DEFAULT_DOC).write_bytes(committed_doc)
        (base_root / CHECKER_PATH).write_bytes(committed_checker)
        (base_root / CONTRACT_PATH).write_bytes(contract_bytes)
        try:
            for relative in fixture_files:
                safe = PurePosixPath(relative)
                if safe.is_absolute() or ".." in safe.parts:
                    raise RuntimeError(f"unsafe committed fixture path: {relative}")
                destination = base_root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(git_blob(root, document_revision, relative))
        except (RuntimeError, OSError) as error:
            print(f"SELF-TEST FAIL committed fixtures: {error}")
            return 1
        baseline_path = scratch_root / "legacy-checker.py"
        baseline_path.write_bytes(baseline_file_data)
        environment = os.environ.copy()
        environment["BOUNDARY_DOC_SELF_TEST"] = "1"

        def run_case(name, mutate=None):
            case_root = scratch_root / name
            shutil.copytree(base_root, case_root)
            if mutate is not None:
                mutate(case_root)
            try:
                result = subprocess.run(
                    [sys.executable, str(SCRIPT_PATH), "--_test-root", str(case_root), "--_test-baseline", str(baseline_path)],
                    cwd=root,
                    env=environment,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=False,
                )
            except OSError as error:
                raise RuntimeError(f"could not invoke self-test case {name}: {error}") from error
            actual_ids = parse_finding_ids(result.stdout)
            expected_case = expected[name]
            expected_ids = sorted(set(expected_case["finding_ids"]))
            ok = result.returncode == expected_case["exit"] and actual_ids == expected_ids
            if expected_case.get("replay_cases") is not None:
                observed = next((line.split("=", 1)[1] for line in result.stdout.splitlines() if line.startswith("replay_cases=")), None)
                ok = ok and observed == expected_case["replay_cases"]
            if expected_case.get("forbid_traceback"):
                ok = ok and "Traceback" not in result.stdout + result.stderr
            if not ok:
                print(f"SELF-TEST FAIL {name}: exit={result.returncode} findings={actual_ids}")
                if result.stdout:
                    print(result.stdout.rstrip())
                if result.stderr:
                    print(result.stderr.rstrip())
                return False
            print(f"SELF-TEST PASS {name} exit={result.returncode} findings={actual_ids or 'none'}")
            return True

        def comment_parked(root_path):
            path = root_path / DEFAULT_DOC
            text = path.read_text(encoding="utf-8")
            text = text.replace("Tick findings are NOT qualified", "Tick findings inherit holder qualification")
            text = text.replace("integer comparison", "holder qualification")
            path.write_text(text + "\n<!-- Tick findings are NOT qualified; integer comparison -->\n", encoding="utf-8")

        def wrong_anchor(root_path):
            path = root_path / DEFAULT_DOC
            text = path.read_text(encoding="utf-8")
            old = "comparison gate (`:322`)"
            if old not in text:
                raise RuntimeError("self-test anchor target was not present")
            path.write_text(text.replace(old, "comparison gate (`:325`)", 1), encoding="utf-8")

        def drift_checker(root_path):
            path = root_path / CHECKER_PATH
            path.write_bytes(path.read_bytes() + b"\nraise RuntimeError('changed checker must not execute')\n")

        def remove_document(root_path):
            (root_path / DEFAULT_DOC).unlink()

        def remove_checker(root_path):
            (root_path / CHECKER_PATH).unlink()

        def drift_receipt_input(root_path):
            path = root_path / "corpus/live/runs/round-85/probe-inputs/r85-unique-break-control/entities.json"
            data = path.read_bytes()
            old = b'"to_holder": "vault"'
            if old not in data:
                raise RuntimeError("self-test receipt input target was not present")
            path.write_bytes(data.replace(old, b'"to_holder": "drifted-vault"', 1))

        mutations = {
            "committed_default": None,
            "comment_parked_c9": comment_parked,
            "wrong_bare_anchor": wrong_anchor,
            "checker_drift": drift_checker,
            "missing_document": remove_document,
            "missing_checker": remove_checker,
            "receipt_drift": drift_receipt_input,
        }
        passed = run_anchor_range_control(baseline_file_data, contract["checker"], anchor_control)
        for name in cases:
            try:
                passed = run_case(name, mutations[name]) and passed
            except (RuntimeError, OSError, UnicodeError) as error:
                print(f"SELF-TEST FAIL {name}: {error}")
                passed = False
        if passed:
            print("SELF-TEST PASS")
            return 0
        print("SELF-TEST FAIL")
        return 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check frozen boundary-document drift, recorded receipts, explicit anchor ranges, and structure; no semantic or AST validation."
    )
    parser.add_argument("--doc", help="document path (default: pinned path under the script's repo root)")
    parser.add_argument("--checker", help="delivered checker path (default: pinned path under the script's repo root)")
    parser.add_argument("--self-test", action="store_true", help="exercise isolated committed inputs and adversarial cases")
    parser.add_argument("--_test-root", help=argparse.SUPPRESS)
    parser.add_argument("--_test-baseline", help=argparse.SUPPRESS)
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        return 0 if error.code == 0 else 1
    if args.self_test:
        if args.doc is not None or args.checker is not None or args._test_root is not None or args._test_baseline is not None:
            print("SELF-TEST FAIL: --self-test cannot be combined with path overrides")
            return 1
        return run_self_test()
    if args._test_root is not None or args._test_baseline is not None:
        if os.environ.get("BOUNDARY_DOC_SELF_TEST") != "1" or args._test_root is None or args._test_baseline is None:
            print("FINDING internal_test_mode: isolated root override is available only to --self-test")
            print("CERTIFICATION FAIL")
            return 1
        root = Path(args._test_root)
        try:
            baseline_override = Path(args._test_baseline).read_bytes()
        except OSError as error:
            return print_result(fail_result([("baseline_checker_unavailable", f"cannot read isolated baseline checker: {error}")]))
    else:
        root = DEFAULT_ROOT
        baseline_override = None
    return print_result(audit(root, args.doc, args.checker, baseline_override))


def print_result(result):
    for line in result.lines:
        print(line)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
