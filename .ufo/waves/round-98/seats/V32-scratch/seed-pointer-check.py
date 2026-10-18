"""V32 independent seed-block diff + evidence-pointer resolution (read-only)."""
from pathlib import Path
import subprocess, sys

root = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
fleet = Path("/home/vgpnk/Projects/shokunin")

# --- seed block from PROTOCOL.md:425-432 ---
pl = (fleet / "PROTOCOL.md").read_text(encoding="utf-8").splitlines()
seed = [l[4:] if l.startswith("    ") else l for l in pl[424:432]]
seed = [l.replace("<name>", "lore-shokunin") for l in seed]
print("seed raw lines 425-432:")
for i, l in enumerate(seed, start=425):
    print(f"  {i}: {l!r}")

live = (root / "SHONEN.md").read_text(encoding="utf-8").splitlines()
frame_live = live[0:4]
frame_seed = seed[0:4]
print("frame match:", frame_live == frame_seed)

def box_text(line):
    # '- [m] text'
    return line[6:]

live_boxes = [l for l in live if l.startswith("- [")]
seed_boxes = seed[4:8]
lt = [box_text(l) for l in live_boxes]
st = [box_text(l) for l in seed_boxes]
print("box texts match (marks/evidence excluded):", lt == st)
print("seed marks all '[ ]':", all(l[3] == " " for l in seed_boxes))
for i in range(4):
    print(f"  frame {i+1} OK: {frame_live[i] == frame_seed[i]}; box {i+1} OK: {lt[i] == st[i]}")

# --- evidence pointer resolution ---
ptr_paths = [
    "SKILL.md",
    ".ufo/waves/round-93/recovery/R08-skill-check.py",
    ".ufo/waves/round-93/deepseek/F21.md",
    ".ufo/waves/round-93/deepseek/F29.md",
    "reports/round-1/baseline-probes.json",
    ".ufo/waves/round-93/deepseek/F01.md",
    ".ufo/waves/round-93/deepseek/F25-replay.py",
    ".ufo/waves/round-93/deepseek/F31.md",
    ".ufo/waves/round-93/deepseek/F14-postrepair-check.py",
    ".ufo/waves/round-93/deepseek/F03.md",
    ".ufo/waves/round-93/deepseek/F24.md",
]
ok = 0
for p in ptr_paths:
    e = (root / p).exists()
    ok += e
    print(f"PTR {'OK ' if e else 'MISS'} {p}")
print(f"pointers resolved: {ok}/{len(ptr_paths)}")
print("PROVINCE.md exists:", (root / "PROVINCE.md").exists())
print("LOG.md exists:", (root / "LOG.md").exists())

log = (root / "LOG.md").read_text(encoding="utf-8")
entry = "Fleet round 1 — calibration declaration before batched dispatch"
print(f"LOG entry count: {log.count(entry)}")
prov = (root / "PROVINCE.md").read_text(encoding="utf-8").splitlines()
print("PROVINCE.md:3-11 ->", prov[2:11])
