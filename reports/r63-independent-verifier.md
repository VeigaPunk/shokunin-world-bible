# r63 independent verifier report

## Scope and regression comparison
Independent verifier leaf; no children. Archived pinned r62 report commit `b8c1eeed94ef677349ee32a08c2244a7b4a4d8bf` independently with `git archive` to a temporary root. Compared full `.shokunin/lore/corpus` path sets and raw bytes (SHA-256): archived and current each contain 1,298 files; 0 paths added, 0 removed, 0 byte changes. All 623 archived fixture JSON paths are byte-identical. All 125 archived fixture directories were replayed from archive and current roots with identical repo-root-relative argv: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <repo-root-relative-fixture-dir>`. Raw stdout, stderr, and exit-status tuples: **0/125 mismatches**.

## Independent permissive-JSON probe
Created a temporary clone of the `consistent` fixture. Added extra source-object keys with JSON constants `NaN`, `Infinity`, and `-Infinity`; ran current checker from repo root with argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py <absolute-temp-clone>`. Exact output: `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty; exit 0.

Then changed first timeline `tick` to `NaN` (JSON constant). Exact stdout: `VIOLATION: timeline[0].tick: required nonempty int\nVIOLATION: timeline[1].depends_on: unknown event 'departure'\n2 violation(s); no canon changed\n`; stderr empty; exit 1. Changed tick to finite decimal `1.25`; exact same stdout, empty stderr, exit 1. The dependency message follows the invalid first event being excluded. These are narrowly observed checker outputs, not a parser-candidate comparison.

## Limits and verdict
No parser candidate exists; no candidate result is invented and no full producer compatibility is claimed. The executor's NO-GO expectation is supported: all pinned legacy corpus bytes and all 125 fixture stdout/stderr/status tuples are unchanged. Temporary archives/probes were outside the repository. No source/canon claim is made.
