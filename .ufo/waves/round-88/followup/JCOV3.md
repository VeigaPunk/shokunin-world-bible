# JCOV3 — Coverage judge #3 (branch-exercise auditor)

Subject: `corpus/fixtures/r88-m3-maya-cluster` on the DELIVERED tree, HEAD `2ea9ef1`
(baseline `dfd1fbc`). `git status --porcelain` was empty at probe time; checker
`corpus/fixtures/check_bible.py` sha256 `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`;
per-file cluster hashes and every raw probe output are in `followup/JCOV3-probes.json`.

## Work performed

- Read the delivered cluster and the delivered checker, then enumerated which
  structural elements the artifact actually carries. Result: `relations.json` = `[]`,
  `contradictions.json` = `[]`, both timeline events have `depends_on: []`, there are
  no faction entities and no `provenance` blocks. **Three of the four branch families
  named in my seat block (reciprocal alliance, `depends_on` inversion, contradiction
  path) are absent from this artifact**, so for those the block's requested mutation
  ("drop one direction") has no direction to drop. I probed them for *reachability*
  and recorded where their real coverage lives (below) instead of inventing elements.
- Ran 14 probe runs (1 positive + 13 mutations) under `/tmp/jcov3-r88`, each mutation
  applied to a fresh copy of the delivered directory; the repo was never written by any
  probe. Script: `/tmp/jcov3-r88/consolidate.py` (writes only `followup/JCOV3-probes.json`).
- Ran a static coverage scan over all 149 fixture directories to locate the absent
  branches' corpus-level coverage.
- Independently corroborated the citation layer against live source text: fetched
  `https://www.gutenberg.org/files/53080/53080-h/53080-h.htm` (curl exit 0, 1,035,633
  bytes) and checked the quoted sentences, chapter/section labels, and the printed-page
  marker bracketing myself.
- Mechanically re-checked the clause→element index of **both** clusters (r88 and the
  r87 excerpt M4 repaired).

## Before → after measurements

Invocation for every probe: `python3 corpus/fixtures/check_bible.py <copy>` with cwd =
repo root (the delivered `README.md` replay line, `python3 corpus/fixtures/check_bible.py
corpus/fixtures/r88-m3-maya-cluster`, also exits 0).

**Positive path (delivered artifact, unmutated).** `base-unmutated` → `CLEAN: schema,
citations, relations, timeline; 0 violations`, exit 0. Same command on
`corpus/fixtures/r87-myth-cluster` → identical CLEAN, exit 0 (C2's "both clusters exit 0"
holds). Baseline `dfd1fbc` had one cluster; the after-state has two, both clean.

**Fire/pass probe matrix** (each row = one fresh copy; observed output verbatim):

| Probe | Mutation | Intended branch | exit | observed |
|---|---|---|---|---|
| p-f1a-ally-one-way | +2 faction entities, 1 `allied_with` edge | reciprocal alliance | 1 | `relations[0]: allied_with faction relation 'lantern-wardens' -> 'salt-wardens' lacks a sourced reciprocal relation` |
| p-f1b-ally-reciprocal | +reverse edge | reciprocal alliance (pass) | 0 | CLEAN |
| p-f2a-collide-other-place | `timeline[1].entity_id := 'aru'` | occupied slot | 1 | `timeline[1]: double-booked 'aru' at tick 9 in timeline[0] ('quiet-rise') and 'salt-court'` |
| p-f2b-collide-same-place | `entity_id := 'aru'` **and** `place_id := 'quiet-rise'` | same slot, same place (pass) | 0 | CLEAN |
| p-f2c-same-place-distinct-actor | `timeline[1].place_id := 'quiet-rise'` | control: same place, distinct slot | 0 | CLEAN |
| p-f3a-dep-inversion | `timeline[0].depends_on := ['evin-ninth-bell']` | `depends_on` inversion | 1 | `timeline[0].depends_on: timeline inversion 'evin-ninth-bell' tick 9 not before 'aru-ninth-bell' tick 9` |
| p-f3b-dep-forward | + earlier event at tick 5, forward edge | dependency order (pass) | 0 | CLEAN |
| p-f4a-contra-unresolved | ledger row with `claim_b.event_id := 'no-such-event'` | contradiction event resolution | 1 | `contradictions[0].claim_b.event_id: expected exactly one timeline event 'no-such-event'` |
| p-f4b-contra-resolvable | ledger row with both events resolvable | contradiction resolution (pass) | 0 | CLEAN |
| p-f5-unknown-source | `entities[0].claims[0].source_id := 'no-such-source'` | source membership | 1 | `entities[0].claims[0].source_id: unknown in-world source 'no-such-source'` |
| p-f6-place-kind | `quiet-rise.kind := 'item'` | place comparability | 1 | `timeline[0].place_id: not a place 'quiet-rise'` |
| p-f7-dangling-place | `timeline[0].place_id := 'no-such-place'` | dangling entity | 1 | `timeline[0].place_id: dangling entity 'no-such-place'` |
| p-f8-ambiguous-actor | + duplicate entity id `aru` | ambiguous identity | 1 | `entities[4].id: duplicate entities id 'aru'` **and** `timeline[0].entity_id: ambiguous actor entity 'aru'` |

Every mutation fired **exactly** its own branch's template; no probe produced a
collateral template except p-f8, where the duplicate id is the direct cause of both
findings. The clean cluster stayed CLEAN through all 14 runs.

**Citation layer, checked against the live source text** (`/tmp/jcov3-r88/gutenberg-53080.htm`):

- quoted sentence `He called out “Earth,” and the solid land appeared.` → present at
  index 384339; `The beginning of this interesting book is taken up with the Kiche story
  of the creation` → present at 384089.
- page marker bracketing: nearest marker before the passage = `[209]` (383477), nearest
  after = `[210]` (385208) → the delivered locator "printed p. 209" is independently correct.
- labels: `CHAPTER V: MYTHS OF THE MAYA` (the excerpt's "Chapter V, 'The Maya'" is a
  slightly loose rendering of the heading, but the subsection `The Creation-Story` is
  verbatim); `Gutenberg eBook 53080` and the `53080-h.htm` URL both present in the
  excerpt and the note.
- clause→element index vs delivered excerpt: **2/2** clause rows resolve after
  quote-glyph normalization, **1/2** byte-exact (see debt D2).
- r87 `lowwater-hymn-excerpt.md` vs its clause map: **8/8** real clause rows byte-exact,
  independently corroborating C2's "8/8 clause matches".

**Corpus scan (149 fixture dirs).** Same-slot-same-place pair (the double-booking rule's
pass path): 4 fixtures (`r21-same-place`, `r37-ledger-ambiguous`, `r59-duplicate-tower-harbor`,
`r62-duplicate`); none of the four emits a `double-booked` finding, so the pass path is
genuinely exercised there (`r59-*` fails to load its timeline, so it does not reach it).
Same-slot-different-place (fire path): 37 fixtures. `allied_with` relations: 6 fixtures
(`ally-one-way` fires, `ally-reciprocal` passes, `r61-allied-*` gate on index availability,
`r7-ally-reverse-ambiguous`, `r87-myth-cluster`). Fixtures with ≥1 contradiction row: 27.
Fixtures with zero dependency edges: 50 of 149. Reference runs: `r20-valid-inversion`
fires the inversion template, `r22-valid-order` exits 0.

## Findings & named debt

**Verdict recommendation — coverage: improved (bounded).** A second sourced cluster now
exists, both clusters exit 0, and every element the artifact *does* carry is
load-bearing: each was shown to fire exactly its own template under a targeted mutation
while the unmutated cluster stayed CLEAN. The bound is the same as r87's JCOV3 bound —
this is a positive-path surface and it adds no new finding template — plus the two
precisions below.

**D1 (main finding): the advertised "occupied-slot near-miss" is not a near-miss of the
slot.** `r88-m3-maya-cluster/README.md` states "The two register events both occur at
tick 9, but have distinct actors and distinct places: this is an occupied-slot
near-miss, not a double-booking." The occupancy key is `(entity_id, tick)`, and the
delivered keys are `('aru', 9)` and `('evin', 9)` — **distinct**. The branch's
discriminating condition (`slot in occupied and occupied[slot][1] != row['place_id']`) is
therefore never evaluated by the cluster; its second event takes the `else` insert path
like any unrelated slot. The pair's tick equality is not what keeps it clean — the actor
and place distinctness are. M3's own receipt ("near-miss assertion output: `[(9, 'aru',
'quiet-rise'), (9, 'evin', 'salt-court')]`") tests tick/entity/place distinctness, not
the branch condition, so it does not close this gap either. The genuine same-slot
near-miss (same actor, same tick, same place) is covered by other fixtures, so **this is
claim precision, not a coverage loss**: either reword to "same-tick, distinct-slot pair",
or make the pair share a slot and a place (which would duplicate `r21-same-place` /
`r37-ledger-ambiguous` / `r62-duplicate`).

**D2: one clause-map row is not byte-exact against the delivered excerpt.**
`symbolism-clause-map.md` row 1 writes `“He called out ‘Earth,’”` (single curly quotes)
where both `source-excerpt.md` and the live Gutenberg text have `“Earth,”` (double
quotes). Consequence: the "every attributed claim mechanically resolvable in the
delivered excerpt" test passes only after quote-glyph normalization (2/2 normalized,
1/2 exact). One-glyph fix in the clause map; meaning is unaffected.

**D3: three branch families have no exercise in this cluster.**
`relations.json` = `[]` (no factions at all → reciprocal alliance untested here),
`depends_on` edges = 0 (inversion untested here), `contradictions.json` = `[]`
(contradiction path untested here). My p-f1/p-f3/p-f4 probes show all three branches are
live and reachable, and their real coverage sits in the fixtures named above. The wave
should therefore not read "second cluster" as "same structural surface as r87's": r87's
cluster carries the reciprocal-alliance edge and a reported-not-resolved contradiction;
this one carries neither.

**D4: index debt still open.** `corpus/fixtures/README.md`'s highest section is
`## Round 83`; there is no Round 87 or Round 88 section registering either cluster (or
the C1 fixtures). This is exactly the debt r87's JCOV3 carried forward; it is unresolved
at `2ea9ef1`.

**Positive-path inventory (what the cluster really exercises, for the record):** three
availability flags set true (`sources`/`entities`/`timeline` load as arrays); 4 entity
claims + 2 event citations resolved through the source index (0 relation rows → that call
site is untested); the entity-kind whitelist over `character`/`place`; place-kind
comparability on both events (which is what lets the occupancy branch run at all); the
occupancy insert path twice; the present-but-empty ledger path; the empty dependency-list
path. No `provenance` block, so the entire C1 provenance surface is untouched by this
cluster.

**Not this seat's to fix:** C1's stop-cause deltas (JCAL* lanes) and the r87 OBS-1
excerpt content are outside my subject; I only re-ran the r87 clause map mechanically.

## Handoff

- Deliverables: `followup/JCOV3.md` (this file) and `followup/JCOV3-probes.json`
  (14 probe records with exit codes, verbatim output, checker + cluster hashes, corpus
  scan counts, and the delivered structure inventory). No other repo writes; no commit,
  no push. The `l0-questions.md` modification visible in `git status` at probe time is
  K1's authorized append, not mine.
- Reproduction: `python3 /tmp/jcov3-r88/consolidate.py` regenerates every receipt
  (it copies the cluster to `/tmp/jcov3-r88/<probe>` and writes the JSON into
  `followup/`); `/tmp/jcov3-r88/probe.py` is the earlier variant. All scratch is under
  `/tmp`; deleting `/tmp/jcov3-r88` loses nothing that is not recorded in the JSON.
- Gaps for the parent: (a) my seat block specified no 60-second wait-check, and none was
  needed — all judging inputs existed at `2ea9ef1`; (b) I did not need any sibling
  seat's verdict, so no dependency gap affects this report; (c) the four branch families
  were probed against the delivered checker only — I did not compare against any
  scratch patch, so no patch-vs-delivered drift is claimed here.
- Suggested follow-ups, in cost order: fix D2 (one glyph), decide D1 (reword the README
  sentence or change the pair), open the Round 87/88 section in
  `corpus/fixtures/README.md` (D4), and record in the round's coverage claim that the
  second cluster deliberately omits the reciprocal-alliance, dependency, and
  contradiction surfaces (D3).
