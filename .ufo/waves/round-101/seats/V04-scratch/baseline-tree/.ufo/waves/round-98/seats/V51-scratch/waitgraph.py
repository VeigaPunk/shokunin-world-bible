#!/usr/bin/env python3
"""V51 wait-graph static analyzer — classify every poll script in round-98.

For each poll script: which seats/artifacts it waits on; whether it has an
all-reports condition; whether it subtracts SELF; whether it has a bounded escape.
Writes TSV to V51-scratch/waitgraph.tsv (overwritten each run).
"""
import os, re, glob, datetime

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
W = os.path.join(R, ".ufo/waves/round-98")
OUT = os.path.join(W, "seats/V51-scratch/waitgraph.tsv")

def seat_of(path):
    # .../seats/V07-scratch/poll.sh -> V07 ; .../scratch/V31/poll.sh -> V31
    parts = path.replace(W, "").split(os.sep)
    for p in parts:
        m = re.match(r"^(V\d{2}|S\d|R\d)", p)
        if m:
            return m.group(1)
    return "?"

def analyze(path):
    try:
        txt = open(path, errors="replace").read()
    except OSError:
        return None
    seat = seat_of(path)
    waits_reports = re.search(r"ls[^\n]*seats[^\n]*\*\.md|seats/\*\.md|\.md.*wc -l", txt) is not None
    allre = None
    m = re.search(r"grep -v[^\n]*", txt)
    selfsub = None
    if m:
        g = m.group(0)
        selfsub = ("YES" if re.search(rf"(V{seat[1:]}|\^{seat}|{seat})", g) else "?") if seat != "?" else "?"
    # more precise: look for grep -v '<seat>' patterns
    if seat != "?":
        pats = [rf"grep -v ['\"]?/?{seat}", rf"grep -v ['\"]?\.\*{seat}", rf"grep -v ['\"]?{seat}-",
                rf"grep -v \"\^{seat}\"", rf"grep -v '/{seat}"]
        selfsub = "YES" if any(re.search(p, txt) for p in pats) else "NO"
    # thresholds like -ge 63 / -ge 5 on report counts
    thr = re.findall(r"(?:n|reports|nrep|REP|tot)[^=\n]*?(?:-ge|-eq)\s*(\d+)", txt)
    tries = re.findall(r"seq 1 (\d+)|-lt (\d+)|\"(\d+)\"", txt)
    ntry = None
    mt = re.search(r"seq 1 (\d+)", txt) or re.search(r"-lt (\d+)", txt)
    if mt:
        ntry = mt.group(1) or mt.group(2)
    esc = "NO"
    if re.search(r"TIMEOUT|DEADLINE|EXHAUST|POLL_TERMINAL|CAP|HARD-CAP|STALL", txt, re.I):
        esc = "YES"
    # wait target class
    prods = "S1" in txt or "S[1-5]" in txt or re.search(r"^\s*for s in S", txt, re.M)
    vers = re.search(r"V\d{2}", txt)
    kind = []
    if waits_reports:
        kind.append("reports")
    if re.search(r"corpus/", txt):
        kind.append("artifacts")
    return (seat, os.path.relpath(path, R), "YES" if waits_reports else "no", selfsub,
            str(ntry), esc, "|".join(kind) or "-")

rows = []
for pat in ["seats/*scratch*/poll*.sh", "seats/scratch/*.sh", "scratch/*/poll*.sh", "*.sh"]:
    for p in sorted(glob.glob(os.path.join(W, pat))):
        a = analyze(p)
        if a:
            rows.append(a)
with open(OUT, "w") as f:
    f.write(f"# waitgraph {datetime.datetime.now().isoformat(timespec='seconds')} rows={len(rows)}\n")
    f.write("seat\tscript\twaits_reports\tsubtract_self\ttries\tbounded_escape\tkind\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
print(f"rows={len(rows)}")
for r in rows:
    print("\t".join(r))
