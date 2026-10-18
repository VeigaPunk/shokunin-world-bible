import re, sys, pathlib
d = pathlib.Path(".")
for f in sorted(d.glob("*.md")):
    if f.name.startswith("V35"):
        continue
    text = f.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    print(f"\n########## {f.name} ({len(lines)} lines) ##########")
    # verdict/status/bottom-line lines and any flagged items
    pat = re.compile(r"(bottom line|verdict|STATUS|PASS|FAIL|INCONCLUSIVE|ABSENT|PENDING|IN PROGRESS|conflict|harm|residual|bound|NOTE|MISMATCH|OPEN)", re.I)
    shown = 0
    for i, l in enumerate(lines):
        if re.match(r"^\s*(#|Bottom|BOTTOM|VERDICT|Status|STATUS)", l) and shown < 60:
            print(f"  H| {l.strip()[:240]}"); shown += 1
    for i, l in enumerate(lines):
        if pat.search(l) and not l.strip().startswith("#"):
            s = l.strip()
            if len(s) > 3:
                print(f"  {i+1:4d}| {s[:300]}")
