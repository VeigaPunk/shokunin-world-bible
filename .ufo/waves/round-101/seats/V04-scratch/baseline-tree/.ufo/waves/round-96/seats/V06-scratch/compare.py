#!/usr/bin/env python3
"""V06 compare: expected post-r96 exit/finding table vs observed runs.

Required expectations encode the C1 claim text (exit 1 / exit 2 / stable IDs);
co-firing extras (e.g. inventory_mismatch alongside duplicate_mapping) are
reported as EXTRAS, not failures, because the gating change legitimately adds
the inventory finding when observed != declared rows.
"""
import re
import sys
from pathlib import Path

SC = Path(__file__).resolve().parent

EXPECTED = {
    # case: (exit, required_ids, note)
    "base":  (0, [], "unmodified r93 copy stays PASS"),
    "a":     (1, ["missing_obligation"], "unmapped raw claim"),
    "b":     (1, ["duplicate_mapping"], "duplicate map row"),
    "c":     (1, ["phantom_obligation"], "phantom pointer"),
    "d":     (1, ["source_id_mismatch"], "source-ID mismatch"),
    "e":     (2, ["malformed_json"], "truncated entities.json"),
    "f1":    (2, ["map_missing"], "--map missing-map.md"),
    "f2":    (2, ["foreign_path"], "--map outside cluster"),
    "f3":    (2, ["unsafe_path"], "--map ../outside-map/..."),
    "f4":    (2, ["map_missing"], "--map . (directory)"),
    "g1":    (1, ["schema_drift"], "renamed claims key, row removed"),
    "g2":    (1, ["schema_drift"], "renamed claims key, row kept"),
    "h1":    (1, ["inventory_mismatch"], "deleted entities[0].claims + its row"),
    "h2":    (1, ["inventory_mismatch"], "deleted one claim + its row"),
    "i1":    (1, ["dual_pointer"], "legacy parenthetical, canonical 2nd pointer"),
    "i2":    (1, ["dual_pointer"], "legacy parenthetical, legacy 2nd pointer"),
    "i3":    (1, ["dual_pointer"], "legacy colon prose, legacy 2nd pointer"),
    "i4":    (1, ["dual_pointer"], "legacy colon prose, mapped 2nd pointer"),
    "ctrl-legacy-note":  (0, [], "legacy cell, non-pointer note"),
    "ctrl-legacy-prose": (0, [], "legacy cell, non-pointer prose"),
    "ctrl-canonical-note": (2, ["unsupported_map"], "canonical cell, pointer in note"),
    "ctrl-inv-declared-wrong": (1, ["inventory_mismatch"], "declared 99 vs observed 12"),
    "ctrl-inv-malformed": (None, [], "malformed declaration: record observed"),
}

FINDING = re.compile(r"^FINDING ([a-z_]+):")
RESULT = re.compile(r"^RESULT ([A-Z]+)")
EXIT = re.compile(r"^EXIT=([0-9]+)")


def parse(path):
    ids, res, code = [], None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = FINDING.match(line)
        if m:
            ids.append(m.group(1))
        m = RESULT.match(line)
        if m:
            res = m.group(1)
        m = EXIT.match(line)
        if m:
            code = int(m.group(1))
    return ids, res, code


def main(label):
    runs = SC / f"runs-{label}"
    verdict = True
    for case, (exp_exit, req, note) in EXPECTED.items():
        for pass_no in (1, 2):
            path = runs / f"{case}-run{pass_no}.out"
            if not path.exists():
                print(f"{case:22s} pass{pass_no} MISSING {path}")
                verdict = False
                continue
            ids, res, code = parse(path)
            missing = [i for i in req if i not in ids]
            extras = [i for i in ids if i not in req]
            ok = (exp_exit is None or code == exp_exit) and not missing
            verdict &= ok
            tag = "MATCH" if ok else "CHANGED"
            extra_s = f" extras=[{','.join(extras)}]" if extras else ""
            print(f"{case:22s} pass{pass_no} {tag:8s} exit={code} "
                  f"required={'+'.join(req) or 'none'}{extra_s}  # {note}")
            if not ok:
                print(f"    observed findings={ids} result={res}")
    print(f"VERDICT: {'ALL-MATCH' if verdict else 'CHANGED-CASES-PRESENT'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "new"))
