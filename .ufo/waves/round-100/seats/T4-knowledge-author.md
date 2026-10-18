# T4 — knowledge author (2026-10-17)

Scope: round-100 C2 component 2 and C3 knowledge records only, against r99 closure `fe1ce46` with the round-100 wave tree delivered in place. Axes: depth (complete arc docket and preserved unresolved status), calibration (byte detection separated from meaning and three replayed corrections), freshness (dated supersessions), operability/adjacency (real gate replays and exclusive ownership). This is an author-seat receipt, not independent admission of the round.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; all Python commands used `python3`. No nested agents, network, commits, pushes, live fixture mutations, live contract writes, or writes outside the owned paths and declared scratch.

## Delivered files

- `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r100-crossing-arc-synthesis.md`: seven-record docket, r94 seed plus six continuation beats r95–r100; per-record fixture/event/source pointers and E/R/T/source/obligation counts; exact unresolved-throughout temporal scope; testimony/chronology/editorial tick-and-ID/rights/permission bounds; all-beat preservation and delivered-revision gate receipts. Explicitly distinguishes the seven dossier snapshots from the different seven frozen fixtures.
- `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r100-provenance-semantics-boundary.md`: the full-file pin's identity/detectability/path/named-file/semantic-inventory precedence guarantees and non-guarantees; r99 AC-1/AC-2/AC-3 citations; the historical r98 prose bound in row 6; freshly replayed controls. “Semantic inventory” is modeled JSON comparison, not natural-language semantics.
- `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge/r99-gate-blind-spot-table.md:272-375`: append-only dated addendum with rows 10, 11, 12 (each `2026-10-17 / r100`), explicit mutations, actual commands, observed outputs/exits, and a dated current-coverage supersession. All 20,526 baseline bytes remain an exact prefix; historical rows were not rewritten. Added bytes: 8,907.
- `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T4-knowledge-author.md`: this exclusive report.
- Declared scratch only: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T4-scratch/`. The exhaustive scratch-file path list is `file-manifest.json` there. It contains three audit/replay scripts, generated output/JSON receipts, five isolated tool/contract/fixture mirrors, and the map self-test receipt. Self-test temporary trees were automatically removed inside this scratch root; no archive or repo-root temporary was created by this seat.

No `AGENTS.md` exists in the lane or its subdirectories (initial direct Read and Glob checks); no project instruction file required updating. Only the three owned corpus knowledge paths above were written by T4.

Final delivered SHA-256 values:

```text
r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
r99-gate-blind-spot-table.md f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
```

## Producer wait and naming bounds

T2 artifacts and its actual report `.ufo/waves/round-100/seats/T2-fixture-author.md` were required, then read. The 20-second / 40-try poll completed at attempt 6 (100 seconds); observed final lines:

```text
POLL 6/40 T2_reports=['T2-fixture-author.md'] missing=[]
READY artifacts+T2-report exist
```

T3's completed README/map and `.ufo/waves/round-100/seats/T3-fixture-docs.md` were also required before the final 21-gate arc replay. Its independent 20-second / 40-try poll completed at attempt 7 (120 seconds):

```text
POLL 7/40 T3_reports=['T3-fixture-docs.md'] artifacts=True
READY artifacts+T3-report exist
```

Both reports and delivered artifacts were read; no plan was accepted as implementation. No all-reports poll, self-inclusive wait, timeout, or stall escape was used. Both background polls completed before this report; no needed background task remains.

Two literal naming issues are resolved explicitly rather than hidden:

- The requested “six-beat” list includes seven snapshots. The prior notes call r98 the fourth continuation and r99 the fifth; the synthesis therefore calls r94 the seed plus r95–r100 six continuation beats and retains all seven records.
- There is no separate r98 blind-spot-table file in `corpus/knowledge/`. The historical r98 prose limitation is preserved in row 6 of the existing `r99-gate-blind-spot-table.md:158-194`; that exact record is cited, not a fabricated path.

## C3 — three corrections replayed on delivered bytes

Preparation command, exit 0:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replay.py prepare
```

Observed five `PREPARED` mirrors: `pre-r99-anchor`, `delivered-anchor`, `delivered-precedence`, `delivered-prose-control`, `delivered-self-test`. Historical files were extracted with `git show 4265df5:<path>`; delivered tool and contract were byte copies. Scratch mutations used exact `Edit` calls after reading the targets: four excerpt-only `depends on both ninth-bell entries` → `follows both ninth-bell entries` replacements, and one removal of `evin-ninth-bell` from the precedence mirror's `paired-crossing-decision.depends_on`. Live fixtures and pins were untouched.

Actual replay command, run twice (initial absolute-path argv, then lane-root-relative argv for the filed commands), each exit 0:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replay.py run
```

Observed final summary:

```text
A1-pre-r99-support: exit=1 expected=1
A2-pre-r99-freeze: exit=0 expected=0
A3-delivered-support: exit=1 expected=1
A4-delivered-freeze: exit=2 expected=2
A5-delivered-check-bible: exit=0 expected=0
A6-delivered-map: exit=0 expected=0
B1-semantic-precedence: exit=1 expected=1
B2-prose-control: exit=2 expected=2
C1-combined-invalid: exit=2 expected=2
SELF-delivered-freeze: exit=0 expected=0
SELF-TEST 18/18
RESULT PASS
REPLAY failures=[]
```

**Row 10 / AC-2:** the excerpt-only replacement removes J14's verbatim anchor without changing the map. Pre-r99 and delivered support tools both print `FAIL: J14: source-support anchor missing`, `RESULT FAIL`, exit 1; they are byte-identical at SHA-256 `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`. Historical JSON-only freeze passes exit 0; delivered freeze exits 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`. The live checker and map tool on the delivered mutant stay CLEAN/PASS, exits 0, with `OBLIGATIONS raw=15 mapped=15`. Thus “invisible to every gate” must exclude unmatched mapped anchors. Exact per-gate commands and stdout are filed at table lines 287–324 and in `T4-scratch/replay-output.txt`.

**Row 11 / AC-1:** the edge-plus-prose mutant's actual command was:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

No `DIGEST-MISMATCH` was emitted. The prose-only twin, with identical inventory, exits 2 and names `fictional-excerpts.md` in a `DIGEST-MISMATCH`. Its command and full digest line are filed at table lines 345–353. This scopes the blanket “any edit → exit 2” sentence without claiming natural-language meaning was checked.

**Row 12 / AC-3:** actual live invalid invocation (no freeze write):

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

Exactly one finding; no inventory or digest receipt. Contract SHA-256 was `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5` before and after the replay, and remained that value at the final audit. The delivered freeze tool was `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; the pre-r99 tool/contract were `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` / `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.

## C2 — arc, preservation, and delivered scenario

Actual post-producer command:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/arc_audit.py
```

Observed exit 0, `ARC-AUDIT failures=[]`; 21 real CLI gate calls (checker/support/map × all seven dossier snapshots) each exit 0. The raw counts and map receipts respectively were:

```text
r94-paired-crossing        5/1/3 sources=3 obligations=14 / raw=14 mapped=14
r95-crossing-aftermath     5/1/4 sources=4 obligations=15 / raw=15 mapped=15
r96-crossing-response      5/1/5 sources=5 obligations=16 / raw=16 mapped=16
r97-crossing-acknowledgment 5/1/6 sources=6 obligations=17 / raw=17 mapped=17
r98-clerk-filing           6/1/7 sources=7 obligations=20 / raw=20 mapped=20
r99-window-lapse           6/1/8 sources=8 obligations=21 / raw=21 mapped=21
r100-docket-review         6/1/9 sources=9 obligations=22 / raw=22 mapped=22
CENSUS 174
ARC-AUDIT failures=[]
```

The exact new-scenario commands were real child calls of the audit, all exit 0:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Observed checker `CLEAN: schema, citations, relations, timeline; 0 violations`; support `INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20`, `SOURCE-SUPPORT 22/22`, `RESULT PASS`; map `OBLIGATIONS raw=22 mapped=22`, `RESULT PASS`. Complete unabridged stdout and commands: `T4-scratch/arc-output.txt`; structured counts/receipts/final fixture digests: `T4-scratch/arc-results.json`.

All six continuation steps preserved inherited entity prefixes, full relations, timeline/source prefixes, excerpt byte prefixes, inspiration/external excerpt bytes, and inherited map cells after normalizing only the namespace column: all eight checks per step were `True`. Every contradiction table is `[]`. The r99→r100 five preserved files are byte-identical; the old 5,114-byte excerpt is a prefix of the new 5,961-byte file. At final audit all ten r100 file hashes still matched the 21-gate replay.

The note itself, not a gate, carries the unresolved bounds: `fictional-excerpts.md:82-86` says the entry remains open, no new filings have been lodged, the clerk makes no finding and resolves nothing, and both accounts stand unresolved. The synthesis distinguishes reported assertions from truth and does not retroactively invent an OPEN docket at r94/r95.

## Regression controls, coverage observation, and final audit

The isolated delivered freeze mirror ran `--self-test` as part of the replay above: `SELF-TEST 18/18`, `RESULT PASS`, exit 0. The map tool and contract were then copied into the same owned mirror, and this actual command passed:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-self-test/corpus/tools/map_obligations.py --self-test
```

Observed `SELF-TEST CASES 25/25 pinned`, 25 `SELF-TEST PASS` lines, `RESULT PASS`, exit 0; full receipt in `T4-scratch/replays/delivered-self-test/map-self-test-output.txt`. All self-test temporary writes were contained under the declared scratch. No production code change or new production test was made.

Actual final audit command:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/final_audit.py
```

Observed exit 0 and these summary lines:

```text
TABLE historical_prefix=20526 bytes preserved; added_bytes=8907
TABLE dated_rows=3 exact; historical_rows_unmodified=PASS
ARC saved_real_gate_receipts=21/21 clean; delivered_r100_file_stability=10/10
REPLAY all_expected_outcomes=PASS; contract_stable=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
CHAIN 7/7 clean; six inherited pins unchanged; r100 explicitly unpinned
GIT-DIFF-CHECK PASS (new-file whitespace independently checked above)
CITED_PATHS 96; EXPLICIT_RANGES 28; MISSING 0
FINAL-AUDIT PASS
```

The final audit re-ran all seven actual `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<pinned-name>` invocations concurrently, each `RESULT PASS` exit 0. The new r99 pin's digest was `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`, events 8/8, edges 7/7, relations 1/1; every field in the six inherited pins equaled `git show fe1ce46:corpus/tools/dependency-freeze-contract.json`. This is an independent coverage observation, not credit for T1's guarded authoring and not an r100 pin claim.

`git diff --check -- corpus/knowledge/r99-gate-blind-spot-table.md` exited 0, no output. Because the two new documents are untracked during the wave, the audit separately checked their final newlines, trailing whitespace, fence balance, metadata, cited paths, and explicit numeric ranges rather than pretending tracked diff checking covers them. Full final receipt: `T4-scratch/final-audit-output.txt`.

## Residuals and verdict scope

No implementation or validation failure remains in this seat's deliverable. Initial expected absent-path Reads and the intentional non-zero negative probes are not concealed; their meanings are recorded above. The corpus remains an authored arc, not testimony/chronology authentication or whole-proposition semantic proof. Rights and AI-training permission remain unassessed. The r100 tick-16 edge remains outside the delivered seven-pin set by the declared C1 scope; both new notes name that boundary explicitly. Round-wide admission and independent non-author review remain with the verifier/adjudicator seats.

PASS — T4's three owned knowledge deliverables landed; seven-record/six-continuation dossier, three freshly replayed dated corrections, all 21 arc gates and 7 chain verifications green, self-tests 18/18 and 25/25, historical table preserved, cited paths checked, and no unresolved seat blocker.
