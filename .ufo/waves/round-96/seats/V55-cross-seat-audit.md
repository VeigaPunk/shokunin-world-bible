# V55 — cross-seat-audit (round 96)

Seat V55, round 96, lore-shokunin lane. Scope per seat spec: **re-run 6 load-bearing
quoted outputs from other seats' reports; mark each REPRODUCED or MISMATCHED.** No
nested agents, no commits, no pushes, no network. Only writes: this report (absolute
path) and `.ufo/waves/round-96/seats/V55-scratch/` (captures:
`depfreeze-selftest-full.txt`, `depfreeze-selftest-r2.txt`, `map-oblig-selftest-24.txt`,
`q3red-a.txt`, `q3red-b.txt`).

Baseline r95 closure `dcb2d92`; working-tree HEAD `60dba0c` plus the round's
uncommitted producer edits. All commands run from the lane repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

Method: I read every r96 seat report as it landed, selected the quoted command/output
blocks that carry the round's declared claims (C1 before/after, C2, C3, carried
gates), re-ran each quoted command myself, and compared my observed stdout/exit
against the quoted text. Revision state is pinned per quote; where a producer was
still rewriting its artifact, that is recorded explicitly.

Revision pins at audit close (17:53-03:00): `map_obligations.py` `2b0ba815…` +
`map-obligations-contract.json` `97b76bb8…` (Q1/Q2 final), `dependency_freeze.py`
`a3b57978…` + `dependency-freeze-contract.json` `7d568cc4…` (Q3 final),
`check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`. Both producer
landings that occurred after my first six quotes (Q1 at 17:50, Q2 at 17:50/17:52)
are audited in the Addendum.

---

## Quote 1 — V34: baseline revision identity + C1(a) deletion-class demo

Source: `.ufo/waves/round-96/seats/V34-verdict-calibration.md` (lines 8–35, 47–51).
V34 quotes three baseline sha256s, the deletion-class demo (exit 0 with the
non-gating ` MISMATCH` receipt), the untouched control, and the V37-D1 demo.

My re-runs (at ~17:41, when the tree tool still carried the r95 revision
`d1c239cc…`):

```
$ git show dcb2d92:corpus/tools/map_obligations.py | sha256sum
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  -
$ git show dcb2d92:corpus/tools/map-obligations-contract.json | sha256sum
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  -
$ git show dcb2d92:corpus/tools/README.md | sha256sum
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  -

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V34-scratch/del-demo/cluster
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
RESULT PASS
EXIT=0

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V34-scratch/control/cluster
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
EXIT=0

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V34-scratch/d1-demo/cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
EXIT=0
```

All six quoted values match byte-for-byte (shas, both demo outputs, the control).
**REPRODUCED.**

## Quote 2 — V01: C1(a) four-variant baseline table

Source: `.ufo/waves/round-96/seats/V01-c1-deletion-demo.md` §Phase 1 (lines 50–75).
V01's Phase 1 runs the baseline tool copy kept in its own scratch
(`V01-scratch/old/map_obligations.py`) over pristine + three mutation copies.

My re-runs:

```
$ python3 .ufo/waves/round-96/seats/V01-scratch/old/map_obligations.py .ufo/waves/round-96/seats/V01-scratch/old/corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                      # exit 0
$ ... key+row   OBLIGATIONS raw=14 mapped=14 / INVENTORY … 16/17 MISMATCH / RESULT PASS      # exit 0
$ ... row-only  OBLIGATIONS raw=15 mapped=14 / INVENTORY … 16/17 MISMATCH
                FINDING missing_obligation: entities.json#/4/claims/0 has no map row
                RESULT FAIL       # exit 1
$ ... key-only  OBLIGATIONS raw=14 mapped=15 / INVENTORY … 17/17
                FINDING phantom_obligation: entities.json#/4/claims/0 is not a raw source-attributed obligation
                RESULT FAIL       # exit 1
```

Exact match on all four variants, including the asymmetry that only the pair
(key + row removed) is silent at exit 0. **REPRODUCED.**

## Quote 3 — V33: BR-01 gate-blindness receipts + census

Source: `.ufo/waves/round-96/seats/V33-verdict-coverage.md` §1 (lines 39–48) and §2
(lines 77–81). V33 quotes the three pre-existing fixture gates on its
`br01-reduce` copy (r94 with `evin-ninth-bell` dropped from the tick-10
`depends_on`), plus the census commands.

My re-runs:

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
CLEAN: schema, citations, relations, timeline; 0 violations      # exit 0
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS                                                      # exit 0
$ python3 corpus/tools/support_check.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
… SOURCE-SUPPORT 14/14; … MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                      # exit 0

$ git ls-tree -d --name-only dcb2d92 corpus/fixtures/ | wc -l    → 169
$ find corpus/fixtures -maxdepth 1 -mindepth 1 -type d | wc -l   → 170
```

V33's four-scenario table (reduce / add2 / endpoint-valid / endpoint-dangling) also
reproduces on the matching scratch dirs (`br01-add2` all exit 0; `br01-endpoint-valid`
all exit 0; `br01-endpoint-to` check_bible exit 1, map 0, support 0 — the bare `br01`
dir is a 1-file intermediate, not a table row). V33's independent chain-inventory
table matches my own recompute from the raw JSONs exactly (r88 `{}`; r94 one edge;
r95 two edges; r96 three edges + the tick-12 edge; same relation triple). The
`support_check` quote in V33 is a truncation ("RESULT PASS") but the load-bearing
content (exit 0, PASS) matches. **REPRODUCED.**

## Quote 4 — Q4: fixture delivery hashes, byte copies, counts, gates

Source: `.ufo/waves/round-96/seats/Q4-fixture-json.md` §1–§6. Q4 quotes the eight
delivered sha256s, five byte-copy identities vs `dcb2d92`, the r95 baseline hashes
of the extended files, `check_bible` CLEAN, counts 5/1/0/5/5 with 16 obligations,
the `map_missing` receipt while Q5's map was absent, and the r95 control.

My re-runs (fixture bytes frozen since 17:40:16; map absent at my first run):

```
$ sha256sum corpus/fixtures/r96-crossing-response/{entities,relations,contradictions}.json \
    …/{inspiration-note,source-excerpt}.md …/{sources,timeline}.json …/fictional-excerpts.md
026af0bc…2ae03b  c279254b…4a6ff9  37517e5f…985b570  58f5390e…bcc82d37  b5edc2fd…4d76d4cd
9f973f63…fabf32d  ea0225f9…08815b9  06b11bec…41cb2fe3          # all == Q4's declared set

$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    a=$(git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/$f | sha256sum | cut -d' ' -f1)
    b=$(sha256sum corpus/fixtures/r96-crossing-response/$f | cut -d' ' -f1); [ "$a" = "$b" ] && echo "$f SAME"
entities.json SAME  relations.json SAME  contradictions.json SAME  inspiration-note.md SAME  source-excerpt.md SAME

$ git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/sources.json | sha256sum → fd9e30e8…1927e64a
$ … timeline.json → 3c0faad6…b00ea177 ; … fictional-excerpts.md → 0ef6734a…0880b282

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations      # exit 0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response   # Q5 map absent
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR                                                     # exit 2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath  # control
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                      # exit 0

counts: entities 5, relations 1, contradictions 0, sources 5, timeline 5, obligations 16
```

Every quoted value matches, including the intermediate-state `map_missing` receipt.
**REPRODUCED.**

## Quote 5 — Q3: C3 chain freeze, BR-01 closure, self-test 14/14

Source: `.ufo/waves/round-96/seats/Q3-dependency-freeze.md` §2, §3, §5. Q3 quotes
the 4/4 clean chain with digests, the BR-01 closure triple (check_bible green,
map_obligations green, freeze RED), and the self-test.

My re-runs on Q3's pinned revision (`dependency_freeze.py` `a3b57978…`, contract
`7d568cc4…`):

```
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0   DIGEST 15ef230e…3fc279  PASS 0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1   DIGEST 2527beb9…cebe75  PASS 0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1 DIGEST d541ae64…6d2ec9  PASS 0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1  DIGEST d422a9b3…57d7f6  PASS 0

$ R=.ufo/waves/round-96/seats/Q3-scratch/reduction/r94-paired-crossing
$ python3 corpus/fixtures/check_bible.py $R                    → CLEAN …; 0 violations      rc=0
$ python3 corpus/tools/map_obligations.py $R                   → raw=14 mapped=14; 16/16; RESULT PASS  rc=0
$ python3 corpus/tools/dependency_freeze.py $R
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL                                                     rc=1     # two runs byte-identical (cmp)

$ python3 corpus/tools/dependency_freeze.py --self-test
… CASE lines all ok … SELF-TEST 14/14 / RESULT PASS / exit 0

$ for d in addition endpoint tamper (Q3-scratch copies of r94-paired-crossing):
ADDITION-DETECTED exit 1; ENDPOINT-CHANGE exit 1; DIGEST-MISMATCH exit 2     # exact findings as quoted
```

Q3's §4 demo table, §2 digests, §3 closure triple and §5 14/14 all match my runs.
The contract's fifth pin `c3red` (foreign scratch pin, Q3 §7) also verifies:
`FREEZE c3red: events 3/3; dependency-edges 1/1; relations 1/1; DIGEST eff4b354…;
RESULT PASS` exit 0 — reproduced.

My own independent observation of the pre-fix revision (R1, ~17:43:45, before Q3's
17:44:37 rewrite): `SELF-TEST 5/14`, `FINDING SELF-TEST-MISMATCH: cases failed:
['addition_edge_phantom', 'digest_tamper', …]`, every failing case reporting
`FILE-MISSING: timeline.json is missing from …/missing_timeline/r95-crossing-aftermath`
(the late-binding `lambda: [scratch]` closure bug). This is consistent with Q3 §5's
disclosure and V19's R1 receipt (`d17297bb…` → 5/14) and is exactly why the
delivered R2 was re-run from scratch. **REPRODUCED** (delivered revision).

## Quote 6 — V26: checker pin, boundary gates, discriminator pair, environment anomaly

Source: `.ufo/waves/round-96/seats/V26-gates-boundary.md` §0–§4, §6. V26 quotes the
pin, the boundary gate outputs, the discriminator pair, blob identities, and the
`/tmp` inode exhaustion.

My re-runs:

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py

$ python3 corpus/tools/boundary_doc_check.py
CHECK pinned inputs: PASS / CHECK receipt replay: PASS / CHECK explicit anchor ranges: PASS /
CHECK document structure: PASS / replay_receipts=3/3 / replay_cases=14/14 / anchors=2/2 /
CERTIFIED (bounded: …)                                            # exit 0
$ python3 corpus/tools/boundary_doc_check.py --self-test
… 8 case lines + final SELF-TEST PASS (9 "SELF-TEST PASS" lines)  # exit 0

$ python3 corpus/tools/discriminate_check.py
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   # exit 0
$ python3 corpus/tools/discriminate_check.py --checker e97613c
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present  # exit 2

$ echo "HEAD: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree: $(git hash-object corpus/fixtures/check_bible.py)"   → 20c56dbb…  (same)
$ echo "dcb2d92: $(git rev-parse dcb2d92:corpus/fixtures/check_bible.py)" → 20c56dbb… (same)

$ df -i /tmp | tail -1
tmpfs          1048576 1048576     0  100% /tmp
```

All V26 quoted values reproduce, including the environment anomaly (0 free inodes on
`/tmp`), which I also independently confirmed. **REPRODUCED.**

---

## Supplementary reproductions (not counted in the six)

- **V15** (`.ufo/waves/round-96/seats/V15-c2-ordering.md`): re-ran
  `V15-scratch/order_probe.py corpus/fixtures/r96-crossing-response` →
  `tick-sequence: [9, 9, 10, 11, 12] / backward-check: OK all deps strictly backward`;
  re-ran all three `chain2/` injections → exact quoted VIOLATION lines, exits 1/1/1.
  REPRODUCED.
- **V16** (`V16-c3-gate-clean.md`): re-ran `.ufo/waves/round-96/scratch/V16/compare_full.py`
  → `checks run: 84; failures: 0 / VERDICT: ALL PINS MATCH INDEPENDENT RECOMPUTE`, exit 0.
  REPRODUCED.
- **V51** (`V51-pins-c9.md`): watch pair on `r91-c1-null-chain` (1 violation) and
  `r91-c1-tick-unresolved` (3 violations) — exact quoted wording, exit 1 each;
  historical blob `git show e97613c… | sha256sum` → `e2bb9639…` as quoted. REPRODUCED.
- **V53** (`V53-byte-prefix-2.md`): `cmp` loop → five `cmp OK … byte-identical`;
  `verify_v53.py` → shared-prefix parsed-equal True, appended rows as quoted. REPRODUCED.
- **Q5** (`Q5-fixture-docs.md`): doc sha256s (`ff52ced4…`, `5093d72e…`), support_check
  `16/16 … 18/18 … 14/14 / RESULT PASS`, map_obligations `raw=16 mapped=16 / RESULT PASS`,
  check_bible CLEAN. REPRODUCED.
- **Q6** (`Q6-knowledge-note.md`): census 170, check_bible CLEAN, support/map receipts,
  byte-prefix and row inheritance. REPRODUCED.

## Addendum (17:50–17:52) — Q1/Q2 post-change quotes, landed after the six above

Q1's report `.ufo/waves/round-96/seats/Q1-tool-hardening.md` landed at 17:50; its
delivered revision (`map_obligations.py` `2b0ba815…`, 900 lines) is what I re-ran.
These quotes close the C1 post-change gap noted in §Mid-flight.

Deletion class, delivered revision (Q1 §2):

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/Q1-scratch/work/deletion-class
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
RESULT FAIL                                                      # exit 1
$ python3 .ufo/waves/round-96/seats/Q1-scratch/baseline-map_obligations.py …/deletion-class
… same OBLIGATIONS/INVENTORY lines … RESULT PASS                 # exit 0
```

V37-D1 three forms (Q1 §4) — all exact, row/line/token wording included, exit 1
each; baseline exits 0 on all three:

```
FINDING dual_pointer: row P1 (line 23) names a second pointer token 'relations.json#/0' alongside entities.json#/0/first_appearance
FINDING dual_pointer: row P2 (line 24) names a second pointer token 'entities[9].claims[0]' alongside entities.json#/1/first_appearance
FINDING dual_pointer: row T2 (line 32) names a second pointer token 'entities[9].claims[0]' alongside timeline.json#/1
```

Self-test and battery (Q1 §3, §5): `SELF-TEST CASES 22/24 pinned` → 22 case
lines PASS, `RESULT PASS`, exit 0; r88/r93/r94/r95/r96 exit 0; r87/r89 exit 2;
frozen-r93 replay `FROZEN expected=PASS/0 findings=none matched` exit 0; r96
explicit-map run exit 0. **REPRODUCED.**

**Q2 landing (17:50–17:52).** Q2's 24-case contract landed at 17:50:17
(`map-obligations-contract.json` sha `97b76bb8…`) and its report
`.ufo/waves/round-96/seats/Q2-contract-docs.md` at 17:52. Re-runs:

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
… SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
… SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
… (24 PASS lines, 0 FAIL) … RESULT PASS                          # exit 0

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/Q2-scratch/demo-del
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15
RESULT FAIL                                                      # exit 1

$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/Q2-scratch/demo-dup
FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside entities.json#/0/first_appearance
RESULT FAIL                                                      # exit 1
```

Q2's four extra `dual_pointer` probes (`demo-dup-bare-entity`, `-bare-token`,
`-canonical-token`, `-colon`) all exit 1 with the quoted token wording; its
README addendum sha `965b29cd…` and contract sha `97b76bb8…` match its report;
battery spot checks (r88, r96) exit 0. **REPRODUCED.** Q2 §1 discloses one
brief-vs-implementation divergence: the pinned `inventory_mismatch` self-test case
is an intact fixture whose map over-declares (5/0/5 vs 4 rows), not the
"claims key + row removed" mutation its brief described — the finding/exit are
identical, and the deletion-class scenario is verified separately (Q1 §2, Addendum).

## Mid-flight observations (evidence, not seat defects)

1. **Q1/Q2 landed mid-audit; the full C1 bundle is now audited.** The tool was
   rewritten several times during my window (`d1c239cc…` → `f97e4b72…` →
   `c2c284c0…` → `2b0ba815…` at 17:47:24); Q1's report landed 17:50 and Q2's
   contract/report at 17:50:17/17:52. Post-change quotes reproduce for both (see
   Addendum), including the delivered `SELF-TEST CASES 24/24 pinned` → `RESULT PASS`
   exit 0 run on contract `97b76bb8…`. One disclosed divergence: Q2 §1's
   `inventory_mismatch` pinned case is an over-declaring intact fixture, not the
   deletion mutation its brief named (same finding/exit; deletion verified separately).
2. **BR-05-class residue visible live, then self-cleaned.** At 17:53:42 `git status`
   showed an untracked `map-obligations-self-test-akn7khg_/` directory in the repo
   root — the self-test scratch under `ROOT` that Q1 §7.5 documents as transient; on
   re-check at 17:54:06 it had vanished (a concurrent seat's run, not mine). Evidence
   for the carried BR-05 residual's documented behavior (visible mid-run, cleaned on
   normal exit), not a leak.
3. **Contract pollution (C3).** `dependency-freeze-contract.json` carries a fifth pin
   `c3red` whose `fixture` field is `.ufo/waves/round-96/seats/V41-scratch/c3red`
   (a verifier scratch dir holding the BR-01 reduction). Q3 §7 and V33 §4 both report
   it; I reproduced its verify (exit 0). Pins are basename-keyed so the four chain
   pins are unaffected, but `--freeze` on an out-of-corpus copy rewrites the delivered
   contract — flagged by two seats for closure action (delete `pins.c3red` or add a
   `--freeze` scope guard).
4. **R1 self-test defect (C3) independently observed** (see Quote 5): the persisted
   expectations caught a real harness bug (5/14, exit 1) rather than passing silently;
   fixed at R2 (14/14). My capture: `V55-scratch/depfreeze-selftest-full.txt`.
5. `/tmp` inode exhaustion (1048576/1048576, 0 free) is real on this host; my captures
   were written under the lane repo scratch, not `/tmp`.

## Bounds

- I re-ran **quoted outputs**, not whole reports: claims a report makes without a
  quoted command/output were not audited here (e.g. V15's r19/r20 probe table beyond
  the three injections, V26's `stderr_bytes` bookkeeping, provenance prose).
- Verdicts are point-in-time against the revisions pinned above. All producer
  reports (Q1–Q6) landed during the audit window and their quoted outputs were
  re-run; Q1/Q2's post-change quotes were re-run on the delivered `2b0ba815…` /
  `97b76bb8…` revisions (Addendum).
- This seat asserts nothing about C1/C2/C3 claim content beyond the reproduced
  receipts, and no verdict on the round's admission.

## Bottom line

**PASS (bounded)** — 6 of 6 required load-bearing quoted outputs from other seats'
reports reproduced exactly (V34 baseline identity + deletion-class demo; V01
four-variant deletion table; V33 BR-01 gate-blindness + census; Q4 fixture
hashes/counts/gates; Q3 C3 chain + BR-01 closure + 14/14 self-test; V26
pin/gates/discriminator + /tmp anomaly), plus 8 further reproductions in the
Addendum and Supplementary sections (Q1 post-change `inventory_mismatch` exit 1
and three `dual_pointer` exit 1 forms + battery; Q2 24/24 pinned self-test +
demos; V15 ordering + injections; V16 84-check recompute; V51 watch pair + blob;
V53 preservation; Q5/Q6 receipts). No MISMATCHED verdict; one disclosed
brief-vs-implementation divergence (Q2's `inventory_mismatch` pinned case) and
two closure-worthy anomalies (foreign `c3red` pin in the C3 contract; BR-05
self-test residue) are reported, both corroborated by the producer/verifier seats.
