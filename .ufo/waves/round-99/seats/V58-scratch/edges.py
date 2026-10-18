#!/usr/bin/env python3
"""Build a wait-edge list from dumped proc cmdlines + top-level poll scripts.

A seat waits on another seat only when its poll *exit condition* names that
seat's report (or an all-reports threshold that includes it). Logging a count
is not a wait.

Outputs V58-scratch/edges.txt
"""
import glob
import os
import re

SCR = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V58-scratch"
SEATS = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats"
PROC = os.path.join(SCR, "procs")
OUT = os.path.join(SCR, "edges.txt")

SEAT = re.compile(r"\b(S[1-5]|V\d{2,3})\b")


def own_seat(name, text):
    m = re.match(r"(S[1-5]|V\d{2,3})__", os.path.basename(name))
    if m:
        return m.group(1)
    m = re.search(r"round-99/seats/(S[1-5]|V\d{2,3})-scratch", text)
    return m.group(1) if m else "?"


def is_poll(text):
    return any(k in text for k in ("sleep(20)", "sleep 20", "time.sleep(20)", "seq 1"))


def classify_text(seat, text, src):
    """Return a dict of wait facts."""
    # strip comments-ish for condition detection: keep full text but also a
    # "condition window": lines that contain if / while / exit / break near a compare.
    facts = {
        "seat": seat,
        "src": src,
        "poll": is_poll(text),
        "all_reports": False,
        "threshold": None,
        "self_sub": False,
        "self_inclusive": False,
        "bounded": False,
        "tries": None,
        "targets": set(),  # seats whose reports gate exit
        "notes": [],
    }
    # tries
    for pat in (
        r"seq 1 (\d+)",
        r"range\(1,\s*(\d+)\)",
        r"range\(\s*(\d+)\s*\)",
        r"MAX\s*=\s*(\d+)",
        r"max_tries\s*=\s*(\d+)",
        r"for \w+ in range\(1,\s*(\d+)\)",
    ):
        m = re.search(pat, text)
        if m:
            facts["tries"] = int(m.group(1))
            break
    if re.search(r"DEADLINE|TIMEOUT|STALL_ESCAPE|POLL-TIMEOUT|ABSENT after|SAMPLER_CAP|cap=\d+", text):
        facts["bounded"] = True
    if facts["tries"]:
        facts["bounded"] = True

    # all-reports thresholds on a report count
    # V123: reports -ge 128
    m = re.search(r"reports.{0,40}-ge\s*(12[0-8])", text)
    if m:
        facts["all_reports"] = True
        facts["threshold"] = int(m.group(1))
    m = re.search(r"len\(files\)\s*>=\s*(12[0-8])", text)
    if m:
        facts["all_reports"] = True
        facts["threshold"] = int(m.group(1))
    m = re.search(r"len\(missing\)\s*==\s*0", text)
    if m and re.search(r"roster", text) and re.search(r"127", text):
        facts["all_reports"] = True
        facts["threshold"] = 127
    m = re.search(r"others\s*>=\s*(12[0-8])|nonself\s*>=\s*(12[0-8])", text)
    if m:
        facts["all_reports"] = True
        facts["threshold"] = int(next(g for g in m.groups() if g))

    # self subtraction evidence
    if seat != "?":
        if re.search(rf"!=\s*[\"']?{seat}|startswith\(\"{seat}-\"|not p\.name\.startswith\(\"{seat}", text):
            facts["self_sub"] = True
        if re.search(rf"if s != \"{seat}\"|if s != '{seat}'|roster = \[s for s in roster if s != \"{seat}\"\]", text):
            facts["self_sub"] = True
        if re.search(rf"grep -v[^\n]*{seat}", text):
            facts["self_sub"] = True
        if re.search(rf"! -name '{seat}-|! -name \"{seat}-", text):
            facts["self_sub"] = True
        if re.search(r"subtract SELF|SELF excluded|excluding SELF|nonself", text, re.I):
            facts["self_sub"] = True
    if facts["all_reports"] and facts["threshold"] == 128:
        facts["self_inclusive"] = not facts["self_sub"]
    if facts["all_reports"] and facts["threshold"] == 127:
        facts["self_sub"] = True  # 127 of 128 is self-subtraction by construction
        facts["self_inclusive"] = False

    # named report gates: a seat id that appears in an exit condition.
    # Heuristic: seat token within 200 chars before an exit 0 / break / READY / ALL-PRESENT
    # AND the token is in a test (-f, -s, compgen, glob, startswith).
    # Simpler robust heuristic used by prior seats: if the script's success
    # condition mentions Seat-*.md or REPORT:Seat, it waits on that seat.
    # Exclude the seat itself and exclude pure log labels.
    waited = set()
    # explicit report file tests
    for m in re.finditer(r"(S[1-5]|V\d{2,3})-\*\.md|(S[1-5]|V\d{2,3})-\{\*\.md\}|(S[1-5]|V\d{2,3})\*\.md", text):
        waited.add(m.group(1) or m.group(2) or m.group(3))
    for m in re.finditer(r"REPORT:(S[1-5]|V\d{2,3})", text):
        waited.add(m.group(1))
    for m in re.finditer(r"name=['\"](S[1-5]|V\d{2,3})-\*\.md", text):
        waited.add(m.group(1))
    for m in re.finditer(r"startswith\(\"(S[1-5]|V\d{2,3})-\"\)", text):
        # this is usually self-exclusion, not a wait
        pass
    # Vnn report variable gates: if v39 / "V39" in an if that exits
    # Look for lines assigning a hit from a specific report name used later in exit.
    for m in re.finditer(r"(S[1-5]|V\d{2,3})-[A-Za-z0-9_-]+\.md", text):
        token_seat = m.group(1)
        # only count if the filename literal is inside a test (-f/-s/exists/compgen)
        span_start = max(0, m.start() - 80)
        window = text[span_start:m.end() + 40]
        if re.search(r"-f |-s |exists\(|compgen|is_file|Path\(", window):
            waited.add(token_seat)
    waited.discard(seat)
    # producers list that gates: `for s in S1 S2 S3 S4 S5` combined with missing→continue
    if re.search(r"for s in S1 S2 S3 S4 S5|for seat in S1 S2 S3 S4 S5|producers = \[.S1", text):
        if re.search(r"missing|MISS|ALL-PRESENT|exit 0", text):
            waited.update(["S1", "S2", "S3", "S4", "S5"])
    facts["targets"] = waited

    # all-reports implies waiting on every other seat — mark specially, don't expand
    return facts


def main():
    facts = []
    # proc dumps
    for p in sorted(glob.glob(os.path.join(PROC, "*.txt"))):
        text = open(p, errors="replace").read()
        seat = own_seat(p, text)
        if not is_poll(text):
            continue
        # skip our own tools
        if "V58-scratch" in text and ("sampler.py" in text or "dump_procs" in text or "edges.py" in text or "scan_inline" in text or "waitgraph.py" in text):
            continue
        facts.append(classify_text(seat, text, os.path.basename(p)))
    # top-level poll scripts (may duplicate procs; keep both, dedupe later)
    for p in sorted(glob.glob(os.path.join(SEATS, "*-scratch/poll.sh"))):
        if "/archive/" in p:
            continue
        text = open(p, errors="replace").read()
        seat = re.match(r"(S[1-5]|V\d{2,3})", os.path.basename(os.path.dirname(p))).group(1)
        facts.append(classify_text(seat, text, "script:" + os.path.basename(os.path.dirname(p)) + "/poll.sh"))

    # dedupe by seat keeping the richest (all_reports preferred, else more targets)
    by = {}
    for f in facts:
        cur = by.get(f["seat"])
        if cur is None:
            by[f["seat"]] = f
            continue
        # merge targets, prefer all_reports True
        cur["targets"] |= f["targets"]
        if f["all_reports"] and not cur["all_reports"]:
            cur["all_reports"] = True
            cur["threshold"] = f["threshold"]
            cur["self_sub"] = f["self_sub"] or cur["self_sub"]
            cur["self_inclusive"] = f["self_inclusive"]
            cur["src"] = cur["src"] + "+" + f["src"]
        cur["bounded"] = cur["bounded"] or f["bounded"]
        if cur["tries"] is None:
            cur["tries"] = f["tries"]
        cur["self_sub"] = cur["self_sub"] or f["self_sub"]

    lines = []
    lines.append(f"seats_with_polls={len(by)}")
    allrep = [s for s, f in sorted(by.items()) if f["all_reports"]]
    lines.append("ALL_REPORTS:")
    if not allrep:
        lines.append("  none")
    for s in allrep:
        f = by[s]
        lines.append(
            f"  {s} thr={f['threshold']} self_sub={f['self_sub']} "
            f"self_inclusive={f['self_inclusive']} tries={f['tries']} "
            f"bounded={f['bounded']} src={f['src']}"
        )
    # mutual named pairs
    lines.append("NAMED_EDGES (exit-gated, not all-reports expansion):")
    edges = []
    for s, f in sorted(by.items()):
        for t in sorted(f["targets"]):
            if t == s:
                continue
            edges.append((s, t))
            lines.append(f"  {s} -> {t}  (tries={f['tries']} bounded={f['bounded']})")
    lines.append("MUTUAL_NAMED_PAIRS:")
    mutual = []
    eset = set(edges)
    for a, b in edges:
        if a < b and (b, a) in eset:
            mutual.append((a, b))
    if not mutual:
        lines.append("  none")
    for a, b in mutual:
        lines.append(f"  {a} <-> {b}")
    # all-reports clique analysis
    lines.append("ALL_REPORTS_CLIQUE:")
    if len(allrep) < 2:
        lines.append("  fewer than 2 all-reports waiters; no all-reports cycle possible yet")
    else:
        # a cycle exists among all-reports waiters iff each one's threshold
        # cannot be met until another all-reports waiter writes.
        # Self-inclusive (thr=128) can NEVER be met by its own poll (it waits
        # for its own report). Self-subtracted (thr=127) CAN be met once every
        # other seat including the self-inclusive one has written — so the
        # self-subtracted waiter is blocked on the self-inclusive waiter, but
        # not vice versa unless the self-inclusive one is also blocked.
        # Deadlock requires every member to be unable to exit without another member.
        si = [s for s in allrep if by[s]["self_inclusive"]]
        ss = [s for s in allrep if by[s]["self_sub"] and not by[s]["self_inclusive"]]
        lines.append(f"  self_inclusive={si or 'none'}")
        lines.append(f"  self_subtracted={ss or 'none'}")
        if si and not ss:
            lines.append("  DEFECT: self-inclusive all-reports with no peer to release it; bounded escape is the only release")
        elif si and ss:
            lines.append("  NOT a deadlock: self-subtracted waiters can complete once non-all-reports seats land;")
            lines.append("  self-inclusive waiter cannot hit 128 from inside its own poll (counts own unwritten report).")
            lines.append("  Release path: self-inclusive escape fires OR seat writes without the condition; then self-subtracted conditions can hit.")
            lines.append("  This is the r96 self-inclusive class, one-sided, not an n-cycle, IF no self-subtracted waiter is the only missing report for another self-subtracted waiter.")
            if len(ss) >= 2:
                lines.append(f"  WARNING: {len(ss)} self-subtracted all-reports waiters. Each needs the others' reports (127 includes peers).")
                lines.append("  That IS an n-cycle among the self-subtracted set PLUS the self-inclusive seat, unless one of them writes without waiting.")
                lines.append("  Bounded escapes are the designed release. Record whether any escape has fired.")
        else:
            lines.append("  all self-subtracted. n-cycle among them if each requires the others (thr=127 includes peers).")
            lines.append("  Release requires one seat to write without the condition, or an escape to fire.")
    # unbounded
    lines.append("UNBOUNDED_POLLS:")
    ub = [s for s, f in sorted(by.items()) if f["poll"] and not f["bounded"]]
    if not ub:
        lines.append("  none")
    for s in ub:
        f = by[s]
        lines.append(f"  {s} all={f['all_reports']} targets={sorted(f['targets'])} src={f['src']}")
    text = "\n".join(lines) + "\n"
    open(OUT, "w").write(text)
    print(text)


if __name__ == "__main__":
    main()
