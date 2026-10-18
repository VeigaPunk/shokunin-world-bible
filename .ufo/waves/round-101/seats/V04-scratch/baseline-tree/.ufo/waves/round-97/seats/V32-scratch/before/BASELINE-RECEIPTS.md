# V32 baseline "before" receipts — r97 pre-state at HEAD 2393934 (r96 closure)

C1 map drop-protection (copied tree V32-scratch/before/map-tree):
  drop schema_drift        -> SELF-TEST CASES 23/24 pinned / RESULT PASS  exit=0  (fail-open)
  drop inventory_mismatch  -> SELF-TEST CASES 23/24 pinned / RESULT PASS  exit=0  (fail-open)
  drop phantom (core)      -> FINDING self_test_contract: contract drops implemented self-test cases: phantom / RESULT ERROR exit=2
  restored                 -> SELF-TEST CASES 24/24 pinned / RESULT PASS exit=0
  contract ids (24): complete missing duplicate phantom source_id_mismatch schema_drift inventory_mismatch malformed_json
    co_mapped_grammar legacy_grammar invalid_pointer empty_segment noncanonical_index noncanonical_claim_index
    foreign_path traversal_path symlink_path frozen_complete frozen_tampered frozen_missing_digests
    frozen_expected_failure frozen_verdict_mismatch map_missing invalid_arguments   (NO dual_pointer)

C2 dep path binding (live tool, read-only): V32-scratch/foreign/r94-paired-crossing (same basename, foreign path)
  -> FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1 / DIGEST 2527beb9… / RESULT PASS exit=0  (verifies identically)

C2 DIGEST-MISMATCH wording (V32-scratch/foreign2/r94-paired-crossing, timeline.json trailing newline):
  -> FINDING DIGEST-MISMATCH: content digest ed435293… != pin 2527beb9…; fixture bytes changed outside the frozen inventory / RESULT ERROR exit=2   (no filename named)

C2 --freeze scope (copied tree V32-scratch/before/dep-tree, out-of-corpus target):
  -> FROZEN v32-probe-src: events 3; dependency-edges 2; relations 1 / RESULT PASS exit=0; copy contract pins 4 -> 5 (v32-probe-src added)   (no scope guard)

Chain baseline (live tools, read-only):
  dep verify: r88 DIGEST 15ef230e… PASS 0; r94 DIGEST 2527beb9… PASS 0; r95 DIGEST d541ae64… PASS 0; r96 DIGEST d422a9b3… PASS 0
  map: r88 raw=10 mapped=10 / 10/10;2/2;12/12 PASS 0 | r93 12/12 12/12;3/3;15/15 PASS 0 | r94 14/14 14/14;2/2;16/16 PASS 0
       r95 15/15 15/15;2/2;17/17 PASS 0 | r96 16/16 16/16;2/2;18/18 PASS 0
  self-tests: map 24/24 PASS exit=0; dep 14/14 PASS exit=0
  dep contract pins (4): r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response (c3red removed at closure)
  dep contract self_test.expected n=14
  baseline hashes: map_obligations 2b0ba815… map-contract 97b76bb8… tools/README ba7d2ff1… dep_tool a3b57978… dep-contract c65ac3bd… r96-map 5093d72e…
  r96 map blemishes (pre-repair): line 43 header 7 cells vs line 44 delimiter 8 cells; line 50 sentence "The new relation encodes only the agreement for this crossing…"
