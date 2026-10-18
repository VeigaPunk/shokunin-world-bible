#!/usr/bin/env python3
"""Rebuild R18's two baseline boundary-document adversaries."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

BASELINE = "65838f867d6ece8e7b8bdcc4ffc667a08a1b785e"
DOC_PATH = "corpus/knowledge/holder-assessment-boundary.md"


def replace_once(text, old, new, case_id):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{case_id}: expected one mutation target, found {count}")
    return text.replace(old, new, 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[4]
    source = subprocess.run(
        ["git", "-C", str(repo), "show", f"{BASELINE}:{DOC_PATH}"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    comment_attack = replace_once(
        source,
        "Tick findings are NOT qualified:",
        "Tick findings inherit the same qualification: when a compared holder "
        "identity is not uniquely resolvable, the tick line is emitted with the "
        "`input-structural finding, not sourced-canon; ` prefix and an expected-holder note.",
        "R18-C9-HTML-COMMENT-CONTRADICTION",
    )
    limits = (
        "Tick comparisons are not in this class: strict tick order is decided by the\n"
        "  two validated integer tick values, so an unresolved holder id cannot qualify it — the only\n"
        "  tick prefix comes from an independently ambiguous source citation (`:323-326`; seat C9's\n"
        "  round-90 ruling)."
    )
    comment_attack = replace_once(
        comment_attack,
        limits,
        "Tick comparisons are in this class: an unresolved holder id qualifies the tick line like "
        "any chain finding.",
        "R18-C9-HTML-COMMENT-CONTRADICTION",
    )
    comment_attack = replace_once(
        comment_attack,
        "tick order is an integer comparison",
        "tick order compares validated integer values",
        "R18-C9-HTML-COMMENT-CONTRADICTION",
    )
    comment_attack = replace_once(
        comment_attack,
        "tick order, an integer comparison,",
        "the validated tick-order result",
        "R18-C9-HTML-COMMENT-CONTRADICTION",
    )
    comment = (
        "<!-- superseded r90 wording preserved verbatim for history: "
        "Tick findings are NOT qualified by holder identity; tick order is an integer comparison. -->"
    )
    comment_attack = comment_attack.rstrip() + "\n\n" + comment + "\n"
    if comment_attack.count("Tick findings are NOT qualified") != 1:
        raise SystemExit("R18-C9-HTML-COMMENT-CONTRADICTION: marker not isolated to comment")
    if comment_attack.count("integer comparison") != 1:
        raise SystemExit("R18-C9-HTML-COMMENT-CONTRADICTION: marker not isolated to comment")

    wrong_anchor = replace_once(
        source,
        "comparison gate (`:322`) and its branches",
        "comparison gate (`:325`) and its branches",
        "R18-BARE-ANCHOR-IN-RANGE-DRIFT",
    )

    cases = {
        "baseline_commit": BASELINE,
        "expected_new_frozen_document_failure_id": "snapshot_tampered",
        "new_design_expectations_are_not_executed_here": True,
        "cases": [
            {
                "id": "R18-C9-HTML-COMMENT-CONTRADICTION",
                "file": "R18-c9-html-comment.md",
                "old_certifier_expected_exit": 0,
                "new_frozen_document_expected_exit": 1,
                "new_frozen_document_expected_failure_id": "snapshot_tampered",
                "purpose": "Contradict the tick ruling while preserving both raw required markers only in an HTML comment.",
            },
            {
                "id": "R18-BARE-ANCHOR-IN-RANGE-DRIFT",
                "file": "R18-bare-anchor-drift.md",
                "old_certifier_expected_exit": 0,
                "new_frozen_document_expected_exit": 1,
                "new_frozen_document_expected_failure_id": "snapshot_tampered",
                "purpose": "Change bare checker ref :322 to wrong but in-range :325.",
            },
        ],
    }

    outputs = {
        "R18-c9-html-comment.md": comment_attack,
        "R18-bare-anchor-drift.md": wrong_anchor,
    }
    for name, text in outputs.items():
        path = out / name
        path.write_text(text, encoding="utf-8")
        cases["cases"][0 if "c9-" in name else 1]["sha256"] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
    print(json.dumps(cases, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
