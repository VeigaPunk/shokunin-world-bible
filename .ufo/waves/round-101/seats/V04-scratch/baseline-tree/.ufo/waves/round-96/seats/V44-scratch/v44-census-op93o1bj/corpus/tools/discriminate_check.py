#!/usr/bin/env python3
"""Check the two durable fixtures that discriminate the r90 checker repair."""

import argparse
import difflib
import hashlib
import re
import subprocess
import sys
from pathlib import Path

PIN = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"
BASELINE = "e97613cc276f5fa9cac49ff1900798cf6863c020"
FIXTURES = ("r91-c1-null-chain", "r91-c1-tick-unresolved")
EXPECTATION = re.compile(
    r"## Expected output with (e97613c|the delivered checker) "
    r"\(exit 1; stderr empty\)\n\nComplete stdout:\n\n```text\n(.*?)\n```",
    re.DOTALL,
)


def expectations(readme):
    matches = EXPECTATION.findall(readme.read_text(encoding="utf-8"))
    result = {label: output + "\n" for label, output in matches}
    if len(matches) != 2 or set(result) != {"e97613c", "the delivered checker"}:
        raise ValueError(f"unexpected checker expectations in {readme}")
    return result


def run(command, root, input_text=None, check=False):
    return subprocess.run(
        command,
        cwd=root,
        input=input_text,
        capture_output=True,
        text=True,
        check=check,
    )


def delivered_run(checker, fixture, root):
    return run([sys.executable, "-I", str(checker), str(fixture)], root)


def baseline_source(root):
    return run(
        ["git", "show", f"{BASELINE}:corpus/fixtures/check_bible.py"],
        root,
        check=True,
    ).stdout


def baseline_run(source, fixture, root):
    wrapper = (
        "import sys; source=sys.stdin.read(); "
        "sys.argv=['check_bible.py', *sys.argv[1:]]; "
        "exec(compile(source, 'check_bible.py', 'exec'), "
        "{'__name__': '__main__', '__file__': 'check_bible.py'})"
    )
    return run(
        [sys.executable, "-I", "-c", wrapper, str(fixture)],
        root,
        input_text=source,
    )


def delivered_semantics(name, output):
    if name == "r91-c1-null-chain":
        return (
            "provenance chain break; expected from_holder 'mira', got None" in output
            and "is not uniquely resolvable" not in output
        )
    return (
        "VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3"
        in output
        and "holder identity is not uniquely resolvable" not in output
        and "possible provenance chain break" in output
    )


def run_check(mode, root):
    checker = root / "corpus/fixtures/check_bible.py"
    checker_hash = hashlib.sha256(checker.read_bytes()).hexdigest()
    matches_pin = checker_hash == PIN
    print(f"mode={mode} checker_sha256={checker_hash} matches_pin={matches_pin}")
    source = baseline_source(root)
    failures = []
    for name in FIXTURES:
        fixture = root / "corpus/fixtures" / name
        expected = expectations(fixture / "README.md")
        old = baseline_run(source, fixture, root)
        new = delivered_run(checker, fixture, root)
        selected = new if mode == "delivered" else old
        removed = [
            line[2:]
            for line in difflib.ndiff(old.stdout.splitlines(), new.stdout.splitlines())
            if line.startswith("- ")
        ]
        added = [
            line[2:]
            for line in difflib.ndiff(old.stdout.splitlines(), new.stdout.splitlines())
            if line.startswith("+ ")
        ]
        delivered_exact = new.stdout == expected["the delivered checker"]
        baseline_exact = old.stdout == expected["e97613c"]
        gate = delivered_semantics(name, selected.stdout)
        print(
            f"{name}: run_exit={selected.returncode} stderr_empty={selected.stderr == ''} "
            f"README_exact={selected.stdout == expected['the delivered checker']} "
            f"baseline_README_exact={baseline_exact} "
            f"changed_line_pairs={len(added)}/{len(removed)} (old<->new)"
        )
        print(f"  pinned_semantic_gate={'PASS' if gate else 'FAIL'}")
        delivered_ok = (
            new.returncode == 1
            and new.stderr == ""
            and delivered_exact
            and delivered_semantics(name, new.stdout)
            and baseline_exact
            and old.returncode == 1
            and old.stderr == ""
            and len(added) == 1
            and len(removed) == 1
        )
        if not delivered_ok:
            failures.append(name)

    if mode == "delivered":
        if failures or not matches_pin:
            failed = failures or ["checker-hash"]
            print("REGRESSION-DETECTED on " + ",".join(failed) + " — pinned delivered semantics not present")
            return 2
        print("RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression")
        return 0

    if failures or not matches_pin:
        failed = failures or ["checker-hash"]
        print("RESULT: REVERT SIMULATION INCONCLUSIVE on " + ",".join(failed))
        return 1
    print("REGRESSION-DETECTED on " + ",".join(FIXTURES) + " — pinned delivered semantics not present")
    return 2


def main():
    parser = argparse.ArgumentParser(description="Discriminate the r90 checker repair using the r91 fixture pair")
    parser.add_argument("--checker", choices=("delivered", "e97613c"), default="delivered")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.repo_root.resolve()
    try:
        if not (root / "corpus/fixtures/check_bible.py").is_file():
            raise FileNotFoundError(f"checker not found under repository root: {root}")
        return run_check(args.checker, root)
    except (OSError, subprocess.SubprocessError, UnicodeError, ValueError) as error:
        print(f"CHECK ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
