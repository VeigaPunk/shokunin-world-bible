# Round 3 independent verifier report

Role: non-author replay. I made no implementation or fixture changes. Commands below were run from the repository root with `python3`; temporary probes were under `/tmp`.

## Five raw-fixture CLI replays

Command form for each case:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

| Case | Exit | Output |
|---|---:|---|
| `consistent` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `contradictions` | 1 | dangling `missing-map`; `arrival` depends on later tick-3 event; Mira double-booked at tick 2 (`tower` / `harbor`); `3 violation(s); no canon changed` |
| `ally-reciprocal` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `ally-one-way` | 1 | missing sourced reciprocal `allied_with` relation; `1 violation(s); no canon changed` |
| `contradictions-ledger-malformed` | 1 | ledger-local unresolved `absent-event`, followed by the same three original contradiction findings; `4 violation(s); no canon changed` |

These outputs match the saved run at `corpus/live/runs/20261012T162704Z/`.

## Baseline preservation (`ba110ea`)

Commands:

```sh
git archive ba110ea3495571ce027699dc9bfabc9d2912cffb .shokunin/lore/corpus/fixtures | tar -x -C "$tmpbase"
python3 "$tmpbase/.shokunin/lore/corpus/fixtures/check_bible.py" "$tmpbase/.shokunin/lore/corpus/fixtures/<case>"
```

I replayed `consistent`, `contradictions`, `ally-reciprocal`, and `ally-one-way` using the archived baseline checker and obtained the same respective outcomes: clean, the same three original contradiction strings, clean, and the same missing-reciprocal finding. Parsed `entities.json`, `relations.json`, `timeline.json`, and `sources.json` for each case are exactly equal to the baseline versions. In particular, `contradictions/relations.json` still points to `missing-map`; timeline rows still encode arrival tick 2 depending on later tick 3 and Mira at tower/harbor at tick 2. The new ledger adds references but does not alter these assertions.

## Required-file and malformed-pointer probes

Temporary-copy commands/operations and results:

```sh
cp -a .shokunin/lore/corpus/fixtures/consistent "$tmp/missing-ledger"
rm "$tmp/missing-ledger/contradictions.json"
python3 .shokunin/lore/corpus/fixtures/check_bible.py "$tmp/missing-ledger"
```

Exit 1: `contradictions.json: cannot load JSON: [Errno 2] No such file or directory: .../contradictions.json`; one violation, no canon changed.

```sh
cp -a .shokunin/lore/corpus/fixtures/contradictions "$tmp/malformed-pointer"
# Set contradictions[0].claim_a.event_id to "absent-event" in the temporary copy.
python3 .shokunin/lore/corpus/fixtures/check_bible.py "$tmp/malformed-pointer"
```

Exit 1: `contradictions[0].claim_a.event_id: expected exactly one timeline event 'absent-event'`, plus the same three seeded findings; four violations, no canon changed. Both probes left repository fixture inputs untouched.

## Mutation check and verdict

Before the five runs, I SHA-256 hashed the checker and all present case JSON inputs (26 files). The post-run hashes matched exactly; no checker or fixture mutation occurred. The temporary adversarial copies were outside the repository. `git diff ba110ea --` for the four original tables across the four original cases was empty, and parsed-content comparison was equal.

**Verified:** the five CLI outcomes reproduce; all original timeline and relation assertions/findings remain unchanged from `ba110ea`; missing required ledger and malformed pointer fail with ledger/file-local diagnostics; checker does not mutate inputs. Scope limit: this verifies the documented fixtures and two probes, not semantic truth of a ledger `why` or exhaustive malformed-input behavior.
