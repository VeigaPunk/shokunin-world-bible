#!/usr/bin/env python3
"""V05 c1-negative battery for round-101 dependency_freeze.py.

All cases run against scratch mirrors; the delivered tree is never written.
Every case is invoked twice; exit code and full stdout/stderr must be
byte-identical across repeats, with stable FINDING IDs.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
DELIVERED_TOOL = LANE / "corpus/tools/dependency_freeze.py"
DELIVERED_CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"
SCRATCH = LANE / ".ufo/waves/round-101/seats/.v05-scratch"
BATTERY = SCRATCH / "battery"
LOG = []
SUMMARY = {"cases": 0, "runs": 0, "matching_cases": 0, "stable_ids": 0,
           "stable_full_output": 0, "failures": []}

PINNED_FILES = (
    "entities.json", "relations.json", "timeline.json", "sources.json",
    "contradictions.json", "README.md", "claim-excerpt-map.md",
    "fictional-excerpts.md", "inspiration-note.md", "source-excerpt.md",
)


def record(case, argv_desc, run_outputs, expected_exit, expected_ids,
           names_file=None):
    SUMMARY["cases"] += 1
    SUMMARY["runs"] += len(run_outputs)
    ids_per_run = []
    for code, out, err in run_outputs:
        ids = sorted(set(line.split(":", 1)[0].split(" ", 1)[1]
                         for line in out.splitlines() if line.startswith("FINDING ")))
        ids_per_run.append(ids)
    ok = True
    reasons = []
    exits = {code for code, _, _ in run_outputs}
    if exits != {expected_exit}:
        ok = False
        reasons.append(f"exit {sorted(exits)} != [{expected_exit}]")
    full_out = [(out + err) for _, out, err in run_outputs]
    if len(set(full_out)) != 1:
        ok = False
        reasons.append("full output not byte-identical across repeats")
    else:
        SUMMARY["stable_full_output"] += 1
    first_ids = ids_per_run[0]
    if all(ids == first_ids for ids in ids_per_run):
        SUMMARY["stable_ids"] += 1
    else:
        ok = False
        reasons.append(f"finding ids unstable {ids_per_run}")
    if sorted(expected_ids) != first_ids:
        ok = False
        reasons.append(f"ids {first_ids} != expected {sorted(expected_ids)}")
    if names_file and names_file not in full_out[0]:
        ok = False
        reasons.append(f"names_file {names_file} absent from output")
    if "Traceback" in full_out[0]:
        ok = False
        reasons.append("traceback leaked")
    if ok:
        SUMMARY["matching_cases"] += 1
    else:
        SUMMARY["failures"].append({"case": case, "reasons": reasons,
                                    "exit": sorted(exits), "ids": first_ids,
                                    "output": full_out[0].splitlines()[:12]})
    LOG.append(f"CASE {case}: exit={sorted(exits)} ids={first_ids} "
               f"{'ok' if ok else 'MISMATCH ' + '; '.join(reasons)}")
    return ok


def run(argv, cwd):
    if argv and str(argv[0]).endswith(".py"):
        argv = [sys.executable, *argv]
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=120)
    return proc.returncode, proc.stdout, proc.stderr


def make_root(name, contract_mutator=None, drop_contract=False):
    root = BATTERY / name
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(DELIVERED_TOOL, root / "corpus/tools/dependency_freeze.py")
    if not drop_contract:
        text = DELIVERED_CONTRACT.read_text(encoding="utf-8")
        if contract_mutator is not None:
            data = json.loads(text)
            data = contract_mutator(data)
            text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        (root / "corpus/tools/dependency-freeze-contract.json").write_text(text, encoding="utf-8")
    return root


def copy_fixture(root, base_fixture, name=None):
    dest = root / "corpus/fixtures" / (name or base_fixture.name)
    shutil.copytree(base_fixture, dest)
    return dest


def rewrite_json(path, fn):
    data = json.loads(path.read_text(encoding="utf-8"))
    fn(data)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def semantic_cases(base_fixture, tag):
    """Exit-1 semantic classes on a pinned fixture, mirrored."""
    out = []

    def mirror(case):
        root = make_root(f"{tag}_{case}")
        fix = copy_fixture(root, base_fixture)
        return root, fix

    # 1 reduction_edge_drop
    root, fix = mirror("reduction_edge_drop")
    def drop_dep(data):
        for rec in data:
            if rec.get("depends_on"):
                rec["depends_on"] = rec["depends_on"][1:]
                break
    rewrite_json(fix / "timeline.json", drop_dep)
    out.append((f"{tag}/reduction_edge_drop",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["REDUCTION-DETECTED"]))

    # 2 addition_edge_phantom
    root, fix = mirror("addition_edge_phantom")
    def add_phantom(data):
        data[0].setdefault("depends_on", []).append("v05-phantom-dep")
    rewrite_json(fix / "timeline.json", add_phantom)
    out.append((f"{tag}/addition_edge_phantom",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["ADDITION-DETECTED"]))

    # 3 repointed_edge (C3 class): swap a dep for a different valid earlier event
    root, fix = mirror("repointed_edge")
    timeline = json.loads((fix / "timeline.json").read_text(encoding="utf-8"))
    donor_index = next((i for i, rec in enumerate(timeline) if rec.get("depends_on")), None)
    donor = timeline[donor_index] if donor_index is not None else None
    if donor is not None:
        earlier = [rec["id"] for rec in timeline[:donor_index]
                   if rec["id"] not in donor["depends_on"] and rec["id"] != donor["id"]]
        target = earlier[0] if earlier else next(
            (rec["id"] for rec in timeline
             if rec["id"] not in donor["depends_on"] and rec["id"] != donor["id"]), None)
    def repoint(data):
        for rec in data:
            if rec["id"] == donor["id"] and target:
                rec["depends_on"][0] = target
                break
    if donor is not None and target is not None:
        rewrite_json(fix / "timeline.json", repoint)
        out.append((f"{tag}/repointed_edge",
                    lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                    1, ["REDUCTION-DETECTED", "ADDITION-DETECTED"]))

    # 4 event_removed
    root, fix = mirror("event_removed")
    def drop_first(data):
        data.pop(0)
    rewrite_json(fix / "timeline.json", drop_first)
    out.append((f"{tag}/event_removed",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["REDUCTION-DETECTED"]))

    # 5 event_endpoint_change
    root, fix = mirror("event_endpoint_change")
    def bump_place(data):
        rec = data[0]
        cur = rec.get("place_id")
        rec["place_id"] = ("v05-scratch-place" if cur != "v05-scratch-place" else "v05-scratch-place-2")
    rewrite_json(fix / "timeline.json", bump_place)
    out.append((f"{tag}/event_endpoint_change",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["ENDPOINT-CHANGE"]))

    # 6 relation_endpoint_flip
    root, fix = mirror("relation_endpoint_flip")
    def flip(data):
        if data:
            data[0]["from"], data[0]["to"] = data[0]["to"], data[0]["from"]
    rewrite_json(fix / "relations.json", flip)
    out.append((f"{tag}/relation_endpoint_flip",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["ENDPOINT-CHANGE"]))

    # 7 relation_removed
    root, fix = mirror("relation_removed")
    (fix / "relations.json").write_text("[]\n", encoding="utf-8")
    out.append((f"{tag}/relation_removed",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["REDUCTION-DETECTED"]))

    # 8 relation_added
    root, fix = mirror("relation_added")
    def add_rel(data):
        data.append({"from": "v05-a", "to": "v05-b", "type": "v05-unpinned"})
    rewrite_json(fix / "relations.json", add_rel)
    out.append((f"{tag}/relation_added",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["ADDITION-DETECTED"]))

    # 9 precedence: semantic finding + byte tamper => exit 1, semantic IDs only
    root, fix = mirror("semantic_over_digest")
    rewrite_json(fix / "timeline.json", drop_dep)
    timeline_text = (fix / "timeline.json").read_text(encoding="utf-8")
    (fix / "timeline.json").write_text(timeline_text + "\n", encoding="utf-8")
    out.append((f"{tag}/semantic_over_digest",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                1, ["REDUCTION-DETECTED"]))
    return out


def digest_sweep_cases(base_fixture, tag):
    """One case per pinned file: trailing newline => DIGEST-MISMATCH naming the file."""
    out = []
    for fname in PINNED_FILES:
        case = f"digest_newline_{fname.replace('.', '_').replace('-', '_')}"
        root = make_root(f"{tag}_{case}")
        fix = copy_fixture(root, base_fixture)
        target = fix / fname
        target.write_bytes(target.read_bytes() + b"\n")
        out.append((f"{tag}/{case}",
                    lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                    2, ["DIGEST-MISMATCH"], fname))
    # markdown file removed entirely: still exit 2 DIGEST-MISMATCH naming it
    root = make_root(f"{tag}_digest_removed_readme")
    fix = copy_fixture(root, base_fixture)
    (fix / "README.md").unlink()
    out.append((f"{tag}/digest_removed_readme",
                lambda r=root, f=fix: [str(r / "corpus/tools/dependency_freeze.py"), str(f)],
                2, ["DIGEST-MISMATCH"], "README.md"))
    return out


def cli_cases(base_fixture):
    """Exit-2 CLI/path/scope/contract cases, each in its own mirror root."""
    out = []
    tool_name = "dependency_freeze.py"

    def tool_argv(root, *rest):
        return [str(root / "corpus/tools" / tool_name)] + [str(a) for a in rest]

    def bind(root, *rest):
        return lambda: tool_argv(root, *rest)

    # malformed_json
    root = make_root("malformed_json")
    fix = copy_fixture(root, base_fixture)
    (fix / "timeline.json").write_text("[{\n", encoding="utf-8")
    out.append(("malformed_json", bind(root, fix), 2, ["MALFORMED-JSON"]))

    # malformed_model: valid JSON, wrong shape
    root = make_root("malformed_model")
    fix = copy_fixture(root, base_fixture)
    (fix / "timeline.json").write_text("{}\n", encoding="utf-8")
    out.append(("malformed_model", bind(root, fix), 2, ["MALFORMED-MODEL"]))

    # malformed_model: depends_on wrong type
    root = make_root("malformed_model_deps_type")
    fix = copy_fixture(root, base_fixture)
    def deps_bad(data):
        data[0]["depends_on"] = "not-a-list"
    rewrite_json(fix / "timeline.json", deps_bad)
    out.append(("malformed_model_deps_type", bind(root, fix), 2, ["MALFORMED-MODEL"]))

    # missing_timeline
    root = make_root("missing_timeline")
    fix = copy_fixture(root, base_fixture)
    (fix / "timeline.json").unlink()
    out.append(("missing_timeline", bind(root, fix), 2, ["FILE-MISSING"]))

    # missing relations (the other required file)
    root = make_root("missing_relations")
    fix = copy_fixture(root, base_fixture)
    (fix / "relations.json").unlink()
    out.append(("missing_relations", bind(root, fix), 2, ["FILE-MISSING"]))

    # unpinned fixture (renamed copy inside a mirror)
    root = make_root("unpinned_fixture")
    fix = copy_fixture(root, base_fixture, name="v05-unpinned-copy")
    out.append(("unpinned_fixture", bind(root, fix), 2, ["UNPINNED-FIXTURE"]))

    # missing fixture dir: pinned NAME, absent directory => FIXTURE-MISSING
    # (UNPINNED-FIXTURE would win precedence for an unpinned name)
    root = make_root("missing_fixture")
    out.append(("missing_fixture", bind(root, root / "corpus/fixtures" / base_fixture.name),
                2, ["FIXTURE-MISSING"]))

    # invalid arguments variants
    root = make_root("invalid_arguments")
    fix = copy_fixture(root, base_fixture)
    out.append(("invalid_arguments_both", bind(root, fix, "--freeze", fix),
                2, ["INVALID-ARGUMENTS"]))
    out.append(("invalid_arguments_noargs", bind(root), 2, ["INVALID-ARGUMENTS"]))
    out.append(("invalid_arguments_selftest_fixture", bind(root, "--self-test", fix),
                2, ["INVALID-ARGUMENTS"]))
    out.append(("invalid_arguments_selftest_freeze", bind(root, "--self-test", "--freeze", str(fix)),
                2, ["INVALID-ARGUMENTS"]))

    # path_mismatch: same-named copy at a foreign path
    root = make_root("path_mismatch")
    foreign = root / "foreign"
    foreign.mkdir()
    shutil.copytree(base_fixture, foreign / base_fixture.name)
    out.append(("path_mismatch", bind(root, foreign / base_fixture.name),
                2, ["PATH-MISMATCH"]))

    # contract_invalid: corrupt JSON
    root = make_root("contract_invalid_corrupt")
    (root / "corpus/tools/dependency-freeze-contract.json").write_text("{not json", encoding="utf-8")
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_corrupt", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: contract absent
    root = make_root("contract_invalid_absent", drop_contract=True)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_absent", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: root not an object with pins
    def break_root(d):
        return {"schema_version": d.get("schema_version")}
    root = make_root("contract_invalid_root", contract_mutator=break_root)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_root", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: pin payload_schema_version wrong
    def bump_schema(d):
        d["pins"][base_fixture.name]["payload_schema_version"] = 99
        return d
    root = make_root("contract_invalid_schema", contract_mutator=bump_schema)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_schema", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: pin files digest key removed
    def drop_files(d):
        d["pins"][base_fixture.name].pop("files")
        return d
    root = make_root("contract_invalid_no_files", contract_mutator=drop_files)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_no_files", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: pin fixture path absolute
    def abs_path(d):
        d["pins"][base_fixture.name]["fixture"] = str(base_fixture.resolve())
        return d
    root = make_root("contract_invalid_abs_path", contract_mutator=abs_path)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_abs_path", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # contract_invalid: pin fixture path outside corpus/fixtures
    def out_path(d):
        d["pins"][base_fixture.name]["fixture"] = "corpus/knowledge/somewhere"
        return d
    root = make_root("contract_invalid_out_scope_path", contract_mutator=out_path)
    fix = copy_fixture(root, base_fixture)
    out.append(("contract_invalid_out_scope_path", bind(root, fix), 2, ["CONTRACT-INVALID"]))

    # self_test_mismatch: flip clean expectation, run --self-test on the mirror
    def flip_clean(d):
        d["self_test"]["expected"]["clean"]["exit"] = 1
        return d
    root = make_root("self_test_mismatch", contract_mutator=flip_clean)
    copy_fixture(root, base_fixture)
    out.append(("self_test_mismatch", bind(root, "--self-test"), 2, ["SELF-TEST-MISMATCH"]))

    # self-test positive control on the delivered case set (mirror)
    root = make_root("self_test_clean")
    copy_fixture(root, base_fixture)
    out.append(("self_test_clean", bind(root, "--self-test"), 0, []))
    return out


def freeze_cases(base_fixture):
    """--freeze guard negatives and one positive, all on mirrors."""
    out = []
    def tool_argv(root, *rest):
        return [str(root / "corpus/tools/dependency_freeze.py")] + [str(a) for a in rest]

    def bind(root, *rest):
        return lambda: tool_argv(root, *rest)

    # scope_refused: target outside corpus/fixtures
    root = make_root("scope_refused_outside")
    outside = root / "outside-scope"
    outside.mkdir()
    out.append(("scope_refused_outside", bind(root, "--freeze", outside),
                2, ["SCOPE-REFUSED"]))

    # scope_refused: the scope root itself
    root = make_root("scope_refused_root")
    out.append(("scope_refused_root", bind(root, "--freeze", root / "corpus/fixtures"),
                2, ["SCOPE-REFUSED"]))

    # scope_refused: same-named fixture at a different in-scope path would rewrite
    # the delivered pin -> refused because pin already names another path
    root = make_root("scope_refused_same_name")
    other = root / "corpus/fixtures/elsewhere"
    other.mkdir()
    shutil.copytree(base_fixture, other / base_fixture.name)
    out.append(("scope_refused_same_name",
                bind(root, "--freeze", other / base_fixture.name),
                2, ["SCOPE-REFUSED"]))

    # freeze with a pinned file missing => FILE-MISSING, and contract must be unchanged
    root = make_root("freeze_missing_pinned_file")
    fix = copy_fixture(root, base_fixture, name="v05-gap-fixture")
    (fix / "source-excerpt.md").unlink()
    before = (root / "corpus/tools/dependency-freeze-contract.json").read_bytes()
    out.append(("freeze_missing_pinned_file", bind(root, "--freeze", fix),
                2, ["FILE-MISSING"]))
    after = (root / "corpus/tools/dependency-freeze-contract.json").read_bytes()
    SUMMARY["freeze_no_write_on_refusal"] = (before == after)
    if before != after:
        SUMMARY["failures"].append({"case": "freeze_no_write_on_refusal",
                                    "reasons": ["contract bytes changed on refused freeze"]})

    # positive: freeze a fresh in-scope fixture copy, then verify it twice clean
    root = make_root("freeze_positive")
    fix = copy_fixture(root, base_fixture, name="v05-fresh-fixture")
    out.append(("freeze_positive", bind(root, "--freeze", fix), 0, []))
    out.append(("freeze_positive_verify", bind(root, fix), 0, []))
    return out


def live_readonly_checks():
    """Read-only verify of the delivered chain + mirror self-test control."""
    out = []
    contract = json.loads(DELIVERED_CONTRACT.read_text(encoding="utf-8"))
    pins = sorted(contract["pins"])
    SUMMARY["delivered_pins"] = pins
    SUMMARY["delivered_pin_count"] = len(pins)
    for name in pins:
        fix = LANE / "corpus/fixtures" / name
        out.append((f"live_verify/{name}",
                    lambda f=fix: [str(DELIVERED_TOOL), str(f)], 0, []))
    return out, pins


def main():
    if BATTERY.exists():
        shutil.rmtree(BATTERY)
    BATTERY.mkdir(parents=True)
    bases = []
    contract = json.loads(DELIVERED_CONTRACT.read_text(encoding="utf-8"))
    for name in ("r95-crossing-aftermath", "r100-docket-review"):
        if name in contract["pins"]:
            p = LANE / "corpus/fixtures" / name
            if p.is_dir():
                bases.append(p)
    SUMMARY["battery_base_fixtures"] = [b.name for b in bases]

    cases = []
    for base in bases:
        tag = base.name
        cases += semantic_cases(base, tag)
        cases += digest_sweep_cases(base, tag)
    cases += cli_cases(bases[0])
    cases += freeze_cases(bases[0])
    live, pins = live_readonly_checks()
    cases += live

    for case in cases:
        name, argv_fn, want_exit, want_ids = case[0], case[1], case[2], case[3]
        names_file = case[4] if len(case) > 4 else None
        runs = [run(argv_fn(), BATTERY) for _ in range(2)]
        record(name, argv_fn(), runs, want_exit, want_ids, names_file)

    SUMMARY["delivered_tool_sha256"] = hashlib.sha256(DELIVERED_TOOL.read_bytes()).hexdigest()
    SUMMARY["delivered_contract_sha256"] = hashlib.sha256(DELIVERED_CONTRACT.read_bytes()).hexdigest()
    (SCRATCH / "battery_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
    (SCRATCH / "battery_summary.json").write_text(
        json.dumps(SUMMARY, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in SUMMARY.items() if k != "failures"},
                     indent=2, sort_keys=True))
    if SUMMARY["failures"]:
        print("FAILURES:")
        for failure in SUMMARY["failures"]:
            print(json.dumps(failure, indent=2)[:800])
    return 0 if not SUMMARY["failures"] else 1


if __name__ == "__main__":
    sys.exit(main())
