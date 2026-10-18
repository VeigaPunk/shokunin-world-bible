# V05 — C1 full negative battery (round-101)

Seat scope: negative verification of the delivered `dependency_freeze.py` + `dependency-freeze-contract.json` against every documented exit-1 and exit-2 class, stability (twice each, stable IDs), and guard behavior. Not an admission verdict and not a C2/C3 seat.

**Bottom line: PASS — 75/75 battery cases matched documented exit + finding IDs across 150 direct CLI calls (each case run twice, byte-identical full output both repeats), the observed finding-ID inventory is exactly the 14 documented IDs (none undocumented, none missing), the live chain verifies 8/8 clean twice with digests identical to U1's quoted receipts, the new `r100-docket-review` pin detects every mutation class thrown at it on scratch (including the C3 wrong-but-earlier swap, tick-verified), and all `--freeze` guard refusals leave the contract byte-unchanged. Zero failures, zero undocumented IDs, no live-tree writes, no commits.**

## Delivered revision, readiness, ownership

Poll protocol: first poll task (checks every 20 s) was killed by the 600 s background-task cap after covering part of its window — bounded stall-escape, recorded, not fatal; direct re-check showed the pin artifact already present but no producer report yet. Second poll: **READY on try 9 (~160 s)** — both `U1-chain-eight.md` (producer report) and the artifacts (`r100-docket-review` present in contract pins, 8 pins total) were required and present. Report quoted throughout is `.ufo/waves/round-101/seats/U1-chain-eight.md`; no lane `AGENTS.md` exists.

Snapshot identity (recorded by the battery at run time):

- Delivered tool SHA-256: `60a78bc39440917202488e4f6366a26540aeb494a089e5793864c1a4992fe3bf`.
- Delivered contract SHA-256: `b8fc63c3500d626df8d5c34b28327c10716610512a3c72ef56a19f3b46de36ca`.
- Delivered pins (8): `r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response, r97-crossing-acknowledgment, r98-clerk-filing, r99-window-lapse, r100-docket-review`.

All commands ran from `/home/vgpnk/Projects/shokunin` (session cwd) with absolute paths under `lore-shokunin/`, or from the lane root with `python3`. Every mutation happened on scratch mirrors under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats/.v05-scratch/`; the only live-tree invocations were read-only `verify` runs of the eight chain fixtures. No live `--freeze`, no commit, no push, no network, no nested agents. Writes confined to this report and the declared scratch tree.

Harness note (disclosed as evidence): two defects in my own battery script were found by a dry run against the baseline revision and fixed before the delivered run — mirrored tool copies lacked the exec bit (fixed by invoking through `sys.executable`, as the tool's own self-test does) and case lambdas late-bound `root`/`fix` (fixed by `bind()` default-arg binding). The dry run's failures were harness artifacts, not tool behavior; the delivered run below is the corrected harness.

## Battery command and summary

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats/.v05-scratch/run_negative_battery.py
```

Exit 0. Observed summary (`.v05-scratch/battery_summary.json`, `battery_log.txt`):

```json
{
  "battery_base_fixtures": ["r95-crossing-aftermath", "r100-docket-review"],
  "cases": 75, "runs": 150,
  "matching_cases": 75, "stable_ids": 75, "stable_full_output": 75,
  "freeze_no_write_on_refusal": true,
  "delivered_pin_count": 8
}
```

Case set (75 = 18 semantic + 22 digest-sweep + 21 CLI/contract + 6 freeze + 8 live), each run twice against unchanged inputs, exit code and full stdout compared byte-for-byte across repeats:

- Semantic exit-1 classes, per base fixture (r95 AND the new r100 pin): `reduction_edge_drop`, `addition_edge_phantom`, `repointed_edge`, `event_removed`, `event_endpoint_change`, `relation_endpoint_flip`, `relation_removed`, `relation_added`, plus precedence case `semantic_over_digest` (edge drop + trailing newline together → exit 1, `REDUCTION-DETECTED` only — the r99 AC-1 semantic-first precedence holds on the delivered revision).
- Digest sweep, per base: trailing newline appended to each of the ten pinned files (one case per file → exit 2 `DIGEST-MISMATCH` naming that file, `names_file` assertion per case), plus `README.md` removed entirely (→ `DIGEST-MISMATCH` naming it).
- CLI/contract exit-2 classes: `malformed_json`, `malformed_model` (timeline `{}`), `malformed_model_deps_type` (`depends_on` not a list), `missing_timeline`, `missing_relations` (both `FILE-MISSING`), `unpinned_fixture` (`UNPINNED-FIXTURE`), `missing_fixture` (pinned name, absent dir → `FIXTURE-MISSING`; for an unpinned name `UNPINNED-FIXTURE` wins precedence, per contract order), `invalid_arguments` ×4 (fixture+`--freeze`; no args; `--self-test`+fixture; `--self-test`+`--freeze`), `path_mismatch` (same-named copy at foreign path), `contract_invalid` ×7 (corrupt JSON; absent contract; root without `pins`; wrong `payload_schema_version`; `files` key removed; absolute pin path; pin path outside `corpus/fixtures/**`), `self_test_mismatch` (flipped `clean` expectation → exit 2 `SELF-TEST-MISMATCH`), `self_test_clean` (mirror `--self-test` positive control).
- Freeze cases: `scope_refused_outside`, `scope_refused_root` (the scope dir itself), `scope_refused_same_name` (in-scope copy at a different path than the recorded pin), `freeze_missing_pinned_file` (fresh in-scope name, `source-excerpt.md` removed → `FILE-MISSING`, and contract bytes verified **unchanged** across both refused runs — `freeze_no_write_on_refusal: true`), `freeze_positive` + `freeze_positive_verify` (fresh in-scope fixture frozen and re-verified clean through the guarded writer).
- Live read-only: the delivered tool verifying all eight chain fixtures, twice.

Finding-ID inventory across all 150 runs, mechanically extracted from `battery_log.txt`:

```text
distinct observed IDs (14): ADDITION-DETECTED, CONTRACT-INVALID, DIGEST-MISMATCH,
ENDPOINT-CHANGE, FILE-MISSING, FIXTURE-MISSING, INVALID-ARGUMENTS, MALFORMED-JSON,
MALFORMED-MODEL, PATH-MISMATCH, REDUCTION-DETECTED, SCOPE-REFUSED, SELF-TEST-MISMATCH,
UNPINNED-FIXTURE
undocumented observed: [] ; documented never observed: []
```

A designed case-set diff (static expected list vs observed log) confirmed all 75 intended cases ran — none silently skipped (the `repointed_edge` builder appends conditionally, so this was checked explicitly).

## C1 negatives on the new eighth pin

The battery ran the full semantic + digest-sweep set against `r100-docket-review` mirrors: every class was detected with the documented ID and exit (9/9 semantic, 11/11 digest-naming). The eighth pin is live, not merely present. Quotable probe on a scratch mirror of the new pin (byte tamper outside the semantic inventory), run twice, identical:

```text
FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1
FINDING DIGEST-MISMATCH: content digest 1d5ffb6d39827bc97c6d4f527977ee3c158e4310a7712815e56ab045b580f6e2 != pin 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19; changed: claim-excerpt-map.md (sha256 16981162… -> 01a9883e…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2 (both runs)
```

Live eight-fixture verification (read-only, twice, stable):

```text
r88-m3-maya-cluster         exit=0 DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94-paired-crossing         exit=0 DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95-crossing-aftermath      exit=0 DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96-crossing-response       exit=0 DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97-crossing-acknowledgment exit=0 DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98-clerk-filing            exit=0 DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
r99-window-lapse            exit=0 DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
r100-docket-review          exit=0 DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
```

All eight digests are byte-identical to the receipts U1 quoted, and the r100 receipt shape (`events 9/9; dependency-edges 8/8; relations 1/1`) matches U1's `FROZEN` line.

## C3 class fidelity: wrong-but-earlier, tick-verified

My generic `repointed_edge` battery cases (both bases) chose the first dep-bearing event as donor; its strictly-earlier candidate pool was empty in file order, so the fallback swap target could be a later event — the finding class is direction-agnostic (`compare()` reports lost+gained either way), but C3 pins **wrong-but-earlier** specifically. Closed with a focused probe that asserts `tick(target) < tick(donor)` before swapping, on both bases, twice each:

```text
r95-crossing-aftermath: donor=aftermath-missing-evin(tick 11) paired-crossing-decision(tick 10) -> aru-ninth-bell(tick 9)
  twice-identical=True exit=1 ids=['ADDITION-DETECTED', 'REDUCTION-DETECTED']
  FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']
  FINDING REDUCTION-DETECTED: event aftermath-missing-evin lost depends_on ['paired-crossing-decision']
  RESULT FAIL
r100-docket-review: same donor/deps structure (fixture continues the chain), tick 11 / 10 -> 9, same result
EARLIER-SWAP PROBE: PASS
```

This is U1's exact persisted case (`aftermath-missing-evin`: `paired-crossing-decision` → `aru-ninth-bell`), independently reproduced through my own mirror construction, and additionally demonstrated on the new r100 pin. The persisted case itself also runs green inside the mirror self-test on the delivered bytes:

```text
case lines: 19 | all ok: True
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
exit: 0 | stderr empty: True
```

## Parity and adjacency (bounded checks from this seat)

- Contract vs `6f86bf2`: the 18 inherited `self_test.expected` entries are equal (semantic JSON equality, case by case); only `repointed_edge` added (`exit 1`, `['ADDITION-DETECTED','REDUCTION-DETECTED']`); nothing removed; all 7 inherited pins field-identical; among non-pin top-level keys only the writer-managed `revision` changed (`b5fe4729…` → `ebec6bbd…`); `provenance_note`, `precedence`, `scope`, `exit_codes`, etc. all equal. Matches U1's "3 hunks" claim.
- Tool `FROZEN_CASES`: baseline 18 → delivered 19, only `repointed_edge` appended, prior order preserved.
- `git status --porcelain`: exactly U1's four owned files modified (`SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py`); untracked: wave/scratch dirs, U2's `corpus/knowledge/r101-r10-register-first-entry.md`, a pre-existing r98 scratch remnant (`?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`, not from this round's seats).
- Doc rows present: `SKILL.md` freeze row lists the eight-fixture chain, "19 cases (… r101 added `repointed_edge`, the wrong-but-earlier repointed dependency edge)", "exactly the eight chain fixtures, verifying 8/8 clean", and a dated supersession bullet (2026-10-18, round 101); `corpus/tools/README.md` carries "Round-101 addendum: r100 pinned, eight-fixture chain, wrong-but-earlier edge persisted as self-test case (2026-10-18)" at line 423. (Doc wording parity is the doc-parity seat's axis; I checked presence only.)

## Bounds / disclosures

- The baseline dry run (before U1's artifacts were snapshotted into the battery) ran against the r100 revision; its three "failures" were my harness's late-binding lambdas executing the wrong mirror root — fixed and re-run; nothing about the tool is claimed from the dry run.
- The delivered bytes may in principle have changed after my snapshot; all claims are pinned to the recorded SHA-256s above (tool `60a78bc3…`, contract `b8fc63c3…`).
- Endgame convention: no all-reports poll was required (single-producer readiness poll, SELF not applicable); the one bounded stall-escape (poll task killed at the 600 s background cap) is recorded above.
- The battery leaves all scratch under `.v05-scratch/` (battery mirrors, logs); no delivered file was written by this seat; this report is the only file outside that scratch tree.

## Bottom line

PASS — every documented exit-1 and exit-2 class of the delivered freeze gate fires with its stable ID, twice, byte-identically (75/75 cases, 150 runs, 14/14 documented IDs, zero undocumented); the new `r100-docket-review` pin detects all mutation classes including the tick-verified wrong-but-earlier swap; the live chain verifies 8/8 clean twice with digests equal to U1's receipts; freeze guards refuse all three scope classes with no contract write; inherited pins, expectations, and receipts are unchanged; no live writes, no commits.
