# JCAL3 — Calibration judge #3 (method-varied)

Seat: JCAL3. Wave: round-87 follow-up (world-bible lane). Fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Measured tree: `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (`2b48ca7`), taken as `git archive 2b48ca7` — the **commit tree only**; the working directory was never read for any measurement, so concurrent sibling follow-up writes cannot contaminate a result.

This seat repeats JCAL1's census **by a deliberately different method**, verifies the two masked fixtures' per-record disclosures independently, and confirms additions-only on the three r85 live probes. No file under version control was written by this seat.

## Method (what makes this a different measurement, not a repeat)

| dimension | JCAL1 | JCAL3 (this seat) |
|---|---|---|
| tree source | live worktree at repo root | `git archive 2b48ca7 \| tar -x -C /tmp/jcal3/arch-2b48ca7` |
| interpreter | `python3` | `python3 -I` (isolated: no user site, no `PYTHON*` env) |
| traversal | `sorted()` | `random.Random(870).shuffle(sorted(...))` |
| prior-tuple baseline | `patches/B1-tuples.json` | **two** baselines: `B1-tuples.json` *and* `.ufo/rounds/r86/diagnostic.stdout.json` `fixture_runs[].before` |

Archive integrity: `sha256sum /tmp/jcal3/arch-2b48ca7/corpus/fixtures/check_bible.py` → `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`, byte-equal to the delivered checker. `git rev-parse 2b48ca7^{tree}` → `73422a138bbb5e987c83bc18191310ba34c13082`. Interpreter `Python 3.14.7`.

Command form for every census run (`cwd` = archive root):

```
python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>
```

## Verdict recommendation

**Calibration axis — improved (bounded).** The delivered checker discloses, per record, that continuity and tick-order comparison were not performed once a holder identity is ambiguous, and it does so **purely additively**: over 138 census dirs + 5 live probes + 7 scratch probes it removed zero findings, altered zero finding lines, and changed zero exit codes.

The bound is two-part and both parts are pre-existing, not introduced by C1:

1. the disclosure is armed only from **well-shaped** records, so an ambiguous holder reference carried on a malformed record is neither reported nor disclosed, and a genuine later break in that item stays silent (independently reproduced in Part E);
2. it fires only for **holder-ambiguity** stops, not for other stop causes (JCAL4's finding, not re-measured here).

Neither bound weakens the axis verdict: the delivered behavior is a strict superset of the pre-C1 behavior on every input measured.

---

## Part A — census, method-varied

Script `/tmp/jcal3/census2.py`; artifact `.ufo/waves/round-87/followup/JCAL3-census.json`.

```
total 138 clean 30 violations 108 stderr_nonempty []
```

Observed on the archive:

```json
{
  "dir_count": 138,
  "exit_counts": {"0": 30, "1": 108},
  "violation_total": 272,
  "stderr_nonempty": []
}
```

- **Census arithmetic reproduces exactly.** `133 + 5 = 138` dirs; exits `28×0 + 105×1 = 133` inherited, `30×0 + 108×1 = 138` delivered; `259 + 13 = 272` violations, and the whole 13-violation delta sits in the five new dirs.
- **Prior 133 tuples byte-identical against two independent pinned baselines.** vs `B1-tuples.json`: 0 changed, 0 missing. vs the r86 diagnostic's `before` tuples (baseline checker `88c9b1d…` on baseline corpus `5eb9451`): 0 changed. Two different artifacts, same answer — this is stronger than JCAL1's single-baseline check.
- **Order independence.** `sorted` vs `seed=870` vs `seed=99` vs a repeat of `seed=870`: 0 tuple diffs in every pairing. Traversal order does not affect the census.
- **Cross-artifact agreement.** Against I3's `r87-extended-tuples.json` (138 entries): 0 diffs on `exit`, `stdout_sha256`, `violation_count`. JCOV2's independent census records `fixture_dirs 138`, `exit_histogram {"0": 30, "1": 108}` — same.

Per-new-dir tuples (`rc`, violation count, stdout sha256 prefix):

| fixture | exit | violations | stdout sha256 (16) |
|---|---|---|---|
| `r87-chain-unique-valid` | 0 | 0 | `afe570fcebf45fe3` |
| `r87-chain-unique-broken` | 1 | 1 | `6d2e1487098a48da` |
| `r87-masked-break-from-ambiguous` | 1 | 6 | `f6ec78fbeac0c258` |
| `r87-masked-break-to-ambiguous` | 1 | 6 | `bded9b133e16d975` |
| `r87-myth-cluster` | 0 | 0 | `afe570fcebf45fe3` |

### Method hazard found (new, not reported by JCAL1)

Tuple equality is **argv-path-form sensitive**. Re-running the same census passing the fixture directory as an *absolute* path instead of the canonical root-relative `corpus/fixtures/<name>` changes 5 tuples:

```
corpus/fixtures/r5-missing-file
corpus/fixtures/r62-missing
corpus/fixtures/r67-claim-source-unavailable-control
corpus/fixtures/r67-claim-source-unavailable-empty
corpus/fixtures/r67-claim-source-unavailable-whitespace
```

Cause: for these fixtures a table file is absent, and the `OSError` text embedded in the `VIOLATION: … cannot load JSON: …` line contains the path as given. `patches/S4-census-extension.md` is right that the command is not part of tuple equality — but its *effect* on stdout is. Any future census must fix the root-relative form, which both this seat and JCAL1 used.

## Part B — masked fixtures: per-record disclosure, independently verified

Artifact `.ufo/waves/round-87/followup/JCAL3-disclosure.json`.

Both fixtures have one `item` entity at `entities[3]` with **3** provenance records and the ambiguity at record **0**. Delivered output for `r87-masked-break-to-ambiguous` (`python3 -I corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous`, exit 1):

```text
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
6 violation(s); no canon changed
```

The `from_ambiguous` fixture is identical with `from_holder 'dup'` substituted throughout. Independently checked properties:

| property | from-ambiguous | to-ambiguous |
|---|---|---|
| records / stop index | 3 / 0 | 3 / 0 |
| disclosure lines with `unassessed because ambiguous holder identity` | 3 | 3 |
| those lines equal my independently computed expected strings, in order | yes | yes |
| one disclosure per record at/after the stop | yes | yes |
| names holder field + id + origin record | yes | yes |
| chain-break / tick-order finding at/after the stop | none | none |
| finding that chooses among the duplicate identities | none | none |
| vs pre-C1: added lines / removed findings | +4 / 0 | +4 / 0 |

`+4` = three new finding lines plus the derived footer (`3 violation(s)` → `6 violation(s)`). No pre-existing finding line is altered or removed.

**The fixtures genuinely contain masked breaks.** Removing the second `dup` row (holder resolves uniquely) makes both checkers — pre-C1 and delivered — produce byte-identical output with one chain-break finding each:

```
r87-masked-break-from-ambiguous → entities[3].provenance[0]: provenance chain break; first record must have from_holder null
r87-masked-break-to-ambiguous   → entities[3].provenance[1]: provenance chain break; expected from_holder 'dup', got 'mira'
```

So the `from` fixture's masked break is at record 0 (`from_holder 'dup'` where `null` is required) and the `to` fixture's is at record 1; with the holder ambiguous, neither is reported and the new disclosure is the only signal that they were not checked. This also confirms the fixtures are well-formed controls whose only behavioral difference from their unique-holder siblings is the ambiguity itself.

## Part C — the three r85 live probes: additions-only

Artifact `.ufo/waves/round-87/followup/JCAL3-probes.json`. The three are `r85-masked-ambiguous`, `r85-harbor-repro`, `r85-isolated-ambiguous` — the same three tuples C6's audit flags as changed and the same three JCAL1's Part D lists.

Authenticity of the live evidence first: `probe-inputs/*/entities.json` sha256 match the r85 manifest exactly (`69dc7fd1…`, `59655ce3…`, `6ccaf656…`), and the recorded `probe-r85-*.txt` bodies reproduce **byte-for-byte** under the r85-era checker `88c9b1d…` (extracted from `22a95ff`, sha verified), with matching exit codes — for all five probes, not just three.

Pre-C1 (`e8f24162…`) → delivered:

| probe | in the three | findings | removed findings | added outside disclosure signature | findings superset |
|---|---|---|---|---|---|
| `r85-harbor-repro` | yes | 5 → 7 | 0 | 1 (derived footer) | yes |
| `r85-isolated-ambiguous` | yes | 3 → 4 | 0 | 1 (derived footer) | yes |
| `r85-masked-ambiguous` | yes | 3 → 5 | 0 | 1 (derived footer) | yes |
| `r85-control` | no | 0 → 0 | 0 | 0 | yes (CLEAN, exit 0, byte-identical) |
| `r85-unique-break-control` | no | 1 → 1 | 0 | 0 | yes (byte-identical) |

Against the **recorded** r85 outputs (`88c9b1d`) the same property holds: `masked 1 → 5`, `isolated 1 → 4`, `harbor-repro 2 → 7`, zero finding lines removed; the only non-added line in each case is the derived footer, whose value necessarily tracks the count.

**Additions-only: confirmed on all three**, and additionally on the two probes outside the required set. Note the exact sense: every pre-existing *finding* line is preserved verbatim and in order; the only line that changes without being added is the aggregate count footer, which is a derived line, not a finding. A claim of byte-identical stdout would be false; a claim of additions-only findings is true.

## Part D — additions-only at census scale

Pre-C1 checker `e8f24162…` vs delivered, over all 138 census dirs:

```
dirs 138
pre_c1_exit_histogram {0: 30, 1: 108}
rc_changed []
stdout_changed_dirs 2 ['r87-masked-break-from-ambiguous', 'r87-masked-break-to-ambiguous']
removed_non_summary_lines {}
total_added_lines 8
```

Exactly two dirs change, they are the two the C1 commit names, the delta is 8 added lines (4 each), no non-footer line is removed anywhere, and no exit code moves. This is the whole-census form of C1's "prior 133 fixture tuples byte-identical" claim, measured against the pre-C1 revision rather than only against the inherited baseline.

## Part E — residual-gap reproduction and latch controls (scratch, `/tmp`)

Seven probes built in `/tmp/jcal3/probes{2}/` from `corpus/fixtures/r87-chain-unique-broken` by duplicating `mira`; full stdout in `JCAL3-probes.json`.

| probe | construction | delivered result |
|---|---|---|
| `p1` | ambiguous holder well-shaped at `[0]`, genuine break in tail | stop + 3 disclosures; break masked but disclosed; +4 lines |
| `p6` | ambiguity first appears at a **well-shaped** `[1]`, tail unique with a real break | stop at `[1]`, disclosures at `[1]`/`[2]`, +3 lines, break masked-but-disclosed |
| `p5` | ambiguity first appears at a **shape-violating** `[1]`, tail unique with a real break | **+0 lines vs pre-C1; no disclosure anywhere; the real break at `[2]` and the ambiguous reference at `[1]` both unreported** |
| `p7` | as `p5` but tail continuous | +0 lines, no disclosure |
| `p4` | item A ambiguous, item B unique with a genuine break | item B's break **still reported** (`entities[5].provenance[2]: provenance chain break; expected from_holder 'tower', got 'harbor'`) — latch is per item, no cross-item suppression |

`p5`/`p7` reproduce JCAL1's residual gap by an independent construction. In `check_bible.py` the object-shape and key-set checks `continue` before the holder-resolution block, so a malformed record never reaches `record_holder_ambiguous`, never arms `holder_ambiguity_stop`, and (through `can_check_chain = False`) silently disables all later comparisons. Both checkers produce identical output on `p5`/`p7`, so this is an unclosed gap, **not** a C1 regression.

An earlier construction of mine put the malformed ambiguous record at `[0]` with a tail that also referenced the ambiguous id; the disclosure then appeared from `[1]` onward, so the gap did not show. The gap needs the ambiguity to *first* appear at the malformed record — worth stating so a future round does not "disprove" the gap with a mis-built probe.

## Divergences and agreements with sibling seats

- **JCAL1**: agrees on every shared number — 138 dirs, `{0:30,1:108}`, 272 violations, 133 prior tuples unchanged, the two changed dirs, +13 violations in the 5 new dirs, the 3 live-probe deltas, the duplicated notice at the stop record, and the residual gap. My agreement is by a different tree source, interpreter mode, traversal order, and baseline artifact.
- **JCAL4**: its mixed-stop result is consistent with `p5` here; both show that a non-holder stop cause produces no per-record disclosure. I did not re-measure its fixtures.
- **I3 / JCOV2 / H3**: their census artifacts agree with mine to the byte on all 138 entries.
- **One naming caution**: `r87-masked-break-from-ambiguous`'s masked break is at record `0` (first-record-must-be-null), not in the tail — its tail is continuous. Anyone reading the fixture name as "a later break" will mis-scope a probe.

## Named debt (no action taken by this seat)

1. **Malformed-ambiguous residual vector** (Part E). Pre-existing, identical pre- and post-C1. Deserves an explicit accept-as-debt-or-close decision; closing it means resolving holder references independently of record shape, or arming the stop from the shape-failure path.
2. **Non-holder stop causes carry no per-record disclosure** (JCAL4; corroborated by `p5`). Pre-existing; the C1 commit message is correctly scoped to holder stops and should be read that way in the round record.
3. **Stop record carries two near-duplicate notices** (Part B). Verbosity, not correctness.
4. **Census argv-path-form sensitivity** (Part A). Any future census must use the root-relative form.
5. **Coverage of the new path is fixture-thin**: 2 of 138 census dirs exercise the disclosure. C1's own added fixtures are the only census cases guarding it; a regression here would be caught by 2 dirs.

## Handoff / artifacts

- `lore-shokunin/.ufo/waves/round-87/followup/JCAL3.md` — this report (untracked; nothing committed).
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL3-census.json` — method-varied census, two-baseline prior-tuple diff, cross-artifact agreement, path-form hazard.
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL3-disclosure.json` — masked-fixture per-record disclosure verification, pre-C1 delta, and the unmask test.
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL3-probes.json` — the 5 r85 live probes under three checkers, plus 7 scratch probes.
- Scratch retained: `/tmp/jcal3/{census.py,census2.py,verify.py,arch-2b48ca7/,old/check_bible.py,old/check_bible_r85.py,probes/,probes2/,unmask/}`.
