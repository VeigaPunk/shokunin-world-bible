# V94 c1-two-mutation

Axes: calibration (a simultaneous JSON+Markdown byte edit is one `DIGEST-MISMATCH` that names every changed pinned file) and precedence fidelity (that naming matches the contract text, not a first-file truncation). Isolation: scratch mirror only.

Verdict on the delivered bytes: **PASS**. `DIGEST-MISMATCH` names **both** files. It does not stop at the first. The contract's "first failing check" rule is finding-class order, and the semantic-plus-markdown control confirms it.

## What was tested

Delivered bytes, snapshotted before the runs and still identical at 2026-10-17T22:26:18-03:00:

- `corpus/tools/dependency_freeze.py` sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (29104 bytes, mtime 2026-10-17 22:07:33.506669398 -0300)
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes, mtime 2026-10-17 22:08:46.248249589 -0300)

Contract at that revision: `schema_version` 2, `payload_schema_version` 2, six chain pins, each `files` object has all ten declared names. No `r99-window-lapse` pin (not this seat).

S1 producer report: **ABSENT** at 22:26:18. Artifacts were already on disk and unchanged from 22:07:33 / 22:08:46 through the stability checks at 22:22:20, 22:22:40, 22:23:00, and 22:23:20 (`py_match=True ct_match=True`). Stall-escape: did not burn the remaining poll window after the bytes had been still for ~15 minutes. This is a verification of those bytes, not of a plan. Poll log: `.ufo/waves/round-99/seats/V94-scratch/poll.log`.

Live fixtures were not written. Mutations live only under `.ufo/waves/round-99/seats/V94-scratch/mirror/`. Live vs mirror sha256 prefixes diverge exactly on the mutated copies (`r98` `entities.json` live `db2d8e5d3866009b` / mirror `457e41d31d3c78cd`; same pattern for the other four mutated files).

Mirror layout so `Path(__file__).parents[2]` binds the copied pin path `corpus/fixtures/<name>` to the scratch fixture (no `PATH-MISMATCH`, no `--freeze`, no live contract write).

## Contract precedence (quoted)

`corpus/tools/dependency-freeze-contract.json` field `precedence` (one string):

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the semantic inventory does not model exits 2 (DIGEST-MISMATCH) and names each changed pinned file, including the five Markdown files. Exit-2 (could-not-evaluate) checks run in this order and the first failing check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable contract, invalid pin, payload_schema_version other than 2, or a pin that does not digest all ten pinned files), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build of the JSON tables), DIGEST-MISMATCH (inventory clean, any pinned-file bytes changed or missing), INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's recorded path) and FILE-MISSING when a declared pinned file is absent. A path-less legacy pin is migrated in place by --freeze instead of refused. Re-freeze is the payload upgrade path from a schema-1 JSON-only pin to payload_schema_version 2.

Two different rules in that paragraph:

1. File list inside `DIGEST-MISMATCH`: "names **each** changed pinned file, including the five Markdown files." Not "the first file."
2. Which finding wins: "the first failing check decides." That orders finding IDs (semantic exit 1 before digest exit 2; then the exit-2 list). It does not truncate the file list inside a digest finding.

Code matches (1). `changed_files` walks the sorted union and joins every delta:

```358:367:corpus/tools/dependency_freeze.py
def changed_files(pin, observed):
    changes = []
    for name in sorted(set(pin["files"]) | set(observed["files"])):
        before = pin["files"].get(name)
        after = observed["files"].get(name)
        if before != after:
            changes.append(f"{name} (sha256 {before} -> {after})")
    if not changes:
        changes.append("(no per-file digest difference; the pin's file digests disagree with its content digest)")
    return ", ".join(changes)
```

`verify` emits one `DIGEST-MISMATCH` whose detail interpolates that whole string (`corpus/tools/dependency_freeze.py:388-393`). `emit` prints each finding tuple (`:103-106`); only one tuple is passed. Semantic findings return at `:384-387` before the digest check, which is rule (2).

## Runs

Clean baselines on the same mirror, before mutation, both exit 0:

- r98: `FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1` / `DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` / `RESULT PASS`
- r95 (restored after a discarded swapped-role mutation that was not verified): `FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1` / `DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` / `RESULT PASS`
- r96: `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1` / `DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` / `RESULT PASS`

JSON edits in the digest pairs are trailing newlines only. `json.loads` of r95 `timeline.json` before and after compared equal, so the semantic inventory stayed clean and the digest path was the one under test. Markdown edits append a comment line. Both files were written, then one verify.

### Pair A — JSON sorts before Markdown (r98)

`entities.json` `1793→1794` bytes, sha256 `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` → `457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3`. `fictional-excerpts.md` `4187→4214`, sha256 `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de` → `c62880b9beab277b88dfa2321eef5fd4663b256b8189e9a1568d3cd824842c3c`.

```
command: /usr/bin/python3 .../V94-scratch/mirror/corpus/tools/dependency_freeze.py .../mirror/corpus/fixtures/r98-clerk-filing
cwd: .../V94-scratch/mirror
exit: 2
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 9d89ba3f8e19d34394575a782b8a69c38e7a4ee94b823c0cd8912bafe05416ad != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: entities.json (sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 -> 457e41d31d3c78cdde591e532dc04083561d223705cb5d334d945885624242c3), fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> c62880b9beab277b88dfa2321eef5fd4663b256b8189e9a1568d3cd824842c3c); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

stderr empty. Both names are in the one finding. Named shas match the independent hashes above. Saved: `V94-scratch/runs/r98-two-file.txt`.

### Pair B — Markdown sorts before JSON (r95)

`README.md` sha256 `9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b` → `168bbd76884e700dc0ec922b9db9c64293619061f3391d37247b3d34295ef098`. `timeline.json` sha256 `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` → `bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2`. Timeline parse before/after: equal.

```
exit: 2
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 124b8f48687b94f6106731b52c66e1f579b20c6aa5a77fb9671085a3c012ac4c != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: README.md (sha256 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b -> 168bbd76884e700dc0ec922b9db9c64293619061f3391d37247b3d34295ef098), timeline.json (sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

stderr empty. Again both names. Saved: `V94-scratch/runs/r95-two-file.txt`.

The first name in the detail is lexicographic (`sorted` in `changed_files`), not a precedence cut. Pair A leads with the JSON file; pair B leads with the Markdown file. The second file is still named in both.

### Control — semantic finding plus Markdown (r96)

`timeline.json` tick of `aru-ninth-bell` `9 → 10`, and `source-excerpt.md` appended a comment, then one verify.

```
exit: 1
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
FINDING ENDPOINT-CHANGE: event aru-ninth-bell.tick: 9 -> 10
RESULT FAIL
```

stderr empty. No `DIGEST-MISMATCH` line. Saved: `V94-scratch/runs/r96-semantic-plus-md.txt`.

That is the documented "first failing check": semantic inventory decides first, so the digest check does not run and does not name either file. It is not a rule that `DIGEST-MISMATCH` names only the first changed file.

## Comparison

| Contract sentence | Observed |
| --- | --- |
| digest change exits 2 `DIGEST-MISMATCH` and names each changed pinned file, including Markdown | Pairs A and B: exit 2, one finding, both the JSON name and the Markdown name, with before/after sha256 |
| semantic findings decide first | Pair C: exit 1 `ENDPOINT-CHANGE` only; digest finding absent |
| first failing check decides (finding-class order) | Same control. Does not drop the second filename once `DIGEST-MISMATCH` is the deciding check |

No contradiction between the contract precedence text and the runs.

Out of this seat's comparison target, and not scored here: `corpus/tools/README.md` and `SKILL.md` still describe the pre-r99 five-JSON-table bound (README freeze row still says the pin covers JSON tables only; SKILL.md:100 still says Markdown is not pinned). S2 owns those files. The precedence text this seat was told to compare against is the contract field quoted above.

## Bottom line

PASS — simultaneous JSON+Markdown byte edits exit 2 `DIGEST-MISMATCH` naming both files (two fixtures, both sort orders); contract says "names each", and "first failing check" is finding-class order (confirmed: tick change + Markdown exits 1 `ENDPOINT-CHANGE` with no digest line). S1 report absent; tested bytes stable sha256 `6f81f8be…` / `8c2561b0…`.
