#!/usr/bin/env python3
"""V50 replay of quoted seat outputs. Scratch mirrors only; no live --freeze."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
OUT = ROOT / ".ufo/waves/round-99/seats/V50-scratch"
SCRATCH = OUT / "replay"
if SCRATCH.exists():
    shutil.rmtree(SCRATCH)
SCRATCH.mkdir(parents=True)
log = []


def emit(text=""):
    log.append(text)
    print(text)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def core(line):
    return line.split("; fixture bytes")[0].split("; pinned-file bytes")[0]


emit("WHEN " + subprocess.check_output(["date", "+%H:%M:%S"], text=True).strip())
emit(
    "S_REPORTS "
    + " ".join(sorted(p.name for p in (ROOT / ".ufo/waves/round-99/seats").glob("S*.md")))
)
for art in (
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
):
    emit("ART %s exists=%s" % (art, (ROOT / art).is_file()))

live_tool = ROOT / "corpus/tools/dependency_freeze.py"
live_contract = ROOT / "corpus/tools/dependency-freeze-contract.json"
old_tool = (
    ROOT
    / ".ufo/waves/round-99/seats/V94-scratch/mirror/corpus/tools/dependency_freeze.py"
)
emit("LIVE_TOOL %s bytes=%s" % (sha(live_tool), live_tool.stat().st_size))
emit("LIVE_CONTRACT %s bytes=%s" % (sha(live_contract), live_contract.stat().st_size))
emit("V94_TOOL %s bytes=%s" % (sha(old_tool), old_tool.stat().st_size))

CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]
EXPECTED = {
    "r88-m3-maya-cluster": "acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae",
    "r94-paired-crossing": "048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef",
    "r95-crossing-aftermath": "97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710",
    "r96-crossing-response": "43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c",
    "r97-crossing-acknowledgment": "a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54",
    "r98-clerk-filing": "5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0",
}

emit("")
emit("=== CHAIN live verify (V115 quote) ===")
contract_before = sha(live_contract)
chain_ok = True
for name in CHAIN:
    proc = subprocess.run(
        [sys.executable, "corpus/tools/dependency_freeze.py", "corpus/fixtures/%s" % name],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    emit("$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/%s" % name)
    emit(proc.stdout.rstrip())
    if proc.stderr.strip():
        emit("STDERR " + proc.stderr.rstrip())
    digest = ""
    for line in proc.stdout.splitlines():
        if line.startswith("DIGEST "):
            digest = line.split()[1]
    ok = proc.returncode == 0 and digest == EXPECTED[name] and "RESULT PASS" in proc.stdout
    chain_ok = chain_ok and ok
    emit("rc=%s MATCH_V115 %s" % (proc.returncode, ok))
emit("CHAIN_ALL_MATCH %s" % chain_ok)
emit("CONTRACT_UNCHANGED_BY_VERIFY %s" % (sha(live_contract) == contract_before))

emit("")
emit("=== r99 unpinned (V108 quote) ===")
proc = subprocess.run(
    [sys.executable, "corpus/tools/dependency_freeze.py", "corpus/fixtures/r99-window-lapse"],
    cwd=ROOT,
    capture_output=True,
    text=True,
)
emit(proc.stdout.rstrip())
emit("rc=%s" % proc.returncode)
if proc.stderr.strip():
    emit("STDERR " + proc.stderr.rstrip())
unpin_ok = (
    proc.returncode == 2
    and "UNPINNED-FIXTURE" in proc.stdout
    and "r99-window-lapse" in proc.stdout
)
emit("MATCH_V108_UNPINNED %s" % unpin_ok)


def make_mirror(tag, tool_bytes):
    base = SCRATCH / tag
    (base / "corpus/tools").mkdir(parents=True)
    (base / "corpus/fixtures").mkdir(parents=True)
    (base / "corpus/tools/dependency_freeze.py").write_bytes(tool_bytes)
    shutil.copy2(live_contract, base / "corpus/tools/dependency-freeze-contract.json")
    return base


def copy_fixture(base, name):
    dest = base / "corpus/fixtures" / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(ROOT / "corpus/fixtures" / name, dest)
    return dest


def run_verify(base, name):
    tool = base / "corpus/tools/dependency_freeze.py"
    fix = base / "corpus/fixtures" / name
    return subprocess.run(
        [sys.executable, str(tool), str(fix)], cwd=base, capture_output=True, text=True
    )


def prep_v94a(base):
    fix = copy_fixture(base, "r98-clerk-filing")
    (fix / "entities.json").write_bytes((fix / "entities.json").read_bytes() + b"\n")
    (fix / "fictional-excerpts.md").write_bytes(
        (fix / "fictional-excerpts.md").read_bytes() + b"\n<!-- v94-json-then-md -->\n"
    )
    return "r98-clerk-filing"


def prep_v108(base):
    fix = copy_fixture(base, "r98-clerk-filing")
    (fix / "fictional-excerpts.md").write_bytes(
        (fix / "fictional-excerpts.md").read_bytes() + b"\nV108-TAMPER fictional-excerpts\n"
    )
    return "r98-clerk-filing"


def prep_v94b(base):
    fix = copy_fixture(base, "r95-crossing-aftermath")
    (fix / "README.md").write_bytes(
        (fix / "README.md").read_bytes() + b"\n<!-- v94-pair-b -->\n"
    )
    (fix / "timeline.json").write_bytes((fix / "timeline.json").read_bytes() + b"\n")
    return "r95-crossing-aftermath"


def prep_v115(base):
    fix = copy_fixture(base, "r98-clerk-filing")
    (fix / "fictional-excerpts.md").write_bytes(
        (fix / "fictional-excerpts.md").read_bytes()
        + b"\nV115 scratch tamper: prose byte added.\n"
    )
    return "r98-clerk-filing"


quoted = {
    "v94a": (
        "FINDING DIGEST-MISMATCH: content digest 9d89ba3f8e19d34394575a782b8a69c38e7a4ee94b823c0cd8912bafe05416ad "
        "!= pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: entities.json "
        "(sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> "
        "457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3), fictional-excerpts.md "
        "(sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> "
        "c62880b9beab277b88dfa2321eef5fd4663b256b8189e9a1568d3cd824842c3c); "
        "fixture bytes changed outside the frozen inventory"
    ),
    "v108": (
        "FINDING DIGEST-MISMATCH: content digest ef0a7f1a39a306dc06eb74f2a8722865c3fee18371ccf9d6b4585d3bf28a13ea "
        "!= pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md "
        "(sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> "
        "9660d381e09b40c14f7eb3e67ee653bad06ec1a8d9e832c681188a83da457d1c); "
        "fixture bytes changed outside the frozen inventory"
    ),
    "v94b": (
        "FINDING DIGEST-MISMATCH: content digest 124b8f48687b94f6106731b52c66e1f579b20c6aa5a77fb9671085a3c012ac4c "
        "!= pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md "
        "(sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> "
        "168bbd76884e700dc0ec922b9db9c64293619061f3391d37247b3d34295ef098), timeline.json "
        "(sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> "
        "bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2); "
        "fixture bytes changed outside the frozen inventory"
    ),
    "v115": (
        "FINDING DIGEST-MISMATCH: content digest abac966391ca9fb5391b8c0e453a88de067d9473afddf971668950279c415b40 "
        "!= pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md "
        "(sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> "
        "0136a06af0d673703deae1d3de0b7acd7c02bcc8cb3c74ffb691e8da6da9e6ca); "
        "fixture bytes changed outside the frozen inventory"
    ),
}
preps = {
    "v94a": prep_v94a,
    "v108": prep_v108,
    "v94b": prep_v94b,
    "v115": prep_v115,
}
old_bytes = old_tool.read_bytes()
new_bytes = live_tool.read_bytes()

for label, prep in preps.items():
    for rev, blob in (("quoted-tool-6f81f8be", old_bytes), ("live-tool", new_bytes)):
        tag = "%s-%s" % (label, rev)
        base = make_mirror(tag, blob)
        name = prep(base)
        proc = run_verify(base, name)
        finding = next(
            (line for line in proc.stdout.splitlines() if line.startswith("FINDING ")), ""
        )
        emit("")
        emit("=== %s rc=%s ===" % (tag, proc.returncode))
        emit(proc.stdout.rstrip())
        if proc.stderr.strip():
            emit("STDERR " + proc.stderr.rstrip())
        emit("EXACT_MATCH %s" % (finding == quoted[label]))
        emit("CORE_MATCH %s" % (core(finding) == core(quoted[label])))

emit("")
emit("=== CENSUS (V29 quote) ===")
fixture_root = ROOT / "corpus/fixtures"
dirs = sorted(d for d in os.listdir(fixture_root) if (fixture_root / d).is_dir())
clean = negative = violation_lines = 0
odd = []
for name in dirs:
    rel = "corpus/fixtures/%s" % name
    proc = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    out = (proc.stdout + proc.stderr).strip()
    if proc.returncode == 0:
        clean += 1
    elif proc.returncode == 1:
        negative += 1
        violation_lines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else:
        odd.append([rel, proc.returncode])
census = {
    "dirs": len(dirs),
    "clean": clean,
    "negative": negative,
    "violation_lines": violation_lines,
    "odd": odd,
}
emit(json.dumps(census))
base_text = subprocess.check_output(
    ["git", "ls-tree", "-d", "--name-only", "4265df5", "corpus/fixtures"],
    cwd=ROOT,
    text=True,
)
base_dirs = [line for line in base_text.splitlines() if line.strip()]
emit("baseline_dirs %s" % len(base_dirs))
want = {"dirs": 173, "clean": 39, "negative": 134, "violation_lines": 421, "odd": []}
emit("MATCH_V29 %s" % (census == want))
emit(
    "r99_in_worktree %s r99_in_baseline %s"
    % ("r99-window-lapse" in dirs, "corpus/fixtures/r99-window-lapse" in base_dirs)
)

emit("")
emit("=== SUPPORT tail (V12/S4 quote) ===")
proc = subprocess.run(
    [sys.executable, "corpus/tools/support_check.py", "corpus/fixtures/r99-window-lapse"],
    cwd=ROOT,
    capture_output=True,
    text=True,
)
keep = [
    line
    for line in proc.stdout.splitlines()
    if line.startswith("INVENTORY")
    or line.startswith("PASS J21")
    or line.startswith("RECEIPT")
    or line.startswith("SOURCE-SUPPORT")
    or line.startswith("RESULT")
]
emit("\n".join(keep))
emit("rc=%s" % proc.returncode)
emit("MAP_SHA %s" % sha(ROOT / "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md"))
emit("README_SHA %s" % sha(ROOT / "corpus/fixtures/r99-window-lapse/README.md"))

emit("")
emit("=== LIVE TOOL AFTER ===")
emit("LIVE_TOOL_AFTER %s" % sha(live_tool))
emit("LIVE_CONTRACT_AFTER %s" % sha(live_contract))
(OUT / "rerun-final.txt").write_text("\n".join(log) + "\n")
print("WROTE", OUT / "rerun-final.txt")
