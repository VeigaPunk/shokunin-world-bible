#!/usr/bin/env python3
"""V78 cross-gate matrix. Writes only under this scratch directory."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V78-scratch"
MIRRORS = SCRATCH / "mirrors"
TRANS = SCRATCH / "transcripts"
SRC = ROOT / "corpus/fixtures/r98-clerk-filing"

MUTATIONS = ("clean", "edge-reduction", "prose-word-removal", "map-row-drop", "span-break")


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mutate(fixture, kind):
    if kind == "clean":
        return "unchanged"
    if kind == "edge-reduction":
        path = fixture / "timeline.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        found = False
        before = after = None
        for row in rows:
            if row.get("id") == "clerk-filing-open":
                before = list(row.get("depends_on", []))
                row["depends_on"] = [dep for dep in before if dep != "acknowledgment-aru-records"]
                after = row["depends_on"]
                found = True
        if not found:
            raise SystemExit("clerk-filing-open missing")
        path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return f"clerk-filing-open.depends_on {before} -> {after}"
    if kind == "prose-word-removal":
        path = fixture / "fictional-excerpts.md"
        text = path.read_text(encoding="utf-8")
        old = "Their tick-10 decision depends on both"
        new = "Their tick-10 decision on both"
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"prose anchor count {count}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return "removed word 'depends' from fictional-excerpts.md tick-10 sentence"
    if kind == "map-row-drop":
        path = fixture / "claim-excerpt-map.md"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        kept = [line for line in lines if not line.startswith("| J20 |")]
        dropped = len(lines) - len(kept)
        if dropped != 1:
            raise SystemExit(f"J20 drop count {dropped}")
        path.write_text("".join(kept), encoding="utf-8")
        return "deleted claim-excerpt-map.md row J20; declaration left at 20"
    if kind == "span-break":
        path = fixture / "claim-excerpt-map.md"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = 0
        out = []
        for line in lines:
            if line.startswith("| J20 |") and "| 55-64 |" in line:
                line = line.replace("| 55-64 |", "| 1 |", 1)
                changed += 1
            out.append(line)
        if changed != 1:
            raise SystemExit(f"span-break count {changed}")
        path.write_text("".join(out), encoding="utf-8")
        return "J20 line span 55-64 -> 1"
    raise SystemExit(f"unknown mutation {kind}")


def mirror(name, tool, contract, kind):
    dest = MIRRORS / name
    if dest.exists():
        shutil.rmtree(dest)
    fixture = dest / "corpus/fixtures/r98-clerk-filing"
    tools = dest / "corpus/tools"
    tools.mkdir(parents=True)
    shutil.copy2(tool, tools / "dependency_freeze.py")
    shutil.copy2(contract, tools / "dependency-freeze-contract.json")
    shutil.copytree(SRC, fixture)
    note = mutate(fixture, kind)
    return dest, note


def run(cmd, cwd):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def main():
    MIRRORS.mkdir(parents=True, exist_ok=True)
    TRANS.mkdir(parents=True, exist_ok=True)
    delivered_tool = ROOT / "corpus/tools/dependency_freeze.py"
    delivered_contract = ROOT / "corpus/tools/dependency-freeze-contract.json"
    baseline_tool = SCRATCH / "r98-tools/dependency_freeze.py"
    baseline_contract = SCRATCH / "r98-tools/dependency-freeze-contract.json"
    snap = SCRATCH / "snapshot"
    if snap.exists():
        shutil.rmtree(snap)
    snap.mkdir()
    shutil.copy2(delivered_tool, snap / "dependency_freeze.py")
    shutil.copy2(delivered_contract, snap / "dependency-freeze-contract.json")
    pins = {
        "delivered_tool": sha256_file(delivered_tool),
        "delivered_contract": sha256_file(delivered_contract),
        "baseline_tool": sha256_file(baseline_tool),
        "baseline_contract": sha256_file(baseline_contract),
        "r98_files": {p.name: sha256_file(p) for p in sorted(SRC.iterdir()) if p.is_file()},
    }
    (SCRATCH / "pins.json").write_text(json.dumps(pins, indent=2) + "\n", encoding="utf-8")
    summary = []
    for kind in MUTATIONS:
        for label, tool, contract in (
            ("delivered", snap / "dependency_freeze.py", snap / "dependency-freeze-contract.json"),
            ("baseline", baseline_tool, baseline_contract),
        ):
            dest, note = mirror(f"{label}-{kind}", tool, contract, kind)
            fixture = dest / "corpus/fixtures/r98-clerk-filing"
            freeze_cmd = [
                sys.executable,
                str(dest / "corpus/tools/dependency_freeze.py"),
                str(fixture),
            ]
            code, out, err = run(freeze_cmd, ROOT)
            rec = {
                "label": label,
                "kind": kind,
                "note": note,
                "freeze_exit": code,
                "freeze_stdout": out,
                "freeze_stderr": err,
            }
            if label == "delivered":
                for gate, cmd in (
                    ("check_bible", [sys.executable, str(ROOT / "corpus/fixtures/check_bible.py"), str(fixture)]),
                    ("support_check", [sys.executable, str(ROOT / "corpus/tools/support_check.py"), str(fixture)]),
                    ("map_obligations", [sys.executable, str(ROOT / "corpus/tools/map_obligations.py"), str(fixture)]),
                    ("boundary_doc_check", [sys.executable, str(ROOT / "corpus/tools/boundary_doc_check.py")]),
                ):
                    gcode, gout, gerr = run(cmd, ROOT)
                    rec[f"{gate}_exit"] = gcode
                    rec[f"{gate}_stdout"] = gout
                    rec[f"{gate}_stderr"] = gerr
            summary.append(rec)
            (TRANS / f"{label}-{kind}.txt").write_text(
                f"NOTE {note}\nFREEZE_EXIT {code}\n--- stdout ---\n{out}\n--- stderr ---\n{err}\n",
                encoding="utf-8",
            )
            if label == "delivered":
                blob = []
                for gate in ("check_bible", "support_check", "map_obligations", "boundary_doc_check"):
                    blob.append(f"=== {gate} EXIT {rec[f'{gate}_exit']} ===\n{rec[f'{gate}_stdout']}\n--- stderr ---\n{rec[f'{gate}_stderr']}\n")
                (TRANS / f"gates-{kind}.txt").write_text("".join(blob), encoding="utf-8")
    (SCRATCH / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("WROTE", SCRATCH / "summary.json")
    for rec in summary:
        gates = ""
        if rec["label"] == "delivered":
            gates = " bible={check_bible_exit} support={support_check_exit} map={map_obligations_exit} boundary={boundary_doc_check_exit}".format(**rec)
        finding = ""
        for line in rec["freeze_stdout"].splitlines():
            if line.startswith("FINDING") or line.startswith("RESULT") or line.startswith("FREEZE") or line.startswith("DIGEST"):
                finding += " | " + line
        print(f"{rec['label']:9} {rec['kind']:20} freeze={rec['freeze_exit']}{gates}{finding}")


if __name__ == "__main__":
    main()
