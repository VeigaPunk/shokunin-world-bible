#!/usr/bin/env python3
"""F25 independent replay of R24's r89 null-holder definiteness-regression claim.

Read-only: sources are read with `git show` at pinned revisions; the mutated
fixture lives in an auto-removed TemporaryDirectory. Stdlib only.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIXTURE = "corpus/fixtures/r89-fn2-unresolved-chain-break"
FIXTURE_FILES = ["README.md", "contradictions.json", "entities.json",
                 "relations.json", "sources.json", "timeline.json"]
REVS = [("baseline_51b286b", "51b286b"),
        ("r89_closure_e97613c", "e97613c"),
        ("r90_fix_ca7f9ef", "ca7f9ef")]


def git_show(rev, path):
    out = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=REPO, capture_output=True)
    if out.returncode != 0:
        raise SystemExit(f"git show failed for {rev}:{path}: {out.stderr.decode()}")
    return out.stdout


with tempfile.TemporaryDirectory(prefix="f25-replay-") as tmp:
    tmp = Path(tmp)
    files = {name: git_show("e97613c", f"{FIXTURE}/{name}") for name in FIXTURE_FILES}
    checkers = {}
    for label, rev in REVS:
        p = tmp / f"checker-{label}.py"
        p.write_bytes(git_show(rev, "corpus/fixtures/check_bible.py"))
        checkers[label] = p
    entities = json.loads(files["entities.json"].decode())
    seal = entities[4]
    seal["provenance"][0]["to_holder"] = "mira"
    seal["provenance"][1]["from_holder"] = None
    for variant, tick in [("tick3_chain_only", 3), ("tick0_chain_plus_tick", 0)]:
        rows = json.loads(json.dumps(entities))
        rows[4]["provenance"][1]["tick"] = tick
        fixdir = tmp / variant
        fixdir.mkdir()
        for name in FIXTURE_FILES:
            content = files[name]
            if name == "entities.json":
                content = (json.dumps(rows, indent=2) + "\n").encode()
            (fixdir / name).write_bytes(content)
        for label, rev in REVS:
            r = subprocess.run([sys.executable, str(checkers[label]), str(fixdir)],
                               capture_output=True)
            print(f"== {variant} {label} exit={r.returncode}")
            print(r.stdout.decode().rstrip())
            if r.stderr.strip():
                print("STDERR:", r.stderr.decode().rstrip())
