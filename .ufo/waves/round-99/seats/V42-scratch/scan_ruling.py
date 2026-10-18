#!/usr/bin/env python3
"""Lexical + structural scan for a ruling/resolution reading over r99-window-lapse.

Scratch-only. Does not modify corpus. Prints token hits with local negation context.
"""
import json
import re
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX = ROOT / "corpus/fixtures/r99-window-lapse"
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
    "r99-window-lapse",
]

# Ruling / resolution class. Word-ish tokens; order does not matter.
PATTERNS = [
    r"resolut\w*",
    r"resolv\w*",
    r"reconcil\w*",
    r"\bblame\b",
    r"blam\w*",
    r"adjudicat\w*",
    r"\bruling\b",
    r"\bruled\b",
    r"\brules\b",
    r"verdict\w*",
    r"\bfinding\b",
    r"\bfindings\b",
    r"\bjudgment\b",
    r"\bjudgement\b",
    r"\bjudged\b",
    r"decree\w*",
    r"determin\w*",
    r"official\w*",
    r"authorit\w*",
    r"jurisdict\w*",
    r"\bclosed\b",
    r"\bcloses\b",
    r"\bclose\b",
    r"\bclosure\b",
    r"unfulfill\w*",
    r"\blodged\b",
    r"\bclaim\b",
    r"\bclaims\b",
    r"\bbreach\b",
    r"\bdefault\b",
    r"\bforfeit\w*",
    r"\bliable\b",
    r"\bliability\b",
    r"\bguilty\b",
    r"\bfault\b",
    r"\bwinner\b",
    r"\blose[rs]?\b",
    r"\bopen\b",
    r"historical",
    r"window",
]
RX = re.compile("|".join(f"(?:{p})" for p in PATTERNS), re.I)
NEG = re.compile(
    r"\b(no|not|never|neither|nothing|without|asserts no|assert no|assign no|"
    r"assigns no|record no|records no|reach no|reaches no|selects no|select no|"
    r"does not|do not|did not|is not|are not|unresolved|unfulfilled)\b",
    re.I,
)

def windows(text, path):
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for m in RX.finditer(line):
            start = max(0, m.start() - 80)
            end = min(len(line), m.end() + 80)
            ctx = line[start:end].replace("\t", " ")
            before = line[max(0, m.start() - 60):m.start()]
            neg = bool(NEG.search(before)) or bool(re.search(r"\bno\b|\bnot\b", before, re.I))
            print(f"{path}:{i}:{m.start()} TOKEN={m.group()!r} NEG-BEFORE={neg}")
            print(f"    {ctx}")

def main():
    print("=== r99 ten-file token scan ===")
    for p in sorted(FIX.iterdir()):
        if p.is_file():
            windows(p.read_text(encoding="utf-8"), p.name)
    print("=== structural JSON ===")
    ents = json.loads((FIX / "entities.json").read_text())
    rels = json.loads((FIX / "relations.json").read_text())
    tl = json.loads((FIX / "timeline.json").read_text())
    src = json.loads((FIX / "sources.json").read_text())
    con = json.loads((FIX / "contradictions.json").read_text())
    print("entities", [(e["id"], e["kind"]) for e in ents])
    print("relations", rels)
    print("contradictions", con)
    print("events", [(e["id"], e["tick"], e["entity_id"], e["depends_on"], e["source_id"]) for e in tl])
    print("sources", [s["id"] for s in src])
    print("institution entities", [e["id"] for e in ents if e.get("kind") not in ("character", "place", "item")])
    print("=== chain institution/ruling tokens (non-r99) ===")
    chain_rx = re.compile(r"tribunal|registry|court|authority|ruling|verdict|adjudicat|decree|resolution|blame", re.I)
    for name in CHAIN[:-1]:
        d = ROOT / "corpus/fixtures" / name
        if not d.is_dir():
            print(name, "ABSENT")
            continue
        for p in sorted(d.iterdir()):
            if not p.is_file():
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                if chain_rx.search(line):
                    # skip very long map boilerplate by still printing, truncated
                    snippet = line.strip()[:180]
                    print(f"{name}/{p.name}:{i}: {snippet}")

if __name__ == "__main__":
    main()
