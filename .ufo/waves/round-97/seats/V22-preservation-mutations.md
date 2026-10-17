# V22 preservation-mutations — round 97 seat report

- Seat: V22 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands run from the lane repo root with `python3`.
- Written: this report (`.ufo/waves/round-97/seats/V22-preservation-mutations.md`) plus scratch under `.ufo/waves/round-97/seats/V22-scratch/` only. No corpus writes, no commits, no network.
- Poll-wait: producers were polled on a 20 s cadence; artifacts + all six producer reports (`R1`–`R6`) were present before any verification run. Every mutant was built from the delivered bytes and the matrix was re-run at the end against the final revision.
- Delivered revisions measured: `map_obligations.py` sha256 `86b52949…`, `support_check.py` `55a5eb27…`, `dependency_freeze.py` `b06275f3…`, r97 map `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f`, r97 `timeline.json` `73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b`.

## Method

11 mutants, each a full copy of the delivered `corpus/fixtures/r97-crossing-acknowledgment` with exactly one preservation violation, built by `.ufo/waves/round-97/seats/V22-scratch/mutate.py` into `V22-scratch/mutants/`:

```
$ python3 .ufo/waves/round-97/seats/V22-scratch/mutate.py
MUTANT m1-span-break: last JSON-facts row span 44-53 -> 1 (anchor now outside span)
MUTANT m1b-span-off-by-one: first single-line row J01 span 12 -> 13
MUTANT m2-row-drop: last JSON-facts row deleted; declaration untouched
MUTANT m2b-row-drop-declared: last row deleted + declaration downgraded
MUTANT m3-key-row-deletion: timeline.json record acknowledgment-aru-records deleted + its map row deleted; declaration untouched
MUTANT m3c-key-row-deletion-declared: record acknowledgment-aru-records + row deleted + declaration downgraded (self-consistent tamper)
MUTANT m3d-key-row-deletion-fully-declared: record acknowledgment-aru-records + row deleted + facts/rows/anchors all downgraded
MUTANT m4-deps-reduction: timeline.json record acknowledgment-aru-records depends_on ['response-evin-salt-court'] -> []
MUTANT m5a-legacy-token-canonical: canonical cell `timeline.json#/5` (...) -> legacy token
MUTANT m5b-hidden-second-pointer-canonical: hidden second pointer injected into canonical cell
MUTANT m5c-legacy-form-hidden-pointer: map switched to legacy pointer grammar + last row carries a hidden second pointer
```

Baseline on the delivered fixture, canonical corpus path:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; … VALIDATED-ROWS 19/19
RESULT PASS                                  exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                  exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' in corpus/tools/dependency-freeze-contract.json
RESULT ERROR                                 exit=2   # by design: chain is r88/r94/r95/r96 (R3 report, residual 2)
```

## Mutation matrix (delivered revision)

`S=.ufo/waves/round-97/seats/V22-scratch`; each row: `python3 corpus/tools/support_check.py $S/mutants/<m>` / `python3 corpus/tools/map_obligations.py $S/mutants/<m>` (freeze column from the harness below).

| mutant | support | map | freeze | quoted finding |
|---|---:|---:|---:|---|
| m1 span break (J17 44-53→1) | 1 | 0 | — | `FAIL J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.; span=1; outside-span=48` / `FAIL: J17: anchor hit outside declared line span 1 (hit lines: 48)` |
| m1b span off-by-one (J01 12→13) | 1 | 0 | — | `FAIL J01: … span=13; outside-span=12` / `FAIL: J01: anchor hit outside declared line span 13 (hit lines: 12)` |
| m2 row drop (declaration untouched) | 1 | 1 | — | map `INVENTORY JSON-FACTS 16/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/19 MISMATCH` / `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 17/2/19; observed 16/2/18` / `FINDING missing_obligation: timeline.json#/5 has no map row` |
| m2b row drop + declaration 16/2/18 | 1 | 1 | — | map `FINDING missing_obligation: timeline.json#/5 has no map row`; support `FAIL: inventory distinct excerpt anchors mismatch: expected=15 parsed=14` |
| m3 key+row deletion (declaration untouched) | 1 | 1 | — | map `FINDING inventory_mismatch: declared … 17/2/19; observed 16/2/18` |
| m3c + declaration 16/2/18 | 1 | 0 | — | support `FAIL: inventory distinct excerpt anchors mismatch: expected=15 parsed=14` |
| m3d fully self-consistent deletion | 0 | 0 | 1 | freeze `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records is missing; 1 frozen dependency edge(s) gone` |
| m4 depends_on reduction (map untouched) | 0 | 0 | 1 | freeze `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` |
| m5a legacy token in canonical cell | 0 | 2 | — | `FINDING unsupported_map: co-mapped or unsupported pointer grammar` |
| m5b hidden second pointer in canonical note | 0 | 2 | — | `FINDING unsupported_map: co-mapped or unsupported pointer grammar` |
| m5c legacy-form map + hidden second pointer | 0 | 1 | — | `FINDING dual_pointer: row J17 (line 38) names a second pointer token 'relations.json#/0' alongside timeline.json#/5` |

Every row was also run in the earlier pass at ~18:51 with identical exits; the final pass above is the recorded one. Exits were captured without pipes (`python3 … > out.txt 2>&1; echo exit=$?`).

Interpretation, kept to what was measured:

- Span class lives only in `support_check` (map exits 0 on m1/m1b): a wrong span is invisible to the pointer/inventory model and visible only to the anchor-span gate. J17's declared span is 44-53 with the anchor at line 48.
- Row drop is caught twice over when the declaration is untouched (gating `inventory_mismatch` + `missing_obligation`), and once (`missing_obligation`) when the declaration is downgraded.
- Key+row deletion is the r96 `inventory_mismatch` class reproduced on r97: deleting both sides without touching the declaration exits 1.
- The two self-consistent tampers (m3d fully downgraded; m4 edge-only) pass **both** map and support tools (0/0) and are caught only by the frozen inventory (exit 1) — that is the preservation argument for the freeze pin, and the reason the r97 fixture being unpinned (below) matters.

## Freeze half on r97 copies (mirror-root harness)

`dependency_freeze.py` pins are keyed by directory basename and the delivered pin binds the canonical corpus path; verifier seats may not write under `corpus/`. So `V22-scratch/freeze-harness.sh` copies the delivered tool + contract byte-for-byte into a scratch ROOT and pins three r97 copies **through the guarded `--freeze` path**, then mutates in place:

```
delivered tool sha: b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130
harness  tool sha: b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130
$ python3 $H/corpus/tools/dependency_freeze.py --freeze $H/corpus/fixtures/r97-clean
FROZEN r97-clean: events 6; dependency-edges 5; relations 1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS                                  exit=0
$ python3 $H/corpus/tools/dependency_freeze.py $H/corpus/fixtures/r97-clean
FREEZE r97-clean: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS                                  exit=0
# after in-place mutation of the two pinned copies:
$ python3 $H/corpus/tools/dependency_freeze.py $H/corpus/fixtures/r97-deps-reduction
FREEZE r97-deps-reduction: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                  exit=1
$ python3 $H/corpus/tools/dependency_freeze.py $H/corpus/fixtures/r97-key-row-deleted
FREEZE r97-key-row-deleted: events 5/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records is missing; 1 frozen dependency edge(s) gone
RESULT FAIL                                  exit=1
```

On the same two copies the delivered map/support tools exit 0 (`OBLIGATIONS raw=16/17 … RESULT PASS`), i.e. the freeze pin is the only gate that sees them. R3's report (residual 3) states this mirror-root property is intended — binding is to the running tool's own `ROOT` — so the harness measures the delivered logic, not a weakened copy.

Bonus row on the same harness: a title-case-only byte change in `sources.json` of a pinned copy exits 2 with the file named —

```
FINDING DIGEST-MISMATCH: content digest 3a7c6346… != pin 3c922d20…; changed: sources.json (sha256 438fb513… -> eb539638…); fixture bytes changed outside the frozen inventory
RESULT ERROR                                 exit=2
```

## Hidden second pointer: N/A on the delivered map, class demonstrated

The delivered r97 map is canonical-form — `claim-excerpt-map.md:20` header cell is `JSON fact pointer and fields`, not the legacy `json fact and fields`. In canonical mode `parse_pointer_cell(..., legacy=False)` returns no second-pointer mention, so the `dual_pointer` gate is structurally unreachable on the delivered bytes: the hidden-second-pointer mutation is **N/A for this map by construction**, and the equivalent injection is refused as an error instead of passing silently (m5a/m5b, exit 2). To show the r96-added gate is load-bearing rather than dead code, m5c converts a copy's header to legacy grammar and injects `` `timeline[5]` (also `relations.json#/0`) ``: the tool maps the row to `timeline.json#/5` and flags `dual_pointer` (exit 1). Context receipts: `map_obligations.py --self-test` ends `SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']` / `RESULT PASS` (25 cases, exit 0).

## Path binding before/after (supporting evidence for the freeze half)

Pre-hardening tool = HEAD bytes, sha256 `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` (captured at 18:41, before R3's edit landed), on a byte-identical foreign-path copy of r96:

```
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
RESULT PASS                                  exit=0
```

Delivered tool, same trick, plus the scope guard:

```
$ python3 corpus/tools/dependency_freeze.py $S/foreign/r96-crossing-response
FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/V22-scratch/foreign/r96-crossing-response
RESULT ERROR                                 exit=2
$ python3 corpus/tools/dependency_freeze.py $S/foreign/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' …   exit=2   # no r97 pin exists to bind against
$ python3 corpus/tools/dependency_freeze.py --freeze $S/harness/corpus/fixtures/r97-clean
FINDING SCOPE-REFUSED: --freeze refuses …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR                                 exit=2
```

So the foreign-copy class is closed for every pinned fixture (r96 shown); for r97 the delivered revision returns `UNPINNED-FIXTURE` rather than `PATH-MISMATCH`, because r97 is not in the contract's pin set.

## Residuals and notes

1. **r97 is unpinned in the delivered contract** (pins: `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`). The declared C2 chain is "4/4 clean" and R3's residual 2 records r97 as an r98 candidate. Consequence for preservation: on the delivered revision, the freeze half of the r97 preservation argument is exercisable only through a mirror-root pin (as done here); nothing in the delivered tree would catch m3d/m4 on `corpus/fixtures/r97-crossing-acknowledgment` today.
2. **Corroboration of R3's measured discrepancy:** at 18:43, before R3's refresh, the r96 verify digest was already `d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6`, and the contract's post-refresh r96 pin `content_sha256` is still `d422a9b3…` — R4's cosmetic repair did not move the freeze digest (the map is not in `DATA_FILES`). The refresh is a guard/revision refresh, as R3 reports.
3. Map formatting carried into r97 is the repaired form: JSON-facts delimiter `claim-excerpt-map.md:21` has 8 cells for the 8-column table, the editorial delimiter `:45` has 7 cells for the 7-column table, and the stale "new relation" sentence is absent (`grep` returns nothing).
4. Not re-measured here (other seats' scope): census counts, `check_bible`, r96 receipts, the map self-test loader tightening beyond the `dual_pointer` receipt quoted above.
5. Environment: the earlier `dependency_freeze.py --self-test` on the pre-round contract failed mid-flight (`self_test.expected` count changed 14→16 under me); all quoted self-test receipts are from the final revision.

## Bottom line

**PASS** — on the delivered revision, all five preservation-mutation classes reproduce on r97 copies with quoted exits: span break → `support_check` exit 1 (map exit 0); row drop → `map_obligations` exit 1 (`inventory_mismatch` + `missing_obligation`, or `missing_obligation` alone with a downgraded declaration); key+row deletion → `inventory_mismatch` exit 1; depends_on reduction → `REDUCTION-DETECTED` exit 1 (and the fully self-consistent deletion → `REDUCTION-DETECTED` exit 1), both invisible to the map/support pair (0/0); hidden second pointer → **N/A on the delivered canonical-form map by construction**, with the canonical analogue exiting 2 (`unsupported_map`) and a legacy-form copy exiting 1 (`dual_pointer`, gate load-bearing); caveat recorded — the r97 fixture is unpinned in the delivered contract, so its freeze half was measured through a mirror-root pin created by the delivered tool's own guarded `--freeze`.
