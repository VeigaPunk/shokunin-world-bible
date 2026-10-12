.shokunin/lore Round 5 loader scout — observations

Scope: actual loader/CLI behavior for an absent required table, invalid JSON, and valid JSON with a nonarray top-level value. I did not change checker code, fixtures, or shared documentation. The three probe directories are temporary and currently at `/tmp/lore-r5-loader-scout/{absent,invalid-json,nonarray}`; each began as a copy of `.shokunin/lore/corpus/fixtures/consistent` and changed only `entities.json` (deleted, replaced with `{not json\n`, or replaced with `{"rows": []}\n`). These are observed probes, not committed/reproducible repository fixtures.

## Observations (actual CLI)

Checker: `.shokunin/lore/corpus/fixtures/check_bible.py`. Commands were run at the repository root:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-loader-scout/absent` → exit 1. First diagnostic: `entities.json: cannot load JSON: [Errno 2] No such file or directory: '/tmp/lore-r5-loader-scout/absent/entities.json'`; then six dangling-entity diagnostics for relation/timeline references; summary `7 violation(s); no canon changed`.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-loader-scout/invalid-json` → exit 1. First diagnostic: `entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`; then the same six dangling-entity diagnostics; summary `7 violation(s); no canon changed`.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r5-loader-scout/nonarray` → exit 1. First diagnostic: `entities.json: expected array`; then the same six dangling-entity diagnostics; summary `7 violation(s); no canon changed`.
- Control: `python3 .shokunin/lore/corpus/fixtures/check_bible.py /home/vgpnk/Projects/prymeagnt/lore/.shokunin/lore/corpus/fixtures/consistent` → exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`.

All commands had empty stderr. The loader in `check_bible.py` catches `OSError`, `UnicodeError`, and `json.JSONDecodeError` and records `cannot load JSON`; it then sets rows to `[]`. A successfully parsed non-list gets `expected array`, then rows are likewise set to `[]`. The checker continues into cross-table checks in every case, so a missing/invalid entities file creates additional dangling-reference diagnostics. These are CLI findings, not process crashes.

## Recommendations (not implemented)

- The decision table should distinguish the loader-local diagnostic (`cannot load JSON` vs `expected array`) from the downstream dangling-reference diagnostics, and note that all three tested malformed inputs currently exit 1.
- Do not describe these as isolated single-error outputs: the probe mutates one file, but removing its entities predictably triggers dependent checks. If the table needs loader-local-only expected output, use a minimal bible with no dependent references, or explicitly list the cascade.
- The `/tmp` probes are ephemeral. Before citing them as reproducible committed evidence, recreate equivalent fixtures under the round's allowed fixture/evidence path and rerun the exact CLI commands there.
