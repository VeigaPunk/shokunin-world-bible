# Q1 — tool hardening (`map_obligations` C1 bundle)

**Seat:** Q1 (producer; exclusive byte-owner of `corpus/tools/map_obligations.py`)
**Wave:** round-96, single-wave 64-seat swarm (6 producers + 58 verifiers)
**Baseline:** r95 closure `dcb2d92`
**Baseline tool blob:** `git show dcb2d92:corpus/tools/map_obligations.py` → sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` (matches the r95 closure's
pinned tool revision `d1c239cc…`)
**Delivered tool:** `corpus/tools/map_obligations.py` sha256
`2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (809 → 900 lines;
`git diff --numstat` = 115 insertions / 24 deletions, one file)
**Scratch:** `.ufo/waves/round-96/seats/Q1-scratch/` (driver `q1-demos.py`, transcript
`q1-demos-out.txt`, battery `battery.txt`, baseline controls `baseline-controls.txt`, poll log
`contract-poll.log`). Every mutation ran on a scratch copy under that directory; the corpus tree
was never written by this seat.

## 1. What changed

Three parts, all inside the one owned file, stdlib only, no new imports.

**(a) Gating inventory.** `declared_inventory()` now resolves counts through `inventory_counts()`
(strict documented form first, loose integer scan for off-form lines) and the new
`inventory_finding()` turns a declared-vs-observed disagreement — or a declaration whose counts
cannot be parsed at all — into the stable finding `inventory_mismatch`. `run_cluster()` and
`run_frozen()` append it to the finding list, so exit 1. The `INVENTORY …` receipt line is
unchanged (still printed, still appends ` MISMATCH`); it is now backed by a gate. The declared
`distinct excerpt anchors` field stays receipt-only (see §7).

**(b) Persisted pinning hooks.** The implemented self-test set is now
`CORE_SELF_TEST_CASES` (the inherited 22) plus `ADDED_SELF_TEST_CASES = ("schema_drift",
"inventory_mismatch")` → `SELF_TEST_CASES` (24). `prepare_test_case()` grows two isolated setups:
`schema_drift` (claims container renamed to `assertions` on entity 0 with that claim's map row
removed → exactly `["schema_drift"]`, exit 1) and `inventory_mismatch` (fixture declares
`5 JSON facts; 0 editorial rows; 5 total mapped rows` while 4 rows exist → exactly
`["inventory_mismatch"]`, exit 1). `load_test_expectations()` now requires the contract to pin
every core case and to pin no unimplemented case, so the tool passes against the live 22-case
contract **and** against Q2's 24-case contract; `run_self_test()` prints
`SELF-TEST CASES <pinned>/24 pinned` and exercises exactly the pinned cases. Q2 owns the contract
file; this seat did not touch it.

**(c) V37-D1 (`dual_pointer`).** `LEGACY_CELL` keeps its original accepted grammar but captures
the optional parenthetical/colon-prose tail in a named group; `second_pointer_mention()` scans
that tail with `POINTER_MENTION` (backticked canonical pointer, backticked legacy field path,
bare `*.json#…`, bare `entities[i]`/`relations[i]`/`timeline[i]`). A legacy-dialect cell that
names a second pointer now yields `FINDING dual_pointer` with the row ID, line number, the second
token, and the first token it was read as; the row is still read by its first token so no
cascading `missing_obligation` noise is produced. Exit 1.

## 2. Claim (a) — deletion class, before → after

Same scratch copy for both revisions: `cp -r corpus/fixtures/r95-crossing-aftermath
…/Q1-scratch/work/deletion-class`, then `del entities[0]["claims"]` and drop the map row
`| J06 | … entities.json#/0/claims/0 …`.

Baseline `d1c239cc…` (silent pass, as carried):

```
$ python3 .ufo/waves/round-96/seats/Q1-scratch/baseline-map_obligations.py …/work/deletion-class
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
RESULT PASS
exit=0
```

Delivered revision:

```
$ python3 corpus/tools/map_obligations.py …/work/deletion-class
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
RESULT FAIL
exit=1
```

Related probes on scratch copies of `r93-m2-kojiki-cluster`: declaration rewritten to
`11 JSON facts; 3 editorial rows; 14 total mapped rows` → `INVENTORY JSON-FACTS 12/11 … MISMATCH`,
`FINDING inventory_mismatch`, exit 1; declaration rewritten to unparsable prose
(`**Expected inventory:** see the table below.`) → `INVENTORY declaration-malformed`,
`FINDING inventory_mismatch: map declares an **Expected inventory:** line whose counts cannot be
parsed`, exit 1 (fail-closed: corrupting the declaration cannot disable the gate); declaration
line deleted entirely → `OBLIGATIONS raw=10 mapped=10`, `RESULT PASS`, exit 0 (absence of a
declaration is not a disagreement).

## 3. Claim (b) — self-test pinning

Against the **live 22-case contract** (`corpus/tools/map-obligations-contract.json`, mtime
16:27, unchanged by this seat):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 22/24 pinned
SELF-TEST PASS complete exit=0 findings=none
… (22 SELF-TEST PASS lines, one per pinned case; the two unpinned cases are schema_drift,
   inventory_mismatch) …
RESULT PASS
exit=0
```

Against Q2's **live 24-case contract** (`corpus/tools/map-obligations-contract.json` sha256
`97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6`, landed 17:50 during this
seat's run; Q2 owns that file and this seat never wrote it), which pins exactly
`schema_drift` (exit 1, `["schema_drift"]`) and `inventory_mismatch` (exit 1,
`["inventory_mismatch"]`) — the two implemented case IDs:

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS complete exit=0 findings=none
… (24 SELF-TEST PASS lines) …
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
exit=0
```

The same 24/24 result was also reproduced before Q2's file landed, against a synthetic 24-case
contract in `.ufo/waves/round-96/seats/Q1-scratch/contract-24/` (copy of the tool beside a copy of
the contract with the two cases added), so the pinning claim does not depend on Q2's landing time.

## 4. Claim (c) — V37-D1, all three reported forms

Scratch copies of `r88-m3-maya-cluster` (the legacy `JSON fact and fields` dialect), each with
one pointer cell rewritten; baseline `d1c239cc…` exits 0 on all three (silently ignored):

| probe | cell | delivered output | exit |
|---|---|---|---|
| paren, canonical 2nd token | `` `entities[0].first_appearance` (also `relations.json#/0`) `` | `FINDING dual_pointer: row P1 (line 23) names a second pointer token 'relations.json#/0' alongside entities.json#/0/first_appearance` | 1 |
| paren, legacy 2nd token | `` `entities[1].first_appearance` (also `entities[9].claims[0]`) `` | `FINDING dual_pointer: row P2 (line 24) names a second pointer token 'entities[9].claims[0]' alongside entities.json#/1/first_appearance` | 1 |
| colon-prose 2nd token | `` `timeline[1]`: also `entities[9].claims[0]` `` | `FINDING dual_pointer: row T2 (line 32) names a second pointer token 'entities[9].claims[0]' alongside timeline.json#/1` | 1 |

All three print `RESULT FAIL` and exit 1; the `OBLIGATIONS raw=10 mapped=10` and
`INVENTORY … 12/12` lines are unchanged from the clean r88 run. Fail-closed controls, unchanged
from r95: a legacy cell with undocumented tail prose
(`` `entities[0].first_appearance` extra prose ``) → `unsupported_map`, exit 2; a legacy cell
whose first token is canonical with a pointer in the note
(`` `entities.json#/0/first_appearance` (also `relations.json#/0`) ``) → `unsupported_map`,
exit 2; the same note form under a canonical header (r94 copy) → `unsupported_map`, exit 2.
No legacy-grammar relaxation was introduced.

`schema_drift` still exits 1 on the r95-documented mutation: r95 copy with `claims` renamed to
`assertions` and the row kept → `phantom_obligation` + `schema_drift`, exit 1; with the row also
removed → `schema_drift` + `inventory_mismatch`, exit 1 (the second finding is the new gate
reporting the same stale declaration honestly, not a regression).

## 5. Non-regression battery (delivered revision, full transcript in `Q1-scratch/battery.txt`)

| command | observed | exit |
|---|---|---|
| `map_obligations.py corpus/fixtures/r88-m3-maya-cluster` | `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r93-m2-kojiki-cluster` | `raw=12 mapped=12` / `12/12; 3/3; 15/15` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r94-paired-crossing` | `raw=14 mapped=14` / `14/14; 2/2; 16/16` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r95-crossing-aftermath` | `raw=15 mapped=15` / `15/15; 2/2; 17/17` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r96-crossing-response` (Q4/Q5 delivered map) | `raw=16 mapped=16` / `16/16; 2/2; 18/18` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r87-myth-cluster` | `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` / `RESULT ERROR` | 2 |
| `… corpus/fixtures/r89-inspiration-paraphrase` | `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` | 2 |
| `… --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `INVENTORY … 15/15` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` | 0 |
| `… corpus/fixtures/r96-crossing-response --map claim-excerpt-map.md` | `RESULT PASS` | 0 |

Determinism: two consecutive r88 runs are byte-identical (`diff` → `identical`). r87/r89 finding
text and exits match the r95-closure outputs recorded in the r95 LOG corrections (detail string
unchanged by this revision).

Usage probes (all `RESULT ERROR`, exit 2): no arguments → `invalid_arguments: cluster directory is
required`; `--self-test <cluster>` → `invalid_arguments: --self-test cannot be combined with
cluster, --map, or --frozen`; `--frozen <dir> <cluster>` and `--frozen <dir> --map …` →
`invalid_arguments: --frozen cannot be combined with cluster or --map`; `--map /etc/hosts` →
`foreign_path: map path is outside the cluster`; `--bogus` → `invalid_arguments: unrecognized
arguments: --bogus`.

## 6. Contract-ownership boundary

This seat wrote only `corpus/tools/map_obligations.py`. `corpus/tools/map-obligations-contract.json`
and `corpus/tools/README.md` are Q2's; no other corpus file was modified (`git status --short`
shows `M LOG.md` (wave owner), `M corpus/tools/map_obligations.py` (this seat), and untracked
r96 producer artifacts from Q3/Q4/Q5/Q6). No commits, no pushes, no network.

## 7. Bounded residuals (declared, not hidden)

1. **Anchor counts stay receipt-only.** The declaration's fourth field (`N distinct excerpt
   anchors`) is not compared, because this tool does not read anchor columns; anchor counting is
   `support_check.py`'s scope. A map that declares a wrong anchor count still passes.
2. **`dual_pointer` is bounded to the legacy dialect.** A second pointer in a canonical-header
   cell is still rejected as `unsupported_map` exit 2 (the pre-existing screening), not
   `dual_pointer`; and the legacy check only sees the documented parenthetical/colon-prose tail.
3. **Loose declaration parsing.** An off-form `**Expected inventory:**` line with ≥4 integers is
   compared positionally (facts, editorial, total, anchors); a line with <4 integers gates as
   unparsable. This is deliberate fail-closed behavior for a line the tool cannot verify, and is a
   behavior change beyond the literal "disagrees with observed rows" wording.
4. **Self-test coverage is subset-tolerant by design** (core 22 must be pinned; nothing
   unimplemented may be pinned) so the tool passes both the live 22-case contract and Q2's
   24-case contract. Once the 24-case contract is committed, the 22/24 printout is history, not a
   defect.
5. **BR-05 unchanged.** The self-test scratch still lives under the repository root
   (`tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`) and is not
   gitignored; residue is cleaned on normal exit. One transient `map-obligations-self-test-*`
   directory was observed mid-round during a concurrent seat's run and had vanished when re-checked
   — consistent with the documented BR-05 behavior, not new residue.
6. **Environment note.** `/tmp` reported `No space left on device` for one probe; the probe was
   re-run under the seat scratch dir. No tool output depends on `/tmp`.

## 8. Q2 contract poll (24-case run)

Poll protocol: `.ufo/waves/round-96/seats/Q1-scratch/poll-contract.py`, 20 s cadence, 40 tries
(~13 min), checking `corpus/tools/map-obligations-contract.json` for ≥24 cases and running
`--self-test` the moment it lands. **Result: LANDED.** Q2's contract reached 24 cases at 17:50
(mtime `17:50:17`, sha256 `97b76bb8…`); the poll's own run recorded
`SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']`, `RESULT PASS`,
`self-test exit=0`, and this seat's independent re-run printed `SELF-TEST CASES 24/24 pinned`
with all 24 `SELF-TEST PASS` lines and exit 0 (transcript
`.ufo/waves/round-96/seats/Q1-scratch/selftest-24.txt`, poll log `contract-poll.log`). The two
case IDs Q2 pinned are exactly the two this seat implemented, so no adaptation was needed; the
subset-tolerant loader only had to carry the tool across the window before the contract landed
(22/22, exit 0, transcript §3).

## 9. Cross-check against verifier probe forms (already-visible seat reports)

Read-only cross-check against probes that verifier seats had already built when this report was
written; all three ran on scratch copies built by this seat under `Q1-scratch/work/`.

V34's exact V37-D1 form (second pointer late in the colon-prose, r88 copy,
`` | E4 | `entities[3].claims[0]`: the register locates Evin's south-bell entry at Salt Court; see also `entities[2].claims[0]` | ``):

```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
FINDING dual_pointer: row E4 (line 30) names a second pointer token 'entities[2].claims[0]' alongside entities.json#/3/claims/0
RESULT FAIL
exit=1
```

V34's drift-scope bounds (r94 copies; the drift rule itself is untouched by this revision — the
diff changes no line of `claim_shaped` or the drift loop): entity unexpected key `notes` with
claim-shaped records → `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s)
under unexpected key 'notes'`, exit 1; entity unexpected key `tags` holding plain strings →
`RESULT PASS`, exit 0; timeline key `extra_notes` holding claim-shaped records → `RESULT PASS`,
exit 0. Identical to V34's baseline pins, so the declared bound ("drift scope unchanged") holds.

V01's single-sided controls (J10 `row-only` / `key-only` on r95) are covered by the unchanged
finding paths, verified on this revision:

```
### v01-row-only  (J10 row removed, claims key kept)
OBLIGATIONS raw=15 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
FINDING missing_obligation: entities.json#/4/claims/0 has no map row
RESULT FAIL
exit=1

### v01-key-only  (claims key deleted, J10 row kept)
OBLIGATIONS raw=14 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
FINDING phantom_obligation: entities.json#/4/claims/0 is not a raw source-attributed obligation
RESULT FAIL
exit=1
```

The row-only case gains `inventory_mismatch` (the declaration is now stale as well); the key-only
case keeps a consistent inventory (15/15) and is unchanged apart from the exit-1 path it always
had.

## Bottom line

**PASS** — all three C1 parts verify on the delivered revision `2b0ba815…`: the r95 deletion class
now exits 1 with the stable `inventory_mismatch` finding (baseline `d1c239cc…` exits 0 on the same
input), `--self-test` passes 24/24 with exit 0 against Q2's live 24-case contract (`97b76bb8…`,
pinning `schema_drift` and `inventory_mismatch`) and passed 22/22 before it landed, and all three
V37-D1 legacy hidden-second-pointer forms — including V34's colon-prose form — now exit 1 with the
stable `dual_pointer` finding while every other control (r87/r89/r88/r93/r94/r95/r96, frozen-r93
replay, usage probes, legacy and canonical fail-closed forms, drift-scope bounds) keeps its
baseline exit code and finding text.
