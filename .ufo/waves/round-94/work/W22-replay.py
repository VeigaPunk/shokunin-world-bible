#!/usr/bin/env python3
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CHECKER = Path("corpus/fixtures/check_bible.py")
EXPECTED_CHECKER_SHA256 = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"
EXPECTED_HEAD = "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b"
EXPECTED_MISSING = {
    "r5-missing-file": ["contradictions"],
    "r62-missing": ["timeline"],
    "r67-claim-source-unavailable-control": ["sources"],
    "r67-claim-source-unavailable-empty": ["sources"],
    "r67-claim-source-unavailable-whitespace": ["sources"],
}
SECTION_FILES = ("sources.json", "entities.json", "relations.json", "timeline.json", "contradictions.json")
EXPECTED_TUPLES = Path(".ufo/waves/round-93/deepseek/F02-tuples.json")

VARIANTS = (
    {"id": "canonical_python3_isolated", "python": "python3", "flags": ["-I"], "path": "relative", "env": {}},
    {"id": "dot_relative_python3_isolated", "python": "python3", "flags": ["-I"], "path": "dot_relative", "env": {}},
    {"id": "trailing_slash_python3_isolated", "python": "python3", "flags": ["-I"], "path": "trailing_slash", "env": {}},
    {"id": "absolute_python3_isolated", "python": "python3", "flags": ["-I"], "path": "absolute", "env": {}},
    {"id": "dotdot_python3_isolated", "python": "python3", "flags": ["-I"], "path": "dotdot", "env": {}},
    {"id": "resolved_python_isolated", "python": "sys.executable", "flags": ["-I"], "path": "relative", "env": {}},
    {"id": "seed0_python3", "python": "python3", "flags": [], "path": "relative", "env": {"PYTHONHASHSEED": "0"}},
    {"id": "seed1_python3", "python": "python3", "flags": [], "path": "relative", "env": {"PYTHONHASHSEED": "1"}},
    {"id": "random_seed_python3", "python": "python3", "flags": [], "path": "relative", "env": {"PYTHONHASHSEED": "random"}},
)


def argument_for(style, fixture):
    relative = f"corpus/fixtures/{fixture}"
    if style == "relative":
        return relative
    if style == "dot_relative":
        return f"./{relative}"
    if style == "trailing_slash":
        return relative + "/"
    if style == "absolute":
        return str((ROOT / relative).resolve())
    if style == "dotdot":
        return f"corpus/fixtures/../fixtures/{fixture}"
    raise ValueError(style)


def normalize_missing_paths(stdout, argument, canonical, missing_sections):
    normalized = stdout
    rewrites = 0
    issues = []
    for section in missing_sections:
        filename = f"{section}.json"
        actual_path = os.fsencode(str(Path(argument) / filename))
        canonical_path = os.fsencode(f"{canonical}/{filename}")
        marker = b"No such file or directory: '"
        exact = marker + actual_path + b"'"
        count = stdout.count(exact)
        if count != 1:
            issues.append(f"{filename}: expected exactly one exact missing-path diagnostic, got {count}")
            continue
        normalized = normalized.replace(exact, marker + canonical_path + b"'", 1)
        rewrites += 1
    return normalized, rewrites, issues


def invoke(variant, fixture):
    argument = argument_for(variant["path"], fixture)
    python = sys.executable if variant["python"] == "sys.executable" else variant["python"]
    argv = [python, *variant["flags"], str(CHECKER), argument]
    env = os.environ.copy()
    env.update(variant["env"])
    completed = subprocess.run(argv, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return argument, argv, completed


def main():
    checker_sha = hashlib.sha256((ROOT / CHECKER).read_bytes()).hexdigest()
    expected_tuples = json.loads((ROOT / EXPECTED_TUPLES).read_text(encoding="utf-8"))
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.strip()
    fixture_results = []
    all_passed = checker_sha == EXPECTED_CHECKER_SHA256 and head == EXPECTED_HEAD

    for fixture, expected_missing in EXPECTED_MISSING.items():
        directory = ROOT / "corpus/fixtures" / fixture
        actual_missing = [Path(name).stem for name in SECTION_FILES if not (directory / name).is_file()]
        fixture_ok = actual_missing == expected_missing
        canonical = f"corpus/fixtures/{fixture}"
        baseline = None
        rows = []

        for variant in VARIANTS:
            argument, argv, completed = invoke(variant, fixture)
            normalized, rewrites, normalize_issues = normalize_missing_paths(
                completed.stdout, argument, canonical, expected_missing
            )
            violations = completed.stdout.count(b"VIOLATION:")
            fixture_ok = fixture_ok and not completed.stderr and not normalize_issues and rewrites == len(expected_missing)
            row = {
                "variant": variant["id"],
                "argv": argv,
                "path_argument": argument,
                "exit": completed.returncode,
                "stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
                "normalized_stdout_sha256": hashlib.sha256(normalized).hexdigest(),
                "violation_count": violations,
                "stderr_len": len(completed.stderr),
                "stderr_sha256": hashlib.sha256(completed.stderr).hexdigest(),
                "path_rewrite_count": rewrites,
                "normalization_issues": normalize_issues,
            }
            if baseline is None:
                baseline = (completed.returncode, completed.stdout, completed.stderr)
                expected = expected_tuples.get(canonical)
                row["matches_F02_tuple"] = bool(
                    expected
                    and completed.returncode == expected["exit"]
                    and hashlib.sha256(completed.stdout).hexdigest() == expected["stdout_sha256"]
                    and violations == expected["violation_count"]
                )
                fixture_ok = fixture_ok and row["matches_F02_tuple"]
            else:
                base_exit, base_stdout, base_stderr = baseline
                base_normalized, _, base_issues = normalize_missing_paths(
                    base_stdout, canonical, canonical, expected_missing
                )
                row["matches_canonical_after_path_normalization"] = bool(
                    not normalize_issues
                    and not base_issues
                    and completed.returncode == base_exit
                    and normalized == base_normalized
                    and completed.stderr == base_stderr
                    and violations == base_stdout.count(b"VIOLATION:")
                )
                fixture_ok = fixture_ok and row["matches_canonical_after_path_normalization"]
            rows.append(row)

        fixture_results.append({
            "fixture": fixture,
            "missing_sections": actual_missing,
            "expected_missing_sections": expected_missing,
            "all_variants_match": fixture_ok,
            "runs": rows,
        })
        all_passed = all_passed and fixture_ok

    evidence = {
        "probe": "W22 check_bible missing-file reproducibility",
        "head": head,
        "expected_head": "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b",
        "python_version": sys.version,
        "python3_path": shutil.which("python3"),
        "sys_executable": sys.executable,
        "checker_sha256": checker_sha,
        "expected_checker_sha256": EXPECTED_CHECKER_SHA256,
        "expected_tuple_source": str(EXPECTED_TUPLES),
        "normalization": "Only the exact quoted missing JSON path in its Errno diagnostic is rewritten to the canonical relative path; all other stdout bytes, exit status, violation count, and stderr are compared exactly.",
        "variants_per_fixture": len(VARIANTS),
        "result": "PASS" if all_passed else "FAIL",
        "fixtures": fixture_results,
    }
    output_path = Path(__file__).with_name("W22-evidence.json")
    output_path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"W22_RESULT {evidence['result']} fixtures={len(fixture_results)} runs={len(fixture_results) * len(VARIANTS)} checker_sha256={checker_sha}")
    print(f"W22_EVIDENCE {output_path.relative_to(ROOT)} sha256={hashlib.sha256(output_path.read_bytes()).hexdigest()}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
