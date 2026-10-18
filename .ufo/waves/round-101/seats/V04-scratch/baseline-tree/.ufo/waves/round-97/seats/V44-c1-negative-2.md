# V44 — c1-negative-2 (round-97)

**Seat:** V44 `c1-negative-2` — independent nine-class matrix re-implementation against
`corpus/tools/map_obligations.py` (C1 subject), then FINDING-ID comparison against V04
(the parallel c1-negative seat, `V04-c1-negative-rerun.md` sha256
`c35e3254aeda63fdf1d8568399d4f8678594c6652e659e2f53e94c852babbf85`).
**Harness:** `.ufo/waves/round-97/seats/V44-scratch/matrix-v44.py` (my own fresh construction;
no reuse of V47/V06/V04 harnesses), sha256 `660d08d97a280c6dfcdd0689f21b99d6f8e82015ca18a9dd0846f1713b23b0b9`.
**Control (baseline):** r96 closure tool bytes from `git show f3e09f9:corpus/tools/map_obligations.py`,
sha256 `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8`
(frozen copy `V44-scratch/control-r96/map_obligations.py`).
**Subject (delivered):** `corpus/tools/map_obligations.py` sha256
`86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` (R1's declared delivered
revision; matches `R1-map-pinning.md` and `R2-contract-docs.md`), contract
`map-obligations-contract.json` sha256 `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`
(25 cases, `dual_pointer` pinned).
All commands from the lane repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

---

## 1. Poll-wait record (protocol compliance)

`V44-scratch/poll.sh` (20 s cadence, 40 tries) + `V44-scratch/gate.sh` (both producer reports
present AND tool+contract sha stable over 3 consecutive checks). Logs: `poll.log`, `gate.log`.

```
$ poll.sh  (V44-scratch/poll.log, excerpt)
CHECK try=1 t=20s  tool=86b529496214 contract=97b76bb8b1fe cases=24 dual=0 r1=none r2=none v04=none
CHECK try=2 t=40s  tool=86b529496214 contract=2142b9917694 cases=25 dual=1 r1=none r2=none v04=none
...
CHECK try=16 t=320s tool=86b529496214 contract=2142b9917694 cases=25 dual=1 \
  r1=.../R1-map-pinning.md r2=.../R2-contract-docs.md v04=none

$ gate.sh  (V44-scratch/gate.log, excerpt)
GATE try=5 t=100s r2=.../R2-contract-docs.md sha=275c2e35b47fc321
GATE try=7 t=140s r1=.../R1-map-pinning.md r2=.../R2-contract-docs.md sha=275c2e35b47fc321
STAB i=3 sha=275c2e35b47fc321 stable=2
GATE_READY sha=275c2e35b47fc321 r1=.../R1-map-pinning.md r2=.../R2-contract-docs.md
```

No run was taken against a plan or an unreported revision: the control run used frozen r96
closure bytes re-extracted from git (working-tree bytes at seat start already showed R1's WIP
`86b52949…`), and the delivered run was taken only after `GATE_READY` (both reports landed, pair
sha-stable). The subject sha was re-checked before and after the delivered batch
(`tool_sha256_after` field in the results JSON equals the pre-batch value; `stable_after=True`).
V04's report landed at 18:51 (sha `c35e3254…`, observed directly after poll try=16 still showed
`v04=none`); my comparison below is against that file.

## 2. Method

- **Base:** synthetic 8-obligation cluster built from scratch — `arden` (first_appearance + 2
  claims), `borin` (first_appearance + 1 claim), 1 relation, 2 timeline records; canonical map
  (`JSON fact pointer and fields`, rows R01–R08); declaration `8 JSON facts; 0 editorial rows;
  8 total mapped rows` → pristine base `RESULT PASS` exit 0. No corpus fixture and no other
  seat's fixture is copied (V04, by contrast, used a byte copy of the r93 fixture — the two
  bases are independent).
- **Nine classes:** N1 missing row (raw claim intact), N2 duplicate row, N3 phantom row,
  N4 source-ID mismatch, N5 malformed JSON, N6 map-path errors (f1 missing / f2 foreign /
  f3 traversal / f4 directory), N7 schema_drift, N8 deletion class (claims key + its map rows,
  declaration untouched), N9 dual_pointer (legacy dialect, 2 forms). Controls: clean base,
  legacy-clean, legacy-prose, canonical-note (`unsupported_map`), malformed declaration.
- Each probe: fresh copy, mutation applied, **real CLI** invocation, capture of exit + sorted
  FINDING IDs + INVENTORY receipt; every probe run **twice**, byte-stability checked.

## 3. Control run — r96 tool `2b0ba815…` (harness fidelity)

```
TOOL 2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8 stable_after=True
BASE                     exit=0 findings=none stable=True
K1_legacy_clean          exit=0 findings=none inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
K2_legacy_prose          exit=0 findings=none inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
K3_canonical_note        exit=2 findings=['unsupported_map'] inv=none stable=True
K4_inv_malformed         exit=1 findings=['inventory_mismatch'] inv=['INVENTORY declaration-malformed'] stable=True
N1_missing_row           exit=1 findings=['inventory_mismatch', 'missing_obligation'] inv=['INVENTORY JSON-FACTS 7/8; ... MISMATCH'] stable=True
N2_duplicate_row         exit=1 findings=['duplicate_mapping', 'inventory_mismatch'] inv=['INVENTORY JSON-FACTS 9/8; ... MISMATCH'] stable=True
N3_phantom_row           exit=1 findings=['inventory_mismatch', 'phantom_obligation'] inv=['INVENTORY JSON-FACTS 9/8; ... MISMATCH'] stable=True
N4_source_id_mismatch    exit=1 findings=['source_id_mismatch'] inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
N5_malformed_json        exit=2 findings=['malformed_json'] inv=none stable=True
N6f1_map_missing         exit=2 findings=['map_missing'] inv=none stable=True
N6f2_foreign_path        exit=2 findings=['foreign_path'] inv=none stable=True
N6f3_traversal           exit=2 findings=['unsafe_path'] inv=none stable=True
N6f4_map_is_dir          exit=2 findings=['map_missing'] inv=none stable=True
N7_schema_drift          exit=1 findings=['schema_drift'] inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
N8_deletion_class        exit=1 findings=['inventory_mismatch'] inv=['INVENTORY JSON-FACTS 6/8; ... MISMATCH'] stable=True
N9_dual_pointer          exit=1 findings=['dual_pointer'] inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
N9b_dual_colon           exit=1 findings=['dual_pointer'] inv=['INVENTORY JSON-FACTS 8/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 8/8'] stable=True
```

All nine class IDs reproduce the r96-lineage behavior (compare r96 V47 §3/§4): the two r96 C1
closures (deletion class gating `inventory_mismatch`; legacy dual pointers firing `dual_pointer`)
are present, and no control false-fires. The harness is faithful.

## 4. Delivered run — `86b52949…` (17 probes + base, identical to the control)

```
TOOL 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9 stable_after=True
BASE                     exit=0 findings=none stable=True
K1_legacy_clean          exit=0 findings=none stable=True
K2_legacy_prose          exit=0 findings=none stable=True
K3_canonical_note        exit=2 findings=['unsupported_map'] stable=True
K4_inv_malformed         exit=1 findings=['inventory_mismatch'] stable=True
N1_missing_row           exit=1 findings=['inventory_mismatch', 'missing_obligation'] stable=True
N2_duplicate_row         exit=1 findings=['duplicate_mapping', 'inventory_mismatch'] stable=True
N3_phantom_row           exit=1 findings=['inventory_mismatch', 'phantom_obligation'] stable=True
N4_source_id_mismatch    exit=1 findings=['source_id_mismatch'] stable=True
N5_malformed_json        exit=2 findings=['malformed_json'] stable=True
N6f1_map_missing         exit=2 findings=['map_missing'] stable=True
N6f2_foreign_path        exit=2 findings=['foreign_path'] stable=True
N6f3_traversal           exit=2 findings=['unsafe_path'] stable=True
N6f4_map_is_dir          exit=2 findings=['map_missing'] stable=True
N7_schema_drift          exit=1 findings=['schema_drift'] stable=True
N8_deletion_class        exit=1 findings=['inventory_mismatch'] stable=True
N9_dual_pointer          exit=1 findings=['dual_pointer'] stable=True
N9b_dual_colon           exit=1 findings=['dual_pointer'] stable=True
written: .../V44-scratch/delivered-run/matrix-results.json (sha256 7771cac41944605b7ee1d6a166adc54fd715fcec038126ef8e9d898ce860949f)
```

Programmatic control-vs-delivered comparison over the raw results JSONs (exits + finding-ID
tuples, per case and base): **17/17 cases identical, base identical, all stable both sides**.

```
$ python3 (comparison of control-run/matrix-results.json vs delivered-run/matrix-results.json)
base control   (0, []) / base delivered (0, [])
cases compared 17  ID/exits differing: NONE
all stable control: True / all stable delivered: True
```

Representative raw capture (delivered, N8 deletion class):

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-97/seats/V44-scratch/delivered-run/work/N8_deletion_class
OBLIGATIONS raw=6 mapped=6
INVENTORY JSON-FACTS 6/8; EDITORIAL-ROWS 0/0; TOTAL-ROWS 6/8 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 8/0/8; observed 6/0/6
RESULT FAIL
EXIT=1   (r96 control on the same input: RESULT FAIL exit 1, identical IDs)
```

The pin-hardening changes (self-test case registration + loader) leave all nine negative classes
and all five controls unchanged in exit code and FINDING IDs — exactly the non-regression C1
claims, measured on an independently built harness. (V04 §4b reports the same conclusion
independently: 0/52 output bodies differ between its r96 precheck and r97 runs.)

## 5. FINDING-ID comparison against V04 (seat deliverable)

V04 (`V04-c1-negative-rerun.md`) ran a 26-case matrix (a–i + 5 controls + base) on the same
delivered revision `86b52949…` / contract `2142b991…`, using a **different base** (byte copy of
`corpus/fixtures/r93-m2-kojiki-cluster`) and a harness ported from r96 V06. My matrix (N1–N9,
17 probes + base) uses a from-scratch 8-obligation synthetic base. Class-level comparison:

| class (V04 label → mine) | V04 r97 exit + IDs | V44 r97 exit + IDs | agreement |
|---|---|---|---|
| missing_obligation (a → N1) | 1 `[missing_obligation]` | 1 `[inventory_mismatch, missing_obligation]` | class ID in both; extra explained by shape (below) |
| duplicate_mapping (b → N2) | 1 `[duplicate_mapping, inventory_mismatch]` | 1 `[duplicate_mapping, inventory_mismatch]` | identical sets |
| phantom_obligation (c → N3) | 1 `[inventory_mismatch, phantom_obligation]` | 1 `[inventory_mismatch, phantom_obligation]` | identical sets |
| source_id_mismatch (d → N4) | 1 `[source_id_mismatch]` | 1 `[source_id_mismatch]` | identical |
| malformed_json (e → N5) | 2 `[malformed_json]` | 2 `[malformed_json]` | identical |
| map-path errors (f1–f4 → N6f1–f4) | 2 `[map_missing, foreign_path, unsafe_path, map_missing]` | 2 `[map_missing, foreign_path, unsafe_path, map_missing]` | identical (4/4) |
| schema_drift (g1/g2 → N7) | 1 `[inventory_mismatch, schema_drift]` / 1 `[phantom_obligation, schema_drift]` | 1 `[schema_drift]` | class ID in all three; extras differ by shape |
| inventory_mismatch deletion (h1/h2 → N8) | 1 `[inventory_mismatch]` (both) | 1 `[inventory_mismatch]` | identical |
| dual_pointer (i1–i3,i5–i7 → N9/N9b) | 1 `[dual_pointer]` | 1 `[dual_pointer]` | identical |
| dual_pointer + unmapped (i4 → —) | 1 `[dual_pointer, missing_obligation]` | — (no equivalent probe) | V04 extra explained by shape (its second pointer is genuinely unmapped) |
| controls | legacy-note/prose 0 none; canonical-note 2 `[unsupported_map]`; inv-declared-wrong 1 `[inventory_mismatch]`; inv-malformed 1 `[inventory_mismatch]` | K1/K2 0 none; K3 2 `[unsupported_map]`; K4 1 `[inventory_mismatch]` | consistent |

**Apparent extras resolved by direct inspection (same phenomenon as r96 V47 §5):**

1. **a vs N1.** V04's `case-a` *adds* an unmapped raw claim while the declaration still matches
   observed rows (`raw=13 mapped=12`, declaration `12/12` → no gate, per its raw capture). My N1
   *deletes* an existing map row while the declaration stays at 8 (`raw=8 mapped=7` → observed 7
   vs declared 8 → the inventory gate co-fires). Same class ID `missing_obligation`, different
   mutation shape — no tool discrepancy.
2. **g1/g2 vs N7.** V04's g-mutations change the mapped/observed row sets (hence
   `inventory_mismatch` on g1 and `phantom_obligation` on g2); my N7 adds claim-shaped records
   under a new entity key without touching any row count (`raw=8 mapped=8`, declaration matches
   → `schema_drift` alone). Same class ID in all three probes.
3. **i4.** V04's i4 second pointer is genuinely unmapped, so `missing_obligation` co-fires; my
   N9/N9b dual forms keep the mapped set complete → `dual_pointer` alone. V04 §3 records the
   same as a documented interaction, not a failure.

**Exits:** every class agrees on exit code (finding classes 1, unparsable/unsafe 2, controls 0);
both seats ran every probe twice with byte-identical repeats, and both seats observed the
delivered revision unchanged at re-check after all runs. No cross-seat ID contradiction found.

## 6. Secondary C1 observations (pin-hardening spot-checks, my own probes)

Scratch probe tree `V44-scratch/pin-probe/` (script `pin-probes-v44.py`, sha256
`6b272582f2df7c4b95eb389cf5812da255416d50bb5727115259ff477e53ff6c`); each variant runs a
byte-copy of the delivered tool beside its own contract copy — the live pair is never mutated.

```
A_baseline       exit=0  SELF-TEST CASES 25/25 pinned … RESULT PASS
B_drop_pin       exit=2  FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer
                          RESULT ERROR
C_load_bearing   exit=2  SELF-TEST FAIL dual_pointer exit=0 findings=none
                          FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
                          RESULT ERROR
```

- **A** — the delivered pair is green at 25/25 pinned (matches R1 §2, R2 §1 and V04 §5
  independently).
- **B** — dropping the `dual_pointer` case from a contract copy fails closed
  (`self_test_contract`, exit 2): loader tightening confirmed from a third angle (R1 neutralized
  `parse_map_text`, R2 `second_pointer_mention()`, I dropped the contract entry).
- **C** — neutralizing `second_pointer_mention()` (`return translated, None` in a tool copy)
  turns the pinned case red (`exit=0 findings=none` vs pinned exit 1 `['dual_pointer']`) →
  `self_test_mismatch`, exit 2: the new pin is load-bearing on my probe as well.

## 7. Hygiene

- Writes confined to `V44-scratch/` (harness, probe scripts, poll/gate logs, result JSONs,
  frozen r96 control copy, probe tree) and this report; no corpus file written, no commits, no
  pushes, no network, no nested agents. All paths absolute under the lane repo.
- Subject sha re-checked before/after the delivered batch — unchanged (`stable_after=True`).

**Bottom line: PASS — on the delivered r97 revision (`86b52949…`) my fresh nine-class matrix
(17 probes + base, twice each, all byte-stable) reproduces the r96-lineage exits and FINDING IDs
with zero drift, and its class-level IDs match V04's independent 26-case matrix on a different
base — the only differences are mutation-shape extras (inventory/schema co-fires), explained by
direct inspection, not tool discrepancies; secondary probes independently confirm the 25/25
`dual_pointer` pin, the fail-closed loader, and the pin's load-bearingness.**
