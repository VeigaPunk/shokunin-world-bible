#!/usr/bin/env python3
"""Freeze and verify per-fixture dependency inventories for the crossing chain.

BR-01 class: a dropped `depends_on` edge or a changed relation endpoint leaves
every current gate green. This tool pins, for each delivered continuation-chain
fixture, the event dependency-edge inventory (event id -> sorted `depends_on`
set), the event endpoints (tick, entity_id, place_id), the relation endpoint
triples (from, to, type), and the fixture's content digests. Verification
compares the current fixture against the pin; the semantic inventory decides
first, and a content change the inventory does not model is reported as
could-not-evaluate.

Round-97 hardening: `--freeze` is scope-guarded to `corpus/fixtures/**`
(`SCOPE-REFUSED`), each pin names the fixture's repo-relative path and
verification refuses every other path (`PATH-MISMATCH`) so a same-named copy at
a foreign path can no longer produce a green receipt, and `DIGEST-MISMATCH`
names the changed file.

Round-98 hardening: `SELF-TEST-MISMATCH` exits 2 (the could-not-evaluate class,
matching `map_obligations.py`) and is pinned as self-test case
`self_test_mismatch` (16 -> 17 cases); `--freeze` migrates a path-less legacy
pin in place (the same-named-elsewhere refusal stays); the contract's
`precedence` text names the full exit-2 check order and finding IDs.

Round-99 hardening: the pin payload covers all ten declared fixture files
(five JSON tables plus README, claim-excerpt-map, fictional-excerpts,
inspiration-note, and source-excerpt), not the five JSON tables alone, so an
edit to any pinned file — including dependency wording in an excerpt — exits 2
`DIGEST-MISMATCH` naming that file. The payload carries a schema version;
self-test case `markdown_tamper` pins the Markdown-tamper detection (17 -> 18).
"""

import argparse
import hashlib
import json
import os
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
FIXTURE_SCOPE = ROOT / "corpus/fixtures"
FIXTURE_SCOPE_RELPATH = "corpus/fixtures"
DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")
MARKDOWN_FILES = (
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)
PINNED_FILES = DATA_FILES + MARKDOWN_FILES
PAYLOAD_SCHEMA_VERSION = 2
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
    "scope_refused",
    "path_mismatch",
    "self_test_mismatch",
    "markdown_tamper",
)
SELF_TEST_BASE = "r95-crossing-aftermath"
SELF_TEST_CHILD_ENV = "DEPENDENCY_FREEZE_SELF_TEST_CHILD"


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


def read_bytes(path, label):
    try:
        return path.read_bytes()
    except OSError as error:
        fail("FILE-MISSING", f"{label} is unreadable: {error}")


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
    for name in MARKDOWN_FILES:
        candidate = fixture / name
        if candidate.is_file():
            files[name] = read_bytes(candidate, name)
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
        "payload_schema_version": PAYLOAD_SCHEMA_VERSION,
        "pinned_files": list(PINNED_FILES),
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


def repo_relpath(path):
    try:
        return path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return None


def scope_guard(target):
    scope = FIXTURE_SCOPE.resolve()
    try:
        relative = target.resolve().relative_to(scope)
    except ValueError:
        fail("SCOPE-REFUSED",
             f"--freeze refuses {target} (resolves to {target.resolve()}); "
             f"the frozen scope is {FIXTURE_SCOPE_RELPATH}/** (integration-time operation only)")
    if not relative.parts:
        fail("SCOPE-REFUSED",
             f"--freeze refuses {FIXTURE_SCOPE_RELPATH} itself; the frozen scope is {FIXTURE_SCOPE_RELPATH}/**")


def validate_pin(name, pin):
    if not isinstance(pin, dict):
        fail("CONTRACT-INVALID", f"pin {name} must be an object")
    relpath = pin.get("fixture")
    if not isinstance(relpath, str) or not relpath or Path(relpath).is_absolute():
        fail("CONTRACT-INVALID", f"pin {name} needs a repo-relative fixture path")
    try:
        inside = (ROOT / relpath).resolve().relative_to(FIXTURE_SCOPE.resolve())
    except ValueError:
        inside = None
    if inside is None or not inside.parts:
        fail("CONTRACT-INVALID", f"pin {name} names {relpath}, outside {FIXTURE_SCOPE_RELPATH}/**")
    if pin.get("payload_schema_version") != PAYLOAD_SCHEMA_VERSION:
        fail("CONTRACT-INVALID",
             f"pin {name} payload_schema_version {pin.get('payload_schema_version')!r} "
             f"!= {PAYLOAD_SCHEMA_VERSION} (full-file pin of {len(PINNED_FILES)} files)")
    if pin.get("pinned_files") != list(PINNED_FILES):
        fail("CONTRACT-INVALID",
             f"pin {name} pinned_files {pin.get('pinned_files')!r} != {list(PINNED_FILES)}")
    if not isinstance(pin.get("content_sha256"), str) or SHA256.fullmatch(pin["content_sha256"]) is None:
        fail("CONTRACT-INVALID", f"pin {name} needs a sha256 content digest")
    files = pin.get("files")
    if (not isinstance(files, dict) or sorted(files) != sorted(PINNED_FILES)
            or any(not isinstance(value, str) or SHA256.fullmatch(value) is None for value in files.values())):
        fail("CONTRACT-INVALID",
             f"pin {name} needs sha256 digests for all {len(PINNED_FILES)} pinned files "
             f"({', '.join(PINNED_FILES)})")
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


def bind_path(fixture, name, pin):
    expected = (ROOT / pin["fixture"]).resolve()
    observed = fixture.resolve()
    if observed != expected:
        fail("PATH-MISMATCH",
             f"pin {name} names {pin['fixture']} (resolves to {expected}); "
             f"invoked fixture resolves to {observed}")


def pin_for(fixture, contract):
    name = fixture.resolve().name
    pins = contract["pins"]
    if name not in pins:
        fail("UNPINNED-FIXTURE", f"no pin for {name!r} in {CONTRACT_RELPATH} (pinned: {sorted(pins)})")
    validate_pin(name, pins[name])
    return name, pins[name]


def changed_files(pin, observed):
    changes = []
    for name in sorted(set(pin["files"]) | set(observed["files"])):
        before = pin["files"].get(name)
        after = observed["files"].get(name)
        if before != after:
            changes.append(f"{name} (sha256 {before} -> {after})")
    if not changes:
        changes.append("(no per-file digest difference; the pin's file digests disagree with its content digest)")
    return ", ".join(changes)


def verify(fixture, contract):
    name, pin = pin_for(fixture, contract)
    if not fixture.is_dir():
        fail("FIXTURE-MISSING", f"fixture directory not found: {fixture}")
    bind_path(fixture, name, pin)
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
    missing_pinned = [name for name in PINNED_FILES if name not in observed["files"]]
    if missing_pinned:
        print(receipt)
        emit(2, [("FILE-MISSING",
                  f"pinned file(s) missing from {fixture}: {', '.join(missing_pinned)}")])
        return 2
    if observed["content_sha256"] != pin["content_sha256"]:
        print(receipt)
        emit(2, [("DIGEST-MISMATCH",
                  f"content digest {observed['content_sha256']} != pin {pin['content_sha256']}; "
                  f"changed: {changed_files(pin, observed)}; "
                  "fixture bytes changed outside the frozen inventory")])
        return 2
    print(receipt)
    print(f"DIGEST {observed['content_sha256']}")
    print(f"RESULT {RESULTS[0]}")
    return 0


def freeze(target, contract):
    scope_guard(target)
    observed = build_model(target)
    resolved = target.resolve()
    label = repo_relpath(resolved)
    fixture_label = str(label) if label is not None else str(resolved)
    name = resolved.name
    existing = contract["pins"].get(name)
    if isinstance(existing, dict):
        recorded = existing.get("fixture")
        if isinstance(recorded, str) and recorded:
            if recorded != fixture_label:
                fail("SCOPE-REFUSED",
                     f"--freeze refuses {fixture_label}: pin {name} already names {recorded!r}; "
                     "freezing a same-named path elsewhere would rewrite the delivered pin")
        else:
            print(f"MIGRATED {name}: path-less legacy pin now names {fixture_label}")
    revision = "unversioned"
    try:
        result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            revision = result.stdout.strip()
    except OSError:
        pass
    missing_pinned = [name for name in PINNED_FILES if name not in observed["files"]]
    if missing_pinned:
        fail("FILE-MISSING",
             f"--freeze refuses {fixture_label}: pinned file(s) missing: {', '.join(missing_pinned)}")
    pin = {
        "fixture": fixture_label,
        "revision": revision,
        "payload_schema_version": PAYLOAD_SCHEMA_VERSION,
        "pinned_files": list(PINNED_FILES),
        "content_sha256": observed["content_sha256"],
        "files": observed["files"],
        "events": observed["events"],
        "relations": observed["relations"],
        "counts": observed["counts"],
    }
    validate_pin(name, pin)
    contract["pins"][name] = pin
    contract["revision"] = revision
    CONTRACT_PATH.write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"FROZEN {name}: events {observed['counts']['events']}; "
          f"dependency-edges {observed['counts']['dependency_edges']}; "
          f"relations {observed['counts']['relations']}")
    print(f"DIGEST {observed['content_sha256']}")
    return verify(target, read_contract())


def self_test_cases(workdir, base):
    cases = {}
    tool = Path(__file__).resolve()

    def mirror_root(case):
        root = workdir / case
        (root / "corpus/tools").mkdir(parents=True)
        (root / "corpus/fixtures").mkdir(parents=True)
        shutil.copy2(tool, root / "corpus/tools/dependency_freeze.py")
        shutil.copy2(CONTRACT_PATH, root / "corpus/tools/dependency-freeze-contract.json")
        return root

    def mirror_fixture(root, name=None):
        fixture = root / "corpus/fixtures" / (name or base.name)
        shutil.copytree(base, fixture)
        return fixture

    def mirror_tool(root):
        return root / "corpus/tools/dependency_freeze.py"

    def verify_argv(mirror, fixture):
        return lambda t=mirror, f=fixture: [str(t), str(f)]

    cases["clean"] = (lambda t=tool, f=base: [str(t), str(f)], 0)

    root = mirror_root("reduction_edge_drop")
    scratch = mirror_fixture(root)
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "paired-crossing-decision":
            record["depends_on"] = [dep for dep in record["depends_on"] if dep != "evin-ninth-bell"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["reduction_edge_drop"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("addition_edge_phantom")
    scratch = mirror_fixture(root)
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "aftermath-missing-evin":
            record["depends_on"] = record["depends_on"] + ["phantom-ninth-bell"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["addition_edge_phantom"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("event_removed")
    scratch = mirror_fixture(root)
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    timeline = [record for record in timeline if record["id"] != "aftermath-missing-evin"]
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["event_removed"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("event_endpoint_change")
    scratch = mirror_fixture(root)
    timeline = json.loads((scratch / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "paired-crossing-decision":
            record["place_id"] = "salt-court"
    (scratch / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    cases["event_endpoint_change"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("relation_endpoint_flip")
    scratch = mirror_fixture(root)
    relations = json.loads((scratch / "relations.json").read_text(encoding="utf-8"))
    relations[0]["from"], relations[0]["to"] = relations[0]["to"], relations[0]["from"]
    (scratch / "relations.json").write_text(json.dumps(relations, indent=2) + "\n", encoding="utf-8")
    cases["relation_endpoint_flip"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("relation_removed")
    scratch = mirror_fixture(root)
    (scratch / "relations.json").write_text("[]\n", encoding="utf-8")
    cases["relation_removed"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("relation_added")
    scratch = mirror_fixture(root)
    relations = json.loads((scratch / "relations.json").read_text(encoding="utf-8"))
    relations.append({"from": "aru", "to": "jorin", "type": "unpinned_relation"})
    (scratch / "relations.json").write_text(json.dumps(relations, indent=2) + "\n", encoding="utf-8")
    cases["relation_added"] = (verify_argv(mirror_tool(root), scratch), 1)

    root = mirror_root("digest_tamper")
    scratch = mirror_fixture(root)
    timeline_text = (scratch / "timeline.json").read_text(encoding="utf-8")
    (scratch / "timeline.json").write_text(
        timeline_text.replace("south bell at Salt Court", "South bell at Salt Court", 1), encoding="utf-8")
    cases["digest_tamper"] = (verify_argv(mirror_tool(root), scratch), 2)

    root = mirror_root("malformed_json")
    scratch = mirror_fixture(root)
    (scratch / "timeline.json").write_text("[{\n", encoding="utf-8")
    cases["malformed_json"] = (verify_argv(mirror_tool(root), scratch), 2)

    root = mirror_root("missing_timeline")
    scratch = mirror_fixture(root)
    (scratch / "timeline.json").unlink()
    cases["missing_timeline"] = (verify_argv(mirror_tool(root), scratch), 2)

    root = mirror_root("unpinned_fixture")
    unpinned = mirror_fixture(root, "unpinned_fixture")
    cases["unpinned_fixture"] = (verify_argv(mirror_tool(root), unpinned), 2)

    root = mirror_root("missing_fixture")
    cases["missing_fixture"] = (verify_argv(mirror_tool(root), root / "corpus/fixtures/missing_case" / base.name), 2)

    cases["invalid_arguments"] = (lambda t=tool, f=base: [str(t), str(f), "--freeze", str(f)], 2)

    foreign = workdir / "path_mismatch" / "foreign" / base.name
    shutil.copytree(base, foreign)
    cases["path_mismatch"] = (lambda t=tool, f=foreign: [str(t), str(f)], 2)

    target = workdir / "scope_refused" / "target"
    target.mkdir(parents=True)
    cases["scope_refused"] = (lambda t=tool, d=target: [str(t), "--freeze", str(d)], 2)

    root = mirror_root("self_test_mismatch")
    mirror_contract = root / "corpus/tools/dependency-freeze-contract.json"
    corrupted = json.loads(mirror_contract.read_text(encoding="utf-8"))
    corrupted["self_test"]["expected"]["clean"]["exit"] = 1
    mirror_contract.write_text(json.dumps(corrupted, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not os.environ.get(SELF_TEST_CHILD_ENV):
        mirror_fixture(root)
    # A nested replay of this case (marker set) gets the corrupted mirror without the base
    # fixture: that inner run fails closed on FIXTURE-MISSING before it can replay this
    # case, so the corruption cannot recurse without bound (the enclosing run is already
    # failing on the corrupted `clean` expectation either way).
    cases["self_test_mismatch"] = (lambda t=mirror_tool(root): [str(t), "--self-test"], 2)

    root = mirror_root("markdown_tamper")
    scratch = mirror_fixture(root)
    excerpt = scratch / "fictional-excerpts.md"
    excerpt.write_bytes(excerpt.read_bytes() + b"\n")
    cases["markdown_tamper"] = (verify_argv(mirror_tool(root), scratch), 2)
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
    with tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-", dir=ROOT) as tmp:
        cases = self_test_cases(Path(tmp), base)
        for case in FROZEN_CASES:
            argv, expected_exit = cases[case]
            command = [sys.executable, *argv()]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                    env={**os.environ, SELF_TEST_CHILD_ENV: "1"})
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
        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
        return 2
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
