#!/usr/bin/env python3
"""V46 adversarial scan: try to construct accusation / winner / contradiction readings.

Usage: python3 scan.py <fixture-dir> [--base <prior-fixture-dir>]
Prints: (a) JSON inventory + prefix inheritance vs base, (b) token hits per class with
negation-context window, (c) structural implicit-conflict candidates over timeline,
(d) contradictions.json content, (e) line-numbered dump of text surfaces.
"""
import json
import re
import sys
from pathlib import Path

CLASSES = {
    "accusation": [
        "accus", "blam", "fault", "guilt", "guilty", "breach", "violat",
        "broke", "broken", "renege", "betray", "indict", "charge", "charged",
        "reproach", "shirk", "default", "culpab", "offend", "wrongdo", "in the wrong",
    ],
    "winner": [
        "winner", "win", "won", "prevail", "vindicat", "verdict", "ruling",
        "adjudicat", "upheld", "settle", "resolved", "resolution", "correct",
        "right call", "justified", "acquit", "condemn", "absolv", "truth of",
        "the truth", "in fact", "actually happened",
    ],
    "contradiction": [
        "contradict", "conflict", "incompatib", "inconsisten", "disput",
        "refut", "disprov", "disagree", "contest", "false", "untrue",
        "mistaken", "lied", " lie", "error", "deni", "cannot both", "mutually",
    ],
}
NEGATORS = ["no ", "not ", "never", "neither", "without", "does not", "is not",
            "no-", "un", "non-", "neither", "denies", "declines"]

TEXT_FILES = ["fictional-excerpts.md", "README.md", "claim-excerpt-map.md",
              "inspiration-note.md", "source-excerpt.md"]
JSON_FILES = ["entities.json", "relations.json", "contradictions.json",
              "sources.json", "timeline.json"]


def load(d, name):
    p = d / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def counts(d):
    out = {}
    for name in JSON_FILES:
        data = load(d, name)
        out[name] = None if data is None else len(data)
    return out


def prefix_equal(a, b):
    if a is None or b is None:
        return None
    n = min(len(a), len(b))
    return a[:n] == b[:n]


def main():
    d = Path(sys.argv[1]).resolve()
    base = None
    if "--base" in sys.argv:
        base = Path(sys.argv[sys.argv.index("--base") + 1]).resolve()
    print(f"FIXTURE {d}")
    print(f"counts {json.dumps(counts(d), sort_keys=True)}")
    if base:
        print(f"BASE {base}")
        print(f"base-counts {json.dumps(counts(base), sort_keys=True)}")
        for name in JSON_FILES:
            a, b = load(d, name), load(base, name)
            print(f"prefix-equal {name}: {prefix_equal(a, b)} (len {len(a) if a is not None else None} vs {len(b) if b is not None else None})")

    # (b) token scan
    print("\n== TOKEN SCAN ==")
    for name in TEXT_FILES:
        p = d / name
        if not p.exists():
            print(f"-- {name}: MISSING")
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for cls, toks in CLASSES.items():
            for i, line in enumerate(lines, 1):
                low = line.lower()
                for t in toks:
                    if t in low:
                        idx = low.index(t)
                        ctx = line[max(0, idx - 40):idx + len(t) + 40]
                        neg = any(n in low[max(0, idx - 30):idx] for n in NEGATORS)
                        print(f"{name}:{i} [{cls}:{t!r}] neg-before={neg} :: ...{ctx.strip()}...")
    # JSON text surfaces (sources reliability notes, descriptions, claims)
    print("\n== JSON STRING SCAN ==")
    for name in ["sources.json", "timeline.json", "entities.json", "relations.json"]:
        data = load(d, name)
        if data is None:
            continue
        blob = json.dumps(data, ensure_ascii=False)
        for cls, toks in CLASSES.items():
            for t in toks:
                for m in re.finditer(re.escape(t), blob.lower()):
                    ctx = blob[max(0, m.start() - 50):m.end() + 50]
                    print(f"{name} [{cls}:{t!r}] :: ...{ctx}...")

    # (c) structural implicit-conflict candidates
    print("\n== STRUCTURAL CONFLICT CANDIDATES ==")
    tl = load(d, "timeline.json") or []
    for i, e in enumerate(tl):
        for j, f in enumerate(tl):
            if i >= j:
                continue
            if e.get("entity_id") == f.get("entity_id") and e.get("tick") == f.get("tick") \
               and e.get("place_id") != f.get("place_id"):
                print(f"CONFLICT-CANDIDATE same entity {e.get('entity_id')} tick {e.get('tick')}: "
                      f"{e.get('id')}@{e.get('place_id')} vs {f.get('id')}@{f.get('place_id')}")
    ids = {e.get("id"): e for e in tl}
    for e in tl:
        for dep in e.get("depends_on", []):
            tgt = ids.get(dep)
            if tgt is None:
                print(f"DEP-MISSING {e.get('id')} -> {dep}")
            elif isinstance(tgt.get("tick"), int) and isinstance(e.get("tick"), int) and tgt["tick"] > e["tick"]:
                print(f"DEP-ORDER-CONFLICT {e.get('id')} (tick {e.get('tick')}) -> {dep} (tick {tgt.get('tick')})")
    print("(end of structural candidates)")
    cj = load(d, "contradictions.json")
    print(f"contradictions.json = {json.dumps(cj)}")

    # (e) line dumps
    print("\n== LINE DUMPS ==")
    for name in TEXT_FILES:
        p = d / name
        if not p.exists():
            continue
        print(f"\n---- {name} ----")
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            print(f"{i:4d}\t{line}")


if __name__ == "__main__":
    main()
