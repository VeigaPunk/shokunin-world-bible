#!/usr/bin/env python3
"""F14 second pass: near-miss key distances, per-file mention locations, genre/field probes.

Reads the persisted F14-namespace-inventory.json for the inventories and adds:
- Levenshtein distance 1-2 pairs between M2 keys and prior keys (disguised-identity probe),
- per-file location of prior-cluster display names inside M2 (contrast vs in-world),
- M2 in-world-content token probe for r87/r88 occasion words (vow/tide/bell/saltmonth/moon/basin),
- alias/epithet field census and the corrected r89 demo disclaimer check.
"""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path("corpus/fixtures")
M2 = "r93-m2-kojiki-cluster"
PRIORS = ("r87-myth-cluster", "r88-m3-maya-cluster")
INV = json.loads(Path(".ufo/waves/round-93/deepseek/F14-namespace-inventory.json").read_text(encoding="utf-8"))
CONTENT_FILES = [f for f in INV["fixtures"][M2]["file_sha256"] if f != "README.md"]


def lev(a: str, b: str) -> int:
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def key_set(cluster):
    n = INV["fixtures"][cluster]["normalized"]
    return {
        "entity_ids": n["entity_ids"],
        "entity_labels": n["entity_labels"],
        "event_ids": n["event_ids"],
        "source_ids": n["source_ids_bare"],
    }


print("=== near-miss keys (Levenshtein 1-2), M2 vs priors ===")
m2_keys = key_set(M2)
for prior in PRIORS:
    p_keys = key_set(prior)
    pairs = []
    for kind, a_vals in m2_keys.items():
        for a in a_vals:
            for kind_b, b_vals in p_keys.items():
                for b in b_vals:
                    d = lev(a, b)
                    if 1 <= d <= 2:
                        pairs.append({"m2": f"{kind}:{a}", "prior": f"{kind_b}:{b}", "distance": d})
    print(prior, "near_miss_pairs:", json.dumps(pairs, sort_keys=True))

print("\n=== prior display-name mentions inside M2, by file ===")
for prior in PRIORS:
    names = [e["name"] for e in INV["fixtures"][prior]["referents"]]
    print(f"-- {prior}: {names}")
    for f in sorted(INV["fixtures"][M2]["file_sha256"]):
        text = (ROOT / M2 / f).read_text(encoding="utf-8")
        for n in names:
            for m in re.finditer(r"\b" + re.escape(n) + r"\b", text):
                line = text.count("\n", 0, m.start()) + 1
                print(f"   {f}:{line} name={n!r}")

print("\n=== M2 non-README content probe (r87/r88 occasion words) ===")
probe = ("vow", "tide", "bell", "saltmonth", "moon", "basin", "reed", "dune", "shell", "lantern", "court", "hymn")
for f in sorted(CONTENT_FILES):
    text = (ROOT / M2 / f).read_text(encoding="utf-8").casefold()
    hits = sorted({w for w in probe if re.search(r"\b" + w, text)})
    print(f"   {f}: {hits if hits else 'none'}")

print("\n=== alias/epithet field census ===")
for name in (M2, *PRIORS):
    print(f"   {name}: {INV['fixtures'][name]['alias_epithet_fields']}")

print("\n=== r89 demo disclaimer (corrected substring) ===")
demo = Path("corpus/knowledge/r89-cross-cluster-contradiction.md").read_text(encoding="utf-8")
print("   disclaims_register:", "integration-ready register entry" in demo)
print("   names_live_register_destination:", "corpus/knowledge/cross-cluster-contradictions.md" in demo)

print("\n=== M2 vs r88 near-miss lexical pair check ===")
for a, b in (("slatetable", "saltcourt"), ("slatetable", "saltmonth"), ("lornindex", "lantern")):
    print(f"   {a} vs {b}: distance={lev(a, b)}")
