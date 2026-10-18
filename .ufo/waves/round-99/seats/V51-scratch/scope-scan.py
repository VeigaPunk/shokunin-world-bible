#!/usr/bin/env python3
"""Lexical scope scan of r99 fixture + knowledge notes. Read-only."""
import re
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
fix = ROOT / "corpus/fixtures/r99-window-lapse"
files = sorted(fix.glob("*"))
know = list((ROOT / "corpus/knowledge").glob("r99-*"))
targets = files + know
pat = re.compile(
    r"resolut|reconcil|blame|verdict|finding|winner|duty|breach|obligation|open|claim|unfulfill|closed|close",
    re.I,
)
# negation / scoping window: 80 chars before the match
neg = re.compile(
    r"(no |not |never |asserts no|assert no|assigns no|assign no|without |does not |do not |neither |nothing is |closes no|close no)",
    re.I,
)
for p in targets:
    text = p.read_text(errors="replace")
    print(f"\n===== {p.relative_to(ROOT)} ({len(text)} chars) =====")
    for i, ln in enumerate(text.splitlines(), 1):
        if pat.search(ln):
            # flag if the line has a positive-looking hit without a nearby negator
            hits = list(pat.finditer(ln))
            flags = []
            for h in hits:
                window = ln[max(0, h.start() - 48) : h.end() + 12]
                if not neg.search(window) and not re.search(r"OPEN|open entry|stays open|matter open|historical open|unfulfilled|has closed|window closed|No claim", window, re.I):
                    flags.append(h.group(0))
            mark = "UNSCOPED" if flags else "scoped"
            if flags or True:
                print(f"  L{i} [{mark}{' '+','.join(flags) if flags else ''}] {ln[:220]}")
