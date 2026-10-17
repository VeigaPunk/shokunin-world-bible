#!/usr/bin/env python3
"""F19: independent byte replay of the two r91 differential fixtures.

Re-derives the four outputs (delivered/baseline x two fixtures) without
importing or invoking corpus/tools/discriminate_check.py, extracts the README
blocks with a local parser, and reports byte equality plus the old<->new diff.
Stdlib only; no writes outside its own JSON receipt.
"""

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASELINE = "e97613cc276f5fa9cac49ff1900798cf6863c020"
FIXTURES = ("r91-c1-null-chain", "r91-c1-tick-unresolved")
BLOCK = re.compile(
    r"## Expected output with (e97613c|the delivered checker) \(exit 1; stderr empty\)"
    r"\n\nComplete stdout:\n\n```text\n(.*?)\n```",
    re.DOTALL,
)
WRAPPER = (
    "import sys; source=sys.stdin.read(); "
    "sys.argv=['check_bible.py', *sys.argv[1:]]; "
    "exec(compile(source, 'check_bible.py', 'exec'), "
    "{'__name__': '__main__', '__file__': 'check_bible.py'})"
)


def run(cmd, input_text=None):
    return subprocess.run(
        cmd, cwd=REPO, input=input_text, capture_output=True, text=True
    )


def main():
    checker = REPO / "corpus/fixtures/check_bible.py"
    out = {
        "repo": str(REPO),
        "baseline_revision": BASELINE,
        "delivered_checker_sha256": hashlib.sha256(checker.read_bytes()).hexdigest(),
        "baseline_source_sha256": None,
        "fixtures": {},
    }
    baseline = run(["git", "show", f"{BASELINE}:corpus/fixtures/check_bible.py"])
    baseline.check_returncode()
    src = baseline.stdout
    out["baseline_source_sha256"] = hashlib.sha256(src.encode()).hexdigest()
    ok = True
    for name in FIXTURES:
        fixture = REPO / "corpus/fixtures" / name
        readme = (fixture / "README.md").read_text(encoding="utf-8")
        blocks = dict(BLOCK.findall(readme))
        assert set(blocks) == {"e97613c", "the delivered checker"}, name
        new = run([sys.executable, "-I", str(checker), str(fixture)])
        old = run(
            [sys.executable, "-I", "-c", WRAPPER, str(fixture)], input_text=src
        )
        nd = [
            line[2:]
            for line in difflib.ndiff(old.stdout.splitlines(), new.stdout.splitlines())
            if line.startswith("- ")
        ]
        na = [
            line[2:]
            for line in difflib.ndiff(old.stdout.splitlines(), new.stdout.splitlines())
            if line.startswith("+ ")
        ]
        rec = {
            "delivered": {
                "exit": new.returncode,
                "stderr": new.stderr,
                "readme_exact": new.stdout == blocks["the delivered checker"] + "\n",
            },
            "baseline": {
                "exit": old.returncode,
                "stderr": old.stderr,
                "readme_exact": old.stdout == blocks["e97613c"] + "\n",
            },
            "removed_lines": nd,
            "added_lines": na,
            "diff_pairs": [len(na), len(nd)],
        }
        rec["all_expected"] = (
            rec["delivered"]["exit"] == 1
            and rec["delivered"]["stderr"] == ""
            and rec["delivered"]["readme_exact"]
            and rec["baseline"]["exit"] == 1
            and rec["baseline"]["stderr"] == ""
            and rec["baseline"]["readme_exact"]
            and len(na) == 1
            and len(nd) == 1
        )
        ok = ok and rec["all_expected"]
        out["fixtures"][name] = rec
    out["independent_replay_all_expected"] = ok
    Path(__file__).with_name("F19-replay.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
