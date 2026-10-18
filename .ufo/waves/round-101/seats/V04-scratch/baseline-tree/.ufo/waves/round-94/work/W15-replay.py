#!/usr/bin/env python3
import hashlib
import json
import shutil
import shlex
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve()
WORK = SCRIPT.parent
ROOT = SCRIPT.parents[4]
SOURCE = ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"
COPY = WORK / "W15-fixture"
MARKER = COPY / ".w15-owned"
TRANSCRIPT = WORK / "W15-replay.txt"
MARKER_TEXT = "W15-owned isolated replay fixture\n"
CLAIM = {
    "statement": "Teva says the North Window was sealed before the check.",
    "source_id": "m2-record-archive",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_counts(cluster):
    entities = json.loads((cluster / "entities.json").read_text(encoding="utf-8"))
    relations = json.loads((cluster / "relations.json").read_text(encoding="utf-8"))
    timeline = json.loads((cluster / "timeline.json").read_text(encoding="utf-8"))
    first_appearances = sum("first_appearance" in entity for entity in entities)
    claims = [claim for entity in entities for claim in entity.get("claims", [])]
    assert all(claim.get("source_id") for claim in claims)
    sourced_relations = [record for record in relations if record.get("source_id")]
    sourced_events = [record for record in timeline if record.get("source_id")]
    assert len(sourced_relations) == len(relations)
    assert len(sourced_events) == len(timeline)
    return {
        "first_appearances": first_appearances,
        "entity_claims": len(claims),
        "relations": len(sourced_relations),
        "timeline_events": len(sourced_events),
    }


def render_counts(label, counts):
    total = sum(counts.values())
    return (
        f"{label} raw source-attributed obligations: "
        f"{counts['first_appearances']} first_appearance + "
        f"{counts['entity_claims']} entity claims + "
        f"{counts['relations']} relations + "
        f"{counts['timeline_events']} timeline events = {total}"
    )


def run_command(command, expected=None):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    lines = [f"$ {shlex.join(command)}", f"exit={result.returncode}"]
    if result.stdout:
        lines.extend(["stdout:", result.stdout.rstrip("\n")])
    if result.stderr:
        lines.extend(["stderr:", result.stderr.rstrip("\n")])
    if expected is not None:
        lines.append(f"expected_exit={expected}; observed={'MATCH' if result.returncode == expected else 'MISMATCH'}")
    return lines, result.returncode


def main():
    if not SOURCE.is_dir():
        raise SystemExit(f"source fixture missing: {SOURCE}")
    if COPY.exists():
        if not MARKER.is_file() or MARKER.read_text(encoding="utf-8") != MARKER_TEXT:
            raise SystemExit(f"refusing to replace unmarked W15 path: {COPY}")
        shutil.rmtree(COPY)
    shutil.copytree(SOURCE, COPY)
    MARKER.write_text(MARKER_TEXT, encoding="utf-8")

    before_counts = raw_counts(SOURCE)
    copied_counts = raw_counts(COPY)
    assert before_counts == copied_counts
    entities_path = COPY / "entities.json"
    entities = json.loads(entities_path.read_text(encoding="utf-8"))
    entities[0]["claims"].append(CLAIM)
    entities_path.write_text(json.dumps(entities, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    after_counts = raw_counts(COPY)
    assert after_counts["entity_claims"] == before_counts["entity_claims"] + 1
    assert sum(after_counts.values()) == sum(before_counts.values()) + 1

    original_files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    unchanged = []
    unexpected_changes = []
    for source_file in original_files:
        relative = source_file.relative_to(SOURCE)
        copy_file = COPY / relative
        if relative != Path("entities.json") and sha256(source_file) == sha256(copy_file):
            unchanged.append(str(relative))
        elif relative != Path("entities.json"):
            unexpected_changes.append(str(relative))
    map_path = COPY / "claim-excerpt-map.md"
    excerpt_paths = sorted(COPY.glob("*excerpt.md"))
    excerpts_unchanged = all(sha256(SOURCE / path.name) == sha256(path) for path in excerpt_paths)
    map_unchanged = sha256(SOURCE / map_path.name) == sha256(map_path)
    claim_pointer = "entities.json#/0/claims/1"
    map_has_pointer = claim_pointer in map_path.read_text(encoding="utf-8")
    claim_text_in_excerpts = any(
        CLAIM["statement"] in path.read_text(encoding="utf-8") for path in excerpt_paths
    )

    transcript = [
        "W15 isolated replay: lexical support-check blind spot",
        f"source_fixture={SOURCE.relative_to(ROOT)}",
        f"isolated_copy={COPY.relative_to(ROOT)}",
        render_counts("baseline", before_counts),
        render_counts("mutated copy", after_counts),
        f"new_raw_pointer={claim_pointer}",
        f"new_claim_source_id={CLAIM['source_id']}",
        f"new_pointer_in_map={'yes' if map_has_pointer else 'no'}",
        f"new_claim_text_in_excerpts={'yes' if claim_text_in_excerpts else 'no'}",
        f"map_byte_identical_to_source={'yes' if map_unchanged else 'no'}",
        f"excerpt_files_byte_identical_to_source={sum(1 for path in excerpt_paths if sha256(SOURCE / path.name) == sha256(path))}/{len(excerpt_paths)}",
        f"other_original_files_byte_identical_to_source={len(unchanged)}/{len(original_files) - 1}",
        "expected_modified_original_file=entities.json (appended one claim)",
        f"unexpected_original_file_changes={','.join(unexpected_changes) if unexpected_changes else '(none)'}",
        "",
    ]

    baseline_command = [
        "python3", "corpus/tools/support_check.py", "corpus/fixtures/r93-m2-kojiki-cluster"
    ]
    copy_command = [
        "python3", "corpus/tools/support_check.py", str(COPY.relative_to(ROOT))
    ]
    support_exit_codes = []
    for command in (baseline_command, copy_command):
        lines, exit_code = run_command(command, expected=0)
        support_exit_codes.append(exit_code)
        transcript.extend(lines)
        transcript.append("")

    obligations_tool = ROOT / "corpus/tools/map_obligations.py"
    optional_obligations_exit = None
    if obligations_tool.is_file():
        command = ["python3", "corpus/tools/map_obligations.py", str(COPY.relative_to(ROOT))]
        lines, optional_obligations_exit = run_command(command, expected=1)
        transcript.extend(lines)
        transcript.append("")
    else:
        transcript.append("optional_map_obligations=NOT PRESENT at replay time; no command run")

    transcript_text = "\n".join(transcript).rstrip() + "\n"
    TRANSCRIPT.write_text(transcript_text, encoding="utf-8")
    print(transcript_text, end="")

    expected_shape = {"first_appearances": 4, "entity_claims": 4, "relations": 2, "timeline_events": 2}
    after_shape = {"first_appearances": 4, "entity_claims": 5, "relations": 2, "timeline_events": 2}
    if (
        before_counts != expected_shape
        or after_counts != after_shape
        or not excerpts_unchanged
        or not map_unchanged
        or map_has_pointer
        or claim_text_in_excerpts
        or unexpected_changes
        or support_exit_codes != [0, 0]
        or (optional_obligations_exit is not None and optional_obligations_exit != 1)
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
