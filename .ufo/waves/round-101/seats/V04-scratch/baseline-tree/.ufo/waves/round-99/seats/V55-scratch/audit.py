#!/usr/bin/env python3
"""V55 claim-text audit measurements. Read-only against the lane tree.
Writes only under V55-scratch. Run from anywhere; paths are absolute.
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V55-scratch"
OUT = SCRATCH / "audit-out"
OUT.mkdir(parents=True, exist_ok=True)
PY = sys.executable

PINNED = (
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)
CHAIN = (
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(argv, cwd=LANE, timeout=180):
    proc = subprocess.run(
        argv, cwd=cwd, capture_output=True, text=True, timeout=timeout,
    )
    return {
        "argv": [str(a) for a in argv],
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def section(name, payload):
    path = OUT / name
    if isinstance(payload, (dict, list)):
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        path.write_text(str(payload), encoding="utf-8")
    print(f"WROTE {path.name} ({path.stat().st_size} bytes)")


def measure_hashes():
    paths = [
        LANE / "corpus/tools/dependency_freeze.py",
        LANE / "corpus/tools/dependency-freeze-contract.json",
        LANE / "corpus/tools/README.md",
        LANE / "SKILL.md",
        LANE / "corpus/knowledge/r99-gate-blind-spot-table.md",
        LANE / "corpus/knowledge/r99-lapse-scope-note.md",
    ]
    fix = LANE / "corpus/fixtures/r99-window-lapse"
    if fix.is_dir():
        paths.extend(sorted(fix.iterdir()))
    rows = []
    for path in paths:
        if path.is_file():
            rows.append({"path": str(path.relative_to(LANE)), "sha256": sha256_file(path), "bytes": path.stat().st_size})
        else:
            rows.append({"path": str(path.relative_to(LANE)) if str(path).startswith(str(LANE)) else str(path), "missing": True})
    section("hashes.json", rows)


def measure_contract():
    path = LANE / "corpus/tools/dependency-freeze-contract.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    pins = data.get("pins", {})
    summary = {
        "schema_version": data.get("schema_version"),
        "revision": data.get("revision"),
        "pin_names": list(pins),
        "self_test_expected": sorted((data.get("self_test") or {}).get("expected", {})),
        "self_test_n": len((data.get("self_test") or {}).get("expected", {})),
        "precedence": data.get("precedence"),
        "data_files": data.get("data_files"),
        "required_files": data.get("required_files"),
    }
    per = {}
    for name, pin in pins.items():
        files = pin.get("files") if isinstance(pin, dict) else None
        per[name] = {
            "keys": sorted(pin) if isinstance(pin, dict) else None,
            "payload_schema_version": pin.get("payload_schema_version") if isinstance(pin, dict) else None,
            "pinned_files": pin.get("pinned_files") if isinstance(pin, dict) else None,
            "file_names": sorted(files) if isinstance(files, dict) else None,
            "file_count": len(files) if isinstance(files, dict) else None,
            "counts": pin.get("counts") if isinstance(pin, dict) else None,
            "fixture": pin.get("fixture") if isinstance(pin, dict) else None,
            "content_sha256": pin.get("content_sha256") if isinstance(pin, dict) else None,
        }
    summary["pins"] = per
    section("contract.json", summary)


def measure_fixture_shape():
    fix = LANE / "corpus/fixtures/r99-window-lapse"
    base = LANE / "corpus/fixtures/r98-clerk-filing"
    rows = []
    for name in PINNED:
        a = fix / name
        b = base / name
        row = {"name": name, "r99_exists": a.is_file(), "r98_exists": b.is_file()}
        if a.is_file() and b.is_file():
            ab = a.read_bytes()
            bb = b.read_bytes()
            row["identical"] = ab == bb
            row["r99_bytes"] = len(ab)
            row["r98_bytes"] = len(bb)
            row["r99_startswith_r98"] = ab.startswith(bb)
        rows.append(row)
    parsed = {}
    for name in ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json"):
        data = json.loads((fix / name).read_text(encoding="utf-8"))
        parsed[name] = len(data) if isinstance(data, list) else type(data).__name__
    timeline = json.loads((fix / "timeline.json").read_text(encoding="utf-8"))
    sources = json.loads((fix / "sources.json").read_text(encoding="utf-8"))
    entities = json.loads((fix / "entities.json").read_text(encoding="utf-8"))
    last = timeline[-1] if timeline else None
    last_src = sources[-1] if sources else None
    section("fixture-shape.json", {
        "counts": parsed,
        "cmp": rows,
        "last_event": last,
        "last_source_id": last_src.get("id") if isinstance(last_src, dict) else None,
        "entity_ids": [e.get("id") for e in entities if isinstance(e, dict)],
        "n_entities": len(entities),
    })


def measure_prefix():
    """Parsed-prefix identity of r99 JSON arrays vs r98."""
    out = {}
    for name in ("entities.json", "sources.json", "timeline.json", "relations.json"):
        a = json.loads((LANE / "corpus/fixtures/r99-window-lapse" / name).read_text(encoding="utf-8"))
        b = json.loads((LANE / "corpus/fixtures/r98-clerk-filing" / name).read_text(encoding="utf-8"))
        out[name] = {
            "r99": len(a),
            "r98": len(b),
            "prefix_equal": a[: len(b)] == b,
            "r99_tail_ids": [x.get("id") for x in a[len(b):]] if isinstance(a, list) else None,
        }
    section("prefix.json", out)


def measure_gates():
    fix = "corpus/fixtures/r99-window-lapse"
    results = {}
    for label, argv in (
        ("check_bible", [PY, "corpus/fixtures/check_bible.py", fix]),
        ("map_obligations", [PY, "corpus/tools/map_obligations.py", fix]),
        ("support_check", [PY, "corpus/tools/support_check.py", fix]),
    ):
        results[label] = run(argv, timeout=120)
    section("gates.json", results)
    for label, rec in results.items():
        tail = "\n".join(rec["stdout"].splitlines()[-8:])
        print(f"--- {label} exit={rec['exit']} ---")
        print(tail)


def measure_freeze_verify():
    results = []
    for name in CHAIN:
        rec = run([PY, "corpus/tools/dependency_freeze.py", f"corpus/fixtures/{name}"], timeout=60)
        results.append({"fixture": name, "exit": rec["exit"], "stdout": rec["stdout"], "stderr": rec["stderr"]})
        print(f"VERIFY {name} exit={rec['exit']} last={rec['stdout'].strip().splitlines()[-1:]}")
    section("chain-verify.json", results)


def measure_self_test():
    rec = run([PY, "corpus/tools/dependency_freeze.py", "--self-test"], timeout=180)
    section("self-test.txt", rec["stdout"] + "\n---stderr---\n" + rec["stderr"] + f"\nEXIT {rec['exit']}\n")
    print("SELF-TEST exit", rec["exit"])
    for line in rec["stdout"].splitlines():
        if line.startswith("SELF-TEST") or line.startswith("RESULT") or "MISMATCH" in line or line.startswith("CASE markdown"):
            print(line)


def measure_census():
    root = LANE / "corpus/fixtures"
    dirs = sorted(d for d in os.listdir(root) if (root / d).is_dir())
    clean = negative = violation_lines = 0
    odd = []
    for d in dirs:
        rel = f"corpus/fixtures/{d}"
        proc = subprocess.run(
            [PY, "corpus/fixtures/check_bible.py", rel],
            cwd=LANE, capture_output=True, text=True,
        )
        out = (proc.stdout + proc.stderr).strip()
        if proc.returncode == 0:
            clean += 1
        elif proc.returncode == 1:
            negative += 1
            violation_lines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
        else:
            odd.append({"rel": rel, "exit": proc.returncode, "out": out[:400]})
    res = {
        "fixture_dirs": len(dirs),
        "clean_exit0": clean,
        "negative_exit1": negative,
        "violation_lines": violation_lines,
        "non_0_1_exits": odd,
        "has_r99": "r99-window-lapse" in dirs,
    }
    section("census.json", res)
    print(json.dumps(res))


def main():
    which = sys.argv[1:] or ["hashes", "contract", "shape", "prefix"]
    dispatch = {
        "hashes": measure_hashes,
        "contract": measure_contract,
        "shape": measure_fixture_shape,
        "prefix": measure_prefix,
        "gates": measure_gates,
        "verify": measure_freeze_verify,
        "selftest": measure_self_test,
        "census": measure_census,
    }
    for name in which:
        dispatch[name]()


if __name__ == "__main__":
    main()
