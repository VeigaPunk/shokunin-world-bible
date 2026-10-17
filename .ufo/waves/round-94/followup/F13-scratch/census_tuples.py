#!/usr/bin/env python3
"""F13 behavioral preservation census: (exit, stdout, stderr) tuple per fixture dir.

Own script (F13 seat). Extracts the 9c2eea3 tree of corpus/fixtures/ into
F13-scratch/baseline/ via `git archive`, then runs the baseline checker over
every baseline fixture dir and the delivered checker over every delivered
fixture dir, and compares tuples for the inherited directories.
"""
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = "9c2eea3"
PREFIX = "corpus/fixtures/"
SCRATCH = Path(__file__).resolve().parent
BASE_TREE = SCRATCH / "baseline" / PREFIX
OUT = SCRATCH / "census-tuples.json"

if not (BASE_TREE / "check_bible.py").exists():
    BASE_TREE.mkdir(parents=True, exist_ok=True)
    archive = subprocess.run(
        ["git", "archive", BASE, "--", PREFIX], cwd=REPO, capture_output=True, check=True
    ).stdout
    subprocess.run(["tar", "-x", "-C", str(SCRATCH / "baseline")], input=archive, check=True)


def dirs_under(root: Path):
    return sorted(d.name for d in root.iterdir() if d.is_dir())


DELIV_TREE = REPO / PREFIX


def normalize(text: str) -> str:
    """Blank the harness-specific fixture root so tuples compare on content only.

    The checker echoes the absolute path it was given in cannot-load messages,
    so baseline-tree and delivered-tree runs differ by prefix alone unless the
    root is normalized. This is a harness artifact, not a behavioral change;
    both roots map to the same placeholder.
    """
    return text.replace(str(BASE_TREE), "<FIXTURE_ROOT>").replace(str(DELIV_TREE), "<FIXTURE_ROOT>")


def run(checker: Path, target: Path):
    proc = subprocess.run(
        [sys.executable, str(checker), str(target)],
        cwd=str(REPO), capture_output=True,
    )
    return {
        "exit": proc.returncode,
        "stdout": normalize(proc.stdout.decode("utf-8", "replace")),
        "stderr": normalize(proc.stderr.decode("utf-8", "replace")),
    }


base_checker = BASE_TREE / "check_bible.py"
delivered_checker = REPO / PREFIX / "check_bible.py"

base_dirs = dirs_under(BASE_TREE)
deliv_dirs = dirs_under(REPO / PREFIX)


def digest(entry):
    import re
    m = re.search(r"^(\d+) violation\(s\); no canon changed$", entry["stdout"], re.M)
    return {
        "exit": entry["exit"],
        "stdout_sha256": hashlib.sha256(entry["stdout"].encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256(entry["stderr"].encode()).hexdigest(),
        "stdout_lines": len(entry["stdout"].splitlines()),
        "violations": int(m.group(1)) if m else (0 if entry["stdout"].startswith("CLEAN:") else None),
    }


jobs = []
with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
    for name in base_dirs:
        jobs.append(("base", name, pool.submit(run, base_checker, BASE_TREE / name)))
    for name in deliv_dirs:
        jobs.append(("deliv", name, pool.submit(run, delivered_checker, REPO / PREFIX / name)))
        jobs.append(("base_on_deliv", name, pool.submit(run, base_checker, REPO / PREFIX / name)))
    results = {}
    for side, name, fut in jobs:
        results.setdefault(name, {})[side] = fut.result()

inherited = sorted(set(base_dirs) & set(deliv_dirs))
added_dirs = sorted(set(deliv_dirs) - set(base_dirs))
removed_dirs = sorted(set(base_dirs) - set(deliv_dirs))

changed = []
for name in inherited:
    b, d = digest(results[name]["base"]), digest(results[name]["deliv"])
    if b != d:
        changed.append({"dir": name, "baseline": b, "delivered": d,
                        "baseline_stdout": results[name]["base"]["stdout"],
                        "delivered_stdout": results[name]["deliv"]["stdout"],
                        "baseline_stderr": results[name]["base"]["stderr"],
                        "delivered_stderr": results[name]["deliv"]["stderr"]})

# control: same delivered directory, both checker blobs. Isolates any checker
# behavior change from any fixture-content or path-rendering change.
control_changed = []
for name in deliv_dirs:
    a, d = digest(results[name]["base_on_deliv"]), digest(results[name]["deliv"])
    if a != d:
        control_changed.append({"dir": name, "baseline_checker": a, "delivered_checker": d,
                                "baseline_stdout": results[name]["base_on_deliv"]["stdout"],
                                "delivered_stdout": results[name]["deliv"]["stdout"]})

added_runs = {name: digest(results[name]["deliv"]) for name in added_dirs}

result = {
    "baseline_dirs": len(base_dirs),
    "delivered_dirs": len(deliv_dirs),
    "inherited": len(inherited),
    "changed_tuple_count": len(changed),
    "changed": changed,
    "control_same_dir_checker_changed_count": len(control_changed),
    "control_same_dir_checker_changed": control_changed,
    "added_dirs": added_dirs,
    "added_dir_runs": added_runs,
    "removed_dirs": removed_dirs,
    "per_dir": {name: {"baseline": digest(results[name]["base"]) if "base" in results[name] else None,
                       "delivered": digest(results[name]["deliv"]) if "deliv" in results[name] else None}
                for name in sorted(results)},
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

print(f"baseline dirs: {len(base_dirs)}  delivered dirs: {len(deliv_dirs)}  inherited: {len(inherited)}")
print(f"changed tuples among inherited: {len(changed)}")
for c in changed:
    print(f"  CHANGED {c['dir']}: base={c['baseline']} deliv={c['delivered']}")
print(f"control (same dir, both checker blobs) changed: {len(control_changed)}")
for c in control_changed:
    print(f"  CONTROL CHANGED {c['dir']}")
print(f"added dirs: {added_dirs}")
for name, run_digest in added_runs.items():
    print(f"  {name}: exit={run_digest['exit']} stdout_lines={run_digest['stdout_lines']}")
print(f"removed dirs: {removed_dirs}")
print(f"wrote {OUT}")
