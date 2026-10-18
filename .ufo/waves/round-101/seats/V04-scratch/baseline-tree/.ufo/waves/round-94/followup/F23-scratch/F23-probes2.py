#!/usr/bin/env python3
"""F23 adversarial probe batch 2: grammar, paths, ambiguity, never-empty-success."""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SCRATCH = Path(__file__).resolve().parent
MAPOBL = ROOT / "corpus/tools/map_obligations.py"
SRC = ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"


def run(cmd, cwd=ROOT):
    p = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True, check=False)
    return p.returncode, p.stdout, p.stderr


def show(label, code, out, err, want_code, want_terminal, want_finding_prefix=None):
    term = [l for l in out.splitlines() if l.startswith("RESULT ")]
    found = [l for l in out.splitlines() if l.startswith("FINDING ")]
    ok = code == want_code and term == [f"RESULT {want_terminal}"] and not err
    if want_finding_prefix is not None:
        ok = ok and any(f.startswith(want_finding_prefix) for f in found)
    print(f"[{'PASS' if ok else 'CHECK'}] {label}: exit={code} {term} {found[:3]}")
    if not ok and err.strip():
        print(f"        stderr: {err.strip()[:200]}")
    return ok


results = []

with tempfile.TemporaryDirectory(prefix="f23b-", dir=SCRATCH) as tmp:
    tmp = Path(tmp)

    # 1. prose pointer (no inline code)
    p = tmp / "p_prose"
    shutil.copytree(SRC, p)
    mp = p / "claim-excerpt-map.md"
    mp.write_text(mp.read_text(encoding="utf-8").replace("`entities.json#/0/first_appearance`",
                                                         "entities.json#/0/first_appearance"), encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("prose pointer (no inline code)", c, o, e, 2, "ERROR", "FINDING unsupported_map"))

    # 2. malformed raw JSON
    p = tmp / "p_malformed"
    shutil.copytree(SRC, p)
    (p / "timeline.json").write_text("{not json", encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("malformed raw JSON", c, o, e, 2, "ERROR", "FINDING malformed_json"))

    # 3. traversal --map path
    p = tmp / "p_traversal"
    shutil.copytree(SRC, p)
    c, o, e = run([sys.executable, "-B", MAPOBL, p, "--map", "../../claim-excerpt-map.md"])
    results.append(show("traversal --map path", c, o, e, 2, "ERROR", "FINDING unsafe_path"))

    # 4. duplicate mapping row
    p = tmp / "p_dup"
    shutil.copytree(SRC, p)
    mp = p / "claim-excerpt-map.md"
    lines = mp.read_text(encoding="utf-8").splitlines()
    idx = next(i for i, l in enumerate(lines) if "entities.json#/0/first_appearance" in l)
    lines.insert(idx + 1, lines[idx])
    mp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("duplicate mapping row", c, o, e, 1, "FAIL", "FINDING duplicate_mapping"))

    # 5. source-ID mismatch
    p = tmp / "p_mismatch"
    shutil.copytree(SRC, p)
    mp = p / "claim-excerpt-map.md"
    text = mp.read_text(encoding="utf-8")
    lines = text.splitlines()
    idx = next(i for i, l in enumerate(lines) if "entities.json#/0/first_appearance" in l)
    cells = [c.strip() for c in lines[idx].strip().strip("|").split("|")]
    print(f"        columns={len(cells)}; source column was {cells[2]!r}")
    cells[2] = "`wrong-source-id`"
    lines[idx] = "| " + " | ".join(cells) + " |"
    mp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("source-ID mismatch", c, o, e, 1, "FAIL", "FINDING source_id_mismatch"))

    # 6. unrecognized pointer-column header
    p = tmp / "p_header"
    shutil.copytree(SRC, p)
    mp = p / "claim-excerpt-map.md"
    mp.write_text(mp.read_text(encoding="utf-8").replace("JSON fact pointer and fields", "Pointer"),
                  encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("unrecognized pointer-column header", c, o, e, 2, "ERROR", "FINDING unsupported_map"))

    # 7. two candidate conventional maps -> ambiguity must be ERROR
    p = tmp / "p_ambiguous"
    shutil.copytree(SRC, p)
    (p / "claim-to-excerpt-map.md").write_bytes((p / "claim-excerpt-map.md").read_bytes())
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("two candidate maps present", c, o, e, 2, "ERROR", "FINDING unsupported_map"))

    # 8. new entity with first_appearance and claim, neither mapped -> both must be missing
    p = tmp / "p_new_entity"
    shutil.copytree(SRC, p)
    ep = p / "entities.json"
    entities = json.loads(ep.read_text(encoding="utf-8"))
    entities.append({"id": "f23-new", "first_appearance": "f23-injected-source",
                     "claims": [{"statement": "new claim", "source_id": "f23-injected-source"}]})
    ep.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    found = [l for l in o.splitlines() if l.startswith("FINDING ")]
    want = ["FINDING missing_obligation: entities.json#/4/claims/0 has no map row",
            "FINDING missing_obligation: entities.json#/4/first_appearance has no map row"]
    ok = c == 1 and [l for l in o.splitlines() if l.startswith("RESULT ")] == ["RESULT FAIL"] and found == want and not e
    print(f"[{'PASS' if ok else 'CHECK'}] new entity both obligations missing: exit={c} {found}")
    results.append(ok)

    # 9. map row for an obligation placed outside the JSON facts section -> still missing (no false PASS)
    p = tmp / "p_other_section"
    shutil.copytree(SRC, p)
    mp = p / "claim-excerpt-map.md"
    lines = mp.read_text(encoding="utf-8").splitlines()
    idx = next(i for i, l in enumerate(lines) if "entities.json#/0/first_appearance" in l)
    row = lines.pop(idx)
    lines.append("")
    lines.append("## Editorial comparisons")
    lines.append("")
    lines.append(row)
    mp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    c, o, e = run([sys.executable, "-B", MAPOBL, p])
    results.append(show("row moved outside JSON facts section", c, o, e, 1, "FAIL",
                        "FINDING missing_obligation: entities.json#/0/first_appearance has no map row"))

print(f"\nF23 probe batch 2: {'PASS' if all(results) else 'FAIL'} ({sum(results)}/{len(results)})")
raise SystemExit(0 if all(results) else 1)
