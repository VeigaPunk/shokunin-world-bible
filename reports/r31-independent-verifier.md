# Round 31 independent verifier

## Reproduction

Run from repository root (Python 3):

```sh
git show 4da4b949aa03e6595cf9a0d947fb2ba0c44f6fb0:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/check-bible-r31-baseline.py
python3 - <<'PY'
from pathlib import Path
import subprocess
root = Path(".shokunin/lore/corpus/fixtures")
current = str(root / "check_bible.py")
baseline = "/tmp/check-bible-r31-baseline.py"
old = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("r31-"))
def replay(script, fixture):
    p = subprocess.run(["python3", script, str(fixture)], capture_output=True)
    return p.returncode, p.stdout, p.stderr
assert len(old) == 81
assert all(replay(current, d) == replay(baseline, d) for d in old)
base = "4da4b949aa03e6595cf9a0d947fb2ba0c44f6fb0"
tracked = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", base, "--", str(root)]).splitlines()
json_paths = [p.decode() for p in tracked if p.endswith(b".json")]
assert len(json_paths) == 404
for path in json_paths:
    assert Path(path).read_bytes() == subprocess.check_output(["git", "show", f"{base}:{path}"])
for fixture in ("r31-source-unique", "r31-source-ambiguous"):
    a, b = replay(current, root / fixture), replay(baseline, root / fixture)
    assert a == b
    print(fixture, a)
PY
```

The 81 prior fixture directories reproduce exact `(exit, stdout bytes, stderr bytes)` under baseline and current checker: **81/81 equal**. All **404** prior fixture JSON paths are byte-identical to the baseline commit. The supplied code checks each assertion and prints both new pair tuples.

## Pair result

`r31-source-unique` exits **0**, stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`, stderr empty. `r31-source-ambiguous` exits **1**, stderr empty, and reports exactly these eight findings:

1. `sources[2].id`: duplicate `courier-log`.
2. `entities[0].first_appearance`: ambiguous `courier-log`.
3. `entities[0].claims[0].source_id`: ambiguous `courier-log`.
4. `entities[3].first_appearance`: ambiguous `courier-log`.
5. `entities[3].claims[0].source_id`: ambiguous `courier-log`.
6. `relations[0].source_id`: ambiguous `courier-log`.
7. `timeline[0].source_id`: ambiguous `courier-log`.
8. `timeline[1].source_id`: ambiguous `courier-log`.

The unique fixture matches `consistent/` byte-for-byte across five JSON tables. In the pair, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` are identical; only `sources.json` differs. Thus the duplicate-ID addition causes eight findings, not a relation-only diagnostic. The replay command above also checks both pair cases against the extracted baseline checker using exactly the same fixture argv.

Prior precedent: baseline/current replay of `r7-ally-reverse-ambiguous` is exit 1 with three findings, including `relations[1].source_id` ambiguous `harbor-compact`; it is an existing reverse `allied_with` relation ambiguity, not the controlled non-alliance `carries` case tested here.

This verifies checker behavior and controlled-input coverage only. Duplicate citation identity leaves the referenced source unresolved; it does not establish the relation as true or false, alter canon, or establish source authenticity or rights.
