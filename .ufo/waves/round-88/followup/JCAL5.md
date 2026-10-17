# JCAL5 — Calibration judge #5 (method-varied census)

Round 88 follow-up wave, world-bible lane. Judged tree: delivered work commit
`2ea9ef13a928475b13fd578740ea521bed4bd649` (baseline `dfd1fbc3711f2b28597d74444819aca91fe6bc31`,
tree clean at judgement). All measurements are against a `git archive` copy of
that commit, never against intent or scratch patches. Python `3.14.7`, `python3 -I`.

Method is deliberately varied from the sibling judges: shuffled traversal
(`random.Random(8802)`), isolated interpreter mode, and an **independently
regenerated baseline** rather than trusting `B1-tuples.json`.

## Work performed

1. `git archive 2ea9ef1 | tar -x -C /tmp/lore-r88-JCAL5` and
   `git archive dfd1fbc | tar -x -C /tmp/lore-r88-JCAL5-base`.
2. Wrote `/tmp/lore-r88-JCAL5/census_jcal5.py`: enumerate direct `corpus/fixtures/`
   child directories, shuffle with seed 8802, run
   `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` once per
   directory with the archive root as cwd, record `{exit, stdout_sha256,
   violation_count}`.
3. Ran it on the delivered archive (run1), repeated it (run2), and ran a third
   pass with seed 8803 to test traversal-order independence.
4. Ran the same script on my own baseline archive and compared against
   `patches/B1-tuples.json`.
5. Built the delta table (`/tmp/lore-r88-JCAL5/delta_jcal5.py`) and a mechanical
   disclosure-coverage sweep (`/tmp/lore-r88-JCAL5/sweep2.py`).
6. Diffed baseline vs delivered stdout for every changed fixture, and replayed the
   five `corpus/live/runs/round-85/probe-inputs/*` cases pasted in
   `corpus/knowledge/holder-assessment-boundary.md`.
7. Wrote `followup/JCAL5-delta.json` (this seat's evidence artifact). No tracked
   file outside `followup/JCAL5*` was written; no commit, push, or registry write.

## Before → after measurements

### Independent baseline reproduction

```text
$ python3 -I census_jcal5.py /tmp/lore-r88-JCAL5-base /tmp/lore-r88-JCAL5-base/own-baseline.json
fixture_count=145 seed=8802 first=r61-direct-duplicate-member last=r25-to-unique
exit_counts={"0": 30, "1": 115}
total_violations=331
tuple_file=.../own-baseline.json bytes=25637 sha256=76cf55c0cdce35c538bb869033e1c9642c92901f650304ce547328aec2efb106
```

`own_baseline_keys 145 / B1_keys 145 / key_set_equal True / differing_rows 0`.
My regenerated `dfd1fbc` census is byte-identical to `B1-tuples.json`, so the
delta below does not depend on B1's artifact.

### Delivered census and delta

```text
$ python3 -I census_jcal5.py /tmp/lore-r88-JCAL5 /tmp/lore-r88-JCAL5/run1.json
fixture_count=149 seed=8802 first=r62-partial last=r25-to-unique
exit_counts={"0": 31, "1": 118}
total_violations=367
tuple_file=.../run1.json bytes=26345 sha256=9a54d1e04e60b88f31019fb20ac3c9e424dbfd4cdbb30469fcf67eb2d101d7f0
```

Delta vs `B1-tuples.json` (exact command and full table in `JCAL5-delta.json`):

```text
baseline 145 dirs (exit 0=30, nonzero=115, 331 violations)
delivered 149 dirs (exit 0=31, nonzero=118, 367 violations)
changed_count=9  new_count=4  missing_count=0  exit_change_count=0  violation_delta=+36
```

The **9+4 delta is reproduced a third time, by a different method**: `new_count=4`,
`changed_count=9`, `exit_change_count=0` match the round-88 C1 claim exactly.

New paths (all four are the round's own fixtures):

| path | exit | violations |
|---|---|---|
| `corpus/fixtures/r88-m3-maya-cluster` | 0 | 0 |
| `corpus/fixtures/r88-mixed-stop` | 1 | 6 |
| `corpus/fixtures/r88-nonholder-stop` | 1 | 4 |
| `corpus/fixtures/r88-shape-ambiguous-armed` | 1 | 5 |

The nine changed paths, all `stdout_sha256` + `violation_count` only (no exit
change): `r61-independent-empty` 17→18, `r61-independent-unavailable` 6→7,
`r87-masked-break-from-ambiguous` 6→5, `r87-masked-break-to-ambiguous` 6→5,
`r87-probe-entry-shape` 2→8, `r87-probe-multi-invalid` 6→5,
`r87-probe-nonitem-kinds` 8→9, `r87-probe-record-and-chain` 34→46,
`r87-probe-shape-ambiguous` 2→5. The two pre-r87 `r61-*` deltas are purely
**additive** disclosures (diff shows one added disclosure line and a +1 count;
no line removed). The reductions (`6→5`, `6→5`, `6→5`) are the removal of the
superseded r87 causal wording, not loss of a real finding — verified line-by-line
by diff (below).

### Determinism

```text
run1 sha256 = run2 sha256 = 9a54d1e04e60b88f31019fb20ac3c9e424dbfd4cdbb30469fcf67eb2d101d7f0
$ cmp run1.json run2.json   -> byte-identical
seed 8803 run: fixture_count=149, same totals, sha256 9a54d1e0...  -> run1 == run3 tuple map
```

The tuple map is byte-reproducible and traversal-order independent.

### Disclosure coverage (mechanical sweep)

For every fixture, for each entity that latched a first stop, the sweep asserts
that each provenance record at index ≥ origin carries a disclosure naming that
origin, that no record before the origin carries one, and that every disclosure
line carries the `input-structural finding, not sourced-canon` qualifier.

```text
fixtures_with_disclosures 12 / origin_latches 17 / disclosure_lines 47
qualifier_missing 0 / fixtures_with_gaps 0
disclosures_containing_causal_because 0
```

Observed first-stop causes across the census (each is emitted as
`first stop: <cause> at <origin>`): ambiguous holder identity (to/from, single
and combined), `malformed record (expected object)`,
`malformed record (unexpected field set); ambiguous holder identity …`,
`duplicate item id 'rope'`, `provenance attached to a non-item entity`,
`source table unavailable`, `unknown source '<id>'`.

Direct evidence for the three C1 sub-claims:

- **(i) shape-invalid dict record arms the stop** — `r87-probe-shape-ambiguous`
  now emits 5 findings (was 2), including
  `entities[5].provenance[0].to_holder: ambiguous entity 'dup'` and the combined
  `first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]`
  on records [0] and [1]; the new durable fixture `r88-shape-ambiguous-armed`
  shows the same shape.
- **(ii) no over-attribution** — `r88-mixed-stop` names the earlier cause
  (`first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]`)
  on records [0], [1], [2], while still reporting the later local
  `entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'`. The
  later ambiguity no longer steals the cause.
- **(iii) non-holder causes disclose** — `r88-nonholder-stop` emits the
  unknown-source disclosure on records [0], [1], [2]. The dangling-holder cause
  has **no durable fixture** in the delivered tree (see debt).

### Documentation parity (measured drift)

Replaying the exact commands pasted in `corpus/knowledge/holder-assessment-boundary.md`
against the delivered checker:

```text
r85-masked-ambiguous    baseline dfd1fbc: 5 findings (old wording)   delivered: 4 findings (new wording)
r85-isolated-ambiguous  baseline dfd1fbc: 4 findings                 delivered: 3 findings
r85-harbor-repro        baseline dfd1fbc: 7 findings                 delivered: 6 findings
```

The doc's "Observed output (verbatim)" block and its "The contract" section
describe the r87 two-notice wording (`…unassessed because ambiguous holder
identity … first occurred at …`, `…unassessed at this and all later records
because holder identity is ambiguous`) that the delivered checker no longer
emits. `git show --stat 2ea9ef1` confirms neither
`corpus/knowledge/holder-assessment-boundary.md` nor
`corpus/knowledge/r87-provenance-chain-decision-table.md` was touched.

### C2 / C3 spot checks

- `r88-m3-maya-cluster` exits 0 (`CLEAN: schema, citations, relations, timeline; 0 violations`),
  giving the delivered census its 31st clean exit; it is the 2nd
  `inspiration-note.md` cluster (r87-myth-cluster + r88-m3-maya-cluster).
- `corpus/knowledge/r88-sourced-inspiration-decision-table.md` is present with the
  R1B scope comment; `reference-ledger.md` carries the ETCSL/Inana row with
  attribution, rights, and AI-training permission in three distinct cells.
- `r87-myth-cluster` OBS-1 files (`lowwater-hymn-excerpt.md`, `entities.json`,
  `symbolism-clause-map.md`) are changed in `2ea9ef1` as claimed.

## Findings & named debt

**Axis verdicts (delivered tree at `2ea9ef1`, per-axis, no scalars):**

- **C1 calibration — improved** on the measured behaviors. The 9+4 delta is
  independently reproduced (own baseline byte-identical to B1), 0 exit changes,
  the 145 baseline tuples are preserved except the 9 enumerable disclosure
  deltas, shape-invalid dict records arm the stop, the actual first cause is
  named at and after every stop with 0 coverage gaps, same-record causes are
  combined, the qualifier is on all 47 disclosure lines, and no causal
  `because` wording remains in any delivered output.
- **C2 coverage — improved** on the checked evidence (second sourced-mythology
  cluster exits 0; inspiration-note files 1→2; census 145→149).
- **C3 depth — improved** on the checked evidence (decision table present with
  the R1B scope note; ETCSL row registered in `reference-ledger.md`).
- **Documentation parity — harmed** (this is the trade in the round). Two
  `corpus/knowledge/` documents that state the checker's provenance contract and
  paste its verbatim outputs were not refreshed; their pasted outputs no longer
  reproduce on the delivered tree. Because a trade anywhere is not an
  improvement, C1's "improved" verdict is contingent: it is improved on
  behavior, but the round as a whole is **not** a clean improvement while the
  in-repo contract doc contradicts the shipped checker.

**Named debt (with evidence):**

- **D-1 doc drift (highest).** `corpus/knowledge/holder-assessment-boundary.md`
  and `corpus/knowledge/r87-provenance-chain-decision-table.md` still present the
  r87 wording and the r87 finding counts as the contract. Mitigation on record:
  both pin their own snapshot commit (`2b48ca7`), so they are not fabrications —
  but they are the lane's stated behavioral contract and no r88 successor exists.
  Repair belongs to the follow-up/integration seats (X1 explicitly declined it
  under its write boundary).
- **D-2 dangling-holder disclosure has no durable fixture.** The sweep finds no
  fixture emitting `first stop: dangling holder …`; only X1's scratch probe
  exercised it. The code path exists (`record_stop_cause = 'dangling holder …'`),
  so this is a coverage gap in the delivered artifact, not a behavior gap.
- **D-3 `r88-mixed-stop` combined-cause coverage is single-fixture.** The
  "same-record simultaneous causes" summary is demonstrated only by the
  shape-invalid fixtures (`malformed record … ; ambiguous holder identity …`).
  No fixture combines two non-shape causes on one record.
- **D-4 record-level vs entity-level origin labelling.** Chain-level stops
  (`duplicate item id`, non-item, unavailable source table) name the origin as
  `entities[i].provenance` (no index) while record-level stops name
  `entities[i].provenance[k]`; the sweep had to special-case this. It is
  consistent and disclosed, but the two origin formats are worth an explicit
  line in the refreshed contract doc.

**Scope limits.** This seat judged only the delivered fixture census and the
five r85 probe replays; it did not re-derive the C2 excerpt clause matches or
the C3 table rows beyond presence and exit status. The round-88 follow-up
directory was populated by sibling seats during this run (`JCAL1-delta.json`,
`JCOV5.md`, `JDEP1-4`, `K1.md`, `V2.md`); my delta agrees with `JCAL1`'s
`changed_count=9 / new_count=4` by an independent method.

## Handoff

- `lore-shokunin/.ufo/waves/round-88/followup/JCAL5-delta.json` — method, own
  baseline reproduction, delta table (9 changed + 4 new, full field-level
  before/after), determinism hashes, disclosure sweep, doc-parity check.
- `lore-shokunin/.ufo/waves/round-88/followup/JCAL5.md` — this report.
- Scratch (not committed): `/tmp/lore-r88-JCAL5/` (delivered archive, census
  scripts, run1/run2/run3, sweep) and `/tmp/lore-r88-JCAL5-base/` (baseline
  archive + own baseline census).
- Recommended next move: refresh the two `corpus/knowledge/` provenance docs to
  the delivered wording/counts (D-1), and add one durable dangling-holder-stop
  fixture (D-2) plus one two-non-shape-cause fixture (D-3) before the next
  calibration round.
