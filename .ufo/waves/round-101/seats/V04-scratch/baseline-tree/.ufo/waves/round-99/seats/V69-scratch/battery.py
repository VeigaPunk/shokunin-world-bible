#!/usr/bin/env python3
"""V69 independent coverage battery. Writes only under V69-scratch. Never writes the delivered contract."""
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V69-scratch"
SEATS = LANE / ".ufo/waves/round-99/seats"
LOG = SCRATCH / "battery.txt"
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]
PINNED = [
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
]
MD = PINNED[5:]
BASELINE_COMMIT = "4265df5e86e4121bde4125b649b89bb1676676a5"

lines = []


def ts():
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")


def emit(text=""):
    lines.append(text)
    print(text, flush=True)


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def sha_file(path):
    return sha256_bytes(path.read_bytes())


def run(argv, cwd=LANE):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def content_digest(file_bytes):
    payload = json.dumps(
        {name: sha256_bytes(raw) for name, raw in file_bytes.items()},
        sort_keys=True,
        separators=(",", ":"),
    )
    return sha256_bytes(payload.encode("utf-8"))


def semantic_inventory(fixture):
    timeline = json.loads((fixture / "timeline.json").read_text(encoding="utf-8"))
    relations = json.loads((fixture / "relations.json").read_text(encoding="utf-8"))
    events = {}
    for record in timeline:
        deps = record.get("depends_on", [])
        events[record["id"]] = {
            "depends_on": sorted(set(deps)),
            "endpoint": {key: record.get(key) for key in ("tick", "entity_id", "place_id")},
        }
    triples = sorted([record["from"], record["to"], record["type"]] for record in relations)
    return events, triples


def mirror_root(name):
    root = SCRATCH / "after" / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(
        LANE / "corpus/tools/dependency-freeze-contract.json",
        root / "corpus/tools/dependency-freeze-contract.json",
    )
    return root


def copy_fixture(root, name):
    dest = root / "corpus/fixtures" / name
    shutil.copytree(LANE / "corpus/fixtures" / name, dest)
    return dest


def tool_of(root):
    return root / "corpus/tools/dependency_freeze.py"


def quote_run(label, code, stdout, stderr):
    emit(f"$ {label}")
    emit(stdout.rstrip() if stdout.strip() else "(empty stdout)")
    if stderr.strip():
        emit("STDERR: " + stderr.rstrip())
    emit(f"EXIT:{code}")
    emit("")


def stability():
    emit(f"=== stability watch {ts()} ===")
    prev = None
    stable = 0
    for i in range(1, 7):
        tool = sha_file(LANE / "corpus/tools/dependency_freeze.py")
        contract = sha_file(LANE / "corpus/tools/dependency-freeze-contract.json")
        s1 = any(SEATS.glob("S1-*.md"))
        v30 = any(SEATS.glob("V30-*.md"))
        emit(f"stab={i} ts={ts()} tool={tool[:16]} contract={contract[:16]} s1={s1} v30={v30}")
        if (tool, contract) == prev:
            stable += 1
            if stable >= 2:
                emit(f"STABLE after stab={i}")
                return tool, contract
        else:
            stable = 0
        prev = (tool, contract)
        if i < 6:
            time.sleep(20)
    emit("NOT-STABLE after 6 checks; measuring the then-current bytes anyway")
    return prev


def before_demo():
    emit("=== BEFORE (baseline tool+contract from 4265df5, mirror ROOT) ===")
    base = SCRATCH / "before/baseline-root"
    tool_hash = sha_file(base / "corpus/tools/dependency_freeze.py")
    contract_hash = sha_file(base / "corpus/tools/dependency-freeze-contract.json")
    emit(f"baseline tool {tool_hash}")
    emit(f"baseline contract {contract_hash}")
    clean = base / "corpus/fixtures/r98-clerk-filing"
    code, out, err = run([sys.executable, str(base / "corpus/tools/dependency_freeze.py"), str(clean)])
    quote_run("baseline clean r98", code, out, err)

    def tamper_tree(tag, mutate):
        root = SCRATCH / "before" / tag
        if root.exists():
            shutil.rmtree(root)
        shutil.copytree(base, root)
        fixture = root / "corpus/fixtures/r98-clerk-filing"
        mutate(fixture)
        code, out, err = run([sys.executable, str(root / "corpus/tools/dependency_freeze.py"), str(fixture)])
        quote_run(f"BEFORE {tag}", code, out, err)
        return code, out

    def drop_depends(fixture):
        path = fixture / "fictional-excerpts.md"
        raw = path.read_text(encoding="utf-8")
        new = raw.replace("depends on", "follows", 1)
        path.write_text(new, encoding="utf-8")
        emit(f"wording removal changed={raw != new} count={raw.count('depends on')}->{new.count('depends on')}")

    def append_readme(fixture):
        path = fixture / "README.md"
        path.write_bytes(path.read_bytes() + b"\n<!-- prose-half probe -->\n")

    def json_space(fixture):
        path = fixture / "timeline.json"
        raw = path.read_bytes()
        path.write_bytes(raw.replace(b'"tick": 14', b'"tick": 14 ', 1))

    tamper_tree("wording-removal", drop_depends)
    tamper_tree("readme-append", append_readme)
    tamper_tree("json-space", json_space)


def other_gates(fixture, label):
    commands = [
        [sys.executable, "corpus/fixtures/check_bible.py", str(fixture)],
        [sys.executable, "corpus/tools/map_obligations.py", str(fixture)],
        [sys.executable, "corpus/tools/support_check.py", str(fixture)],
    ]
    for argv in commands:
        code, out, err = run(argv)
        quote_run(f"{label} :: {' '.join(argv[1:])}", code, out, err)


def after_battery(tool_hash, contract_hash):
    emit(f"=== AFTER delivered revision {ts()} ===")
    emit(f"tool {tool_hash}")
    emit(f"contract {contract_hash}")
    contract = json.loads((LANE / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    emit(f"schema_version {contract.get('schema_version')} payload_top {contract.get('payload_schema_version')}")
    emit(f"pinned_files {contract.get('pinned_files')}")
    emit(f"npins {len(contract['pins'])} names {list(contract['pins'])}")
    emit(f"self_test cases {list(contract['self_test']['expected'])} n={len(contract['self_test']['expected'])}")
    baseline_contract = json.loads(
        (SCRATCH / "before/baseline-root/corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8")
    )

    emit("--- chain verify ---")
    for name in CHAIN:
        code, out, err = run(
            [sys.executable, "corpus/tools/dependency_freeze.py", f"corpus/fixtures/{name}"]
        )
        quote_run(f"verify {name}", code, out, err)

    emit("--- r99 unpinned ---")
    code, out, err = run(
        [sys.executable, "corpus/tools/dependency_freeze.py", "corpus/fixtures/r99-window-lapse"]
    )
    quote_run("verify r99-window-lapse", code, out, err)

    emit("--- independent recompute (no tool import) ---")
    for name, pin in contract["pins"].items():
        fixture = LANE / "corpus/fixtures" / name
        blobs = {fn: (fixture / fn).read_bytes() for fn in PINNED}
        file_hashes = {fn: sha256_bytes(raw) for fn, raw in blobs.items()}
        digest = content_digest(blobs)
        events, triples = semantic_inventory(fixture)
        base_pin = baseline_contract["pins"][name]
        file_ok = file_hashes == pin["files"]
        digest_ok = digest == pin["content_sha256"]
        events_ok = events == pin["events"]
        rel_ok = triples == pin["relations"]
        base_events_ok = events == base_pin["events"]
        base_rel_ok = triples == base_pin["relations"]
        extra = sorted(
            p.name for p in fixture.iterdir() if p.is_file() and p.name not in PINNED
        )
        emit(
            f"PIN {name}: files={file_ok} digest={digest_ok} events={events_ok} relations={rel_ok} "
            f"vs-baseline-events={base_events_ok} vs-baseline-relations={base_rel_ok} "
            f"payload={pin.get('payload_schema_version')} nfiles={len(pin.get('files', {}))} "
            f"rev={pin.get('revision')} digest={pin.get('content_sha256')} extra={extra}"
        )
        if not file_ok:
            for fn in PINNED:
                if file_hashes.get(fn) != pin["files"].get(fn):
                    emit(f"  FILE-DIFF {fn} disk={file_hashes.get(fn)} pin={pin['files'].get(fn)}")
        if not digest_ok:
            emit(f"  DIGEST-DIFF disk={digest} pin={pin.get('content_sha256')}")

    emit("--- self-test ---")
    before = sha_file(LANE / "corpus/tools/dependency-freeze-contract.json")
    code, out, err = run([sys.executable, "corpus/tools/dependency_freeze.py", "--self-test"])
    after = sha_file(LANE / "corpus/tools/dependency-freeze-contract.json")
    quote_run("self-test", code, out, err)
    emit(f"contract unchanged by self-test: {before == after}")
    leftovers = list(LANE.glob("dependency-freeze-self-test-*"))
    emit(f"self-test leftovers: {[p.name for p in leftovers]}")

    emit("--- scope guard (delivered tool, out-of-scope target; contract must not change) ---")
    outscope = SCRATCH / "outscope"
    outscope.mkdir(exist_ok=True)
    before = sha_file(LANE / "corpus/tools/dependency-freeze-contract.json")
    code, out, err = run(
        [sys.executable, "corpus/tools/dependency_freeze.py", "--freeze", str(outscope)]
    )
    after = sha_file(LANE / "corpus/tools/dependency-freeze-contract.json")
    quote_run("scope-refused outscope", code, out, err)
    emit(f"contract unchanged by refused freeze: {before == after}")

    emit("--- path mismatch (mirror) ---")
    root = mirror_root("path-mismatch")
    foreign = root / "foreign" / "r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", foreign)
    code, out, err = run([sys.executable, str(tool_of(root)), str(foreign)])
    quote_run("path-mismatch foreign r98", code, out, err)

    emit("--- guarded --freeze reproducibility (mirror; delivered contract never written) ---")
    root = mirror_root("freeze-repro")
    for name in CHAIN:
        copy_fixture(root, name)
    delivered = json.loads((LANE / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    for name in CHAIN:
        target = root / "corpus/fixtures" / name
        code, out, err = run([sys.executable, str(tool_of(root)), "--freeze", str(target)])
        quote_run(f"mirror --freeze {name}", code, out, err)
    frozen = json.loads((root / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    for name in CHAIN:
        got = frozen["pins"][name]
        want = delivered["pins"][name]
        emit(f"PIN-REPRODUCIBILITY {name}: {'EXACT-MATCH' if got == want else 'DIFF'}")
        if got != want:
            for key in sorted(set(got) | set(want)):
                if got.get(key) != want.get(key):
                    emit(f"  key {key} differs")

    emit("--- markdown tamper, one file at a time (mirror, pinned path) ---")
    for fn in MD:
        root = mirror_root(f"md-{fn}")
        fixture = copy_fixture(root, "r98-clerk-filing")
        path = fixture / fn
        path.write_bytes(path.read_bytes() + b"\n")
        code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
        quote_run(f"append newline to {fn}", code, out, err)

    emit("--- dependency-wording removal on pinned path ---")
    root = mirror_root("wording-removal")
    fixture = copy_fixture(root, "r98-clerk-filing")
    path = fixture / "fictional-excerpts.md"
    raw = path.read_text(encoding="utf-8")
    path.write_text(raw.replace("depends on", "follows", 1), encoding="utf-8")
    code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
    quote_run("wording removal fictional-excerpts.md", code, out, err)
    # same bytes, other gates (tools are unchanged vs baseline, so this is also the before)
    other_gates(fixture, "wording-removal other gates")

    emit("--- other gates on intact r98 (control) ---")
    other_gates(LANE / "corpus/fixtures/r98-clerk-filing", "intact r98")

    emit("--- semantic reduction still exit 1, and still first when markdown also changes ---")
    root = mirror_root("reduction")
    fixture = copy_fixture(root, "r98-clerk-filing")
    timeline = json.loads((fixture / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "clerk-filing-open":
            record["depends_on"] = []
    (fixture / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
    quote_run("drop clerk-filing-open edge", code, out, err)

    root = mirror_root("reduction-plus-md")
    fixture = copy_fixture(root, "r98-clerk-filing")
    timeline = json.loads((fixture / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record["id"] == "clerk-filing-open":
            record["depends_on"] = []
    (fixture / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    excerpt = fixture / "fictional-excerpts.md"
    excerpt.write_bytes(excerpt.read_bytes() + b"\n")
    code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
    quote_run("edge drop PLUS excerpt newline", code, out, err)

    emit("--- r88 extra file outside the ten ---")
    root = mirror_root("r88-extra")
    fixture = copy_fixture(root, "r88-m3-maya-cluster")
    extra = fixture / "symbolism-clause-map.md"
    extra.write_bytes(extra.read_bytes() + b"\n")
    code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
    quote_run("r88 symbolism-clause-map.md newline", code, out, err)

    emit("--- delete one pinned markdown (verify, not freeze) ---")
    root = mirror_root("md-delete")
    fixture = copy_fixture(root, "r98-clerk-filing")
    (fixture / "inspiration-note.md").unlink()
    code, out, err = run([sys.executable, str(tool_of(root)), str(fixture)])
    quote_run("delete inspiration-note.md", code, out, err)

    emit("--- end hashes ---")
    emit(f"tool {sha_file(LANE / 'corpus/tools/dependency_freeze.py')}")
    emit(f"contract {sha_file(LANE / 'corpus/tools/dependency-freeze-contract.json')}")
    emit(f"s1 report {list(SEATS.glob('S1-*.md'))}")
    emit(f"s2 report {list(SEATS.glob('S2-*.md'))}")
    emit(f"s5 report {list(SEATS.glob('S5-*.md'))}")
    emit(f"v30 report {list(SEATS.glob('V30-*.md'))}")
    emit(f"table exists {(LANE / 'corpus/knowledge/r99-gate-blind-spot-table.md').is_file()}")


def main():
    emit(f"V69 battery start {ts()}")
    tool_hash, contract_hash = stability()
    before_demo()
    after_battery(tool_hash, contract_hash)
    # bounded stall-escape for V30/S1, recorded, max 4 x 20s
    emit("=== post-battery stall-escape (max 4) ===")
    for i in range(1, 5):
        s1 = list(SEATS.glob("S1-*.md"))
        v30 = list(SEATS.glob("V30-*.md"))
        emit(f"escape={i} ts={ts()} s1={bool(s1)} v30={bool(v30)} tool={sha_file(LANE / 'corpus/tools/dependency_freeze.py')[:16]}")
        if s1 and v30:
            emit("ESCAPE-HIT")
            break
        if i < 4:
            time.sleep(20)
    else:
        emit("ESCAPE-EXPIRED")
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    emit(f"WROTE {LOG}")


if __name__ == "__main__":
    main()
