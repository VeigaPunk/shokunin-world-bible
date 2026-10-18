#!/usr/bin/env python3
"""V08 accumulated negative battery for dependency_freeze. Scratch mirrors only."""

import hashlib
import json
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V08-scratch"
BASELINE_COMMIT = "4265df5e86e4121bde4125b649b89bb1676676a5"
SUBJECT = "r95-crossing-aftermath"
JSON_FILES = (
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
)
MD_FILES = (
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)
WORD = re.compile(r"[A-Za-z]{4,}")


def sha256_file(path):
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def findings(stdout):
    ids = []
    details = []
    for line in stdout.splitlines():
        if line.startswith("FINDING "):
            head, _, detail = line.partition(": ")
            ids.append(head.split(" ", 1)[1])
            details.append(detail)
    return ids, details


def quote_cmd(argv):
    return shlex.join(argv)


def invoke(argv, timeout=180):
    proc = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
    return proc.returncode, proc.stdout, proc.stderr


def make_mirror(dest, tool_src, contract_src, fixtures):
    if dest.exists():
        shutil.rmtree(dest)
    tools = dest / "corpus/tools"
    tools.mkdir(parents=True)
    shutil.copy2(tool_src, tools / "dependency_freeze.py")
    shutil.copy2(contract_src, tools / "dependency-freeze-contract.json")
    copied = []
    for rel, src in fixtures:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, target)
        copied.append(target)
    return dest, tools / "dependency_freeze.py", tools / "dependency-freeze-contract.json", copied


def subject_fixture(root):
    return root / "corpus/fixtures" / SUBJECT


def remove_prose_word(path):
    text = path.read_text(encoding="utf-8")
    match = WORD.search(text)
    if not match:
        path.write_text(text + "\nv08-tamper-token\n", encoding="utf-8")
        return "appended token (no 4-letter word)"
    path.write_text(text[: match.start()] + text[match.end() :], encoding="utf-8")
    return f"removed {match.group(0)!r} at offset {match.start()}"


def append_newline(path):
    path.write_bytes(path.read_bytes() + b"\n")
    return "appended trailing newline"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def mutate_edge_drop(fix):
    timeline = load_json(fix / "timeline.json")
    for record in timeline:
        deps = list(record.get("depends_on") or [])
        if deps:
            dropped = deps.pop()
            record["depends_on"] = deps
            dump_json(fix / "timeline.json", timeline)
            return f"dropped {dropped!r} from {record['id']}"
    raise RuntimeError("no depends_on edge to drop")


def mutate_event_removed(fix):
    timeline = load_json(fix / "timeline.json")
    for index, record in enumerate(timeline):
        if record.get("depends_on"):
            removed = timeline.pop(index)
            dump_json(fix / "timeline.json", timeline)
            return f"removed event {removed['id']}"
    raise RuntimeError("no event with depends_on")


def mutate_relation_removed(fix):
    relations = load_json(fix / "relations.json")
    if not relations:
        raise RuntimeError("relations.json already empty")
    dump_json(fix / "relations.json", [])
    return f"removed {len(relations)} relation(s)"


def mutate_edge_phantom(fix):
    timeline = load_json(fix / "timeline.json")
    record = timeline[0]
    deps = list(record.get("depends_on") or [])
    deps.append("phantom-v08-edge")
    record["depends_on"] = deps
    dump_json(fix / "timeline.json", timeline)
    return f"added phantom-v08-edge to {record['id']}"


def mutate_relation_added(fix):
    relations = load_json(fix / "relations.json")
    relations.append({"from": "v08-a", "to": "v08-b", "type": "v08_unpinned"})
    dump_json(fix / "relations.json", relations)
    return "added relation [v08-a, v08-b, v08_unpinned]"


def mutate_unpinned_event(fix):
    timeline = load_json(fix / "timeline.json")
    parent = timeline[0]["id"]
    timeline.append({
        "id": "v08-unpinned-event",
        "depends_on": [parent],
        "tick": 99,
        "entity_id": "v08",
        "place_id": "v08-place",
    })
    dump_json(fix / "timeline.json", timeline)
    return f"added v08-unpinned-event depends_on [{parent}]"


def mutate_endpoint(fix):
    timeline = load_json(fix / "timeline.json")
    record = timeline[0]
    before = record.get("place_id")
    record["place_id"] = "v08-other-place"
    dump_json(fix / "timeline.json", timeline)
    return f"event {record['id']}.place_id {before!r} -> 'v08-other-place'"


def mutate_relation_flip(fix):
    relations = load_json(fix / "relations.json")
    if not relations:
        raise RuntimeError("no relation to flip")
    record = relations[0]
    record["from"], record["to"] = record["to"], record["from"]
    dump_json(fix / "relations.json", relations)
    return f"flipped relation from/to on type {record.get('type')!r}"


def corrupt_clean_expectation(contract_path):
    data = json.loads(contract_path.read_text(encoding="utf-8"))
    data["self_test"]["expected"]["clean"]["exit"] = 1
    contract_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return "self_test.expected.clean.exit := 1"


def prepare_case(case_dir, tool_src, contract_src, fixture_src, mutate):
    root, tool, contract, copied = make_mirror(
        case_dir, tool_src, contract_src,
        [(f"corpus/fixtures/{SUBJECT}", fixture_src)],
    )
    fix = copied[0]
    note = mutate(root, tool, contract, fix) if mutate else "pristine"
    return root, tool, contract, fix, note


def run_twice(name, argv_builder, expect_exit, expect_ids, name_file, log, timeout=180):
    runs = []
    for index in (1, 2):
        argv = argv_builder()
        code, stdout, stderr = invoke(argv, timeout=timeout)
        ids, details = findings(stdout)
        runs.append({
            "index": index,
            "argv": argv,
            "cmd": quote_cmd(argv),
            "exit": code,
            "stdout": stdout,
            "stderr": stderr,
            "ids": ids,
            "details": details,
        })
    same_ids = runs[0]["ids"] == runs[1]["ids"] and runs[0]["exit"] == runs[1]["exit"]
    same_bytes = (
        runs[0]["stdout"] == runs[1]["stdout"] and runs[0]["stderr"] == runs[1]["stderr"]
    )
    named = True
    if name_file:
        named = all(name_file in detail for detail in runs[0]["details"]) and bool(runs[0]["details"])
    traceback = any("Traceback" in run["stderr"] or "Traceback" in run["stdout"] for run in runs)
    id_ok = runs[0]["ids"] == expect_ids and runs[0]["exit"] == expect_exit and named and not traceback
    status = "MATCH" if id_ok and same_ids else "MISMATCH"
    log.write(f"\n### {name} expect exit={expect_exit} ids={expect_ids} file={name_file}\n")
    log.write(f"mutation: {runs[0].get('note', '')}\n")
    for run in runs:
        log.write(f"$ {run['cmd']}\n")
        log.write(run["stdout"])
        if not run["stdout"].endswith("\n"):
            log.write("\n")
        if run["stderr"].strip():
            log.write("--- stderr ---\n")
            log.write(run["stderr"])
            if not run["stderr"].endswith("\n"):
                log.write("\n")
        log.write(f"EXIT={run['exit']}\n")
        log.write(f"FINDINGS={run['ids']}\n")
    log.write(
        f"STABILITY ids={'IDENTICAL' if same_ids else 'DIFF'} "
        f"stdio={'IDENTICAL' if same_bytes else 'DIFF'} "
        f"named={named} traceback={traceback} {status}\n"
    )
    return {
        "name": name,
        "status": status,
        "exit": runs[0]["exit"],
        "ids": runs[0]["ids"],
        "expect_exit": expect_exit,
        "expect_ids": expect_ids,
        "same_ids": same_ids,
        "same_bytes": same_bytes,
        "named": named,
        "traceback": traceback,
        "cmd": runs[0]["cmd"],
        "stdout": runs[0]["stdout"],
        "stderr": runs[0]["stderr"],
        "exit2": runs[1]["exit"],
        "ids2": runs[1]["ids"],
        "name_file": name_file,
    }


def git_archive_baseline(dest):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    archive = subprocess.run(
        ["git", "archive", BASELINE_COMMIT,
         "corpus/tools/dependency_freeze.py",
         "corpus/tools/dependency-freeze-contract.json",
         f"corpus/fixtures/{SUBJECT}"],
        cwd=LANE, capture_output=True,
    )
    if archive.returncode != 0:
        raise RuntimeError(archive.stderr.decode("utf-8", "replace"))
    extract = subprocess.run(["tar", "-x", "-C", str(dest)], input=archive.stdout, capture_output=True)
    if extract.returncode != 0:
        raise RuntimeError(extract.stderr.decode("utf-8", "replace"))
    return dest


def phase_before():
    out = SCRATCH / "before"
    out.mkdir(parents=True, exist_ok=True)
    mirror_src = git_archive_baseline(out / "tree")
    tool = mirror_src / "corpus/tools/dependency_freeze.py"
    contract = mirror_src / "corpus/tools/dependency-freeze-contract.json"
    fixture = mirror_src / "corpus/fixtures" / SUBJECT
    log_path = out / "log.txt"
    rows = []
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"baseline commit {BASELINE_COMMIT}\n")
        log.write(f"tool sha256 {sha256_file(tool)}\n")
        log.write(f"contract sha256 {sha256_file(contract)}\n")
        log.write(f"fixture {fixture}\n")

        def pristine():
            case = out / "cases" / "clean"
            root, tool_copy, _, _ = make_mirror(
                case, tool, contract, [(f"corpus/fixtures/{SUBJECT}", fixture)],
            )
            return [sys.executable, str(tool_copy), str(subject_fixture(root))]

        rows.append(run_twice(
            "before_clean", pristine, 0, [], None, log,
        ))
        for name in MD_FILES:
            def builder(filename=name):
                case = out / "cases" / f"md-{filename}"
                root, tool_copy, _, copied = make_mirror(
                    case, tool, contract, [(f"corpus/fixtures/{SUBJECT}", fixture)],
                )
                note = remove_prose_word(copied[0] / filename)
                builder.note = note
                return [sys.executable, str(tool_copy), str(copied[0])]

            row = run_twice(f"before_md_{name}", builder, 0, [], None, log)
            row["note"] = getattr(builder, "note", "")
            rows.append(row)
        def json_builder():
            case = out / "cases" / "json-timeline"
            root, tool_copy, _, copied = make_mirror(
                case, tool, contract, [(f"corpus/fixtures/{SUBJECT}", fixture)],
            )
            append_newline(copied[0] / "timeline.json")
            return [sys.executable, str(tool_copy), str(copied[0])]

        rows.append(run_twice(
            "before_json_timeline", json_builder, 2, ["DIGEST-MISMATCH"], "timeline.json", log,
        ))
    summary = {
        "tool": sha256_file(tool),
        "contract": sha256_file(contract),
        "rows": [{k: row[k] for k in (
            "name", "status", "exit", "ids", "expect_exit", "expect_ids",
            "same_ids", "same_bytes", "named", "traceback", "cmd",
        )} for row in rows],
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"BEFORE rows={len(rows)} mismatches={sum(r['status'] != 'MATCH' for r in rows)}")
    for row in rows:
        print(f"  {row['status']} {row['name']} exit={row['exit']} ids={row['ids']} stable={row['same_ids']}")
    return 0 if all(row["status"] == "MATCH" for row in rows) else 1


def snapshot_delivered(dest):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    tool = LANE / "corpus/tools/dependency_freeze.py"
    contract = LANE / "corpus/tools/dependency-freeze-contract.json"
    shutil.copy2(tool, dest / "dependency_freeze.py")
    shutil.copy2(contract, dest / "dependency-freeze-contract.json")
    data = json.loads(contract.read_text(encoding="utf-8"))
    fixtures = dest / "fixtures"
    fixtures.mkdir()
    copied = {}
    for name, pin in data.get("pins", {}).items():
        rel = pin.get("fixture")
        if not isinstance(rel, str):
            copied[name] = None
            continue
        src = LANE / rel
        if not src.is_dir():
            copied[name] = None
            continue
        target = fixtures / name
        shutil.copytree(src, target)
        copied[name] = {"rel": rel, "src": str(src), "snap": str(target)}
    meta = {
        "tool": sha256_file(dest / "dependency_freeze.py"),
        "contract": sha256_file(dest / "dependency-freeze-contract.json"),
        "schema_version": data.get("schema_version"),
        "payload_schema_version": data.get("payload_schema_version"),
        "pins": sorted(data.get("pins", {})),
        "fixtures": copied,
    }
    (dest / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return dest, meta


def phase_after():
    poll = (SCRATCH / "poll.log").read_text(encoding="utf-8")
    if "POLL_HIT" not in poll:
        print("REFUSING after-phase: poll.log has no POLL_HIT")
        return 3
    hit = next(line for line in poll.splitlines() if line.startswith("POLL_HIT"))
    out = SCRATCH / "after"
    out.mkdir(parents=True, exist_ok=True)
    snap, meta = snapshot_delivered(out / "snapshot")
    tool_src = snap / "dependency_freeze.py"
    contract_src = snap / "dependency-freeze-contract.json"
    subject_src = snap / "fixtures" / SUBJECT
    if not subject_src.is_dir():
        print(f"REFUSING: snapshot missing {SUBJECT}")
        return 3
    live_tool = sha256_file(LANE / "corpus/tools/dependency_freeze.py")
    live_contract = sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json")
    log_path = out / "log.txt"
    rows = []
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"POLL_HIT {hit}\n")
        log.write(f"snapshot tool {meta['tool']}\n")
        log.write(f"snapshot contract {meta['contract']}\n")
        log.write(f"live tool at snapshot {live_tool}\n")
        log.write(f"live contract at snapshot {live_contract}\n")
        log.write(f"schema_version {meta['schema_version']} payload {meta['payload_schema_version']}\n")
        log.write(f"pins {meta['pins']}\n")

        def mirror_verify(case_name, mutate=None, extra=None):
            def builder(case_name=case_name, mutate=mutate, extra=extra):
                case = out / "cases" / case_name
                root, tool, contract, copied = make_mirror(
                    case, tool_src, contract_src,
                    [(f"corpus/fixtures/{SUBJECT}", subject_src)],
                )
                fix = copied[0]
                note = mutate(fix) if mutate else "pristine"
                if extra:
                    extra(root, tool, contract, fix)
                    note = note + "; " + getattr(extra, "note", "extra")
                builder.note = note
                before = sha256_file(contract)
                argv = [sys.executable, str(tool), str(fix)]
                builder.contract_before = before
                builder.contract_path = contract
                return argv
            return builder

        def check_contract_untouched(builder, row):
            if not hasattr(builder, "contract_path"):
                return
            after = sha256_file(builder.contract_path)
            row["contract_unchanged"] = after == builder.contract_before

        # clean control
        builder = mirror_verify("clean")
        row = run_twice("clean", builder, 0, [], None, log)
        row["note"] = getattr(builder, "note", "")
        rows.append(row)

        semantic = [
            ("reduction_edge_drop", mutate_edge_drop, 1, ["REDUCTION-DETECTED"]),
            ("reduction_event_removed", mutate_event_removed, 1, ["REDUCTION-DETECTED"]),
            ("reduction_relation_removed", mutate_relation_removed, 1, ["REDUCTION-DETECTED"]),
            ("addition_edge_phantom", mutate_edge_phantom, 1, ["ADDITION-DETECTED"]),
            ("addition_relation_added", mutate_relation_added, 1, ["ADDITION-DETECTED"]),
            ("addition_unpinned_event", mutate_unpinned_event, 1, ["ADDITION-DETECTED"]),
            ("endpoint_event", mutate_endpoint, 1, ["ENDPOINT-CHANGE"]),
            ("endpoint_relation_flip", mutate_relation_flip, 1, ["ENDPOINT-CHANGE"]),
        ]
        for name, mutate, expect_exit, expect_ids in semantic:
            builder = mirror_verify(name, mutate)
            row = run_twice(name, builder, expect_exit, expect_ids, None, log)
            row["note"] = getattr(builder, "note", "")
            check_contract_untouched(builder, row)
            rows.append(row)

        def combined(fix):
            note = mutate_edge_drop(fix)
            append_newline(fix / "README.md")
            return note + "; README.md trailing newline"

        builder = mirror_verify("precedence_reduction_and_md", combined)
        row = run_twice(
            "precedence_reduction_and_md", builder, 1, ["REDUCTION-DETECTED"], None, log,
        )
        row["note"] = getattr(builder, "note", "")
        rows.append(row)

        for filename in JSON_FILES:
            def mutate(fix, filename=filename):
                append_newline(fix / filename)
                return f"trailing newline on {filename}"

            builder = mirror_verify(f"digest_json_{filename}", mutate)
            row = run_twice(
                f"digest_json_{filename}", builder, 2, ["DIGEST-MISMATCH"], filename, log,
            )
            row["note"] = getattr(builder, "note", "")
            rows.append(row)

        for filename in MD_FILES:
            def mutate(fix, filename=filename):
                return remove_prose_word(fix / filename)

            builder = mirror_verify(f"digest_md_{filename}", mutate)
            row = run_twice(
                f"digest_md_{filename}", builder, 2, ["DIGEST-MISMATCH"], filename, log,
            )
            row["note"] = getattr(builder, "note", "")
            rows.append(row)

        def missing_timeline(fix):
            (fix / "timeline.json").unlink()
            return "unlinked timeline.json"

        builder = mirror_verify("file_missing_timeline", missing_timeline)
        row = run_twice("file_missing_timeline", builder, 2, ["FILE-MISSING"], None, log)
        row["note"] = getattr(builder, "note", "")
        rows.append(row)

        def malformed(fix):
            (fix / "timeline.json").write_text("[{\n", encoding="utf-8")
            return "timeline.json truncated to '[{'"

        builder = mirror_verify("malformed_json", malformed)
        row = run_twice("malformed_json", builder, 2, ["MALFORMED-JSON"], None, log)
        row["note"] = getattr(builder, "note", "")
        rows.append(row)

        def malformed_utf8(fix):
            (fix / "timeline.json").write_bytes(b"\xff\xfe not-utf8")
            return "timeline.json non-UTF-8 bytes"

        builder = mirror_verify("malformed_json_utf8", malformed_utf8)
        row = run_twice("malformed_json_utf8", builder, 2, ["MALFORMED-JSON"], None, log)
        row["note"] = getattr(builder, "note", "")
        rows.append(row)

        def scope_outside():
            case = out / "cases" / "scope_refused_outside"
            root, tool, contract, _ = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            target = root / "outside-scope" / "target"
            target.mkdir(parents=True)
            before = sha256_file(contract)
            argv = [sys.executable, str(tool), "--freeze", str(target)]
            scope_outside.before = before
            scope_outside.contract = contract
            return argv

        row = run_twice("scope_refused_outside", scope_outside, 2, ["SCOPE-REFUSED"], None, log)
        row["contract_unchanged"] = sha256_file(scope_outside.contract) == scope_outside.before
        rows.append(row)

        def scope_root():
            case = out / "cases" / "scope_refused_root"
            root, tool, contract, _ = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            before = sha256_file(contract)
            argv = [sys.executable, str(tool), "--freeze", str(root / "corpus/fixtures")]
            scope_root.before = before
            scope_root.contract = contract
            return argv

        row = run_twice("scope_refused_root", scope_root, 2, ["SCOPE-REFUSED"], None, log)
        row["contract_unchanged"] = sha256_file(scope_root.contract) == scope_root.before
        rows.append(row)

        def scope_same_name():
            case = out / "cases" / "scope_refused_same_name"
            root, tool, contract, copied = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            foreign = root / "corpus/fixtures/nested" / SUBJECT
            shutil.copytree(copied[0], foreign)
            before = sha256_file(contract)
            argv = [sys.executable, str(tool), "--freeze", str(foreign)]
            scope_same_name.before = before
            scope_same_name.contract = contract
            return argv

        row = run_twice("scope_refused_same_name", scope_same_name, 2, ["SCOPE-REFUSED"], None, log)
        row["contract_unchanged"] = sha256_file(scope_same_name.contract) == scope_same_name.before
        rows.append(row)

        def path_mismatch():
            case = out / "cases" / "path_mismatch"
            root, tool, contract, copied = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            foreign = root / "foreign" / SUBJECT
            foreign.parent.mkdir(parents=True)
            shutil.copytree(copied[0], foreign)
            return [sys.executable, str(tool), str(foreign)]

        rows.append(run_twice("path_mismatch", path_mismatch, 2, ["PATH-MISMATCH"], None, log))

        def invalid_none():
            case = out / "cases" / "invalid_none"
            root, tool, _, _ = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            return [sys.executable, str(tool)]

        rows.append(run_twice("invalid_arguments_none", invalid_none, 2, ["INVALID-ARGUMENTS"], None, log))

        def invalid_both():
            case = out / "cases" / "invalid_both"
            root, tool, _, copied = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            return [sys.executable, str(tool), str(copied[0]), "--freeze", str(copied[0])]

        rows.append(run_twice("invalid_arguments_both", invalid_both, 2, ["INVALID-ARGUMENTS"], None, log))

        def invalid_selftest():
            case = out / "cases" / "invalid_selftest"
            root, tool, _, copied = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            return [sys.executable, str(tool), "--self-test", str(copied[0])]

        rows.append(run_twice(
            "invalid_arguments_selftest", invalid_selftest, 2, ["INVALID-ARGUMENTS"], None, log,
        ))

        def self_test_mismatch():
            case = out / "cases" / "self_test_mismatch"
            root, tool, contract, _ = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            note = corrupt_clean_expectation(contract)
            self_test_mismatch.note = note
            return [sys.executable, str(tool), "--self-test"]

        row = run_twice(
            "self_test_mismatch", self_test_mismatch, 2, ["SELF-TEST-MISMATCH"], None, log,
            timeout=240,
        )
        row["note"] = getattr(self_test_mismatch, "note", "")
        rows.append(row)

        # extra: --freeze canonical path with README removed
        def freeze_missing_md():
            case = out / "cases" / "freeze_missing_readme"
            root, tool, contract, copied = make_mirror(
                case, tool_src, contract_src,
                [(f"corpus/fixtures/{SUBJECT}", subject_src)],
            )
            (copied[0] / "README.md").unlink()
            before = sha256_file(contract)
            freeze_missing_md.before = before
            freeze_missing_md.contract = contract
            return [sys.executable, str(tool), "--freeze", str(copied[0])]

        row = run_twice("freeze_missing_readme", freeze_missing_md, 2, ["FILE-MISSING"], "README.md", log)
        row["contract_unchanged"] = sha256_file(freeze_missing_md.contract) == freeze_missing_md.before
        row["extra"] = True
        rows.append(row)

        # sweep other pinned fixtures: each markdown wording removal, twice
        for pin_name, info in meta["fixtures"].items():
            if pin_name == SUBJECT or not info:
                log.write(f"\n### sweep skip {pin_name} info={info}\n")
                continue
            pin_src = Path(info["snap"])
            rel = info["rel"]
            for filename in MD_FILES:
                if not (pin_src / filename).is_file():
                    log.write(f"\n### sweep {pin_name} {filename} ABSENT from fixture\n")
                    continue

                def sweep(pin_name=pin_name, filename=filename, pin_src=pin_src, rel=rel):
                    case = out / "cases" / f"sweep-{pin_name}-{filename}"
                    root, tool, _, copied = make_mirror(
                        case, tool_src, contract_src, [(rel, pin_src)],
                    )
                    note = remove_prose_word(copied[0] / filename)
                    sweep.note = note
                    return [sys.executable, str(tool), str(copied[0])]

                row = run_twice(
                    f"sweep_{pin_name}_{filename}", sweep, 2, ["DIGEST-MISMATCH"], filename, log,
                )
                row["note"] = getattr(sweep, "note", "")
                row["extra"] = True
                rows.append(row)

        end_tool = sha256_file(LANE / "corpus/tools/dependency_freeze.py")
        end_contract = sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json")
        log.write(f"\nLIVE_END tool {end_tool} contract {end_contract}\n")
        log.write(f"DRIFT tool={end_tool != meta['tool']} contract={end_contract != meta['contract']}\n")
        residue = sorted(p.name for p in LANE.glob("dependency-freeze-self-test-*"))
        log.write(f"LANE_SELF_TEST_RESIDUE {residue}\n")

    required = [row for row in rows if not row.get("extra")]
    failed = [row for row in required if row["status"] != "MATCH" or not row["same_ids"]]
    summary = {
        "hit": hit,
        "tool": meta["tool"],
        "contract": meta["contract"],
        "schema_version": meta["schema_version"],
        "payload_schema_version": meta["payload_schema_version"],
        "pins": meta["pins"],
        "live_end_tool": sha256_file(LANE / "corpus/tools/dependency_freeze.py"),
        "live_end_contract": sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json"),
        "rows": [{
            "name": row["name"],
            "status": row["status"],
            "exit": row["exit"],
            "ids": row["ids"],
            "expect_exit": row["expect_exit"],
            "expect_ids": row["expect_ids"],
            "same_ids": row["same_ids"],
            "same_bytes": row["same_bytes"],
            "named": row["named"],
            "traceback": row["traceback"],
            "cmd": row["cmd"],
            "stdout": row["stdout"],
            "stderr": row["stderr"],
            "note": row.get("note", ""),
            "extra": row.get("extra", False),
            "contract_unchanged": row.get("contract_unchanged"),
        } for row in rows],
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"AFTER required={len(required)} failed={len(failed)} extras={len(rows) - len(required)}")
    for row in rows:
        mark = "EXTRA" if row.get("extra") else row["status"]
        print(
            f"  {mark} {row['name']} exit={row['exit']} ids={row['ids']} "
            f"stable={row['same_ids']} bytes={row['same_bytes']} named={row['named']}"
        )
    return 0 if not failed else 1


def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else "before"
    if phase == "before":
        return phase_before()
    if phase == "after":
        return phase_after()
    print(f"unknown phase {phase}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
