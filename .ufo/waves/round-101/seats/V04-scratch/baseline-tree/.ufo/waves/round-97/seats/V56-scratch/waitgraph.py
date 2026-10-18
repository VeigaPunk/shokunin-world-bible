#!/usr/bin/env python3
"""V56 wait-graph analyzer: parse round-97 poll scripts, map each seat's wait
condition to the seat(s) that own the awaited artifacts/reports, and detect
cycles (A waits on B AND B waits on A) and all-reports mutual waits.

Usage: python3 waitgraph.py
Prints edges and cycles; exits 0 always (analysis tool).
"""
import re
from pathlib import Path

SEATS = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats")

# artifact path fragment -> owning seat
ARTIFACT_OWNER = [
    ("map_obligations.py", "R1"),
    ("map-obligations-contract.json", "R2"),
    ("tools/README.md", "R2"),
    ("dependency_freeze.py", "R3"),
    ("dependency-freeze-contract.json", "R3"),
    ("r96-crossing-response/claim-excerpt-map.md", "R4"),
    ("r97-crossing-acknowledgment/README.md", "R5"),
    ("r97-crossing-acknowledgment/claim-excerpt-map.md", "R5"),
    ("r97-acknowledgment-scope-note.md", "R6"),
]

ALL_REPORTS_PAT = re.compile(
    r"(lane\s*[->=]+\s*64|N\s*[->=]+\s*63|\$N.*-ge *63|\"\$N\" -ge 63|ALL.*-ge *64|>= *63|>= *64|others *>= *63|reps *-ge *6|allr *-ge *6|n *-ge *20|-ge *6[0-9]|>= *6[0-9])"
)
R_REPORT_PAT = re.compile(r"R([1-6])(?:-\*|\*|-\w+|\.md|[\s\"'$]|$)")
V_REPORT_PAT = re.compile(r"V(\d{2})")


def parse_script(path: Path):
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None
    edges = set()
    all_reports = bool(ALL_REPORTS_PAT.search(text))
    for frag, owner in ARTIFACT_OWNER:
        if frag in text:
            edges.add(owner)
    # explicit R report references like R3-*.md, $S/R3, R4-fixture-json.md
    for m in re.finditer(r"R([1-6])", text):
        edges.add(f"R{m.group(1)}")
    # explicit V report references (e.g., crosscheck waiting on another verifier)
    for m in re.finditer(r"V(\d{2})", text):
        edges.add(f"V{m.group(1)}")
    return {"edges": sorted(edges), "all_reports": all_reports, "text": text}


def main():
    scripts = {}
    for d in sorted(SEATS.glob("*scratch*")):
        if not d.is_dir() or d.name == "V56-scratch":
            continue
        name = d.name
        m = re.match(r"scratch-([RV]\d{1,2})", name) or re.match(r"([RV]\d{1,2})[-.]", name)
        seat = m.group(1) if m else name.split("-")[0].split(".")[0]
        for f in sorted(d.glob("*.sh")):
            if "poll" not in f.name and "wait" not in f.name:
                continue
            r = parse_script(f)
            if r is None:
                continue
            r["file"] = str(f)
            r["seat"] = seat
            scripts.setdefault(seat, []).append(r)

    print("=== poll scripts per seat ===")
    for seat in sorted(scripts):
        for r in scripts[seat]:
            print(f"{seat}: {r['file'].split('/')[-1]} all_reports={r['all_reports']} edges={r['edges']}")

    # wait edges seat -> owner (drop self)
    wait = {}
    for seat, rs in scripts.items():
        tgt = set()
        for r in rs:
            for e in r["edges"]:
                if e != seat:
                    tgt.add(e)
        wait[seat] = tgt

    print("\n=== wait edges (seat -> owners) ===")
    for s in sorted(wait):
        print(f"{s} -> {sorted(wait[s])}")

    print("\n=== direct mutual pairs (A->B and B->A) ===")
    found = False
    for a in sorted(wait):
        for b in sorted(wait[a]):
            if b in wait and a in wait.get(b, set()):
                if a < b:
                    print(f"MUTUAL: {a} <-> {b}")
                    found = True
    if not found:
        print("(none)")

    # all-reports condition + absent reports -> r96-style deadlock detector
    md = sorted(p.name for p in SEATS.glob("*.md"))
    present = set()
    for m in md:
        mm = re.match(r"([RV]\d{1,2})", m)
        if mm:
            present.add(mm.group(1))
    all_seats = {f"V{i:02d}" for i in range(1, 59)} | {f"R{i}" for i in range(1, 7)}
    absent = sorted(all_seats - present)
    allr_seats = sorted(s for s, rs in scripts.items() if any(r["all_reports"] for r in rs))
    print(f"\n=== all-reports pollers ===\n{allr_seats}")
    print(f"=== absent reports ({len(absent)}) ===\n{absent}")
    if allr_seats and absent:
        potential = [s for s in allr_seats if s in absent]
        if potential and set(absent) <= set(allr_seats):
            print("POTENTIAL ALL-REPORTS DEADLOCK: absent seats are all themselves pollers ->")
            print(f"  pollers {allr_seats} each require all reports; only {absent} missing -> mutual wait")
        elif potential:
            print(f"NOTE: all-reports pollers that are themselves absent: {potential}; other absent: {sorted(set(absent)-set(allr_seats))}")


def scan_terminals():
    import glob
    import pathlib
    print("\n=== poll terminal markers in logs ===")
    found = False
    for f in sorted(glob.glob(str(SEATS / "*scratch*/poll*.log")) + glob.glob(str(SEATS / "*scratch*/*poll*.log")) + glob.glob(str(SEATS / "*scratch*/*poll*.out"))):
        try:
            text = pathlib.Path(f).read_text(errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            if any(k in line for k in ("TIMEOUT", "ABSENT", "DEADLINE", "STALL", "POLL_HIT", "POLL_READY", "READY", "DONE", "POLL_STABLE", "CAP ")):
                print(f"  [{f.split('/')[-2]}/{f.split('/')[-1]}] {line.strip()}")
                found = True
    if not found:
        print("  (none yet)")


if __name__ == "__main__":
    main()
    scan_terminals()
