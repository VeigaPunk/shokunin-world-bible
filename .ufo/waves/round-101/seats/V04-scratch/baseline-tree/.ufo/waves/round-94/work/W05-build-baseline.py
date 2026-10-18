import hashlib
import subprocess
from pathlib import Path

COMMIT = "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b"
MANIFEST = Path(".ufo/waves/round-94/work/W05-baseline-corpus.sha256")
REQUIRED_TOOLS = (
    "corpus/tools/support_check.py",
    "corpus/tools/discriminate_check.py",
    "corpus/tools/boundary_doc_check.py",
    "corpus/tools/boundary-doc-contract.json",
)

raw = subprocess.check_output(["git", "ls-tree", "-r", "-z", COMMIT, "--", "corpus/fixtures", "corpus/tools"])
entries = {}
for record in raw.split(b"\0"):
    if not record:
        continue
    meta, raw_path = record.split(b"\t", 1)
    _, kind, oid = meta.split(b" ", 2)
    if kind == b"blob":
        entries[raw_path.decode("utf-8")] = oid.decode("ascii")

fixtures = sorted(path for path in entries if path.startswith("corpus/fixtures/"))
check_bible = "corpus/tools/check_bible.py" if "corpus/tools/check_bible.py" in entries else "corpus/fixtures/check_bible.py"
paths = sorted(set(fixtures + list(REQUIRED_TOOLS) + [check_bible]))
missing = [path for path in paths if path not in entries]
if missing:
    raise SystemExit("baseline missing paths: " + ", ".join(missing))

def blob_bytes(object_ids):
    data = subprocess.check_output(
        ["git", "cat-file", "--batch"],
        input=b"".join(oid.encode("ascii") + b"\n" for oid in object_ids),
    )
    offset = 0
    for expected_oid in object_ids:
        end = data.find(b"\n", offset)
        header = data[offset:end].split()
        if len(header) != 3 or header[0].decode("ascii") != expected_oid or header[1] != b"blob":
            raise SystemExit("unexpected Git object response")
        size = int(header[2])
        offset = end + 1
        content = data[offset:offset + size]
        if len(content) != size or data[offset + size:offset + size + 1] != b"\n":
            raise SystemExit("truncated Git object response")
        offset += size + 1
        yield content

hashes = {path: hashlib.sha256(data).hexdigest() for path, data in zip(paths, blob_bytes([entries[path] for path in paths]))}
MANIFEST.parent.mkdir(parents=True, exist_ok=True)
MANIFEST.write_text("".join(f"{hashes[path]}  {path}\n" for path in paths), encoding="utf-8", newline="\n")

rows = MANIFEST.read_text(encoding="utf-8").splitlines()
if len(rows) != len(paths):
    raise SystemExit("manifest row count mismatch")
for line, path in zip(rows, paths):
    expected, listed_path = line.split("  ", 1)
    actual = hashlib.sha256(subprocess.check_output(["git", "cat-file", "blob", f"{COMMIT}:{path}"])).hexdigest()
    if listed_path != path or expected != actual:
        raise SystemExit(f"verification mismatch: {path}")

fixture_directories = {path.rsplit("/", 1)[0] for path in fixtures if path.rsplit("/", 1)[0] != "corpus/fixtures"}
print(f"baseline_commit={COMMIT}")
print(f"fixture_files={len(fixtures)}")
print(f"fixture_directories={len(fixture_directories)}")
print(f"additional_tool_files={len(REQUIRED_TOOLS)}")
print(f"manifest_entries={len(paths)} verified")
print(f"check_bible_path={check_bible}")
print(f"check_bible_sha256={hashes[check_bible]}")
print(f"boundary_gate_sha256={hashes['corpus/tools/boundary_doc_check.py']}")
print(f"manifest_sha256={hashlib.sha256(MANIFEST.read_bytes()).hexdigest()}")
