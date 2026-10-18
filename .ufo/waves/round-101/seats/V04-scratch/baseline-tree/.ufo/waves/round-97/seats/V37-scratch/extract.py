#!/usr/bin/env python3
"""V37 scratch: extract summary lines from round-97 seat reports.

Usage: python3 extract.py <seats-dir> [--bounds]
Prints per report: file, first heading, bottom-line candidate, and keyword lines.
"""
import sys, os, re, glob

KW = re.compile(r"(bound|debt|residual|caveat|not shown|unproven|limitation|"
                r"cannot|does not|no persisted|carried|open|absent|stale|drift|"
                r"FAIL|INCONCLUSIVE|hazard|boundary|gap)", re.I)
BOTTOM = re.compile(r"bottom line", re.I)

def main():
    d = sys.argv[1]
    bounds = "--bounds" in sys.argv
    files = sorted(glob.glob(os.path.join(d, "*.md")))
    for f in files:
        base = os.path.basename(f)
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"== {base}: UNREADABLE {e}")
            continue
        lines = text.splitlines()
        first = next((l for l in lines if l.strip()), "")
        bottom = ""
        for i, l in enumerate(lines):
            if BOTTOM.search(l):
                bottom = " / ".join(x.strip() for x in lines[i:i+4] if x.strip())[:400]
                break
        print(f"== {base} | {first[:150]}")
        if bottom:
            print(f"   BOTTOM: {bottom}")
        if bounds:
            seen = 0
            for i, l in enumerate(lines):
                if KW.search(l) and len(l.strip()) > 12:
                    print(f"   L{i+1}: {l.strip()[:220]}")
                    seen += 1
                    if seen >= 14:
                        break

if __name__ == "__main__":
    main()
