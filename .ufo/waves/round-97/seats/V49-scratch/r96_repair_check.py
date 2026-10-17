#!/usr/bin/env python3
"""V49 r96-repair scope check: prove the r96-crossing-response diff touches ONLY
claim-excerpt-map.md, and that its data rows are byte-unchanged (cosmetic only)."""
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "f3e09f9"
FIXTURE = "corpus/fixtures/r96-crossing-response"


def run(*a):
    return subprocess.run(a, cwd=REPO, capture_output=True, text=True)


def main():
    ns = run("git", "diff", "--name-status", BASE, "--", FIXTURE).stdout.strip()
    print(f"## git diff --name-status {BASE} -- {FIXTURE}\n{ns or '(empty)'}")
    changed = [l.split("\t")[-1] for l in ns.splitlines() if l.strip()]
    print(f"## files changed in fixture: {len(changed)} -> {changed}")
    if changed != ["corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"]:
        print("## RESULT: UNEXPECTED SCOPE")
    else:
        print("## RESULT: scope == exactly claim-excerpt-map.md (declared cosmetic target)")

    old = run("git", "show", f"{BASE}:{FIXTURE}/claim-excerpt-map.md").stdout.splitlines()
    try:
        new = open(f"{REPO}/{FIXTURE}/claim-excerpt-map.md", encoding="utf-8").read().splitlines()
    except OSError as e:
        print(f"## cannot read worktree file: {e}")
        return
    print(f"## lines: base={len(old)} wt={len(new)}")
    # data rows = table rows beginning with '|' excluding header/delimiter
    def rows(lines):
        out = []
        for ln in lines:
            s = ln.strip()
            if s.startswith("|") and set(s.replace("|", "").replace(" ", "")) <= {"-", ":"}:
                continue
            if s.startswith("|"):
                out.append(s)
        return out
    o, n = rows(old), rows(new)
    print(f"## data rows (non-delimiter): base={len(o)} wt={len(n)}")
    same = sum(1 for a, b in zip(o, n) if a == b)
    print(f"## data rows identical positionally: {same}/{min(len(o), len(n))}")
    for i, (a, b) in enumerate(zip(o, n)):
        if a != b:
            print(f"  ROW-DIFF[{i}]\n    base: {a}\n    wt  : {b}")
    print("## unified diff:")
    print(run("git", "diff", "--no-color", "-U2", BASE, "--", f"{FIXTURE}/claim-excerpt-map.md").stdout)


if __name__ == "__main__":
    sys.exit(main())
