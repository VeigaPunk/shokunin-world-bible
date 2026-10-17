#!/usr/bin/env python3
"""F08 third probe (v2): guard reachability with a corrected control, source
heading removal, and the superseded historical block's blindness control."""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
DOSSIER_REL = "corpus/knowledge/r93-r8-worked-example.md"
text = (ROOT / DOSSIER_REL).read_text()
table = (ROOT / "corpus/knowledge/r88-sourced-inspiration-decision-table.md").read_text()
raw = re.findall(r"```sh\n(.*?)\n```", text, re.S)
HIST_RAW, ACTIVE_RAW = raw[0], raw[-1]
ACTIVE = "\n".join(ACTIVE_RAW.splitlines()[1:-1])
MARK = "### Corrected illustrative R8 review record"
END = "### Corrected replay"
record_block = MARK + "\n" + text.split(MARK, 1)[1].split(END, 1)[0]
LIMITS_PARA = (
    "\nLimits: this is a hypothetical editorial example; no source-use, rights, or canon "
    "finding is made, and no live integration review or source inspection is claimed.\n"
)

results = {}
tmp = tempfile.mkdtemp(prefix="f08c2-")
try:
    def run(code, dossier_text, table_text, label, cwd=None, env_path=None):
        sub = Path(tmp) / label
        (sub / "corpus" / "knowledge").mkdir(parents=True, exist_ok=True)
        dpath = sub / "dossier.md"
        dpath.write_text(dossier_text)
        (sub / "corpus" / "knowledge" / "r88-sourced-inspiration-decision-table.md").write_text(table_text)
        p = subprocess.run(
            [sys.executable, "-c", code],
            cwd=cwd or sub,
            env=dict(os.environ, D2_DOSSIER=str(env_path or dpath)),
            capture_output=True,
            text=True,
            timeout=120,
        )
        m = re.search(r"finding: (.+)", p.stdout)
        return p.returncode, (m.group(1).strip() if m else ""), p.stdout.strip(), p.stderr.strip()[:200]

    cases = [
        ("record_only_with_limits", record_block + LIMITS_PARA, table, "ok"),
        ("record_only_no_limits", record_block + LIMITS_PARA.replace(
            "no source-use, rights, or canon finding is made",
            "the example is bounded"), table, "nolim"),
        ("r9_heading_all_removed", record_block + LIMITS_PARA, table.replace("### R9 appendix", "### R9-appendix-x"), "nors9"),
        ("host_limits_stripped", text.replace("no source-use, rights, or canon finding is made", "a bounded example is made", 1), table, "host"),
    ]
    for label, dossier_text, table_text, tag in cases:
        code, finding, out, err = run(ACTIVE, dossier_text, table_text, tag)
        last = out.splitlines()[-1] if out else (err.splitlines()[-1] if err else "-")
        print(f"{label:26s} exit={code} finding={finding or '-':18s} last={last[:70]}")
        results[label] = {"exit": code, "finding": finding}

    # historical block blindness, run from the repository root (read-only)
    contra = [ln for ln in text.splitlines() if ln.startswith("| Gate result |")][-1]
    mutated = text.replace(contra, contra[:-2].rstrip() + " Both conditions passed; R2 passes and is available. |", 1)
    (Path(tmp) / "mutated.md").write_text(mutated)
    p = subprocess.run(
        ["bash", "-s"], input=HIST_RAW + "\n", cwd=ROOT,
        env=dict(os.environ, D2_DOSSIER=str(Path(tmp) / "mutated.md")),
        capture_output=True, text=True, timeout=180,
    )
    print(f"\nhistorical_on_contradiction exit={p.returncode}\n{p.stdout.strip()}")
    results["historical_on_contradiction"] = {"exit": p.returncode, "stdout": p.stdout.strip()}
finally:
    shutil.rmtree(tmp, ignore_errors=True)

(ROOT / ".ufo/waves/round-93/deepseek/F08-results-3.json").write_text(json.dumps(results, indent=2) + "\n")
print("wrote F08-results-3.json")
