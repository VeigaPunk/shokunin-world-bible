# F23 — verdict-calibration (r94 FOLLOW-UP)

Seat: F23, verdict-calibration. Axis: **CALIBRATION (C2)**. Independent verdict, no author self-report reused as evidence.

Method: my own scratch demos (`F23-demo.py`, `F23-probes2.py`, `F23-probes3.py` under `.ufo/waves/round-94/followup/F23-scratch/`, outputs in matching `.out` files), run against `corpus/tools/map_obligations.py` and `corpus/tools/support_check.py` at HEAD `65a9329` (candidate `abbc3e0`). Isolated clones only; no live fixture was written.

## 0. Identity of the artifact under test

- Round delta under `corpus/tools/`: `git diff --stat 9c2eea3 abbc3e0 -- corpus/tools/` → only `map-obligations-contract.json | 48 +` and `map_obligations.py | 691 +`. `support_check.py` is byte-identical baseline→HEAD: my check printed `[PASS] support_check.py bytes identical baseline->HEAD sha256=55a5eb2753901be7`.
- Working tree equals the commit: `git hash-object corpus/tools/map_obligations.py` = `5801192b60f2905356ec6802f757d36dd58d2f25` = `git rev-parse HEAD:...`; contract `e26574ad36706594…` likewise; `git status --short -- corpus/` empty. Only commit touching the tool: `abbc3e0`.
- Imports are stdlib only (`argparse, hashlib, json, os, re, subprocess, sys, tempfile, collections, pathlib`), matching the "no dependencies" claim.

## 1. Before→after blind spot — independently reproduced

Setup per fixture: full clone, then append one raw claim `{"statement": "F23 isolated unmapped raw claim", "source_id": "f23-injected-source"}` to `entities[0].claims` (index 1) and add **no** map row.

| Fixture | BEFORE: lexical `support_check.py` (HEAD, == baseline) | BEFORE: `support_check.py` from `git show 9c2eea3:` | AFTER: `map_obligations.py` |
|---|---|---|---|
| r93-m2-kojiki-cluster | exit 0, `RESULT PASS`, no findings | exit 0, `RESULT PASS` | exit 1, `RESULT FAIL`, `FINDING missing_obligation: entities.json#/0/claims/1 has no map row` |
| r94-paired-crossing (round's own fixture) | exit 0, `RESULT PASS` | exit 0, `RESULT PASS` | exit 1, `RESULT FAIL`, same finding shape |

The "before" state is structural, not incidental: `grep -n "entities.json\|relations.json\|timeline.json\|first_appearance\|source_id" corpus/tools/support_check.py` returns **no matches** — the lexical checker reads the map and excerpt files only, so a raw JSON obligation with no map row is invisible to it. The counterexample is real on both the pre-existing fixture and the new one.

Clean (unmodified) runs: `map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` → `OBLIGATIONS raw=12 mapped=12` / `RESULT PASS`; on r94 → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS`. My own parse of r94 confirms the 14 = 5 first_appearance + 5 claims + 1 relation + 3 timeline composition and 14 data rows in one `## JSON facts` table. Frozen mode: `--frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified`, `raw=12 mapped=12`, `FROZEN expected=PASS/0 findings=none matched`, exit 0. Self-test: exit 0, `RESULT PASS`, 20 `SELF-TEST PASS` lines; no leftover temp dir under the repo root (`ls -d map-obligations-self-test-*` empty) and `git status --short -- corpus/` still empty after all runs.

## 2. Could-not-evaluate classes are honest (never empty-success)

19 independent probes, each a real CLI invocation on a scratch clone (never the tool's own self-test alone). The 17 below plus the two renamed-key probes in §3 all returned ERROR/2 or FAIL/1 **except one PASS**, which is the §3 residual and occurred on a fully enumerated canonical-key input — no probe returned PASS on an unevaluated or empty inventory.

| Probe | Observed |
|---|---|
| zero-row `## JSON facts` table | exit 2, `unsupported_map: JSON facts section has no supported table` |
| `## JSON facts` section absent | exit 2, `unsupported_map: map must contain exactly one JSON facts section` |
| raw claim with renamed `source` field (no `source_id`) | exit 2, `invalid_raw_data: … /source_id must contain a non-empty source ID` |
| empty raw arrays vs non-empty map | exit 1, 12 × `phantom_obligation` |
| unmapped raw relation | exit 1, `missing_obligation: relations.json#/2 has no map row` |
| prose pointer (no inline code) | exit 2, `unsupported_map: pointer cells must contain one canonical inline-code pointer` |
| malformed raw JSON | exit 2, `malformed_json` |
| traversal `--map` path | exit 2, `unsafe_path: map path contains traversal` |
| duplicate row | exit 1, `duplicate_mapping: entities.json#/0/first_appearance appears 2 times` |
| source-ID mismatch | exit 1, `source_id_mismatch: … does not bind to 'm2-record-archive'` |
| unrecognized pointer-column header | exit 2, `unsupported_map: table needs one JSON fact pointer and one source-ID column` |
| two candidate conventional maps present | exit 2, `unsupported_map: expected exactly one conventional claim-to-excerpt map` |
| new entity, both obligations unmapped | exit 1, both `missing_obligation` findings (`entities.json#/4/first_appearance`, `…/4/claims/0`) |
| row moved outside the JSON facts section | exit 1, `missing_obligation` (no false PASS) |
| legacy bracket grammar `entities[0].first_appearance` | exit 2, `unsupported_map: co-mapped or unsupported pointer grammar` |
| co-mapped grammar `a.json#/p; b.json#/q` | exit 2, same finding |
| `claims` key as an object | exit 2, `invalid_raw_data: … /claims must be an array` |

Every run also printed exactly one `RESULT` line with empty stderr. Two method notes for transparency: (a) my first source-ID-mismatch probe edited the `Exact anchor` column instead of the `In-world source ID` column and returned exit 0 — after correcting it to column 2 the tool returned exit 1 `source_id_mismatch` as required; (b) `support_check.py`'s non-reading of raw JSON was confirmed by grep, not assumed from its PASS behavior.

## 3. Residual limitation found (reported as observed, not smoothed)

- Renaming an entity's claim container to a non-canonical key (`claims` → `claim_list`) **and** removing that claim's map row yields `exit=0 RESULT PASS` with no finding (`F23-probes3.py` case C). The tool has no unknown-key/schema-drift class; it enumerates `entity["claims"]` with a `[]` default, so the claim is silently invisible rather than ERROR.
- Mitigation in the common drift direction: with the map row **kept**, the same rename is caught — `exit=1 FINDING phantom_obligation: entities.json#/0/claims/0 is not a raw source-attributed obligation` (case C2). So the silent path requires both a schema deviation and removal of the corresponding map row.
- Assessment: this is outside the declared canonical scope (contract JSON pins "entity claims" and the canonical one-pointer-per-row form; r93 and r94 both use `claims`), and it does not reproduce the C2 counterexample class. It is a bounded residual, not a failure of the claimed capability, but it means "never empty-success" holds for grammar/path/type errors and for canonical-key inputs, not for arbitrary key renaming.

## 4. Movement judgement — CALIBRATION

- **Before**: no tool read raw JSON obligations; the lexical checker demonstrably returns PASS on an unmapped raw claim (reproduced on both fixtures, with the baseline-commit tool bytes).
- **After**: the same input returns exit 1 with a stable finding ID, and the tool additionally detects duplicate, phantom, and source-ID-mismatch conditions while routing unsupported grammar/paths/types to exit 2. Verified independently, not via the tool's self-report; the artifact is identical to the committed blob.
- **Bounded**: mapping completeness and source-ID equality only (the code performs no entailment/fidelity/chronology/rights/canon check, consistent with its declared scope), canonical map form only, and the residual in §3.
- The C2 evidence chain does not depend on the failed W20 seat: W20 was assigned "first-appearance/motif identity critic" (`.ufo/waves/round-94/work-results.xml:219`, agent-607), unrelated to this axis.

## Bottom line

**PASS — CALIBRATION improved.** The before→after blind spot reproduces independently (lexical `support_check.py` exit 0 PASS vs `map_obligations.py` exit 1 `missing_obligation`) on both r93 and r94 clones, clean runs give 12/12 and 14/14, the frozen snapshot and 20-case self-test pass, and 18 of 19 adversarial probes returned ERROR/2 or FAIL/1 with the single PASS being the §3 residual; the residual (non-canonical `claims` key + removed map rows → silent PASS) is out of the declared canonical scope and recorded as an observed limitation.
