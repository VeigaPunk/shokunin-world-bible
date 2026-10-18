# V27 operability — running notes (round 97)

Lane root: /home/vgpnk/Projects/shokunin/lore-shokunin (session cwd = parent repo; all paths absolute).
Baseline HEAD at start: 2393934 (r96 SCORECARD closure; declaration baseline f3e09f9).
Seat: V27 operability. Scope: after producers, run every documented command in R5 README (r97 fixture),
R6 note (r97 scope note), both tools README addenda (map_obligations R2, dependency_freeze R3);
check exit contracts.

## Poll log
- poll1 (18:42:45–18:55:45, 40 tries): TIMEOUT, all six R reports absent.
- poll2 started 18:56:10.

## Landing order (mtime, observed)
- R4 r96 map cosmetic repair: 18:43:42
- r97 fixture JSON tables + copies: 18:44:16; fictional-excerpts/sources/timeline: 18:44:30
- R5 r97 map: 18:48:56; R5 r97 README: 18:49:14
- R6 note: 18:50:46
- R1 tool final write: 18:45:37 (38693 B, sha 86b52949…)
- R2 contract: 18:46:12 (3189 B, sha 2142b991…); R2 README r97 addendum: 18:47:13 (sha 6278e59b…)
- R3 tool: 18:51:24 (21001 B mid) → 18:53:00 (25044 B final)
- R3 contract: 18:53:21 (9445 B) → 18:55:14 (12025 B, r96 pin refresh through guarded path; top revision 2393934; r96 pin revision 2393934, digest unchanged d422a9b3…)
- R3 README addendum: PENDING at time of writing.

## Provisional receipts (to re-run at final freeze)
### r97 fixture replay (R5 README:26-28 / R6 note:52-60)
- check_bible → CLEAN exit 0
- support_check → INVENTORY 17/17; 2/2; 19/19; DISTINCT-ANCHORS 15/15 … SOURCE-SUPPORT 17/17; MODES 19/19; VALIDATED-ROWS 19/19 / RESULT PASS exit 0
- map_obligations → OBLIGATIONS raw=17 mapped=17 / INVENTORY 17/17; 2/2; 19/19 / RESULT PASS exit 0
- census: ls -d corpus/fixtures/*/ | wc -l = 171 (matches note)
- r96 repair receipts unchanged: check_bible CLEAN 0; support_check 16/16 PASS 0; map_obligations raw=16 mapped=16 PASS 0

### map_obligations (R2 addendum)
- --self-test → SELF-TEST CASES 25/25 pinned; 25 PASS; RESULT PASS exit 0
- loader-drop probes (scratch copies): drop schema_drift → FINDING self_test_contract: contract drops implemented self-test cases: schema_drift / RESULT ERROR exit 2; drop complete → same with 'complete' exit 2
- neutralization probe (scratch copy, second_pointer_mention→return None): SELF-TEST FAIL dual_pointer exit=0 findings=none; FINDING self_test_mismatch…; RESULT ERROR exit 2
- Unchanged battery: r88 10/10, r93 12/12, r94 14/14, r95 15/15, r96 16/16 exit 0; frozen r93 replay exit 0; r87/r89 exit 2 unsupported_map

### dependency_freeze (R3)
- --self-test → SELF-TEST 16/16 / RESULT PASS exit 0
- chain r88/r94/r95/r96: 4/4 exit 0, digests match pins (15ef230e…, 2527beb9…, d541ae64…, d422a9b3…)
- PATH-MISMATCH: same-named copy at V27-scratch/foreign → exit 2
- SCOPE-REFUSED: --freeze on scratch path → exit 2; --freeze corpus/fixtures itself → exit 2
- freeze same-named elsewhere (mirror) → SCOPE-REFUSED exit 2; legitimate refresh in mirror works (freeze+verify, exit 0)
- DIGEST-MISMATCH (mirror, inventory-neutral tamper): names timeline.json (sha256 ea0225f9→be77a509) exit 2

## Hash staleness note
R6 note cites map_obligations sha 70795150… / contract 97b76bb8…; delivered = 86b52949… / 2142b991….
Note instructs re-run against delivered revision — done; receipt counts match. Report exactly.

## Environment
- /tmp at 100% inodes observed early; mktemp worked later. No documented command has failed on /tmp so far in r97.

## Remaining at draft time
- R3 README addendum (dependency_freeze Round-97 section) — run its commands when landed.
- All six R reports (poll2 running).
- Final freeze: re-run battery, hash all artifacts, git status before/after.
