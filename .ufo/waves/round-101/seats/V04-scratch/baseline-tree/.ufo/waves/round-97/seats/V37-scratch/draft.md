# V37 — debt-ledger (round 97) [DRAFT v2]

## CO table (r96 V40 items → r97 status), evidence from my battery/reports
| r96 item | r97 status | evidence |
|---|---|---|
| NB-25 (dual_pointer unpinned; droppable added pins) | CLOSED | my probes: 25/25; drop→exit 2; baseline 23/24 exit 0 |
| NB-04 (--freeze scope guard; c3red) | CLOSED (guard) | my SCOPE-REFUSED probe; c3red already removed r96 |
| NB-06 (basename-only pins) | CLOSED | my PATH-MISMATCH probe; baseline exit 0 |
| NB-08 (DIGEST-MISMATCH names file) | CLOSED | my digest probe names relations.json |
| NB-05 (pin-set validation for freeze) | CLOSED | contract 16 cases incl. scope_refused/path_mismatch; loader exact-set |
| NB-09 (SELF-TEST-MISMATCH exit convention) | CHECK R3 report/code | freeze self-test mismatch → emit(1) SELF-TEST-MISMATCH; convention? |
| NB-10 (freeze() discards verify result) | CLOSED (freeze propagates exit) | R3 report "freeze now propagates the post-freeze verify exit code" |
| NB-07 (BR-01 prose half) | OPEN (not claimed) | declaration C2 doesn't cover; R3 note |
| NB-11 (chain-scoped/byte-sensitive/unregistered) | PARTIAL: registration done r96; chain stays 4; r97 not pinned | my UNPINNED-FIXTURE probe |
| NB-15 (map nits) | 2/3 CLOSED (delimiter+sentence); ":18 r94 pointers" nit OPEN | diff 2/2; grep :18 unchanged |
| NB-14/NB-26 (stale note pins) | RECURRED: r97 note pins 70795150…+97b76bb8… | note receipts para; R6 report discloses |
| NB-17 (/tmp inode exhaustion) | OPEN (host); now also drove dependency_freeze self-test scratch to dir=ROOT | V09/V20/V26/V53; R3 report |
| NB-18 (BR-05 scratch) | WORSENED: now both tools write self-test scratch under repo root | R3 report; V31/V48 observations |
| NB-20/NB-21 (drift scope; regeneration) | OPEN/accepted | V31 bounds |
| NB-16 (docs presupposition) | check R5/R6 text | pending |
| CL-04 (C9 row-6) | proposed by V48, not written | V48 |

## NB candidates (final numbering TBD)
1. r97 fixture not freeze-pinned (chain 4/4; UNPINNED-FIXTURE exit 2) — r98 candidate (R3 residual 2; V53 obs 3).
2. r97 note receipt pins in-flight tool rev 70795150… + r96 contract 97b76bb8… (self-caveated; closure re-run) — R6 report; note text.
3. Doc parity: tools README:175 stale freeze paragraph (R2-owned; R2 addendum silent on dependency_freeze); SKILL.md:87 24 cases + "both r97 debt"; corpus/README.md:37 24 persisted cases; fixtures README no Round-97 section, census 170.
4. Calibration: dual_pointer canonical-dialect bare second token passes silently (V31 bound 2).
5. Calibration: consistent regeneration exits 0 (V31 bound 3; carried, restated in R2 README).
6. Process: BR-05 now both tools (map self-test dir=ROOT; freeze self-test dir=ROOT); transient dirs observed (V31 ~21:50:20Z; V48).
7. Host: /tmp inode exhaustion (df -i 100%); tempfile-based self-tests need TMPDIR; freeze self-test now immune (dir=ROOT) — but new scratch under repo root.
8. Docs: repaired r96 map lost standalone relation-bound sentence (V51 obs 1; V29 records) — bound survives in J11 anchor/README/scope-note; closure note candidate.
9. Depth: checker dependency blind spots (empty depends_on, wrong-but-earlier edge, deleted terminal row stay CLEAN) (V20 bounds).
10. Process: R1 report quote slip (V05 LOW): neutralized run quoted exit=1 findings=[] vs actual exit=0 findings=none.
11. Coverage/declaration: C2 claim parenthetical "digest changes by the repair" inaccurate (digest unchanged; refresh = revision/format) — R3 recorded discrepancy; LOG wording candidate.
12. Process: mutual poll-wait windows (V56: R4↔R5 ~3 min no deadlock; endgame triangle risk {V24,V35,V40}).
13. Freshness: census text stale at fixtures README:1217 (170) vs 171 (V18/V26).
14. Operability: freeze self-test no longer depends on /tmp (dir=ROOT) — improvement note; but self-test scratch not gitignored (BR-05).

## CL candidates (closure items)
- CL-01 fixtures README Round-97 + census 171/37/134/421 (V26 §3.1 precise list).
- CL-02 tools README Round-97 addendum for dependency_freeze (R3 residual 1; or R2 fix).
- CL-03 SKILL.md + corpus/README case counts (25; freeze 16; registration rows).
- CL-04 C9 watch row-6 append (V48 text; V23/V26/V48 receipts).
- CL-05 r97 note receipt re-run at delivered revision (70795150→86b52949); also r95/r96 note stale pins (NB-14 lineage).
- CL-06 LOG/SCORECARD r97 entries + declaration errata (C2 digest parenthetical; maybe the r96-map repair scope note).
- CL-07 SHONEN/fleet/receipt (L1; V36/V39).
- CL-08 host /tmp condition record (operator).
