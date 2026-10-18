# V03 — c1-schema-drift-pinned seat report (round 96)

- Seat: V03 `c1-schema-drift-pinned`. Report path (only repo file written by this seat):
  this file. Scratch: `.ufo/waves/round-96/seats/V03-scratch/` (arms `A`–`F`, probe fixtures,
  hand-reconstructed case, captured stdout). No commits, no pushes, no network, no nested agents.
- Baseline: r95 closure `dcb2d92` (`lore r95: freeze admitted wave + closure docs`, 2026-10-17
  17:31:49 -0300). Round: r96, 64-seat single wave, lore-shokunin.
- Scope (from the seat brief): poll for Q1+Q2; confirm the persisted `schema_drift` self-test
  case is **load-bearing** — mutate the case's fixture so the drift check would not fire on a
  scratch copy → that case must FAIL; restore → 24/24 PASS.
- All commands run from the lane repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`; every
  path below is under it unless stated otherwise.

## 0. Poll-wait outcome and verified revision

Q1's tool landed 17:47:24 and its report at 17:49; Q2's contract landed 17:50:17 and its report
at 17:52 (my poll hits: `POLL_HIT`-style lines `cases=24 contract=24 q1reports=1` then
`contract=24 q2reports=1 / READY`). No ABSENT. Hashes re-pinned after both producer reports
landed and identical to the runs below:

| Artifact | sha256 | bytes | mtime |
|---|---|---|---|
| `corpus/tools/map_obligations.py` (Q1) | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` | 37739 | 17:47:24 |
| `corpus/tools/map-obligations-contract.json` (Q2) | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` | 3115 | 17:50:17 |

Producer receipts pin the same revisions: `Q1-tool-hardening.md` ("Delivered tool … sha256
`2b0ba815…`") and `Q2-contract-docs.md` (contract `97b76bb8…`, "Reference: Q1's delivered tool
… `2b0ba815…` unchanged through all runs"). No revision drift between producer receipts and mine.

Baseline residual reproduced before the delivery (17:38, r95 bytes `d1c239cc…` / `8173bb97…`):
`--self-test` was 22/22 PASS exit 0, and the contract contained **no** case expecting
`schema_drift` or `inventory_mismatch` (parsed check: `cases expecting schema_drift: []`,
`cases expecting inventory_mismatch: []`). The r95-carried residual ("`schema_drift` not pinned
by a persisted self-test case") is therefore real, not assumed.

## 1. Delivered revision: 24/24 pinned, PASS, exit 0

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS complete exit=0 findings=none
… (22 inherited cases, unchanged ids/expectations) …
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
exit=0
```

24 `SELF-TEST PASS`, 0 FAIL, stderr 0 bytes, stdout sha256
`4b9fbb347a2da8fda9f5fa1a3296682e056362f7ee36fa457558cc2bb54567fc`
(`V03-scratch/restore-selftest.txt`, byte-identical to `delivered-selftest.txt` and to arm A's
`out.txt`). Case-set equality verified independently by AST + JSON parse: implemented
`CORE_SELF_TEST_CASES` (22) + `ADDED_SELF_TEST_CASES` (2: `schema_drift`, `inventory_mismatch`)
= 24, contract ids = 24, no duplicates, `sets equal: True`, `missing from contract: []`,
`extra in contract: []`. The delivered contract pins the target case as
`{"id": "schema_drift", "exit": 1, "finding_ids": ["schema_drift"]}`.

## 2. Load-bearing experiment (the seat's decisive test)

Six arms, each an isolated copy of the delivered tool + a contract copy inside
`V03-scratch/arms/<arm>/` (the tool resolves its contract as `Path(__file__).with_name(...)`,
so a copy pairs tool and contract). Run command per arm:

```
cd V03-scratch/arms/<arm> && python3 map_obligations.py --self-test
```

| Arm | Tool | Contract | Exit | PASS/FAIL | `schema_drift` case line | stdout sha256 |
|---|---|---|---|---|---|---|
| A | delivered `2b0ba815…` | delivered `97b76bb8…` | 0 | 24/0 | `PASS exit=1 findings=['schema_drift']` | `4b9fbb34…` |
| B | fixture mutated `7fc62a19…` | delivered | 2 | 23/1 | `FAIL schema_drift exit=0 findings=none` | `185a575a…` |
| C | fixture mutated `7fc62a19…` | delivered, only the `schema_drift` line relaxed to `exit 0, []` | 0 | 24/0 | `PASS exit=0 findings=none` | `d5b37fcb…` |
| D | delivered | delivered, only the `schema_drift` line relaxed to `exit 0, []` | 2 | 23/1 | `FAIL schema_drift exit=1 findings=['schema_drift']` | `1c4fb850…` |
| E | delivered | delivered with the `schema_drift` case line deleted | 0 | 23/0 | (case absent; `SELF-TEST CASES 23/24 pinned`) | `8ef344df…` |
| F | drift emission disabled `…` | delivered | 2 | 23/1 | `FAIL schema_drift exit=0 findings=none` | `185a575a…` |

**Arm B — the brief's test.** The one-site mutation removes claim-shapedness from the case's
fixture (the drift check requires a dict with non-empty `statement` **and** `source_id`), so
drift cannot fire; the fixture stays otherwise complete (3 obligations ↔ 3 rows):

```
--- arms/A/map_obligations.py
+++ arms/B/map_obligations.py
@@ -714,7 +714,8 @@
         rows = [row for row in rows if not row[1].endswith("/claims/0")]
         write_test_fixture(cluster, rows)
         entities = json.loads((cluster / "entities.json").read_text(encoding="utf-8"))
-        entities[0]["assertions"] = entities[0].pop("claims")
+        entities[0]["assertions"] = [{"statement": "test claim"}]
+        entities[0].pop("claims")
```

Observed (full arm B stdout, `V03-scratch/arms/B/out.txt`):

```
SELF-TEST CASES 24/24 pinned
… 23 × SELF-TEST PASS (identical to arm A) …
SELF-TEST FAIL schema_drift exit=0 findings=none
OBLIGATIONS raw=3 mapped=3
RESULT PASS
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

Only the `schema_drift` case fails (23 PASS / 1 FAIL, stderr 0 bytes) — the mutation is surgical
and the failure is exactly the case the brief asks about.

**Arm C (isolation, why B fails).** Same mutated fixture, contract copy with the single
`schema_drift` line flipped to `{"id": "schema_drift", "exit": 0, "finding_ids": []}`
(byte diff = that one line): `SELF-TEST CASES 24/24 pinned`, 24 PASS, `RESULT PASS`, exit 0.
So the arm-B failure is caused precisely by the drift check not firing, not by a malformed or
incomplete fixture.

**Arm D (expectation is not vacuous).** Delivered fixture, relaxed expectation:
`SELF-TEST FAIL schema_drift exit=1 findings=['schema_drift']` with
`FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key
'assertions'`, exit 2. The pinned expectation is a real claim about observed behavior.

**Arm F (check-side load-bearing).** Delivered tool with the emission site disabled
(`if shaped:` → `if shaped and False:`, one site, fixture untouched) + delivered contract:
`SELF-TEST FAIL schema_drift exit=0 findings=none`, exit 2 — stdout byte-identical to arm B
(sha `185a575a…`). The case fails if the *check* disappears, not merely if the *fixture* changes.

**Restore (brief's second half).** Back on the delivered pair, from the repo root:
`python3 corpus/tools/map_obligations.py --self-test` → `SELF-TEST CASES 24/24 pinned`,
24 PASS / 0 FAIL, `RESULT PASS`, exit 0, stderr 0 bytes.

## 3. Independent confirmation outside the self-test hook

The self-test drives the real CLI (subprocess, real cluster), but both sides of it come from the
same producer file. Two independent checks:

1. **Hand-reconstructed case fixture** (`V03-scratch/hand-drift-case/`, built by this seat from
   the code's semantics, not by calling `prepare_test_case`): entity 0 with `assertions` holding
   one claim-shaped record, map rows only for `first_appearance`/relations/timeline. Delivered
   tool: `OBLIGATIONS raw=3 mapped=3` / `FINDING schema_drift: entities.json#/0: 1
   sourced-claim-shaped record(s) under unexpected key 'assertions'` / `RESULT FAIL`, exit 1 —
   exactly the pinned `["schema_drift"]`/exit 1, with no other finding.
2. **Unrelated probe fixture** (`V03-scratch/probe-drift/`, `probe-control/`, also built by this
   seat): control → `OBLIGATIONS raw=4 mapped=4` / `RESULT PASS` exit 0; drift (unexpected key
   `claim_records`) → `FINDING schema_drift … under unexpected key 'claim_records'` /
   `RESULT FAIL` exit 1. Identical behavior on the r95 baseline tool, so r96 did not change the
   class's observable semantics — it pinned them.

Scope note (bounded, unchanged from r95): the case pins drift on claim-shaped records under an
**unexpected entity key**. Relations/timeline/nested drift and the general drift-scope question
remain as recorded in the r95 SCORECARD; r96 did not claim to widen them.

## 4. Non-regression and environment

- Corpus tree byte-identical before/after the delivered self-test run (recursive sha256 of all
  non-`__pycache__` files under `corpus/`, aggregate `0216e44b…` both sides, `diff` empty);
  zero leftover `map-obligations-self-test-*` directories at the repo root.
- The 22 inherited cases keep their r95 ids and expectations (case-set equality check in §1;
  arm A stdout shows all 22 PASS lines identical to the r95 22-case output).
- Environment note (reproduced, matches Q2's report): `/tmp` is inode-exhausted
  (`df -i /tmp` → `1048576 1048576 0 100%`, space 45% used). One of my early captures that
  redirected to `/tmp` failed with `No space left on device`; the tool's own self-test scratch
  lives under `ROOT` (the repo), so `--self-test` still runs correctly under this condition —
  the r95 BR-05 scratch-location choice is empirically doing its job. All evidence in this
  report was captured under `V03-scratch/`, not `/tmp`.

## 5. Bounded observations (no axis harm claimed, for the adjudicator)

1. **Added cases are contract-declared, not tool-enforced.** Arm E: deleting the `schema_drift`
   case from the contract copy leaves the loader green — `SELF-TEST CASES 23/24 pinned` /
   `RESULT PASS` / exit 0. This is deliberate (Q2's report: pre-edit the loader printed
   `SELF-TEST CASES 22/24 pinned` / `RESULT PASS` so the r95 22-case contract still passes), and
   the delivered pair is fully pinned at 24/24, so nothing in C1 is harmed. But a future contract
   edit could drop one of the two new cases while exit stays 0; the only signal is the receipt
   line. Candidate r97 debt: make a non-24 pin fail closed (or require all `SELF_TEST_CASES`
   pinned), unless the 22-case tolerance is load-bearing elsewhere.
2. Arm F is a mutation of the delivered tool, not of the delivered corpus; the delivered bytes
   themselves were never modified by this seat (corpus hash check in §4).

## 6. Bottom line

**PASS** — on the pinned delivered revision (tool `2b0ba815…`, contract `97b76bb8…`) the
`schema_drift` self-test case is load-bearing in both directions: mutating its fixture so drift
cannot fire makes exactly that case FAIL (arm B, exit 2), disabling the drift check makes it
fail identically (arm F), relaxing only the expectation also fails (arm D), while relaxing the
expectation *and* mutating the fixture passes 24/24 (arm C, isolating the cause); restoring the
delivered pair gives `SELF-TEST CASES 24/24 pinned` / 24 PASS / `RESULT PASS` exit 0 with the
corpus tree byte-unchanged.
