#!/usr/bin/env python3
"""Certify the delivered holder-assessment boundary document."""

import argparse
import pathlib
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


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
            "start": start,
            "end": end + 1,
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
            failures.append(
                f"receipt at line {line} case order/name mismatch: expected={expected_name!r} observed={actual_name!r}"
            )
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


def replay_receipts(root, checker, fences):
    failures = []
    commands = {
        index: block for index, block in enumerate(fences)
        if block["language"] in {"sh", "bash"} and CHECKER_PATH.encode() in block["body"]
    }
    receipts = [
        (index, block) for index, block in enumerate(fences)
        if looks_like_receipt(block["body"])
    ]
    paired = set()
    matched_receipts = 0
    matched_cases = 0
    total_cases = 0
    if not receipts:
        failures.append("no checker output receipt blocks found")
    for index, receipt in receipts:
        command_index = index - 1
        if command_index not in commands:
            failures.append(f"checker receipt at line {receipt['line']} has no immediately preceding checker command block")
            continue
        if command_index in paired:
            failures.append(f"checker command at line {commands[command_index]['line']} has multiple receipt blocks")
            continue
        paired.add(command_index)
        command, command_failures = parse_checker_command(commands[command_index])
        failures.extend(command_failures)
        if command is None:
            continue
        if command["wrapped"]:
            expected, parse_failures = parse_wrapped_receipt(
                receipt["body"], command["names"], receipt["line"]
            )
        else:
            expected_one, parse_failures = parse_direct_receipt(receipt["body"], receipt["line"])
            expected = [expected_one] if expected_one is not None else []
        failures.extend(parse_failures)
        total_cases += len(command["paths"])
        if len(expected) != len(command["paths"]):
            failures.append(
                f"receipt at line {receipt['line']} case count mismatch: "
                f"commands={len(command['paths'])} receipts={len(expected)}"
            )
        receipt_ok = len(expected) == len(command["paths"]) and not parse_failures
        for case_index, path in enumerate(command["paths"]):
            case_name = command["names"][case_index]
            fixture = root / path
            if not fixture.is_dir():
                failures.append(f"replay fixture missing for {case_name or path}: {path}")
                receipt_ok = False
                continue
            try:
                result = subprocess.run(
                    [sys.executable, str(checker), path],
                    cwd=root,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )
            except OSError as error:
                failures.append(f"replay could not start for {case_name or path}: {error}")
                receipt_ok = False
                continue
            item = expected[case_index] if case_index < len(expected) else None
            case_ok = item is not None
            if item is None:
                continue
            if item["stdout"] != result.stdout:
                failures.append(
                    f"stdout mismatch for {case_name or path} (receipt line {receipt['line']})"
                )
                case_ok = False
            if item["returncode"] != result.returncode:
                failures.append(
                    f"return-code mismatch for {case_name or path}: "
                    f"receipt={item['returncode']} observed={result.returncode}"
                )
                case_ok = False
            if result.stderr:
                failures.append(
                    f"unexpected stderr for {case_name or path}: {result.stderr.decode('utf-8', errors='replace').rstrip()!r}"
                )
                case_ok = False
            if case_ok:
                matched_cases += 1
            else:
                receipt_ok = False
        if receipt_ok:
            matched_receipts += 1
    for index, block in commands.items():
        if index not in paired:
            failures.append(f"checker command block at line {block['line']} has no receipt block")
    return matched_receipts, len(receipts), matched_cases, total_cases, failures


def check_anchors(doc_text, checker_path):
    matches = list(ANCHOR.finditer(doc_text))
    failures = []
    if not checker_path.is_file():
        return len(matches), 0, [f"delivered checker not found: {checker_path}"]
    try:
        line_count = len(checker_path.read_bytes().splitlines())
    except OSError as error:
        return len(matches), 0, [f"could not read delivered checker {checker_path}: {error}"]
    resolved = 0
    for match in matches:
        first = int(match.group(1))
        last = int(match.group(2) or first)
        citation = match.group(0)
        if first < 1 or last < first or last > line_count:
            failures.append(
                f"unresolved anchor {citation}: checker has {line_count} lines"
            )
        else:
            resolved += 1
    return len(matches), resolved, failures


def check_structure(doc_text, fenced_lines, fence_errors):
    failures = list(fence_errors)
    original_lines = doc_text.splitlines()
    prose_lines = [
        "" if number in fenced_lines else line
        for number, line in enumerate(original_lines, 1)
    ]
    marker_count = 0
    for line_number, line in enumerate(prose_lines, 1):
        if line_number in fenced_lines:
            continue
        for match in INSTRUCTION_MARKERS.finditer(line):
            marker_count += 1
            failures.append(
                f"instruction marker {match.group(0)!r} at non-fenced line {line_number}"
            )
    prose = "\n".join(prose_lines)
    without_comments = re.sub(
        r"<!--.*?-->",
        lambda match: "\n" * match.group(0).count("\n"),
        prose,
        flags=re.DOTALL,
    )
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
        failures.append(f"expected exactly one level-one heading; observed {h1_count}")
    by_title = {}
    for _, title, line_number in headings:
        by_title.setdefault(title, []).append(line_number)
    duplicates = [(title, lines) for title, lines in by_title.items() if len(lines) > 1]
    for title, lines in duplicates:
        failures.append(f"duplicate heading {title!r} at lines {lines}")
    return h1_count, len(duplicates), marker_count, failures


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Replay boundary-document receipts and check its anchors and structure"
    )
    parser.add_argument("--doc", default=DEFAULT_DOC, help="document path (default: %(default)s)")
    parser.add_argument("--checker", default=CHECKER_PATH, help="delivered checker path (default: %(default)s)")
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        return 0 if error.code == 0 else 1
    root = Path.cwd().resolve()
    doc_path = Path(args.doc)
    checker_path = Path(args.checker)
    if not doc_path.is_absolute():
        doc_path = root / doc_path
    if not checker_path.is_absolute():
        checker_path = root / checker_path
    failures = []
    ok, digest = checker_pin_check(args.checker)
    if not ok:
        failures.append(f"checker hash pin: {digest[:16]}... != pinned {EXPECTED_CHECKER_SHA256[:16]}...")
    if not c9_semantics_check(pathlib.Path(args.doc).read_text()):
        failures.append("C9 semantics: required markers missing or a legacy tick-qualification claim present")
    try:
        doc_bytes = doc_path.read_bytes()
        doc_text = doc_bytes.decode("utf-8")
    except (OSError, UnicodeError) as error:
        print(f"FAIL document: cannot read {doc_path}: {error}")
        print("CERTIFICATION FAIL")
        return 1
    fences, fenced_lines, fence_errors = markdown_fences(doc_text)
    receipt_counts = replay_receipts(root, checker_path, fences)
    matched_receipts, found_receipts, matched_cases, total_cases, replay_failures = receipt_counts
    anchor_total, anchor_resolved, anchor_failures = check_anchors(doc_text, checker_path)
    h1_count, duplicate_count, marker_count, structure_failures = check_structure(
        doc_text, fenced_lines, fence_errors
    )
    failures.extend(replay_failures)
    failures.extend(anchor_failures)
    failures.extend(structure_failures)
    replay_ok = not replay_failures and found_receipts > 0 and matched_receipts == found_receipts
    anchors_ok = not anchor_failures and anchor_resolved == anchor_total
    structure_ok = not structure_failures and h1_count == 1 and duplicate_count == 0 and marker_count == 0
    print(f"CHECK receipt replay: {'PASS' if replay_ok else 'FAIL'}")
    print(f"CHECK code anchors: {'PASS' if anchors_ok else 'FAIL'}")
    print(f"CHECK document structure: {'PASS' if structure_ok else 'FAIL'}")
    print(f"replay_receipts={matched_receipts}/{found_receipts}")
    print(f"replay_cases={matched_cases}/{total_cases}")
    print(f"anchors={anchor_resolved}/{anchor_total}")
    print(f"h1_count={h1_count}")
    print(f"duplicate_headings={duplicate_count}")
    print(f"instruction_markers={marker_count}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("CERTIFICATION FAIL")
        return 1
    print("CERTIFIED")
    return 0


EXPECTED_CHECKER_SHA256 = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"
REQUIRED_C9_MARKERS = ["Tick findings are NOT qualified", "integer comparison"]
FORBIDDEN_LEGACY_TICK = "holder identity is not uniquely resolvable: {expected}"

def checker_pin_check(checker_path):
    import hashlib, pathlib
    digest = hashlib.sha256(pathlib.Path(checker_path).read_bytes()).hexdigest()
    return digest == EXPECTED_CHECKER_SHA256, digest

def c9_semantics_check(doc_text):
    has_markers = all(m in doc_text for m in REQUIRED_C9_MARKERS)
    has_legacy = FORBIDDEN_LEGACY_TICK in doc_text
    return has_markers and not has_legacy


if __name__ == "__main__":
    raise SystemExit(main())
