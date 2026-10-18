#!/usr/bin/env python3
"""Freeze and verify per-fixture dependency inventories for the crossing chain.

BR-01 class: a dropped `depends_on` edge or a changed relation endpoint leaves
every current gate green. This tool pins, for each delivered continuation-chain
fixture, the event dependency-edge inventory (event id -> sorted `depends_on`
set), the event endpoints (tick, entity_id, place_id), the relation endpoint
triples (from, to, type), and the fixture's JSON content digests. Verification
compares the current fixture against the pin; the semantic inventory decides
first, and a content change the inventory does not model is reported as
could-not-evaluate.
"""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "corpus/tools/dependency-freeze-contract.json"
CONTRACT_RELPATH = "corpus/tools/dependency-freeze-contract.json"
DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")
REQUIRED_FILES = ("relations.json", "timeline.json")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
RESULTS = {0: "PASS", 1: "FAIL", 2: "ERROR"}
FROZEN_CASES = (
    "clean",
    "reduction_edge_drop",
    "addition_edge_phantom",
    "event_removed",
    "event_endpoint_change",
    "relation_endpoint_flip",
    "relation_removed",
    "relation_added",
    "digest_tamper",
    "malformed_json",
    "missing_timeline",
    "unpinned_fixture",
    "missing_fixture",
    "invalid_arguments",
)
SELF_TEST_BASE = "r95-crossing-aftermath"


class ToolError(Exception):
    def __init__(self, finding_id, detail):
        super().__init__(detail)
        self.finding_id = finding_id
        self.detail = detail


class CliParser(argparse.ArgumentParser):
    def error(self, message):
        raise ToolError("INVALID-ARGUMENTS", message)


def fail(finding_id, detail):
    raise ToolError(finding_id, detail)


def emit(code, findings=()):
    for finding_id, detail in sorted(findings):
        print(f"FINDING {finding_id}: {detail}")
    print(f"RESULT {RESULTS[code]}")


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def content_digest(files):
    payload = json.dumps({name: sha256_bytes(raw) for name, raw in files.items()},
                         sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def read_json(path, label):
    try:
        raw = path.read_bytes()
    except OSError as error:
        fail("FILE-MISSING", f"{label} is unreadable: {error}")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        fail("MALFORMED-JSON", f"{label} is not UTF-8: {error}")
    try:
        return raw, json.loads(text)
    except json.JSONDecodeError as error:
        fail("MALFORMED-JSON", f"{label}: {error}")


def scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def build_model(fixture):
    if not fixture.is_dir():
        fail("FIXTURE-MISSING", f"fixture directory not found: {fixture}")
    files = {}
    for name in DATA_FILES:
        candidate = fixture / name
        if candidate.is_file():
            raw, _ = read_json(candidate, name)
            files[name] = raw
    for name in REQUIRED_FILES:
        if name not in files:
            fail("FILE-MISSING", f"{name} is missing from {fixture}")
    parsed = {}
    for name in sorted(files):
        try:
            parsed[name] = json.loads(files[name].decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            fail("MALFORMED-JSON", f"{name}: {error}")
    timeline = parsed["timeline.json"]
    relations = parsed["relations.json"]
    if not isinstance(timeline, list) or not isinstance(relations, list):
        fail("MALFORMED-MODEL", "timeline.json and relations.json must be JSON arrays")
    events = {}
    for index, record in enumerate(timeline):
        if not isinstance(record, dict) or not isinstance(record.get("id"), str) or not record["id"]:
            fail("MALFORMED-MODEL", f"timeline[{index}] needs a nonempty string id")
        event_id = record["id"]
        if event_id in events:
            fail("MALFORMED-MODEL", f"timeline[{index}] repeats event id {event_id}")
        deps = record.get("depends_on", [])
        if not isinstance(deps, list) or any(not isinstance(dep, str) or not dep for dep in deps):
            fail("MALFORMED-MODEL", f"timeline[{index}].depends_on must be an array of nonempty strings")
        endpoint = {}
        for key in ("tick", "entity_id", "place_id"):
            value = record.get(key)
            if not scalar(value):
                fail("MALFORMED-MODEL", f"timeline[{index}].{key} must be a scalar")
            endpoint[key] = value
        events[event_id] = {"depends_on": sorted(set(deps)), "endpoint": endpoint}
    triples = []
    for index, record in enumerate(relations):
        if (not isinstance(record, dict)
                or any(not isinstance(record.get(key), str) or not record[key] for key in ("from", "to", "type"))):
            fail("MALFORMED-MODEL", f"relations[{index}] needs nonempty string from/to/type")
        triples.append([record["from"], record["to"], record["type"]])
    counts = {
        "events": len(events),
        "dependency_edges": sum(len(entry["depends_on"]) for entry in events.values()),
        "relations": len(triples),
    }
    for name, key in (("entities.json", "entities"), ("sources.json", "sources")):
        value = parsed.get(name)
        if isinstance(value, list):
            counts[key] = len(value)
    return {
        "events": events,
        "relations": sorted(triples),
        "content_sha256": content_digest(files),
        "files": {name: sha256_bytes(raw) for name, raw in sorted(files.items())},
        "counts": counts,
    }


def format_triples(counter):
    return ", ".join(f"[{', '.join(triple)}]" for triple in sorted(counter))


def compare(pin, observed):
    findings = []
    frozen_events = pin["events"]
    current_events = observed["events"]
    for event_id in sorted(frozen_events):
        frozen = frozen_events[event_id]
        if event_id not in current_events:
            findings.append((
                "REDUCTION-DETECTED",
                f"event {event_id} is missing; {len(frozen['depends_on'])} frozen dependency edge(s) gone",
            ))
            continue
        current = current_events[event_id]
        frozen_deps = set(frozen["depends_on"])
        current_deps = set(current["depends_on"])
        lost = sorted(frozen_deps - current_deps)
        gained = sorted(current_deps - frozen_deps)
        if lost:
            findings.append(("REDUCTION-DETECTED", f"event {event_id} lost depends_on {lost}"))
        if gained:
            findings.append(("ADDITION-DETECTED", f"event {event_id} gained depends_on {gained}"))
        for key in sorted(frozen["endpoint"]):
            before = frozen["endpoint"][key]
            after = current["endpoint"].get(key)
            if before != after:
                findings.append(("ENDPOINT-CHANGE", f"event {event_id}.{key}: {before!r} -> {after!r}"))
    for event_id in sorted(set(current_events) - set(frozen_events)):
        deps = current_events[event_id]["depends_on"]
        if deps:
            findings.append(("ADDITION-DETECTED", f"unpinned event {event_id} introduces depends_on {deps}"))
    frozen_rel = Counter(tuple(triple) for triple in pin["relations"])
    current_rel = Counter(tuple(triple) for triple in observed["relations"])
    lost_rel = frozen_rel - current_rel
    gained_rel = current_rel - frozen_rel
    if lost_rel and gained_rel:
        findings.append(("ENDPOINT-CHANGE",
                         f"relation endpoints changed: removed {format_triples(lost_rel)}; "
                         f"added {format_triples(gained_rel)}"))
    elif lost_rel:
        findings.append(("REDUCTION-DETECTED", f"relation edge(s) removed: {format_triples(lost_rel)}"))
    elif gained_rel:
        findings.append(("ADDITION-DETECTED", f"relation edge(s) added: {format_triples(gained_rel)}"))
    return findings


def read_contract():
    if not CONTRACT_PATH.is_file():
        fail("CONTRACT-INVALID", f"contract not found: {CONTRACT_RELPATH}")
    try:
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        fail("CONTRACT-INVALID", f"{CONTRACT_RELPATH}: {error}")
    if not isinstance(contract, dict) or not isinstance(contract.get("pins"), dict):
        fail("CONTRACT-INVALID", "contract root must be an object with a pins object")
    return contract


def validate_pin(name, pin):
    if not isinstance(pin, dict):
        fail("CONTRACT-INVALID", f"pin {name} must be an object")
    if not isinstance(pin.get("content_sha256"), str) or SHA256.fullmatch(pin["content_sha256"]) is None:
        fail("CONTRACT-INVALID", f"pin {name} needs a sha256 content digest")
    files = pin.get("files")
    if not isinstance(files, dict) or not files or any(
            not isinstance(value, str) or SHA256.fullmatch(value) is None for value in files.values()):
        fail("CONTRACT-INVALID", f"pin {name} needs per-file sha256 digests")
    events = pin.get("events")
    if not isinstance(events, dict):
        fail("CONTRACT-INVALID", f"pin {name} needs an events object")
    for event_id, entry in events.items():
        if (not isinstance(event_id, str) or not event_id or not isinstance(entry, dict)
                or not isinstance(entry.get("depends_on"), list)
                or any(not isinstance(dep, str) for dep in entry["depends_on"])
                or not isinstance(entry.get("endpoint"), dict)):
            fail("CONTRACT-INVALID", f"pin {name} has an invalid event entry for {event_id!r}")
    relations = pin.get("relations")
    if not isinstance(relations, list) or any(
            not isinstance(triple, list) or len(triple) != 3
            or any(not isinstance(item, str) for item in triple) for triple in relations):
        fail("CONTRACT-INVALID", f"pin {name} needs relation endpoint triples")


def pin_for(fixture, contract):
    name = fixture.resolve().name
    pins = contract["pins"]
    if name not in pins:
        fail("UNPINNED-FIXTURE", f"no pin for {name!r} in {CONTRACT_RELPATH} (pinned: {sorted(pins)})")
    validate_pin(name, pins[name])
    return name, pins[name]


def verify(fixture, contract):
    name, pin = pin_for(fixture, contract)
    observed = build_model(fixture)
    findings = compare(pin, observed)
    counts = pin.get("counts") if isinstance(pin.get("counts"), dict) else {}
    observed_counts = observed["counts"]
    receipt = (
        f"FREEZE {name}: events {observed_counts['events']}/{counts.get('events', '?')}; "
        f"dependency-edges {observed_counts['dependency_edges']}/{counts.get('dependency_edges', '?')}; "
        f"relations {observed_counts['relations']}/{counts.get('relations', '?')}"
    )
    if findings:
        print(receipt)
        emit(1, findings)
        return 1
    if observed["content_sha256"] != pin["content_sha256"]:
        print(receipt)
        emit(2, [("DIGEST-MISMATCH",
                  f"content digest {observed['content_sha256']} != pin {pin['content_sha256']}; "
                  "fixture bytes changed outside the frozen inventory")])
        return 2
    print(receipt)
    print(f"DIGEST {observed['content_sha256']}")
    print(f"RESULT {RESULTS[0]}")
    return 0


def freeze(fixture, contract):
    observed = build_model(fixture)
    name = fixture.resolve().name
    revision = "unversioned"
    try:
        result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            revision = result.stdout.strip()
    except OSError:
        pass
    try:
        fixture_label = str(fixture.resolve().relative_to(ROOT))
    except ValueError:
        fixture_label = str(fixture.resolve())
    pin = {
        "fixture": fixture_label,
        "revision": revision,
        "content_sha256": observed["content_sha256"],
        "files": observed["files"],
        "events": observed["events"],
        "relations": observed["relations"],
        "counts": observed["counts"],
    }
    contract["pins"][name] = pin
    contract["revision"] = revision
    CONTRACT_PATH.write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"FROZEN {name}: events {observed['counts']['events']}; "
          f"dependency-edges {observed['counts']['dependency_edges']}; "
          f"relations {observed['counts']['relations']}")
    print(f"DIGEST {observed['content_sha256']}")
    verify(fixture, read_contract())
    return 0


def self_test_cases(workdir, base):
    cases = {}

    def copy_case(name):
        target = workdir / name / base.name
        shutil.copytree(base, target)
        return target

    cases["clean"] = (lambda p=base: [p], 0)
    scratch = copy_case("reduction_edge_drop")
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "paired-crossing-decision":
            record["depends_on"] = [dep for dep in record["depends_on"] if dep != "evin-ninth-bell"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["reduction_edge_drop"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("addition_edge_phantom")
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "aftermath-missing-evin":
            record["depends_on"] = record["depends_on"] + ["phantom-ninth-bell"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["addition_edge_phantom"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("event_removed")
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    timeline = [record for record in timeline if record["id"] != "aftermath-missing-evin"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["event_removed"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("event_endpoint_change")
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "paired-crossing-decision":
            record["place_id"] = "salt-court"
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["event_endpoint_change"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("relation_endpoint_flip")
    relations = json.loads((scratch / "relations.json").read_text(encoding="utf-8"))
    relations[0]["from"], relations[0]["to"] = relations[0]["to"], relations[0]["from"]
    (scratch / "relations.json").write_text(json.dumps(relations, indent=2) + "\n", encoding="utf-8")
    cases["relation_endpoint_flip"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("relation_removed")
    (scratch / "relations.json").write_text("[]\n", encoding="utf-8")
    cases["relation_removed"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("relation_added")
    relations = json.loads((scratch / "relations.json").read_text(encoding="utf-8"))
    relations.append({"from": "aru", "to": "jorin", "type": "unpinned_relation"})
    (scratch / "relations.json").write_text(json.dumps(relations, indent=2) + "\n", encoding="utf-8")
    cases["relation_added"] = (lambda p=scratch: [p], 1)

    scratch = copy_case("digest_tamper")
    timeline_text = (scratch / "timeline.json").read_text(encoding="utf-8")
    (scratch / "timeline.json").write_text(
        timeline_text.replace("south bell at Salt Court", "South bell at Salt Court", 1), encoding="utf-8")
    cases["digest_tamper"] = (lambda p=scratch: [p], 2)

    scratch = copy_case("malformed_json")
    (scratch / "timeline.json").write_text("[{\n", encoding="utf-8")
    cases["malformed_json"] = (lambda p=scratch: [p], 2)

    scratch = copy_case("missing_timeline")
    (scratch / "timeline.json").unlink()
    cases["missing_timeline"] = (lambda p=scratch: [p], 2)

    unpinned = workdir / "unpinned_fixture"
    shutil.copytree(base, unpinned)
    cases["unpinned_fixture"] = (lambda p=unpinned: [p], 2)
    cases["missing_fixture"] = (lambda p=workdir / "missing_case" / base.name: [p], 2)
    cases["invalid_arguments"] = (lambda p=base: [p, "--freeze", str(p)], 2)
    return cases


def run_self_test():
    contract = read_contract()
    expected = contract.get("self_test", {}).get("expected") if isinstance(contract.get("self_test"), dict) else None
    if not isinstance(expected, dict):
        fail("CONTRACT-INVALID", "self_test.expected must be an object")
    missing = sorted(set(FROZEN_CASES) - set(expected))
    extra = sorted(set(expected) - set(FROZEN_CASES))
    if missing or extra:
        fail("CONTRACT-INVALID", f"self-test expectation set mismatch; missing={missing} extra={extra}")
    base = ROOT / "corpus/fixtures" / SELF_TEST_BASE
    if not base.is_dir():
        fail("FIXTURE-MISSING", f"self-test base fixture not found: {base}")
    failures = []
    with tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-") as tmp:
        cases = self_test_cases(Path(tmp), base)
        for case in FROZEN_CASES:
            argv, expected_exit = cases[case]
            paths = [str(item) for item in argv()]
            command = [sys.executable, str(Path(__file__).resolve()), *paths]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            output = result.stdout + result.stderr
            observed_findings = sorted(
                line.split(":", 1)[0].split(" ", 1)[1] for line in result.stdout.splitlines()
                if line.startswith("FINDING "))
            want = expected[case]
            want_exit = want.get("exit")
            want_findings = sorted(want.get("finding_ids", []))
            ok = (result.returncode == expected_exit == want_exit
                  and observed_findings == want_findings
                  and (not want.get("forbid_traceback") or "Traceback" not in output))
            print(f"CASE {case}: exit={result.returncode} expected={want_exit} "
                  f"findings={observed_findings} {'ok' if ok else 'MISMATCH'}")
            if not ok:
                failures.append(case)
                print(f"  observed stdout: {result.stdout.strip().splitlines()}")
                if result.stderr.strip():
                    print(f"  observed stderr: {result.stderr.strip().splitlines()}")
    total = len(FROZEN_CASES)
    passed = total - len(failures)
    print(f"SELF-TEST {passed}/{total}")
    if failures:
        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
        return 1
    print(f"RESULT {RESULTS[0]}")
    return 0


def main(argv=None):
    parser = CliParser(prog="dependency_freeze.py", add_help=True,
                       description="Freeze or verify per-fixture dependency inventories.")
    parser.add_argument("fixture", nargs="?", help="fixture directory to verify against its pin")
    parser.add_argument("--freeze", metavar="DIR", help="(re)build the pin for DIR (delivery-time only)")
    parser.add_argument("--self-test", action="store_true", help="run isolated cases against persisted expectations")
    try:
        args = parser.parse_args(argv)
        if args.self_test and (args.fixture or args.freeze):
            fail("INVALID-ARGUMENTS", "--self-test cannot be combined with a fixture or --freeze")
        if args.freeze and args.fixture:
            fail("INVALID-ARGUMENTS", "pass either a fixture (verify) or --freeze DIR, not both")
        if args.self_test:
            return run_self_test()
        if args.freeze:
            return freeze(Path(args.freeze), read_contract())
        if not args.fixture:
            fail("INVALID-ARGUMENTS", "expected a fixture directory, --freeze DIR, or --self-test")
        return verify(Path(args.fixture), read_contract())
    except ToolError as error:
        emit(2, [(error.finding_id, error.detail)])
        return 2


if __name__ == "__main__":
    sys.exit(main())
