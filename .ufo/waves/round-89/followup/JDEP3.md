# JDEP3 — Depth judge #3 (register readiness), round 89

Seat: JDEP3. Wave: round-89 follow-up (world-bible lane), repo `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Judged on the DELIVERED tree at `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (`1b09f3f`), baseline `51b286b`.
Scratch: `/tmp/jdep3/`. Receipts: `.ufo/waves/round-89/followup/JDEP3-probes.json`.
Tree at measure: `git status --porcelain --untracked-files=no | wc -l` → `0`; the only untracked entry is the
harness-created `followup/` directory. Two timestamped 60 s wait-checks ran (`04:18:32`, `04:19:40` local);
HEAD stayed `1b09f3f` and no tracked modification appeared, so no evidence gap was left by the wait window.

**Seat question.** Per R10 (delivered at `corpus/knowledge/r88-sourced-inspiration-decision-table.md:24`,
sha256 `9afb6ce9…a4b5f9`): (1) does ANY shared referent exist between `corpus/fixtures/r87-myth-cluster/`
and `corpus/fixtures/r88-m3-maya-cluster/` — entity names, place names, source ids; (2) would the worked
example's format (`corpus/knowledge/r89-cross-cluster-contradiction.md`, sha256 `7f56bdd6…0cb580`) accept a
real entry; (3) is r87's own Hara/Sen pair correctly intra-cluster rather than a register case.

**Scoped depth verdicts (register readiness).**

| sub-axis | verdict | basis |
|---|---|---|
| R10 row + worked-example artifact (format completeness, pointer resolution, cluster scoping) | **improved** | every R10-required field present at record and pair level; all landed-side pointers resolve to the asserted values; both fixtures still replay `CLEAN` alone |
| Register operability (first real cross-cluster entry) | **unprovable-but-better** | no shared referent and no candidate discrepancy exists anywhere in the delivered corpus between the two landed clusters, so the register has no trigger to exercise; the row is prospective by its own closure note |

No axis is harmed: R10 is additive governance (no checker/schema change), and the r87 local contradiction
record is byte-identical to baseline (`14bf96df…74aa4`, unchanged at `51b286b`), so nothing was collapsed,
reconciled, or rewritten by the demo.

## Work performed

- Read the delivered R10 row and the closure note (`r88-sourced-inspiration-decision-table.md:24,32–36`), the
  worked example (`r89-cross-cluster-contradiction.md`), both landed cluster fixture sets in full
  (`entities/sources/timeline/relations/contradictions.json` + README, excerpts, maps, notes), the reference
  ledger, and `corpus/fixtures/check_bible.py`'s scope.
- Ran the R10 comparison on the delivered tree at all three levels it names, plus two extra levels it does not
  name (timeline event ids, relation endpoints/types), and a text-level sweep (capitalized tokens, whole-word
  proper nouns, substring hits).
- Ran a corpus-wide ID-collision sweep over all 160 fixture directories to test whether the R10 comparison, if
  applied unscoped, would produce spurious register candidates.
- Parsed the worked example mechanically against R10's field list and resolved every cited pointer against the
  delivered tree; byte-compared the demo's quoted statements with the delivered `timeline.json` descriptions.
- Ran two control probes in `/tmp/jdep3/` that mutate a copy of the r87 fixture's local contradiction record, to
  prove the pair is resolved (and only resolvable) intra-cluster.
- No tracked file was written; the only repository writes are this report and `JDEP3-probes.json`. No commit, no push.

## Before → after measurements

All commands run from the repository root. `BEFORE` = `git archive 51b286b` extraction in `/tmp/jdep3/base`
(read-only on the repo); `AFTER` = delivered tree at `1b09f3f`.

**1. R10's own three levels — structured ID sets (AFTER).**

```sh
python3 - <<'EOF'
import json,pathlib
A=pathlib.Path('corpus/fixtures/r87-myth-cluster'); B=pathlib.Path('corpus/fixtures/r88-m3-maya-cluster')
for kind,key in [('entities','id'),('sources','id'),('timeline','id')]:
    a={r[key] for r in json.load(open(A/(kind+'.json')))}
    b={r[key] for r in json.load(open(B/(kind+'.json')))}
    print(kind, 'INTERSECTION', sorted(a&b))
EOF
```

Observed:

```
entities INTERSECTION []
sources INTERSECTION []
timeline INTERSECTION []
```

Supporting sets: r87 entities `['ash-dune-sanctuary','hara','mother-tide-gate','reed-bell','reedwardens','sen','shellweavers']`
vs r88-m3 `['aru','evin','quiet-rise','salt-court']`; r87 sources `['dune-register','gate-witness','lowwater-hymn','shell-charter','tide-bell-tally']`
vs r88-m3 `['paired-clock','veil-verse']`; r87 place_ids `['ash-dune-sanctuary','mother-tide-gate']` vs r88-m3
`['quiet-rise','salt-court']`; relation endpoints/types (`allied_with`, `keeps_watch_with`, `records_at`) exist only in r87
(r88-m3 `relations.json` is `[]`).

**2. Entity *names* and text-level referents.**

```sh
grep -rniE '\b(hara|sen|mother-tide-gate|ash-dune|shellweavers|reedwardens|reed-bell)\b' corpus/fixtures/r88-m3-maya-cluster/
grep -rniE '\b(aru|evin|quiet-rise|salt-court|paired-clock|veil-verse|chalk-stair)\b' corpus/fixtures/r87-myth-cluster/
```

Observed: `(no whole-word hara/sen)` for the first; `(none)` for the second. Capitalized-token intersection is
governance vocabulary only (`Source`, `Sourced`, `Rights`, `Round`, `Parallel`, `Symbolism`, `Bell`, `Attribution`,
`Editorial`, `Limit`, `Newly`, `Public`, `Replay`, `Consult`, `AI-training`); no proper noun of either cluster
appears in the other.

Raw `grep -ric` substring counts (`hara`=2, `sen`=3 in r88-m3) are **non-referents**, confirmed by `grep -on`:

```sh
grep -on 'hara' corpus/fixtures/r88-m3-maya-cluster/*
grep -on 'sen'  corpus/fixtures/r88-m3-maya-cluster/*
```

Observed: `hara` only inside `"kind": "character"` (`entities.json:4,16`); `sen` only inside `represent`,
`presentation` (`inspiration-note.md:7,15`) and `sentence` (`symbolism-clause-map.md:3`).

**3. Field-level overlap without a referent (near-miss check).**

Both clusters contain a `bell` object and a `register`-kind source, so the R10 *field* overlaps even though no
referent does: r87 `reed-bell` / `tide-bell-tally` / `dune-register` vs r88-m3 south bell / `paired-clock`
(`"Ninth Bell Paired Clock Register"`). Ticks do not collide either (r87 `[1,2,3]`, r88-m3 `[9]`). This is exactly
the case R10's first test is written to reject ("similar names or wording alone do not establish identity"), and
it is also an intra-cluster near-miss already handled locally: `r88-m3-maya-cluster/README.md:5` calls the two
tick-9 events "an occupied-slot near-miss, not a double-booking". No register entry is warranted in either
direction.

**4. Corpus-wide sweep — the scoping boundary (AFTER).**

```sh
python3 - <<'EOF'   # every fixture dir, ids across entities/sources/timeline
... collects id -> {dirs} for all dirs under corpus/fixtures ...
EOF
```

Observed: 160 fixture dirs scanned; 65 unique entity ids, 32 source ids, 36 timeline ids; 55 ids appear in more
than one directory — **all** of them scaffolding/probe fixtures (`harbor`, `mira`, `seal`, `tower`, `quay`,
`archive-ledger`, `courier-log`, `arrival`, `departure`, `vela`/`tarin`/`sella` families, `ally-*`, `r89-f2-*`,
`r9-*`, `r17/r18/r19/r20/r21/r22-*`). No collision involves `r87-myth-cluster` or `r88-m3-maya-cluster` against
anything. Only two fixture directories carry the cluster signature (`inspiration-note.md` + `symbolism-clause-map.md`):
`corpus/fixtures/r87-myth-cluster/` and `corpus/fixtures/r88-m3-maya-cluster/` (plus the R9 demo
`corpus/fixtures/r89-inspiration-paraphrase/`, which is a support-mode demo, not a second landed cluster).

**5. Format acceptance — mechanical field parse + pointer resolution (AFTER).**

```sh
python3 /tmp/jdep3/accept.py
```

Observed:

```
== record-level R10 fields ==
  'Status': present
  'Relative cluster paths': present
  'Existing local record': present
== pair-level R10 fields (Pair A / Pair B) ==
  Pair A — Hara account versus hypothetical account: missing=none
  Pair B — Sen account versus hypothetical account: missing=none
== pointer resolution (delivered tree) ==
  corpus/fixtures/r87-myth-cluster/contradictions.json#moon-basin-vow-location -> ok: record moon-basin-vow-location present
  corpus/fixtures/r87-myth-cluster/timeline.json#moon-basin-vow-dune-account.place_id -> ok: place_id='ash-dune-sanctuary' source_id='dune-register'
  corpus/fixtures/r87-myth-cluster/timeline.json#moon-basin-vow-gate-account.place_id -> ok: place_id='mother-tide-gate' source_id='gate-witness'
  corpus/fixtures/r89-hypothetical-moon-basin/timeline.json#moon-basin-vow-river-account.place_id -> FILE ABSENT: corpus/fixtures/r89-hypothetical-moon-basin/timeline.json
== relative cluster paths ==
  corpus/fixtures/r87-myth-cluster/: exists
  corpus/fixtures/r89-hypothetical-moon-basin/: ABSENT (declared hypothetical)
```

The two "ABSENT" lines are the demo's own declared hypothetical side (the demo says the path, source, assertion,
and sentence "do not exist in the corpus"). Every R10-required slot has a landed counterpart except that one
substitution point, which a real entry fills with a second landed cluster.

Statement fidelity (byte-equality against the delivered fixture, not paraphrase):

```sh
python3 -c "import json;d={r['id']:r for r in json.load(open('corpus/fixtures/r87-myth-cluster/timeline.json'))};print(d['moon-basin-vow-gate-account']['description'])"
```

Observed: demo Pair A statement == `timeline.json` description → `True`; Pair B → `True`; the demo's asserted
`place_id`/`source_id` pairs (`mother-tide-gate`/`gate-witness`, `ash-dune-sanctuary`/`dune-register`) match the
delivered records exactly.

Register destination and tooling (AFTER):

```sh
ls -l corpus/knowledge/cross-cluster-contradictions.md      # -> No such file or directory
grep -rn "corpus/knowledge" --include=*.py --include=*.sh .  # -> (no matches)
grep -rn "register" corpus/knowledge/seed.md corpus/knowledge/2026-10-12-lore-consistency-checklist.md README.md corpus/README.md  # -> (no matches)
```

Observed: the register file does not exist (consistent with the row's own prospective scoping and the closure
note "R10's register is created on first real cross-cluster conflict"); no code reads `corpus/knowledge`; no
index/checklist/README points at the register destination. The destination is referenced only from the R10 row
and the demo's own scope paragraph.

**6. Cluster replays (AFTER).**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster
```

Observed: both `CLEAN: schema, citations, relations, timeline; 0 violations`, exit `0` — unchanged from BEFORE
(baseline `51b286b` replays identically), so the R10 delivery changed no fixture behaviour.

**7. Hara/Sen intra-cluster controls (scratch, `/tmp/jdep3/`).**

```sh
cp -r corpus/fixtures/r87-myth-cluster /tmp/jdep3/r87-mut   # then set claim_a.event_id to the hypothetical id
python3 corpus/fixtures/check_bible.py /tmp/jdep3/r87-mut
```

Observed: `VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'moon-basin-vow-river-account'`
/ `1 violation(s); no canon changed`, exit `1`. Second control (delivered `timeline.json` `source_id` set to
`reed-arch-register`): `VIOLATION: contradictions[0].claim_a: event 'moon-basin-vow-gate-account' has no resolvable
source_id` + `VIOLATION: timeline[2].source_id: unknown in-world source 'reed-arch-register'`, exit `1`. Control
(both `event_id` and `source_id` left as delivered): the `CLEAN` result above.

### Re-run verification (second JDEP3 dispatch)

A second dispatch of this seat re-ran checks 1–7 on the delivered tree at `1b09f3f` against this report
(sha256 `592887ab…c49482`). The receipt file this report's header cites, `JDEP3-probes.json`, was **absent** at
`04:27–04:32` local (both wait-checks below report `jdep3probes=no`); it has now been written by the re-run
(`.ufo/waves/round-89/followup/JDEP3-probes.json`, full commands + observed outputs). All first-pass results
replicated, on the same tree:

- Referent comparison: `[]` intersection at entities/sources/timeline ids, place ids, and relation tuples
  (r87: 4 edges; r88-m3: `[]`); both whole-word greps `rc=1`; capitalized-token intersection is governance
  vocabulary only; the `hara`/`sen` substring hits are `character`/`represent`/`sentence`.
- Scoping sweep: 160 dirs, 55 ids shared across directories (all scaffolding), cluster-signature dirs exactly
  `['r87-myth-cluster','r88-m3-maya-cluster']`, no shared id involving either.
- Format acceptance + fidelity: all record- and pair-level R10 fields present; every landed pointer resolves;
  both quoted statements strictly byte-equal to `timeline.json`; only the declared-hypothetical path absent.
- Hara/Sen controls (fresh copies, `/tmp/jdep3v/`): foreign `event_id` → `1 violation(s)`, exit `1`; foreign
  `source_id` → `2 violation(s)`, exit `1`; unmutated copy → `CLEAN`, exit `0`.
- Replays + baseline: both clusters `CLEAN`, exit `0`; `git diff --stat 51b286b 1b09f3f -- <cluster dirs>` →
  4 excerpt files, 44 insertions; `contradictions.json` sha `14bf96df…74aa4` identical on both sides.

Wait-checks: `WAIT1 2026-10-17T04:30:22-03:00 HEAD=1b09f3f dirty=1` and `WAIT2 2026-10-17T04:32:27-03:00
HEAD=1b09f3f dirty=1` (followup/ 36 → 44 files; sibling seats still landing). The single tracked working-tree
modification is K1's authorized `l0-questions.md` append (mtime `04:21:16`), not a seat write. No first-pass
claim required correction.

Cross-seat (r89 follow-up artifacts read at integration): JDEP1 replays the same R8–R10 rows and the demo's
landed pointers and agrees on resolution, while naming the row-rendering debt (D1: the R8–R10 block has no
GFM header/delimiter row, so the three rows render as pipe text) and the R10 evidence-cell freshness debt (D2:
the quoted r88 scan predates the r89 demo file) — both owned by that lane, not re-verdict here. JDEP2 classifies
R10 as *uncovered (partial)*: "the no-register-entry answer is covered, the required record is not", which this
seat's F3/P6 read as the demo supplying the record *shape* while the register stays legitimately empty (F1).
JDEP4 rules depth *improved (bounded)*. JCOV1's coverage verdict (r87 14/14 anchors) is the provenance of the
four excerpt files P9 shows added to the r87 cluster; it does not touch the contradiction record (sha unchanged).

## Findings & named debt

**F1 (primary, negative finding). No shared referent exists between `r87-myth-cluster` and `r88-m3-maya-cluster`.**
Zero intersection at entity ids, entity names, place ids, source ids, timeline event ids, and relation
endpoints/types; no whole-word mention of either cluster's proper nouns in the other's files. R10's trigger
requires a shared referent *and* field *and* occasion; with no referent the comparison yields not even a
"candidate discrepancy and missing evidence". The register is therefore correctly empty, and no r89 artifact
falsely asserts a cross-cluster conflict: the demo labels its second side hypothetical and unlanded, and the R10
row's closure note keeps the register prospective. This is a *positive* result for register integrity: nothing
was invented to make the register non-empty.

**F2 (boundary finding, worth recording before the first real entry). The R10 comparison must be scoped to landed
story clusters, not to fixture directories.** An unscoped sweep finds 55 ids shared across fixture dirs, all of
them scaffolding (`harbor`, `mira`, `seal`, `tower`, `archive-ledger`, `courier-log`, `vela`/`tarin`/`sella`, …).
Applying R10 naively at corpus scale would manufacture spurious register candidates from shared probe vocabulary.
The discriminating signature is the cluster artifact set (`inspiration-note.md` + `symbolism-clause-map.md` +
its own `sources.json`), which currently matches exactly the two clusters this seat compared. The row does not
state this scoping rule.

**F3 (format acceptance). The worked example's format accepts a real entry; verified mechanically, with two
limits.** Every R10-required field is present at record level (stable ID, both relative cluster paths, status) and
at pair level (conflicting assertions with file+id+field pointers, cited in-world `source_id`s, why-they-cannot-both-
be-true, status `unresolved`); all landed-side pointers resolve to the asserted values; the quoted statements are
byte-identical to the delivered fixture. The two limits: (i) the two-landed-side path is *unexercised* — the demo's
second side is intentionally absent, and F1 shows no real pair exists to exercise it; (ii) the register destination
`corpus/knowledge/cross-cluster-contradictions.md` does not exist, so the first real entry must create the file, and
nothing in the tree defines a header, multi-entry ordering, or ID-uniqueness convention for it (the demo gives one
record shape only). Both limits are consistent with the row's stated prospective scoping; neither is a defect in the
delivered artifact.

**F4 (Hara/Sen is correctly intra-cluster, not a register case).** Both disputed events (`moon-basin-vow-gate-account`,
`moon-basin-vow-dune-account`) live in r87's own `timeline.json`; both cited sources (`gate-witness`, `dune-register`)
live in r87's own `sources.json`; the local record `contradictions.json#moon-basin-vow-location` is validated by the
checker inside that single directory (controls above: a foreign event id or a foreign source id turns the same run
into `1`–`2` violations, exit `1`). The demo therefore links it as an *existing local record* without copying its
pointers into the register — which is what R10 requires ("Keep `contradictions.json` for references the local fixture
checker can resolve; do not represent a foreign-cluster pointer as locally validated"). No promotion to the
cross-cluster register is warranted, and none was made.

**Named debt (register readiness).**
- *Register discoverability.* The register destination is named only inside the R10 row and the demo; no index,
  checklist, README, or `seed.md` line points at it (`grep -rn "register"` over `seed.md`, the consistency checklist,
  `README.md`, `corpus/README.md` → no matches). A future entry would be discoverable only by reading the R10 row.
- *Register file/format.* No `corpus/knowledge/cross-cluster-contradictions.md` exists; no header, ordering, or ID
  convention is defined for it, and no tooling reads `corpus/knowledge` (grep over `*.py`/`*.sh` → no matches), so
  acceptance remains a manual gate exactly as the row states.
- *Scoping rule unstated* (F2): add the cluster-signature scoping to the row or to the register header when the
  register is created.
- *Adjacent, outside this seat's verdict:* in the delivered `reference-ledger.md` the Spence row sits **after** the
  ledger's closing paragraph ("These citations record real-world references, not fictional canon…"), splitting the
  table from its own summary. Present already at `51b286b` (r88 closure); r89 changed only the ETCSL `Use here` cell
  (`git diff 51b286b 1b09f3f -- corpus/knowledge/reference-ledger.md` shows one line). Flagged for the C2/C7 ledger
  lane, not counted against depth here.

## Handoff

- **Answers.** (1) No shared referent of any kind between the r87 myth cluster and the r88 M3 Maya cluster — a clean
  negative, with the near-miss (both have a bell/register/tick field vocabulary) correctly filtered by R10's
  referent test. (2) The worked example's format would accept a real entry: all R10 fields present and every landed
  pointer resolving; the only unexercised path is the second landed side, and the register file itself is still
  absent by design. (3) r87's Hara/Sen pair is correctly intra-cluster — both events and both sources resolve inside
  `r87-myth-cluster/`, and the checker validates the local record there (control probes confirm it rejects a foreign
  pointer), so it is not a register case and must not be promoted.
- **Verdicts.** Register-readiness artifact: **improved**; register operability: **unprovable-but-better**; no axis
  harmed (R10 is additive; r87 local records byte-identical to baseline).
- **Files written:** `.ufo/waves/round-89/followup/JDEP3.md`, `.ufo/waves/round-89/followup/JDEP3-probes.json`.
  Scratch only under `/tmp/jdep3/`. No tracked file touched, no commit, no push.
- **For the integrator.** Fold F1 as the register's trigger-state evidence (empty register is correct, not
  overlooked). F2's scoping rule and F3's two format limits are the concrete items to record when the register is
  first created. JDEP1 (same wave) already replayed the R10 row's cited commands and the demo's pointers; my F1/F3
  results are independent of that and agree with it on pointer resolution.
- **Gaps.** No gap from the wait window (HEAD constant, no tracked writes). Unresolved by construction: no real
  cross-cluster conflict exists in the corpus, so no runnable end-to-end register-append receipt can be produced
  this round.
