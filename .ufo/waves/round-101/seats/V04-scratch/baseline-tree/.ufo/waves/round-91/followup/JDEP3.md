# JDEP3 — Register + namespace (r91 follow-up)

## Work performed

Axes: register correctness (must stay empty / correctly absent), R10 namespace-rule
operability (worked negative case), delivered-tree evidence discipline.

Read `.ufo/waves/round-91/wave-spec.md`, the delivered R10 row and appendix incl. the
r91 namespace text in `corpus/knowledge/r88-sourced-inspiration-decision-table.md:26`
and `:104-108`, the r91 work patches `.ufo/waves/round-91/patches/D1-edges.patch` /
`D2-edges.patch`, seat J3's r91 register re-check, and the JDEP3 lineage cited in the
decision table. All measurements were run from `lore-shokunin/` against the delivered
tree at `c2ab3d0`; the scratch demo used only `/tmp/jdep3-ns` (10 tiny JSON files,
swept at the end). No tracked file other than this report and `JDEP3-namespace.json`
was written; no commit, no push.

Dependency wait protocol (default two 60-second checks, one background call):
check-01 `2026-10-17T08:33:06-03:00` followup_dir=yes head=c2ab3d0; check-02
`08:34:06` followup_dir=yes head=c2ab3d0; terminal `08:35:06`
files=`H4-c1-discrimination.json,H4-census.json,H4-lineage.json,H4.md,H4-probes.json,JCAL5-delta.json`.
Both work commits and peer follow-up artifacts were already present, so the seat
worked with the delivered tree and the observed peer inventory.

## Before → after measurements

**1. Delivered-tree preconditions.**

```sh
git rev-parse HEAD && sha256sum corpus/fixtures/check_bible.py && git diff a7c6a17..c2ab3d0 -- corpus/fixtures/check_bible.py | wc -l && git log -S "NAMESPACE COLLISION" --oneline -- corpus/knowledge/r88-sourced-inspiration-decision-table.md
```

```text
c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
0
c2ab3d0 lore r91: C3 R8/R10 r91 edge decisions (failed-gate disposition, withhold precedence, source_id namespace) + the r89 paraphrase demo's Inventory line (missed from the work commit)
```

The r91 checker is unchanged (`ff9fd2aa`); the namespace rule text landed at integration
(`c2ab3d0`). Delivered rule (read, not re-worded): `source_id` values are cluster-local
identifiers; a `source_id` shared across clusters is a NAMESPACE COLLISION, not identity
evidence — comparison keys are `(cluster-relative path, source_id)` pairs; a bare shared
id triggers the namespace check (rename or qualify one side) before any referent
comparison; a collision alone never enters the register.

**2. Register state (delivered tree).**

```sh
python3 -c "from pathlib import Path; print('register_present=', Path('corpus/knowledge/cross-cluster-contradictions.md').exists())"
```

```text
register_present= False
```

The only near-register artifact, `corpus/knowledge/r89-cross-cluster-contradiction.md`,
still carries `not a new canon assertion or an integration-ready register entry` and
`Do not treat this demo as an append` (both True). No other corpus path is a register.
Cross-check: `SCORECARD.md:232` (r90 record) states "Register correctly absent (JDEP3,
JDEP2)"; the r91 delivered tree still matches.

**3. Shared-referent comparison (must stay empty), delivered tree.**

```sh
python3 - <<'PY'   # entity ids/names, bare source ids, event ids, places, place refs, relation tuples, (entity,place,tick) slots
# full script in the seat log; compares corpus/fixtures/r87-myth-cluster vs r88-m3-maya-cluster and both r91-c1 fixtures
PY
```

```text
shared_entity_ids=[]
shared_entity_names_casefold=[]
shared_source_ids_bare=[]
shared_timeline_event_ids=[]
shared_place_ids=[]
shared_timeline_place_ids=[]
shared_relation_tuples=[]
shared_timeline_entity_place_tick=[]
r91-c1-null-chain_vs_r87-myth-cluster: entity_ids=[] names=[] source_ids=[] event_ids=[]
r91-c1-null-chain_vs_r88-m3-maya-cluster: entity_ids=[] names=[] source_ids=[] event_ids=[]
r91-c1-tick-unresolved_vs_r87-myth-cluster: entity_ids=[] names=[] source_ids=[] event_ids=[]
r91-c1-tick-unresolved_vs_r88-m3-maya-cluster: entity_ids=[] names=[] source_ids=[] event_ids=[]
```

All eight structured categories between the two landed clusters are empty, and the two
new r91 C1 fixtures share no entity id, name, source id, or event id with either landed
cluster. No register entry is justified.

**4. Namespace inventory over the delivered fixture corpus** (152 dirs with all four
tables; malformed-JSON dirs skipped as unserializable inputs).

```text
bare_source_id: distinct_ids=37 shared_across_dirs=10
  'courier-log' in 126 dirs, 'archive-ledger' in 121, 'tarin-note' in 20,
  'sella-bell7-note' in 18, 'vela-note' in 6, 'harbor-compact' in 3,
  'jorin-note' in 3, 'r89-f2-source' in 3, ...
landed source ids reused by other dirs: r87 (dune-register, gate-witness, lowwater-hymn,
  shell-charter, tide-bell-tally) = 0 each; r88-m3 (paired-clock, veil-verse) = 0 each
r91 fixture own ids: archive-ledger reused in 126 dirs, courier-log in 131 dirs
namespace_scoped_key_duplicates=0
```

So no bare source-id collision touches either landed cluster; the collisions that exist
are calibration-scaffolding reuse (the new r91-c1 fixtures copy the `mira`/`harbor`
base), which is exactly the class the namespace rule + landed-cluster register scope
handles without entries.

**5. Worked negative case in scratch** (`/tmp/jdep3-ns/cluster-a`, `cluster-b`; each one
source row with the same bare id `shared-marker` used by `first_appearance`, claims, and
a timeline event; otherwise disjoint: `a-court`/`a-warden` tick 4 vs
`b-dune`/`b-singer` tick 9; invented calibration text).

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3-ns/cluster-a ; printf 'cluster_a_exit=%s\n' "$?"
python3 corpus/fixtures/check_bible.py /tmp/jdep3-ns/cluster-b ; printf 'cluster_b_exit=%s\n' "$?"
python3 corpus/fixtures/check_bible.py /tmp/jdep3-ns/cluster-a /tmp/jdep3-ns/cluster-b ; printf 'two_dir_exit=%s\n' "$?"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
cluster_a_exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
cluster_b_exit=0
usage: check_bible.py [-h] bible
check_bible.py: error: unrecognized arguments: /tmp/jdep3-ns/cluster-b
two_dir_exit=2
```

Namespace check vs referent screen on the pair:

```text
bare_source_id_collision= ['shared-marker'] -> namespace check TRIGGERED
namespace_scoped_pair_intersection= []
referent_screen_shared_entity_ids= []
referent_screen_shared_names= []
referent_screen_shared_entity_place_tick= []
claim_a= 'The warden reads the marker at dawn.'
claim_b= 'The chanter names the marker at dusk.'
shared_field_or_occasion=false
```

Disposition applied per the rule (rename one side), then rerun:

```text
cluster-b source ids now: ['b-shared-marker']
CLEAN: schema, citations, relations, timeline; 0 violations
renamed_cluster_b_exit=0
bare_source_id_collision_after_rename= []
```

Control — intra-cluster duplicate instead of cross-cluster collision (temporary second
`shared-marker` row in cluster-a, restored afterwards):

```text
VIOLATION: sources[1].id: duplicate sources id 'shared-marker'
VIOLATION: entities[0].first_appearance: ambiguous in-world source 'shared-marker'
VIOLATION: entities[0].claims[0].source_id: ambiguous in-world source 'shared-marker'
VIOLATION: entities[1].first_appearance: ambiguous in-world source 'shared-marker'
VIOLATION: entities[1].claims[0].source_id: ambiguous in-world source 'shared-marker'
VIOLATION: timeline[0].source_id: ambiguous in-world source 'shared-marker'
6 violation(s); no canon changed
dup_control_exit=1
restored cluster-a to one shared-marker row → CLEAN, exit 0
```

Register outcome after the whole demo: `register_present=False`; no entry was written
anywhere; the collision's only correct dispositions were the namespace rename (or
qualify) — never a register entry.

## Findings & named debt

- **Namespace rule operative as delivered.** The bare collision fires the namespace
  check; path-qualified keys remove the false overlap; the rename clears it; per the
  rule text a collision alone never enters the register. The demo also reproduces the
  known manual-gate limit: the checker is single-directory (two-dir invocation exits 2)
  and has no cross-cluster registry, so this stays an integration-gate procedure, not a
  mechanical check. The control shows uniqueness is enforced only *within* a cluster.
- **Register correctly absent.** `corpus/knowledge/cross-cluster-contradictions.md` does
  not exist; the r89 worked example is still marked hypothetical/not-an-entry; no r91
  artifact created a register file. The shared-referent comparison stays empty on the
  delivered tree (landed pair 8/8 empty; r91-c1 fixtures empty vs both landed clusters).
- **Named debt (manual gate, pre-existing).** The namespace disposition ("rename or
  qualify one side") has no naming convention or durable note artifact; my demo used a
  `b-` prefix. A future corpus-wide validator would need to pick a convention (and could
  then mechanize the collision scan). No harness exists today, so this is not a defect
  in the delivered text — it is the boundary of what it can prove.
- **Observation for the CB1/JCAL lane (not JDEP3's surface, no write made):** the
  delivered reconstruction header (`corpus/knowledge/holder-assessment-boundary.md:1-6`)
  names one skipped item — `Skipped as named debt: D1 — Decision-table row 2 code refs.`
  The round brief describes two items named as skipped debt; the second is not in the
  delivered header (only occurrence of "Skipped" in the file). Worth reconciling before
  closure.
- **No harm and no trade observed** on the register/namespace surface: nothing changed,
  the register is still absent, and every probe left the repo untouched.

## Handoff

Wrote only `.ufo/waves/round-91/followup/JDEP3.md` and
`.ufo/waves/round-91/followup/JDEP3-namespace.json` (machine receipt: hashes, screen
results, scratch-case outcomes). Scratch `/tmp/jdep3-ns` swept; no `/tmp` archives kept.
No commit or push. Peer follow-up artifacts present during this seat: H4 (`H4.md` +
JSONs) and `JCAL5-delta.json`.

For the parent: the register/namespace lane can be closed as verified — register
correctly absent, shared-referent comparison empty on the delivered tree, and the R10
namespace rule's negative case reproduced end-to-end in scratch. Remaining items are
the two observations above (manual gate boundary; boundary-doc header skipped-debt count)
for the CB1/Q1 lanes, not blockers for this seat.