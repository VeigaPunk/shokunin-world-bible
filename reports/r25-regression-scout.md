# Round 25 regression scout: exact replay and JSON identity

## Scope and baseline

The round-25 declaration is `.shokunin/lore/LOG.md:366-369`. It names baseline work commit `cc2b73a2227326746aa80d05cd5cc7e5676d7855` and report commit `1919faea7a4790244e8dc2cdbb60b652ecfee3c0`. The requested regression population is the 73 fixture directories and 364 JSON paths established by round-24 independent replay (`.shokunin/lore/reports/r24-independent-verifier.md`, “Fixture JSON identity”; closure `.shokunin/lore/LOG.md:362-364`).

Baseline checker behavior: `index()` retains the last row by ID while reporting duplicates (`.shokunin/lore/corpus/fixtures/check_bible.py:45-51`); the relation loop visits both `from` and `to`, reports dangling IDs, and emits ambiguity when the admitted entity-ID count exceeds one (`.shokunin/lore/corpus/fixtures/check_bible.py:118-129`). Round 24 explicitly says the `to` branch lacked an independent duplicate-`to` fixture (`.shokunin/lore/LOG.md:364`). These facts motivate an endpoint-position probe, but do not themselves constitute evidence of new behavior.

## Exact 73-case replay

From repository root, extract the declared baseline checker and run it and the working-tree checker once on each fixture directory. Capture stdout bytes, stderr bytes, and return code separately; compare the fixture JSON path set and file bytes independently. This Python replay is reproducible and avoids shell-loop status/output ambiguity:

```python
import pathlib, subprocess, tempfile
root = pathlib.Path(".shokunin/lore/corpus/fixtures")
old = pathlib.Path(tempfile.gettempdir()) / "check_bible_r25_baseline.py"
old.write_bytes(subprocess.run(
    ["git", "show", "cc2b73a2227326746aa80d05cd5cc7e5676d7855:.shokunin/lore/corpus/fixtures/check_bible.py"],
    check=True, stdout=subprocess.PIPE).stdout)
fixtures = sorted(p for p in root.iterdir() if p.is_dir())
assert len(fixtures) == 73
for fixture in fixtures:
    results = []
    for checker in (old, root / "check_bible.py"):
        proc = subprocess.run(["python3", str(checker), str(fixture)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        results.append((proc.stdout, proc.stderr, proc.returncode))
    # Inspect/report every differing tuple; do not treat matching violation
    # totals alone as equality or suppress unexpected differences.
    if results[0] != results[1]:
        print(fixture.name, results[0], results[1])
old_paths = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", "cc2b73a2227326746aa80d05cd5cc7e5676d7855",
     "--", ".shokunin/lore/corpus/fixtures"], check=True,
    stdout=subprocess.PIPE, text=True).stdout.splitlines()
old_json = {p for p in old_paths if p.endswith(".json")}
new_json = {p.as_posix() for p in root.rglob("*.json")}
assert len(old_json) == 364
assert old_json == new_json
for relative in sorted(old_json):
    assert pathlib.Path(relative).read_bytes() == subprocess.run(
        ["git", "show", f"cc2b73a2227326746aa80d05cd5cc7e5676d7855:{relative}"],
        check=True, stdout=subprocess.PIPE).stdout
```

The loop prints the tuple deltas for review; it should not be replaced with an assumed “all unchanged” assertion if round-25 fixtures are intentionally added. For the identity comparison, if newly authored r25 fixture JSON is expected, report the 364 old paths as unchanged and enumerate additions separately instead of requiring set equality. The declaration requests unchanged old JSON paths, not absence of legitimate new ones (`.shokunin/lore/LOG.md:368`).

For focused behavior, replay each named fixture and inspect all `relations[0].from` / `.to` diagnostics, not only exit status:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<r25-to-duplicate>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<r25-both-duplicate>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<r25-unique-control>
```

Use actual committed fixture directory names in place of placeholders. Required evidence is a local `relations[0].to: ambiguous entity ...` for the duplicate-to case, both precise endpoint-local findings if both IDs are duplicated, and no ambiguity at either endpoint in the unique control. All should retain expected existing duplicate-ID/source diagnostics. Compare fixture tables against their stated minimal mutation and confirm source IDs are unique/resolvable; an exit code alone cannot establish the targeted rule.

## Risks and limits

- `r12` and `r21` provide prior duplicate-`from` evidence, not a substitute for a duplicate-`to` case. The checker’s shared loop makes the expected `to` result plausible, but only the actual fixture replay demonstrates it (`.shokunin/lore/corpus/fixtures/check_bible.py:123-129`; `.shokunin/lore/LOG.md:367-368`).
- A fixture that duplicates both endpoints can show two diagnostics but cannot isolate `to`; retain a `to`-only paired case and unique control. Ensure endpoint IDs are otherwise well-formed and cited. Do not accidentally change relation type/source fields while claiming endpoint-only variation.
- Duplicate IDs make the dictionary index last-wins (`check_bible.py:45-51`); the new finding must be described as ambiguity, not a selected entity. A unique-ID control should check both fields, while a missing-ID control can guard the existing dangling path if included.
- The declaration’s exact-output regression assertion applies to the 73 prior directories. New r25 fixtures are additions, not regressions; compare all old directories against the baseline and report additions separately. Current tracked/untracked status matters when asserting 73 is the total after authoring.
- JSON identity is byte/path identity only. Unique source-ID resolution, structural endpoint ambiguity and checker outputs do not prove that a source supports a relation, that duplicate rows denote distinct people, or that any relationship is canon. No truth, narrative or game-mechanics inference follows from this replay.
