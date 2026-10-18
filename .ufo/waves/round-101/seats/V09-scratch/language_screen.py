#!/usr/bin/env python3
"""V09 lexical screen: winner-selection / world-truth / chronology-auth language.

Prints every regex hit with line number and the full line so each hit can be
adjudicated in context (quoted excerpt text legitimately contains e.g.
"select no winner" — negations are fine; assertions are not).
"""
import re
import sys

PATH = sys.argv[1]
text = open(PATH, encoding="utf-8").read()

GROUPS = {
    "winner-selection": (
        r"\b(winners?|wins?|won|prevails?|vindicated?|refuted?|disprov(?:e|en|es)|"
        r"adjudicat\w*|arbitrat\w*|verdicts?|reconcil\w*|resolves?|resolved|resolving|"
        r"corroborat\w*|confirms?|confirmed|prefer(?:s|red|rence)?|settles?|settled|"
        r"overrules?|overruled|superseded?\b|retired?\b|favors?|favour\w*)\b"
    ),
    "world-truth": (
        r"\b(actually|in fact|establish(?:es|ed)?|proves?|proven|proof|truth|true|false|"
        r"real(?:ly|ity)?|objective(?:ly)?|canon(?:ical)?|authentic\w*|verified|"
        r"grounds?|facts?)\b"
    ),
    "chronology-auth": (
        r"\b(chronolog\w*|date[sd]? (?:of|is|was)|real date|historical fact|"
        r"proves? the (?:order|sequence|timing)|establishes? the (?:order|sequence|timing)|"
        r"literal tick|actual tick|tick (?:proves|establishes|confirms)|"
        r"depends_on (?:proves|establishes|confirms)|sequence (?:proves|establishes|confirms))\b"
    ),
}

hits = 0
for group, pat in GROUPS.items():
    rx = re.compile(pat, re.I)
    print(f"=== {group} ===")
    for i, line in enumerate(text.splitlines(), 1):
        m = rx.search(line)
        if m:
            hits += 1
            print(f"L{i} [{m.group(0)}] {line.strip()}")
    print()

# convention probes: bare source-id mentions and namespace-qualification forms
print("=== source-id qualification probes ===")
for probe in (
    r"aru-aftermath-note", r"evin-response-note", r"crossing-minute",
    r"r95-crossing-aftermath:", r"r96-crossing-response:",
    r"r94-paired-crossing:", r"cluster-relative", r"namespace",
    r"path-qualified", r"cross-cluster-contradictions",
    r"l0-questions", r"comparison outcomes",
):
    rx = re.compile(re.escape(probe) if probe.startswith(("r9", "aru", "evin", "crossing")) else probe, re.I)
    n = len(rx.findall(text))
    print(f"{probe!r}: {n} occurrence(s)")
    for i, line in enumerate(text.splitlines(), 1):
        if rx.search(line):
            print(f"  L{i}: {line.strip()[:160]}")
print(f"\nTOTAL language hits: {hits}")
