# V37 running notes (round 97) — scratch

## Baseline (f3e09f9) hashes measured 18:43
- map_obligations.py `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (24-case contract `97b76bb8…`)
- dependency_freeze.py `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980`
- freeze contract `c65ac3bd4fc090d8696b5739a6e5971cc06aba4700ad7458b9f9b04a8e99a4d2` (4 pins: r88, r94, r95, r96)
- tools README `ba7d2ff12851dff1175dc09a0dcb9679875a19a45840431d5e720d462cfe6945`
- r96 map pre-repair `90c208f…`? (git index blob); worktree repair landed by 18:44:30 (2 ins/2 del)

## r96 V40 ledger item list (carried) → r97 claim mapping
- NB-01 dual_pointer legacy-only → C1(a) pin (R1/R2)
- NB-02 inventory gating scope → accepted bound
- NB-04 --freeze scope guard + c3red (c3red already removed at r96 closure) → C2(a)
- NB-05 pin-set validation for freeze → C2(d)? verify
- NB-06 basename-only pins → C2(b) path binding
- NB-07 BR-01 prose half → NOT claimed → open
- NB-08 DIGEST-MISMATCH names file → C2(c)
- NB-09 SELF-TEST-MISMATCH exit convention → verify R3
- NB-10 freeze() discards verify result; MALFORMED-MODEL/CONTRACT-INVALID unpinned → verify R3
- NB-11 chain-scoped/byte-sensitive/unregistered → registration done r96; r97 fixture NOT in chain (4/4) → new bound
- NB-14/NB-26 stale note pins (r95 note :51 9224a684; r96 note :55 6634e176) → check r97 closure re-runs
- NB-15 r96 map nits: delimiter + "new relation" → C3 repair (done in worktree); THIRD nit ":18 'r94 JSON pointers'" NOT in r97 scope → open
- NB-16 docs presupposition → check R5/R6 text
- NB-17 /tmp inode exhaustion → host condition (V09 confirms still exhausted 18:4x)
- NB-18 BR-05 scratch (map tool self-test dir under repo root) → check R1 delivered
- NB-20/NB-21 drift scope + consistent regeneration → not claimed → open
- NB-25 dual_pointer unpinned + droppable pins → C1(a)+C1(b)
- CL-04 C9 watch row-6 due at r97 (watch says "Next re-check: r97")
- CL-02 fixtures README Round-97 section + census 171
- CL-03 corpus/README + SKILL.md case counts (24→25 map; 14→16 freeze)

## Early seat findings (round 97)
- V09 (c2-selftest): /tmp inodes exhausted (`df -i /tmp` 1048576/1048576 100%); self-test fails ENOSPC unless TMPDIR redirected; pre-change 14/14 with TMPDIR=scratch; perturbation harness validated (flip clean.exit → 13/14 SELF-TEST-MISMATCH). STATUS INCONCLUSIVE pending R3.
- V45 (c2-guard-2): baseline B-A shadow copy verifies identically exit 0; B-B DIGEST-MISMATCH no file name (sources.json re-indent); B-C --freeze accepts out-of-scope path in fakerepo sandbox and rewrites pin fixture path. After-state pending R3.
- V44 (c1-negative-2): nine-class matrix harness vs frozen r96 control; delivered table pending R1+R2 report.

## Mid-flight producer observations
- 18:45:31 R1 edit: ADDED_SELF_TEST_CASES += dual_pointer; loader `missing = set(SELF_TEST_CASES) - set(expected)` (tightening); legacy_test_rows/DUAL_POINTER_CELL helpers; docstring updated.
- 18:46:30 R2 edit: contract 25 cases (dual_pointer added).
- 18:44 R4: r96 map repair landed (both halves); r97 fixture skeleton (entities/relations/contradictions copies; sources 6; timeline 6 w/ tick-13 ack event; fictional-excerpts w/ folio 7).
- r97 map still 16 rows at 18:47 (missing J17); README still r96 copy.
