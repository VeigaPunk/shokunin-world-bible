# Round 25 independent verifier

## Result

Independent replay passes. I used the declared report baseline `1919faea7a4790244e8dc2cdbb60b652ecfee3c0`, extracted its checker with `git show`, and compared it with the working-tree checker. All **73 pre-existing fixture directories** produced byte-identical stdout and stderr and identical exit codes (**73/73 exact; 0 differences**). All **364 baseline JSON paths** remain present and byte-identical (**364/364**). The two added fixtures account for 10 new JSON paths; no old path changed.

## Reproduction

Run at the repository root; this extracts the baseline checker to a temporary file and checks outputs per fixture:

```python
import pathlib, subprocess, tempfile
root = pathlib.Path(".shokunin/lore/corpus/fixtures")
commit = "1919faea7a4790244e8dc2cdbb60b652ecfee3c0"
old = pathlib.Path(tempfile.gettempdir()) / "check_bible_r25_independent.py"
old.write_bytes(subprocess.run(
    ["git", "show", f"{commit}:.shokunin/lore/corpus/fixtures/check_bible.py"],
    check=True, capture_output=True).stdout)
fixtures = sorted(p for p in root.iterdir()
                  if p.is_dir() and not p.name.startswith("r25-"))
assert len(fixtures) == 73
for fixture in fixtures:
    result = []
    for checker in (old, root / "check_bible.py"):
        p = subprocess.run(["python3", str(checker), str(fixture)], capture_output=True)
        result.append((p.stdout, p.stderr, p.returncode))
    assert result[0] == result[1], fixture.name
paths = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", commit,
     "--", ".shokunin/lore/corpus/fixtures"],
    check=True, capture_output=True, text=True).stdout.splitlines()
json_paths = [p for p in paths if p.endswith(".json")]
assert len(json_paths) == 364
for path in json_paths:
    before = subprocess.run(["git", "show", f"{commit}:{path}"],
                            check=True, capture_output=True).stdout
    assert pathlib.Path(path).read_bytes() == before, path
```

The checker commands for the focused cases are:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
```

Observed unique result: exit **0**, stdout `CLEAN: schema, citations, relations, timeline; 0 violations
`, empty stderr. Observed ambiguous result: exit **1**, empty stderr, stdout exactly:

```text
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
```

There is no `relations[0].from` ambiguity. In the two added fixtures, byte comparisons of `contradictions.json`, `relations.json`, `sources.json`, and `timeline.json` all match. `entities.json` is the sole differing table; the ambiguous fixture appends one structurally admitted duplicate `seal` row. The unique fixture retains the five tables from `consistent/` unchanged.

## Scope and caveats

This is a fixture/checker regression and diagnostic-position result, not evidence that the cited relation is true, that the duplicate rows identify distinct people, or that any canon should change. The empty claims on the added row and a resolvable `first_appearance` source establish neither textual entailment nor narrative truth. The 73-case filter deliberately excludes the two new `r25-*` directories; baseline path enumeration is rooted at the baseline commit. No production file was changed.
