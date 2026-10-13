# Round 29 independent verifier

Independent non-author replay performed in the repository working tree. The historical checker was extracted from baseline `5ca92778c86b47bdc06c9cd971a82334c501359f` with `git show` into a temporary directory. The checked-in current checker was compared against it on every pre-r29 fixture directory.

Reproduce the full check with `python3 /tmp/r29verify.py` (the script uses only Python 3 standard library and `git`; its source is recorded below). Results:

- **79/79** old fixture directories: baseline and current checker matched exactly in stdout bytes, stderr bytes, and exit status.
- **394/394** old committed fixture JSON paths: working-tree bytes match baseline bytes.
- **5/5** r29 JSON tables (`entities.json`, `relations.json`, `sources.json`, `timeline.json`, `contradictions.json`): byte-identical to `r28-courier-excerpt`.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` and the corresponding `r29-near-miss` command both exit **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations\n`, stderr empty.

The checker reads JSON, not Markdown. It does **not** assess the positive prose, the near-miss prose, or either manual map. The paired prose supports the narrow human decision that “I, Mira, carried the blue seal” lexically supports `carries` conditional on editorial Mira/seal-to-ID alignment, whereas “The blue seal was near Mira” does not entail carrying. The negative map properly labels that claim unsupported by this excerpt, not contradicted or false. This verifies artifact identity and checker behavior, not source authenticity, canon, or broader relation truth.

## Reproducible command source

The verifier was run from repository root as `python3 /tmp/r29verify.py`. Equivalent source:

```python
import pathlib, subprocess, tempfile
root = pathlib.Path(".shokunin/lore/corpus/fixtures")
base = "5ca92778c86b47bdc06c9cd971a82334c501359f"
old = subprocess.check_output(["git", "show", f"{base}:.shokunin/lore/corpus/fixtures/check_bible.py"])
with tempfile.TemporaryDirectory() as td:
    baseline = pathlib.Path(td) / "check_bible.py"
    baseline.write_bytes(old)
    dirs = sorted(d for d in root.iterdir() if d.is_dir() and not d.name.startswith("r29-"))
    for d in dirs:
        a = subprocess.run(["python3", str(baseline), str(d)], capture_output=True)
        b = subprocess.run(["python3", str(root / "check_bible.py"), str(d)], capture_output=True)
        assert (a.stdout, a.stderr, a.returncode) == (b.stdout, b.stderr, b.returncode), d
    paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", base, "--", str(root)], text=True).splitlines()
    json_paths = [x for x in paths if x.endswith(".json") and "/r29-" not in x]
    assert all(pathlib.Path(x).read_bytes() == subprocess.check_output(["git", "show", f"{base}:{x}"]) for x in json_paths)
    names = ["entities.json", "relations.json", "sources.json", "timeline.json", "contradictions.json"]
    assert all((root / "r28-courier-excerpt" / n).read_bytes() == (root / "r29-near-miss" / n).read_bytes() for n in names)
    expected = b"CLEAN: schema, citations, relations, timeline; 0 violations\n"
    for d in ("r28-courier-excerpt", "r29-near-miss"):
        r = subprocess.run(["python3", str(root / "check_bible.py"), str(root / d)], capture_output=True)
        assert (r.returncode, r.stdout, r.stderr) == (0, expected, b"")
```
