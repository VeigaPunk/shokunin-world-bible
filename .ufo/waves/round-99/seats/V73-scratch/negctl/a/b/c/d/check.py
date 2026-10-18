"""F29 — SHONEN.md canonical-form + evidence-pointer replay (read-only).

Replays the mechanical verification PROTOCOL.md:417 describes for the
canonical SHONEN.md form (seed block byte-identical modulo <name>; marks
confined to the box character plus at most one indented evidence line per
box; no added/removed boxes), and resolves the two evidence pointers the
file carries. Writes nothing; exits 0 iff every check passes.
"""
from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parents[4]  # .ufo/waves/round-93/deepseek -> lane root

seed_boxes = [
    "SKILL.md contains real decision tables, error patterns, checklists, cited sources",
    "At least one end-to-end domain task executed and logged in LOG.md",
    "Instructions executable by an agent without oral context",
    "No cross-domain bleed (PROVINCE.md still accurate)",
]

text = (root / "SHONEN.md").read_text(encoding="utf-8")
lines = text.splitlines()
checks = {}

checks["title matches seed modulo <name>"] = (
    lines[0] == f"# {root.name} — Promotion checklist"
)
checks["seed frame (blank + manifest line)"] = lines[1:4] == [
    "",
    "Promotion to shokunin requires all of:",
    "",
]

boxes = []
evidence = {}
i = 4
while i < len(lines):
    line = lines[i]
    if line.startswith("- [") and len(line) > 6 and line[4] == "]" and line[5] == " ":
        boxes.append((line[3], line[6:]))
        block = []
        j = i + 1
        while j < len(lines) and lines[j].startswith("  "):
            block.append(lines[j])
            j += 1
        if block:
            evidence[len(boxes) - 1] = block
        i = j
    else:
        checks[f"line {i + 1} is not a box or evidence line"] = False
        i += 1

checks["four boxes, seed order and text"] = [b for _, b in boxes] == seed_boxes
checks["marks confined to box character"] = all(m in " ~x" for m, _ in boxes)
checks["no [x] promotion claim present"] = all(m != "x" for m, _ in boxes)
checks["at most one evidence line per box"] = all(
    len(block) == 1 for block in evidence.values()
)
checks["both [~] boxes carry their required pointer"] = all(
    idx in evidence for idx, (m, _) in enumerate(boxes) if m == "~"
)

log = (root / "LOG.md").read_text(encoding="utf-8")
b2 = evidence.get(1, [""])[0]
checks["box2 evidence names the LOG.md entry"] = (
    "LOG.md" in b2
    and "Fleet round 1 — calibration declaration before batched dispatch" in log
    and "Fleet round 1 — calibration declaration before batched dispatch" in b2
)
checks["box2 evidence names reports/round-1/baseline-probes.json"] = (
    (root / "reports/round-1/baseline-probes.json").is_file()
    and "reports/round-1/baseline-probes.json" in b2
)

province = (root / "PROVINCE.md").read_text(encoding="utf-8").splitlines()
b4 = evidence.get(3, [""])[0]
checks["box4 evidence cites PROVINCE.md:3-11 within range"] = (
    "PROVINCE.md:3-11" in b4 and len(province) >= 11
)

for label, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'} {label}")
for name in ("SHONEN.md", "SKILL.md", "PROVINCE.md"):
    digest = sha256((root / name).read_bytes()).hexdigest()
    print(f"SHA256 {name} {digest}")
raise SystemExit(not all(checks.values()))
