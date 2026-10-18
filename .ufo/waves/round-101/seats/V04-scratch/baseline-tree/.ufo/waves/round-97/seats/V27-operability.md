# V27 — operability (round 97)

Seat: V27 operability. Exclusive write scope: this report plus
`.ufo/waves/round-97/seats/V27-scratch/` (all absolute under the lane repo; the session cwd is the
parent repo). No product file written, no commit, no push, no network, no nested agents. All
commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`
(3.14.7). Baseline: r96 closure `f3e09f9`; `git log --oneline -1` at start →
`2393934 lore r96: close round — SCORECARD admitted section`.

Task as seated: after the producers land, run **every documented command in R5's r97 fixture
README, R6's r97 knowledge note, and the two tools README Round-97 addenda exactly as written**,
check the 0/1/2 exit contracts, and report failures/absences as written. Never verify a plan.

## 0. Poll-wait, landing order, frozen revision

Two background polls (20 s cadence). **Poll defect, self-recorded:** the first poll matched only
`R1.md … R6.md`; the delivered reports use slugged names (`R1-map-pinning.md`,
`R2-contract-docs.md`, `R3-freeze-hardening.md`, `R4-fixture-author.md`, `R5-fixture-docs.md`,
`R6-knowledge-note.md`), so it reported the producers absent while five of six reports were
already on disk. Presence confirmed by directory listing at 19:00:24; only R3's report (18:56:23)
landed after the last poll check that mattered. No artifact was verified before it existed.

Landing order (mtime, observed):

| Artifact | Landed |
|---|---|
| R4 r96 cosmetic repair (`claim-excerpt-map.md`) | 18:43:42 |
| r97 fixture JSON tables + byte copies | 18:44:16–18:44:30 |
| R1 `map_obligations.py` (final write) | 18:45:37 |
| R2 `map-obligations-contract.json` / tools README Round-97 addendum | 18:46:12 / 18:47:13 |
| R5 r97 `claim-excerpt-map.md` / `README.md` | 18:48:56 / 18:49:14 |
| R6 `r97-acknowledgment-scope-note.md` (final revision) | 18:52:38 |
| R3 `dependency_freeze.py` / contract (pre-refresh) | 18:53:00 / 18:53:21 |
| R3 contract (r96 pin refresh through guarded path) | 18:55:14 |
| Reports: R2 18:49:31 · R4 18:50:14 · R5 18:51:25 · R1 18:52:25 · R6 18:53:37 · R3 18:56:23 | |

Every producer artifact's mtime precedes that producer's report. Frozen revision for every
receipt below (sha256; re-verified **after** all runs — identical, `diff hashes-before.txt
hashes-after.txt` → clean):

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md
```

These match the producers' own cited revisions (R1/R2: `86b52949…`/`2142b991…`; R3:
`b06275f3…`/`27273be2…`). Transcript: `V27-scratch/final-transcript.txt` (334 lines; every
command below captured with stdout+stderr and true exit code — no pipelines in the harness, after
the r96 lesson that `cmd | tail` masks the tool's exit with `tail`'s).

## 1. R5 fixture README replay block (README.md:25–29) — run exactly as written

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations                  EXIT=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… PASS J01–J17, PASS S01, PASS S02 …
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                                  EXIT=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                                  EXIT=0
```

README count claims reproduce: README:21 "17 source-attributed JSON pointer obligations" →
`raw=17 mapped=17`; README:3 "5 entities / 1 relation / 6 events / 6 sources" → `json.load`
counts `5 1 6 6 0` (contradictions `[]`); tick-13 row =
`('acknowledgment-aru-records', 13, 'aru', 'chalk-stair', ['response-evin-salt-court'], 'aru-acknowledgment-note')`.

## 2. R6 knowledge-note receipts block (note:51–61) — run exactly as written

Same three commands; every quoted receipt line matches verbatim (see §1). The note's own census
claim also reproduces: `ls -d corpus/fixtures/*/ | wc -l` → **171** (170 at r96 closure).

Revision-citation note, reported exactly: the note's final revision cites `map_obligations.py`
`86b52949…` (the delivered hash) and records that an earlier run the same pass at `70795150…`
gave the identical r97 result ("this tool was still moving during the round — re-run against the
closure revision"). That re-run is this pass; receipts unchanged. No fabricated receipt found in
the note.

## 3. Retained r96 replay (README r96:26–28, re-run after R4's repair)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations                  EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18 / RESULT PASS  EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16 / INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18 / RESULT PASS  EXIT=0
```

r96 receipts unchanged by the cosmetic repair, as the round claims.

## 4. Tools README Round-97 addendum — `map_obligations` (README:177–224)

Documented command, run as written:

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
… 25 × "SELF-TEST PASS <case> exit=<0|1|2> findings=[…]" (incl. dual_pointer exit=1 ['dual_pointer']) …
RESULT PASS                                                                  EXIT=0
```

The 25 printed cases match the persisted contract set exactly (25 `"id"` entries; no
missing/extra; exits and finding sets match). The addendum's prose demos were reproduced on
scratch copies (delivered files never mutated; the loader reads the contract from the tool's own
directory, so each probe moved a byte-identical tool copy next to a scratch contract copy):

```
loader, drop 'schema_drift'      FINDING self_test_contract: contract drops implemented self-test cases: schema_drift  / RESULT ERROR  EXIT=2
loader, drop core 'complete'     FINDING self_test_contract: contract drops implemented self-test cases: complete        / RESULT ERROR  EXIT=2
loader, extra unimplemented case FINDING self_test_contract: contract pins unimplemented self-test cases: no_such_case  / RESULT ERROR  EXIT=2
neutralize second_pointer_mention (scratch copy)
                                 SELF-TEST FAIL dual_pointer exit=0 findings=none
                                 FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
                                 RESULT ERROR                                                            EXIT=2
```

The pin is load-bearing; the r96 subset tolerance is closed for added and core pins. The
addendum's hand-derived expectation for the 25th case was reproduced on a scratch fixture of the
documented shape (legacy header, rows E1/E2/R1/T1):

```
$ python3 corpus/tools/map_obligations.py …/handderive-dual
OBLIGATIONS raw=4 mapped=4
FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL                                                                  EXIT=1
$ python3 corpus/tools/map_obligations.py …/handderive-clean
OBLIGATIONS raw=4 mapped=4 / RESULT PASS                                     EXIT=0
```

"Unchanged" claims, each re-run on the delivered revision:

```
r88-m3-maya-cluster      raw=10 mapped=10 / INVENTORY 10/10; 2/2; 12/12 / RESULT PASS  EXIT=0
r93-m2-kojiki-cluster    raw=12 mapped=12 / INVENTORY 12/12; 3/3; 15/15 / RESULT PASS  EXIT=0
r94-paired-crossing      raw=14 mapped=14 / INVENTORY 14/14; 2/2; 16/16 / RESULT PASS  EXIT=0
r95-crossing-aftermath   raw=15 mapped=15 / INVENTORY 15/15; 2/2; 17/17 / RESULT PASS  EXIT=0
r96-crossing-response    raw=16 mapped=16 / INVENTORY 16/16; 2/2; 18/18 / RESULT PASS  EXIT=0
--frozen .ufo/waves/round-94/frozen/map-obligations-r93
                         SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS  EXIT=0
r87-myth-cluster         FINDING unsupported_map … / RESULT ERROR  EXIT=2
r89-inspiration-paraphrase  FINDING unsupported_map … / RESULT ERROR  EXIT=2
```

## 5. Tools README Round-97 addendum for `dependency_freeze` — ABSENT (finding)

`corpus/tools/README.md` gained **only** the map_obligations Round-97 section. The
dependency_freeze documentation surface is still the Round-96 paragraph (README:175), which is
**stale against the delivered tool**:

- README:175 says self-test "(14/14, persisted in the contract)" — the delivered tool prints
  **16/16**;
- README:175's "Hazards (r97 debt)" lists all three hazards as open — all three are closed in the
  delivered revision (scope guard, path binding, digest naming);
- the new stable FINDING IDs `SCOPE-REFUSED` and `PATH-MISMATCH` (and the out-of-scope-pin
  `CONTRACT-INVALID`) are documented nowhere in the README.

R3's own report records this as an open doc-parity item (§Residuals.1: "README is stale and is
not mine to write … R2's report does not mention `dependency_freeze` at all"); R2's report
(§Observations.1) flags other stale docs (SKILL.md, corpus/README.md) but not this one. Reported
exactly: the second Round-97 tools README addendum is **absent**; the commands themselves still
run (below), but the only in-repo documented expected output for them is wrong.

I ran the dependency_freeze commands from the delivered README entry sentence, `--help`, and the
contract's `exit_codes`/`self_test` blocks — the delivered documentation surfaces:

```
$ python3 corpus/tools/dependency_freeze.py --self-test
… 16 × "CASE <case>: exit=<0|1|2> expected=<…> findings=[…] ok" (incl. scope_refused, path_mismatch) …
SELF-TEST 16/16
RESULT PASS                                                                  EXIT=0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0 / DIGEST 15ef230e… / RESULT PASS  EXIT=0
r94-paired-crossing      events 3/3; 2/2; 1/1 / DIGEST 2527beb9… / RESULT PASS  EXIT=0
r95-crossing-aftermath   events 4/4; 3/3; 1/1 / DIGEST d541ae64… / RESULT PASS  EXIT=0
r96-crossing-response    events 5/5; 4/4; 1/1 / DIGEST d422a9b3… / RESULT PASS  EXIT=0
```

Each printed digest equals the corresponding `content_sha256` pin. Exit-contract probes (scratch
copies / mirrored roots; the delivered contract was never at risk):

```
foreign same-named copy of r96 (V27-scratch/foreign/r96-crossing-response)
    FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …); invoked fixture resolves to …  / RESULT ERROR  EXIT=2
--freeze on that foreign path (and on corpus/fixtures itself)
    FINDING SCOPE-REFUSED: … the frozen scope is corpus/fixtures/** (integration-time operation only)  / RESULT ERROR  EXIT=2
mirror: --freeze same-named copy at another in-scope path
    FINDING SCOPE-REFUSED: … pin r96-crossing-response already names 'corpus/fixtures/r96-crossing-response' …  EXIT=2
mirror: legitimate --freeze corpus/fixtures/r96-crossing-response
    FROZEN r96-crossing-response: events 5; dependency-edges 4; relations 1 / DIGEST … / RESULT PASS  EXIT=0
mirror: inventory-neutral prose tamper (timeline.json case change)
    FINDING DIGEST-MISMATCH: … changed: timeline.json (sha256 ea0225f9… -> be77a509…) …  / RESULT ERROR  EXIT=2
r97-crossing-acknowledgment (unpinned by design)
    FINDING UNPINNED-FIXTURE … (pinned: ['r88-m3-maya-cluster','r94-paired-crossing','r95-crossing-aftermath','r96-crossing-response'])  EXIT=2
```

Pin refresh through the guarded path, as claimed: the delivered contract now records top-level
revision `2393934237ea076366f3db6dceeff033edb52ab1` and the r96 pin's revision likewise;
`pins.r96-crossing-response.content_sha256` is **unchanged** (`d422a9b3…`) — the repair touched
only `claim-excerpt-map.md`, which is not one of the tool's `DATA_FILES`. R3's report records the
same measured discrepancy against the claim's "digest changes by the repair" parenthetical. Pins
count 4/4 (no stray `c3red`).

## 6. Exit contract 0/1/2 on the claimed paths

| Path (as documented) | Documented | Observed exit | Terminal line |
|---|---|---|---|
| r97 fixture (R5 README, R6 note) | 0 | 0 | `RESULT PASS` / `CLEAN` |
| r96 fixture (retained README) | 0 | 0 | `RESULT PASS` |
| r88 / r93 / r94 / r95 (addendum "Unchanged") | 0 | 0 | `RESULT PASS` |
| `--frozen` r93 snapshot | 0 | 0 | `RESULT PASS` |
| r87 / r89 | 2 | 2 | `RESULT ERROR` (`unsupported_map`) |
| `map_obligations --self-test` | 0 | 0 | `RESULT PASS` (25/25) |
| map_obligations loader drops / unimplemented case / neutralization | 2 | 2 | `RESULT ERROR` |
| dependency_freeze chain ×4 / `--self-test` | 0 | 0 | `RESULT PASS` (16/16) |
| dependency_freeze SCOPE-REFUSED / PATH-MISMATCH / DIGEST-MISMATCH / UNPINNED | 2 | 2 | `RESULT ERROR` |

Usage probes: map_obligations no-args / `--self-test`+cluster / `--bogus` → `FINDING
invalid_arguments …` EXIT=2; dependency_freeze no-args / `--self-test`+fixture → `FINDING
INVALID-ARGUMENTS …` EXIT=2. `--help` on both tools: EXIT=0 with **zero** RESULT lines.
Retained documented commands still run: `support_check` r87 `14/14 … MODES 22/22` PASS exit 0,
r88 `10/10 … 12/12` PASS exit 0; `discriminate_check.py` → `RESULT: DISCRIMINATION HELD` exit 0
and `--checker e97613c` → `REGRESSION-DETECTED` exit 2; `boundary_doc_check.py` → `CERTIFIED …`
exit 0 and `--self-test` → `SELF-TEST PASS` exit 0.

## 7. Environment

`/tmp` was inode-exhausted early in the wave (`df -i /tmp` at 18:44 → `1048576 1048576 0 100%`,
matching the r96 host note) and recovered during the round (19:0x → `15696 / 1032880 / 2%`).
Unlike r96, no documented command was wrong-reason-passed by it: the tools README's r93-addendum
`mktemp` negative control ran **as written** and produced the documented outcome —

```
$ tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT; cp corpus/knowledge/holder-assessment-boundary.md "$tmp"; printf '\nDeliberate R05 pin-drift probe.\n' >> "$tmp"; python3 corpus/tools/boundary_doc_check.py --doc "$tmp"; rc=$?; printf 'observed_exit=%s\n' "$rc"; test "$rc" -eq 1
CHECK pinned inputs: FAIL
FINDING document_drift: document digest differs from pinned 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e bytes
CERTIFICATION FAIL
observed_exit=1            (script assertion passes)
```

Both self-tests now create scratch under the repo root (`dir=ROOT`), so they no longer depend on
the system temp dir.

## 8. Preservation and residue

- `git status --porcelain` before and after the whole replay is identical
  (`V27-scratch/git-status-before.txt` vs `-after.txt`, `diff` clean): ` M LOG.md`,
  ` M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`,
  ` M corpus/tools/{README.md,dependency-freeze-contract.json,dependency_freeze.py,map-obligations-contract.json,map_obligations.py}`,
  `?? .ufo/waves/round-97/`, `?? corpus/fixtures/r97-crossing-acknowledgment/`,
  `?? corpus/knowledge/r97-acknowledgment-scope-note.md`. No corpus modification by this seat.
- All frozen hashes re-verified identical after the runs (§0). No leftover self-test scratch:
  `ls -d map-obligations-self-test-* dependency-freeze-self-test-*` → none.
- Every scratch probe (loader copies, neutralized tool, hand-derived fixtures, foreign copy,
  mirrored roots) lives under `V27-scratch/`; the delivered contract and all corpus files were
  never written by this seat.

## Findings summary (all failures/absences reported exactly)

1. **Round-97 `dependency_freeze` tools README addendum ABSENT.** `corpus/tools/README.md` has
   only the map_obligations Round-97 section; README:175 (Round-96) still claims self-test
   "14/14" and lists all three closed hazards as open, and the new stable FINDING IDs
   (`SCOPE-REFUSED`, `PATH-MISMATCH`) are undocumented. The commands themselves run and pass
   (16/16, chain 4/4, all probes); the documented expected output is stale. R3's report flags the
   same doc-parity item (README is R2-owned).
2. **Claim parenthetical vs measurement (recorded, R3-owned):** the round claim says the r96 pin
   refresh is needed because "the digest changes by the repair"; measured, the digest is
   unchanged (`d422a9b3…`) — the repair touched only the map, not `DATA_FILES`. The refresh
   (revision fields through the guarded path) works and the chain re-verifies 4/4 clean.
3. **R6 note revision citations:** the note's final revision correctly cites the delivered tool
   hash `86b52949…` and transparently records the earlier mid-flight `70795150…`; the
   delivered-revision re-run reproduces every receipt. No action.
4. **Environment:** early `/tmp` inode exhaustion (100% at 18:44, recovered to 2% by 19:0x) — no
   documented command failed on it this round; the r93-addendum `mktemp` control produced the
   documented `FINDING document_drift` exit 1.
5. No other documented command failed as written: R5 README (3 commands), R6 note (3 commands +
   census), the tools README Round-97 map_obligations addendum (self-test 25/25, loader and
   neutralization probes, hand-derived fixture, five clean corpus paths, frozen replay, r87/r89
   fail-closed), the retained r96 replay (unchanged receipts), and the retained r93/r94/r95
   addendum commands all reproduce their documented output and exit codes on the frozen revision.

## Bottom line

PASS — every documented command in R5's r97 README, R6's r97 note, and the tools README Round-97
addendum runs as written on the frozen revision (r97 `raw=17 mapped=17` CLEAN/PASS exit 0; 25/25
and 16/16 self-tests; dependency_freeze chain 4/4; loader/scope/path/digest probes exit 0/1/2 as
contracted; r96 replay unchanged), with two reported operability gaps: the Round-97
`dependency_freeze` README addendum is absent and README:175 is stale (14/14 + open hazards), and
the claim's digest-change parenthetical for the r96 pin refresh does not match measurement
(digest unchanged; recorded by R3 too).
