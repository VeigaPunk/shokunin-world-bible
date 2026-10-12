# Round 2 independent verifier report — non-author CLI replay

## Scope and method

I independently read `.shokunin/lore/LOG.md` round 2, `corpus/fixtures/check_bible.py`, `corpus/fixtures/README.md`, the round-2 decision table, fixtures, round-1 and round-2 saved run evidence, and wave-1 scout/critic/executor reports. I did not edit canon, checker, fixtures, or commit. Replayed the CLI from the repository root and generated three probe directories under `/tmp/lore-r2-independent-wo9ha6bb` by copying `ally-reciprocal` and changing only JSON there.

## Raw CLI replay

Command (shell loop; each invocation used the exact `python3` CLI shown):

```sh
set +e
for d in consistent contradictions ally-reciprocal ally-one-way; do
  echo "--- $d ---"
  python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/$d
  echo exit_code=$?
done
```

Observed stdout and exit codes:

```text
--- consistent ---
CLEAN: schema, citations, relations, timeline; 0 violations
exit_code=0
--- contradictions ---
VIOLATION: relations[1].to: dangling entity 'missing-map'
VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2
VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'
3 violation(s); no canon changed
exit_code=1
--- ally-reciprocal ---
CLEAN: schema, citations, relations, timeline; 0 violations
exit_code=0
--- ally-one-way ---
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
1 violation(s); no canon changed
exit_code=1
```

These match the saved `corpus/live/runs/20261012T161753Z/{consistent,contradictions,ally-reciprocal,ally-one-way}.txt`. The one-way diagnostic is relation-local. The contradiction fixture still emits exactly its three seeded violation classes: dangling endpoint, timeline inversion, and double booking.

## Temporary edge probes

Commands were `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-directory>` for each directory:

1. `/tmp/lore-r2-independent-wo9ha6bb/unknown-source-reverse`: copied reciprocal fixture; changed `relations[1].source_id` to `no-such-source`.

```text
exit_code=1
VIOLATION: relations[1].source_id: unknown in-world source 'no-such-source'
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
2 violation(s); no canon changed
```

The unknown-source reverse is not accepted as a qualified witness, as required by the round-2 claim.

2. `/tmp/lore-r2-independent-wo9ha6bb/nonfaction`: copied reciprocal fixture; changed `entities[1].kind` from `faction` to `place`.

```text
exit_code=0
CLEAN: schema, citations, relations, timeline; 0 violations
```

This confirms non-faction endpoints are outside the new symmetry check; the checker does not currently enforce a relation endpoint's kind generally.

3. `/tmp/lore-r2-independent-wo9ha6bb/dangling-endpoint`: copied reciprocal fixture; changed `relations[0].to` to `no-such-faction`, leaving reverse row intact.

```text
exit_code=1
VIOLATION: relations[0].to: dangling entity 'no-such-faction'
VIOLATION: relations[1]: allied_with faction relation 'bell-wardens' -> 'quay-guild' lacks a sourced reciprocal relation
2 violation(s); no canon changed
```

Caveat: the dangling relation itself does not get a missing-reciprocal cascade, but its formerly reciprocal, still-valid reverse row is reported as now lacking a witness. This is consistent with per-row checking; it means this probe is not “dangling endpoint only” when a paired edge remains. The base contradictions fixture's dangling `consults` edge is unaffected by this symmetry rule.

## Nonmutation check and conclusion

Before and after the CLI replays, SHA-256 hashes were compared for `check_bible.py` and every repository fixture `*.json`; no tracked input changed. Probe edits were confined to `/tmp`. CLI output says `no canon changed` for each violating invocation. I observed no source-file writes from the checker.

Independent verification: **pass for the declared narrow behavior**: consistent and reciprocal fixtures exit 0; one-way and unknown-source-reverse exit 1 with expected violations; unrelated round-1 violation classes remain; nonfaction pair is outside rule. Caveats: no broader semantic/canon correctness is tested; dangling-endpoint probe reports both the dangling error and the remaining reverse row's now-missing reciprocal, as noted above.
