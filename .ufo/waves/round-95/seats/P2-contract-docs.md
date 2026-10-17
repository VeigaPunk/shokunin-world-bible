# P2 — contract-docs seat report (round 95)

Seat: P2 contract-docs. Owned files (only these two written, plus this report):
`corpus/tools/map-obligations-contract.json`, `corpus/tools/README.md`.
Baseline: r94 closure `fb118c4`. No commits, no pushes, no network, no nested agents.
Scratch: `/tmp` only (`/tmp/p2-*`); no repo scratch dir declared for this seat, no repo residue.

Deliverable state at report time: `git diff --numstat` →
`20  0  corpus/tools/README.md` and `8  1  corpus/tools/map-obligations-contract.json`
(the one deleted line is the r94 `frozen_verdict_mismatch` entry re-emitted with a trailing comma).

## 1. Poll-wait: P1's final tool revision

Poll loop (20 s cadence, `schema_drift` present + P1 report present + mtime stable):

```
try=29 mtime=1792265187 stable=no  report=none schema_drift_hits=1
try=33 READY try=33 mtime=1792265187 report=.ufo/waves/round-95/seats/P1-tool-code.md schema_drift_hits=1
```

Final revision verified: `corpus/tools/map_obligations.py` sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, size 33320,
mtime `2026-10-17 16:26:27.696443074 -0300`. All receipts below are from that revision.

### 1a. Mid-flight defect observed and disclosed (evidence, fixed by P1 before its report)

At 16:25, on P1's then-current revision (mtime 16:24:43, size 33297), `prepare_test_case`
had no branch for `invalid_arguments`. Direct call proof:

```
SELF_TEST_CASES count: 22
map_missing prepared OK; files: ['entities.json', 'relations.json', 'timeline.json']
invalid_arguments ToolError: self_test_contract | unknown self-test case 'invalid_arguments'
```

so `--self-test` could not reach 22/22 on that revision. I did not touch P1's file
(byte ownership); I persisted the contract anyway so that any self-test run would
surface the true defect rather than a contract-set mismatch. P1's next revision
(16:26:27) added `if case_name in {"complete", "invalid_arguments"}: return`
(`map_obligations.py:638`) and the no-argument CLI invocation (`:728`), and the
delivered revision now passes.

## 2. Hand-derived expectations, persisted, and confirmed

Hand-derivation was done from the delivered contract text before writing (no
persisted P2 value existed yet). Sources: `exit_codes` = `{"0":"PASS","1":"FAIL","2":"ERROR"}`;
r94 README exit contract "`2` could-not-evaluate (unsupported map grammar, malformed
raw JSON, invalid paths, usage errors)"; `resolve_map` (`map_obligations.py:114-135`);
`CliParser.error` (`:70`) and the three usage guards (`:791`, `:795`, `:801`);
case preparation (`:638`, `:651`) and invocation (`:728`).

- `map_missing` ⇒ exit **2**, finding_ids **["map_missing"]**.
  Fixture: raw tables written, then `claim-excerpt-map.md` unlinked → `resolve_map`
  finds zero conventional candidates → `fail("map_missing", ...)`, one finding.
- `invalid_arguments` ⇒ exit **2**, finding_ids **["invalid_arguments"]**.
  Fixture written but unused; CLI invoked with no operand → `main` guard
  `cluster directory is required` → one `invalid_arguments` finding.
  Cross-checked against the r94 tool's live usage paths (all exit 2, single finding):
  no args → `invalid_arguments: cluster directory is required`;
  `--self-test <dir>` → `invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen`;
  `--nope` → `invalid_arguments: unrecognized arguments: --nope`.

Persisted entries (appended; the 20 r94 entries verified byte-identical in order):

```json
{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]},
{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}
```

No expectation needed correction: both matched the delivered behavior on the first run
of the frozen revision. The only mismatch ever observed was P1's missing
`prepare_test_case` branch (§1a), which was a tool defect, not a wrong expectation.

## 3. `--self-test` after the contract edit — 22/22

```
$ python3 corpus/tools/map_obligations.py --self-test
... 22 lines "SELF-TEST PASS ..." (including
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments'])
RESULT PASS
exit=0          # PASS lines=22, FAIL lines=0
```

Hash stability across the self-test (no live-tree write by the tool):

```
HASHES STABLE across --self-test
# contract + README + tool sha256 identical before and after; no map-obligations-self-test-* residue
```

## 4. README addendum (append-only)

`git diff corpus/tools/README.md` = **20 insertions, 0 deletions**; the r94 text is
preserved verbatim (`new.startswith(old)` → `True`, old 10721 B → new 14082 B).
Added `### Round-95 addendum: schema_drift, 22-case self-test, r88 map dialect (2026-10-17)` covering:

- **`schema_drift` class (BR-02)** — exit 1, stable FINDING ID, demonstrated mutation,
  with the bounded scope (entity claim containers only; not general schema validation).
- **22-case self-test** — the two new persisted cases with their exits/findings, and
  the note that the contract is compared as a case set, not an order.
- **r88 dialect coverage** — `OBLIGATIONS raw=10 mapped=10` /
  `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS`
  exit 0, the dialect gate (legacy `JSON fact and fields` column, field-path tokens
  translated to canonical pointers, canonical cells still accepted), r87/r89 fail-closed
  preserved, r93/r94/frozen unchanged, and the new `INVENTORY` receipt line.
- **Honest bound** — the `INVENTORY ... MISMATCH` line is a receipt, not a gate: a
  tampered declared count alone leaves exit 0 (observed below).
- **BR-05** explicitly stated as still open (self-test scratch still under the repo
  root and not gitignored), so the r94 "relocation candidate for r95" line is not
  misread as closed.

## 5. Cross-checks (all on the frozen revision, quoted from actual runs)

```
r88-m3-maya-cluster          OBLIGATIONS raw=10 mapped=10
                             INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
                             RESULT PASS            exit=0
r87-myth-cluster             FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer   exit=2
r89-inspiration-paraphrase   FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column     exit=2
r93-m2-kojiki-cluster        OBLIGATIONS raw=12 mapped=12 / RESULT PASS   exit=0
r94-paired-crossing          OBLIGATIONS raw=14 mapped=14 / RESULT PASS   exit=0
--frozen round-94/map-obligations-r93   SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 matched / RESULT PASS  exit=0
```

BR-02 mutation (scratch copy of `r94-paired-crossing`: `claims`→`assertions` on
entities[0] with content preserved, map row `entities.json#/0/claims/0` removed):

```
OLD tool (git fb118c4)   OBLIGATIONS raw=13 mapped=13 / RESULT PASS                      exit=0   (silent)
DELIVERED tool           OBLIGATIONS raw=13 mapped=13
                         INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                         FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
                         RESULT FAIL                                                     exit=1
```

Control (rename kept, map row kept): exit 1 with `phantom_obligation` + `schema_drift`.
Inventory-receipt bound (declared `14` facts tampered to `13`, map otherwise intact):
`INVENTORY JSON-FACTS 14/13; ... TOTAL-ROWS 16/16 MISMATCH` / `RESULT PASS` exit 0 —
the receipt does not gate, documented as such in the addendum.

## 6. Disclosures beyond the two persisted cases

1. **`legacy_pointer_dialect` key added to the contract** (one new top-level key; no
   prior key or value changed). It documents the r88 acceptance gate that C3 ships,
   cited to code: `LEGACY_POINTER_COLUMN`/`LEGACY_POINTER` (`map_obligations.py:19-25`),
   `legacy_pointer`/`parse_pointer_cell(cell, legacy)` (`:154-179`), dialect selection
   by normalized pointer-column header (`:292-303`). Verified empirically by the r88
   PASS, the r87/r89 exit-2 runs, and the `legacy_grammar` self-test case.
2. **"12/12" is the r88 inventory receipt, not an obligation count.** r88 has 10 raw
   obligations (4 `first_appearance` + 4 entity claims + 2 timeline events; relations
   empty); 12 is the map's declared total row count (10 JSON facts + 2 editorial rows).
   The tool prints both numbers correctly labeled (`raw=10 mapped=10`,
   `TOTAL-ROWS 12/12`), matching P1's §6.1.
3. **The r93/r94 example receipts in the r94 addendum now gain one `INVENTORY` line**;
   their `OBLIGATIONS`/`RESULT` lines and exit codes are unchanged. Disclosed in the
   addendum rather than rewriting the r94 text.
4. **Scope kept:** no other corpus, tool, checker, knowledge, or past-wave byte was
   touched by this seat; `git status --porcelain` shows only the round's producer files
   (`LOG.md`, `corpus/tools/*`, `corpus/fixtures/r95-crossing-aftermath/`,
   `corpus/knowledge/r95-aftermath-scope-note.md`) plus `.ufo/waves/round-95/`.

**Bottom line: PASS — contract persists 22 cases (20 r94 entries byte-identical plus hand-derived `map_missing`/`invalid_arguments`), `--self-test` is 22/22 `RESULT PASS` exit 0, the README Round-95 addendum is append-only (20 insertions, 0 deletions) and states only receipts reproduced in this report; one mid-flight P1 defect (`invalid_arguments` case unimplemented) was found by this seat and fixed by P1 before its report, and is disclosed here.**
