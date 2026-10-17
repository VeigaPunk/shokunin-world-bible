#!/usr/bin/env python3
"""V16 preservation-mutations: scratch replays on r95-crossing-aftermath copies.

Reads the live fixture read-only, builds mutants under this scratch dir only,
runs check_bible / support_check / map_obligations (delivered + git-baseline
fb118c4) and prints every command with its exit code. The live tree is never
modified; writes are confined to this scratch dir.
"""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd()
LIVE = ROOT / "corpus" / "fixtures" / "r95-crossing-aftermath"
SCRATCH = ROOT / ".ufo" / "waves" / "round-95" / "seats" / "V16-scratch"
NEW_TOOL = ROOT / "corpus" / "tools" / "map_obligations.py"
OLD_TOOL = SCRATCH / "map_obligations_OLD.py"
SUPPORT = ROOT / "corpus" / "tools" / "support_check.py"
BIBLE = ROOT / "corpus" / "fixtures" / "check_bible.py"
MAP_NAMES = ("claim-to-excerpt-map.md", "claim-excerpt-map.md")
LIVE_FILES = ("README.md", "claim-excerpt-map.md", "entities.json", "relations.json",
              "contradictions.json", "inspiration-note.md", "source-excerpt.md",
              "sources.json", "timeline.json", "fictional-excerpts.md")


def say(line=""):
    print(line, flush=True)


def sh(args, label=""):
    if label:
        say(f"\n### {label}")
    say("$ " + " ".join(str(a) for a in args))
    r = subprocess.run([str(a) for a in args], cwd=ROOT, capture_output=True, text=True)
    if r.stdout:
        say(r.stdout.rstrip())
    if r.stderr:
        say("[stderr] " + r.stderr.rstrip())
    say(f"[exit={r.returncode}]")
    return r


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(label):
    out = {}
    for name in LIVE_FILES:
        p = LIVE / name
        if p.exists():
            out[name] = sha(p)
    say(f"# {label}: live fixture SHA-256")
    for name, digest in sorted(out.items()):
        say(f"  {digest}  {name}")
    return out


def copy_mutant(name):
    dst = SCRATCH / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(LIVE, dst)
    return dst


def find_map(cluster):
    for name in MAP_NAMES:
        p = cluster / name
        if p.exists():
            return p
    raise SystemExit(f"no map in {cluster}")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", value.strip().strip("`").lower()).strip()


def map_rows(map_path):
    headers = None
    section = None
    rows = []
    for line in map_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            h = norm(line[3:])
            section = "json" if h.startswith("json facts") else ("editorial" if h.startswith("editorial rows") else None)
            continue
        if not line.lstrip().startswith("|"):
            continue
        cs = cells(line)
        low = [norm(c) for c in cs]
        if any("delivery mode" in c for c in low) and any("anchor" in c for c in low):
            headers = low
            continue
        if headers is None or len(cs) != len(headers):
            continue
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cs):
            continue
        row = {"kind": section, "line": line}
        for h, c in zip(headers, cs):
            if "anchor" in h:
                row["anchor"] = c.strip("`")
            elif "pointer" in h:
                m = re.search(r"`([^`]+)`", c)
                row["pointer"] = m.group(1) if m else c.strip("`")
            elif "excerpt" in h and ("path" in h or h == "excerpt"):
                row["path"] = c.strip("`")
            elif "span" in h or h in {"line", "lines"}:
                row["span"] = c.strip("`")
            elif h in {"id", "fact id", "fact"}:
                row["id"] = c.strip("`")
        rows.append(row)
    return rows


def restate_inventory(map_path):
    rows = map_rows(map_path)
    jsonc = sum(1 for r in rows if r.get("kind") == "json")
    edc = sum(1 for r in rows if r.get("kind") == "editorial")
    total = len(rows)
    anchors = len({(r.get("path", ""), r.get("anchor", "")) for r in rows})
    text = map_path.read_text(encoding="utf-8")
    new_line = (f"**Expected inventory:** {jsonc} JSON facts; {edc} editorial rows; "
                f"{total} total mapped rows; {anchors} distinct excerpt anchors.")
    text2, n = re.subn(r"\*\*Expected inventory:\*\*[^\n]*", lambda m: new_line, text, count=1)
    assert n == 1, "inventory line not found"
    map_path.write_text(text2, encoding="utf-8")
    say(f"# restated inventory -> {jsonc} JSON facts; {edc} editorial rows; {total} total; {anchors} anchors")
    return jsonc, edc, total, anchors


def row_line_index(map_path, needle):
    lines = map_path.read_text(encoding="utf-8").splitlines()
    hits = [i for i, l in enumerate(lines) if needle in l and l.lstrip().startswith("|")]
    assert len(hits) == 1, f"expected exactly one row for {needle!r}, got {len(hits)}"
    return lines, hits[0]


def remove_row(map_path, needle):
    lines, idx = row_line_index(map_path, needle)
    say(f"# removing map row containing {needle!r}: {lines[idx]}")
    del lines[idx]
    map_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    restate_inventory(map_path)


def break_span(map_path, pointer):
    lines, idx = row_line_index(map_path, pointer)
    line = lines[idx]
    row = next(r for r in map_rows(map_path) if r.get("pointer") == pointer)
    span = row["span"]
    m = re.fullmatch(r"(\d+)(?:-(\d+))?", span)
    assert m, f"unexpected span {span!r}"
    last = int(m.group(2) or m.group(1))
    wrong = last + 1
    excerpt = map_path.parent / row["path"]
    g = subprocess.run(["grep", "-nF", "--", row["anchor"], str(excerpt)], capture_output=True, text=True)
    assert g.returncode == 0, f"anchor not found: {row['anchor']!r}"
    hit = int(g.stdout.splitlines()[0].split(":", 1)[0])
    parts = line.split("|")
    idxs = [i for i, p in enumerate(parts) if p.strip() == span]
    assert len(idxs) == 1, f"span cell not unique: {idxs}"
    parts[idxs[0]] = f" {wrong} "
    lines[idx] = "|".join(parts)
    map_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    say(f"# broke span for {pointer}: {span} -> {wrong} (anchor hit at line {hit})")
    return span, wrong, hit


def mutate_source_id(cluster, event_id="aftermath-missing-evin"):
    path = cluster / "timeline.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    rec = next(r for r in data if r.get("id") == event_id)
    old = rec["source_id"]
    new = "crossing-minute" if old != "crossing-minute" else "paired-clock"
    text = path.read_text(encoding="utf-8")
    start = text.index(f'"{event_id}"')
    needle = f'"source_id": "{old}"'
    j = text.index(needle, start)
    text = text[:j] + f'"source_id": "{new}"' + text[j + len(needle):]
    path.write_text(text, encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))
    say(f"# timeline.json {event_id} source_id {old!r} -> {new!r}")
    return old, new


def mutate_schema_drift(cluster):
    path = cluster / "entities.json"
    text = path.read_text(encoding="utf-8")
    occ = [m.start() for m in re.finditer(r'"claims":', text)]
    assert len(occ) == 5, f"expected 5 claims keys, got {len(occ)}"
    i = occ[4]
    text = text[:i] + '"assertions":' + text[i + len('"claims":'):]
    path.write_text(text, encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))
    say("# entities.json: 5th \"claims\" key renamed to \"assertions\" (content preserved)")
    remove_row(find_map(cluster), "entities.json#/4/claims/0")


def main():
    say(f"# V16 scratch root: {SCRATCH}")
    before = snapshot("before")
    if not OLD_TOOL.exists():
        r = subprocess.run(["git", "show", "fb118c4:corpus/tools/map_obligations.py"],
                           cwd=ROOT, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        OLD_TOOL.write_text(r.stdout, encoding="utf-8")
        say(f"# extracted git-baseline tool -> {OLD_TOOL}")
    say(f"# delivered tool sha256 {sha(NEW_TOOL)}")
    say(f"# git-baseline tool sha256 {sha(OLD_TOOL)}")

    sh(["python3", BIBLE, LIVE], "baseline check_bible (live)")
    sh(["python3", SUPPORT, LIVE], "baseline support_check (live)")
    sh(["python3", NEW_TOOL, LIVE], "baseline map_obligations delivered (live)")
    sh(["python3", OLD_TOOL, LIVE], "baseline map_obligations git-baseline fb118c4 (live)")

    m = copy_mutant("mut-c-break-span")
    break_span(find_map(m), "timeline.json#/3")
    sh(["python3", SUPPORT, m], "mut-c-break-span support_check (expect FAIL)")
    sh(["python3", NEW_TOOL, m], "mut-c-break-span map_obligations")
    sh(["python3", BIBLE, m], "mut-c-break-span check_bible")

    m = copy_mutant("mut-b-drop-new-row")
    remove_row(find_map(m), "timeline.json#/3")
    sh(["python3", SUPPORT, m], "mut-b-drop-new-row support_check (expect PASS: blind spot)")
    sh(["python3", NEW_TOOL, m], "mut-b-drop-new-row map_obligations (expect FAIL missing_obligation)")
    sh(["python3", BIBLE, m], "mut-b-drop-new-row check_bible")

    m = copy_mutant("mut-b2-drop-inherited-row")
    remove_row(find_map(m), "entities.json#/0/claims/0")
    sh(["python3", SUPPORT, m], "mut-b2-drop-inherited-row support_check (expect PASS: blind spot)")
    sh(["python3", NEW_TOOL, m], "mut-b2-drop-inherited-row map_obligations (expect FAIL missing_obligation)")

    m = copy_mutant("mut-d-source-id")
    mutate_source_id(m)
    sh(["python3", NEW_TOOL, m], "mut-d-source-id map_obligations (expect FAIL source_id_mismatch)")
    sh(["python3", SUPPORT, m], "mut-d-source-id support_check")
    sh(["python3", BIBLE, m], "mut-d-source-id check_bible")

    m = copy_mutant("mut-e-schema-drift")
    mutate_schema_drift(m)
    sh(["python3", NEW_TOOL, m], "mut-e-schema-drift map_obligations delivered (expect FAIL schema_drift)")
    sh(["python3", OLD_TOOL, m], "mut-e-schema-drift map_obligations git-baseline (expect silent PASS)")
    sh(["python3", SUPPORT, m], "mut-e-schema-drift support_check")
    sh(["python3", BIBLE, m], "mut-e-schema-drift check_bible")

    after = snapshot("after")
    say(f"# live fixture byte-identical before==after: {before == after}")
    sh(["git", "status", "--short"], "git status after all runs")


if __name__ == "__main__":
    main()
