#!/usr/bin/env python3
"""V16 scratch: build the normalized source-debt inventory (r94-r101)
from the original ledgers, for cross-checking U1's r102-debt-ledger.json.
Read-only on all sources. Output: V16-scratch/source-inventory.json
"""
import json, re, os

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source-inventory.json")

inv = {}  # source_key -> {"path":..., "count":N, "items":[{"id":..,"group":..,"note":str}]}

def add(src, path, items):
    inv[src] = {"path": path, "count": len(items), "items": items}

def item(gid, group, note=""):
    return {"id": gid, "group": group, "note": note[:160]}

# ---- r94 F29 (markdown tables) ----
txt = open(f"{LANE}/.ufo/waves/round-94/followup/F29-debt.md").read()
rows = re.findall(r"^\| ((?:CC|BR|CR|S)-\d+) \|", txt, re.M)
add("r94-F29", ".ufo/waves/round-94/followup/F29-debt.md", [item(r, r.split("-")[0]) for r in rows])

# ---- r95 / r96 / r97 (JSON items[]) ----
for src, path in [("r95-V31", ".ufo/waves/round-95/seats/V31-debt.json"),
                  ("r96-V40", ".ufo/waves/round-96/seats/V40-debt.json"),
                  ("r97-V37", ".ufo/waves/round-97/seats/V37-debt.json")]:
    d = json.load(open(f"{LANE}/{path}"))
    add(src, path, [item(i["id"], i.get("group", ""), i.get("description", "")) for i in d["items"]])

# ---- r98 V33 (JSON, split structure) ----
d = json.load(open(f"{LANE}/.ufo/waves/round-98/seats/V33-debt.json"))
its = [item(i["id"], "NB", i.get("summary", "")) for i in d["bounds_new"]]
bc = d["bounds_carried"]
for gid, note in bc["closed"].items():
    its.append(item(gid, "CO-closed", str(note)))
for gid, note in bc["recurring"].items():
    its.append(item(gid, "CO-recurring", str(note)))
for el in bc["open_or_accepted"]:
    gid = el.split()[0] if isinstance(el, str) else el.get("id", "?")
    its.append(item(gid, "CO-open_or_accepted", el if isinstance(el, str) else json.dumps(el)))
for gid, note in bc["not_recurring"].items():
    its.append(item(gid, "CO-not_recurring", str(note)))
its += [item(i["id"], "CL", i.get("summary", "")) for i in d["closure_items"]]
its += [item(i["id"], "PR", i.get("summary", "")) for i in d["process_observations"]]
its += [item(i["id"], "ST", i.get("summary", "")) for i in d["supersessions"]]
add("r98-V33", ".ufo/waves/round-98/seats/V33-debt.json", its)

# ---- r99 V36 (JSON) ----
d = json.load(open(f"{LANE}/.ufo/waves/round-99/seats/V36-debt.json"))
its = [item(i["id"], "NB", i.get("summary", "")) for i in d["bounds_new"]]
for grp, els in d["bounds_carried"].items():
    for el in els:
        gid = el.split()[0]
        its.append(item(gid, f"CO-{grp}", el))
its += [item(el.split()[0], "CL", el) for el in d["closure_items"]]
add("r99-V36", ".ufo/waves/round-99/seats/V36-debt.json", its)

# ---- r99 V74-debt-2 (markdown tables) ----
txt = open(f"{LANE}/.ufo/waves/round-99/seats/V74-debt-2.md").read()
rows = re.findall(r"^\| ((?:NB|CO|CL|PR|ST)-\d+) \|", txt, re.M)
add("r99-V74", ".ufo/waves/round-99/seats/V74-debt-2.md",
    [item(r, r.split("-")[0]) for r in sorted(set(rows))])

# ---- r100 carried notes (LOG closure AC items, extracted by hand from prose) ----
r100_notes = ["AC-ROSTER", "AC-BASELINE", "AC-RECEIPT-ERRATUM", "AC-DOCS", "AC-SCOPE", "AC-CLOSE",
              "V15-FAIL-recorded", "V18-FAIL-recorded", "V20-FAIL-recorded",
              "V21-qualification-recorded", "V30-qualification-recorded"]
add("r100-LOG-notes", "LOG.md Round-100 closure section", [item(x, "AC") for x in r100_notes])

# ---- r101 carried notes (V24 adjudicator AC + defects) ----
r101_notes = ["AC-1", "AC-2", "AC-3", "AC-4",
              "defect-1", "defect-2", "defect-3", "defect-4", "defect-5", "defect-6"]
add("r101-V24-notes", ".ufo/waves/round-101/seats/V24-adjudicator.md", [item(x, "AC") for x in r101_notes])

json.dump(inv, open(OUT, "w"), indent=1)
total = sum(v["count"] for v in inv.values())
print(f"wrote {OUT}")
for k, v in inv.items():
    print(f"{k:16s} {v['count']:4d}  {v['path']}")
print(f"{'TOTAL':16s} {total:4d}")
