# V49 — gates-cross (round 96)

**Seat:** V49, cross-gate consistency on the BR-01 mutated copy.
**Cwd:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (all paths below relative to it unless absolute).
**Baseline:** r95 closure `dcb2d92`; HEAD at test time `60dba0c2aa344860b10a2fc63e00468d1b134f27`. Python 3.14.7.
**Tested revisions:** `corpus/tools/dependency_freeze.py` sha256 `d17297bb…` (in-flight) and **`a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980`** = Q3's delivered revision (`Q3-dependency-freeze.md`), used for all results below unless noted; `corpus/tools/dependency-freeze-contract.json` `7d568cc4…`; `corpus/tools/map_obligations.py` — blind to BR-01 at the HEAD/r95 revision `d1c239cc…` and again at **`2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8`** = Q1's delivered revision (`Q1-tool-hardening.md`), with Q2's delivered contract **`97b76bb8…`** (`--self-test` now `SELF-TEST CASES 24/24 pinned`, RESULT PASS; the fixture-verify path `run_cluster` never reads the contract — only `run_self_test` does, so the contract cannot change the BR-01 result); `corpus/fixtures/check_bible.py` `ff9fd2aa…`; `corpus/tools/support_check.py` `55a5eb27…`; `corpus/tools/boundary_doc_check.py` `ebb6a084…`. The final five-gate run on the BR-01 copy at this fully-delivered revision set reproduces the table below unchanged.

## 1. Mutation under test (BR-01)

BR-01 = dependency reduction is undetectable: dropping `evin-ninth-bell` from the r94 tick-10 `depends_on` leaves every prior gate green.

Scratch copy built by `cp -r corpus/fixtures/r94-paired-crossing .ufo/waves/round-96/seats/V49-scratch/mutated/r94-paired-crossing` (name-preserving, because `dependency_freeze.pin_for` keys pins by `fixture.resolve().name`, dependency_freeze.py:251-252) then a byte-level edit of `timeline.json`:

```
26,27c26
<       "aru-ninth-bell",
<       "evin-ninth-bell"
---
>       "aru-ninth-bell"
```

Mutated `timeline.json` sha256 `dd66ded2d8f690cb3884389ccacde059f2bf9c174907e3c718648027c84ba7fd` (clean: `f0209f90…`). No other byte differs. Control copy (clean, name-preserving): `.ufo/waves/round-96/seats/V49-scratch/clean/r94-paired-crossing`.

## 2. Cross-gate tabulation

Every command run from the lane repo root against the same copies; exit codes observed, not inferred.

| Gate | Command | Clean copy | BR-01 mutated copy | Catches? |
|---|---|---|---|---|
| `check_bible` | `python3 corpus/fixtures/check_bible.py <dir>` | exit 0 `CLEAN: schema, citations, relations, timeline; 0 violations` | exit 0 `CLEAN: schema, citations, relations, timeline; 0 violations` | **No** |
| `support_check` | `python3 corpus/tools/support_check.py <dir>` | exit 0 `RESULT PASS` (`SOURCE-SUPPORT 14/14; … MODES 16/16; VALIDATED-ROWS 16/16`) | exit 0 `RESULT PASS`, identical receipt (`INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12`) | **No** |
| `map_obligations` | `python3 corpus/tools/map_obligations.py <dir>` | exit 0 `OBLIGATIONS raw=14 mapped=14` / `INVENTORY … 16/16` / `RESULT PASS` | exit 0, byte-identical output (`raw=14 mapped=14`, `16/16`, `RESULT PASS`) | **No** |
| `dependency_freeze` | `python3 corpus/tools/dependency_freeze.py <dir>` | exit 0 `FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1` + `DIGEST 2527beb9…` + `RESULT PASS` | **exit 1** `FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1` / `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` / `RESULT FAIL` | **YES** |
| `boundary_doc_check` (default) | `python3 corpus/tools/boundary_doc_check.py` | exit 0 `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; …)` | exit 0, identical (gate reads no fixture input) | **No** (out of scope by construction) |

Conclusion for the seat brief: **dependency_freeze is the only gate that catches BR-01; the other four do not.** The mutated copy is exit-1 only under `dependency_freeze`.

Control side: on the *delivered* fixtures at the same revisions all five gates are clean — `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response` each exit 0 under `check_bible`, `support_check`, `map_obligations`, `dependency_freeze`, and the boundary default exits 0 `CERTIFIED`.

Full transcripts: `.ufo/waves/round-96/seats/V49-scratch/v49-final-tabulation.txt`, `v49-crossgate-tabulation.txt`, `v49-baseline-mutated-evidence.txt`.

## 3. Why the four are blind (mechanism, not accident)

- `check_bible.py:393-414` validates `depends_on` member *shape* and per-member properties — self dependency, repeated member, unknown/ambiguous event ID, tick inversion — but never holds an expected edge set. Removing one well-formed member breaks none of those checks.
- `map_obligations.py:416-431` compares the raw obligation **pointer set** and per-pointer `source_id` only (`phantom_obligation`, `missing_obligation`, `source_id_mismatch`); it never compares field *values*, so `depends_on` content is invisible. Fixtures README already states this scope ("covers raw-JSON↔map completeness and source-ID agreement only").
- `support_check.py` validates map-declared rows, anchors, spans, modes against the excerpt text; J14's anchor text and span are untouched by the mutation.
- `boundary_doc_check.py` verifies the frozen boundary document/checker pins and receipts; it takes no fixture input (`--help` lists only `--doc`, `--checker`, `--self-test`), so its default run is identical before and after any fixture mutation.

## 4. Corroborating variants (same revision)

All on name-preserving scratch copies; mutations other than the duplicate case are inventory-visible (counts unchanged), so the other gates stay blind unless noted.

| Variant | dependency_freeze | check_bible | support_check | map_obligations |
|---|---|---|---|---|
| r96 chain reduction: drop `paired-crossing-decision` from tick-11 `aftermath-missing-evin` | exit 1 `REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']` (edges 3/4) | exit 0 CLEAN | exit 0 PASS | exit 0 PASS |
| r96 genuine added edge: `aru-ninth-bell` added to tick-12 `response-evin-salt-court` | exit 1 `ADDITION-DETECTED: event response-evin-salt-court gained depends_on ['aru-ninth-bell']` (edges 5/4) | exit 0 CLEAN | exit 0 PASS | exit 0 PASS |
| r94 endpoint change: tick-10 `place_id` `chalk-stair`→`quiet-rise` | exit 1 `ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'quiet-rise'` | exit 0 CLEAN | — | — |
| r94 duplicate added member: tick-10 `depends_on` gains a repeated `aru-ninth-bell` | **exit 2** `DIGEST-MISMATCH: content digest bb6bf275… != pin 2527beb9…; fixture bytes changed outside the frozen inventory` | **exit 1** `VIOLATION: timeline[2].depends_on[2]: repeated dependency 'aru-ninth-bell'` | — | — |

Nuance worth recording: because the frozen model is a *set*, a repeated added member is not an inventory change, so the tool falls through to the digest guard and exits 2 (could-not-evaluate) — not exit 1. That is consistent with its declared precedence ("a content digest change the frozen inventory does not model exits 2"), and in that one case `check_bible` is the gate that names the defect. The C3 declaration's "an added-edge mutation must also exit 1" holds for a *distinct* added edge (row 2 above), which is the case the declaration describes.

## 5. Tool self-test — defect observed and resolved mid-run

At revision `d17297bb…` (17:42-17:43, Q3's report not yet filed), `python3 corpus/tools/dependency_freeze.py --self-test` printed `SELF-TEST 5/14` / `FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'digest_tamper', 'event_endpoint_change', 'event_removed', 'malformed_json', 'reduction_edge_drop', 'relation_added', 'relation_endpoint_flip', 'relation_removed']` / `RESULT FAIL` / exit 1. Every failed case ran against `…/missing_timeline/r95-crossing-aftermath` — a late-binding closure bug: each `cases[name] = (lambda: [scratch], …)` captured the *variable* `scratch`, so all lambdas returned the last assignment (`missing_timeline`). Q3's report now describes fixing exactly this ("all case lambdas…" under "Defects the self-test caught in its own first runs").

At the delivered revision `a3b57978…` the same command prints `SELF-TEST 14/14` / `RESULT PASS` / exit 0, and the persisted contract expectations match (14 cases). Re-verified at that revision: chain clean 4/4 (`r88` 2/2 edges, `r94` 2/2, `r95` 3/3, `r96` 4/4, all `RESULT PASS` exit 0), BR-01 mutated copy exit 1 `REDUCTION-DETECTED`, and the self-test still 14/14 under load. `corpus/tools/map_obligations.py --self-test` passes at Q1's delivered revision `2b0ba815` with Q2's delivered contract `97b76bb8`: `SELF-TEST CASES 24/24 pinned` / 24 `SELF-TEST PASS` lines (including the new `schema_drift` and `inventory_mismatch` cases) / `RESULT PASS` exit 0.

## 6. Harness observation (not a seat defect)

At ~17:47 the environment hit **`/tmp` tmpfs inode exhaustion** (1048576/1048576 inodes used, 100%; block space only 45% used, 8.5 GB free). Commands redirecting to `/tmp` failed with `No space left on device` for about a minute; retries succeeded with output captured in-memory. Both tools' self-tests still passed during and after this. The same condition can make any seat's `tempfile`-based scratch work fail spuriously this round; a future round should clean `/tmp` or set `TMPDIR` under the lane tree.

## 7. Scope of this evidence

What is shown: at the revisions pinned by sha256 above — the `dependency_freeze` and `map_obligations` revisions and Q2's contract all confirmed as delivered by their producers' reports, and re-run at that full set — the BR-01 reduction class is caught by `dependency_freeze` alone, with a stable finding ID and exit 1, and the other four gates' blindness is structural (each quoted). What is not shown: that the frozen inventories are semantically correct beyond the pin, that chronology/entailment/canon claims are true (the tool's own scope line disclaims this), or that the r96 delivery is byte-final (Q2's `README.md` was the only artifact still in flight at writing). No corpus file was modified by this seat; all work happened in `.ufo/waves/round-96/seats/V49-scratch/`.

## Bottom line

**PASS** — on the BR-01 mutated copy only `dependency_freeze` catches the dropped `evin-ninth-bell` edge (exit 1, `FINDING REDUCTION-DETECTED`), while `check_bible`, `support_check`, `map_obligations`, and `boundary_doc_check` all exit 0, exactly as the cross-gate claim requires; the same pattern replicates on the r96 chain member and for a genuine added edge, the tool's `--self-test` defect seen at `d17297bb` was fixed by Q3 at `a3b57978` (14/14), and the five gates are jointly clean on the delivered r94/r95/r96 chain.
