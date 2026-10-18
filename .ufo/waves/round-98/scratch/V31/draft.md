# V31 — adjudicator (round 98) — DRAFT

DRAFT STAGING ONLY. Final report goes to .ufo/waves/round-98/seats/V31-adjudicator.md.

Structure planned:
- Poll record (63-other-reports target, subtract SELF; stall-escape if any)
- Independent verification C1/C2/C3 with exact commands/outputs
- Per-axis table (calibration/coverage/depth owned; operability/freshness/adjacency witnessed)
- Conflicts reconciled (V53 vs V29; V35 vs V30/V24/V34/V52; timing ABSENTs)
- Exact conditions C-1..C-8
- Admission + bottom line

Key evidence already captured (session log):
- Baseline self-test 16/16 PASS; delivered 17/17 PASS; 16 inherited expectations value-identical; +self_test_mismatch.
- Corruption mirror: delivered rc=2 FINDING SELF-TEST-MISMATCH/RESULT ERROR vs baseline rc=1 RESULT FAIL (same mutation).
- Path-less pin: delivered MIGRATED + rc=0 digest d541ae64; baseline SCOPE-REFUSED "...already names None" rc=2.
- Precedence: all 11 code finding IDs present (programmatic check).
- Chain 6/6 PASS: r88 2/2, r94 3/3, r95 4/4, r96 5/5, r97 6/6 (digest 3c922d20), r98 7/7 (digest 59a0f4fa); pins path-bound; revision dd4df1b.
- V46 discharge: control rc=0; tick-13 edge dropped rc=1 REDUCTION-DETECTED "event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']".
- C3: 6/1/7 entities/relations/events + 7 sources; check_bible CLEAN; map_obligations raw=20 mapped=20, 20/20, 22/22; census 172; inherited parsed equality PASS (5/6/6/1/0); 19 inherited map rows identical modulo namespace; J18-J20 new.
- r95 repair: 1-line prose diff (80440d61 vs 30281ff1); receipts unchanged (map raw=15 mapped=15 PASS; freeze d541ae64 PASS; check_bible CLEAN).
- S5 hashes: map 86b52949, contract 2142b991, check_bible ff9fd2aa, support 55a5eb27 all verified; dep freeze 03d04365 matches; contract c435239d STALE (current 153ebc5b).
- Defects: S2 README :232 BR-05 "not gitignored" false (gitignore:4 *-self-test-*/; check-ignore verified); :284 "lists only" false (README.md also in diff); S5 note c435239d snapshot (V53 FAIL narrow; V29 F-2 disclosed); fixtures README census still 171 (closure item).
- Strays/hygiene: parent-root baseline-analyze.txt (105 B, 20:30:10; V24 evidence -> V57); v05-self-test-scratch (gitignored, convention deviation); V14 poll files at wave top level; /tmp scratch (~50 entries, disclosed).
- PROVINCE/SHONEN/SKILL/corpus README/fixtures README byte-identical vs 9a3d648; no commits (HEAD dd4df1b); MANIFEST.json = committed orchestrator write.
