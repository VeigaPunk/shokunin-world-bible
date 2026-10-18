# V30 — receipt presence (round 100)

Scope: receipt presence and byte inventory only, not C1/C2/C3 admission or an all-axis verdict. Axes: coverage (reported seats and producer artifacts), calibration (observed bytes, no invented identities or absent-as-present credit), operability (bounded, self-subtracted waits), and non-interference (exclusive outputs).

Every command ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` for Python. Baseline is r99 closure `fe1ce46`; observed HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (the r100 declaration). `git merge-base --is-ancestor fe1ce46 HEAD` exited 0. The wave is uncommitted. No nested agents, commits, pushes, network, live freeze operation, corpus mutation, or other-seat report edit was performed by V30.

Authorized output paths are this report, the specifically requested `.ufo/waves/round-100/receipt.json` skeleton, and declared scratch `.ufo/waves/round-100/seats/V30-scratch/`. Absolute destinations were resolved and asserted within the lane before creation. The lane has no `AGENTS.md` (direct Read returned nonexistent; the lane Glob found none).

## Bounded poll — SELF subtracted

Actual command:

```sh
python3 -u /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V30-scratch/poll_presence.py
```

Observed exit 0. The durable records are `V30-scratch/poll.jsonl` and `V30-scratch/poll-result.json`. Poll cadence was 20 seconds, with the producer protocol's 40-try bound and this seat's explicit 1,200-second endgame bound. A report counted only as a nonempty top-level `seats/<SEAT>-*.md`; scratch directories were never reports. Every count removed V30, even though its own report did not yet exist.

Opening observation, `2026-10-18T02:33:37.001279+00:00`: 0 other reports; producer reports T1/T2/T3/T4 absent; the two r100 knowledge files absent; r99 pin present. Artifact existence alone did not constitute producer completion.

Observed final poll summary:

```text
tries_run: 34
artifacts_ready_try: 21
producer_protocol_exhausted_without_ready: false
endgame_threshold_others: 30
self_subtracted: true
stopped_reason: threshold_met_30_others_and_producer_artifacts
elapsed_seconds: 660.033
final.utc: 2026-10-18T02:44:37.033657+00:00
final.reports_present_excl_self: 30
final.producer_missing: []
final.artifact_missing: []
final.r99_pin_present: true
final.duplicates: {}
final.empty_reports: []
```

All four producer reports and all 16 artifact paths were ready at try 21, before the 40-try producer bound. The 30-other-report endgame condition was actually observed at try 34. No bounded stall escape or absent-as-present credit was used in this poll.

## Pre-report audit — actual files, not plans

Actual command:

```sh
python3 .ufo/waves/round-100/seats/V30-scratch/audit_presence.py --label pre-report
```

Observed exit 0, snapshot `2026-10-18T02:44:59.019650+00:00`:

```text
reports_present: 30
reports_present_excl_self: 30
reports_missing_count: 2
producer_absent: []
candidate_paths_present: 16
missing_candidate_paths: []
duplicates: {}
empty_reports: []
header_seat_mismatches: []
header_token_misses: []
unexpected_md: []
parent_tree_files: []
pin_count: 7
new_pins: [r99-window-lapse]
inherited_pins_changed: []
protected_files_changed: []
receipt_written: false
```

The 30 actual identifiers were T1–T4, V01–V17, V19–V23, and V25–V28. V30 was not created yet, and no V29 top-level report existed at that snapshot. The task supplies a total of 32 seats but not a full dispatch identifier roster; absent identifiers are not invented by filling numeric gaps. In particular, this audit does not assume that V18 or V24 was dispatched.

Producer report paths, each present and hashed:

- `.ufo/waves/round-100/seats/T1-chain-seven.md`
- `.ufo/waves/round-100/seats/T2-fixture-author.md`
- `.ufo/waves/round-100/seats/T3-fixture-docs.md`
- `.ufo/waves/round-100/seats/T4-knowledge-author.md`

The 16 artifact paths are `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/README.md`, `SKILL.md`; all ten files in `corpus/fixtures/r100-docket-review/` (`README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`); and `corpus/knowledge/{r100-crossing-arc-synthesis.md,r100-provenance-semantics-boundary.md,r99-gate-blind-spot-table.md}`. The audit records each SHA-256, size, and modification timestamp, rather than only a path count.

The protected files compared byte-for-byte against `fe1ce46` were `PROVINCE.md`, `SHONEN.md`, `README.md`, `l0-questions.md`, `corpus/fixtures/check_bible.py`, and `corpus/tools/{dependency_freeze.py,support_check.py,map_obligations.py,boundary_doc_check.py}`: all nine matched. An independent `python3`/`git diff --name-only HEAD --` check observed exactly four tracked wave changes: `SKILL.md`, the r99 blind-spot table, the tools README, and the freeze contract; `unexpected_tracked_changes` was `[]`. The preexisting r98 V58 resume note was left untouched. No parent-tree round-100 files were found.

Parsed contract comparison against `git show fe1ce46:corpus/tools/dependency-freeze-contract.json` observed six pins before, seven after, only `r99-window-lapse` added, no removed or changed inherited pin, schema/payload version 2, and only top-level `revision` changed outside `pins`. The revision refresh is not hidden as a literally addition-only text diff.

## Independent read-only artifact smoke checks

After T1's report landed, these actual commands were run concurrently, without `--freeze`:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

All seven exited 0, printed `RESULT PASS`, and had empty stderr. The last receipt was:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

After all four producer reports existed, these actual commands were run concurrently on the delivered r100 fixture:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

All exited 0 with empty stderr. Observed terminal receipts (support output excerpted, not represented as the full per-anchor output):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

These receipts establish their stated bounded structural/lexical/byte properties only. V30 does not infer whole-claim entailment, dependency semantics, testimony truth, chronology authentication, rights, permission, canon, or round admission from them. r100 is not silently added to the seven pinned fixtures.

## Receipt skeleton contract and reproducibility

The scratch builder and validator are `V30-scratch/audit_presence.py` and `V30-scratch/validate_receipt.py`; `poll_presence.py` supplies the finished bounded-poll record. The audit snapshots are `interim-audit.json`, `midwait-audit.json`, `producers-ready-audit.json`, and `pre-report-audit.json`; generated Python cache files remain inside this same scratch root.

A `python3` in-memory JSON round trip of the real builder passed before receipt creation: 13 observed reports were represented as 13 rows, all `agent_id` and `outcome` fields were null, all 16 artifact hashes were represented, and no dispatch ID or served-backend echo was invented. This was a builder-shape check, not a claim of final presence. An `ast.parse` check printed `SYNTAX PASS` for all three scripts; the audit itself has executed successfully on actual wave files.

The companion receipt is intentionally a skeleton: L1 must fill real `agent_id`, `outcome`, `dispatch_tool_call_id`, and returned dispatch summary from its actual dispatch result. Requested model/alias/effort are declaration fields, not a served-backend claim. Report existence does not mean that its agent completed or that its verdict is true. L1 must reconcile the real dispatch roster and refresh hashes after any later report or closure edits.

## Endgame follow-up and cardinality contradiction

This report was first landed only after the required 30-other-report threshold. The pre-report count above is retained as a historical snapshot, not presented as the final count. Follow-up `python3 -` polling used 20-second sleeps and explicitly subtracted SELF, with each follow-up capped at 240 seconds and also bounded by the original 20-minute endgame deadline. Durable evidence is `V30-scratch/followup-poll.json` and `V30-scratch/roster-poll.json`.

Observed follow-up output excerpts:

```text
2026-10-18T02:45:49.496765+00:00 reports_present=31 reports_present_excl_self=30 V29_present=false
2026-10-18T02:46:09.498264+00:00 reports_present=32 reports_present_excl_self=31 V29_present=false
FOLLOWUP all_31_others_present_after_V30_report_landing
2026-10-18T02:47:48.351907+00:00 reports_present=33 reports_present_excl_self=32 V29_present=false excess_over_declared_32=1
2026-10-18T02:51:08.349252+00:00 reports_present=34 reports_present_excl_self=33 V29_present=true excess_over_declared_32=2
ROSTER_FOLLOWUP known_V29_report_landed_roster_count_reaudited
```

The first follow-up's count-only success did **not** establish roster closure: V24 was the new landing while V29 remained absent. V18 then landed, followed by V29. Those late reports were retained, not dropped to fit 32. No stall escape was invoked: the known V29 report appeared at the final bounded observation, still inside the original 20-minute window.

Actual final-inventory command:

```sh
python3 .ufo/waves/round-100/seats/V30-scratch/audit_presence.py --label full-roster
```

Observed exit 0, snapshot `2026-10-18T02:51:23.714077+00:00`:

```text
reports_present: 34
reports_present_excl_self: 33
present: T1, T2, T3, T4, V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30
producer_absent: []
candidate_paths_present: 16
missing_candidate_paths: []
duplicates: {}
empty_reports: []
header_seat_mismatches: []
header_token_misses: []
unexpected_md: []
parent_tree_files: []
protected_files_changed: []
```

**Confirmed collection contradiction:** the declaration says 32 seats = 4 producers + 28 verifiers, but the actual top-level set is 34 distinct report identifiers = T1–T4 + V01–V30 (4 + 30). These are report identifiers, **not proof of 34 distinct agents**. Neither a 32-seat completion assertion nor a 34-agent assertion is established without L1's real dispatch result and identity mapping. `reports_missing_count: 0` is only arithmetic against the declared total and must not be read as a reconciled roster. The receipt preserves `requested_seats: 32`, all 34 observed rows, `reports_excess_count: 2`, and an explicit known-defect entry rather than silently normalizing either side.

A first 20-second `python3 -` hash-stability comparison intentionally failed its no-change assertion (exit 1):

```text
other_reports: 33
candidate_files: 16
report_changes: [V29-adjudicator.md]
candidate_changes: []
AssertionError
```

That failure records V29 still finishing its own report, not a changed producer deliverable. The same read-only hash-comparison logic was rerun over another 20 seconds, excluding only this currently finalized V30 report. Observed exit 0, recorded in `V30-scratch/stability-final.json`:

```text
seconds: 20
self_excluded_from_report_stability: true
other_reports: 33
candidate_files: 16
report_changes: []
candidate_changes: []
```

The earlier failed comparison is retained at `V30-scratch/stability.json`. No other-seat report was edited to obtain stability. The final receipt is generated after this V30 text is finalized so its own row can hash these final bytes. Companion generation/verification commands are:

```sh
python3 .ufo/waves/round-100/seats/V30-scratch/audit_presence.py --build-receipt --label delivered
python3 .ufo/waves/round-100/seats/V30-scratch/validate_receipt.py
```

The validator distinguishes structural/hash errors (exit 1) from the known declared-count contradiction (exit 2 even if all hashes and null identities validate). Its actual delivered-file result belongs to the final handoff, after receipt creation; no future validation is credited here. L1 must fill actual dispatch metadata, reconcile all 34 report identifiers, and refresh final hashes after closure. V29's delivered `V29-adjudicator.md` independently records AC-ROSTER and withholds admission; this presence audit neither re-adjudicates nor overrides that report.

FAIL — declared 32-report collection is contradicted by 34 distinct reports (T1–T4 + V01–V30); all producer/artifact paths are present, but dispatch identities and roster reconciliation remain L1 work.
