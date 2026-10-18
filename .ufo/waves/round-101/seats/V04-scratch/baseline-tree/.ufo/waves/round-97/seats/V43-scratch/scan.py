#!/usr/bin/env python3
"""V43 lexical + structural scan: reconciliation / blame / resolution constructibility."""
import json, re, sys, pathlib

FIX = pathlib.Path(sys.argv[1])
CLASSES = {
    "reconciliation": r"reconcil|forgiv|pardon|settl|peace|accord|amends|mutual|reunit|both stand|stand together|accept(?:s|ed)? the account|closes? the (?:question|matter)",
    "blame": r"accus|blam|fault|guilt|culp|breach|betray|liar|lied|wrong(?:s|ed|ing)?\b|charge[ds]?|indict|at fault|to blame",
    "resolution": r"resolv|winner|adjudicat|verdict|decid(?:e|es|ed) (?:who|which)|prevail|supersed|conclud|settle|truth of|correct(?:ly)?|prove[ds]?",
}
NEG = re.compile(r"\b(no|not|never|neither|nor|without|un(?:resolved|reconciled)|nothing)\b", re.I)

def scan_text(label, text):
    out = []
    for name, pat in CLASSES.items():
        for m in re.finditer(pat, text, re.I):
            s, e = m.start(), m.end()
            before = text[max(0, s-60):s].replace("\n", " ")
            after = text[e:e+60].replace("\n", " ")
            neg = bool(NEG.search(text[max(0, s-40):e+10]))
            line = text[:s].count("\n") + 1
            out.append((name, line, neg, text[s:e], before, after))
    return out

print("== TEXT SURFACES ==")
for f in sorted(FIX.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    for name, line, neg, tok, before, after in scan_text(f.name, t):
        print(f"{f.name}:{line} class={name} neg={neg} token={tok!r} ...{before}[[{tok}]]{after}...")
for f in sorted(FIX.glob("*.json")):
    t = f.read_text(encoding="utf-8")
    for name, line, neg, tok, before, after in scan_text(f.name, t):
        print(f"{f.name}:{line} class={name} neg={neg} token={tok!r} ...{before}[[{tok}]]{after}...")

print("\n== STRUCTURAL: timeline ==")
tl = json.loads((FIX / "timeline.json").read_text())
by_id = {e["id"]: e for e in tl}
# same actor same tick different place
pairs = []
for i, a in enumerate(tl):
    for b in tl[i+1:]:
        if a.get("entity_id") == b.get("entity_id") and a.get("tick") == b.get("tick") and a.get("place_id") != b.get("place_id"):
            pairs.append((a["id"], b["id"]))
print("same-actor-same-tick-different-place pairs:", pairs)
# depends_on resolution + forward-time
for e in tl:
    for d in e.get("depends_on", []):
        if d not in by_id:
            print(f"UNRESOLVED edge {e['id']} -> {d}")
        elif by_id[d].get("tick", 0) >= e.get("tick", 0):
            print(f"FORWARD-TIME edge {e['id']}(tick {e['tick']}) -> {d}(tick {by_id[d]['tick']})")
print("ticks:", [(e["id"], e.get("tick"), e.get("entity_id"), e.get("place_id")) for e in tl])
