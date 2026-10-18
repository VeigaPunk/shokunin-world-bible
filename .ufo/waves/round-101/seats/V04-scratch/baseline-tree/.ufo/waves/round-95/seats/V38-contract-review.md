# V38 — contract-review (round 95)

Seat: V38 contract-review. Scope per seat spec: after P2 lands, hand-derive the
expected exit+finding for the two new persisted self-test cases (`map_missing`,
`invalid_arguments`) from the tool's documented contract BEFORE reading P2's
persisted values, then compare; verify the 22-case self-test passes with
persisted (not regenerated) expectations; verify corpus/ hashes are unchanged by
`--self-test`.

Baseline: HEAD `fb118c4` (r94 closure); working tree clean except `M LOG.md`
(round declaration) and untracked `.ufo/waves/round-95/`.

Verified revision (all runs below): tool
`corpus/tools/map_obligations.py` sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`,
contract `corpus/tools/map-obligations-contract.json` sha256
`8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`,
README `corpus/tools/README.md` sha256
`5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264`
(hashes re-confirmed identical after P2's report landed, 19:31:44Z; all P1–P5
reports present).

## Step 1 — hand-derivation recorded BEFORE P2 landed (2026-10-17T19:17:54Z)

Baseline inputs used for the derivation (all pre-r95):

- `corpus/tools/map-obligations-contract.json` sha256
  `349a1956714c4496bbd17a00be00e3cd66a173edac015b88fdf10809e8fc7a50`
  — 20 persisted cases; `exit_codes` = `{"0": "PASS", "1": "FAIL", "2": "ERROR"}`.
- `corpus/tools/map_obligations.py` @ `fb118c4` sha256
  `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790`
  — `SELF_TEST_CASES` had 20 entries; the finding vocabulary already included
  `map_missing` (in `resolve_map`) and `invalid_arguments` (in `CliParser.error`
  and the three usage guards in `main`).
- `corpus/tools/README.md` @ `fb118c4` sha256
  `f2011009907e343560e5eccd795d495ecca93e967e6929f8383bb578e65f7169`
  — documented exit contract: "`0` clean; `1` failed comparison; `2`
  could-not-evaluate (unsupported map grammar, malformed raw JSON, invalid
  paths, usage errors)".

Hand-derived expectations (before reading any P2-persisted value):

- `map_missing` ⇒ exit **2**, `RESULT ERROR`, `finding_ids` **["map_missing"]**.
  Reasoning: `resolve_map` fails with `map_missing` when zero conventional map
  candidates exist; that happens before raw-file parsing, so exactly one finding
  is emitted; documented exit 2 = ERROR.
- `invalid_arguments` ⇒ exit **2**, `RESULT ERROR`, `finding_ids`
  **["invalid_arguments"]**. Reasoning: every usage-error path (`CliParser.error`
  → `ToolError`; `--self-test` combined with an operand; `--frozen` combined
  with an operand; no cluster argument) emits exactly one `invalid_arguments`
  finding through `emit(2, …)`; documented exit 2 = ERROR.

## Step 2 — baseline CLI probes confirming the derivation

Run on the read-only r94 tool (no repo writes; fixture cluster in /tmp):

```
$ python3 corpus/tools/map_obligations.py /tmp/v38-probe/cluster-nomap   # raw JSONs, no map file
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py
FINDING invalid_arguments: cluster directory is required
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py --bogus-flag
FINDING invalid_arguments: unrecognized arguments: --bogus-flag
RESULT ERROR
exit=2   (stderr empty)

$ python3 corpus/tools/map_obligations.py --frozen /tmp/v38-probe/cluster-nomap /tmp/v38-probe/cluster-nomap
FINDING invalid_arguments: --frozen cannot be combined with cluster or --map
RESULT ERROR
exit=2   (stderr empty)

$ python3 corpus/tools/map_obligations.py --self-test /tmp/v38-probe/cluster-nomap
FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen
RESULT ERROR
exit=2   (stderr empty)
```

All five probes match the hand derivation exactly (exit 2, single finding with
the case's own ID, one `RESULT ERROR` line, empty stderr).

Baseline corpus manifest recorded at 19:17:41Z: 1783 files hashed to
`/tmp/v38-corpus-manifest-before.txt` (scratch, outside repo).

Mid-flight observation (independent corroboration of P2's report §1a): at
19:23:15Z the then-current P1 revision already listed 22 `SELF_TEST_CASES`
including both new IDs, but `prepare_test_case` had no branch for either and
`run_cluster` still treated `parse_map` as returning a bare row list. I did not
verify that partial revision; the delivered revision (tool mtime
`1792265187` = 16:26:27 local) contains
`if case_name in {"complete", "invalid_arguments"}: return` (line 638),
`map_missing` unlink branch (line 651), the no-operand invocation
(`elif case_name == "invalid_arguments": pass`, line 728), and the 4-tuple
`run_cluster` (lines 438–442).

## Step 3 — persisted values vs the locked derivation

Comparison via `/tmp/v38-compare.py` (baseline contract read from
`git show fb118c4:…`, delivered read from the working tree):

```
baseline cases: 20  delivered cases: 22
new IDs: ['map_missing', 'invalid_arguments']
removed IDs: []
inherited rows changed vs baseline: none
inherited row order preserved: True

map_missing:       derived={'exit': 2, 'finding_ids': ['map_missing']}       persisted={'id': 'map_missing', 'exit': 2, 'finding_ids': ['map_missing']}       MATCH=True
invalid_arguments: derived={'exit': 2, 'finding_ids': ['invalid_arguments']} persisted={'id': 'invalid_arguments', 'exit': 2, 'finding_ids': ['invalid_arguments']} MATCH=True
```

Also: unique IDs True; row types valid; `exit_codes` unchanged
(`{"0": "PASS", "1": "FAIL", "2": "ERROR"}`); the only other top-level change
is the new `legacy_pointer_dialect` key (C3 documentation). The 20 r94 rows are
value- and order-identical to `fb118c4`; P2's reported `8 insertions, 1
deletion` in the contract is consistent with appending two rows plus the new
key block and adding a trailing comma to the previous last row.

The two new rows as persisted (`corpus/tools/map-obligations-contract.json:51-52`):

```json
{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]},
{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}
```

## Step 4 — delivered 22-case self-test with persisted expectations

```
$ python3 corpus/tools/map_obligations.py --self-test
... SELF-TEST PASS lines = 22, SELF-TEST FAIL lines = 0
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
RESULT PASS
exit=0   (stderr 0 bytes)
```

Persisted-not-regenerated evidence:

- Contract sha256 and mtime (`1792265222` = 16:27:02 local) identical before and
  after the self-test run; tool sha256/mtime likewise unchanged.
- Source inspection: `load_test_expectations` only reads the contract
  (`map_obligations.py:691-695`); no `write_text`/`write_bytes`/`json.dump`
  call anywhere in the tool targets the contract path (all writes target
  scratch fixtures / frozen snapshot files).
- Tamper control (Step 5) shows the persisted file actually drives verdicts.

Corpus invariance:

```
$ find corpus -type f | sort | xargs sha256sum > /tmp/v38-hash-pre-final.txt    # 1794 files
$ python3 corpus/tools/map_obligations.py --self-test    # exit 0
$ find corpus -type f | sort | xargs sha256sum > /tmp/v38-hash-post-final.txt
$ diff /tmp/v38-hash-pre-final.txt /tmp/v38-hash-post-final.txt
CORPUS UNCHANGED BY --self-test
```

No leftover `map-obligations-self-test-*` scratch at the repo root after the
run (`ls -d map-obligations-self-test-*` → none). Transient scratch dirs from
concurrent seats' runs were observed during the round (e.g.
`map-obligations-self-test-hwsfqdca/` at 19:21) and removed on clean exit;
BR-05 (scratch under repo root, not gitignored) remains open and is disclosed
in P2's README addendum.

## Step 5 — tamper control (negative proof that expectations are persisted)

Mirror layout `/tmp/v38root/corpus/tools/` (so `ROOT=parents[2]=/tmp/v38root`),
delivered tool + contract copied in; script `/tmp/v38-tamper-control.sh`:

- Control A (untampered mirror): `RESULT PASS`, exit 0.
- Control B (persisted `map_missing` expectation tampered 2→0):
  `SELF-TEST FAIL map_missing exit=2 findings=['map_missing']`,
  `FINDING self_test_mismatch: isolated CLI outcomes differ from persisted
  expectations`, `RESULT ERROR`, exit 2.
- Control C (contract restored from the repo): `RESULT PASS`, exit 0.

So the self-test verdict is driven by the persisted contract bytes, not
regenerated at runtime, and a wrong persisted expectation is caught (exit 2).

## Step 6 — observations (contract-text precision and doc parity)

1. **SKILL.md gate-registry row is now stale** — `SKILL.md:87` still says
   "20 cases with independently persisted expected exits and finding IDs".
   The delivered contract has 22. SKILL.md is read-only this round (not in
   P1–P5 ownership), so this is a closure/next-round parity item, not a P2
   defect. `SKILL.md:89`'s scope sentence ("for the canonical map form used by
   the r93 and r94 clusters") is likewise understated after C3 but not false.
2. **`legacy_pointer_dialect.fallback` overstates acceptance for one cell
   shape.** The contract says "canonical file.json#/pointer cells remain
   accepted in a legacy-header table". Measured:
   - canonical cell in canonical shape under a legacy header → `RESULT PASS`
     exit 0 (minimal fixture `/tmp/v38-probe/canon-legacy-a`; also r88 P/E-row
     shapes after 1:1 substitution);
   - canonical token carrying the r88-style legacy tail
     (`` `timeline.json#/0` (`description`, `source_id`): prose ``) → exit 2
     `unsupported_map` (minimal fixture `/tmp/v38-probe/canon-legacy-b`).
     A full 1:1 canonical-pointer substitution into the r88 map
     (`/tmp/v38-probe/r88-canonical3`) exits 2 and the only failing rows are
     T1/T2 — the two rows whose cells use the `(fields): prose` tail.
   Behavior is defensible (no corpus fixture needs a canonical token with a
   legacy tail; C3 only requires the field-path form), but the contract
   sentence as written is broader than the code. Suggested tightening for the
   byte owner: "canonical cells in canonical cell shape (backticked pointer,
   optional parenthetical note) remain accepted; a canonical pointer carrying a
   legacy `(fields): prose` tail is rejected as `unsupported_map`."
3. **`schema_drift` is not enumerated in the persisted contract JSON** (no
   top-level key, no self-test case). It is documented in the README Round-95
   addendum, and the round claim only required the two new self-test cases, so
   this is an observation, not a claim violation. The BR-02 mutation demo
   itself is other seats' scope.
4. Adjacent sanity (not this seat's claims, quoted for context): delivered tool
   gives r94 `14/14 RESULT PASS` exit 0, r93 `12/12 RESULT PASS` exit 0, r88
   `raw=10 mapped=10` + `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2;
   TOTAL-ROWS 12/12` exit 0, r87 exit 2 `unsupported_map`, r89 exit 2
   `unsupported_map` — consistent with the round declaration.
5. The r94 README addendum's "20/20 SELF-TEST PASS" line is kept as delivered
   history and explicitly superseded by the Round-95 addendum; acceptable.

Limits: all receipts above are for the quoted revision hashes. I did not verify
C1's BR-02 mutation exit-1 demo, C2's fixture claims, or C3's receipt set
beyond the adjacent sanity in item 4 — those are other seats' scopes. My run
itself left no repo writes beyond this report; fixtures/scratch live in /tmp.

**Bottom line: PASS — the delivered 22-case self-test passes (22 PASS lines,
RESULT PASS, exit 0, empty stderr) with persisted expectations proven
load-bearing by a tamper control, corpus/ hashes are unchanged by the run, and
both new persisted rows (`map_missing`, `invalid_arguments` → exit 2 + own
finding) match my pre-P2 hand-derivation exactly; one bounded contract-text
precision gap (legacy-header canonical-cell fallback wording) and the stale
`SKILL.md:87` "20 cases" line are reported for closure.**
