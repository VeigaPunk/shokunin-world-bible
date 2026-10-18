#!/usr/bin/env python3
"""V40 negative-dialect harness: scratch mutations of the r88 map+fixture under dialect mode.

Mutations (each on a fresh scratch copy, run twice):
  1. missing_row        remove one JSON-fact row   -> expect exit 1
  2. source_id_mismatch alter one row's source id  -> expect exit 1
  3. duplicate_row      duplicate one JSON-fact row-> expect exit 1
  4. malformed_json     corrupt entities.json      -> expect exit 2
Baseline (unmutated copy) also run twice. Live tree is never modified.
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = REPO / "corpus/tools/map_obligations.py"
FIX = REPO / "corpus/fixtures/r88-m3-maya-cluster"
SCRATCH = REPO / ".ufo/waves/round-95/seats/V40-scratch/dialect"
MAP = "claim-excerpt-map.md"
ROW_RE = re.compile(r"^\| (?:P\d|E\d|T\d) \|")


def fresh(name):
    dst = SCRATCH / name
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(FIX, dst)
    return dst


def run(cluster, extra_args=()):
    cmd = [sys.executable, str(TOOL), *extra_args, str(cluster)]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    findings = sorted(
        line[len("FINDING "):].split(":", 1)[0]
        for line in r.stdout.splitlines()
        if line.startswith("FINDING ")
    )
    results = [line for line in r.stdout.splitlines() if line.startswith("RESULT ")]
    return {
        "cmd": " ".join(cmd),
        "exit": r.returncode,
        "findings": findings,
        "result_lines": results,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }


def mutate_map(cluster, kind):
    path = cluster / MAP
    lines = path.read_text(encoding="utf-8").splitlines()
    row_idx = [i for i, line in enumerate(lines) if ROW_RE.match(line)]
    if kind == "missing_row":
        del lines[row_idx[-1]]
    elif kind == "source_id_mismatch":
        i = row_idx[0]
        lines[i] = lines[i].replace("`paired-clock`", "`bell-tally`", 1)
    elif kind == "duplicate_row":
        lines.insert(row_idx[0] + 1, lines[row_idx[0]])
    else:
        raise SystemExit(f"unknown map mutation {kind}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    cases = {}
    for name in ("baseline", "missing_row", "source_id_mismatch", "duplicate_row", "malformed_json"):
        cluster = fresh(name)
        if name == "malformed_json":
            (cluster / "entities.json").write_text("{", encoding="utf-8")
        elif name != "baseline":
            mutate_map(cluster, name)
        cases[name] = {"cluster": str(cluster), "runs": [run(cluster), run(cluster)]}
    print(json.dumps(cases, indent=2))


if __name__ == "__main__":
    main()
