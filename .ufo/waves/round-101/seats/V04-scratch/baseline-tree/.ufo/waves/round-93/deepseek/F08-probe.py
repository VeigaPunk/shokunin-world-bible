#!/usr/bin/env python3
"""F08 adversarial probe of the ACTIVE R8 dossier replay (seat F08).

Extracts the effective replay from the committed dossier, recomputes the
canonical record digest two independent ways, then runs the mutation matrix in
isolated scratch copies. Read-only over the repository; writes only under a
small temp dir removed on exit.
"""

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
DIGEST_LITERAL = "da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05"

dossier_text = (ROOT / DOSSIER_REL).read_text()
table_text = (ROOT / TABLE_REL).read_text()
def unwrap(block):
    lines = block.splitlines()
    assert lines[0].startswith("D2_DOSSIER="), lines[0]
    assert lines[-1].strip() == "PY", lines[-1]
    body = "\n".join(lines[1:-1])
    assert "python3" not in body.splitlines()[0], body.splitlines()[0]
    return body


blocks = re.findall(r"```sh\n(.*?)\n```", dossier_text, re.S)
HISTORICAL, ACTIVE = unwrap(blocks[0]), unwrap(blocks[-1])
assert DIGEST_LITERAL in ACTIVE, "active block must be the corrected one"
assert DIGEST_LITERAL not in HISTORICAL, "historical block must not carry the digest"

MARK = "### Corrected illustrative R8 review record"
END = "### Corrected replay"


def record_lines(text):
    tail = text.split(MARK, 1)[1].split(END, 1)[0]
    return [ln for ln in tail.splitlines() if ln.startswith("|")]


def strip_cell(line):
    return [p.strip() for p in line[1:-1].split("|")]


# --- independent route A: hand-transcribed canonical values -----------------
CANON_A = [
    "Hypothetical proposed element: the entire element consisting of the same seven threshold names in the same order as *Kesh Hymn* lines 12\u201319; no live corpus element ID is supplied.",
    "The hypothetical creator denies using a source. This is an account, not an adjudication.",
    "D2, this dossier's author, acts only as the named example reviewer; 2026-10-17. Example-only: no live integration review or source inspection occurred.",
    "R2 unavailable. The hypothetical creator's no-source account is recorded, but contrary source-specific sequence evidence defeats the gate; this does not prove source use and does not establish R1.",
    "The hypothetical reviewer records the scenario-stipulated same seven threshold names in the same order as *Kesh Hymn* lines 12\u201319; this is contrary source-specific evidence for the editorial screen, not evidence that the creator consulted that work.",
    "The hypothetical element consists entirely of that sequence; removing it leaves no independently authored, independently supportable remainder. The source-dependent detail is inseparable in this case.",
    "Withhold the whole element from supported canon until it is re-derived without the dependency or a permitted source text is delivered and a separately reviewed R1 decision establishes a claim-specific basis. Preserve the neutral note and evidence. This does not itself prove copying, source use, rights status, or canon.",
    "Keep a dated `possible influence: unverified` note and mark R2 unavailable. If influence or separability remains disputed, record the unresolved question and missing evidence in `l0-questions.md`. Re-derive without the dependency, or deliver permitted source text and obtain a separately reviewed R1 decision with a claim-specific basis. Remove the provisional note only after a later review records both R2 conditions passing or a confirmed R1 source-use decision.",
    "Normative owner: the lore integration editor records the two-part R2 gate result, affected element, and separability decision. Illustrative case owner: D2, this dossier's author, acting only as the hypothetical integration editor; no real integration owner or live review is claimed. The creator supplies the provenance account; a named reviewer assesses contrary source-specific evidence and whether an independently authored, independently supportable remainder exists.",
    "Both conjuncts are required: (1) either R2 condition fails or remains unresolved; AND (2) the reviewer cannot separate the source-dependent detail from the element while leaving an independently authored, independently supportable remainder.",
    "Separate inspiration-note target: create or update the hypothetical element's dated `possible influence: unverified` note; record the gate result, affected element, contrary evidence, separability rationale, whole-element hold, and next action. Preserve the neutral note and evidence; this does not state that influence occurred.",
    "Separate element-map target: create or update a distinct map entry for the same hypothetical element; record its affected aspect, gate result, contrary evidence, separability rationale, whole-element hold, and next action. The inspiration-note entry does not substitute for this element-map record.",
]

# --- independent route B: minimal parser over the delivered corrected table
ROWS_B = [strip_cell(ln) for ln in record_lines(dossier_text)][1:]
CANON_B = [
    cells[1]
    for cells in ROWS_B
    if len(cells) == 2 and not all(re.fullmatch(r":?-{3,}:?", c) for c in cells)
]


def digest_of(values):
    payload = json.dumps(
        [re.sub(r"\s+", " ", v).strip() for v in values],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


digest_a = digest_of(CANON_A)
digest_b = digest_of(CANON_B)
print("route A hand-typed :", digest_a, "| cells", len(CANON_A))
print("route B parser     :", digest_b, "| cells", len(CANON_B))
print("literal in dossier :", DIGEST_LITERAL)
print("A==B:", digest_a == digest_b, "A==literal:", digest_a == DIGEST_LITERAL)
if digest_a != digest_b:
    for i, (x, y) in enumerate(zip(CANON_A, CANON_B)):
        if x != y:
            print("  cell", i, "differs")
            print("   A:", repr(x[:160]))
            print("   B:", repr(y[:160]))

# --- mutation harness -------------------------------------------------------
GATE = "| Gate result |"
OWNER = "| Owner |"
SCOPE = "| Scope / disposition |"
MAP = "| Element-map target |"
NOTE = "| Inspiration note target |"
OLD_SCOPE_SENT = (
    "Withhold the whole element from supported canon until it is re-derived without "
    "the dependency or a permitted source text is delivered and a separately reviewed "
    "R1 decision establishes a claim-specific basis."
)
LIMITS_SENT = "no source-use, rights, or canon finding is made"


def swap_line(text, prefix, new_line, limit=MARK):
    out, seen = [], 0
    active = False
    for ln in text.splitlines(keepends=True):
        if ln.startswith(MARK):
            active = True
        if active and ln.startswith(prefix):
            out.append(new_line + "\n")
            seen += 1
        else:
            out.append(ln)
    assert seen == 1, (prefix, seen)
    return "".join(out)


def gate_value(line):
    return [p.strip() for p in line[1:-1].split("|")][1]


def build(mutation):
    text = dossier_text
    if mutation == "baseline":
        return text
    if mutation == "blank_gate":
        return swap_line(text, GATE, "| Gate result |   |")
    if mutation == "filler_owner":
        return swap_line(text, OWNER, "| Owner | TODO |")
    if mutation == "duplicate_field":
        gline = [ln for ln in text.splitlines() if ln.startswith(GATE)][-1]
        return swap_line(text, GATE, gline + "\n" + gline)
    if mutation == "append_gate_contradiction":
        gline = [ln for ln in text.splitlines() if ln.startswith(GATE)][-1]
        new = gline[:-2].rstrip() + " Both conditions passed; R2 passes and is available. |"
        return swap_line(text, GATE, new)
    if mutation == "hold_inversion":
        return swap_line(
            text,
            SCOPE,
            "| Scope / disposition | The whole element should remain in supported canon with an uncertainty notice. Preserve the neutral note and evidence. This does not itself prove copying, source use, rights status, or canon. |",
        )
    if mutation == "map_note_collapse":
        nline = [ln for ln in text.splitlines() if ln.startswith(NOTE)][-1]
        return swap_line(text, MAP, "| Element-map target |" + nline.split("|", 2)[2])
    if mutation == "map_row_deleted":
        return "".join(
            ln for ln in text.splitlines(keepends=True) if not ln.startswith(MAP)
        )
    if mutation == "ws_internal_gate":
        gline = [ln for ln in text.splitlines() if ln.startswith(GATE)][-1]
        new = gline.replace("R2 unavailable.", "R2    unavailable.", 1)
        return swap_line(text, GATE, new)
    if mutation == "ws_edges_gate":
        gline = [ln for ln in text.splitlines() if ln.startswith(GATE)][-1]
        value = gate_value(gline)
        new = "| Gate result | \t" + value + " \t |"
        return swap_line(text, GATE, new)
    if mutation == "nonws_control_gate":
        gline = [ln for ln in text.splitlines() if ln.startswith(GATE)][-1]
        new = gline.replace("R2 unavailable.", "R2 unavailable!", 1)
        return swap_line(text, GATE, new)
    if mutation == "historical_table_edit":
        out, active = [], False
        for ln in text.splitlines(keepends=True):
            if ln.startswith("## Illustrative R8 review record"):
                active = True
            elif ln.startswith(MARK):
                active = False
            if active and ln.startswith("| Element and scope pointer |"):
                ln = ln[:-2].rstrip() + " MUTATED IN HISTORICAL TABLE. |\n"
            out.append(ln)
        return "".join(out)
    if mutation == "limits_sentence_removed":
        return text.replace(LIMITS_SENT, "a bounded example is made", 1)
    raise SystemExit("unknown mutation " + mutation)


def run(code, text, table, tmp):
    sub = Path(tmp) / "scratch"
    sub.mkdir(exist_ok=True)
    (sub / "corpus").mkdir(exist_ok=True)
    dpath = sub / "dossier.md"
    dpath.write_text(text)
    (sub / "corpus" / "knowledge").mkdir(exist_ok=True)
    (sub / "corpus" / "knowledge" / Path(TABLE_REL).name).write_text(table)
    env = dict(os.environ, D2_DOSSIER=str(dpath))
    proc = subprocess.run(
        [sys.executable, "-c", code],
        cwd=sub,
        env=env,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return proc


MUTATIONS = [
    "baseline",
    "blank_gate",
    "filler_owner",
    "duplicate_field",
    "append_gate_contradiction",
    "hold_inversion",
    "map_note_collapse",
    "map_row_deleted",
    "ws_internal_gate",
    "ws_edges_gate",
    "nonws_control_gate",
    "historical_table_edit",
    "limits_sentence_removed",
]

results = {}
tmp = tempfile.mkdtemp(prefix="f08-")
try:
    for name in MUTATIONS:
        text = build(name)
        proc = run(ACTIVE, text, table_text, tmp)
        finding = ""
        m = re.search(r"finding: (.+)", proc.stdout)
        if m:
            finding = m.group(1).strip()
        results[name] = (proc.returncode, finding)
        last = proc.stdout.strip().splitlines()[:1]
        print(
            f"{name:28s} exit={proc.returncode} finding={finding or '-':18s} "
            f"first={last[0] if last else '-'}"
        )
        if proc.stderr.strip():
            print("   stderr:", proc.stderr.strip()[:200])

    # source-content control: drop an R8 appendix string from a scratch table copy
    proc = run(ACTIVE, dossier_text, table_text.replace("creator denies using a source", "creator declines to comment", 1), tmp)
    m = re.search(r"finding: (.+)", proc.stdout)
    print(f"{'source_content_drop':28s} exit={proc.returncode} finding={(m.group(1).strip() if m else '-')}")
    results["source_content_drop"] = (proc.returncode, m.group(1).strip() if m else "")

    # historical block on the appended-contradiction dossier (must not detect)
    text = build("append_gate_contradiction")
    proc = run(HISTORICAL, text, table_text, tmp)
    print(f"{'historical_on_mutation':28s} exit={proc.returncode} stdout={proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else '-'}")
    results["historical_on_mutation"] = (proc.returncode, proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else "-")

    # historical block on the pristine dossier (its stated 5/5)
    proc = run(HISTORICAL, dossier_text, table_text, tmp)
    print(f"{'historical_baseline':28s} exit={proc.returncode} stdout={proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else '-'}")
    results["historical_baseline"] = (proc.returncode, proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else "-")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

out = ROOT / ".ufo/waves/round-93/deepseek/F08-results.json"
out.write_text(
    json.dumps(
        {
            "dossier_sha256": hashlib.sha256((ROOT / DOSSIER_REL).read_bytes()).hexdigest(),
            "table_sha256": hashlib.sha256((ROOT / TABLE_REL).read_bytes()).hexdigest(),
            "active_block_lines": len(ACTIVE.splitlines()),
            "digest_route_a": digest_a,
            "digest_route_b": digest_b,
            "digest_literal": DIGEST_LITERAL,
            "results": {k: {"exit": v[0], "finding": v[1]} for k, v in results.items()},
        },
        indent=2,
    )
    + "\n"
)
print("wrote", out)
