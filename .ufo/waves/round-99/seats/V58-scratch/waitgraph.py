#!/usr/bin/env python3
"""V58 mutual-wait-guard static wait-graph (round 99).

Read-only. Classifies every poll/watch script under the wave tree:
  - report-count conditions (all-reports vs targeted)
  - SELF subtraction
  - bounded escape (tries / deadline / stall / cap)
  - named seat targets and whether the reverse edge exists
Writes TSV + a mutual-pair summary under V58-scratch only.
"""
import datetime
import glob
import os
import re
import sys

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
W = os.path.join(R, ".ufo/waves/round-99")
OUT = os.path.join(W, "seats/V58-scratch/waitgraph.tsv")
SUM = os.path.join(W, "seats/V58-scratch/waitgraph-summary.txt")

SEAT_RE = re.compile(r"^(S[1-5]|V\d{2,3})$")


def seat_of(path):
    rel = path.replace(W, "")
    parts = rel.split(os.sep)
    for p in parts:
        m = re.match(r"^(S[1-5]|V\d{2,3})", p)
        if m:
            return m.group(1)
    base = os.path.basename(path)
    m = re.match(r"^(S[1-5]|V\d{2,3})", base)
    if m:
        return m.group(1)
    return "?"


def named_targets(txt, self_seat):
    found = set(re.findall(r"\b(S[1-5]|V\d{2,3})\b", txt))
    found.discard(self_seat)
    # drop incidental mentions of the protocol numbers that look like seats? none.
    return found


def classify(path):
    try:
        txt = open(path, errors="replace").read()
    except OSError as e:
        return None
    seat = seat_of(path)
    # report-counting: ls of seats/*.md or wc of report globs
    waits_reports = bool(re.search(
        r"seats/?\*\.md|seats\"?\s*/\s*\*\.md|\*\.md[^\n]{0,40}wc\s+-l|reports?\s*=.*wc",
        txt,
    ))
    # all-reports threshold: a numeric compare against a large count
    thr = []
    for m in re.finditer(
        r"(?:-ge|-gt|-eq|>=|>|==)\s*(\d{2,3})", txt
    ):
        thr.append(int(m.group(1)))
    high = [t for t in thr if t >= 50]
    all_reports = waits_reports and bool(high)
    # self subtraction
    selfsub = "n/a"
    if seat != "?":
        pats = [
            rf"grep\s+-v[^\n]*{seat}",
            rf"grep\s+-vE[^\n]*{seat}",
            rf"nonself",
            rf"!=\s*['\"]?{seat}",
            rf"not\s+{seat}",
            rf"exclude[^\n]*{seat}",
            rf"SELF",
            rf"subtract",
        ]
        hits = [p for p in pats if re.search(p, txt)]
        # stricter: does the exclusion actually name this seat, or a generic SELF token?
        names_self = bool(re.search(rf"grep\s+-v[^\n]*{re.escape(seat)}", txt)) or bool(
            re.search(rf"{re.escape(seat)}-(?:mutual|presence|adjudicator|receipt|endgame|scope)", txt)
            and re.search(r"grep\s+-v", txt)
        )
        generic = bool(re.search(r"\bSELF\b|nonself|subtract.self|exclude.self", txt, re.I))
        if names_self:
            selfsub = "YES-named"
        elif generic:
            selfsub = "YES-generic"
        elif waits_reports:
            selfsub = "NO"
        else:
            selfsub = "n/a"
    # bounded escape
    tries = None
    mt = re.search(r"seq\s+1\s+(\d+)", txt)
    if mt:
        tries = int(mt.group(1))
    else:
        mt = re.search(r"range\(\s*1?\s*,?\s*(\d+)\s*\)", txt)
        if mt:
            tries = int(mt.group(1))
        else:
            mt = re.search(r"for\s+\w+\s+in\s+\$\(\s*seq\s+1\s+(\d+)", txt)
            if mt:
                tries = int(mt.group(1))
    # python while i < N
    mt2 = re.search(r"while\s+\w+\s*<\s*(\d+)", txt)
    if tries is None and mt2:
        tries = int(mt2.group(1))
    esc_tokens = []
    for tok in ("TIMEOUT", "DEADLINE", "EXHAUST", "POLL_TERMINAL", "POLL-TIMEOUT",
                "CAP", "HARD-CAP", "HARD_CAP", "STALL", "ABSENT", "break", "exit 2",
                "exit 1", "sys.exit"):
        if re.search(re.escape(tok) if tok not in ("break",) else tok, txt):
            if tok == "break" or re.search(tok, txt):
                esc_tokens.append(tok)
    # dedupe preserving order
    seen = []
    for t in esc_tokens:
        if t not in seen:
            seen.append(t)
    bounded = "YES" if (tries is not None or any(
        t in seen for t in ("TIMEOUT", "DEADLINE", "EXHAUST", "POLL_TERMINAL",
                            "POLL-TIMEOUT", "CAP", "HARD-CAP", "HARD_CAP", "STALL")
    )) else "NO"
    targets = named_targets(txt, seat)
    # producer reports specifically
    prod_wait = bool(re.search(r"\bS[1-5]\b", txt)) and (
        "report" in txt.lower() or "*.md" in txt or "S1" in txt
    )
    kind = []
    if all_reports:
        kind.append("all-reports")
    elif waits_reports:
        kind.append("reports")
    if re.search(r"corpus/", txt):
        kind.append("artifacts")
    if prod_wait and "all-reports" not in kind:
        kind.append("producers")
    rel = os.path.relpath(path, R)
    return {
        "seat": seat,
        "script": rel,
        "bytes": os.path.getsize(path),
        "waits_reports": "YES" if waits_reports else "no",
        "all_reports": "YES" if all_reports else "no",
        "threshold": ",".join(str(t) for t in sorted(set(high))) if high else "-",
        "subtract_self": selfsub,
        "tries": str(tries) if tries is not None else "-",
        "bounded": bounded,
        "escape_tokens": ",".join(seen) if seen else "-",
        "targets": ",".join(sorted(targets)) if targets else "-",
        "kind": "|".join(kind) if kind else "-",
        "txt": txt,
    }


def main():
    pats = [
        "seats/*scratch*/*.sh",
        "seats/*scratch*/*.py",
        "scratch/*/*.sh",
        "scratch/*/*.py",
        "seats/scratch/*.sh",
    ]
    paths = []
    for pat in pats:
        paths.extend(glob.glob(os.path.join(W, pat)))
    # keep scripts that look like polls/watches, plus every .sh
    keep = []
    for p in sorted(set(paths)):
        base = os.path.basename(p).lower()
        if p.endswith(".sh"):
            keep.append(p)
            continue
        if any(k in base for k in ("poll", "watch", "wait", "sample", "liveness", "audit")):
            keep.append(p)
    rows = []
    for p in keep:
        c = classify(p)
        if c:
            rows.append(c)

    # mutual pairs from named targets (script A names seat B AND script B names seat A)
    by_seat = {}
    for r in rows:
        by_seat.setdefault(r["seat"], set()).update(
            t for t in r["targets"].split(",") if t != "-"
        )
    mutual = []
    seats = sorted(by_seat)
    for i, a in enumerate(seats):
        for b in seats[i + 1:]:
            if b in by_seat[a] and a in by_seat[b]:
                mutual.append((a, b))

    # all-reports clique: seats whose scripts are all-reports
    allrep = sorted({r["seat"] for r in rows if r["all_reports"] == "YES"})

    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    with open(OUT, "w") as f:
        f.write(
            f"# waitgraph {now} rows={len(rows)} scripts_seen={len(keep)}\n"
        )
        f.write(
            "seat\tscript\twaits_reports\tall_reports\tthreshold\t"
            "subtract_self\ttries\tbounded\tescape_tokens\ttargets\tkind\n"
        )
        for r in rows:
            f.write("\t".join([
                r["seat"], r["script"], r["waits_reports"], r["all_reports"],
                r["threshold"], r["subtract_self"], r["tries"], r["bounded"],
                r["escape_tokens"], r["targets"], r["kind"],
            ]) + "\n")

    lines = []
    lines.append(f"when={now}")
    lines.append(f"scripts={len(rows)}")
    lines.append(f"all_reports_seats={','.join(allrep) if allrep else 'none'}")
    lines.append(f"mutual_named_pairs={len(mutual)}")
    if mutual:
        for a, b in mutual:
            lines.append(f"  PAIR {a}<->{b}")
            for r in rows:
                if r["seat"] in (a, b):
                    lines.append(
                        f"    {r['seat']} {os.path.basename(r['script'])} "
                        f"all={r['all_reports']} self={r['subtract_self']} "
                        f"tries={r['tries']} bounded={r['bounded']} "
                        f"thr={r['threshold']}"
                    )
    else:
        lines.append("  none")
    # unbounded all-reports
    lines.append("unbounded_all_reports:")
    ub = [r for r in rows if r["all_reports"] == "YES" and r["bounded"] == "NO"]
    if not ub:
        lines.append("  none")
    for r in ub:
        lines.append(f"  {r['seat']} {r['script']} self={r['subtract_self']}")
    # self-inclusive all-reports (the r96/r97 defect)
    lines.append("self_inclusive_all_reports:")
    si = [r for r in rows if r["all_reports"] == "YES" and r["subtract_self"] == "NO"]
    if not si:
        lines.append("  none")
    for r in si:
        lines.append(
            f"  {r['seat']} {r['script']} thr={r['threshold']} tries={r['tries']} bounded={r['bounded']}"
        )
    text = "\n".join(lines) + "\n"
    with open(SUM, "w") as f:
        f.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
