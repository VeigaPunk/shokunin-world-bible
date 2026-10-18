#!/usr/bin/env python3
"""V11 inherited-equality: r99-window-lapse vs r98-clerk-filing at 4265df5.

r98 side is always the bytes extracted from git show 4265df5 (baseline-r98/),
never the worktree, except where a second comparison is explicitly labeled.
Key order is part of equality: json.loads(object_pairs_hook=OrderedDict).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = LANE / ".ufo/waves/round-99/seats/V11-scratch/baseline-r98"
R99 = LANE / "corpus/fixtures/r99-window-lapse"
R98_WT = LANE / "corpus/fixtures/r98-clerk-filing"
COMMIT = "4265df5"

fails = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global fails
    if not ok:
        fails += 1
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""))


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(rel: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(LANE), "show", f"{COMMIT}:{rel}"],
    )


def main() -> int:
    print(f"python {sys.version.split()[0]}")
    print(f"baseline dir {BASE}")
    print(f"r99 dir {R99}")

    ent98 = load(BASE / "entities.json")
    ent99 = load(R99 / "entities.json")
    rel98 = load(BASE / "relations.json")
    rel99 = load(R99 / "relations.json")
    tl98 = load(BASE / "timeline.json")
    tl99 = load(R99 / "timeline.json")
    src98 = load(BASE / "sources.json")
    src99 = load(R99 / "sources.json")
    con98 = load(BASE / "contradictions.json")
    con99 = load(R99 / "contradictions.json")

    check("entities len==6", len(ent99) == 6, f"got {len(ent99)} r98={len(ent98)}")
    check(
        "entities parsed-equal (all 6, key-order sensitive)",
        ent99 == ent98,
        f"r98 ids={[e['id'] for e in ent98]} r99 ids={[e['id'] for e in ent99]}",
    )
    # per-row key order
    for i, (a, b) in enumerate(zip(ent98, ent99)):
        check(
            f"entities[{i}] keys equal and ordered",
            list(a.keys()) == list(b.keys()) and a == b,
            f"r98={list(a.keys())} r99={list(b.keys())} id98={a.get('id')} id99={b.get('id')}",
        )
        if "claims" in a and "claims" in b:
            for j, (ca, cb) in enumerate(zip(a["claims"], b["claims"])):
                check(
                    f"entities[{i}].claims[{j}] key-order",
                    list(ca.keys()) == list(cb.keys()) and ca == cb,
                    f"r98={list(ca.keys())} r99={list(cb.keys())}",
                )

    check("relations len==1", len(rel99) == 1, f"got {len(rel99)}")
    check(
        "relations parsed-equal (key-order sensitive)",
        rel99 == rel98,
        f"r99={json.dumps(rel99)}",
    )
    if rel98 and rel99:
        check(
            "relations[0] keys ordered",
            list(rel98[0].keys()) == list(rel99[0].keys()),
            f"r98={list(rel98[0].keys())} r99={list(rel99[0].keys())}",
        )

    check("timeline len==8", len(tl99) == 8, f"got {len(tl99)} r98={len(tl98)}")
    check(
        "timeline[:7] parsed-equal (key-order sensitive)",
        tl99[:7] == tl98,
        f"r98 len {len(tl98)}",
    )
    for i, (a, b) in enumerate(zip(tl98, tl99[:7])):
        check(
            f"timeline[{i}] keys equal and ordered id={a.get('id')}",
            list(a.keys()) == list(b.keys()) and a == b,
            f"r98={list(a.keys())} r99={list(b.keys())}",
        )
    if len(tl99) >= 8:
        new = tl99[7]
        check("timeline[7].id==clerk-lapse-recorded", new.get("id") == "clerk-lapse-recorded", str(new.get("id")))
        check("timeline[7].tick==15", new.get("tick") == 15, str(new.get("tick")))
        check("timeline[7].entity_id==clerk-maren", new.get("entity_id") == "clerk-maren", str(new.get("entity_id")))
        check("timeline[7].place_id==chalk-stair", new.get("place_id") == "chalk-stair", str(new.get("place_id")))
        check(
            "timeline[7].depends_on==[clerk-filing-open]",
            new.get("depends_on") == ["clerk-filing-open"],
            str(new.get("depends_on")),
        )
        check("timeline[7].source_id==clerk-lapse-note", new.get("source_id") == "clerk-lapse-note", str(new.get("source_id")))
        check(
            "timeline[7] key order",
            list(new.keys()) == ["id", "tick", "entity_id", "place_id", "depends_on", "description", "source_id"],
            str(list(new.keys())),
        )
        desc = new.get("description") or ""
        for needle in (
            "crossing-window named in the original minute has closed",
            "agreement was unfulfilled",
            "no claim was lodged",
            "historical open entry",
        ):
            check(f"timeline[7] description contains {needle!r}", needle in desc)
        # forbidden positive assertions in the new description
        lowered = desc.lower()
        for bad in ("resolved the matter", "blames", "reconciled the accounts"):
            check(f"timeline[7] description lacks {bad!r}", bad not in lowered)

    check("sources len==8", len(src99) == 8, f"got {len(src99)} r98={len(src98)}")
    check(
        "sources[:7] parsed-equal (key-order sensitive)",
        src99[:7] == src98,
        f"r98 len {len(src98)}",
    )
    for i, (a, b) in enumerate(zip(src98, src99[:7])):
        check(
            f"sources[{i}] keys equal and ordered id={a.get('id')}",
            list(a.keys()) == list(b.keys()) and a == b,
            f"r98={list(a.keys())} r99={list(b.keys())}",
        )
    if len(src99) >= 8:
        ns = src99[7]
        check("sources[7].id==clerk-lapse-note", ns.get("id") == "clerk-lapse-note", str(ns.get("id")))
        check(
            "sources[7].title",
            ns.get("title") == "Maren's Chalk Stair Lapse Note",
            str(ns.get("title")),
        )
        check(
            "sources[7].kind",
            ns.get("kind") == "fictional first-person note",
            str(ns.get("kind")),
        )
        check(
            "sources[7] key order",
            list(ns.keys()) == ["id", "title", "kind", "reliability_note"],
            str(list(ns.keys())),
        )

    check(
        "contradictions parsed-equal ([])",
        con99 == con98 == [],
        repr(con99),
    )
    check("contradictions is a list", isinstance(con99, list) and isinstance(con98, list))

    # only-new ids
    check(
        "no new entity id",
        [e["id"] for e in ent99] == [e["id"] for e in ent98],
        str([e["id"] for e in ent99]),
    )
    check(
        "only new source id is clerk-lapse-note",
        [s["id"] for s in src99] == [s["id"] for s in src98] + ["clerk-lapse-note"],
        str([s["id"] for s in src99]),
    )
    check(
        "only new timeline id is clerk-lapse-recorded",
        [e["id"] for e in tl99] == [e["id"] for e in tl98] + ["clerk-lapse-recorded"],
        str([e["id"] for e in tl99]),
    )

    # byte prefix of the three extended files vs extracted baseline
    print("--- byte prefix ---")
    for name in ("sources.json", "timeline.json", "fictional-excerpts.md"):
        b98 = (BASE / name).read_bytes()
        b99 = (R99 / name).read_bytes()
        # also confirm baseline extraction matches git show
        blob = git_blob(f"corpus/fixtures/r98-clerk-filing/{name}")
        check(f"{name} baseline-extract == git show 4265df5", b98 == blob, f"len {len(b98)}")
        if name.endswith(".json"):
            # inherited bytes: r98 ends with "\n]\n"; append inserts ",\n" before closing bracket
            # longest common prefix should be len(r98)-3 (start of trailing "\n]\n") OR
            # len(r98)-2 if they replaced "]\n" keeping the preceding newline differently.
            lcp = 0
            for x, y in zip(b98, b99):
                if x != y:
                    break
                lcp += 1
            else:
                lcp = min(len(b98), len(b99))
            tail98 = b98[lcp:]
            head99_div = b99[lcp:lcp + 8]
            prefix_exact = b99.startswith(b98[:lcp]) and lcp == len(b98) - 3 and b98.endswith(b"\n]\n")
            check(
                f"{name} LCP == len(r98)-3 and r98 tail is newline-bracket",
                prefix_exact,
                f"LCP={lcp} len98={len(b98)} len99={len(b99)} r98_tail={tail98!r} r99_div={head99_div!r} r99_tail={b99[-4:]!r}",
            )
            check(f"{name} r99 still ends with newline-bracket", b99.endswith(b"\n]\n"), repr(b99[-4:]))
            check(f"{name} divergence starts with comma-newline", b99[lcp:lcp + 2] == b",\n", repr(b99[lcp:lcp + 2]))
        else:
            check(
                f"{name} strict byte-prefix (r99 startswith r98)",
                b99.startswith(b98),
                f"len98={len(b98)} len99={len(b99)} appended={len(b99) - len(b98)}",
            )
            if b99.startswith(b98):
                appended = b99[len(b98):]
                check(
                    f"{name} appended region starts with newline then Round 99 heading",
                    appended.startswith(b"\n## Round 99 lapse note"),
                    repr(appended[:80]),
                )

    # cmp of the seven copied files vs git show AND vs worktree
    print("--- copied files cmp ---")
    copied = [
        "README.md",
        "claim-excerpt-map.md",
        "contradictions.json",
        "entities.json",
        "inspiration-note.md",
        "relations.json",
        "source-excerpt.md",
    ]
    for name in copied:
        b99 = (R99 / name).read_bytes()
        blob = git_blob(f"corpus/fixtures/r98-clerk-filing/{name}")
        wt = (R98_WT / name).read_bytes()
        base = (BASE / name).read_bytes()
        check(f"cmp {name} r99 == 4265df5 blob", b99 == blob, f"sha99={sha256(b99)} shablob={sha256(blob)}")
        check(f"cmp {name} r99 == worktree r98", b99 == wt)
        check(f"cmp {name} baseline-extract == blob", base == blob)

    # extended files must NOT be identical
    for name in ("sources.json", "timeline.json", "fictional-excerpts.md"):
        b99 = (R99 / name).read_bytes()
        blob = git_blob(f"corpus/fixtures/r98-clerk-filing/{name}")
        check(f"{name} is NOT byte-identical (extension expected)", b99 != blob, f"len99={len(b99)} len98={len(blob)}")

    # key-order sensitive negative: a reordered dict must not compare equal
    # (documents that OrderedDict equality is order-sensitive in this interpreter)
    a = OrderedDict([("id", "x"), ("kind", "y")])
    b = OrderedDict([("kind", "y"), ("id", "x")])
    check("harness: OrderedDict equality is key-order sensitive", a != b, f"{list(a)} vs {list(b)}")

    print(f"FAILS: {fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
