# V02 — c1-selftest seat report (round 95)

- Seat: V02 `c1-selftest`. Report path (only file written by this seat): this file.
- Baseline: r94 closure `fb118c4` (`lore r94: close round — SCORECARD admitted section + LOG closure`, 2026-10-17 16:05:45 -0300). Round: r95, 64-seat single wave, lore-shokunin.
- Scope: C1 self-test / contract cross-check. Poll-wait for P1 + P2; `--self-test` at 22/22 exit 0; 22 persisted cases must match printed behavior **without regenerating anything**; `map_missing` and `invalid_arguments` present and meaningful; `corpus/` hashed before/after the run to prove no live-tree writes.
- Scratch: `/tmp/v02/c1/` only (harness, mutation copies, captures). No repo scratch dir declared for this seat; nothing outside this report path was written in the repo. No commits, no pushes, no network, no nested agents.

## 0. Poll-wait outcome and verified revision

Both producer reports landed inside the 40-try / 20 s window (P1 at try 35–37, P2 at try 39); no ABSENT.

| Artifact | sha256 | bytes | mtime |
|---|---|---|---|
| `corpus/tools/map_obligations.py` (P1) | `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` | 33320 | 16:26:27 |
| `corpus/tools/map-obligations-contract.json` (P2) | `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` | 2955 | 16:27:02 |
| `corpus/tools/README.md` (P2) | (not pinned) | 14082 | 16:28:26 |

Both producer hashes are stable across every run below (re-checked after P2's report landed). P1's own report pins the same tool hash; P2's pins the same tool + contract revision — no revision drift between producer receipts and mine.

Mid-flight observation (disclosed by P2 §1a, reproduced by me at 16:24–16:25): on P1's 16:24:43 revision `--self-test` failed closed with `FINDING self_test_contract: contract self-test cases do not match the implemented cases`, exit 2 (contract still at 20 cases). That revision is superseded; nothing below uses it.

## 1. C1 — `--self-test` on the delivered revision: 22/22 PASS, exit 0

Command (from repo root, hash-guarded harness `/tmp/v02/c1/hashcheck.sh`):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
exit=0
```

Captured stdout `sha256 900192a62e82a7c8a515955bd16077417cddb06196861ac685485602ddfacc90` (1457 bytes, 22 SELF-TEST lines + 1 RESULT line), stderr **0 bytes**. A second identical run reproduced the same bytes (`diff` empty → `SELFTEST_OUTPUT_IDENTICAL_TO_HASHGUARDED_RUN`).

**Expectation coverage:** the tool implements `SELF_TEST_CASES` with exactly these 22 ids and refuses to run if the contract's case set differs (`self_test_contract`, exit 2 — observed mid-flight above), so the persisted expectations cannot silently drift from the implementation.

## 2. C1 — persisted 22 cases vs printed behavior, without regenerating anything

Independent cross-check (`/tmp/v02/c1/crosscheck.py`, its own regex parser over the tool's stdout — it does not call any contract-writing code and writes nothing):

```
persisted_cases 22  printed_cases 22  n_pass 22
terminal_lines  ['RESULT PASS']  exit 0  stderr_bytes 0
new_case_ids    map_missing=(2, ['map_missing']) invalid_arguments=(2, ['invalid_arguments'])
schema_drift_in_contract False
STRICT_CROSSCHECK PASS
```

Checks performed and satisfied: case-id sets equal; per case the printed exit equals the persisted `exit`; the printed finding-id list (sorted) equals the persisted `finding_ids`; every line carries the `PASS` verdict; exactly one terminal `RESULT` line, equal to `RESULT PASS`; process exit 0; stderr empty. No case needed correction.

Nothing was regenerated: the contract file was hashed immediately before and after the run and is **byte-identical** (`CONTRACT_HASH_IDENTICAL`), i.e. the tool reads expectations and never writes them back. Contract structure cross-checked against `fb118c4`:

```
old n= 20 new n= 22
first20 identical (byte-level json): True
new keys in new contract: ['legacy_pointer_dialect']
old top-level keys all present: True
appended: ['map_missing', 'invalid_arguments']
```

So the 20 r94 entries are preserved verbatim and in order; only two case entries were appended plus one new documentation key (`legacy_pointer_dialect`, P2 §6.1). Exit distribution over the 22 cases: 15× exit 2, 5× exit 1, 2× exit 0.

## 3. C1 — the two new case IDs are present and meaningful

Both are present and each is the **only** case in the contract producing its finding id (`map_missing`: 1 case; `invalid_arguments`: 1 case).

- `map_missing` — harness branch `map_obligations.py:651` unlinks `claim-excerpt-map.md` after writing the raw tables, then the case is run as a normal cluster invocation; expectation `{"id": "map_missing", "exit": 2, "finding_ids": ["map_missing"]}`. Independent reproduction outside the harness (scratch copy of `r94-paired-crossing` with the map removed):
  ```
  $ python3 corpus/tools/map_obligations.py /tmp/v02/c1/nomap
  FINDING map_missing: expected exactly one conventional claim-to-excerpt map
  RESULT ERROR
  exit=2
  ```
- `invalid_arguments` — harness invokes the real CLI with **no operand** (`map_obligations.py:728`, `elif case_name == "invalid_arguments": pass`); expectation `{"id": "invalid_arguments", "exit": 2, "finding_ids": ["invalid_arguments"]}`. Independent reproduction:
  ```
  $ python3 corpus/tools/map_obligations.py
  FINDING invalid_arguments: cluster directory is required
  RESULT ERROR
  exit=2
  $ python3 corpus/tools/map_obligations.py --self-test corpus/fixtures/r94-paired-crossing
  FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen
  RESULT ERROR
  exit=2
  ```

**Precision note (evidence, not a defect):** both finding IDs pre-existed at `fb118c4` — `git show fb118c4:corpus/tools/map_obligations.py` already contains `fail("map_missing" if not candidates else "unsupported_map", ...)`, `CliParser.error → invalid_arguments`, and the `cluster directory is required` guard. The old tool on the map-removed copy prints the identical `FINDING map_missing … exit=2`. The two new *cases* therefore persist coverage of pre-existing behaviors (BR-03 closure), they do not introduce the behaviors; the round text ("two new persisted self-test cases") matches this reading.

**Coverage gap found by this seat (report exactly, do not paper over):** the C1 headline behavior — BR-02 `schema_drift` — is **not** pinned by any persisted self-test case. `schema_drift_in_contract False` (no contract entry expects that finding id), and no branch of `prepare_test_case` renames or reshapes a raw key (`case branches: ['missing','duplicate','phantom','source_id_mismatch','malformed_json','map_missing','co_mapped_grammar','legacy_grammar','invalid_pointer','empty_segment','noncanonical_index','noncanonical_claim_index','foreign_path','traversal_path','symlink_path']`; no `pop(`/`claims` rewrite in the case-prep block). A future regression that removed the drift check would still show `--self-test` 22/22 exit 0. The class is covered only by the mutation demo (below) and by the r94 fixtures' invariance.

## 4. C1 — no live-tree writes (corpus hash before/after)

Harness: `find corpus -type f | sort | xargs sha256sum` immediately before the self-test, the self-test, then the same inventory immediately after, in one script run.

```
selftest_exit=0
=== corpus hash diff (before -> after) ===
CORPUS_HASH_IDENTICAL
=== contract hash diff ===
CONTRACT_HASH_IDENTICAL
=== stray self-test dirs ===
before=0 after=0
=== git status diff ===
GIT_STATUS_IDENTICAL
=== stderr ===
```

- Recursive `corpus/` inventory: 1783 files at run time, `sha256 50331e1cfd9ce816f256f4f4cca1c2ecd924a532ba6a24978137f9295bc69ab9` on **both** sides (identical files, identical digests, identical order).
- Re-hash minutes later (after P2's report landed): `CORPUS_STILL_IDENTICAL` against the same before-file (now 1794 files — the extra 11 are P3/P4/P5 producer writes under `corpus/fixtures/r95-crossing-aftermath/` and `corpus/knowledge/r95-aftermath-scope-note.md`, not tool writes).
- Contract byte-identical before/after (no regeneration, §2).
- No `map-obligations-self-test-*` residue under the repository root (0 before, 0 after); whole-repo `git status --porcelain` unchanged across the run.
- Bound to state honestly: the self-test still creates a **transient** `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` under the repository root (r94 design; BR-05 remains open, and P2's README addendum says so). My check shows it is created and removed with no persistent residue and no git-status change; `corpus/` itself is never written.

## 5. C1 — BR-02 mutation demo against the delivered tool (independent of P1's copy)

Scratch copy of `corpus/fixtures/r94-paired-crossing` at `/tmp/v02/c1/mutation-claims-renamed`: `entities[0].claims` renamed to `claim_rows` (record content preserved byte-for-byte), map row `entities.json#/0/claims/0` (J06) deleted.

```
OLD tool (git fb118c4)   OBLIGATIONS raw=13 mapped=13 / RESULT PASS            exit=0   <- silent pass, BR-02
DELIVERED tool           OBLIGATIONS raw=13 mapped=13
                         INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                         FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_rows'
                         RESULT FAIL                                                      exit=1
CONTROL (unmutated copy) OBLIGATIONS raw=14 mapped=14
                         INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
                         RESULT PASS                                                      exit=0
```

The before→after C1 obligation is reproduced exactly: same mutation, old tool silent exit 0, delivered tool exit 1 with stable `FINDING schema_drift`.

## 6. Negative control — the 22/22 result is discriminating, not vacuous

Copied the delivered tool + contract to `/tmp/v02/c1/negctl/` and tampered one persisted expectation (`map_missing` → `exit 0, finding_ids []`):

```
$ python3 /tmp/v02/c1/negctl/corpus/tools/map_obligations.py --self-test
SELF-TEST FAIL map_missing exit=2 findings=['map_missing']
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

So a wrong expectation is caught (`self_test_mismatch`, exit 2); the live contract's 22/22 is a real match, not a harness that always passes. (This also confirms the contract is loaded from the tool's own directory, and that my §2 comparison has teeth.)

## 7. Adjacent regression evidence on the same delivered revision (C1's "unchanged" clauses)

```
r93-m2-kojiki-cluster   exit=0  OBLIGATIONS raw=12 mapped=12  INVENTORY 12/12; 3/3; 15/15  RESULT PASS
r94-paired-crossing     exit=0  OBLIGATIONS raw=14 mapped=14  INVENTORY 14/14; 2/2; 16/16  RESULT PASS
r88-m3-maya-cluster     exit=0  OBLIGATIONS raw=10 mapped=10  INVENTORY 10/10; 2/2; 12/12  RESULT PASS
r87-myth-cluster        exit=2  FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
r89-inspiration-paraphrase exit=2 FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
--frozen .ufo/waves/round-94/frozen/map-obligations-r93
                        exit=0  SNAPSHOT inputs=4 digests=verified / OBLIGATIONS raw=12 mapped=12
                                FROZEN expected=PASS/0 findings=none matched / RESULT PASS
```

`support_check.py` is untouched by the round (`git status --porcelain` lists only `LOG.md`, `corpus/tools/{map_obligations.py,map-obligations-contract.json,README.md}`, the r95 fixture, the r95 knowledge note, `.ufo/waves/round-95/`), and its receipts read identically before and after the producer edits: r93 `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; MODES 15/15` PASS; r94 `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16` PASS.

New receipt line disclosed by both producers and reproduced here: r93/r94/frozen stdout gained one `INVENTORY JSON-FACTS a/b; EDITORIAL-ROWS c/d; TOTAL-ROWS e/f` line. Their obligation counts, findings and exit codes are unchanged, and the line is a receipt, not a gate (P2 §5: a tampered declared count alone still exits 0).

## 8. Findings for the round (evidence; adjudication belongs to closure)

1. **Declaration-vs-evidence contradiction on C3's "12/12".** Raised independently by P1 (§6.1) and P2 (§6.2) and confirmed by my run: `r88-m3-maya-cluster` has **10** raw source-attributed obligations (4 `first_appearance` + 4 entity claims + 2 timeline events; `relations.json` empty). "12" is the map's declared total row count (10 JSON facts + 2 editorial rows — the same 12 rows `support_check` validates as `MODES 12/12`). The tool reports `OBLIGATIONS raw=10 mapped=10` plus `INVENTORY ... TOTAL-ROWS 12/12`, both correctly labelled. The round's C3 wording "12/12 PASS" is traceable only as the inventory/total-row figure, not as an obligation count.
2. **BR-02 behavior is unpinned by the persisted self-test** (§3) — the new cases close BR-03 coverage gaps but not for the schema_drift class itself.
3. **BR-05 still open** (§4): self-test scratch is created under the repository root and `.gitignore` (`.ufo/interactive-sessions/`, `__pycache__/`) does not cover it; the README addendum states this explicitly, so the r94 "relocation candidate for r95" is correctly not read as closed.
4. **Bounded residuals inherited from the producers' own reports**, not re-litigated here: drift fires only on claim-shaped records (`statement` + `source_id`) under an unexpected *entity* key — a rename that also changes inner record shape still passes silently, and relations/timeline are not drift-scanned (P1 §6.3); the `INVENTORY` line never gates (P2 §5).

## 9. Reproducibility

Scratch artifacts kept under `/tmp/v02/c1/`: `hashcheck.sh` (§4 harness), `crosscheck.py` (§2 cross-check), `selftest.out`/`selftest.err`, `corpus.hash.{before,after,now}`, `contract.hash.{before,after}`, `mutation-claims-renamed/`, `nomap/`, `control/`, `negctl/`. All commands above were run from the repository root with `python3` on the pinned revision.

Bottom line: **PASS** — on the pinned delivered revision (tool `d1c239cc…`, contract `8173bb97…`), `--self-test` prints 22/22 SELF-TEST PASS + `RESULT PASS`, exit 0, stderr empty; all 22 persisted expectations match printed exits/finding-ids exactly under an independent parser with the contract byte-identical before/after (nothing regenerated); the two new cases `map_missing` and `invalid_arguments` are present, uniquely identified, and reproduce outside the harness (both cover pre-existing finding ids); `corpus/` (1783 files) is byte-identical before/after the run with no residue and no git-status change; BR-02 is independently reproduced (old exit 0 silent → delivered exit 1 `schema_drift`) — with two caveats recorded, not waived: the persisted self-test does not pin `schema_drift`, and the round's r88 "12/12" is the map's total row count, not an obligation count.
