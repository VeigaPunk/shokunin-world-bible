#!/usr/bin/env python3
"""Compare J-rows of two claim-excerpt maps. Cells split on '|'. Namespace cell is index 3."""
import sys


def jrows(path):
    rows = {}
    order = []
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.startswith("| J"):
                continue
            parts = line.rstrip("\n").split("|")
            cells = [p.strip() for p in parts[1:-1]]
            rid = cells[0]
            rows[rid] = (lineno, cells)
            order.append(rid)
    return rows, order


def main():
    a_path, b_path = sys.argv[1], sys.argv[2]
    a, a_order = jrows(a_path)
    b, b_order = jrows(b_path)
    print(f"A rows: {len(a)}  B rows: {len(b)}")
    print("B-only:", [k for k in b_order if k not in a])
    print("A-only:", [k for k in a_order if k not in b])
    ns_only = []
    other = []
    for rid in a_order:
        if rid not in b:
            continue
        ac, bc = a[rid][1], b[rid][1]
        diffs = []
        n = max(len(ac), len(bc))
        for i in range(n):
            av = ac[i] if i < len(ac) else None
            bv = bc[i] if i < len(bc) else None
            if av != bv:
                diffs.append((i, av, bv))
        if not diffs:
            print(f"{rid}: cells={len(ac)}/{len(bc)} IDENTICAL line {a[rid][0]}->{b[rid][0]}")
        elif len(diffs) == 1 and diffs[0][0] == 3:
            ns_only.append(rid)
            print(f"{rid}: cells={len(ac)}/{len(bc)} diffs={diffs}")
        else:
            other.append(rid)
            print(f"{rid}: cells={len(ac)}/{len(bc)} diffs={diffs}")
    print(f"namespace-only inherited: {len(ns_only)} {ns_only}")
    print(f"other diffs: {other}")
    if "J11" in a and "J11" in b:
        print("J11 line A", a["J11"][0], "B", b["J11"][0])
        print("J11 cells equal except index 3:", all(
            a["J11"][1][i] == b["J11"][1][i] for i in range(len(a["J11"][1])) if i != 3
        ))
        print("J11 anchor equal:", a["J11"][1][-1] == b["J11"][1][-1])
        print("J11 A anchor:", a["J11"][1][-1])
        print("J11 B anchor:", b["J11"][1][-1])


if __name__ == "__main__":
    main()
