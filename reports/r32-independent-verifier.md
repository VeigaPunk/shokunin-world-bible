# Round 32 independent verifier

## Reproduction

Run from repository root (Python 3). The baseline checker is extracted from the requested commit; the baseline fixture inventory and JSON byte comparisons are taken from that same committed tree.

```sh
git show cfaf03a885f36fb6398b5c9dc0810a39cb573807:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/check-bible-r32-baseline.py
python3 - <<'PY'
from pathlib import Path
import subprocess
base = "cfaf03a885f36fb6398b5c9dc0810a39cb573807"
root = Path(".shokunin/lore/corpus/fixtures")
def replay(script, fixture):
    p = subprocess.run(["python3", script, str(fixture)], capture_output=True)
    return p.returncode, p.stdout, p.stderr
old = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("r32-"))
assert len(old) == 83
assert all(replay(str(root / "check_bible.py"), d) == replay("/tmp/check-bible-r32-baseline.py", d) for d in old)
tracked = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", base, "--", str(root)]).decode().splitlines()
json_paths = [p for p in tracked if p.endswith(".json")]
assert len(json_paths) == 414
assert all(Path(p).read_bytes() == subprocess.check_output(["git", "show", f"{base}:{p}"]) for p in json_paths)
for name in ("r32-source-malformed", "r31-source-ambiguous", "r31-source-unique"):
    print(name, replay(str(root / "check_bible.py"), root / name))
PY
```

Result: **83/83** pre-existing fixture directories match baseline/current exactly in `(exit status, stdout bytes, stderr bytes)` under identical fixture argv. All **414/414** JSON paths tracked at the baseline commit are byte-identical in the current worktree.

## r32 controlled mutation and outcomes

Compared `r32-source-malformed/` with `r31-source-ambiguous/`: only `sources.json` differs; only `sources[2].title` changes from `"Courier Log Registry Duplicate Index"` to `""`. The other four JSON files are byte-identical, and the raw second `courier-log` ID remains.

- `r32-source-malformed`: exit **1**, stderr empty; sole finding `VIOLATION: sources[2].title: required nonempty str` (summary: `1 violation(s); no canon changed`). No duplicate admitted source-ID or ambiguous-reference findings.
- `r31-source-ambiguous`: exit **1**, stderr empty; exactly eight findings: duplicate ID plus seven ambiguous references.
- `r31-source-unique`: exit **0**, stderr empty; `CLEAN: schema, citations, relations, timeline; 0 violations`.

This confirms the checker’s required-field screening and admitted-source ID count for these inputs only. It does not establish source falsity or uniqueness in-world, source authenticity, rights clearance, or canon; no raw source row or lore assertion was changed by the replay.
