#!/usr/bin/env python3
"""V42 integration-checklist harness: C1/C2/C3 verification for round 96."""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = ROOT / ".ufo/waves/round-96/seats/V42-scratch"
FIX96 = ROOT / "corpus/fixtures/r96-crossing-response"
FIX95 = ROOT / "corpus/fixtures/r95-crossing-aftermath"

log = []


def run(cmd, cwd=ROOT):
    result = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def note(line):
    print(line, flush=True)
    log.append(line)


def check(name, ok, detail=""):
    note(f"[{'PASS' if ok else 'FAIL'}] {name}{' — ' + detail if detail else ''}")
    return ok


results = {}


def main():
    # ---------------- C1 ----------------
    # C1b: self-test and contract
    rc, out, err = run(["python3", "corpus/tools/map_obligations.py", "--self-test"])
    pass_lines = [l for l in out.splitlines() if l.startswith("SELF-TEST PASS")]
    fail_lines = [l for l in out.splitlines() if l.startswith("SELF-TEST FAIL")]
    contract = json.load(open(ROOT / "corpus/tools/map-obligations-contract.json"))
    cases = contract["self_test"]["cases"]
    ids = [c["id"] for c in cases]
    results["c1_selftest"] = {
        "exit": rc, "pass_lines": len(pass_lines), "fail_lines": len(fail_lines),
        "result_line": [l for l in out.splitlines() if l.startswith("RESULT")],
        "contract_cases": len(cases), "ids": ids,
    }
    check("C1b self-test exit 0", rc == 0, f"exit={rc}")
    check("C1b 24 SELF-TEST PASS lines", len(pass_lines) == 24, f"n={len(pass_lines)}")
    check("C1b 0 FAIL lines", not fail_lines, f"n={len(fail_lines)}")
    check("C1b contract 24 cases", len(cases) == 24, f"n={len(cases)}")
    check("C1b pins schema_drift+inventory_mismatch",
          any("schema_drift" in json.dumps(c) for c in cases)
          and any("inventory_mismatch" in json.dumps(c) for c in cases))

    # C1a: deletion class gating (stale declaration variant)
    work = SCRATCH / "c1a_del"
    if work.exists():
        shutil.rmtree(work)
    shutil.copytree(FIX96, work)
    ents = json.load(open(work / "entities.json"))
    del ents[0]["claims"]
    json.dump(ents, open(work / "entities.json", "w"), indent=2, ensure_ascii=False)
    mp = work / "claim-excerpt-map.md"
    lines = mp.read_text().splitlines()
    kept = [l for l in lines if "entities.json#/0/claims/0" not in l]
    mp.write_text("\n".join(kept) + "\n")
    rc, out, err = run(["python3", "corpus/tools/map_obligations.py", str(work)])
    results["c1a_deletion_stale"] = {"exit": rc, "stdout": out}
    check("C1a deletion-class exit 1", rc == 1, f"exit={rc}")
    check("C1a inventory_mismatch FINDING", "FINDING inventory_mismatch" in out)
    note("    stdout: " + " | ".join(out.strip().splitlines()))

    # C1a bound: consistent regeneration (declared adjusted) — reported as bound
    work2 = SCRATCH / "c1a_consistent"
    if work2.exists():
        shutil.rmtree(work2)
    shutil.copytree(work, work2)
    mp2 = work2 / "claim-excerpt-map.md"
    t = mp2.read_text()
    m = re.search(r"\*\*Expected inventory:\*\* (\d+) JSON facts; (\d+) editorial rows; (\d+) total mapped rows; (\d+) distinct excerpt anchors\.", t)
    if m:
        f, e, _, a = (int(x) for x in m.groups())
        t = t.replace(m.group(0), f"**Expected inventory:** {f-1} JSON facts; {e} editorial rows; {f-1+e} total mapped rows; {a} distinct excerpt anchors.")
    mp2.write_text(t)
    rc2, out2, _ = run(["python3", "corpus/tools/map_obligations.py", str(work2)])
    results["c1a_consistent_bound"] = {"exit": rc2, "stdout": out2}
    note(f"    BOUND consistent-regeneration exit={rc2}")

    # C1c: dual pointer in legacy dialect cell
    work3 = SCRATCH / "c1c_dual"
    if work3.exists():
        shutil.rmtree(work3)
    shutil.copytree(ROOT / "corpus/fixtures/r88-m3-maya-cluster", work3)
    mp3 = work3 / "claim-excerpt-map.md"
    t = mp3.read_text()
    old = "| E1 | `entities[0].claims[0]`: Aru carries the north lantern at Quiet Rise at tick 9 |"
    new = "| E1 | `entities[0].claims[0]`: Aru carries the north lantern at Quiet Rise at tick 9 (see also `entities[1].first_appearance`) |"
    assert old in t
    mp3.write_text(t.replace(old, new))
    rc3, out3, _ = run(["python3", "corpus/tools/map_obligations.py", str(work3)])
    results["c1c_dual"] = {"exit": rc3, "stdout": out3}
    check("C1c dual_pointer exit 1", rc3 == 1, f"exit={rc3}")
    check("C1c dual_pointer FINDING", "FINDING dual_pointer" in out3)
    note("    stdout: " + " | ".join(out3.strip().splitlines()))

    # C1c non-regression: unmodified r88 legacy map still exit 0
    rc4, out4, _ = run(["python3", "corpus/tools/map_obligations.py", "corpus/fixtures/r88-m3-maya-cluster"])
    check("C1 non-reg r88 exit 0", rc4 == 0 and "OBLIGATIONS raw=10 mapped=10" in out4, f"exit={rc4}")
    results["c1_r88"] = {"exit": rc4, "stdout": out4}

    # C1 non-regression matrix
    matrix = {}
    for d in ["r87-myth-cluster", "r88-m3-maya-cluster", "r89-inspiration-paraphrase",
              "r93-m2-kojiki-cluster", "r94-paired-crossing", "r95-crossing-aftermath",
              "r96-crossing-response"]:
        rc, out, _ = run(["python3", "corpus/tools/map_obligations.py", f"corpus/fixtures/{d}"])
        obl = re.search(r"OBLIGATIONS raw=(\d+) mapped=(\d+)", out)
        matrix[d] = {"exit": rc, "raw": int(obl.group(1)) if obl else None,
                     "mapped": int(obl.group(2)) if obl else None,
                     "mismatch": "MISMATCH" in out,
                     "first_line": out.strip().splitlines()[0] if out.strip() else ""}
    results["c1_matrix"] = matrix
    for d, v in matrix.items():
        note(f"    matrix {d}: exit={v['exit']} raw={v['raw']} mapped={v['mapped']} mismatch={v['mismatch']}")

    # frozen r93 replay
    rc, out, _ = run(["python3", "corpus/tools/map_obligations.py", "--frozen",
                      ".ufo/waves/round-94/frozen/map-obligations-r93"])
    check("C1 frozen r93 replay exit 0", rc == 0 and "digests=verified" in out, f"exit={rc}")
    results["c1_frozen"] = {"exit": rc, "stdout": out}

    # ---------------- C2 ----------------
    counts = {f: len(json.load(open(FIX96 / f))) for f in
              ["entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json"]}
    results["c2_counts"] = counts
    check("C2 counts 5/1/5/5/0", counts == {"entities.json": 5, "relations.json": 1,
          "timeline.json": 5, "sources.json": 5, "contradictions.json": 0}, json.dumps(counts))

    rc, out, _ = run(["python3", "corpus/fixtures/check_bible.py", "corpus/fixtures/r96-crossing-response"])
    check("C2 check_bible CLEAN exit 0", rc == 0 and "CLEAN" in out, f"exit={rc} out={out.strip()}")
    results["c2_check_bible"] = {"exit": rc, "stdout": out}

    rc, out, _ = run(["python3", "corpus/tools/map_obligations.py", "corpus/fixtures/r96-crossing-response"])
    check("C2 map_obligations 16/16 exit 0", rc == 0 and "raw=16 mapped=16" in out and "MISMATCH" not in out, f"exit={rc}")
    results["c2_map"] = {"exit": rc, "stdout": out}

    rc, out, _ = run(["python3", "corpus/tools/support_check.py", "corpus/fixtures/r96-crossing-response"])
    check("C2 support_check exit 0", rc == 0 and "RESULT PASS" in out, f"exit={rc}")
    results["c2_support"] = {"exit": rc, "stdout": out}

    # inherited rows identical: compare r95 vs r96 map rows for common pointers
    def rows(path):
        text = path.read_text()
        section = text.split("## JSON facts", 1)[1]
        table = {}
        for line in section.splitlines():
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 7 or cells[0] in ("ID", "") or set(cells[0]) <= set("-: "):
                continue
            table[cells[0]] = cells
        return table
    r95rows = rows(FIX95 / "claim-excerpt-map.md")
    r96rows = rows(FIX96 / "claim-excerpt-map.md")

    def norm(cells):
        return [c.replace("r95-crossing-aftermath:", "CLUSTER:")
                 .replace("r96-crossing-response:", "CLUSTER:") for c in cells]
    common = sorted(set(r95rows) & set(r96rows))
    field_diffs = [k for k in common if norm(r95rows[k]) != norm(r96rows[k])]
    new_rows = sorted(set(r96rows) - set(r95rows))
    missing_rows = sorted(set(r95rows) - set(r96rows))
    results["c2_row_fields"] = {"common": len(common), "field_diffs": field_diffs}
    results["c2_rows"] = {"r95_rows": len(r95rows), "r96_rows": len(r96rows),
                          "new_rows": new_rows, "missing_rows": missing_rows}
    check("C2 inherited rows preserved (path-normalized)", not missing_rows, f"missing={len(missing_rows)}")
    check("C2 exactly one new map row", len(new_rows) == 1, f"new={len(new_rows)}")
    for r in new_rows:
        note("    new row: " + r.strip())

    # census
    dirs = sorted(d for d in (ROOT / "corpus/fixtures").iterdir()
                  if d.is_dir() and (d / "entities.json").exists())
    clean = neg = other = 0
    for d in dirs:
        rc, _, _ = run(["python3", "corpus/fixtures/check_bible.py", f"corpus/fixtures/{d.name}"])
        if rc == 0:
            clean += 1
        elif rc == 1:
            neg += 1
        else:
            other += 1
    results["c2_census"] = {"total": len(dirs), "clean": clean, "negative": neg, "other": other}
    check("C2 census 170 dirs / 36 clean / 134 negative / 0 other",
          (len(dirs), clean, neg, other) == (170, 36, 134, 0),
          f"total={len(dirs)} clean={clean} neg={neg} other={other}")

    # ---------------- C3 ----------------
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", "--self-test"])
    results["c3_selftest"] = {"exit": rc, "stdout": out}
    check("C3 --self-test exit 0", rc == 0, f"exit={rc}")
    note("    " + " | ".join(out.strip().splitlines()[:3]))

    chain = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response"]
    chain_results = {}
    for d in chain:
        rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", f"corpus/fixtures/{d}"])
        chain_results[d] = {"exit": rc, "stdout": out.strip()}
    results["c3_chain"] = chain_results
    clean4 = sum(1 for v in chain_results.values() if v["exit"] == 0)
    check("C3 chain 4/4 clean", clean4 == 4, f"clean={clean4}/4")
    for d, v in chain_results.items():
        note(f"    chain {d}: exit={v['exit']} :: {v['stdout'].splitlines()[-1] if v['stdout'] else ''}")

    # BR-01 mutation: drop evin-ninth-bell edge from r94 tick-10
    # NOTE: pins are basename-keyed, so the scratch copy must keep the fixture's name
    mutroot = SCRATCH / "mutroot"
    if mutroot.exists():
        shutil.rmtree(mutroot)
    mut = mutroot / "br01" / "r94-paired-crossing"
    mut.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mut)
    t = json.load(open(mut / "timeline.json"))
    for e in t:
        if e["id"] == "paired-crossing-decision":
            e["depends_on"] = [x for x in e["depends_on"] if x != "evin-ninth-bell"]
    json.dump(t, open(mut / "timeline.json", "w"), indent=2, ensure_ascii=False)
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(mut)])
    results["c3_br01"] = {"exit": rc, "stdout": out}
    check("C3 BR-01 mutation exit 1", rc == 1, f"exit={rc}")
    check("C3 BR-01 REDUCTION-DETECTED", "REDUCTION-DETECTED" in out)
    note("    " + " | ".join(out.strip().splitlines()))

    # added edge mutation
    mut2 = mutroot / "addition" / "r94-paired-crossing"
    mut2.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mut2)
    t = json.load(open(mut2 / "timeline.json"))
    for e in t:
        if e["id"] == "paired-crossing-decision":
            e["depends_on"].append("aftermath-missing-evin")
    json.dump(t, open(mut2 / "timeline.json", "w"), indent=2, ensure_ascii=False)
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(mut2)])
    results["c3_addition"] = {"exit": rc, "stdout": out}
    check("C3 addition mutation exit 1", rc == 1, f"exit={rc}")
    note("    " + " | ".join(out.strip().splitlines()))

    # endpoint change mutation (relation endpoint flip)
    mut3 = mutroot / "endpoint" / "r94-paired-crossing"
    mut3.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mut3)
    rel = json.load(open(mut3 / "relations.json"))
    for r in rel:
        r["from"], r["to"] = r["to"], r["from"]
    json.dump(rel, open(mut3 / "relations.json", "w"), indent=2, ensure_ascii=False)
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(mut3)])
    results["c3_endpoint"] = {"exit": rc, "stdout": out}
    check("C3 endpoint mutation exit 1", rc == 1, f"exit={rc}")
    note("    " + " | ".join(out.strip().splitlines()))

    # event endpoint change (tick) mutation
    mut4 = mutroot / "evtendpoint" / "r94-paired-crossing"
    mut4.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mut4)
    t = json.load(open(mut4 / "timeline.json"))
    for e in t:
        if e["id"] == "paired-crossing-decision":
            e["tick"] = 11
    json.dump(t, open(mut4 / "timeline.json", "w"), indent=2, ensure_ascii=False)
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(mut4)])
    results["c3_evt_endpoint"] = {"exit": rc, "stdout": out}
    check("C3 event endpoint change exit 1 ENDPOINT-CHANGE",
          rc == 1 and "ENDPOINT-CHANGE" in out, f"exit={rc}")
    note("    " + " | ".join(out.strip().splitlines()))

    # cosmetic digest tamper -> could-not-evaluate exit 2
    mut5 = mutroot / "digest" / "r94-paired-crossing"
    mut5.parent.mkdir(parents=True)
    shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mut5)
    raw = (mut5 / "sources.json").read_text()
    (mut5 / "sources.json").write_text(raw.replace('"id"', '"id" ', 1))
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(mut5)])
    results["c3_digest"] = {"exit": rc, "stdout": out}
    check("C3 digest-only tamper exit 2", rc == 2 and "DIGEST-MISMATCH" in out, f"exit={rc}")

    # could-not-evaluate
    rc, out, _ = run(["python3", "corpus/tools/dependency_freeze.py", str(SCRATCH / "does-not-exist")])
    results["c3_error"] = {"exit": rc, "stdout": out}
    check("C3 missing fixture exit 2", rc == 2, f"exit={rc}")

    # zero corpus modifications beyond the two tool files
    rc, out, _ = run(["git", "status", "--porcelain"])
    results["git_status"] = out
    note("--- git status --porcelain ---")
    note(out.strip())

    # ---------------- C4 integration: corpus README/tools README claims ----------------
    for f in ["corpus/tools/README.md", "corpus/knowledge/r96-response-scope-note.md",
              "corpus/fixtures/r96-crossing-response/README.md",
              "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"]:
        p = ROOT / f
        results[f] = p.exists()

    (SCRATCH / "harness-results.json").write_text(json.dumps(results, indent=1))
    note("=== harness complete ===")


if __name__ == "__main__":
    main()
