#!/usr/bin/env python3
"""V57 round-98 wait-graph + liveness analyzer. One-shot; prints findings.

Combines: report presence, live poll/wait processes (with ages), static wait
edges parsed from every seat poll/wait script, mutual-pair detection, and the
all-reports n-cycle detector (the r96/r97 mutual-wait class).
"""
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
WAVE = ROOT / ".ufo/waves/round-98"
SEATS = WAVE / "seats"
T0 = datetime(2026, 10, 17, 23, 27, 36, tzinfo=timezone.utc)

OWNER = [
    (r"dependency_freeze|dependency-freeze-contract", "S1"),
    (r"tools/README", "S2"),
    (r"r98-clerk-filing/(entities|sources|timeline|fictional-excerpts)", "S3"),
    (r"r98-clerk-filing/(README|claim-excerpt-map)", "S4"),
    (r"r98-clerk-scope-note|r95-aftermath-scope-note|r96-response-scope-note", "S5"),
    (r"r95-crossing-aftermath/claim-excerpt-map", "S3"),
]


def main():
    now = datetime.now(timezone.utc)
    el = (now - T0).total_seconds()
    print(f"NOW {now:%H:%M:%SZ} round_elapsed={el / 60:.1f}min (t0=23:27:36Z)")

    md = sorted(p.name for p in SEATS.glob("*.md"))
    present = set()
    for m in md:
        mm = re.match(r"([SV]\d+)", m)
        if mm:
            present.add(mm.group(1))
    absent_s = [f"S{k}" for k in range(1, 6) if f"S{k}" not in present]
    absent_v = [f"V{k:02d}" for k in range(1, 60) if f"V{k:02d}" not in present]
    print(f"reports_total={len(md)} present_n={len(present)}")
    print(f"absent_S={absent_s}")
    print(f"absent_V={absent_v}")

    try:
        ps = subprocess.run(
            ["ps", "-eo", "pid,etimes,stat,cmd"],
            capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception as e:
        ps = ""
        print(f"PS-ERROR {e!r}")
    procs = []
    for ln in ps.splitlines():
        if ("lore-shokunin" in ln or "round-98" in ln) and (
            "poll" in ln or "watch" in ln or "for i in" in ln or "while" in ln or "seq 1" in ln
        ):
            if "V57-scratch" in ln:
                continue
            procs.append(" ".join(ln.split()))
    print(f"\n=== live poll/wait processes ({len(procs)}) ===")
    for p in procs:
        print(f"  {p[:260]}")

    scripts = []
    dirs = list(SEATS.glob("*scratch*")) + list((WAVE / "scratch").glob("*"))
    dirs += [d for d in ROOT.glob("*scratch*") if d.is_dir()]
    for d in dirs:
        if not d.is_dir() or d.name == "V57-scratch":
            continue
        for f in sorted(set(d.glob("*.sh")) | set(d.glob("*.py"))):
            try:
                t = f.read_text(errors="replace")
            except OSError:
                continue
            if not re.search(r"poll|wait|seq 1|while|sleep 20", t):
                continue
            seat = None
            mm = re.search(r"([SV]\d+)", d.name)
            if mm:
                seat = mm.group(1)
            edges = set()
            for pat, o in OWNER:
                if re.search(pat, t):
                    edges.add(o)
            for m in re.finditer(r"\b(S\d)[-_]", t):
                edges.add(m.group(1))
            for m in re.finditer(r"\b(V\d{2})[-_]", t):
                edges.add(m.group(1))
            allr = bool(re.search(r"(-ge|>=|==)\s*(6[0-4])\b", t)) or bool(
                re.search(r"(ALL|lane|others)\s*[><=]", t, re.I)
            )
            selfsub = bool(re.search(r"grep -v[^\n]*(V\d{2}|S\d)", t)) or bool(re.search(r"-\s*1\b", t))
            scripts.append((seat, str(f.relative_to(ROOT)), sorted(edges), allr, selfsub))
    print("\n=== scripts (seat, path, edges, all_reports, self_subtract) ===")
    for s in scripts:
        print(f"  {s}")

    wait = {}
    for seat, path, edges, allr, selfsub in scripts:
        if seat:
            wait.setdefault(seat, set()).update(e for e in edges if e != seat)
    print("\n=== edges seat->seats ===")
    for k in sorted(wait):
        print(f"  {k} -> {sorted(wait[k])}")
    mutual = []
    for a in sorted(wait):
        for b in wait[a]:
            if b in wait and a in wait.get(b, set()):
                if a < b:
                    mutual.append((a, b))
    print(f"\nMUTUAL PAIRS (static, direct): {mutual if mutual else '(none)'}")

    allr_seats = sorted({s[0] for s in scripts if s[3] and s[0]})
    print(f"ALL-REPORTS waiters: {allr_seats}")
    live_seats = set()
    for p in procs:
        for m in re.finditer(r"(V\d{2}|S\d)[-_]scratch", p):
            live_seats.add(m.group(1))
        for m in re.finditer(r"scratch/(V\d{2}|S\d)\b", p):
            live_seats.add(m.group(1))
    print(f"live_poll_seats(guess)={sorted(live_seats)}")
    absent_all = absent_s + absent_v
    pot = [s for s in absent_all if s in set(allr_seats)]
    if pot and set(absent_all) <= set(allr_seats):
        print(f"POTENTIAL ALL-REPORTS N-CYCLE: absent={absent_all} are all all-reports waiters")
    elif pot:
        print(f"NOTE: absent all-reports waiters: {pot}; absent others: {sorted(set(absent_all) - set(allr_seats))}")


if __name__ == "__main__":
    main()
