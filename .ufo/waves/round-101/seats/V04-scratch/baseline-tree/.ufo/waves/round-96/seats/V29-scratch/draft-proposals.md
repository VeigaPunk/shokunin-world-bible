# V29 draft proposals (r96 doc-parity inventory) — work file v2

Confirmed receipts (all measured this seat, 2026-10-17):
- census replica validated on dcb2d92: 169/35/134/421/0 (exact r95 closure match)
- working tree census: 170/36/134/421/0
- r96 check_bible: CLEAN exit 0
- r96 map_obligations (Q1 pre-hardening rev d1c239cc): OBLIGATIONS raw=16 mapped=16; INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; RESULT PASS exit 0
- r96 support_check: SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18; RESULT PASS exit 0 (J16 anchor fictional-excerpts:37)
- C9: sha256 ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421; discriminate_check exit 0 DISCRIMINATION HELD; --checker e97613c exit 2 REGRESSION-DETECTED
- dependency_freeze: self-test 14/14 PASS exit 0; chain r88/r94/r95/r96 4/4 clean with digests 15ef230e…/2527beb9…/d541ae64…/d422a9b3…
- dependency-freeze-contract.json pins: c3red (FOREIGN, V41 scratch), r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response

## P1. fixtures README Round-96 section (proposed; append after line 1196)

## Round 96 — `r96-crossing-response` (2026-10-17)

Added at round 96: a preserving continuation of `r95-crossing-aftermath`. A second account of the same occasion: Evin's authored response note (`evin-response-note`) and one tick-12 event (`response-evin-salt-court`, actor `evin`, place `salt-court`, `depends_on: ["aftermath-missing-evin"]`) record that Evin was at Salt Court through the same agreed bell. The two first-person accounts stand unresolved: the note asserts no accusation and selects no winner, and no contradiction is asserted (the accounts name different actors at different places). Inherited r95 records are parsed-value identical; the r95 fixture itself is untouched. Map: 16 obligations (15 inherited rows unchanged + the new event row); support receipt 16 JSON facts + 2 editorial rows.

Replay commands and receipts (measured at the r96 closure, HEAD cited in LOG.md):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
# OBLIGATIONS raw=16 mapped=16; INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18 / RESULT PASS   exit 0
```

Round 96 also hardened `map_obligations` (see the tools README Round-96 addendum): a declared-vs-observed inventory mismatch is now GATING (deletion class → exit 1, stable `inventory_mismatch` FINDING), `schema_drift` and `inventory_mismatch` are pinned by persisted self-test cases (24 total), and a legacy-dialect map cell naming a second pointer in prose exits 1 `dual_pointer` (V37-D1 closed). The new `dependency_freeze` gate (see the tools README Round-96 addendum) freezes dependency-edge inventories, event endpoints and relation endpoints for the continuation chain; the delivered chain verifies 4/4 clean and the BR-01 reduction mutation exits 1 `REDUCTION-DETECTED`.

### 2026-10-17 census re-declaration

A full repo-relative corpus run at the r96 closure observed **170 fixture directories: 36 clean (exit 0), 134 intentional negative (exit 1), 421 violation lines, zero non-0/1 exits**. This supersedes the Round-95 census (169/35/134/421) as a measured statement at this revision, not a pinned invariant. One directory was added (`r96-crossing-response`); zero inherited tuples changed.

Dated pin note: this Round-96 append changes this file's bytes; the W05 preservation pin recorded at `.ufo/waves/round-94/work/W05-baseline-corpus.sha256` for this file no longer matches (third consecutive round; the census re-declaration above is the measured state at closure).

## P2. corpus/README.md edits

(a) after line 22 (r95 bullet) insert:

- `fixtures/r96-crossing-response/README.md` — continuation of the r95 fixture: a second account of the same occasion — Evin's response note reports Evin at Salt Court through the same agreed bell (tick-12 event depending on the tick-11 aftermath event). The two first-person accounts stand unresolved: no accusation, no winner, no contradiction asserted. Navigate `claim-excerpt-map.md` (16 obligations) and `fictional-excerpts.md`.

(b) line 36 replace with:

- `tools/map_obligations.py` (rounds 94–96) — raw-JSON↔map obligation completeness and source-ID agreement for canonical one-obligation-per-row cluster maps and the r88-m3 legacy dialect; a declared-vs-observed inventory mismatch is gating (`inventory_mismatch`, exit 1), legacy-dialect hidden-second-pointer cells exit 1 `dual_pointer`, `--self-test` persists 24 cases, and a digest-pinned `--frozen` snapshot is available. Mapping completeness only, never entailment, authentication, chronology, rights, permission, or canon.

(c) new bullet after (b):

- `tools/dependency_freeze.py` (round 96) — frozen dependency-edge inventory, event endpoints and relation endpoints for the continuation chain (`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`) pinned with fixture content digests; exit 0 clean / 1 reduction, addition, or endpoint change with stable FINDING IDs / 2 could-not-evaluate; `--self-test` persists 14 cases. Detects silent dependency reduction (BR-01); not a canon or chronology judgment.

(d) line 37 add `tools/dependency_freeze.py` to the tools/README bullet tool list.

## P3. SKILL.md

(a) map_obligations row updates:
- code → class exit-1 list: add `inventory_mismatch` / `dual_pointer`.
- self-test command: "22 cases (r95 added `map_missing`, `invalid_arguments`)" → "24 cases (r96 added persisted `schema_drift` and `inventory_mismatch` cases)"; delete the "(r95 debt)" sentence.
- scope: add gating inventory mismatch (three observed counts; anchor count stays a receipt) + dual_pointer; update residuals line.

(b) new registry row after map_obligations:

### Dependency freeze (continuation chain)

- **name:** `dependency_freeze`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/dependency_freeze.py <fixture-directory>` (repository root; `--freeze <fixture-directory>` (re)builds the pin and is delivery-time only, not part of the verify path)
- **code → class:** `0 → clean`; `1 → failed` (`REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE` with stable FINDING IDs); `2 → could-not-evaluate` (`DIGEST-MISMATCH` for content changes outside the frozen inventory, `UNPINNED-FIXTURE`, `FIXTURE-MISSING`, `FILE-MISSING`, `MALFORMED-JSON`, `MALFORMED-MODEL`, `CONTRACT-INVALID`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`); other codes → `could-not-evaluate`
- **self-test command:** `python3 corpus/tools/dependency_freeze.py --self-test`; 14 isolated cases with persisted expected exits and finding IDs under `self_test.expected` in `corpus/tools/dependency-freeze-contract.json`
- **pinned-values path:** `corpus/tools/dependency-freeze-contract.json` (per-fixture event → sorted `depends_on` sets, event endpoints, relation endpoint triples, per-file and content SHA-256 digests). Note: the delivered contract also carries one foreign scratch pin `c3red` written by a verifier `--freeze` probe; closure should remove it or scope-guard `--freeze`.
- **scope:** verifies the frozen dependency edges, event endpoints and relation endpoints of the named continuation-chain fixtures against the committed pin; semantic inventory findings decide first (exit 1), and a content change the inventory does not model exits 2. Not a canon, chronology, entailment, rights, or permission judgment.
- **owner:** `lore-shokunin`

## P4. C9 watch row 5 (append to corpus/knowledge/r91-c9-watch.md)

## 2026-10-17 — r96 re-check (fifth)

Fifth periodic re-check, executed at the r96 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r96) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 5 (r96 closure): delivered discrimination held; the `e97613c` control reported REGRESSION-DETECTED as expected; ruling retained. Next re-check: r97. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r96 changes the sequence-scope evidence state.

## P5. Stale wording list

1. corpus/README.md:36 "(22 persisted cases)" → 24; "rounds 94–95" → 94–96; classes list. [LIVE]
2. SKILL.md:87 "22 cases (r95 added …)" → 24; "(r95 debt)" schema_drift sentence → delete. [LIVE]
3. SKILL.md:89 residuals "(deletion class, hidden-second-pointer D1, drift scope)" → superseded by C1. [LIVE]
4. corpus/README.md:37 tool list omits `dependency_freeze.py`. [LIVE]
5. corpus/tools/README.md Round-95 addendum "22 cases" (lines 101–114) — historical section; Q2's Round-96 addendum supersedes (pending). [history — verify Q2]
6. corpus/fixtures/README.md:1190 "22 total" — historical Round-95 section; Round-96 section supersedes. [history]
7. SCORECARD.md r95 "planned (r96)" debt block — superseded by L1's r96 admitted section at closure. [L1 closure]

## Anomalies / evidence for L1

- `corpus/tools/dependency-freeze-contract.json` carries foreign pin `c3red` (fixture label `.ufo/waves/round-96/seats/V41-scratch/c3red`, revision 60dba0c) written by a verifier `--freeze` probe; V22/V33 receipts quote the pin list including it. Harmless to verification (basename-keyed) but a tool hazard and a doc-relevant wart.
- /tmp tmpfs exhausted transiently during the round (two `mktemp`/redirect failures, "No space left on device") under the 64-seat load; workarounds used scratch-local TMPDIR. Harness observation, not a lane defect.
