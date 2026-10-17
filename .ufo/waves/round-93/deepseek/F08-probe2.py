#!/usr/bin/env python3
"""F08 second probe: as-delivered verbatim replay runs, extra adversarial cases,
and the self-reference check on the dossier's limits guard."""

import hashlib
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
TABLE_REL = "corpus/knowledge/r88-sourced-inspiration-decision-table.md"
DOSSIER = ROOT / DOSSIER_REL
text = DOSSIER.read_text()
raw_blocks = re.findall(r"```sh\n(.*?)\n```", text, re.S)
HIST_RAW, ACTIVE_RAW = raw_blocks[0], raw_blocks[-1]


def unwrap(block):
    lines = block.splitlines()
    return "\n".join(lines[1:-1])


ACTIVE, HIST = unwrap(ACTIVE_RAW), unwrap(HIST_RAW)
results = {}

# --- 1. verbatim as-delivered runs from the repository root -----------------
for name, block in (("verbatim_active", ACTIVE_RAW), ("verbatim_historical", HIST_RAW)):
    p = subprocess.run(["bash", "-s"], input=block + "\n", cwd=ROOT, capture_output=True, text=True, timeout=180)
    results[name] = {"exit": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip()[:300]}
    print(f"== {name} exit={p.returncode}")
    print(p.stdout.strip())
    if p.stderr.strip():
        print("   stderr:", p.stderr.strip()[:300])

# --- 2. self-reference check on the limits guard ---------------------------
phrase = "no source-use, rights, or canon finding is made"
outside = "\n".join(l for l in text.splitlines() if phrase in l and not l.startswith("    "))
inside = phrase in ACTIVE
print(f"\nlimits phrase in active checker code: {inside}; in non-code lines: {len([l for l in text.splitlines() if phrase in l])}")
results["limits_phrase_occurrences"] = {
    "in_active_code": inside,
    "total_lines": len([l for l in text.splitlines() if phrase in l]),
}

# --- 3. extra adversarial cases in scratch ---------------------------------
MARK = "### Corrected illustrative R8 review record"
END = "### Corrected replay"


def swap_line(t, prefix, new_line):
    head, tail = t.split(MARK, 1)
    body, rest = tail.split(END, 1)
    out, seen = [], 0
    for ln in body.splitlines(keepends=True):
        if ln.startswith(prefix) and ln != new_line:
            out.append(new_line + "\n")
            seen += 1
        else:
            out.append(ln)
    assert seen == 1, (prefix, seen)
    return head + MARK + "".join(out) + END + rest


def rows_of(t):
    tail = t.split(MARK, 1)[1].split(END, 1)[0]
    return [ln for ln in tail.splitlines() if ln.startswith("|")]


GATE_LINE = [ln for ln in text.splitlines() if ln.startswith("| Gate result |")][-1]
CE_LINE = [ln for ln in text.splitlines() if ln.startswith("| Contrary evidence |")][-1]


def build(case):
    if case == "value_swap_gate_contrary":
        gv = [p.strip() for p in GATE_LINE[1:-1].split("|")][1]
        cv = [p.strip() for p in CE_LINE[1:-1].split("|")][1]
        t = swap_line(text, "| Gate result |", "| Gate result | " + cv + " |")
        return swap_line(t, "| Contrary evidence |", "| Contrary evidence | " + gv + " |")
    if case == "nbsp_whitespace_variant":
        return swap_line(text, "| Gate result |", GATE_LINE.replace("R2 unavailable.", "R2\u00a0\u00a0unavailable.", 1))
    if case == "emspace_whitespace_variant":
        return swap_line(text, "| Gate result |", GATE_LINE.replace("R2 unavailable.", "R2\u2003unavailable.", 1))
    if case == "second_record_block_appended":
        block = "\n".join(rows_of(text)) + "\n"
        return text.replace(END, block + "\n" + END, 1)
    if case == "case_only_change_gate":
        return swap_line(text, "| Gate result |", GATE_LINE.replace("R2 unavailable.", "R2 Unavailable.", 1))
    if case == "punct_only_change_scope":
        return swap_line(
            text,
            "| Scope / disposition |",
            [ln for ln in text.splitlines() if ln.startswith("| Scope / disposition |")][-1].replace(
                "supported canon until", "supported canon. Until", 1
            ),
        )
    raise SystemExit("unknown " + case)


def run_active(t, table_text, tmp):
    sub = Path(tmp) / "scratch"
    (sub / "corpus" / "knowledge").mkdir(parents=True, exist_ok=True)
    dpath = sub / "dossier.md"
    dpath.write_text(t)
    (sub / "corpus" / "knowledge" / Path(TABLE_REL).name).write_text(table_text)
    p = subprocess.run(
        [sys.executable, "-c", ACTIVE],
        cwd=sub,
        env=dict(os.environ, D2_DOSSIER=str(dpath)),
        capture_output=True,
        text=True,
        timeout=120,
    )
    m = re.search(r"finding: (.+)", p.stdout)
    return p.returncode, (m.group(1).strip() if m else ""), p.stdout.strip().splitlines()[:1]


tmp = tempfile.mkdtemp(prefix="f08b-")
try:
    table_text = (ROOT / TABLE_REL).read_text()
    for case in (
        "value_swap_gate_contrary",
        "nbsp_whitespace_variant",
        "emspace_whitespace_variant",
        "second_record_block_appended",
        "case_only_change_gate",
        "punct_only_change_scope",
    ):
        code, finding, first = run_active(build(case), table_text, tmp)
        print(f"{case:30s} exit={code} finding={finding or '-':18s} {first[0] if first else '-'}")
        results[case] = {"exit": code, "finding": finding}

    # no round-92 patch present in scratch: proves the active replay does not read it
    patch = ROOT / ".ufo/waves/round-92/patches/E1-edges.md"
    print(f"\nround-92 patch present in scratch cwd: {Path(tmp).joinpath('.ufo').exists()}; patch exists in repo: {patch.exists()}")
    results["patch_presence"] = {"repo": patch.exists()}
finally:
    shutil.rmtree(tmp, ignore_errors=True)

out = ROOT / ".ufo/waves/round-93/deepseek/F08-results-2.json"
out.write_text(json.dumps(results, indent=2) + "\n")
print("wrote", out)
