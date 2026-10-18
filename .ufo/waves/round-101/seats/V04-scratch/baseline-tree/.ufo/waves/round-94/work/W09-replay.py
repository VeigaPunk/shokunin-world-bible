#!/usr/bin/env python3
import json
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
BASELINE_COMMIT = "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b"
FIXTURE = REPO / "corpus/fixtures/r88-m3-maya-cluster"
CHECKER = REPO / "corpus/fixtures/check_bible.py"
INHERITED_IDS = ("aru-ninth-bell", "evin-ninth-bell")


def run_case(name, bible, expected_exit, expected_lines):
    command = [sys.executable, str(CHECKER), str(bible)]
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"CASE {name}")
    print(f"COMMAND {shlex.join(command)}")
    print(f"EXIT {result.returncode}")
    print(result.stdout.rstrip())
    if result.stderr:
        print("STDERR")
        print(result.stderr.rstrip())
    actual_lines = result.stdout.splitlines()
    assert result.returncode == expected_exit, (name, result.returncode, result.stdout, result.stderr)
    for expected in expected_lines:
        assert expected in actual_lines, (name, expected, actual_lines)
    return result.returncode


def isolated_case(root, name, tick, dependencies):
    case = root / name
    case.mkdir()
    for filename in ("entities.json", "relations.json", "contradictions.json"):
        shutil.copyfile(FIXTURE / filename, case / filename)

    sources = json.loads((FIXTURE / "sources.json").read_text(encoding="utf-8"))
    sources.append({
        "id": "w09-probe",
        "title": "W09 isolated structural probe",
        "kind": "test input",
        "reliability_note": "Synthetic checker data only; not corpus evidence or in-world canon.",
    })
    (case / "sources.json").write_text(json.dumps(sources, indent=2) + "\n", encoding="utf-8")

    timeline = json.loads((FIXTURE / "timeline.json").read_text(encoding="utf-8"))
    timeline.append({
        "id": f"w09-{name}",
        "tick": tick,
        "entity_id": "aru",
        "place_id": "quiet-rise",
        "depends_on": list(dependencies),
        "description": "Synthetic event used only for structural checker probing.",
        "source_id": "w09-probe",
    })
    (case / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    return case


def main():
    inherited = json.loads((FIXTURE / "timeline.json").read_text(encoding="utf-8"))
    observed = tuple(event["id"] for event in inherited)
    assert observed == INHERITED_IDS, observed
    assert tuple(event["tick"] for event in inherited) == (9, 9)
    print(f"BASELINE_COMMIT {BASELINE_COMMIT}")
    print(f"INHERITED_EVENTS {observed[0]}@9 {observed[1]}@9")
    print("TEMP_SCOPE .ufo/waves/round-94/work (temporary case inputs removed on exit)")

    run_case(
        "r88-inherited-baseline",
        FIXTURE,
        0,
        ["CLEAN: schema, citations, relations, timeline; 0 violations"],
    )
    with tempfile.TemporaryDirectory(prefix="W09-replay-", dir=WORK) as scratch:
        root = Path(scratch)
        cases = (
            ("clean-tick10", 10, INHERITED_IDS),
            ("equal-tick", 9, INHERITED_IDS),
            ("inverted-tick", 8, INHERITED_IDS),
            ("missing-dependency", 10, (*INHERITED_IDS, "missing-tick8")),
        )
        expected = {
            "clean-tick10": (0, ["CLEAN: schema, citations, relations, timeline; 0 violations"]),
            "equal-tick": (1, [
                "VIOLATION: timeline[2].depends_on: timeline inversion 'aru-ninth-bell' tick 9 not before 'w09-equal-tick' tick 9",
                "VIOLATION: timeline[2].depends_on: timeline inversion 'evin-ninth-bell' tick 9 not before 'w09-equal-tick' tick 9",
                "2 violation(s); no canon changed",
            ]),
            "inverted-tick": (1, [
                "VIOLATION: timeline[2].depends_on: timeline inversion 'aru-ninth-bell' tick 9 not before 'w09-inverted-tick' tick 8",
                "VIOLATION: timeline[2].depends_on: timeline inversion 'evin-ninth-bell' tick 9 not before 'w09-inverted-tick' tick 8",
                "2 violation(s); no canon changed",
            ]),
            "missing-dependency": (1, [
                "VIOLATION: timeline[2].depends_on: unknown event 'missing-tick8'",
                "1 violation(s); no canon changed",
            ]),
        }
        for name, tick, dependencies in cases:
            case = isolated_case(root, name, tick, dependencies)
            run_case(name, case, *expected[name])

    print("ASSERTIONS PASS: baseline clean; tick10/two dependencies clean; equal and inverted ticks report both inversions; unknown dependency reports unknown event.")


if __name__ == "__main__":
    main()
