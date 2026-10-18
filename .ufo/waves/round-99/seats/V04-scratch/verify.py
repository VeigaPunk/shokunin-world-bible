#!/usr/bin/env python3
"""V04 c1-selftest verification. Reads lane bytes; writes only under V04-scratch."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = LANE / ".ufo/waves/round-99/seats/V04-scratch"
TOOL = LANE / "corpus/tools/dependency_freeze.py"
CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"
EXPECT_TOOL = "fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c"
EXPECT_CONTRACT = "8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628"
INHERITED = [
    "clean", "reduction_edge_drop", "addition_edge_phantom", "event_removed",
    "event_endpoint_change", "relation_endpoint_flip", "relation_removed",
    "relation_added", "digest_tamper", "malformed_json", "missing_timeline",
    "unpinned_fixture", "missing_fixture", "invalid_arguments", "scope_refused",
    "path_mismatch", "self_test_mismatch",
]
PINNED = [
    "entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json",
    "README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md",
    "source-excerpt.md",
]


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd, cwd, env=None):
    print(f"$ {' '.join(cmd)}")
    print(f"  cwd={cwd}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)
    sys.stdout.write(result.stdout)
    if result.stderr:
        print("--- stderr ---")
        sys.stdout.write(result.stderr)
        if not result.stderr.endswith("\n"):
            print()
    print(f"EXIT={result.returncode}")
    return result


def corpus_index():
    rows = []
    for path in sorted(LANE.joinpath("corpus").rglob("*")):
        if path.is_file():
            rows.append(f"{sha256_file(path)}  {path.relative_to(LANE)}")
    return "\n".join(rows) + "\n"


def object_slice(text, key):
    marker = f'"{key}": {{'
    start = text.find(marker)
    if start < 0:
        return None
    i = start + len(marker) - 1
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[start:j + 1]
    return None


def main():
    print("=== preflight hashes ===")
    tool_sha = sha256_file(TOOL)
    contract_sha = sha256_file(CONTRACT)
    print(f"tool {tool_sha}")
    print(f"contract {contract_sha}")
    if tool_sha != EXPECT_TOOL or contract_sha != EXPECT_CONTRACT:
        print("ABORT hash moved before verification")
        return 3
    report = LANE / ".ufo/waves/round-99/seats/S1-full-file-pins.md"
    print(f"S1 report sha256 {sha256_file(report)} bytes {report.stat().st_size}")

    print("=== corpus snapshot before ===")
    before = corpus_index()
    (SCR / "corpus-before-selftest.sha256").write_text(before)
    print(f"files {before.count(chr(10))}")

    print("=== live --self-test ===")
    selftest = run([sys.executable, str(TOOL), "--self-test"], LANE)
    (SCR / "delivered-selftest.log").write_text(selftest.stdout + selftest.stderr)
    print(f"SELFTEST_EXIT={selftest.returncode}")

    print("=== hashes after self-test ===")
    print(f"tool {sha256_file(TOOL)} unchanged={sha256_file(TOOL)==tool_sha}")
    print(f"contract {sha256_file(CONTRACT)} unchanged={sha256_file(CONTRACT)==contract_sha}")
    after = corpus_index()
    (SCR / "corpus-after-selftest.sha256").write_text(after)
    print(f"corpus_index_equal {before == after}")
    if before != after:
        bset = set(before.splitlines())
        aset = set(after.splitlines())
        print("corpus_only_before")
        for line in sorted(bset - aset):
            print(line)
        print("corpus_only_after")
        for line in sorted(aset - bset):
            print(line)

    residue = sorted(p.name for p in LANE.iterdir() if p.name.startswith("dependency-freeze-self-test-"))
    print(f"selftest_residue {residue}")

    print("=== inherited CASE lines vs baseline log ===")
    base_lines = [
        line for line in (SCR / "baseline-selftest.log").read_text().splitlines()
        if line.startswith("CASE ")
    ]
    live_lines = [line for line in selftest.stdout.splitlines() if line.startswith("CASE ")]
    inherited_live = live_lines[:17]
    print(f"baseline_case_count {len(base_lines)} live_case_count {len(live_lines)}")
    print(f"inherited_case_lines_byte_identical {inherited_live == base_lines}")
    if inherited_live != base_lines:
        for i, (a, b) in enumerate(zip(base_lines, inherited_live)):
            if a != b:
                print(f"DIFF {i}")
                print(f" base {a}")
                print(f" live {b}")
        if len(base_lines) != len(inherited_live):
            print(f"length base={len(base_lines)} live17={len(inherited_live)}")
    if len(live_lines) == 18:
        print(f"NEW_CASE_LINE {live_lines[17]}")

    print("=== inherited expectation objects vs 4265df5 ===")
    base_raw = subprocess.check_output(
        ["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"], cwd=LANE
    ).decode()
    live_raw = CONTRACT.read_text()
    base = json.loads(base_raw)
    live = json.loads(live_raw)
    be = base["self_test"]["expected"]
    le = live["self_test"]["expected"]
    parsed_equal = all(be[k] == le[k] for k in INHERITED)
    slices_equal = all(object_slice(base_raw, k) == object_slice(live_raw, k) for k in INHERITED)
    print(f"parsed_equal {parsed_equal}")
    print(f"file_slice_byte_identical {slices_equal}")
    print(f"added {sorted(set(le) - set(be))}")
    print(f"removed {sorted(set(be) - set(le))}")
    print(f"base_fixture {base['self_test'].get('base_fixture')} {live['self_test'].get('base_fixture')}")
    md = le["markdown_tamper"]
    print(f"persisted_markdown_tamper {json.dumps(md, sort_keys=True)}")

    print("=== hand-derive markdown_tamper FINDING ===")
    pin = live["pins"]["r95-crossing-aftermath"]
    fix = LANE / "corpus/fixtures/r95-crossing-aftermath"
    observed = {}
    for name in PINNED:
        raw = (fix / name).read_bytes()
        observed[name] = hashlib.sha256(raw).hexdigest()
        print(f"pin_match {name} {observed[name] == pin['files'][name]}")
    payload = json.dumps({n: observed[n] for n in PINNED}, sort_keys=True, separators=(",", ":"))
    live_digest = hashlib.sha256(payload.encode()).hexdigest()
    print(f"live_content_digest {live_digest}")
    print(f"pin_content_digest {pin['content_sha256']}")
    print(f"live_matches_pin {live_digest == pin['content_sha256']}")
    raw_md = (fix / "fictional-excerpts.md").read_bytes() + b"\n"
    new_file = hashlib.sha256(raw_md).hexdigest()
    tampered = dict(observed)
    tampered["fictional-excerpts.md"] = new_file
    tpayload = json.dumps(tampered, sort_keys=True, separators=(",", ":"))
    tdigest = hashlib.sha256(tpayload.encode()).hexdigest()
    derived = (
        "FINDING DIGEST-MISMATCH: "
        f"content digest {tdigest} != pin {pin['content_sha256']}; "
        f"changed: fictional-excerpts.md (sha256 {pin['files']['fictional-excerpts.md']} -> {new_file}); "
        "pinned-file bytes changed outside the semantic inventory"
    )
    print("HAND_DERIVED")
    print(derived)
    (SCR / "hand-derived-finding.txt").write_text(derived + "\n")
    print(
        "DERIVED_MATCHES_PERSISTED "
        f"{md.get('exit') == 2 and md.get('finding_ids') == ['DIGEST-MISMATCH'] and md.get('names_file') == 'fictional-excerpts.md' and md.get('forbid_traceback') is True}"
    )

    print("=== reproduce case in scratch mirror ===")
    repro = SCR / "repro"
    if repro.exists():
        shutil.rmtree(repro)
    (repro / "corpus/tools").mkdir(parents=True)
    shutil.copy2(TOOL, repro / "corpus/tools/dependency_freeze.py")
    shutil.copy2(CONTRACT, repro / "corpus/tools/dependency-freeze-contract.json")
    shutil.copytree(fix, repro / "corpus/fixtures/r95-crossing-aftermath")
    excerpt = repro / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
    excerpt.write_bytes(excerpt.read_bytes() + b"\n")
    reproduced = run(
        [sys.executable, str(repro / "corpus/tools/dependency_freeze.py"),
         str(repro / "corpus/fixtures/r95-crossing-aftermath")],
        repro,
    )
    finding_lines = [line for line in reproduced.stdout.splitlines() if line.startswith("FINDING ")]
    print(f"REPRO_FINDING_COUNT {len(finding_lines)}")
    print(f"REPRO_MATCHES_HAND_DERIVED {finding_lines == [derived]}")
    print(f"REPRO_NAMES_FILE {'fictional-excerpts.md' in reproduced.stdout}")
    print(f"REPRO_EXIT {reproduced.returncode}")
    (SCR / "repro-verify.log").write_text(reproduced.stdout + reproduced.stderr)

    print("=== perturb expectation names_file in scratch ===")
    pert = SCR / "perturb-expect"
    if pert.exists():
        shutil.rmtree(pert)
    (pert / "corpus/tools").mkdir(parents=True)
    (pert / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(TOOL, pert / "corpus/tools/dependency_freeze.py")
    corrupted = json.loads(CONTRACT.read_text())
    corrupted["self_test"]["expected"]["markdown_tamper"]["names_file"] = "README.md"
    (pert / "corpus/tools/dependency-freeze-contract.json").write_text(
        json.dumps(corrupted, indent=2, ensure_ascii=False) + "\n"
    )
    shutil.copytree(fix, pert / "corpus/fixtures/r95-crossing-aftermath")
    pert_run = run(
        [sys.executable, str(pert / "corpus/tools/dependency_freeze.py"), "--self-test"],
        pert,
    )
    (SCR / "perturb-expect.log").write_text(pert_run.stdout + pert_run.stderr)
    print(f"PERTURB_EXPECT_EXIT {pert_run.returncode}")
    print(f"live_contract_unchanged {sha256_file(CONTRACT) == contract_sha}")
    print(f"live_tool_unchanged {sha256_file(TOOL) == tool_sha}")

    print("=== perturb case to no-op tamper in scratch ===")
    noop = SCR / "perturb-noop"
    if noop.exists():
        shutil.rmtree(noop)
    (noop / "corpus/tools").mkdir(parents=True)
    (noop / "corpus/fixtures").mkdir(parents=True)
    tool_text = TOOL.read_text()
    old = 'excerpt.write_bytes(excerpt.read_bytes() + b"\\n")'
    new = "excerpt.write_bytes(excerpt.read_bytes())"
    if old not in tool_text:
        print("ABORT noop pattern missing")
        return 4
    (noop / "corpus/tools/dependency_freeze.py").write_text(tool_text.replace(old, new, 1))
    shutil.copy2(CONTRACT, noop / "corpus/tools/dependency-freeze-contract.json")
    shutil.copytree(fix, noop / "corpus/fixtures/r95-crossing-aftermath")
    noop_run = run(
        [sys.executable, str(noop / "corpus/tools/dependency_freeze.py"), "--self-test"],
        noop,
    )
    (SCR / "perturb-noop.log").write_text(noop_run.stdout + noop_run.stderr)
    print(f"PERTURB_NOOP_EXIT {noop_run.returncode}")
    print(f"live_contract_unchanged {sha256_file(CONTRACT) == contract_sha}")
    print(f"live_tool_unchanged {sha256_file(TOOL) == tool_sha}")
    print(f"S1_report_unchanged {sha256_file(report) == hashlib.sha256(report.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
