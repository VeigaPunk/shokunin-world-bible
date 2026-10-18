# F18 — operability

Seat: F18, round-94 FOLLOW-UP wave, role: operability of the new r94 gate.
All commands below were run from the repository root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; outputs are quoted verbatim. No `corpus/` file, sibling report, or tool was modified; the only write is this report. `git status --short` after all runs showed only `?? .ufo/waves/round-94/followup/` (the untracked follow-up directory from other seats, pre-existing), so none of the runs wrote into the tracked tree.

## 1. Documented commands in the r94 fixture README and knowledge doc — run as written

The fixture README's only runnable block is `corpus/fixtures/r94-paired-crossing/README.md:21-26` ("Replay from the repository root"). A `grep -n "python3"` over the README and `corpus/knowledge/r94-cross-myth-design-comparison.md` found exactly two invocations, the same two in both files (README:24-25; knowledge:27,29); no other command is documented.

**1a. `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing`**

Observed output (exit 0):

```
CLEAN: schema, citations, relations, timeline; 0 violations
```

This matches the README claim ("Replay…") and the knowledge-doc line 27 statement verbatim, including the "exit 0" parenthetical.

**1b. `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing`**

Observed key output lines (exit 0):

```
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
```

Every number in the knowledge doc's lexical receipt (line 29: facts 14/14, editorial 2/2, total 16/16, anchors 12/12, support 14/14, editorial anchors 2/2, modes 16/16, validated 16/16, `RESULT PASS`, exit 0) matches the actual run. The doc's specific anchor claims were also checked in the same output: `J05 … 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.`, `J10 … 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.`, `J11 … 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`, `J14 … 20:> Their tick-10 decision depends on both ninth-bell entries…`. All four line numbers as documented.

Result: both documented commands run from repo root as written and produce the documented output and exit codes.

## 2. `map_obligations.py` — 0/1/2 exit contract

**Positive paths (all exit 0, `RESULT PASS`):**

- `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` / exit 0. The 14 matches `wave-spec.json:17` `canonical_map_obligations: 14`.
- `python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` → `OBLIGATIONS raw=12 mapped=12` / `RESULT PASS` / exit 0.
- `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing --map claim-excerpt-map.md` → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` / exit 0 (the `--map` value is resolved relative to the cluster directory; see note below).
- `python3 corpus/tools/map_obligations.py --self-test` → 20 `SELF-TEST PASS` lines covering exits 0, 1 and 2, then `RESULT PASS`, process exit 0. A programmatic diff of the observed cases against the persisted contract `corpus/tools/map-obligations-contract.json` (all 20 case IDs, exit codes and finding-ID lists) reported: `contract cases: 20 observed cases: 20`, `missing: [] extra: [] value diffs: []`, `VERDICT: MATCH`. So the contract's 0/1/2 semantics — including `missing`/`duplicate`/`phantom`/`source_id_mismatch`/`frozen_expected_failure` at 1 and the 13 could-not-evaluate cases at 2 — are reproduced by the real CLI.
- `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` / exit 0.

**Read-only negative probes (no fixture modified):**

- `python3 corpus/tools/map_obligations.py /nonexistent-cluster-path-xyz` → `FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: '/nonexistent-cluster-path-xyz'` / `RESULT ERROR` / exit 2. Fail-closed, not an empty successful inventory.
- `python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster` → `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` / exit 2. This is the documented scope boundary (r94 `wave-spec.md`: "no claim of general migration of older maps"), and it behaves fail-closed rather than silently reporting an empty inventory.
- `--map` accepts a path relative to the cluster; passing a repo-relative foreign path is joined to the cluster dir and yields `FINDING map_missing … /corpus/fixtures/r94-paired-crossing/corpus` exit 2. Operability note only; the accepted invocation above is clean.

**Hygiene:** no `map-obligations-self-test-*` temp directory was left at the repo root after the self-test (`ls -d map-obligations-self-test-*` → `No such file or directory`).

## 3. `.ufo/waves/round-93/validate_wave_spec.py`

The file exists (28946 bytes). Run as instructed:

- Default run (round-93 spec beside the script): `python3 .ufo/waves/round-93/validate_wave_spec.py` → `authorized_work_seat_total=63 allowed=32..64` / `WARN served_backend_echo_unknown:corrective-luna-work` / `PASS closure_ready` / `CLOSURE_GATE=PASS`, exit 0.
- `python3 .ufo/waves/round-93/validate_wave_spec.py --self-test` → 9 `PASS selftest:…` lines (closure_ready, four corrective-result controls, duplicate_seat_id, required_report_missing, phase_unresolved, failure_reason_missing, unknown_backend_echo warning), exit 0.
- Applicability (phase structure only, per seat instruction): the validator is round-93-bound by construction — it pins `round != 93`, the schema, baseline, and the phase IDs `initial-luna-work` / `corrective-luna-work` (`validate_wave_spec.py:276-321`), and it expects exactly 32 F01–F32 follow-up slots (`:353-360`). Run against the r94 spec it exits 1 with 17 findings: `FAIL schema_mismatch`, `round_mismatch`, `baseline_mismatch`, `receipt_policy_invalid:spec`, `work_phases_missing`, `work_phase_count_mismatch:0`, `initial_work_seat_count:invalid:expected_31`, `corrective_work_seat_count:invalid:expected_32`, `corrective_result_phase_missing`, `authorized_work_range_missing`, `authorized_work_total_out_of_range:0`, `authorized_work_total_expected:0:expected_63`, `authorized_work_total_mismatch:0`, `required_followup_missing`, `prior_followup_attempts_missing`, `prior_deepseek_transport_accounting_invalid`, `glm_preliminary_accounting_invalid`, `CLOSURE_GATE=FAIL`. This is non-applicability of the r93 validator to the r94 spec shape, not an r94 product defect; no r94 phase claim is validated by it.

## 4. `wave-spec.json` parses; phase fields vs the actual wave shape

`json.loads` on `.ufo/waves/round-94/wave-spec.json` succeeds; top-level keys are `round, regimen_round, baseline_commit, state, claims, work, followup, boundaries, expected_C1_counts, expected_preservation`.

**Fields that match the actual shape:**

- `work.requested_seats: 32` (`:9`), `seat_ids` W01–W32, `work.status: "completed"` (`:11`), `work.result: "work-receipt.json"` (`:12`). The receipt exists and `work-receipt.json` has 32 seat entries whose IDs equal `spec.work.seat_ids` exactly, all with tool outcome `completed`, `requested_seats: 32`.
- `expected_C1_counts.candidate` 5/1/3 (`:17`) equals actual record counts: `entities.json` 5, `relations.json` 1, `timeline.json` 3. `canonical_map_obligations: 14` equals the CLI's `raw=14`.
- `expected_preservation` (`:18`): fixture directories now 168 = `fixture_directories_before: 167` + the one new fixture; `sha256(corpus/fixtures/check_bible.py)` = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, identical to the pinned `checker_sha256`.
- Caveat recorded in the evidence, not in the spec: `work.status: "completed"` is accurate as the tool-label outcome only. `work-receipt.json:56` records `standalone_seat_reports: 31` and `:57` records the W20 defect (`"No W20.md was created. The raw returned text is malformed tool-call-like output with extensive repetition…"`); `ls .ufo/waves/round-94/work/ | grep -i w20` returns nothing. The receipt already reconciles this honestly; the spec field alone does not distinguish 32 labels from 31 usable reports.

**Field that diverges from the live shape:**

- `followup` (`:15`): `{"requested_model":"opencode-go/deepseek-v4.1-flash","requested_seats":32,"status":"not-dispatched","result":null}`. At observation time the actual shape is: `LOG.md:2687` declares "one batched AgentSwarm FOLLOW-UP of 40 seats" on that model (commit `65a9329`, which changed only `LOG.md`), and `.ufo/waves/round-94/followup/` contains `F01-c1-checker.md`, `F11-c2-negative.md`, `F32-checker-discriminator.md`, `F33-support-regression.md` plus `F11/F13/F23/F31-scratch/` — i.e. at least 33 live F-slots. So `requested_seats: 32` does not match the declared/dispatched 40, and `status: "not-dispatched"` is the pre-dispatch declaration superseded by `65a9329`. Note `wave-spec.md:5` authorizes a "32–64-seat" follow-up, so 40 is inside the authorized range; the divergence is a stale numeric field in `spec.json`, not an out-of-range dispatch. Whether the declaration contract requires updating `spec.json` after the dispatch declaration is a parent/L1 judgment, not measured here.

## Bottom line

PASS (gate operability) — every documented command runs from repo root as written with the documented exits and outputs, and `map_obligations.py` honors its 0/1/2 contract on all positive paths (r94 14/14, r93 12/12, `--map`, `--self-test` 20/20 matching the persisted contract, `--frozen`) plus fail-closed negatives; one flagged divergence for L1 judgment: `wave-spec.json:15` still declares follow-up `requested_seats: 32` / `not-dispatched` while `LOG.md:2687` and the live `followup/` directory show a 40-seat dispatched wave.
