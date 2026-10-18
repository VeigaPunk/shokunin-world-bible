#!/usr/bin/env python3
"""V40 independent census. Own implementation (not a copy of V17/V37).

For every directory directly under <root>/corpus/fixtures (dot-dirs excluded),
run the check_bible that lives in that same root, with cwd = root and a
repo-relative argv. Record exit code and sha256 of the combined stdout+stderr
bytes exactly as captured (no stripping). Count violation lines under two
conventions: line startswith "VIOLATION" and the substring "VIOLATION".
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


def census(root: Path) -> dict:
    root = root.resolve()
    checker = root / "corpus" / "fixtures" / "check_bible.py"
    fixtures = root / "corpus" / "fixtures"
    if not checker.is_file():
        raise SystemExit(f"no checker at {checker}")
    dirs = sorted(
        p for p in fixtures.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )
    receipts = {}
    clean = negative = other = dash = word = 0
    non01 = []
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    for d in dirs:
        rel = f"corpus/fixtures/{d.name}"
        proc = subprocess.run(
            [sys.executable, "corpus/fixtures/check_bible.py", rel],
            cwd=root,
            env=env,
            capture_output=True,
        )
        blob = proc.stdout + proc.stderr
        digest = hashlib.sha256(blob).hexdigest()
        text = blob.decode("utf-8", "replace")
        lines = text.splitlines()
        dash_n = sum(1 for line in lines if line.startswith("- "))
        word_n = sum(1 for line in lines if "VIOLATION" in line)
        dash += dash_n
        word += word_n
        code = proc.returncode
        if code == 0:
            clean += 1
        elif code == 1:
            negative += 1
        else:
            other += 1
            non01.append({"dir": rel, "exit": code})
        receipts[rel] = {
            "exit": code,
            "sha256": digest,
            "dash_lines": dash_n,
            "violation_word_lines": word_n,
            "stdout_bytes": len(proc.stdout),
            "stderr_bytes": len(proc.stderr),
        }
    return {
        "root": str(root),
        "checker": str(checker),
        "fixture_dirs": len(dirs),
        "clean_exit0": clean,
        "negative_exit1": negative,
        "non01_count": other,
        "violation_lines_dash": dash,
        "violation_lines_word": word,
        "non01": non01,
        "receipts": receipts,
    }


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: census_v40.py <root> <out.json>")
    result = census(Path(sys.argv[1]))
    out = Path(sys.argv[2])
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {k: result[k] for k in result if k != "receipts"}
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
