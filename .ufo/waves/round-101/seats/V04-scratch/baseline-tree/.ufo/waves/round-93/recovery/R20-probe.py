#!/usr/bin/env python3
"""Mutate the R8 dossier's actual record cells and replay its embedded checker."""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DOSSIER_REL = Path("corpus/knowledge/r93-r8-worked-example.md")
TABLE_REL = Path("corpus/knowledge/r88-sourced-inspiration-decision-table.md")
E1_REL = Path(".ufo/waves/round-92/patches/E1-edges.md")
RECORD_HEADING = "## Illustrative R8 review record"
CROSSWALK_HEADING = "## Record-to-decision crosswalk"
REPLAY_MARKER = "python3 - <<'PY'\n"

MUTATIONS = (
    (
        "blank_gate_field",
        "Gate result",
        "",
        "An empty actual record cell must be rejected.",
    ),
    (
        "filler_contrary_evidence",
        "Contrary evidence",
        "TBD — evidence to be added",
        "A placeholder is not a recorded contrary-evidence finding.",
    ),
    (
        "inverted_hold_release",
        "Scope / disposition",
        "Retain the whole element in supported canon with an uncertainty notice.",
        "The disposition must not reverse the required whole-element hold.",
    ),
    (
        "removed_reviewer_owner",
        "Reviewer / record date",
        "Reviewer not assigned; 2026-10-17.",
        "A date without a named reviewer must be rejected.",
    ),
    (
        "note_only_record_target",
        "Element and scope pointer",
        "See the inspiration note/map only; no affected element or scope is identified.",
        "A note-only target must not replace an element/scope pointer.",
    ),
)


def extract_replay(source):
    start = source.find(REPLAY_MARKER)
    if start < 0:
        raise ValueError("embedded `python3 - <<'PY'` replay was not found")
    start += len(REPLAY_MARKER)
    end = source.find("\nPY", start)
    if end < 0:
        raise ValueError("embedded replay has no closing PY marker")
    return source[start:end]


def replace_record_cell(source, label, value):
    start = source.find(RECORD_HEADING)
    end = source.find(CROSSWALK_HEADING, start + len(RECORD_HEADING))
    if start < 0 or end < 0:
        raise ValueError("illustrative record table boundaries were not found")
    lines = source.splitlines(keepends=True)
    changed = 0
    offset = 0
    for index, line in enumerate(lines):
        line_end = offset + len(line)
        if start <= offset < end:
            body = line.rstrip("\r\n")
            cells = body.split("|")
            if len(cells) == 4 and cells[1].strip() == label:
                ending = line[len(body):]
                lines[index] = f"| {label} | {value} |{ending}"
                changed += 1
        offset = line_end
    if changed != 1:
        raise ValueError(f"expected one `{label}` record row, found {changed}")
    return "".join(lines)


def git_show(repo, revision, path):
    return subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{revision}:{path.as_posix()}"],
        text=True,
        encoding="utf-8",
    )


def load_inputs(repo, dossier_path, revision):
    if revision:
        contents = {
            DOSSIER_REL: git_show(repo, revision, DOSSIER_REL),
            TABLE_REL: git_show(repo, revision, TABLE_REL),
            E1_REL: git_show(repo, revision, E1_REL),
        }
        source_label = f"git:{revision}"
    else:
        contents = {
            DOSSIER_REL: dossier_path.read_text(encoding="utf-8"),
            TABLE_REL: (repo / TABLE_REL).read_text(encoding="utf-8"),
            E1_REL: (repo / E1_REL).read_text(encoding="utf-8"),
        }
        head = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
        ).strip()
        source_label = f"worktree@{head}"
    return contents, source_label


def bundle_digest(contents):
    digest = hashlib.sha256()
    for path in sorted(contents, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(contents[path].encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def replay_once(code, scratch, dossier_text):
    target = scratch / DOSSIER_REL
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dossier_text, encoding="utf-8")
    env = os.environ.copy()
    env["D2_DOSSIER"] = DOSSIER_REL.as_posix()
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=scratch,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def output_summary(result):
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return lines[-1] if lines else "(no stdout)"


def self_test():
    sample = """## Illustrative R8 review record

| Field | Recorded value |
|---|---|
| Gate result | original value |

## Record-to-decision crosswalk
| Gate result | crosswalk value |

```sh
D2_DOSSIER=sample python3 - <<'PY'
print('R20-SELFTEST')
PY
```
"""
    code = extract_replay(sample)
    assert code == "print('R20-SELFTEST')"
    changed = replace_record_cell(sample, "Gate result", "")
    section = changed.split(CROSSWALK_HEADING, 1)[0]
    assert "| Gate result |  |" in section
    assert "| Gate result | crosswalk value |" in changed
    print("SELFTEST PASS R20-PROBE-PARSER")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--dossier", type=Path, default=None)
    parser.add_argument(
        "--revision",
        help="read the dossier and both replay references from this git revision",
    )
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.revision and args.dossier:
        parser.error("--revision and --dossier cannot be combined")

    repo = args.repo.resolve()
    dossier_path = args.dossier or (repo / DOSSIER_REL)
    if not dossier_path.is_absolute():
        dossier_path = repo / dossier_path
    contents, source_label = load_inputs(repo, dossier_path, args.revision)
    source = contents[DOSSIER_REL]
    code = extract_replay(source)
    print(f"source={source_label}")
    print(f"dossier_sha256={hashlib.sha256(source.encode('utf-8')).hexdigest()}")
    print(f"input_bundle_sha256={bundle_digest(contents)}")

    rejected = 0
    unevaluable = 0
    with tempfile.TemporaryDirectory(prefix="R20-dossier-probe-") as temp:
        scratch = Path(temp)
        for path, text in contents.items():
            target = scratch / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        control = replay_once(code, scratch, source)
        print(
            f"intact_control: exit={control.returncode} expected=0 "
            f"summary={output_summary(control)!r}"
        )
        if control.returncode != 0 or "Traceback" in control.stderr:
            unevaluable += 1

        for case_id, label, value, _reason in MUTATIONS:
            mutated = replace_record_cell(source, label, value)
            result = replay_once(code, scratch, mutated)
            if result.returncode == 1 and "Traceback" not in result.stderr:
                status = "REJECTED"
                rejected += 1
            elif result.returncode == 0:
                status = "FALSE_PASS"
            else:
                status = "UNEVALUABLE"
                unevaluable += 1
            print(
                f"{case_id}: {status} exit={result.returncode} "
                f"expected=REJECTED(exit 1) summary={output_summary(result)!r}"
            )

    print(f"negative_mutations_rejected={rejected}/{len(MUTATIONS)}")
    if unevaluable:
        print(f"probe_verdict=UNEVALUABLE cases={unevaluable}")
        return 2
    if rejected != len(MUTATIONS):
        print("probe_verdict=FAIL false-positive(s) remain")
        return 1
    print("probe_verdict=PASS intact control accepted; all negative mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
