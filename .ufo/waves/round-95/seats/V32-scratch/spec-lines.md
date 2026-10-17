# r95 LOG declaration — line inventory for conformance mapping

Source: LOG.md tail, "## Round 95 — declaration before dispatch (2026-10-17)".
Baseline fb118c4 (verified `git log --oneline -1` = fb118c4 at seat start).

## Declaration-context lines
L0.1 Operator 100-round regimen round 1 of 6 (r95–r98 64-seat deepseek-v4.1-flash; r99 128-seat grok-4.7-fast; r100 32-seat sol-max).
L0.2 Baseline = r94 closure fb118c4.
L0.3 One batched AgentSwarm, 64 seats: 5 producer + 59 verifier/judge.
L0.4 Verifier seats poll-wait for declared artifact paths (20 s cadence, 40 tries), report ABSENT rather than verify a plan.
L0.5 Seat reports exclusive under .ufo/waves/round-95/seats/.
L0.6 Scores remain unmeasured; claims are falsifiable before→after obligations.
L0.7 Owned axis set: depth, coverage, calibration; operability/freshness/adjacency judged as witnessed (r93/r94 precedent).

## C1 — calibration
C1.a Close BR-02 (schema-drift class) and BR-03 (self-test coverage gaps) in map_obligations.
C1.b BEFORE: renamed `claims` key (claim content preserved) + removal of that claim's map row → silent `RESULT PASS` exit 0.
C1.c AFTER: that exact mutation class yields exit 1 with stable `schema_drift` FINDING ID.
C1.d Persisted contract carries 22 self-test cases including `map_missing` and `invalid_arguments`.
C1.e r93 12/12 unchanged.
C1.f r94 14/14 unchanged.
C1.g frozen-r93 digest replay unchanged.
C1.h r87/r89 fail-closed behavior unchanged.
C1.i Counting: mutation demo on scratch copies (old tool from git vs delivered).
C1.j `python3 corpus/tools/map_obligations.py --self-test` exit 0.

## C2 — depth
C2.a First reported non-performance against a crossing-scoped agreement.
C2.b New fixture corpus/fixtures/r95-crossing-aftermath/ = preserving copy of r94-paired-crossing + one authored aftermath note (`aru-aftermath-note`) + one tick-11 event (`aftermath-missing-evin`, actor `aru`, place `chalk-stair`, `depends_on: ["paired-crossing-decision"]`) recording Aru waited through the agreed bell, Evin did not come.
C2.c Explicitly scoped: agreement covered this crossing only; record asserts no other duty or breach.
C2.d BEFORE: 5 entities / 1 relation / 3 events / 3 sources, 14 map obligations at r94.
C2.e AFTER: 5/1/4, 4 sources, 15 map obligations (14 inherited rows unchanged + new event row; no new claims/entities/relations).
C2.f check_bible CLEAN exit 0.
C2.g Inherited r94 rows parsed-value identical.
C2.h census 168→169.
C2.i No perpetual-breach, canon-truth, or identity inference.

## C3 — coverage
C3.a map_obligations dialect coverage of r88 map form — tool surface only, zero corpus modifications.
C3.b BEFORE: `map_obligations.py corpus/fixtures/r88-m3-maya-cluster` exits 2 `unsupported_map`.
C3.c AFTER: 12/12 PASS over the r88 map's obligations with same anchors/spans/modes.
C3.d r87/r89 legacy forms remain exit 2 fail-closed.
C3.e support_check receipts on r88 (10 JSON + 2 editorial) and r93/r94 unchanged.

## Admission rule + invariants
A.1 Admit iff C1, C2, C3 each verify on delivered revision and no axis harmed.
A.2 Per-axis verdicts, no scalars; harmed/unprovable reported as such, not forced.
A.3 Same-lane seats are the lane (no [x], no promotion, no capability row before demonstrated final result).
A.4 r96 does not start on unclosed r95.
I.1 Producer byte-ownership: P1 map_obligations.py; P2 map-obligations-contract.json + README addendum; P3 fixture JSON tables + fictional-excerpts.md; P4 fixture README.md + claim-excerpt-map.md; P5 corpus/knowledge/r95-aftermath-scope-note.md.
I.2 Everything else read-only except seat reports.
I.3 No commits by seats.
I.4 Poll-wait honesty (ABSENT not plan-verification).

## My independent baselines captured (V32-scratch/baseline/)
- baseline tool sha256 cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790
- baseline contract 20 cases; self-test exit 0 (20/20)
- r88 → exit 2 unsupported_map; r87-myth-cluster → exit 2; r89-inspiration-paraphrase → exit 2
- r93 → 12/12 PASS exit 0; r94 → 14/14 PASS exit 0
- frozen r93 replay → PASS exit 0 (snapshot .ufo/waves/round-94/frozen/map-obligations-r93)
- census 168; r94 check_bible CLEAN exit 0
- support_check r88 10/10 + 2/2; r93 12/12 + 3/3; r94 14/14 + 2/2
- BR-02 mutation on scratch copy of r94 under baseline tool → `OBLIGATIONS raw=13 mapped=13 / RESULT PASS` exit 0
