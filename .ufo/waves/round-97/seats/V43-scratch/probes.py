#!/usr/bin/env python3
"""V43 schema probes: can the delivered gate *speak* reconciliation/blame classes?
On scratch copies only. Mirrors r96 V46 §4 method."""
import json, pathlib, shutil, subprocess, sys

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"
SCR = ROOT / ".ufo/waves/round-97/seats/V43-scratch"

def run(label, cluster):
    r = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", str(cluster)],
                       cwd=ROOT, capture_output=True, text=True)
    print(f"[{label}] exit={r.returncode} stdout={r.stdout.strip()!r} stderr={r.stderr.strip()!r}")

# 1) reconciliation probe: add an entity claim + relation asserting reconciliation
c1 = SCR / "probe-reconciliation"
if c1.exists(): shutil.rmtree(c1)
shutil.copytree(SRC, c1)
ent = json.loads((c1 / "entities.json").read_text())
ent[0]["claims"].append({"statement": "Aru and Evin reconciled at the Chalk Stair and the two accounts were merged into one settled record.",
                         "source_id": "aru-acknowledgment-note"})
(c1 / "entities.json").write_text(json.dumps(ent, indent=2, ensure_ascii=False) + "\n")
rel = json.loads((c1 / "relations.json").read_text())
rel.append({"from": "aru", "to": "evin", "type": "reconciled_after_crossing_dispute", "source_id": "aru-acknowledgment-note"})
(c1 / "relations.json").write_text(json.dumps(rel, indent=2, ensure_ascii=False) + "\n")
run("reconciliation", c1)

# 2) blame probe: add an entity claim asserting fault
c2 = SCR / "probe-blame"
if c2.exists(): shutil.rmtree(c2)
shutil.copytree(SRC, c2)
ent = json.loads((c2 / "entities.json").read_text())
ent[0]["claims"].append({"statement": "Aru blames Evin for the non-arrival and asserts Evin breached the crossing agreement.",
                         "source_id": "aru-acknowledgment-note"})
(c2 / "entities.json").write_text(json.dumps(ent, indent=2, ensure_ascii=False) + "\n")
run("blame", c2)

# 3) contradiction/resolution probe: add a ledger row over the two accounts
c3 = SCR / "probe-contradiction"
if c3.exists(): shutil.rmtree(c3)
shutil.copytree(SRC, c3)
con = json.loads((c3 / "contradictions.json").read_text())
con.append({"id": "account-pair-resolution",
            "claim_a": {"event_id": "aftermath-missing-evin", "field": "place_id"},
            "claim_b": {"event_id": "response-evin-salt-court", "field": "place_id"},
            "why": "Probe: the two accounts conflict and one must prevail."})
(c3 / "contradictions.json").write_text(json.dumps(con, indent=2, ensure_ascii=False) + "\n")
run("contradiction", c3)
