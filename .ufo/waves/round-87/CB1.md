## Work performed

- Snapshotted the requested revision outside the lane with `git -C /home/vgpnk/Projects/shokunin/lore-shokunin archive 28706dc | tar -x -C /tmp/r87-CB1`; extracted the historical checker separately with `git show 5eb9451baff217c19d5786405f9b2aa500b7c1b7:corpus/fixtures/check_bible.py > /tmp/r87-CB1/baseline-check_bible.py`. Audited HEAD `28706dc73a9b7667851fd82adb71e905ae5eb896`.
- Read `corpus/knowledge/holder-assessment-boundary.md:14-30,32-75,105-133,135-157,191-214` and checker state/outputs at `corpus/fixtures/check_bible.py:157-183,193-255,329-339`. `Glob **/AGENTS.md` in the snapshot returned no matches.
- Replayed the five named r85 probes plus `item-chain-valid` / `item-chain-broken`; generated additional input-only cases under `/tmp/r87-CB1/probes/` from `corpus/fixtures/consistent` and `corpus/fixtures/contradictions`. No lane fixture or checker was edited.

## Before → after measurements

All commands below ran from `/tmp/r87-CB1`. Each `[rc=N]` is the observed process return code. The five r85 probe directories contain five JSON files each; byte comparisons against commit `5eb9451baff217c19d5786405f9b2aa500b7c1b7` reported `files=5; baseline_bytes_match=True` for every case.

**Baseline checker and the recorded r85 cases.** Command:

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  python3 /tmp/r87-CB1/baseline-check_bible.py "corpus/live/runs/round-85/probe-inputs/$case"
done
```

Observed output (trimmed per case):

- `r85-control`: `CLEAN: schema, citations, relations, timeline; 0 violations` `[rc=0]`.
- `r85-unique-break-control`: `entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'`; `1 violation(s); no canon changed` `[rc=1]`.
- `r85-masked-ambiguous` and `r85-isolated-ambiguous`: only `entities[5].id: duplicate entities id 'vault'`; `1 violation(s); no canon changed` `[rc=1]` each.
- `r85-harbor-repro`: `entities[4].id: duplicate entities id 'harbor'` and `timeline[0].place_id: ambiguous place entity 'harbor'`; `2 violation(s); no canon changed` `[rc=1]`.

These match `reports/round-1/current-baseline.json:5-9` and `reports/round-1/baseline-probes.json:6-10`; the baseline fixture JSON bytes also match the audited snapshot.

**HEAD checker, same five byte-identical inputs.** Command:

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  python3 corpus/fixtures/check_bible.py "corpus/live/runs/round-85/probe-inputs/$case"
done
```

Observed additions, enumerated against the baseline findings above:

- `r85-control`: no output addition; same `CLEAN...0 violations` `[rc=0]`.
- `r85-unique-break-control`: no output addition; same record-2 chain-break line and count `[rc=1]`.
- `r85-masked-ambiguous`: retained the old duplicate-ID finding; added exactly `entities[3].provenance[1].to_holder: ambiguous entity 'vault'` and `entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous`; `3 violation(s); no canon changed` `[rc=1]`. The downstream record-2 chain break remains unreported.
- `r85-isolated-ambiguous`: retained the duplicate-ID finding; added exactly `entities[3].provenance[2].to_holder: ambiguous entity 'vault'` and the same notice at `entities[3].provenance[2]`; `3 violation(s); no canon changed` `[rc=1]`.
- `r85-harbor-repro`: retained the old duplicate-ID and timeline-place lines; added `entities[3].provenance[1].to_holder: ambiguous entity 'harbor'`, the notice at `entities[3].provenance[1]`, and `entities[3].provenance[2].from_holder: ambiguous entity 'harbor'`; `5 violation(s); no canon changed` `[rc=1]`.

Comparison command: `python3 /tmp/r87-CB1/compare_outputs.py`. Observed output: `r85-control: baseline_rc=0; head_rc=0; preexisting_violation_lines_preserved=True`; the same `preexisting_violation_lines_preserved=True` with `baseline_rc=1; head_rc=1` for `r85-unique-break-control`, `r85-masked-ambiguous`, `r85-isolated-ambiguous`, and `r85-harbor-repro`. The comparison filters only new holder-local ambiguity and unassessed-notice lines. This establishes the exact current C1 delta: one notice is emitted at the first ambiguous record, not at each later record.

**Clean/broken chain, order, and dangling states.** Commands and observed outputs:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-valid
# CLEAN: schema, citations, relations, timeline; 0 violations [rc=0]
python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-broken
# VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
# 1 violation(s); no canon changed [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-clean-provenance
# CLEAN: schema, citations, relations, timeline; 0 violations [rc=0]
python3 corpus/fixtures/check_bible.py probes/r87-first-from-break
# VIOLATION: entities[3].provenance[0]: provenance chain break; first record must have from_holder null [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-tick-order-break
# VIOLATION: entities[3].provenance[1].tick: provenance tick 0 must be greater than previous tick 0 [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-dangling-to
# VIOLATION: entities[3].provenance[1].to_holder: dangling entity 'missing-holder' [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-dangling-from
# VIOLATION: entities[3].provenance[2].from_holder: dangling entity 'missing-holder' [rc=1]
```

Each violating case ended `N violation(s); no canon changed`. This confirms the documented clean chain, non-null first `from_holder`, wrong later holder, non-increasing tick, and dangling classification in both fields.

**Ambiguous holder identity, both directions, and local disclosure.** Commands ran against scratch cases with a duplicated, schema-valid `vault` entity:

```sh
python3 corpus/fixtures/check_bible.py probes/r87-ambiguous-to
python3 corpus/fixtures/check_bible.py probes/r87-first-ambiguous-from
python3 corpus/fixtures/check_bible.py probes/r87-ambiguous-both
```

Observed output (all findings and summary lines):

- `r87-ambiguous-to`: `VIOLATION: entities[5].id: duplicate entities id 'vault'`; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; `VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous`; `3 violation(s); no canon changed` `[rc=1]`.
- `r87-first-ambiguous-from`: `VIOLATION: entities[5].id: duplicate entities id 'vault'`; `VIOLATION: entities[3].provenance[0].tick: required nonnegative integer`; `VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'vault'`; the same notice at record 1; `4 violation(s); no canon changed` `[rc=1]`.
- `r87-ambiguous-both`: duplicate-ID finding; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; `VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'vault'`; one exact notice at record 1; `4 violation(s); no canon changed` `[rc=1]`.

The ambiguous record does not generate a definite chain/tick comparison. `r87-ambiguous-masks-tick` has a later unique-holder record whose tick equals the ambiguous record's tick and whose `from_holder` would break continuity. Command `python3 corpus/fixtures/check_bible.py probes/r87-ambiguous-masks-tick` observed exactly the duplicate-ID line, the record-1 `to_holder` ambiguity line, the record-1 unassessed notice, and `3 violation(s); no canon changed` `[rc=1]`; no later chain-break or tick-order finding appeared.

**Permanent latch and record-local diagnostics after an earlier stop.** Commands:

```sh
python3 corpus/fixtures/check_bible.py probes/r87-ambiguous-after-invalid-tick
python3 corpus/fixtures/check_bible.py probes/r87-malformed-before-ambiguity
python3 corpus/fixtures/check_bible.py probes/r87-dangling-before-ambiguity
python3 corpus/fixtures/check_bible.py probes/r87-unknown-source-before-ambiguity
```

Observed output (repeated unchanged lines abbreviated only after their full signature is given above):

- `r87-ambiguous-after-invalid-tick`: `VIOLATION: entities[5].id: duplicate entities id 'vault'`; `VIOLATION: entities[3].provenance[0].tick: required nonnegative integer`; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; the record-1 notice with the exact text shown above; `4 violation(s); no canon changed` `[rc=1]`.
- `r87-malformed-before-ambiguity`: same duplicate-ID line; `VIOLATION: entities[3].provenance[0]: expected exactly tick, from_holder, to_holder, source_id`; record-1 `to_holder` ambiguity and notice; `4 violation(s); no canon changed` `[rc=1]`.
- `r87-dangling-before-ambiguity`: same duplicate-ID line; `VIOLATION: entities[3].provenance[0].to_holder: dangling entity 'missing-holder'`; record-1 `to_holder` ambiguity and notice; `VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'vault'`; `5 violation(s); no canon changed` `[rc=1]`.
- `r87-unknown-source-before-ambiguity`: same duplicate-ID line; `VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'unknown-source'`; record-1 `to_holder` ambiguity and notice; `4 violation(s); no canon changed` `[rc=1]`.

Thus the notice is emitted even when another invalidity already latched comparisons. After ambiguity, record-level diagnostics still run:

- Command `python3 corpus/fixtures/check_bible.py probes/r87-later-local-dangling`: `VIOLATION: entities[5].id: duplicate entities id 'vault'`; record-0 `to_holder` ambiguity and notice; `VIOLATION: entities[3].provenance[1].to_holder: dangling entity 'missing-holder'`; `4 violation(s); no canon changed` `[rc=1]`.
- Command `python3 corpus/fixtures/check_bible.py probes/r87-later-unique-source-unknown`: duplicate-ID line; record-0 `to_holder` ambiguity and notice; `VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'missing-source'`; `4 violation(s); no canon changed` `[rc=1]`.
- Command `python3 corpus/fixtures/check_bible.py probes/r87-later-key-error`: duplicate-ID line; record-0 `to_holder` ambiguity and notice; `VIOLATION: entities[3].provenance[1]: expected exactly tick, from_holder, to_holder, source_id`; `5 violation(s); no canon changed` `[rc=1]`.
- Command `python3 corpus/fixtures/check_bible.py probes/r87-repeat-ambiguity`: duplicate-ID line; `VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'vault'`; one exact notice at record 0; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; `VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'vault'`; `5 violation(s); no canon changed` `[rc=1]`.
- Command `python3 corpus/fixtures/check_bible.py probes/r87-two-item-notices`: `VIOLATION: entities[6].id: duplicate entities id 'vault'`; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; notice at `entities[3].provenance[1]`; `VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'vault'`; `VIOLATION: entities[4].provenance[0].to_holder: ambiguous entity 'vault'`; notice at `entities[4].provenance[0]`; `6 violation(s); no canon changed` `[rc=1]`.

**Upstream eligibility, ambiguous-source qualifier, and independent checks.** Commands and observed output:

```sh
python3 corpus/fixtures/check_bible.py probes/r87-nonitem
# VIOLATION: entities[3].provenance: only valid on item entities
# 1 violation(s); no canon changed [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-duplicate-item
# VIOLATION: entities[4].id: duplicate entities id 'seal'
# VIOLATION: relations[0].to: ambiguous entity 'seal'
# 2 violation(s); no canon changed [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-source-unavailable
# VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'probes/r87-source-unavailable/sources.json'
# 1 violation(s); no canon changed [rc=1]
python3 corpus/fixtures/check_bible.py probes/r87-ambiguous-source-break
# VIOLATION: entities[3].provenance[2]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'vault', got 'mira'
# 9 violation(s); no canon changed [rc=1]
```

The first three suppress chain comparison for non-item, non-unique item ID, and unavailable source index; their remaining local/global findings continue. The source-ambiguous case retains the documented input-structural prefix on a definite break. Command `python3 corpus/fixtures/check_bible.py probes/r87-independent-all-checks` observed: `VIOLATION: entities[5].id: duplicate entities id 'vault'`; `VIOLATION: relations[1].to: dangling entity 'missing-map'`; record-0 `to_holder` ambiguity and notice; `VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2`; `VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'`; `6 violation(s); no canon changed` `[rc=1]`. The same three independent relation/timeline lines appear from `python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions`.

No-mutation verification command: `python3 /tmp/r87-CB1/verify_no_mutation.py`. Observed output: `command_returncode=1`; `VIOLATION: entities[5].id: duplicate entities id 'vault'`; `VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'`; the exact record-1 unassessed notice shown above; `3 violation(s); no canon changed`; `fixture_bytes_unchanged=True` after SHA-256 snapshots of every fixture file. The standard-recheck command `python3 corpus/fixtures/measure_holder_disclosure.py --revision HEAD` failed with `python3: can't open file '/tmp/r87-CB1/corpus/fixtures/measure_holder_disclosure.py': [Errno 2] No such file or directory` `[rc=2]`; `git cat-file -e HEAD:corpus/fixtures/measure_holder_disclosure.py` also reported that the path does not exist.

## Findings & named debt

- **Confirmed at HEAD:** holder ambiguity in either field produces the matching local diagnostic and leaves the record invalid (`check_bible.py:217-230`); the first ambiguous holder emits the exact one-per-item notice (`:231-233`); invalid records latch the comparison gate and later records do not resume it (`:243-255`). The unique-chain, dangling, tick-order, source-prefix, and upstream eligibility claims in `holder-assessment-boundary.md:70-75,105-129` match the replay evidence above.
- **Historical baseline confirmed:** the baseline checker and baseline-byte-identical probes reproduce the stored round-1 outputs, including duplicate-only ambiguity and the unique break. HEAD adds only the intended local holder disclosures/notice on the five cases; old finding lines and exit codes remain.
- **Stale status snapshot:** `holder-assessment-boundary.md:14-20,191-208` labels integrated behavior “STATIC PENDING PARENT RUNTIME” / “CONTRACT-SPECIFIED, PENDING PARENT RUNTIME.” Those were valid author-time notes, but they do not describe the audited HEAD and should be replaced with an as-of revision plus the CB1 replay pointer. The measured-results slot `:210-214` should distinguish this replay from the separate five-gate score.
- **Unavailable measurement entry point:** `holder-assessment-boundary.md:22-30,146-157` presents `measure_holder_disclosure.py` as the agreed recheck command, but the file is absent from HEAD. No five-gate `passed` count or score is claimed. Draft replacements are in `patches/CB1-drift.json`.
- **C1 coordination debt:** the current doc's “exactly one notice per item” wording (`:52-55,73-75,107-112`) correctly matches HEAD. C1's requested every-record disclosure after the stop is a later behavioral change; if C1 lands, update these rows before C2 cites the table. HEAD itself still emits one notice only at the first ambiguous record.
- The editor checklist's safe-action recommendations and the explicit non-claims about fictional truth, source support, rights, and AI-training permission are normative/editorial boundaries, not propositions this structural checker can adjudicate; no such truth claim was inferred from a clean result.

## Handoff

- Land `lore-shokunin/.ufo/waves/round-87/CB1.md` as this seat's replay evidence and `lore-shokunin/.ufo/waves/round-87/patches/CB1-drift.json` as the proposed knowledge-file correction. No checker or fixture patch is proposed.
- After C1 is integrated, update `corpus/knowledge/holder-assessment-boundary.md` from the draft status/recheck replacements and revise the one-notice wording to the actual per-record output; then rerun the recorded cases against the delivered checker before C2 uses the boundary table.
