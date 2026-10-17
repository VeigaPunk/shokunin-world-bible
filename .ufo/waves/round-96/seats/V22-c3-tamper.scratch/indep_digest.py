#!/usr/bin/env python3
"""V22 independent recomputation of the dependency_freeze content digest.

Two independent methods:
  A) same algorithm re-implemented from the tool's documented construction
     (per-file sha256 -> json.dumps sorted/compact -> sha256), and
  B) a shell-sha256sum-based reconstruction cross-check.

Prints per-file digests and the content digest for a fixture dir.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")


def method_a(fixture: Path):
    files = {}
    for name in DATA_FILES:
        p = fixture / name
        if p.is_file():
            files[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    payload = json.dumps(files, sort_keys=True, separators=(",", ":"))
    return files, hashlib.sha256(payload.encode("utf-8")).hexdigest(), payload


def method_b(fixture: Path):
    files = {}
    for name in DATA_FILES:
        p = fixture / name
        if p.is_file():
            out = subprocess.run(["sha256sum", str(p)], capture_output=True, text=True, check=True).stdout
            files[name] = out.split()[0]
    payload = "{" + ",".join(
        f'"{k}":"{files[k]}"' for k in sorted(files)
    ) + "}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest(), payload


if __name__ == "__main__":
    fixture = Path(sys.argv[1])
    files_a, digest_a, payload_a = method_a(fixture)
    digest_b, payload_b = method_b(fixture)
    print(f"fixture={fixture.resolve().name}")
    for name in sorted(files_a):
        print(f"  file {name} sha256={files_a[name]}")
    print(f"payload={payload_a}")
    print(f"content_sha256_A={digest_a}")
    print(f"content_sha256_B={digest_b}")
    print(f"methods_agree={digest_a == digest_b}")
