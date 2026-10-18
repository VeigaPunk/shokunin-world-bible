#!/usr/bin/env python3
"""V33 scratch: build mutated fixture copies for dependency_freeze replays.

Usage: python3 mutate.py <scenario> <src_fixture_dir> <dst_fixture_dir>
Scenarios: reduce, add, endpoint-from, endpoint-to, malformed-timeline,
           missing-timeline, missing-relations, empty-timeline
"""
import json
import os
import shutil
import sys


def load(p):
    with open(p) as f:
        return json.load(f)


def dump(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=2)


def main():
    scenario, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.exists(dst):
        shutil.rmtree(dst)
    if scenario in ("missing-timeline", "missing-relations"):
        shutil.copytree(src, dst)
        drop = "timeline.json" if scenario == "missing-timeline" else "relations.json"
        os.remove(os.path.join(dst, drop))
        print("removed", drop)
        return
    if scenario == "malformed-timeline":
        shutil.copytree(src, dst)
        with open(os.path.join(dst, "timeline.json"), "w") as f:
            f.write("{ this is not json ,,, ")
        print("wrote malformed timeline.json")
        return
    shutil.copytree(src, dst)
    tl_path = os.path.join(dst, "timeline.json")
    rel_path = os.path.join(dst, "relations.json")
    if scenario == "reduce":
        tl = load(tl_path)
        for e in tl:
            if e["depends_on"]:
                before = list(e["depends_on"])
                e["depends_on"] = e["depends_on"][:-1]
                print("REDUCED", e["id"], before, "->", e["depends_on"])
                break
        else:
            print("NO DEPENDENT EVENT FOUND")
        dump(tl_path, tl)
    elif scenario == "add":
        tl = load(tl_path)
        ids = {e["id"] for e in tl}
        for e in tl:
            if e["depends_on"]:
                cand = "aru-ninth-bell" if "aru-ninth-bell" not in e["depends_on"] else "evin-ninth-bell"
                if cand in ids and cand not in e["depends_on"]:
                    e["depends_on"] = sorted(e["depends_on"] + [cand])
                    print("ADDED", cand, "to", e["id"], "->", e["depends_on"])
                    break
        else:
            print("NO TARGET EVENT FOUND")
        dump(tl_path, tl)
    elif scenario in ("endpoint-from", "endpoint-to"):
        rel = load(rel_path)
        if not rel:
            print("NO RELATIONS TO MUTATE")
        else:
            key = "from" if scenario == "endpoint-from" else "to"
            before = rel[0][key]
            rel[0][key] = "unknown-endpoint-x"
            print("ENDPOINT", key, before, "->", rel[0][key])
        dump(rel_path, rel)
    elif scenario == "empty-timeline":
        dump(tl_path, [])
        print("timeline emptied")
    else:
        sys.exit("unknown scenario " + scenario)


if __name__ == "__main__":
    main()
