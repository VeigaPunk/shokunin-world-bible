#!/usr/bin/env python3
"""V118 c1-negative-3: live exit-2 matrix vs precedence text.

Mutates only this seat's scratch. Delivered tool/contract are copied, never written.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V118-scratch"
SNAP = SCRATCH / "snap"
CASES = SCRATCH / "cases"
LOG = SCRATCH / "matrix.log"
PY = sys.executable
R95 = "r95-crossing-aftermath"
PINNED = [
    "entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json",
    "README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md",
    "source-excerpt.md",
]
EXIT2 = [
    "UNPINNED-FIXTURE", "CONTRACT-INVALID", "FIXTURE-MISSING", "PATH-MISMATCH",
    "FILE-MISSING", "MALFORMED-JSON", "MALFORMED-MODEL", "DIGEST-MISMATCH",
    "INVALID-ARGUMENTS", "SELF-TEST-MISMATCH", "SCOPE-REFUSED",
]
EXIT1 = ["REDUCTION-DETECTED", "ADDITION-DETECTED", "ENDPOINT-CHANGE"]
ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b")

rows = []
logf = open(LOG, "w", encoding="utf-8")


def emit_log(text):
    print(text, flush=True)
    logf.write(text + "\n")
    logf.flush()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(tool, args):
    cmd = [PY, str(tool), *args]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr, cmd


def parse(stdout):
    findings = []
    lines = []
    result = ""
    for line in stdout.splitlines():
        if line.startswith("FINDING "):
            lines.append(line)
            findings.append(line.split(":", 1)[0].split(" ", 1)[1])
        elif line.startswith("RESULT "):
            result = line
    return findings, lines, result


def record(label, code, stdout, stderr, cmd, want_exit, want_ids, absent=(), contains=(), note=""):
    findings, lines, result = parse(stdout)
    ok = code == want_exit and all(i in findings for i in want_ids) and all(i not in findings for i in absent)
    for needle in contains:
        if needle not in stdout:
            ok = False
    status = "PASS" if ok else "FAIL"
    rows.append({
        "label": label, "status": status, "exit": code, "want_exit": want_exit,
        "findings": findings, "want_ids": list(want_ids), "result": result, "note": note,
    })
    emit_log(f"\n### {label}  [{status}]")
    emit_log("$ " + " ".join(cmd))
    emit_log(f"EXIT={code} want={want_exit} findings={findings} result={result}")
    if note:
        emit_log(f"NOTE {note}")
    if stdout.strip():
        emit_log("--- stdout ---")
        emit_log(stdout.rstrip())
    if stderr.strip():
        emit_log("--- stderr ---")
        emit_log(stderr.rstrip())
    return ok


def new_case(label):
    dest = CASES / label
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SNAP, dest)
    return dest


def tool_of(dest):
    return dest / "corpus/tools/dependency_freeze.py"


def contract_of(dest):
    return dest / "corpus/tools/dependency-freeze-contract.json"


def fx_of(dest, name=R95):
    return dest / "corpus/fixtures" / name


def load_contract(dest):
    return json.loads(contract_of(dest).read_text(encoding="utf-8"))


def dump_contract(dest, contract):
    contract_of(dest).write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def invoke(dest, args, label, want_exit, want_ids, absent=(), contains=(), note=""):
    code, out, err, cmd = run(tool_of(dest), args)
    record(label, code, out, err, cmd, want_exit, want_ids, absent, contains, note)
    return code, out


def main():
    if CASES.exists():
        shutil.rmtree(CASES)
    if SNAP.exists():
        shutil.rmtree(SNAP)
    SNAP.mkdir(parents=True)
    (SNAP / "corpus/tools").mkdir(parents=True)
    (SNAP / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", SNAP / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json", SNAP / "corpus/tools/dependency-freeze-contract.json")
    contract = json.loads((SNAP / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    for name in sorted(contract["pins"]):
        src = LANE / "corpus/fixtures" / name
        if src.is_dir():
            shutil.copytree(src, SNAP / "corpus/fixtures" / name)
    tool_sha = sha256(LANE / "corpus/tools/dependency_freeze.py")
    ct_sha = sha256(LANE / "corpus/tools/dependency-freeze-contract.json")
    emit_log(f"SNAPSHOT tool={tool_sha}")
    emit_log(f"SNAPSHOT contract={ct_sha}")
    emit_log(f"SNAPSHOT pins={sorted(contract['pins'])}")
    emit_log(f"SNAPSHOT schema={contract.get('schema_version')} payload={contract.get('payload_schema_version')}")
    precedence = contract.get("precedence", "")
    emit_log("PRECEDENCE " + precedence)
    parsed_ids = ID_RE.findall(precedence)
    emit_log(f"PRECEDENCE_IDS {parsed_ids}")
    missing_from_text = [i for i in EXIT2 + EXIT1 if i not in parsed_ids]
    extra_in_text = [i for i in parsed_ids if i not in EXIT2 + EXIT1]
    emit_log(f"PRECEDENCE_MISSING_FROM_TEXT {missing_from_text}")
    emit_log(f"PRECEDENCE_EXTRA_IDS {extra_in_text}")

    tool_src = (SNAP / "corpus/tools/dependency_freeze.py").read_text(encoding="utf-8")
    code_ids = sorted(set(re.findall(r'fail\("([A-Z0-9-]+)"', tool_src) + re.findall(r'\("([A-Z0-9-]+)"', tool_src)))
    # tighten to known-looking finding literals actually passed to fail/emit
    code_fail = sorted(set(re.findall(r'(?:fail|emit)\(\s*\d*\s*,?\s*\[?\("([A-Z0-9-]+)"', tool_src)))
    code_fail2 = sorted(set(re.findall(r'fail\("([A-Z0-9-]+)"', tool_src)))
    code_tuple = sorted(set(re.findall(r'\("([A-Z][A-Z0-9-]+)"', tool_src)))
    emit_log(f"CODE_FAIL_IDS {code_fail2}")
    emit_log(f"CODE_TUPLE_IDS {code_tuple}")
    emit_log(f"names_file referenced in runner: {'names_file' in tool_src}")

    expected = contract["self_test"]["expected"]
    emit_log(f"SELF_TEST_CASES {len(expected)} {sorted(expected)}")
    selftest_ids = sorted({i for spec in expected.values() for i in spec.get("finding_ids", [])})
    emit_log(f"SELF_TEST_FINDING_IDS {selftest_ids}")
    emit_log(f"SELF_TEST_EXIT2_NOT_PINNED {[i for i in EXIT2 if i not in selftest_ids]}")

    for doc in ("corpus/tools/README.md", "SKILL.md"):
        text = (LANE / doc).read_text(encoding="utf-8", errors="replace")
        ids = sorted(set(ID_RE.findall(text)) & set(EXIT2 + EXIT1))
        emit_log(f"DOC_IDS {doc} {ids}")
        emit_log(f"DOC_HAS_R99 {doc} {'Round-99' in text or 'round 99' in text or 'payload_schema_version' in text}")

    delivered = LANE / "corpus/tools/dependency_freeze.py"
    before = sha256(LANE / "corpus/tools/dependency-freeze-contract.json")

    # Delivered-entrypoint probes that cannot write (or refuse before write).
    code, out, err, cmd = run(delivered, [])
    record("delivered/no-args", code, out, err, cmd, 2, ["INVALID-ARGUMENTS"])
    code, out, err, cmd = run(delivered, ["--not-a-real-flag"])
    record("delivered/unknown-flag", code, out, err, cmd, 2, ["INVALID-ARGUMENTS"])
    code, out, err, cmd = run(delivered, [str(LANE / "corpus/fixtures" / R95), "--freeze", str(LANE / "corpus/fixtures" / R95)])
    record("delivered/fixture-and-freeze", code, out, err, cmd, 2, ["INVALID-ARGUMENTS"], note="CLI pre-dispatch; precedence lists this ID after DIGEST-MISMATCH")
    code, out, err, cmd = run(delivered, ["--self-test", str(LANE / "corpus/fixtures" / R95)])
    record("delivered/self-test-and-fixture", code, out, err, cmd, 2, ["INVALID-ARGUMENTS"])
    code, out, err, cmd = run(delivered, ["--self-test", "--freeze", str(LANE / "corpus/fixtures" / R95)])
    record("delivered/self-test-and-freeze", code, out, err, cmd, 2, ["INVALID-ARGUMENTS"])
    missing = LANE / "corpus/fixtures/missing-parent" / R95
    code, out, err, cmd = run(delivered, [str(missing)])
    record("delivered/missing-dir-pinned-name", code, out, err, cmd, 2, ["FIXTURE-MISSING"], absent=["UNPINNED-FIXTURE", "DIGEST-MISMATCH"])
    code, out, err, cmd = run(delivered, [str(LANE / "corpus/fixtures/v118-not-a-pin")])
    record("delivered/missing-unpinned-name", code, out, err, cmd, 2, ["UNPINNED-FIXTURE"], absent=["FIXTURE-MISSING"])
    r99 = LANE / "corpus/fixtures/r99-window-lapse"
    if r99.is_dir():
        code, out, err, cmd = run(delivered, [str(r99)])
        record("delivered/r99-window-lapse", code, out, err, cmd, 2, ["UNPINNED-FIXTURE"], note="r99 is not a chain pin")
    foreign = SCRATCH / "foreign" / R95
    if foreign.exists():
        shutil.rmtree(foreign)
    shutil.copytree(LANE / "corpus/fixtures" / R95, foreign)
    code, out, err, cmd = run(delivered, [str(foreign)])
    record("delivered/foreign-copy", code, out, err, cmd, 2, ["PATH-MISMATCH"], absent=["DIGEST-MISMATCH", "SCOPE-REFUSED"])
    outside = SCRATCH / "outside-target"
    outside.mkdir(exist_ok=True)
    code, out, err, cmd = run(delivered, ["--freeze", str(outside)])
    record("delivered/freeze-outside", code, out, err, cmd, 2, ["SCOPE-REFUSED"])
    after = sha256(LANE / "corpus/tools/dependency-freeze-contract.json")
    emit_log(f"DELIVERED_CONTRACT_UNCHANGED_AFTER_REFUSED_FREEZE {before == after} {after}")

    emit_log("\n## delivered chain verify")
    for name in sorted(contract["pins"]):
        code, out, err, cmd = run(delivered, [str(LANE / "corpus/fixtures" / name)])
        record(f"delivered/clean/{name}", code, out, err, cmd, 0, [], note="control; not an exit-2 class")

    # Mirror controls and mutations.
    dest = new_case("clean-r95")
    invoke(dest, [str(fx_of(dest))], "mirror/clean-r95", 0, [])

    # Each pinned file, trailing newline: valid JSON, semantic inventory unchanged.
    for name in PINNED:
        dest = new_case(f"tamper-{name.replace('.', '_')}")
        path = fx_of(dest) / name
        path.write_bytes(path.read_bytes() + b"\n")
        invoke(
            dest, [str(fx_of(dest))], f"mirror/digest-one/{name}", 2, ["DIGEST-MISMATCH"],
            absent=["REDUCTION-DETECTED", "ADDITION-DETECTED", "ENDPOINT-CHANGE", "FILE-MISSING", "MALFORMED-JSON"],
            contains=[name],
            note="trailing newline; must name this file",
        )

    dest = new_case("tamper-two")
    for name in ("README.md", "source-excerpt.md"):
        path = fx_of(dest) / name
        path.write_bytes(path.read_bytes() + b"\n")
    invoke(
        dest, [str(fx_of(dest))], "mirror/digest-two-files", 2, ["DIGEST-MISMATCH"],
        contains=["README.md", "source-excerpt.md"],
        note="precedence: names each changed pinned file",
    )

    dest = new_case("digest-pin-lie")
    ct = load_contract(dest)
    ct["pins"][R95]["content_sha256"] = "0" * 64
    dump_contract(dest, ct)
    invoke(
        dest, [str(fx_of(dest))], "mirror/digest-pin-content-sha-lie", 2, ["DIGEST-MISMATCH"],
        contains=["no per-file digest difference"],
        note="bytes unchanged; pin content digest disagrees with its file digests",
    )

    dest = new_case("missing-readme")
    (fx_of(dest) / "README.md").unlink()
    invoke(
        dest, [str(fx_of(dest))], "mirror/missing-readme", 2, ["DIGEST-MISMATCH"],
        absent=["FILE-MISSING"],
        contains=["README.md"],
        note="markdown absence is digest class, not model-build FILE-MISSING",
    )

    dest = new_case("missing-entities")
    (fx_of(dest) / "entities.json").unlink()
    invoke(
        dest, [str(fx_of(dest))], "mirror/missing-entities-json", 2, ["DIGEST-MISMATCH"],
        absent=["FILE-MISSING", "MALFORMED-JSON"],
        contains=["entities.json"],
        note="entities.json is pinned but not required for model build",
    )

    dest = new_case("missing-timeline")
    (fx_of(dest) / "timeline.json").unlink()
    (fx_of(dest) / "README.md").write_bytes((fx_of(dest) / "README.md").read_bytes() + b"\n")
    invoke(
        dest, [str(fx_of(dest))], "mirror/missing-timeline-masks-digest", 2, ["FILE-MISSING"],
        absent=["DIGEST-MISMATCH"],
        contains=["timeline.json"],
        note="FILE-MISSING (model build) decides before DIGEST-MISMATCH",
    )

    dest = new_case("unreadable-timeline")
    tl = fx_of(dest) / "timeline.json"
    tl.chmod(0)
    try:
        invoke(dest, [str(fx_of(dest))], "mirror/unreadable-timeline", 2, ["FILE-MISSING"], contains=["unreadable"])
    finally:
        tl.chmod(0o644)

    dest = new_case("bad-json")
    (fx_of(dest) / "timeline.json").write_text("[{\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-json-truncated", 2, ["MALFORMED-JSON"], absent=["DIGEST-MISMATCH", "MALFORMED-MODEL"])

    dest = new_case("bad-utf8")
    (fx_of(dest) / "timeline.json").write_bytes(b"\xff\xfe not utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-json-utf8", 2, ["MALFORMED-JSON"], contains=["UTF-8"])

    dest = new_case("model-not-array")
    (fx_of(dest) / "timeline.json").write_text("{}\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-model-not-array", 2, ["MALFORMED-MODEL"], absent=["MALFORMED-JSON", "DIGEST-MISMATCH"])

    dest = new_case("model-dup-id")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    tl.append(dict(tl[0]))
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-model-dup-id", 2, ["MALFORMED-MODEL"], contains=["repeats event id"])

    dest = new_case("model-bad-deps")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    tl[0]["depends_on"] = [1]
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-model-deps", 2, ["MALFORMED-MODEL"], contains=["depends_on"])

    dest = new_case("model-nonsclar")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    tl[0]["tick"] = {"not": "scalar"}
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-model-nonsclar", 2, ["MALFORMED-MODEL"], contains=["must be a scalar"])

    dest = new_case("model-bad-rel")
    (fx_of(dest) / "relations.json").write_text('[{"from": "a", "to": "b"}]\n', encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/malformed-model-relation", 2, ["MALFORMED-MODEL"], contains=["from/to/type"])

    dest = new_case("semantic-reduction")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    hit = False
    for rec in tl:
        deps = rec.get("depends_on") or []
        if deps:
            rec["depends_on"] = deps[1:]
            hit = rec["id"]
            break
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(
        dest, [str(fx_of(dest))], "mirror/semantic-before-digest-reduction", 1, ["REDUCTION-DETECTED"],
        absent=["DIGEST-MISMATCH"], note=f"dropped a depends_on on {hit}",
    )

    dest = new_case("semantic-endpoint")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    tl[0]["place_id"] = str(tl[0].get("place_id")) + "-shifted"
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/semantic-before-digest-endpoint", 1, ["ENDPOINT-CHANGE"], absent=["DIGEST-MISMATCH"])

    dest = new_case("semantic-addition")
    tl = json.loads((fx_of(dest) / "timeline.json").read_text(encoding="utf-8"))
    tl[0]["depends_on"] = list(tl[0].get("depends_on") or []) + ["phantom-edge"]
    (fx_of(dest) / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/semantic-before-digest-addition", 1, ["ADDITION-DETECTED"], absent=["DIGEST-MISMATCH"])

    dest = new_case("unpinned-present")
    shutil.copytree(fx_of(dest), dest / "corpus/fixtures/v118-not-a-pin")
    invoke(dest, [str(dest / "corpus/fixtures/v118-not-a-pin")], "mirror/unpinned-present-dir", 2, ["UNPINNED-FIXTURE"], absent=["FIXTURE-MISSING", "DIGEST-MISMATCH"])

    dest = new_case("contract-missing")
    contract_of(dest).unlink()
    invoke(dest, [str(fx_of(dest))], "mirror/contract-missing", 2, ["CONTRACT-INVALID"], contains=["contract not found"])

    dest = new_case("contract-bad-json")
    contract_of(dest).write_text("{", encoding="utf-8")
    invoke(dest, [str(fx_of(dest))], "mirror/contract-bad-json", 2, ["CONTRACT-INVALID"])

    dest = new_case("contract-bad-utf8")
    contract_of(dest).write_bytes(b"\xff")
    invoke(dest, [str(fx_of(dest))], "mirror/contract-bad-utf8", 2, ["CONTRACT-INVALID"])

    dest = new_case("contract-unreadable")
    contract_of(dest).chmod(0)
    try:
        invoke(dest, [str(fx_of(dest))], "mirror/contract-unreadable", 2, ["CONTRACT-INVALID"])
    finally:
        contract_of(dest).chmod(0o644)

    dest = new_case("contract-pins-list")
    ct = load_contract(dest)
    ct["pins"] = []
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/contract-pins-not-object", 2, ["CONTRACT-INVALID"], contains=["pins object"])

    dest = new_case("pin-not-object")
    ct = load_contract(dest)
    ct["pins"][R95] = "nope"
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-not-object", 2, ["CONTRACT-INVALID"], contains=["must be an object"])

    dest = new_case("pin-absolute")
    ct = load_contract(dest)
    ct["pins"][R95]["fixture"] = "/tmp/r95-crossing-aftermath"
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-absolute-path", 2, ["CONTRACT-INVALID"], contains=["repo-relative"])

    dest = new_case("pin-outside")
    ct = load_contract(dest)
    ct["pins"][R95]["fixture"] = "corpus/tools"
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-outside-fixtures", 2, ["CONTRACT-INVALID"], contains=["outside"])

    dest = new_case("pin-empty-path")
    ct = load_contract(dest)
    ct["pins"][R95]["fixture"] = ""
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/verify-pathless-empty", 2, ["CONTRACT-INVALID"], contains=["repo-relative"], note="verify refuses path-less; freeze migrates")

    dest = new_case("pin-null-path")
    ct = load_contract(dest)
    ct["pins"][R95]["fixture"] = None
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/verify-pathless-null", 2, ["CONTRACT-INVALID"], contains=["repo-relative"])

    dest = new_case("schema-1-and-worse")
    ct = load_contract(dest)
    ct["pins"][R95]["payload_schema_version"] = 1
    ct["pins"][R95]["pinned_files"] = ["relations.json"]
    ct["pins"][R95]["files"].pop("README.md", None)
    dump_contract(dest, ct)
    missing_path = dest / "corpus/fixtures/absent-parent" / R95
    invoke(
        dest, [str(missing_path)], "mirror/schema1-before-fixture-missing", 2, ["CONTRACT-INVALID"],
        absent=["FIXTURE-MISSING", "DIGEST-MISMATCH"],
        contains=["payload_schema_version"],
        note="first failing check: schema before FIXTURE-MISSING and before pinned_files",
    )

    dest = new_case("schema-missing")
    ct = load_contract(dest)
    ct["pins"][R95].pop("payload_schema_version", None)
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/schema-missing", 2, ["CONTRACT-INVALID"], contains=["payload_schema_version"])

    dest = new_case("schema-3")
    ct = load_contract(dest)
    ct["pins"][R95]["payload_schema_version"] = 3
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/schema-3", 2, ["CONTRACT-INVALID"], contains=["payload_schema_version"])

    dest = new_case("pinned-files-short")
    ct = load_contract(dest)
    ct["pins"][R95]["pinned_files"] = PINNED[:-1]
    ct["pins"][R95]["files"].pop(PINNED[-1], None)
    dump_contract(dest, ct)
    invoke(
        dest, [str(fx_of(dest))], "mirror/pinned-files-list-short", 2, ["CONTRACT-INVALID"],
        contains=["pinned_files"],
        note="pinned_files check decides before the files-digest check",
    )

    dest = new_case("files-missing-key")
    ct = load_contract(dest)
    ct["pins"][R95]["files"].pop("inspiration-note.md", None)
    dump_contract(dest, ct)
    invoke(
        dest, [str(fx_of(dest))], "mirror/pin-files-missing-markdown-key", 2, ["CONTRACT-INVALID"],
        contains=["10 pinned files"],
        note="pin that does not digest all ten pinned files",
    )

    dest = new_case("files-extra-key")
    ct = load_contract(dest)
    ct["pins"][R95]["files"]["symbolism-clause-map.md"] = "ab" * 32
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-files-extra-key", 2, ["CONTRACT-INVALID"], contains=["10 pinned files"])

    dest = new_case("bad-file-sha")
    ct = load_contract(dest)
    ct["pins"][R95]["files"]["README.md"] = "zz"
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-bad-file-sha", 2, ["CONTRACT-INVALID"], contains=["sha256 digests"])

    dest = new_case("events-not-object")
    ct = load_contract(dest)
    ct["pins"][R95]["events"] = []
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-events-not-object", 2, ["CONTRACT-INVALID"], contains=["events object"])

    dest = new_case("event-entry-bad")
    ct = load_contract(dest)
    ct["pins"][R95]["events"]["broken"] = {"depends_on": [1]}
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-event-entry-bad", 2, ["CONTRACT-INVALID"], contains=["invalid event entry"])

    dest = new_case("relations-bad")
    ct = load_contract(dest)
    ct["pins"][R95]["relations"] = [["only-one"]]
    dump_contract(dest, ct)
    invoke(dest, [str(fx_of(dest))], "mirror/pin-relations-bad", 2, ["CONTRACT-INVALID"], contains=["relation endpoint triples"])

    dest = new_case("path-mismatch-masks-missing")
    foreign = dest / "corpus/fixtures/nested" / R95
    shutil.copytree(fx_of(dest), foreign)
    (foreign / "timeline.json").unlink()
    invoke(
        dest, [str(foreign)], "mirror/path-mismatch-before-file-missing", 2, ["PATH-MISMATCH"],
        absent=["FILE-MISSING", "DIGEST-MISMATCH"],
    )

    dest = new_case("scope-root")
    before_ct = sha256(contract_of(dest))
    invoke(dest, ["--freeze", str(dest / "corpus/fixtures")], "mirror/freeze-scope-root", 2, ["SCOPE-REFUSED"], contains=["itself"])
    emit_log(f"scope-root contract unchanged {sha256(contract_of(dest)) == before_ct}")

    dest = new_case("scope-outside")
    target = dest / "outside-target"
    target.mkdir()
    before_ct = sha256(contract_of(dest))
    invoke(dest, ["--freeze", str(target)], "mirror/freeze-outside", 2, ["SCOPE-REFUSED"], contains=["corpus/fixtures/**"])
    emit_log(f"scope-outside contract unchanged {sha256(contract_of(dest)) == before_ct}")

    dest = new_case("scope-same-name")
    foreign = dest / "corpus/fixtures/nested" / R95
    shutil.copytree(fx_of(dest), foreign)
    before_ct = sha256(contract_of(dest))
    invoke(dest, ["--freeze", str(foreign)], "mirror/freeze-same-name-elsewhere", 2, ["SCOPE-REFUSED"], contains=["already names"])
    emit_log(f"same-name contract unchanged {sha256(contract_of(dest)) == before_ct}")

    dest = new_case("scope-same-name-incomplete")
    foreign = dest / "corpus/fixtures/nested" / R95
    shutil.copytree(fx_of(dest), foreign)
    (foreign / "README.md").unlink()
    invoke(
        dest, ["--freeze", str(foreign)], "mirror/freeze-same-name-masks-file-missing", 2, ["SCOPE-REFUSED"],
        absent=["FILE-MISSING"],
        note="same-name SCOPE-REFUSED is checked before freeze's missing-pinned FILE-MISSING",
    )

    dest = new_case("freeze-missing-md")
    incomplete = dest / "corpus/fixtures/v118-incomplete"
    shutil.copytree(fx_of(dest), incomplete)
    (incomplete / "inspiration-note.md").unlink()
    before_ct = sha256(contract_of(dest))
    invoke(
        dest, ["--freeze", str(incomplete)], "mirror/freeze-missing-pinned-markdown", 2, ["FILE-MISSING"],
        contains=["inspiration-note.md"],
        note="--freeze FILE-MISSING when a declared pinned file is absent",
    )
    emit_log(f"freeze-missing-md contract unchanged {sha256(contract_of(dest)) == before_ct}")

    dest = new_case("freeze-missing-timeline")
    incomplete = dest / "corpus/fixtures/v118-no-timeline"
    shutil.copytree(fx_of(dest), incomplete)
    (incomplete / "timeline.json").unlink()
    invoke(dest, ["--freeze", str(incomplete)], "mirror/freeze-missing-timeline", 2, ["FILE-MISSING"], contains=["timeline.json"])

    dest = new_case("migrate-null")
    ct = load_contract(dest)
    ct["pins"][R95]["fixture"] = None
    dump_contract(dest, ct)
    invoke(
        dest, ["--freeze", str(fx_of(dest))], "mirror/freeze-migrates-pathless", 0, [],
        contains=["MIGRATED"],
        note="documented exception: path-less legacy pin is migrated, not SCOPE-REFUSED",
    )

    dest = new_case("upgrade-schema1")
    ct = load_contract(dest)
    ct["pins"][R95]["payload_schema_version"] = 1
    dump_contract(dest, ct)
    code, out = invoke(
        dest, ["--freeze", str(fx_of(dest))], "mirror/freeze-upgrades-schema1", 0, [],
        note="re-freeze is the payload upgrade path; verify of schema 1 is CONTRACT-INVALID",
    )
    upgraded = json.loads(contract_of(dest).read_text(encoding="utf-8"))
    emit_log(f"upgraded payload_schema_version={upgraded['pins'][R95].get('payload_schema_version')} files={sorted(upgraded['pins'][R95].get('files', {}))}")

    # Extra unpinned file, if any chain fixture has one.
    emit_log("\n## extra files outside the declared ten")
    for name in sorted(contract["pins"]):
        folder = SNAP / "corpus/fixtures" / name
        if not folder.is_dir():
            continue
        extras = sorted(p.name for p in folder.iterdir() if p.is_file() and p.name not in PINNED)
        emit_log(f"EXTRAS {name} {extras}")
        if not extras:
            continue
        dest = new_case(f"extra-{name}")
        target = fx_of(dest, name) / extras[0]
        target.write_bytes(target.read_bytes() + b"\n# v118 extra\n")
        invoke(
            dest, [str(fx_of(dest, name))], f"mirror/unpinned-extra-file/{name}/{extras[0]}", 0, [],
            note="edit outside the declared ten must not be an exit-2",
        )

    dest = new_case("selftest-expected-missing")
    ct = load_contract(dest)
    ct["self_test"]["expected"] = []
    dump_contract(dest, ct)
    invoke(dest, ["--self-test"], "mirror/selftest-expected-not-object", 2, ["CONTRACT-INVALID"], contains=["self_test.expected"])

    dest = new_case("selftest-set-mismatch")
    ct = load_contract(dest)
    ct["self_test"]["expected"].pop("clean", None)
    dump_contract(dest, ct)
    invoke(
        dest, ["--self-test"], "mirror/selftest-set-mismatch", 2, ["CONTRACT-INVALID"],
        contains=["expectation set mismatch"],
        absent=["SELF-TEST-MISMATCH"],
    )

    emit_log("\n## self-test mismatch (slow)")
    dest = new_case("selftest-mismatch")
    # The case needs the base fixture present beside the corrupted contract.
    ct = load_contract(dest)
    ct["self_test"]["expected"]["clean"]["exit"] = 1
    dump_contract(dest, ct)
    code, out, err, cmd = run(tool_of(dest), ["--self-test"])
    record(
        "mirror/selftest-mismatch-clean-exit-flipped", code, out, err, cmd, 2, ["SELF-TEST-MISMATCH"],
        contains=["cases failed"],
        note="persisted expectation disagrees with observed clean exit",
    )

    end_tool = sha256(LANE / "corpus/tools/dependency_freeze.py")
    end_ct = sha256(LANE / "corpus/tools/dependency-freeze-contract.json")
    emit_log(f"\nEND tool={end_tool} unchanged={end_tool == tool_sha}")
    emit_log(f"END contract={end_ct} unchanged={end_ct == ct_sha}")

    demonstrated = sorted({i for row in rows if row["status"] == "PASS" and row["want_exit"] == 2 for i in row["want_ids"]})
    failed = [row["label"] for row in rows if row["status"] == "FAIL"]
    emit_log(f"\nDEMONSTRATED_EXIT2 {demonstrated}")
    emit_log(f"UNDEMONSTRATED_EXIT2 {[i for i in EXIT2 if i not in demonstrated]}")
    emit_log(f"FAILED_ROWS {failed}")
    emit_log(f"ROW_COUNT {len(rows)} FAIL_COUNT {len(failed)}")
    logf.close()


if __name__ == "__main__":
    main()
