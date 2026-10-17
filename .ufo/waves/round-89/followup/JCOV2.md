# JCOV2 — Coverage judge #2 (excerpt discipline + ledger), round 89

Subject: the DELIVERED tree at `1b09f3f` (baseline `51b286b`), tracked tree clean.
Scope: C2's excerpt-discipline surface — (a) no excerpt anchor negates another
fact, with the T3/T4 vow contradiction preserved unresolved; (b) the four new
in-world excerpts (plus the pre-existing hymn) assert no canon beyond cited
facts; (c) the ETCSL ledger row: external-only marker present, three questions
still separate, table shape 4-column, prior rows unaltered.

Every measurement below was re-run by this seat on the delivered tree. No M4/M5
wave receipt is reused as evidence; M4's mapping was consulted only after my own
anchor sweep had been derived from the delivered excerpt text.

## Work performed

- Axes named: (1) **excerpt↔fact consistency** (R5/D1 support rule: no anchor
  negates another fact; contradiction left unresolved); (2) **excerpt scope**
  (delivered in-world text must not assert canon beyond its cited facts);
  (3) **ledger contract** (delivery-status marker, three separate questions,
  4-column shape, prior rows byte-identical).
- Read on the delivered tree: the four new excerpts
  (`gate-witness`, `dune-register`, `shell-charter`, `tide-bell-tally`), the
  pre-existing `lowwater-hymn-excerpt.md` and `symbolism-clause-map.md`,
  `r87-myth-cluster/{entities,relations,timeline,contradictions,sources}.json`
  and its `README.md` + `inspiration-note.md`,
  `corpus/knowledge/reference-ledger.md`, the R5/R8/R9/R10 rows of
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md`,
  `corpus/knowledge/r89-cross-cluster-contradiction.md`, and the R9 demo fixture
  `corpus/fixtures/r89-inspiration-paraphrase/`.
- Probes: (i) independent 22-fact anchor sweep with anchors derived by me from
  the delivered excerpt text; (ii) same-predicate/different-object pair scan
  over excerpt assertions vs `contradictions.json`; (iii) line-level content
  inventory of all five excerpts; (iv) ledger shape/identity probes against
  both revisions; (v) checker replays; (vi) `external-only` corpus-wide grep.
- Scratch: none needed (all probes read-only). Repository writes by this seat:
  this file only. No commit, no push.
- Two timed 60-second dependency checks were run (log
  `/tmp/lore-r89-jcov2-wait.log`); the delivered tree hash was stable and no
  dependency artifact was missing, so judging proceeded on the delivered tree.

## Before → after measurements

Tree state at probe time:

```sh
git log --oneline -3 && git status --porcelain
```

```text
1b09f3f lore r89: C1 cause-branch fixtures + multi-cause summary + FN-1/2, C2 r87 support completion, C3 R8-R10 governance — work wave (32 luna-max seats)
51b286b lore r88: closure — verdicts ruled (calibration/coverage/depth improved, bounded), documentation-parity repair, round record
2ea9ef1 lore r88: C1 stop-cause repair + C2 Maya cluster + C3 inspiration table — work wave (37 luna-max seats)
(no porcelain output — tracked tree clean)
```

Pinned hashes (delivered tree): checker `corpus/fixtures/check_bible.py`
`e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`;
`reference-ledger.md` `7ffab17dd9fee76af87ccd489012910e6d6fc6e575384d2fd9049177385f46d6`;
excerpts `gate-witness` `d490e2c2…`, `dune-register` `bddefccc…`, `shell-charter`
`9ebedb8d…`, `tide-bell-tally` `991c5337…`, `lowwater-hymn` `b0bf4236…`.

**Fact inventory (before the anchors).** Command: python3 heredoc enumerating
`first_appearance` pointers + entity claims + relation edges + timeline events.
Observed:

```text
sources: ['dune-register', 'gate-witness', 'lowwater-hymn', 'shell-charter', 'tide-bell-tally']
excerpts: ['dune-register', 'gate-witness', 'lowwater-hymn', 'shell-charter', 'tide-bell-tally']
FACT COUNT: 22
UNRESOLVED SOURCES: []
NO DELIVERED EXCERPT: []
```

**Anchor sweep (my own anchors, `grep -nF` per fact).** Observed (22 lines,
abridged to the first hit per fact):

```text
ent[0].first_appearance    src=gate-witness    MATCH  5:> I am Hara, keeper of the Mother-Tide Gate.
ent[1].claims[0]           src=dune-register   MATCH  5:> I, Sen, serve as recorder at Ash-Dune Sanctuary.
ent[2].claims[0]           src=lowwater-hymn   MATCH  3:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
ent[3].claims[0]           src=dune-register   MATCH  6:> Place of keeping: Ash-Dune Sanctuary is a record-keeping place.
ent[4].claims[0]           src=shell-charter   MATCH  7:> Shellweavers signed this charter as a signatory faction.
ent[5].claims[0]           src=shell-charter   MATCH  8:> Reedwardens signed this charter as a signatory faction.
ent[6].claims[0]           src=tide-bell-tally MATCH  9:| 1 | We carried the Reed Bell for the low-water signal. |
rel[0]                     src=shell-charter   MATCH  9:> By this charter, Shellweavers stand allied with Reedwardens.
rel[1]                     src=shell-charter   MATCH 10:> By this charter, Reedwardens stand allied with Shellweavers.
rel[2]                     src=shell-charter   MATCH 11:> Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.
rel[3]                     src=dune-register   MATCH  7:> At Ash-Dune Sanctuary, Sen kept the register.
tl[0]                      src=gate-witness    MATCH  6:> I sounded the Reed Bell at the Mother-Tide Gate before the Moon-Basin Vow, at the first low-water bell.
tl[1]                      src=tide-bell-tally MATCH 10:| 2 | At Ash-Dune Sanctuary, Sen's tally records the return of the first low-water signal before the Moon-Basin Vow. |
tl[2]                      src=gate-witness    MATCH  7:> I record the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.
tl[3]                      src=dune-register   MATCH  8:> I record that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.

ANCHOR PASS: 22/22
FAILURES: []
```

(All 22 lines were printed; the seven `first_appearance` pointers and remaining
claim rows also matched. Two pointers share their excerpt line with the entity's
own claim — `ent[0]`/`ent[0].claims[0]` both hit line 5 — which is expected.)

**Negation-pair scan (a).** Command: pair every excerpt assertion on
`(subject, predicate, object)` and report same-predicate/different-object pairs;
compare with `contradictions.json`. Observed:

```text
incompatible same-predicate pairs among excerpt assertions: [(('gate-witness', 'vow place', 'mother-tide-gate'), ('dune-register', 'vow place', 'ash-dune-sanctuary'))]
recorded in contradictions.json: ['moon-basin-vow-location']
```

Exactly one incompatible pair exists among the delivered excerpt assertions, and
it is precisely the recorded contradiction. Its two surfaces are unchanged from
baseline (`git diff --name-only 51b286b..1b09f3f -- README.md contradictions.json
inspiration-note.md symbolism-clause-map.md` → no output):

- prose: `corpus/fixtures/r87-myth-cluster/README.md:5` — "**The contradiction is reported, not resolved.**"; the checker "does not judge source truth or select canon".
- JSON: `corpus/fixtures/r87-myth-cluster/contradictions.json:12` — "The disagreement is reported and left unresolved; the checker validates references, not source truth or canon."
- the new r89 R10 demo does not resolve it: `corpus/knowledge/r89-cross-cluster-contradiction.md:32` — "Keep all three claims distinct and unresolved, and do not select a canonical location."

Neither excerpt declares the other account false; both assert the same single vow
(`gate-witness-excerpt.md:7` "the single Moon-Basin Vow"; `dune-register-excerpt.md:8`
"that same single Moon-Basin Vow"), which entrenches the shared referent without
picking a side. The only negations present in the five excerpts are the hymn's own
imagery (`lowwater-hymn-excerpt.md:4` "The bowl keeps no name, and no voice owns the
tide" — bounded by `symbolism-clause-map.md`) and two meta footers
(`lowwater-hymn-excerpt.md:7`, `shell-charter-excerpt.md:13`); neither touches a fact.

**Line-level content inventory (b).** Every content line of the five excerpts maps
to a cited fact or is explicitly framing/meta:

```text
gate-witness L5→ent[0].claims[0]  L6→tl[0]  L7→tl[2]              (L9 meta footer)
dune-register L5→ent[1].claims[0] L6→ent[3].claims[0] L7→rel[3] L8→tl[3] (L10 meta)
shell-charter L5=NO JSON FACT (framing) L7→ent[4] L8→ent[5] L9→rel[0] L10→rel[1] L11→rel[2] (L13 meta)
tide-bell-tally L5=NO JSON FACT (tally hand) L9→ent[6].claims[0] L10→tl[1] (L12 meta)
lowwater-hymn L3→ent[2].claims[0] L4,L5=verse (bounded by symbolism-clause-map.md) (L7 meta)
```

**Ledger probes (c).** Shape + marker, on the delivered file:

```text
pipe_rows: 7 col_counts: [4, 4, 4, 4, 4, 4, 4]
header: | Work / attribution | Rights question | AI-training permission question | Use here |
ETCSL rows: 1
marker_present: True
attrib_has_url: True   rights_open: True   training_open: True
```

Cell-level identity baseline→delivered (my own probe, not M5's):

```text
baseline rows: 7 delivered rows: 7
cell0: identical=True  delivered_len=217
cell1: identical=True  delivered_len=226
cell2: identical=True  delivered_len=124
cell3: identical=False  delivered_len=321
use_cell_superset_of_baseline: True
prior_rows_identical: True
```

File-level diff — exactly one line changed in the whole file:

```sh
git diff 51b286b..1b09f3f -- corpus/knowledge/reference-ledger.md
```

```text
@@ -5,7 +5,7 @@
 | W3C, *PROV-O: The PROV Ontology*, … |
 | JSON Schema authors, *JSON Schema Validation, Draft 2020-12*, … |
 | Python Software Foundation, *graphlib …* |
-| University of Oxford, … lines 122–163 | … | … | Motif-level comparison only: lines 122–163 describe entry through seven gates and removal of dress and regalia; the fixture uses original shore-threshold imagery. Not an in-world source or canon. |
+| University of Oxford, … lines 122–163 | … | … | external-only / text not delivered at lore; citation is a research lead with verified line locators, not delivered support. Motif-level comparison only: … Not an in-world source or canon. |
```

**Checker replays (delivered tree).** Observed:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

## Findings & named debt

**Verdict recommendation — coverage (excerpt discipline + ledger sub-scope):
improved (bounded).** On the delivered tree the r87 cluster moves from 8/22
anchor-supported facts at `51b286b` to 22/22 by my own sweep, the ETCSL citation
now carries an explicit delivery-status marker, and every one of the three
ledger questions is preserved untouched. No other axis is harmed: cluster JSON,
`contradictions.json`, `README.md`, `inspiration-note.md` and the clause map are
byte-identical to baseline, the checker stays `CLEAN`, and prior ledger rows are
byte-identical. The bound is the debt below (R8's element-side marker, the marker
literal, the R9 mode declaration, the undefined relation type, and two
completeness gaps).

- **(a) PASS.** One and only one incompatible same-predicate pair exists among the
  excerpt assertions and it is the recorded `moon-basin-vow-location`
  contradiction, preserved unresolved in both prose and JSON; no excerpt anchor
  negates another fact. The contradiction's surfaces are unchanged from baseline.
- **(b) PASS, bounded.** Every content line of the four new excerpts maps to a
  cited fact or is framing/meta. Three lines carry in-world detail the JSON does
  not extract as a fact — `shell-charter-excerpt.md:5` ("By the seal of both
  shores, these terms stand:"), `tide-bell-tally-excerpt.md:5` ("Tally hand:
  Sen"), and `lowwater-hymn-excerpt.md:4–5` (bounded by
  `symbolism-clause-map.md`). None contradicts a JSON fact; the first two are
  unbounded by any delivered map. Low severity, worth naming: source text is now
  richer than the canon surface, so a future extraction pass should re-scan these
  lines rather than assume the JSON is complete.
- **(c) PASS.** Marker present; ETCSL cells 0–2 byte-identical to baseline (three
  questions still separate); all seven pipe rows 4-column; prior rows
  byte-identical; exactly one line changed in the file.

**Named debt.**

1. **R8's element-side marker is absent (new finding).** R8 requires the affected
   element be marked "in the note/map `external-only / unverified inspiration`"
   and the ledger `Use here` to state the text is not delivered. Only the
   ledger-side half landed. Command and observed output:

   ```sh
   grep -rn "external-only" corpus/
   ```

   ```text
   corpus/knowledge/r88-sourced-inspiration-decision-table.md:15, :17, :22   (rule text)
   corpus/knowledge/reference-ledger.md:8                                      (ETCSL row)
   ```

   `corpus/fixtures/r87-myth-cluster/inspiration-note.md` and
   `symbolism-clause-map.md` contain no `external-only` string, though R8's own
   evidence cell points at exactly this r87 element. Fix: add the marker to the
   note (one line) or record why the r87 note is out of R8's retroactive scope.
2. **Marker literal diverges from the decision table's token.** The row reads
   `external-only / text not delivered at lore` (+ "with verified line locators"),
   while the passage-specific row asks for `external-only / unverified`. The
   "verified" wording is not fabricated — locator receipts are tracked in-tree
   (`.ufo/waves/round-87/C7.md:73`, `.ufo/waves/round-87/followup/JDEP2.md:49`,
   `.ufo/waves/round-88/followup/JDEP2.md`) — but the prescribed literal token is
   still absent. Meaning is correct; low severity. (Converges with JCOV4's D4.)
3. **`keeps_watch_with` is an undefined relation type.** It occurs exactly once in
   the corpus (`corpus/fixtures/r87-myth-cluster/relations.json:17`) and the
   checker validates `type` only as a non-empty string
   (`corpus/fixtures/check_bible.py:28`); only `allied_with` has semantics
   (`:354-372`). Its pledge/performance boundary lives only in prose
   (`shell-charter-excerpt.md:13`, `sources.json` reliability note). The excerpt is
   *more* careful than the JSON, so this is not a negation — but a reader of
   `relations.json` alone reads a watch state with no gloss. Fix: gloss
   non-`allied_with` types in `corpus/fixtures/README.md`, or carry the pledge
   qualifier in the record.
4. **No R9 delivery-mode declaration for the four new excerpts.** The r87 cluster
   has no claim-to-excerpt map, so no excerpt declares `verbatim` / `translation` /
   `paraphrase` / `summary`. The delivered integration note scopes R9 "from r89
   onward" and defers r87/r88 to "their next content touch" — but r89 *is* a content
   touch of that cluster, so the exemption does not cleanly cover the four new
   files. (Independently found by JCOV4 as D2; my sweep confirms the absence.)
5. **The ledger table is split by prose (my own finding).** Lines 3–8 are the table
   (header, separator, three method rows, ETCSL row); line 9 is blank, lines 10–12
   are the "These citations record…" paragraph, and line 13 is the Spence row with
   no delimiter row before it — so the Spence row renders as paragraph text, not a
   table row. The numeric 4-column check passes (7 pipe rows, all 4 cells) and
   therefore masks this. Pre-existing and byte-identical at `51b286b`; r89 neither
   caused nor repaired it. Fix at the next ledger touch: move the paragraph below
   the Spence row.
6. **The R9 demo map dispositions 1 of its bible's 2 support-rule facts.** The D1
   support rule's SCOPE covers "entity claims **and first-appearance pointers**".
   `r89-inspiration-paraphrase/` has two such facts — `entities.json#/0/first_appearance`
   (`west-stair` → `ash-ledger`) and `entities.json#/0/claims/0` — but
   `claim-to-excerpt-map.md` has one row (the claim). R9 itself is claim-scoped, so
   the demo still demonstrates its message; this is a completeness gap for a
   fixture whose purpose is to show the rule's full surface.
7. **Anchor evidence is not recorded in the corpus (agrees with JCOV4 D1).** My
   22/22 sweep is reproducible from the delivered tree alone (I derived the anchors
   from the delivered excerpt text, not from M4's JSON), but the *mapping record*
   exists only in `.ufo/waves/round-89/patches/M4-verify.json`. Bounded: the R5 row
   asks for the map, and no in-corpus map was delivered.

## Handoff

- **Verdict recommendation for the round record:** coverage — **improved
  (bounded)**, on the strength of (a) 22/22 anchors verified on the delivered tree
  by an independent sweep, (b) the sole incompatible excerpt pair being the
  recorded contradiction left unresolved in prose + JSON, (c) the ETCSL ledger row
  carrying the delivery-status marker with cells 0–2 and all prior rows
  byte-identical to `51b286b`.
- **Files this seat wrote:** `.ufo/waves/round-89/followup/JCOV2.md` only. No
  tracked file was modified; no commit or push was made. Sibling repositories were
  read-only (not touched this seat).
- **For the integrator:** the cheapest high-value repairs are debt 1 (one marker
  line in `inspiration-note.md`) and debt 5 (move the ledger paragraph below the
  Spence row). Debt 4 needs an explicit decision — either add a delivery-mode line
  to the four excerpts or state in the decision table why the r89 touch of the r87
  cluster is exempt.
- **Left undone / not this seat's lane:** the R9 demo and R10 record conformance
  audit (JCOV3), C1 calibration deltas (B/JCOV1 seats), and the fixture-index /
  documentation-parity debt (`corpus/fixtures/README.md` has no Round 89 section,
  so a README-only reader cannot discover the four new support excerpts).

## Re-verification addendum (second dispatch of seat JCOV2)

This seat was re-dispatched with the same mission after the report above had already been delivered (file mtime `2026-10-17 04:20:42 -0300`) and cited by the wave's integration artifacts (`JAXIS.md:191`; `JAXIS-verdicts.json:47`; `P1-measurements.json:76`; `Q1-r89-debt.json:43`). The second run re-executed every receipt above against the delivered tree; all numbers reproduced, no finding changed, and the verdict recommendation stands. Nothing above this line was edited, so debt numbering (`#1`–`#7`) and line references (e.g. `JDEP1.md:212` → `JCOV2.md:263`) remain valid. Repo writes by this run: this addendum only. Scratch: `/tmp/lore-r89-jcov2-probe.py` / `.out`, `/tmp/lore-r89-jcov2-grepanchors.out`, `/tmp/lore-r89-jcov2-wait.log`.

**Tree state + wait-checks.** `git rev-parse HEAD` → `1b09f3ff8016b26a2259e086f673d0112f4f54e5`, stable across both timed 60s checks. `git status --porcelain` at probe time: `M l0-questions.md` (K1's authorized round-89 append, uncommitted — the clean-tree line in the main body predates it) and `?? .ufo/waves/round-89/followup/`. The judged files equal their committed blobs: `git diff --stat 1b09f3f -- corpus/fixtures/r87-myth-cluster corpus/knowledge/reference-ledger.md` → empty.

**Anchor sweep (own table, fixed-string).** `ANCHOR PASS: 22/22`; the C2 subset (6 entity claims + 4 relations + 4 timeline from the four new excerpts) `14/14`; pointer failures `[]`. Lines: E1 gate:5, E2 dune:5, E3 hymn:3, E4 dune:6, E5 shell:7, E6 shell:8, E7 tally:9; R1 shell:9, R2 shell:10, R3 shell:11, R4 dune:7; T1 gate:6, T2 tally:10, T3 gate:7, T4 dune:8. Baseline `git ls-tree 51b286b -- corpus/fixtures/r87-myth-cluster/` holds only `lowwater-hymn-excerpt.md` (0/14 new anchors). Corroboration: JCOV1 (14/14; pointers 1/7→7/7; 8→22 under the anchor rule), JCOV4 (`delivered_fixed_string_anchors=14/14`), JDEP4 (`anchors: OK=14 FAIL=0`), P4 (22/22; baseline 8/22). Carried caution (JCOV1-D1; P4): `M4-verify.json`'s own command prints `facts=22 OK=8 not-OK=14`; the wave's 22 is a composed number, valid only via per-fact anchors.

**Negation scan.** Exactly one same-predicate/different-object pair — `(gate-witness, vow place, mother-tide-gate)` × `(dune-register, vow place, ash-dune-sanctuary)` — matching `contradictions.json` id `moon-basin-vow-location`. `git diff --name-status 51b286b..1b09f3f -- corpus/fixtures/r87-myth-cluster/` → only four `A` excerpt files; README, contradictions, entity/relation/timeline/sources JSON, inspiration note and clause map all `changed=False`. Negation tokens in content lines: only `lowwater-hymn-excerpt.md:4`, bounded by `symbolism-clause-map.md:11-12`; other hits are meta footers (`lowwater-hymn-excerpt.md:7`, `shell-charter-excerpt.md:13`). T3 (`gate-witness-excerpt.md:7`) and T4 (`dune-register-excerpt.md:8`) keep the single shared vow with no side chosen.

**Excerpt scope.** Same content-line map; the unextracted lines remain `shell-charter-excerpt.md:5` (framing) and `tide-bell-tally-excerpt.md:5` ("Tally hand: Sen"); hymn `:4-5` bounded by the clause map; real-world token scan of the five excerpts (`kojid|etcsl|sumer|inana|maya|spence|völusp|gutenberg|http`) → no matches, grep exit 1.

**Ledger.** 7 pipe rows × 4 columns in both revisions; ETCSL row `:8`; `external-only` present; cells 0–2 byte-identical; cell 3 = marker sentence + baseline cell text verbatim; every other row byte-identical (Spence `:13`). `git diff 51b286b..1b09f3f -- corpus/knowledge/reference-ledger.md` → one changed line (`@@ -5,7 +5,7 @@`). Corpus-wide `external-only`: decision table `:15,:17,:22` + ledger `:8` only. Independent agreement: JCOV4 (four-column shape, separate questions), JCOV5 F5 (Spence row detached, inherited), JDEP1 (`1 1 …/reference-ledger.md`).

**Checker replays.** `r87-myth-cluster`, `r89-inspiration-paraphrase`, `r88-m3-maya-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0; checker sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556` (matches V2's freeze verification).

**Sibling convergence.** Debts `#1`–`#6` corroborated: JCOV4-D4, JCOV5 F5, K1 F2 (element marker + literal), JDEP2 D-JDEP2-2/D-3, JDEP1 D3 + out-of-scope observation, H5 `#3`/`#5`, JCOV1-D4 / JCOV4-D2 (R9 mode). Verdict recommendation unchanged: **coverage (excerpt discipline + ledger sub-scope) — improved (bounded)**; bounds remain debts `#1`–`#7`.
