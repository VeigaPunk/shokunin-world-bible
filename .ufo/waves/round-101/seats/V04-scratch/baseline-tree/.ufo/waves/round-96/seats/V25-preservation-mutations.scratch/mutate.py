#!/usr/bin/env python3
"""V25 preservation-mutation harness: mutate scratch copies of the r96 fixture and run the gates."""
import json, shutil, subprocess, sys, re
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = ROOT / "corpus/fixtures/r96-crossing-response"
SCRATCH = Path(__file__).resolve().parent
NAME = "r96-crossing-response"


def fresh(tag):
    dst_parent = SCRATCH / tag
    if dst_parent.exists():
        shutil.rmtree(dst_parent)
    dst_parent.mkdir(parents=True)
    dst = dst_parent / NAME
    shutil.copytree(SRC, dst)
    return dst


def map_rows(text):
    """Return (lines, list of (line_index, cells)) for JSON-fact table rows."""
    lines = text.split("\n")
    rows = []
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("|") and re.match(r"^\s*\|\s*J\d+\s*\|", ln):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows.append((i, cells))
    return lines, rows


def header_cells(text):
    for ln in text.split("\n"):
        if ln.lstrip().startswith("|") and "anchor" in ln.lower():
            return [c.strip() for c in ln.strip().strip("|").split("|")]
    raise SystemExit("no header")


def mut_span_break(dst):
    p = dst / "claim-excerpt-map.md"
    text = p.read_text()
    hdr = header_cells(text)
    lines, rows = map_rows(text)
    i, cells = rows[-1]  # last JSON fact row
    anchor = cells[hdr.index("Exact anchor") if "Exact anchor" in hdr else len(cells) - 1].strip("`")
    excerpt = cells[hdr.index("Excerpt path")].strip("`")
    span_idx = hdr.index("Line span")
    hits = subprocess.run(["grep", "-nF", "--", anchor, str(dst / excerpt)],
                          capture_output=True, text=True).stdout.splitlines()
    anchor_line = int(hits[0].split(":")[0]) if hits else 1
    new_span = "1" if anchor_line != 1 else "999"
    cells[span_idx] = new_span
    lines[i] = "| " + " | ".join(cells) + " |"
    p.write_text("\n".join(lines))
    return f"row {cells[0]}: span -> {new_span} (anchor at line {anchor_line})"


def mut_row_drop(dst):
    p = dst / "claim-excerpt-map.md"
    text = p.read_text()
    lines, rows = map_rows(text)
    i, cells = rows[-1]
    del lines[i]
    p.write_text("\n".join(lines))
    return f"dropped map row {cells[0]}"


def mut_key_row_deletion(dst):
    p = dst / "claim-excerpt-map.md"
    text = p.read_text()
    lines, rows = map_rows(text)
    # pick first entity index with a claims row in the map
    ent = json.loads((dst / "entities.json").read_text())
    idx = next(i for i, e in enumerate(ent) if isinstance(e.get("claims"), list) and e["claims"])
    pointer = f"entities.json#/{idx}/claims/0"
    victim = None
    for i, cells in rows:
        if pointer in " ".join(cells):
            victim = (i, cells)
            break
    if victim is None:
        raise SystemExit(f"no map row for {pointer}")
    i, cells = victim
    del lines[i]
    p.write_text("\n".join(lines))
    del ent[idx]["claims"]
    (dst / "entities.json").write_text(json.dumps(ent, indent=2) + "\n")
    return f"deleted entities[{idx}].claims + map row {cells[0]} ({pointer})"


def mut_reduction(dst):
    p = dst / "timeline.json"
    tl = json.loads(p.read_text())
    ev = next(e for e in tl if e["id"] == "paired-crossing-decision")
    before = list(ev["depends_on"])
    ev["depends_on"] = [d for d in before if d != "evin-ninth-bell"]
    p.write_text(json.dumps(tl, indent=2) + "\n")
    return f"paired-crossing-decision.depends_on {before} -> {ev['depends_on']}"


def mut_addition(dst):
    p = dst / "timeline.json"
    tl = json.loads(p.read_text())
    ev = next(e for e in tl if e["id"] == "paired-crossing-decision")
    before = list(ev["depends_on"])
    ev["depends_on"] = sorted(before + ["aftermath-missing-evin"])
    p.write_text(json.dumps(tl, indent=2) + "\n")
    return f"paired-crossing-decision.depends_on {before} -> {ev['depends_on']}"


MUTS = {
    "m1-span-break": mut_span_break,
    "m2-row-drop": mut_row_drop,
    "m3-key-row-deletion": mut_key_row_deletion,
    "m4-reduction": mut_reduction,
    "m5-addition": mut_addition,
}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    out = (r.stdout + r.stderr).strip()
    result = next((l for l in out.splitlines() if l.startswith("RESULT")), "")
    findings = [l for l in out.splitlines() if l.startswith("FINDING")]
    return r.returncode, result, findings, out


def main():
    only = sys.argv[1:] or list(MUTS)
    report = []
    # baseline
    if "m0-baseline" in only or not sys.argv[1:]:
        dst = fresh("m0-baseline")
        report.append(("m0-baseline", "unmutated copy", dst, [
            ("check_bible", run(["python3", "corpus/fixtures/check_bible.py", str(dst)])),
            ("support_check", run(["python3", "corpus/tools/support_check.py", str(dst)])),
            ("map_obligations", run(["python3", "corpus/tools/map_obligations.py", str(dst)])),
            ("dependency_freeze", run(["python3", "corpus/tools/dependency_freeze.py", str(dst)])),
        ]))
    for tag in only:
        if tag == "m0-baseline" or tag not in MUTS:
            continue
        dst = fresh(tag)
        detail = MUTS[tag](dst)
        report.append((tag, detail, dst, [
            ("check_bible", run(["python3", "corpus/fixtures/check_bible.py", str(dst)])),
            ("support_check", run(["python3", "corpus/tools/support_check.py", str(dst)])),
            ("map_obligations", run(["python3", "corpus/tools/map_obligations.py", str(dst)])),
            ("dependency_freeze", run(["python3", "corpus/tools/dependency_freeze.py", str(dst)])),
        ]))
    print("| mutation | gate | exit | result | findings |")
    print("|---|---|---:|---|---|")
    for tag, detail, dst, runs in report:
        for gate, (code, result, findings, out) in runs:
            print(f"| {tag} | {gate} | {code} | {result} | {'; '.join(findings) or '-'} |")
        print(f"| {tag} | MUTATION | - | {detail} | - |")
    # full outputs to files
    for tag, detail, dst, runs in report:
        with open(SCRATCH / f"{tag}.log", "w") as fh:
            fh.write(f"# {tag}: {detail}\n# dir={dst}\n\n")
            for gate, (code, result, findings, out) in runs:
                fh.write(f"===== {gate} exit={code} =====\n{out}\n\n")
    print(f"\nlogs written to {SCRATCH}")


if __name__ == "__main__":
    main()
