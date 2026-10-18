# V47 — c1-negative-rerun-2 (round-96)

**Seat:** V47 `c1-negative-rerun-2` — independent re-implementation of the negative matrix
(all nine classes) with a **fresh script**, on an **independently built synthetic base**, then
FINDING-ID comparison against V06 (`V06-c1-negative-rerun.md`).
**Subject (delivered):** `corpus/tools/map_obligations.py` sha256
`2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` (sha re-checked identical
before and after every run batch; Q1's declared delivered revision).
**Baseline (control):** r95 tool sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` — verified byte-identical
to `git show dcb2d92:corpus/tools/map_obligations.py` (closure commit).
**Harness:** `V47-scratch/matrix.py` sha256 `36bf1a4b…38f0f0` (my own construction; no reuse of
V06/V04/R95 harnesses or fixtures). Raw captures: `V47-scratch/hardened/matrix-results.json`
sha256 `9741bcc9…cf21c` (delivered) and `V47-scratch/control-r95/matrix-results.json`
sha256 `7f2550d4…87285` (baseline). Every probe ran **twice**; all 21 probes + base are
byte-stable across repeats (`stable all: True`).
All commands from the lane repo root with `python3`.

---

## 1. Poll-wait record (protocol compliance)

Two pollers, 20 s cadence, 40-try budget, logs in `V47-scratch/`:

- `poll-q1.log`: first `try=1 tool_sha=d1c239cc… dual=0 inv=0 contract_cases=22 q1_report=none`;
  `READY try=29 tool_sha=2b0ba815… contract_cases=24 q1_report=.ufo/waves/round-96/seats/Q1-tool-hardening.md`.
  Nine distinct tool shas observed mid-iteration (`8729f1f3…`, `44a6ffd4…`, `c2c284c0…`,
  `6634e176…`, `2b0ba815…` among them); no run was taken against a plan or an unreported revision.
- `poll-v06.log`: `READY try=28 v06_report=.ufo/waves/round-96/seats/V06-c1-negative-rerun.md`
  (sha256 `2aa1cc20…05ad579`).

## 2. Method

- **Base:** my script builds a synthetic cluster from scratch — 2 entities × (first_appearance +
  1 claim) + 1 relation + 1 timeline record = 6 raw obligations, canonical-header map
  (`JSON fact pointer and fields`), declared inventory `6 JSON facts; 0 editorial rows; 6 total
  mapped rows`, so the pristine base is `RESULT PASS` exit 0. No fixture file is copied from any
  seat or from the corpus.
- **Nine classes / 21 probes:** N1 missing row (raw claim intact), N2 duplicate row, N3 phantom
  row, N4 source-ID mismatch, N5 malformed JSON, N6 map-path errors (f1 missing / f2 foreign /
  f3 traversal / f4 directory), N7 schema_drift, N8 deletion class (claims key + its map row),
  N9 dual_pointer (4 forms) + 2 no-false-fire legacy controls + N10/N11 canonical-note
  boundaries + N12 malformed declaration; N8b declaration-consistent shrink probe.
- Each probe: fresh copy, mutation applied, **real CLI** invocation of the live tool, capture of
  exit + sorted FINDING IDs + `INVENTORY` receipt; two runs each.

## 3. Control run — r95 tool `d1c239cc…` (proves harness fidelity)

```
BASE                exit=0 findings=none
N1_missing_row      exit=1 findings=['missing_obligation']        inv=5/6 MISMATCH (non-gating)
N2_duplicate_row    exit=1 findings=['duplicate_mapping']         inv=7/6 MISMATCH (non-gating)
N3_phantom_row      exit=1 findings=['phantom_obligation']        inv=7/6 MISMATCH (non-gating)
N4_source_mismatch  exit=1 findings=['source_id_mismatch']
N5_malformed_json   exit=2 findings=['malformed_json']
N6f1..f4            exit=2 findings=[map_missing, foreign_path, unsafe_path, map_missing]
N7_schema_drift     exit=1 findings=['schema_drift']
N8_deletion_class   exit=0 findings=none        inv=5/6 MISMATCH  <-- carried defect reproduced
N9/N9b/N9c/N9d      exit=0 findings=none                          <-- V37-D1 reproduced (all 4)
```

The r94-lineage IDs and the three carried residuals (silent deletion class, silently-ignored
legacy dual pointers, non-gating inventory) all reproduce — the harness is faithful.

## 4. Delivered run — r96 tool `2b0ba815…`

```
BASE                 exit=0 findings=none
N1_missing_row       exit=1 findings=['inventory_mismatch','missing_obligation']
N2_duplicate_row     exit=1 findings=['duplicate_mapping','inventory_mismatch']
N3_phantom_row       exit=1 findings=['inventory_mismatch','phantom_obligation']
N4_source_mismatch   exit=1 findings=['source_id_mismatch']
N5_malformed_json    exit=2 findings=['malformed_json']
N6f1_map_missing     exit=2 findings=['map_missing']
N6f2_foreign_path    exit=2 findings=['foreign_path']
N6f3_traversal       exit=2 findings=['unsafe_path']
N6f4_map_is_dir      exit=2 findings=['map_missing']
N7_schema_drift      exit=1 findings=['schema_drift']
N8_deletion_class    exit=1 findings=['inventory_mismatch']       <-- was exit 0
N8b_consistent_shrink exit=0 findings=none                        <-- boundary probe (see §6)
N9_dual_pointer      exit=1 findings=['dual_pointer']             <-- was exit 0
N9b_dual_canonical   exit=1 findings=['dual_pointer']
N9c_dual_colon       exit=1 findings=['dual_pointer']
N9d_dual_unbackticked exit=1 findings=['dual_pointer']
N9e_legacy_control   exit=0 findings=none
N9f_legacy_prose_control exit=0 findings=none
N10_canonical_note   exit=2 findings=['unsupported_map']
N11_legacy_canonical_first exit=2 findings=['unsupported_map']
N12_inv_malformed    exit=1 findings=['inventory_mismatch']       inv=declaration-malformed
```

Representative raw captures (delivered):

```
$ python3 corpus/tools/map_obligations.py …/N8_deletion_class
OBLIGATIONS raw=5 mapped=5
INVENTORY JSON-FACTS 5/6; EDITORIAL-ROWS 0/0; TOTAL-ROWS 5/6 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 6/0/6; observed 5/0/5
RESULT FAIL   (exit 1; r95 control on same input: RESULT PASS exit 0)

$ python3 corpus/tools/map_obligations.py …/N9_dual_pointer
OBLIGATIONS raw=6 mapped=6
FINDING dual_pointer: row P2 (line 10) names a second pointer token 'timeline[0]' alongside entities.json#/0/claims/0
RESULT FAIL   (exit 1; r95 control: RESULT PASS exit 0)
```

## 5. FINDING-ID comparison against V06 (the seat deliverable)

Class-level (V06 groups a–f, g, h, i = nine classes; mine N1–N9):

| class | V06 case → IDs (r96) | my probe → IDs (r96) | agreement |
|---|---|---|---|
| missing_obligation | a → `[missing_obligation]` | N1 → `[inventory_mismatch, missing_obligation]` | ID present in both; extra explained (see below) |
| duplicate_mapping | b → `[duplicate_mapping]` + extra `[inventory_mismatch]` | N2 → `[duplicate_mapping, inventory_mismatch]` | identical sets |
| phantom_obligation | c → `[inventory_mismatch, phantom_obligation]` | N3 → same | identical |
| source_id_mismatch | d → `[source_id_mismatch]` | N4 → same | identical |
| malformed_json | e → exit 2 `[malformed_json]` | N5 → same | identical |
| map-path errors | f1/f2/f3/f4 → exit 2 `[map_missing, foreign_path, unsafe_path, map_missing]` | N6f1–f4 → same | identical |
| schema_drift | g1 → `[inventory_mismatch, schema_drift]`; g2 → `[phantom_obligation, schema_drift]` | N7 → `[schema_drift]` | ID present in all; extras differ by mutation shape |
| inventory_mismatch (deletion) | h1/h2 → `[inventory_mismatch]` exit 1 | N8 → `[inventory_mismatch]` exit 1 | identical |
| dual_pointer | i1/i2/i3/i5/i6/i7 → `[dual_pointer]` exit 1; i4 → `[dual_pointer, missing_obligation]` | N9/N9b/N9c/N9d → `[dual_pointer]` exit 1 | identical |
| no-false-fire controls | ctrl-legacy-note/prose exit 0; ctrl-canonical-note exit 2 `unsupported_map`; ctrl-inv-declared-wrong exit 1 `inventory_mismatch`; ctrl-inv-malformed exit 1 `inventory_mismatch` | N9e/N9f exit 0; N10/N11 exit 2 `unsupported_map`; N12 exit 1 `inventory_mismatch` | consistent (N11 and N8b are additional boundaries) |

**Apparent mismatch resolved by direct inspection.** V06's case-a showed no `inventory_mismatch`
extra; I ran the delivered tool on V06's actual `case-a` inputs (read-only) and diffed them
against its base: case-a **adds** a raw claim (`entities.json#/0/claims/1`) with no map row
(`raw=13 mapped=12`, declaration 12/12 → observed matches declaration → no gate). My N1
**deletes** an existing map row (`raw=6 mapped=5` → observed 5 vs declared 6 → gate fires).
Same class ID, different mutation shape — no tool discrepancy. (V06's b/c extras carry
`inventory_mismatch` for exactly the reason mine do: the mutation changes observed row count.)

**Independent delivered-fixture probe.** On a scratch copy of `corpus/fixtures/r96-crossing-response`
(claims key + its map row J06 removed, not the synthetic base):

```
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/18 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17
RESULT FAIL   EXIT=1
```

This matches V06's `case-r96-del` probe byte-for-byte in exit and ID, on a separately built copy.

## 6. Honest extras / boundaries (recorded, not hidden)

1. **Inventory gate co-fires on any row-count-changing mutation** (N1/N2/N3). The r94 lineage's
   "row deleted only" variant therefore gains `inventory_mismatch`; the class ID and exit 1 are
   preserved, and the co-fire is the same behavior V06 records for b/c. Not a regression, but a
   disclosed ID-set change for negative inputs that carry a declaration.
2. **Declaration-consistent shrink stays silent** (N8b: claims key + map row + declaration all
   shrink together → exit 0). Inherent to declared-vs-observed checking; the claim's specific
   mutation (stale declaration) gates, this boundary does not. Worth carrying as a bounded
   residual.
3. **dual_pointer is broader than backticks** — a bare prose token (`(see also timeline[0])`,
   N9d) fires; fail-closed, consistent with V06's i5 boundary probe.
4. **No legacy-grammar relaxation**: canonical-header note (N10) and legacy cell whose first
   token is canonical (N11) remain `unsupported_map` exit 2.
5. **Malformed declaration gates fail-closed** (N12 → `inventory_mismatch` exit 1), matching
   V06's ctrl-inv-malformed and Q1's declared residual 3.

## 7. Hygiene

- Writes confined to `V47-scratch/` (poller scripts/logs, `matrix.py`, result JSONs, frozen
  intermediate snapshot) and this report; no corpus file written, no commits, no pushes, no
  network. `git status --short` shows only other seats' artifacts.
- Delivered sha `2b0ba815…` re-checked before and after every run batch — unchanged throughout.

**Bottom line: PASS — all nine negative classes reproduce V06's FINDING IDs (and exits) on an
independently built fresh harness against the delivered tool `2b0ba815…`, with the two carried
defects (silent deletion class, silently-ignored legacy dual pointers) closed, no false-fire on
any control, byte-stable across repeats, and the single apparent cross-seat mismatch explained
by mutation shape rather than tool behavior.**
