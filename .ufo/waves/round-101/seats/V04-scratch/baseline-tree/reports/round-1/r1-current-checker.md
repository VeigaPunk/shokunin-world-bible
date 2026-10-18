# r1-current checker: holder-ambiguity disclosure

Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline `5eb9451baff217c19d5786405f9b2aa500b7c1b7`.
Owned file: `corpus/fixtures/check_bible.py` (only provenance-loop edit). This report: `reports/round-1/r1-current-checker.md`.
LSP: none configured (parent-verified); static review by reading.

## Change (observed diff applied this seat)

Nine added lines inside `check()`'s per-item provenance record loop; zero removed or rewritten
statements. Old line 330 total, new 339. Old line 185+ shifts by +1 after each insertion point.

1. `:185` (new, per-item init after `chain_has_ambiguous_source = False`):
   `holder_ambiguity_notice_emitted = False`
2. `:204` (new, per-record init after `valid = True`):
   `record_holder_ambiguous = False`
3. `:217-220` (old `elif entity_id_counts[to_holder] != 1:` silent branch) now also appends
   `{record_label}.to_holder: ambiguous entity {to_holder!r}` and sets
   `record_holder_ambiguous = True`, keeping `valid = False`.
4. `:227-230` (old `elif entity_id_counts[from_holder] != 1:` silent branch) symmetrically appends
   `{record_label}.from_holder: ambiguous entity {from_holder!r}`, sets the record flag, keeps
   `valid = False`.
5. `:231-233` (new block after both holder sections, before the `source_id` section):
   `if record_holder_ambiguous and not holder_ambiguity_notice_emitted:` appends
   `{record_label}: provenance continuity and tick-order comparisons unassessed at this and all
   later records because holder identity is ambiguous`
   and latches `holder_ambiguity_notice_emitted = True`.

Message wording/label shape mirrors the existing relations endpoint phrasing
(`{location}.{endpoint}: ambiguous entity {id!r}`, old `:168`) and the shared interface contract
text verbatim.

## Contract trace (static reasoning, not execution)

- Both ambiguous holder references voiced, record remains invalid: `valid = False` retained at
  `:220`/`:230` → old `:234-237` block (now `:243-246`) resets `previous_holder/previous_tick` and
  latches `can_check_chain = False` exactly as before.
- One notice per item at first ambiguous-holder record: second boolean gates re-emission (`:231`,
  `:233`). A record with both fields ambiguous emits both field errors, then a single notice
  (the notice `if` sits outside the `from_holder is not None` block at `:221`).
- Fires even when earlier malformed input already stopped comparisons: the notice gate reads only
  `record_holder_ambiguous` and `holder_ambiguity_notice_emitted`, never `can_check_chain`; holder
  validation at `:211-230` runs on every dict-shaped record regardless of the latch, which is how
  the pre-change code already silently consumed ambiguity.
- Conservative permanent latch preserved: `can_check_chain` is assigned `False` or the initial
  conjunct only; no statement sets it `True` after init (`:183`). Ambiguity and all malformed-input
  paths keep comparisons off for that record and every later one (now `:247-256` comparison block
  textually unchanged). No inferred or resumed "break" finding.
- Nothing suppressed: all pre-existing `errors.append` calls, the dangling-holder branches
  (`:214-216`, `:224-226`), the `chain_has_ambiguous_source` source-ambiguity prefix machinery
  (`:241-242`, `:250-254`), `check()` signature, and every non-provenance section (schema,
  contradictions, relations, allied reciprocity, timeline occupancy/dependency) are byte-identical
  to baseline. Fictional JSON input files untouched.
- Diagnostic ordering nuance for the measurement gates: within one ambiguous record the list order
  is tick/format errors → holder ambiguous-entity error(s) → scope notice → `.source_id` errors.
  Gates should assert membership at the expected `record_label`, not list adjacency.

## Measurement-gate mapping (static expectation)

- Clean chain: no ambiguous branch taken, no notice — unchanged behavior.
- Unique-holder real break: comparison block untouched — unchanged behavior.
- Dangling-holder explicitness (both fields): pre-existing `dangling entity` errors retained
  verbatim at `:215`/`:225`.
- Ambiguous-to / ambiguous-from: two `ambiguous entity` field errors plus exactly one notice at
  the first ambiguous record; later valid records in the same item emit nothing from `:247-256`
  because `can_check_chain` stays `False`.

## Critic falsifier trace (parent-relayed; static only)

Sequence: malformed/invalid record 0 → holder-ambiguous record 1 → two later valid records 2-3
with bad continuity and reversed tick, same item.

- Record 0 takes `:191` or `:197`: `can_check_chain = False`, `continue`.
- Record 1: holder validation `:211-230` runs unconditionally (never under `if can_check_chain`),
  so `record_holder_ambiguous = True` at `:219`/`:229`; the notice gate `:231` reads only
  `record_holder_ambiguous` and `holder_ambiguity_notice_emitted` — both independent of the latch —
  so the notice emits at `records[1]`'s label despite record 0 already having stopped comparisons.
- Records 2-3: `valid` survives, reach `:247 if can_check_chain:` → `False`; every definite
  break/tick-order producer (`:250`, `:252`, `:254`) is inside that block, so reversed ticks and
  continuity mismatch emit nothing. The `:255-256` state updates run but cannot generate errors.
- No comparisons resume: `can_check_chain` post-init assignments are exactly `:191`, `:197`, `:245`,
  all `False`; no `True` writeback exists. Exactly one notice per item at the first ambiguous
  record, and neither of records 2-3 gets one (`holder_ambiguity_notice_emitted` latched at `:233`).

## Evidence retained

- `git status --porcelain` before edit: `corpus/fixtures/check_bible.py` clean vs `5eb9451...`;
  `reports/round-1/` untracked (inherited `dispatch.json`, `critic.md`, `baseline-probes.json`,
  `current-*` files present, untouched by this seat). No concurrent modification observed at any
  point; edit snapshot tag `0B4C` → post-edit `6676`.
- Parent's `reports/round-1/current-baseline.json` r85 probe description (masked ambiguity emits
  only the global duplicate; continuity + tick checks silently dead at and after that record) is
  the pre-change behavior this diff converts into explicit disclosure.

## Risks / blockers

- Unrun (intentionally, mid-flight wave ban): `python3 corpus/fixtures/check_bible.py <dir>` on any
  bible, `corpus/fixtures/measure_holder_disclosure.py` (owned by R1Measure — the CLI contract
  `--revision <commit>` reads this file from the requested revision; parent runs the integrated
  gate once after all seats land), syntax check, test/fixture suites, formatters. Correctness
  above is static review of read-back lines `171-256`, not execution.
- Residual risk: a gate that counts exact total violation lines on an ambiguity sample must expect
  2–3 added lines per affected item (field error(s) + one notice); gates matching on message
  substrings are immune.
- No blocker. Scope complete for the assigned file.
