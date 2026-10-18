#!/usr/bin/env python3
"""Scratch-only probes for the r99 claim-text audit. Does not write the live tree."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V55-scratch"
PROBE = SCRATCH / "probe"
OUT = SCRATCH / "audit-out" / "probes.txt"
PY = sys.executable
PINNED = [
    "entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json",
    "README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md", "source-excerpt.md",
]


def run(argv, cwd):
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def emit(lines, text):
    lines.append(text.rstrip("\n"))
    print(text.rstrip("\n"))


def main():
    if PROBE.exists():
        shutil.rmtree(PROBE)
    lines = []
    before = PROBE / "before"
    after = PROBE / "after"
    for root in (before, after):
        (root / "corpus/tools").mkdir(parents=True)
        (root / "corpus/fixtures").mkdir(parents=True)

    tool_before = subprocess.check_output(
        ["git", "-C", str(LANE), "show", "4265df5:corpus/tools/dependency_freeze.py"]
    )
    contract_before = subprocess.check_output(
        ["git", "-C", str(LANE), "show", "4265df5:corpus/tools/dependency-freeze-contract.json"]
    )
    (before / "corpus/tools/dependency_freeze.py").write_bytes(tool_before)
    (before / "corpus/tools/dependency-freeze-contract.json").write_bytes(contract_before)
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", before / "corpus/fixtures/r98-clerk-filing")

    shutil.copy(LANE / "corpus/tools/dependency_freeze.py", after / "corpus/tools/dependency_freeze.py")
    shutil.copy(LANE / "corpus/tools/dependency-freeze-contract.json", after / "corpus/tools/dependency-freeze-contract.json")
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", after / "corpus/fixtures/r98-clerk-filing")
    shutil.copytree(LANE / "corpus/fixtures/r88-m3-maya-cluster", after / "corpus/fixtures/r88-m3-maya-cluster")

    def verify(root, fixture_rel):
        tool = root / "corpus/tools/dependency_freeze.py"
        return run([PY, str(tool), str(root / fixture_rel)], cwd=root)

    emit(lines, "=== AFTER clean r98 ===")
    code, out, err = verify(after, "corpus/fixtures/r98-clerk-filing")
    emit(lines, out)
    emit(lines, f"exit={code} stderr={err.strip()}")

    emit(lines, "=== BEFORE clean r98 (baseline tool 4265df5) ===")
    code, out, err = verify(before, "corpus/fixtures/r98-clerk-filing")
    emit(lines, out)
    emit(lines, f"exit={code} stderr={err.strip()}")

    phrase = "depends on"
    excerpt_rel = Path("corpus/fixtures/r98-clerk-filing/fictional-excerpts.md")
    for label, root in (("BEFORE", before), ("AFTER", after)):
        path = root / excerpt_rel
        raw = path.read_text(encoding="utf-8")
        if phrase not in raw:
            emit(lines, f"{label} phrase missing")
            continue
        path.write_text(raw.replace(phrase, "comes after", 1), encoding="utf-8")
        emit(lines, f"=== {label} prose removal '{phrase}' -> 'comes after' ===")
        code, out, err = verify(root, "corpus/fixtures/r98-clerk-filing")
        emit(lines, out)
        emit(lines, f"exit={code}")
        for gate, argv in (
            ("check_bible", [PY, str(LANE / "corpus/fixtures/check_bible.py"), str(root / "corpus/fixtures/r98-clerk-filing")]),
            ("support_check", [PY, str(LANE / "corpus/tools/support_check.py"), str(root / "corpus/fixtures/r98-clerk-filing")]),
            ("map_obligations", [PY, str(LANE / "corpus/tools/map_obligations.py"), str(root / "corpus/fixtures/r98-clerk-filing")]),
        ):
            gcode, gout, gerr = run(argv, LANE)
            tail = "\n".join(gout.strip().splitlines()[-3:])
            emit(lines, f"{label} {gate} exit={gcode} tail={tail}")

    # restore after excerpt from live, then per-file newline tamper
    live_fix = LANE / "corpus/fixtures/r98-clerk-filing"
    fix = after / "corpus/fixtures/r98-clerk-filing"
    shutil.rmtree(fix)
    shutil.copytree(live_fix, fix)
    emit(lines, "=== AFTER per-file newline tamper ===")
    for name in PINNED:
        shutil.rmtree(fix)
        shutil.copytree(live_fix, fix)
        target = fix / name
        target.write_bytes(target.read_bytes() + b"\n")
        code, out, err = verify(after, "corpus/fixtures/r98-clerk-filing")
        finding = next((line for line in out.splitlines() if line.startswith("FINDING")), "")
        emit(lines, f"{name} exit={code} {finding}")

    emit(lines, "=== AFTER semantic edge drop (should NOT be digest-first) ===")
    shutil.rmtree(fix)
    shutil.copytree(live_fix, fix)
    timeline = json.loads((fix / "timeline.json").read_text(encoding="utf-8"))
    for event in timeline:
        if event.get("id") == "clerk-filing-open":
            event["depends_on"] = []
    (fix / "timeline.json").write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    code, out, err = verify(after, "corpus/fixtures/r98-clerk-filing")
    emit(lines, out)
    emit(lines, f"exit={code}")

    emit(lines, "=== AFTER non-semantic JSON claim-text edit ===")
    shutil.rmtree(fix)
    shutil.copytree(live_fix, fix)
    sources = json.loads((fix / "sources.json").read_text(encoding="utf-8"))
    sources[0]["reliability_note"] = sources[0].get("reliability_note", "") + " (probe)"
    (fix / "sources.json").write_text(json.dumps(sources, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    code, out, err = verify(after, "corpus/fixtures/r98-clerk-filing")
    emit(lines, out)
    emit(lines, f"exit={code}")

    emit(lines, "=== AFTER r88 extra-file tamper (symbolism-clause-map.md) ===")
    extra = after / "corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md"
    extra.write_bytes(extra.read_bytes() + b"\n")
    code, out, err = verify(after, "corpus/fixtures/r88-m3-maya-cluster")
    emit(lines, out)
    emit(lines, f"exit={code}")

    emit(lines, "=== live r99 unpinned ===")
    code, out, err = run(
        [PY, str(LANE / "corpus/tools/dependency_freeze.py"), "corpus/fixtures/r99-window-lapse"],
        LANE,
    )
    emit(lines, out)
    emit(lines, f"exit={code} stderr={err.strip()}")

    emit(lines, "=== scratch re-freeze reproducibility (live fixtures, scratch contract) ===")
    refreeze_contract = PROBE / "refreeze-contract.json"
    shutil.copy(LANE / "corpus/tools/dependency-freeze-contract.json", refreeze_contract)
    tool_text = (LANE / "corpus/tools/dependency_freeze.py").read_text(encoding="utf-8")
    tool_text = tool_text.replace(
        'ROOT = Path(__file__).resolve().parents[2]',
        f'ROOT = Path("{LANE}")',
    )
    tool_text = tool_text.replace(
        'CONTRACT_PATH = ROOT / "corpus/tools/dependency-freeze-contract.json"',
        f'CONTRACT_PATH = Path("{refreeze_contract}")',
    )
    patched = PROBE / "dependency_freeze_refreeze.py"
    patched.write_text(tool_text, encoding="utf-8")
    for name in (
        "r88-m3-maya-cluster",
        "r94-paired-crossing",
        "r95-crossing-aftermath",
        "r96-crossing-response",
        "r97-crossing-acknowledgment",
        "r98-clerk-filing",
    ):
        code, out, err = run([PY, str(patched), "--freeze", f"corpus/fixtures/{name}"], LANE)
        emit(lines, f"FREEZE {name} exit={code}")
        emit(lines, out)
        if err.strip():
            emit(lines, f"stderr={err.strip()}")
    live = json.loads((LANE / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    regen = json.loads(refreeze_contract.read_text(encoding="utf-8"))
    for name, live_pin in live["pins"].items():
        regen_pin = regen["pins"][name]
        emit(lines, f"pin {name} equal={live_pin == regen_pin}")
        if live_pin != regen_pin:
            for key in sorted(set(live_pin) | set(regen_pin)):
                if live_pin.get(key) != regen_pin.get(key):
                    emit(lines, f"  differ {key}")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()
