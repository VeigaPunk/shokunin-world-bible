# Round 4 independent verifier — exact duplicate display names

Status: **PASS within the stated replay scope; no checker or fixture edits made.** I acted as a non-author verifier. I inspected raw repository fixtures, ran the CLI directly, and extracted the checker and old fixture inputs from round-3 baseline `5ceb0e431f686ed0ee29f11b66939c8f661dcc63`; this is not based only on the author report.

## Commands

All repository commands were run from the repository root. Seven current fixture cases were invoked with the same command pattern:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

Cases: `consistent`, `contradictions`, `ally-reciprocal`, `ally-one-way`, `contradictions-ledger-malformed`, `name-unique`, `name-duplicate`.

For the old five cases, baseline extraction and replay used:

```sh
git archive 5ceb0e431f686ed0ee29f11b66939c8f661dcc63 .shokunin/lore/corpus/fixtures
python3 <extracted-baseline>/check_bible.py <extracted-baseline>/<case>
```

I made two temporary probes by copying raw `consistent/` into `/tmp` and appending one entity row to `entities.json`; no repository inputs were changed. The duplicate-ID probe copied `entities[0]` (same ID and same name); the case-variant probe copied `entities[1]` but assigned a distinct ID and the lowercase name `mira`.

## Current seven-case results

| Fixture | Exit | Exact stdout |
|---|---:|---|
| `consistent` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `contradictions` | 1 | `VIOLATION: relations[1].to: dangling entity 'missing-map'`<br>`VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2`<br>`VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'`<br>`3 violation(s); no canon changed` |
| `ally-reciprocal` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `ally-one-way` | 1 | `VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`<br>`1 violation(s); no canon changed` |
| `contradictions-ledger-malformed` | 1 | `VIOLATION: contradictions[1].claim_b.event_id: expected exactly one timeline event 'absent-event'`<br>then the same three `contradictions` violations above<br>`4 violation(s); no canon changed` |
| `name-unique` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `name-duplicate` | 1 | `VIOLATION: entities[0] and entities[1]: duplicate display name 'Mira' for distinct entity IDs 'mira-one' and 'mira-two'; review, do not merge`<br>`1 violation(s); no canon changed` |

All stderr was empty. These are raw CLI results, not transcribed from the author report.

## Baseline comparison and unchanged records

I ran the five pre-existing fixtures against both the current checker and the checker extracted from baseline `5ceb0e4`. Each pair had identical exit status and byte-identical stdout: `consistent` (0), `contradictions` (1, same three findings), `ally-reciprocal` (0), `ally-one-way` (1, same reciprocal finding), and `contradictions-ledger-malformed` (1, same four findings). No prior outcome changed.

I SHA-256 compared all five JSON tables (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) for those five existing fixture directories against `git show 5ceb0e4:<path>`: **25/25 match**, zero changed or missing records.

## Temporary probes

- Duplicate-ID ambiguous group: exit **1**, stdout `VIOLATION: entities[4].id: duplicate entities id 'mira'` / `1 violation(s); no canon changed`. No duplicate-name message was emitted for that ambiguous ID. This matches the stated exclusion of duplicate IDs from the new rule.
- Case variant: distinct IDs with raw names `Mira` and `mira` exited **0** (`CLEAN: schema, citations, relations, timeline; 0 violations`). The check is case-sensitive for this probe.

## Input stability and limits

Before and after all CLI runs/probes, I SHA-256 hashed all **37 files** under the repository fixture tree (checker and all fixture files): identical path/hash map. Aggregate SHA-256 over sorted `path + file hash` records: `bcd6a793b6757010d7817e4b1443c55eaf6bcc9174b957e0e34ae95a6b7242b2` both before and after. Temporary probe copies were outside the repository.

Limits: this verifies these seven cases and two targeted probes only. It does not establish correctness for all schemas, malformed names, Unicode normalization, whitespace variants, or actual canon. Duplicate names are flagged for review; they are not proof of shared identity or that homonyms are invalid. No commit was made.
