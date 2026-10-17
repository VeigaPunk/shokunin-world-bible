# JCOV1 — Coverage judge #1 (cluster structure + checker)

Seat: `JCOV1`. Wave: round-88 follow-up. Repo: `lore-shokunin`.
Judged artifact: the **delivered tree at `2ea9ef1`** (working tree clean; `git diff 2ea9ef1 --stat` empty, so the blobs I read are the commit's).
Baseline for comparison: `dfd1fbc`. Scratch probes: `/tmp/jcov1/`. Raw measurements: `followup/JCOV1-measurements.json`.

No tracked file was modified except this report and its JSON companion. No commit, no push, no registry write.

## Work performed

1. Confirmed the delivered tree is byte-identical to `2ea9ef1` (`git diff 2ea9ef1 --stat` → empty) and enumerated the cluster from the commit blobs, not the working copy.
2. Ran the seat checklist mechanically against `corpus/fixtures/r88-m3-maya-cluster/` with a purpose-written probe (`/tmp/jcov1_probe.py`): entity kinds, relation types, reciprocal-alliance detection, `depends_on` edges, citation resolution, and the occupied-slot slot key.
3. Ran `corpus/fixtures/check_bible.py` on the new cluster and on its r87 sibling; both exit 0.
4. Built an independent census (`/tmp/jcov1/census.py`): archived `dfd1fbc` to `/tmp/jcov1/base`, then ran the checker over **every** directory in `corpus/fixtures` on both trees and diffed the per-fixture `(exit, first-line, line-count)` tuples. This independently reproduces the C1 census claim.
5. Ran four control probes in scratch (`/tmp/jcov1/ctrl-*`) to prove the checker guards the fixture does not exercise are live: same-entity-same-tick double-booking, reciprocal faction alliance, one-way faction alliance, and a `depends_on` edge.
6. Verified the OBS-1 repair text and the r88 clause-map fidelity with direct text checks (the checker does not read Markdown).
7. Located where the structural coverage the r88 cluster lacks still lives in the census, so the gap can be scored rather than guessed.

## Before → after measurements

### Checklist items (delivered tree)

| Item | Command | Observed | Verdict |
|---|---|---|---|
| ≥1 faction entity kind | `python3 -c "import json;print(sorted(set(e['kind'] for e in json.load(open('corpus/fixtures/r88-m3-maya-cluster/entities.json')))))"` | `['character', 'place']` | **FAIL** |
| ≥3 relations, one reciprocal alliance pair | `python3 -c "import json;print(len(json.load(open('corpus/fixtures/r88-m3-maya-cluster/relations.json'))))"` | `0` | **FAIL** |
| ≥2 timeline events | `python3 -c "import json;print(len(json.load(open('corpus/fixtures/r88-m3-maya-cluster/timeline.json'))))"` | `2` | **PASS** |
| ≥1 `depends_on` edge | `python3 -c "import json;print([(e['id'],e['depends_on']) for e in json.load(open('corpus/fixtures/r88-m3-maya-cluster/timeline.json'))])"` | `[('aru-ninth-bell', []), ('evin-ninth-bell', [])]` | **FAIL** |
| Occupied-slot near-miss (two entities, same tick, different places) | `python3 -c "import json;print([(e['id'],e['tick'],e['entity_id'],e['place_id']) for e in json.load(open('corpus/fixtures/r88-m3-maya-cluster/timeline.json'))])"` | `[('aru-ninth-bell', 9, 'aru', 'quiet-rise'), ('evin-ninth-bell', 9, 'evin', 'salt-court')]` | **PASS** — named: **Aru at Quiet Rise, tick 9** and **Evin at Salt Court, tick 9** |
| Every citation resolves uniquely | `/tmp/jcov1_probe.py` | `source ids: ['veil-verse', 'paired-clock'] unique: True` / `citation refs total: 10 non-uniquely-resolving: []` / `refs per source: Counter({'paired-clock': 10})` | **PASS** |
| Checker exit 0 | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster; echo EXIT=$?` | `CLEAN: schema, citations, relations, timeline; 0 violations` / `EXIT=0` | **PASS** |

r87 sibling: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations`, `EXIT=0`. Both clusters exit 0, as C2 claims.

### Census (independent reproduction of the C1 count claim)

Command: `python3 /tmp/jcov1/census.py <tree> <out.json>` over every dir in `corpus/fixtures`.

- baseline `dfd1fbc`: **145** dirs; delivered `2ea9ef1`: **149** dirs.
- new: `['r88-m3-maya-cluster', 'r88-mixed-stop', 'r88-nonholder-stop', 'r88-shape-ambiguous-armed']`; removed: `[]`.
- **exit-code changes: 0.**
- behaviourally changed fixtures: **9** — `r61-independent-empty` 18→19 lines, `r61-independent-unavailable` 7→8, `r87-masked-break-from-ambiguous` 7→6, `r87-masked-break-to-ambiguous` 7→6, `r87-probe-entry-shape` 3→9, `r87-probe-multi-invalid` 7→6, `r87-probe-nonitem-kinds` 9→10, `r87-probe-record-and-chain` 35→47, `r87-probe-shape-ambiguous` 3→6.
- 5 further tuple diffs are path-string-only (baseline was run from `/tmp`), not behavioural.
- This reproduces the claim "9 changed + 4 new of 149 dirs, 0 exit changes" exactly, including the 2 pre-r87 `r61` additive disclosures.
- `inspiration-note.md` count: 1 → 2.
- New fixture exits at head: `r88-m3-maya-cluster` 0; `r88-mixed-stop` 1 (`duplicate entities id 'f1-mixed-dup'`, 7 lines); `r88-nonholder-stop` 1 (`unknown in-world source 'f1-nonholder-missing-source'`, 5 lines); `r88-shape-ambiguous-armed` 1 (`duplicate entities id 'f1-shape-dup'`, 6 lines).

### Control probes (scratch, to prove the guards the fixture does not touch are live)

| Probe | Mutation | Observed | Exit |
|---|---|---|---|
| `ctrl-doublebook` | same entity at same tick, two places | `VIOLATION: timeline[1]: double-booked 'aru' at tick 9 in timeline[0] ('quiet-rise') and 'salt-court'` | 1 |
| `ctrl-faction-recip` | 2 factions + reciprocal `allied_with` | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 |
| `ctrl-faction-oneway` | 2 factions + one-way `allied_with` | `VIOLATION: relations[0]: allied_with faction relation 'pact-a' -> 'pact-b' lacks a sourced reciprocal relation` | 1 |
| `ctrl-depends` | `depends_on := ['aru-ninth-bell']` | `VIOLATION: timeline[1].depends_on: timeline inversion 'aru-ninth-bell' tick 9 not before 'evin-ninth-bell' tick 9` | 1 |

The `ctrl-doublebook` result is the decisive one for the near-miss item: the guard keys on `(entity_id, tick)`, so the delivered pair (two *different* entities sharing tick 9) never approaches it. `ctrl-depends` also shows the delivered fixture's own tick arrangement makes an intra-fixture `depends_on` edge impossible without a tick bump (both events sit at tick 9, and the checker rejects `dep >= tick`).

### OBS-1 repair (C2 second half)

- Delivered variant is **`M4-obs1-excerpt.patch`**, not the variant M4 recommended (`M4-obs1-repoint.patch`).
- `python3 -c '... gate_named; first_appearance; claim_source; clause_matches ...'` → `gate_named=True; first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=8/8`.
- The hymn excerpt now names the Gate, the Gate's entity claim was narrowed to what that line says, and the map gained the `at the Mother-Tide Gate` row (8 rows). The unsupported "names the Mother-Tide Gate as a shore threshold" claim is gone.

### r88 clause-map fidelity

Strict substring test of each mapped clause against `source-excerpt.md`: 2 mapped, **1 strict match**. `'He called out ‘Earth,’'` → `False`; `'and the solid land appeared.'` → `True`. Row 1 uses curly **single** quotes while the excerpt uses curly **double** quotes; it resolves only after quote normalization (this is M5's `pass_with_punctuation_note`, confirmed).

## Findings & named debt

1. **The delivered cluster is structurally thinner than the seat checklist's cluster template, and three items are simply absent.** `r88-m3-maya-cluster` has 4 entities (`character`×2, `place`×2), **0 factions**, **0 relations**, and **0 `depends_on` edges**. M5 selected M3 over M1/M2 precisely because M3 was the narrowest candidate that passed the excerpt-support bar; M1 carried factions `reedbound`/`flint-choir` with a reciprocal `allied_with` pair and a `depends_on` chain, and M2 carried `grey-chime-guild`/`rainwrights`. Neither was integrated. The round's declared C2 wording ("second sourced-mythology cluster, passage-level locators, clause→element index, 1→2 inspiration notes, census grows, both clusters exit 0") does **not** require factions/relations/`depends_on`, and M5's compliance bar does not either — so this is an unmet *seat-checklist* bar, not a breach of the round's own claim.
2. **No checker path coverage is lost by that gap.** The paths the r88 cluster leaves untouched are exercised elsewhere in the delivered census: `r87-myth-cluster` (2 factions + a reciprocal `allied_with` pair + a 3-edge `depends_on` chain), `ally-one-way`/`ally-reciprocal` (reciprocity), 6 fixtures with faction entities, 13 fixtures producing `double-booked`, and 99 fixtures with non-empty `depends_on`. The gap is richness of the new exemplar, not loss of guard coverage.
3. **The near-miss is a shared-tick near-miss, not an occupied-slot one.** The fixture README calls it "an occupied-slot near-miss"; the checker's occupied slot is `(entity_id, tick)`, and Aru and Evin occupy different slots. The delivered pair demonstrates that a shared tick must not be flagged, which is real and useful, but it does not exercise the double-booking guard. Named debt: if the round wants an occupied-slot near-miss *control pair* (one double-booking that must fire beside one that must not), no such pair was added in r88.
4. **`veil-verse` is declared but never referenced.** `sources.json` lists it; no entity claim, relation, or timeline event cites it. The authored verse it labels lives in `fictional-excerpts.md` outside the JSON graph. Not a violation (the checker does not require full source utilisation), but it is an unused citation slot in a cluster whose whole point is citation discipline.
5. **Clause-map punctuation mismatch (1 of 2 rows).** Row 1's `‘Earth,’` does not appear verbatim in the delivered excerpt's `“Earth,”`. Quote-normalized resolution is what makes it 2/2. Named debt: the clause index's quotation is not byte-faithful to the excerpt it indexes.
6. **OBS-1 was repaired with the non-recommended variant.** M4 recommended `repoint` (attribution moves to the already-attested `gate-witness`, poem and map untouched) and explicitly warned that `excerpt` "adds new authored lore and map maintenance". The integrated tree is `excerpt`. The delivered state is coherent (8/8, claim narrowed, checker clean), so this is a documentation gap — the integration's deviation from the reviewer's recommendation is not recorded anywhere I could find — rather than a defect.
7. **The checker still cannot read the excerpt or the map.** `check_bible.py` accepts a cluster whose Markdown support is broken; clause fidelity and claim-to-excerpt support are only checkable by ad-hoc text scripts like the ones M4 and I ran. This is the pre-existing M4-named debt, unchanged by r88.

## Verdict recommendation

**Coverage axis: `improved`** — measured against the delivered tree at `2ea9ef1` versus `dfd1fbc`, with no trade: a second sourced-mythology cluster from a distinct family (Spence 1913 K'iche/Maya prose vs r87's ETCSL Sumerian) exists with a passage-level locator and a clause→element index; inspiration notes 1→2; census 145→149 with 0 removed and 0 exit-code changes; every one of the cluster's 10 citations resolves uniquely; both clusters exit 0; the OBS-1 attribution is repaired at 8/8 clause fidelity; and the shared-tick near-miss is delivered and correctly not flagged.

**Explicitly not counted as improved:** the seat checklist's three structural items — ≥1 faction, ≥3 relations with a reciprocal alliance pair, ≥1 `depends_on` edge — are **absent from the delivered tree**. If the L1 intends that structural checklist as the bar rather than the round's declared C2 wording, the correct verdict on those three items is **`unchanged`** (nothing delivered), and the axis verdict should be read as improved-on-the-declared-claim with three named unmet items. I did not inflate the verdict to cover them.

Nothing in the delivered tree was found **harmed**: no fixture was removed, no exit code moved, no previously-resolving citation broke.

## Handoff

- Files written by this seat: `.ufo/waves/round-88/followup/JCOV1.md` (this report) and `.ufo/waves/round-88/followup/JCOV1-measurements.json`. No other repo writes; scratch confined to `/tmp/jcov1/`; no commit, push, or registry write.
- Reproduction: `cd lore-shokunin && python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster` (exit 0); the census script is `/tmp/jcov1/census.py` and the checklist probe is `/tmp/jcov1_probe.py` (both scratch-only; the JSON records the exact inline commands if the scripts are gone).
- For the L1: the three unmet structural items and the shared-tick-vs-occupied-slot wording (findings 1, 3) are the decisions that need an owner. If a structural exemplar is wanted, M1's or M2's faction/relation block is the ready-made material already sitting in `patches/M1-cluster2.patch` and `patches/M2-cluster2.patch`.
- Not verified by this seat (outside its mission, another seat's remit): the C1 stop-cause disclosure semantics, the C3 decision table and reference-ledger row, and whether the M3 cluster's Spence locator resolves against the live Gutenberg page.
