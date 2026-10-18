# JCOV1 — coverage judge #1 (r87-myth-cluster)

Seat mission: verify the delivered `corpus/fixtures/r87-myth-cluster/` on the delivered
tree — structural counts (entities incl. factions, relations incl. reciprocal alliance,
timeline events, dependency edges), `check_bible` exit 0, every row sourced with unique
source ids, contradiction record referencing two resolvable events — and give a verdict
recommendation for coverage.

## Measurement anchor

- Measured tree: `lore-shokunin` at `HEAD = 2b48ca72033dfd1060b6f81c4cf27ad83deae57f`
  (`2b48ca7 lore r87: work-wave evidence — 39 seat reports + patches (.ufo/waves/round-87), luna-max wave`).
- Base for all before/after comparisons: `28706dc` (pre-C1/C3; last tree with neither the
  checker disclosure change nor any r87 fixture).
- `git status --porcelain` on the delivered tree: ` M l0-questions.md` and
  `?? .ufo/waves/round-87/followup/`. Both are other seats' in-flight writes; this seat
  wrote no tracked file.
- Delivered fixture SHA-256 (anchor for any later re-measurement):

```text
14bf96df22053ecb7251fb46a5d0b28213cb9b4d5e5a2b7e99c701a83de74aa4  r87-myth-cluster/contradictions.json
7ca735916275b01a83b6ba863c3ce970fe434e150a9c50156f84a9187760c456  r87-myth-cluster/entities.json
1eef38f748c53b18fe7d5a977d340ef5200fdba9ec14c5d0dbb7dd9e57ada59c  r87-myth-cluster/inspiration-note.md
11ea7a0ad9fc424324c770545e1d6a962d485a0f57910a58ad347ff0dcd97e76  r87-myth-cluster/lowwater-hymn-excerpt.md
2b8e35a956829f766358f3d328b60bc2c0e077165d349a7259e03a18ce2a021c  r87-myth-cluster/README.md
8bd0b78801bacee5ffd2df72bad3f0915704ec5918618c8f7d64d840a1272631  r87-myth-cluster/relations.json
23fbb75a0f1f8cf07164debaf68dd1cca6b9a225854a73e7ebe20704efeb2d04  r87-myth-cluster/sources.json
8c3ee88e766b2293432f168d55bf8068d7d1e5f60c8e39585845bbc3d4286443  r87-myth-cluster/symbolism-clause-map.md
b4626c33a9f1d7fda75532e4e221e8c159cd8c4dcc25c80724bb54318c7284f1  r87-myth-cluster/timeline.json
```

## 1. Structural counts — PASS

Command (from the repo root):

```sh
python3 - <<'PY'
import json, collections
from pathlib import Path
p = Path('corpus/fixtures/r87-myth-cluster')
L = lambda n: json.loads((p/(n+'.json')).read_text())
ent, rel, src, tl, con = (L(n) for n in ('entities','relations','sources','timeline','contradictions'))
print('entities:', len(ent), dict(collections.Counter(e['kind'] for e in ent)))
print('relations:', len(rel), dict(collections.Counter(r['type'] for r in rel)))
print('timeline events:', len(tl), 'dependency edges:', sum(len(t['depends_on']) for t in tl))
print('sources:', len(src), 'contradictions:', len(con))
A = {(r['from'], r['to']) for r in rel if r['type'] == 'allied_with'}
print('allied edges:', len(A), 'reciprocal pairs:', sorted(p for p in A if (p[1], p[0]) in A))
print('deps:', [(t['id'], t['depends_on']) for t in tl])
PY
```

Observed:

```text
entities: 7 {'character': 2, 'place': 2, 'faction': 2, 'item': 1}
relations: 4 {'allied_with': 2, 'keeps_watch_with': 1, 'records_at': 1}
timeline events: 4 dependency edges: 3
sources: 5 contradictions: 1
allied edges: 2 reciprocal pairs: [('reedwardens', 'shellweavers'), ('shellweavers', 'reedwardens')]
deps: [('first-lowwater-signal', []), ('bell-tally-return', ['first-lowwater-signal']), ('moon-basin-vow-gate-account', ['bell-tally-return']), ('moon-basin-vow-dune-account', ['bell-tally-return'])]
```

Meets the C3 breadth claim in commit `e4708cb` exactly: 7 entities incl. 2 factions,
4 relations incl. a reciprocal `allied_with` pair, 4 timeline events with dependency edges,
a reported-not-resolved place contradiction.

## 2. `check_bible` exit 0 — PASS

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "EXIT=$?"
```

Observed:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

Checker identity on the delivered tree: `sha256sum corpus/fixtures/check_bible.py` →
`3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237` (base `28706dc`
checker is `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132`).

## 3. Every cited row resolves to a uniquely defined source id — PASS

Command:

```sh
python3 - <<'PY'
import json, collections
from pathlib import Path
p = Path('corpus/fixtures/r87-myth-cluster')
L = lambda n: json.loads((p/(n+'.json')).read_text())
ent, rel, src, tl = (L(n) for n in ('entities','relations','sources','timeline'))
defs = collections.Counter(s['id'] for s in src)
refs = ([('entities.%s.first_appearance' % e['id'], e['first_appearance']) for e in ent]
      + [('entities.%s.claims[%d]' % (e['id'], i), c['source_id']) for e in ent for i, c in enumerate(e['claims'])]
      + [('relations[%d]' % i, r['source_id']) for i, r in enumerate(rel)]
      + [('timeline.%s' % t['id'], t['source_id']) for t in tl])
print('source definitions:', dict(defs))
print('reference count:', len(refs), 'per source:', dict(collections.Counter(s for _, s in refs)))
print('unused sources:', [s for s in defs if s not in dict(collections.Counter(s for _, s in refs))])
print('refs to undefined sources:', [(l, s) for l, s in refs if defs.get(s, 0) == 0])
print('refs to multiply-defined sources:', [(l, s) for l, s in refs if defs.get(s, 0) > 1])
PY
```

Observed:

```text
source definitions: {'shell-charter': 1, 'lowwater-hymn': 1, 'gate-witness': 1, 'dune-register': 1, 'tide-bell-tally': 1}
reference count: 22 per source: {'gate-witness': 4, 'dune-register': 6, 'lowwater-hymn': 2, 'shell-charter': 7, 'tide-bell-tally': 3}
unused sources: []
refs to undefined sources: []
refs to multiply-defined sources: []
```

All 22 citations (7 entity `first_appearance` + 7 entity claims + 4 relation sources +
4 event sources) resolve to a source id defined exactly once; every one of the 5 sources
is used; no duplicates, no unknowns.

## 4. Contradiction references two resolvable events — PASS

Command and observed output (same run as §1/§3):

```text
contradiction moon-basin-vow-location claim_a: event=moon-basin-vow-gate-account count=1 field=place_id event_source=gate-witness
contradiction moon-basin-vow-location claim_b: event=moon-basin-vow-dune-account count=1 field=place_id event_source=dune-register
contradiction events distinct: True
timeline unresolvable entity_id: []
timeline unresolvable place_id: []
dangling depends_on: []
```

Both referenced events exist exactly once, the two references differ (distinct event ids),
the field is `place_id` (an allowed assertion field), each event's own `source_id` is unique
and resolvable, and the two events genuinely assert different values for the compared field
(`mother-tide-gate` vs `ash-dune-sanctuary`) — a real reported disagreement, not a bookkeeping
pair. The fixture README (`README.md:5`) and the ledger `why` both state the conflict is
reported, not resolved, which matches the checker's behaviour (it validates pointers only).

## 5. Falsifiability probes — the clean result is load-bearing, not vacuous

Eight scratch copies under `/tmp/jcov1/` (delivered tree untouched) with one mutation each,
replayed against the delivered checker. A clean fixture is only meaningful if the rules it
satisfies actually fire when violated.

| probe (scratch copy) | mutation | observed exit | observed finding |
|---|---|---|---|
| baseline | none | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `mut-c-ev-missing` | `claim_b.event_id` → `moon-basin-vow-nonexistent` | 1 | `contradictions[0].claim_b.event_id: expected exactly one timeline event 'moon-basin-vow-nonexistent'` |
| `mut-c-same` | `claim_b` := copy of `claim_a` | 1 | `contradictions[0]: claim_a and claim_b references must differ` |
| `mut-r-recip` | drop the `reedwardens -> shellweavers` edge | 1 | `relations[0]: allied_with faction relation 'shellweavers' -> 'reedwardens' lacks a sourced reciprocal relation` |
| `mut-t-dep` | `depends_on` → `['no-such-event']` | 1 | `timeline[1].depends_on: unknown event 'no-such-event'` |
| `mut-s-dup` | duplicate a `sources.json` row | 1 | `sources[5].id: duplicate sources id 'shell-charter'` + 7 `ambiguous in-world source` lines + 2 missing-reciprocal lines (10 total) |
| `mut-u-cite` | `relations[0].source_id` → `ghost-source` | 1 | `relations[0].source_id: unknown in-world source 'ghost-source'` (+ the reciprocal loss it implies) |
| `mut-r-dangle` | `relations[3].to` → `ghost-place` | 1 | `relations[3].to: dangling entity 'ghost-place'` |

Every rule class the cluster claims to satisfy (contradiction event resolvability,
distinct-claim rule, sourced reciprocal alliance, dependency resolvability, source-id
uniqueness, citation resolvability, relation endpoint resolvability) fires on the
corresponding mutation and is silent on the delivered input. The clean exit is therefore
evidence about the input, not a checker that skips these paths.

## 6. Preservation census — no harm to any inherited fixture

**Scope note (census is time-sensitive).** The counts below were measured while the fixture
set held 138 directories. After that measurement, seat I1 wrote two new untracked probe
directories, `corpus/fixtures/r87-probe-entry-shape/` and
`corpus/fixtures/r87-probe-record-and-chain/`, bringing the live count to 140. Both carry
`contradictions.json: []` and no factions, so re-running §7 with 140 directories reproduces
the same table and the same conclusion (re-verified after they appeared). Any census number
should therefore be re-derived at integration time rather than copied from this report.

Exit codes for every immediate fixture directory, delivered checker vs base `28706dc`
checker, both run against the delivered fixture tree:

```sh
for cb in corpus/fixtures/check_bible.py /tmp/jcov1/base/corpus/fixtures/check_bible.py; do
  for d in corpus/fixtures/*/; do
    out=$(python3 "$cb" "$d" 2>&1); printf '%s\t%s\t%s\n' "$(basename "$d")" "$?" "$(echo "$out" | tail -1)"
  done
done
```

Observed:

- 138 fixture directories on the delivered tree; 30 exit 0, 108 exit 1.
- Exit-code differences HEAD vs base: **none** (all 138 equal).
- Full-stdout differences: exactly **2**, and only the intended C1 fixtures —
  `r87-masked-break-from-ambiguous` and `r87-masked-break-to-ambiguous`, each gaining the
  three per-record `provenance continuity and tick-order comparisons unassessed because
  ambiguous holder identity …` lines (3 → 6 violations). No other fixture's output changed
  by a single byte.
- `r87-myth-cluster` output is byte-identical under the base checker and the delivered
  checker, i.e. the C3 coverage increment does not depend on the C1 checker change.

Census arithmetic for the record: base `28706dc` holds 133 fixture directories and 705
corpus JSON files; the delivered tree holds 138 and 730 (+5 directories, +25 JSON, all
5 files per new directory). Note for the census-extension seat: S4's
`S4-census-extension.md:6` assumed one newly added directory (134 runs, 705 + 5 JSON); the
delivered wave added five (`r87-chain-unique-valid`, `r87-chain-unique-broken`,
`r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`, `r87-myth-cluster`).

## 7. Is the coverage increment novel? — yes, measurably

Which clean fixtures carry a genuine (value-differing) contradiction pair, and do they
also carry factions, a reciprocal alliance, and multiple relations?

```sh
python3 - <<'PY'   # full script in the run log; columns: fixture, exit, factions, reciprocal, genuine contradiction pairs, entities, relations, events
PY
```

Observed, restricted to exit-0 fixtures with ≥1 genuine contradiction pair:

```text
fixture                           exit factions recip genCon ent rel ev
r35-bell7-conflict                0    0        False 1      6   1   4
r36-bell7-wrong-date              0    0        False 1      6   1   4
r37-ledger-unique                 0    0        False 1      6   1   4
r39-ledger-source-unique          0    0        False 1      6   1   4
r40-vela-listener                 0    0        False 1      7   1   5
r41-vela-direct-bell              0    0        False 1      7   1   5
r43-jorin-vela-sighting           0    0        False 1      8   1   6
r72-vela-slate-claim              0    0        False 1      8   1   6
r73-jorin-slate-claim             0    0        False 1      8   1   6
r83-vela-joint-nonsighting        0    0        False 1      7   1   5
r87-myth-cluster                  0    2        True  1      7   4   4
```

- 11 clean fixtures carry a genuine unresolved contradiction pair; the other 10 are all
  clones of one lineage (the same `harbor`/`tower` `bell7-location-reports` pair), each with
  exactly 1 relation and 0 factions.
- `r87-myth-cluster` is the only one that combines a genuine unresolved contradiction with
  2 factions, a sourced reciprocal alliance, and multiple dependency edges in one
  independent cluster. Contradiction-pair signature
  `(place_a, place_b, distinct_actors, distinct_event_sources)`:
  `('mother-tide-gate','ash-dune-sanctuary',True,True)` appears exactly once, versus the
  reused `('harbor','tower',True,True)` in 14 fixtures.
- Existing checker-finding templates exercised across the whole fixture set: 65 distinct
  templates. The cluster is clean, so it adds **no new finding template** — the increment is
  admitted positive-path surface (a richer valid input that must keep passing), not new
  error-path coverage. This bounds the claim.

## 8. Delivered artifact equals the reviewed candidate — PASS

```sh
mkdir -p /tmp/jcov1/m3 && git archive 28706dc | tar -x -C /tmp/jcov1/m3
git -C /tmp/jcov1/m3 apply /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-87/patches/M3-myth-cluster.patch
diff -r /tmp/jcov1/m3/corpus/fixtures/r87-myth-cluster corpus/fixtures/r87-myth-cluster
```

Observed: `IDENTICAL` (no diff output). The landed cluster is byte-for-byte the M3
candidate that `M4-compliance.json` recommended landing, and `M1`/`M2` remain unlanded as
recommended (their patches are present in `.ufo/waves/round-87/patches/` but contribute no
tracked file).

## 9. External citation spot check (independent of the checker)

`inspiration-note.md` cites `https://etcsl.orinst.ox.ac.uk/section1/tr141.htm` as
"Inana's descent to the nether world", composition 1.4.1, and describes the opening lines
plus lines 122–163 covering entry through seven gates with removal of dress and regalia.
`FetchURL` on that URL returned the ETCSL page text: lines 1–5 are the descent from heaven;
114–122 have the seven gates of the underworld bolted; 129–163 remove turban, beads,
pectoral, ring, measuring rod, and the *pala* dress at the seven gates. The citation is
substantively accurate, and the note's three separate open questions (attribution, rights,
AI-training permission) each remain explicitly unanswered — no rights or permission claim is
made. This is a citation-accuracy spot check only; it establishes nothing about rights,
permission, canon, or truth, and the note itself says so.

## Verdict recommendation (coverage)

| axis | verdict | evidence and bound |
|---|---|---|
| coverage | **improved** | Delivered tree admits a 5-directory, 25-JSON increment (133 → 138 fixture directories at measurement time, 705 → 730 corpus JSON; see the §6 scope note); `r87-myth-cluster` is the first fixture combining a genuine reported-not-resolved contradiction, 2 factions with a sourced reciprocal alliance, and 3 dependency edges in one independent cluster (§7). `check_bible` exits 0 with 0 violations (§2); all 22 citations resolve to uniquely defined source ids (§3); the contradiction references two distinct, uniquely sourced, resolvable events (§4); and every rule class the cluster satisfies fires under mutation (§5). |
| coverage — bound | — | The cluster is a clean input, so it adds **no new checker finding template** (65 templates unchanged); the gain is positive-path surface, not new error-path coverage. |
| calibration / depth / adjacency | **unchanged, no harm from this seat's measurements** | No checker rule changed for C3; the 138-fixture census (138 at measurement time) shows identical exit codes and only the two intended C1 stdout deltas (§6); `r87-myth-cluster` behaves identically under the base and delivered checker, so C3 neither needs nor masks the C1 change. |

Per the judging rules this is a verdict, not a score: **coverage improved, bounded; no axis
harmed** on the measurements above. This independently corroborates the coverage verdict
already recorded by seat JCOV2 (`.ufo/waves/round-87/followup/JCOV2.md:264`), which reached
the same bounded-improved conclusion through a different route.

## Named gaps and debt (not fixed by this seat — no write authority over these files)

1. **No Round 87 section in the fixture index.** `corpus/fixtures/README.md` documents
   rounds through 83 (`README.md:1000`, "## Round 83: Vela joint non-sighting scope") and
   never mentions `r87-myth-cluster`. The index is the fixture-registration surface, so the
   new cluster is counted by the census but not registered in the corpus index.
2. **Reciprocal alliance is attested by a single document.** Both `allied_with` edges cite
   the same source, `shell-charter`. The checker's reciprocal rule only requires the reverse
   record to cite a *unique* source, not a *different* one, so this cluster does not
   demonstrate two independently sourced reciprocal records — that combination exists only
   in the negative fixture `r7-ally-reverse-ambiguous` (`harbor-compact` vs
   `separate-compact`). The cluster's own README wording ("one sourced `allied_with` edge in
   each direction") is accurate; only the coverage claim must not be read as two-source
   attestation.
3. **`contradictions.json` has no negative sibling in this cluster.** The unresolvable-event
   and same-reference paths are exercised only by inherited fixtures
   (`r62-empty`, `r37-ledger-ambiguous`, `r62-malformed-side`) and by this seat's §5
   scratch probes, not by a landed r87 fixture.
4. **Prose discipline is unenforced by the checker.** `symbolism-clause-map.md`,
   `inspiration-note.md`, and `lowwater-hymn-excerpt.md` are not read by `check_bible.py`
   (the map itself says so at its last line). Their conformance rests on the review seats
   (C7, M4, JCOV4), not on a machine check.
5. **S4 census-extension arithmetic needs updating** for five new directories / 25 new JSON
   files rather than the assumed one directory / five files (§6).

## Reproducibility

Every command above runs from `/home/vgpnk/Projects/shokunin/lore-shokunin` on the delivered
tree `2b48ca7`. Scratch copies and mutation trees live under `/tmp/jcov1/`; no tracked file
in the repository was written by this seat, and nothing was committed or pushed.
