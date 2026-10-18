# Round 2 test scout: independent replay plan

## Evidence inspected

- `.shokunin/lore/LOG.md` Round 2 declares the `allied_with` reciprocal-edge rule and asks for existing-consistent (exit 0), reciprocal (exit 0), and one-way (exit 1 with relation-local violation) cases.
- `.shokunin/lore/corpus/fixtures/check_bible.py` takes one bible directory, prints `VIOLATION: ...` lines and a final count, returns 1 when any exist; clean output is `CLEAN: schema, citations, relations, timeline; 0 violations`.
- `.shokunin/lore/corpus/fixtures/README.md` records the established direct invocation pattern.
- `.shokunin/lore/corpus/live/runs/20261012T155644Z/{consistent,contradictions}.txt` preserve round-1 expected outcomes (clean 0; three current seeded violations and exit 1).
- `.shokunin/lore/corpus/fixtures/consistent/{entities,relations}.json` has no faction/alliance relation and is a useful regression input. Existing faction records/fixture paths for round 2 are not present at scout time, so use the executor's declared new fixture directory names below in place of `<reciprocal-fixture>` and `<one-way-fixture>` if they differ.

## Replay from repository root

Run each independently (do not use `set -e` around the expected-failure cases):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<reciprocal-fixture>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<one-way-fixture>
```

For an executable assertion that preserves expected nonzero results and checks output, run from the repo root:

```sh
python3 - <<'PY'
import subprocess
checker = '.shokunin/lore/corpus/fixtures/check_bible.py'
def replay(folder):
    return subprocess.run(['python3', checker, folder], text=True, capture_output=True)
clean = replay('.shokunin/lore/corpus/fixtures/consistent')
assert clean.returncode == 0, (clean.returncode, clean.stdout, clean.stderr)
assert '0 violations' in clean.stdout, clean.stdout
reciprocal = replay('.shokunin/lore/corpus/fixtures/<reciprocal-fixture>')
assert reciprocal.returncode == 0, (reciprocal.returncode, reciprocal.stdout, reciprocal.stderr)
assert '0 violations' in reciprocal.stdout, reciprocal.stdout
one_way = replay('.shokunin/lore/corpus/fixtures/<one-way-fixture>')
assert one_way.returncode == 1, (one_way.returncode, one_way.stdout, one_way.stderr)
assert 'allied_with' in one_way.stdout and 'relations[' in one_way.stdout, one_way.stdout
assert 'no canon changed' in one_way.stdout, one_way.stdout
contradictions = replay('.shokunin/lore/corpus/fixtures/contradictions')
assert contradictions.returncode == 1, (contradictions.returncode, contradictions.stdout, contradictions.stderr)
assert contradictions.stdout.count('VIOLATION:') == 3, contradictions.stdout
print('PASS: consistent, reciprocal, one-way, and round-1 contradiction replays')
PY
```

Expected assertion outcome: process exits 0 and prints exactly `PASS: consistent, reciprocal, one-way, and round-1 contradiction replays`. The one-way fixture should produce a relation-local message identifying the offending relation and missing reciprocal direction; the assertion intentionally checks the stable `allied_with` and `relations[...]` anchors, not a brittle full diagnostic string. The reciprocal fixture should have no violations. Round-1 contradiction fixture should still report the same three distinct existing classes (dangling endpoint, timeline inversion, double booking); new symmetry rule must not add unrelated diagnostics there.

## Cautions

- Run from repo root and use `python3`; the recorded paths/README are repo-root relative. Do not test an alternate interpreter or import `check_bible` as a module when the user-facing interface is its CLI.
- Confirm and substitute fixture directory names from the integrated tree; none for the new round-2 cases existed during this scout pass. Avoid mistaking a missing path's load errors for the intended one-way test.
- A malformed or missing JSON input may yield other errors; do not treat that as a symmetry-rule result.
- The contract applies to explicit `allied_with` relations between faction entities only. Do not assert symmetry for unrelated relation types, infer relations from prose, or interpret missing alliances as contradictions generally.
- The checker must report only; assert the CLI's `no canon changed` marker, and inspect git diff/fixture state if concerned about mutation. No lore/game-mechanics or real-world rights conclusion is tested here.
