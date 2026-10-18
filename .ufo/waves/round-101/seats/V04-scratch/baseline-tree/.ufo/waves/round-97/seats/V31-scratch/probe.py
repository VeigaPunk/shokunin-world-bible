#!/usr/bin/env python3
"""V31 independent dual_pointer probe: mutated r88 legacy fixture, run against a given tool path."""
import shutil, subprocess, sys, hashlib
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = REPO / "corpus/fixtures/r88-m3-maya-cluster"
PY = sys.executable
CELL = "| P1 | `entities[0].first_appearance` (Aru) |"
M1 = "| P1 | `entities[0].first_appearance` (Aru; see `entities[0].claims[0]`) |"
M2 = "| P1 | `entities[0].first_appearance` (Aru's first mention) |"

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(tool, scratch):
    tool = Path(tool); scratch = Path(scratch)
    if scratch.exists(): shutil.rmtree(scratch)
    for name, repl in (("control", None), ("m1-second-pointer", M1), ("m2-prose", M2)):
        d = scratch / name
        shutil.copytree(SRC, d)
        m = d / "claim-excerpt-map.md"
        text = m.read_text()
        assert CELL in text, f"anchor cell not found in {name}"
        if repl is not None:
            m.write_text(text.replace(CELL, repl))
        r = subprocess.run([PY, str(tool), str(d)], cwd=REPO, capture_output=True, text=True)
        findings = [l for l in r.stdout.splitlines() if l.startswith("FINDING")]
        result = [l for l in r.stdout.splitlines() if l.startswith("RESULT")]
        print(f"{name}: exit={r.returncode} result={result} findings={findings} stderr={r.stderr[:120]!r}")

if __name__ == "__main__":
    print("tool sha256:", sha(sys.argv[1]))
    main(sys.argv[1], sys.argv[2])
