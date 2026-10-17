# JCOV3 — Coverage judge #3 (branch-exercise auditor), completed by the L1 parent inline

Status note: this seat was interrupted twice by the operator before a dispatched
agent could finish; the parent ran the four probes directly on the delivered
tree (checker at HEAD `2b48ca7`, SHA-256 `3ae4134d…`) and writes this report.
Method and receipts below are the parent's own runs, in the same protocol the
seat block declared.

## Question

For each structural element of `corpus/fixtures/r87-myth-cluster/`, prove it
actually exercises its intended checker branch — positively (the clean cluster
passes the branch) and negatively (a targeted mutation fires exactly that
branch's violation).

## Probes (all in `/tmp/jcov3*`, delivered checker, repo-root invocation)

| # | Mutation | Intended branch | Result |
|---|---|---|---|
| P1 | drop `reedwardens -> shellweavers` relation | reciprocal-alliance check (`check_bible.py:258-276`) | FIRED: `allied_with faction relation 'shellweavers' -> 'reedwardens' lacks a sourced reciprocal relation`; clean cluster emits none — the surviving direction exercises the branch positively |
| P2 | event `bell-tally-return` re-booked as `hara` at tick 1 (different valid place `ash-dune-sanctuary`) | occupied-slot / double-booking (`check_bible.py:278-303`) | FIRED: `double-booked 'hara' at tick 1 in timeline[0] ('mother-tide-gate') and 'ash-dune-sanctuary'`; the clean cluster's same-tick-different-place pairs (`hara`/`sen` at tick 3) exercise the near-miss pass path |
| P3 | `first-lowwater-signal.depends_on := [moon-basin-vow-dune-account]` (later tick) | `depends_on` inversion (`check_bible.py:318-325`) | FIRED: `timeline inversion 'moon-basin-vow-dune-account' tick 3 not before 'first-lowwater-signal' tick 1`; the clean cluster's 3 forward edges exercise the pass path |
| P4 | `contradictions[0].claim_b.event_id := 'no-such-event'` | contradiction event resolution (`check_bible.py:130-132`) | FIRED: `expected exactly one timeline event 'no-such-event'`; the clean cluster's resolvable `gate-witness`/`dune-register` pair exercises the pass path |

Every mutated copy exited 1 with exactly its intended violation (P2 also
reports the inversion introduced by re-ticking; P1's allied finding accompanies
P3/P4 as those probes build on the P1 base). The unmutated cluster exits 0,
`CLEAN: schema, citations, relations, timeline; 0 violations`.

Commands (repo root): `python3 corpus/fixtures/check_bible.py /tmp/jcov3` (and
`-p2`, `-p3`, `-p4`).

## Verdict recommendation

Coverage **improved (bounded)**, corroborating JCOV1 §5/§7 and H3 by the
pass+fire pairing: each claimed structural element is load-bearing against its
checker branch, not decorative schema. Bound unchanged from JCOV1: the cluster
is a positive-path surface; it adds no new finding template.

## Debt carried (not this seat's to fix)

- `corpus/fixtures/README.md` has no `## Round 87` section registering the
  cluster (nor the C1 fixtures) — index debt for r88.
- OBS-1 (hymn attribution support gap) stands per Q1/JCOV4.
