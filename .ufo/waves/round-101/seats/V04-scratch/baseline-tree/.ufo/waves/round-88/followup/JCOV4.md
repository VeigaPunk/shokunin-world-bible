# JCOV4 — Coverage judge #4 (province discipline, fresh eyes)

Seat scope: audit both landed clusters' prose (inspiration notes, symbolism
indexes, READMEs, delivered excerpts) plus the C3 table and ledger row against
(a) `lore-shokunin/PROVINCE.md`'s refusal list, (b) the D1 three-question rule,
and (c) the kotodama generation-vs-canon handoff boundary — **without reading
`C7B.md` or `M5-compliance.json` first** — then compare verdicts. Axis judged:
**coverage**. Verdict recommendation at the end.

Judged tree: lore-shokunin `HEAD = 2ea9ef13a928475b13fd578740ea521bed4bd649`
(`git rev-parse HEAD`), work commit of this round; tree clean except this
seat's own untracked output dir. Every measurement below was taken on that
delivered tree (scratch used only for the two external fetches). This seat's
only write is this report.

## Work performed

- Read `PROVINCE.md` (all 11 lines), `corpus/knowledge/seed.md:26-29`, the
  persisted `wave-spec.md` (C2/C3 wording), then the delivered artifacts on the
  committed tree, not on patches:
  - `corpus/fixtures/r87-myth-cluster/` (9 files) and
    `corpus/fixtures/r88-m3-maya-cluster/` (10 files) — READMEs, inspiration
    notes, excerpts, symbolism maps, and all five JSON records each;
  - `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (D1) and
    `corpus/knowledge/reference-ledger.md` (D3 ETCSL row);
  - `git show 2ea9ef1 -- corpus/fixtures/r87-myth-cluster` to see exactly what
    the OBS-1 repair changed.
- Ran the structural checker on both clusters, a citation-resolution probe, a
  three-question-heading probe, a tick-collision probe, a clause→excerpt
  fixed-string match, a rights-token sweep, a cross-province token sweep, and
  an `external-only` marker sweep (commands and outputs below).
- Independently verified **both external citations** over the network
  (`curl`): Gutenberg eBook 53080 (Spence) and ETCSL `tr141.htm`.
- Only after forming the verdicts above did I read `.ufo/waves/round-88/C7B.md`
  and `.ufo/waves/round-88/patches/M5-compliance.json` (plus `C7.md`, `M3.md`,
  `S3.md` for context) and record agreements/disagreements.
- No wait-check was specified for this seat; the C2/C3 artifacts are landed and
  committed, so nothing was unavailable.

## Before → after measurements

Baseline `dfd1fbc`; after = delivered `2ea9ef1`. All commands from the repo root.

**Structural checker (both clusters):**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
```

The checker reads JSON only; a `CLEAN` result is not evidence about prose.

**Refusal 1 — canon without an in-world citation** (citation resolution probe
over entities' `first_appearance` + claims, relations' `source_id`, timeline
`source_id`):

```text
[r87-myth-cluster] unresolved_or_missing=[]
[r88-m3-maya-cluster] unresolved_or_missing=[]
```

**D1 three-question rule** (distinct `##` headings in each inspiration note):

```text
[r87-myth-cluster] inspiration_note_headings=['Parallel cited', 'Attribution question', 'Rights question', 'AI-training-permission question']
[r88-m3-maya-cluster] inspiration_note_headings=['Parallel cited', 'Attribution question', 'Rights question', 'AI-training-permission question']
```

Delivered table columns are the three separate questions, not merged:

```text
rows= 9 pipe_counts= [7, 7, 7, 7, 7, 7, 7, 7, 7]
three_questions_separate_columns= True
```

**Refusal 2 — silently resolving contradictions** (tick-collision probe + the
two contradiction records):

```text
[r87-myth-cluster] tick 3 shared by 2 events; distinct_entities=2 distinct_places=2
[r88-m3-maya-cluster] tick 9 shared by 2 events; distinct_entities=2 distinct_places=2
```

r87's `contradictions.json` holds one record (`moon-basin-vow-location`) whose
`why` states the disagreement is "reported and left unresolved". r88 M3's
`contradictions.json` is `[]`; the README explains the shared tick-9 pair as an
"occupied-slot near-miss, not a double-booking" — both entries carry the same
source `paired-clock` and are consistent, so an empty array is correct, not a
silent resolution.

**Refusal 3 — real-world rights claims** (token sweep over both clusters, the
table, and the ledger):

```sh
grep -rniE "public domain|is free to|permitted to (reproduce|use|train)|no copyright|copyright expired|cc0|creative commons|may be freely|license granted|permission is granted" \
  corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster \
  corpus/knowledge/r88-sourced-inspiration-decision-table.md corpus/knowledge/reference-ledger.md
```

```text
no rights-assertion tokens found
```

Both notes leave rights and AI-training permission explicitly open; the ledger
keeps the three questions in three separate cells for all four rows.

**Clause→excerpt support (the delivered table's own row-5 mechanism):**

```sh
grep -nF -- 'at the Mother-Tide Gate' corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md
```

```text
3:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
```

```text
r87 gate_named= True clause_matches=8/8
r88 cited_clauses= ['He called out ‘Earth,’', 'and the solid land appeared.']
r88 clause_matches=1/2
```

**Census / coverage counters:**

```text
delivered fixture_directories= 149
delivered inspiration_notes= 2
r88 dirs= ['r88-m3-maya-cluster', 'r88-mixed-stop', 'r88-nonholder-stop', 'r88-shape-ambiguous-armed']
```

**Independent external verification (network, `curl`):**

```sh
curl -sS --max-time 45 -o /tmp/spence53080.html https://www.gutenberg.org/files/53080/53080-h/53080-h.htm
curl -sS --max-time 45 -o /tmp/etcsl141.html https://etcsl.orinst.ox.ac.uk/section1/tr141.htm
```

```text
Gutenberg 53080 (1035633 bytes): "He called out “Earth,” and the solid land appeared." verbatim;
  the delivered "[…]" elision drops exactly one intervening sentence (Hurakan), nothing else;
  page marker <span class="pagenum">[<a id="pb209" …>209</a>]</span> present, 1156 chars before the
  sentence with no other page marker between → passage is on printed p. 209;
  Chapter V heading = "CHAPTER V: MYTHS OF THE MAYAS"; H3 subsections include "The Creation-Story".
ETCSL tr141 (34853 bytes): "seven gates" present; turban/pectoral/pala/garment terms present;
  lines 123–128 describe the first gate and the turban removal.
```

Both external citations are therefore substantively correct.

## Findings & named debt

### Province audit — no refusal-list violation found

- **Canon-without-citation:** clean in both clusters (`unresolved_or_missing=[]`).
- **Silent contradiction resolution:** not present; r87 reports, r88 M3 has
  nothing to report (same-source, consistent).
- **Real-world rights claims:** none; the three questions stay distinct and open.
- **Game-mechanics verification (game-dev-2d):** not present. The r88 README's
  "occupied-slot near-miss, not a double-booking" is a statement about lore's
  own timeline schema, verified from the cluster's JSON (2 events, 2 distinct
  entities, 2 distinct places), not a game-mechanics ruling.
- **D1 three-question rule:** held in prose and in the table's three separate
  columns.
- **kotodama handoff boundary:** bounded pass. Neither cluster designs a
  general mythic/symbolic system; both symbolism maps are bounded editorial
  readings tied to named clauses and named fictional elements, and both notes
  state the parallel "supplies no fictional canon". The formal handoff file
  `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`
  is still absent, so procedural conformance cannot be verified (agree with
  S3/C7B — do not report it closed).
- **Cross-province sweep** (`game mechanic|hit ?points|damage|conlang|phonolog|
  lexicon|publish|kdp|prompt`) over both clusters and the table: `none found`.

### Independent findings not raised by C7B or M5

1. **Quote-glyph defect in the r88 clause map (verbatim-match failure).** The
   delivered `symbolism-clause-map.md:7` renders its first cited clause as
   `He called out ‘Earth,’` (single quotes U+2018/U+2019), while the delivered
   excerpt uses `He called out “Earth,”` (double quotes U+201C/U+201D):

   ```sh
   grep -nF -- 'He called out ‘Earth,’' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md ; echo "exit=$?"
   grep -nF -- 'He called out “Earth,”' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md ; echo "exit=$?"
   ```

   ```text
   exit=1
   5:> … He called out “Earth,” and the solid land appeared.
   exit=0
   ```

   The clause resolves only after punctuation normalization, which is *not*
   what the delivered table prescribes ("record a distinctive exact phrase …
   then run a fixed-string, line-numbered search such as `grep -nF …`; a …
   zero match fails"). Recorded as named debt, low severity.

2. **Stale "shore threshold" description left by the OBS-1 repair.** The repair
   narrowed the r87 JSON claim away from "shore threshold" to "places the shell
   ring and bowl at the Mother-Tide Gate", and the map now disclaims the Gate's
   "threshold status". But the same phrase survives in two prose locations:

   ```text
   corpus/fixtures/r87-myth-cluster/inspiration-note.md:5  … "This fixture uses a shore threshold and a shared bowl as original imagery"
   corpus/knowledge/reference-ledger.md:8                  … "the fixture uses original shore-threshold imagery"
   corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md: grep "threshold\|shore" → NONE in hymn verse
   ```

   Under the delivered table's own support rule, the ledger's "shore-threshold
   imagery" is not resolvable in the delivered verse, and it contradicts the
   map's explicit threshold-status disclaimer. The repair fixed the JSON claim
   and the verse but did not sweep the two descriptive prose sites.

3. **C3 table row-5 evidence asymmetry.** The scope note (`table:1`) extends the
   support rule to "EVERY source-attributed in-world JSON fact", and row 5
   flags the unlanded M1/M2 drafts and M4's repoint for metadata-only claims —
   but it does not disclose that the **landed r87 cluster itself** delivers
   prose for only 1 of its 5 in-world source IDs:

   ```text
   r87 claimed source_ids: ['dune-register', 'gate-witness', 'lowwater-hymn', 'shell-charter', 'tide-bell-tally']
   r87 in-world prose files: ['README.md', 'inspiration-note.md', 'lowwater-hymn-excerpt.md', 'symbolism-clause-map.md']
   → gate-witness / dune-register / shell-charter / tide-bell-tally → prose_files: NONE
   ```

   Six of seven entities, both relation edges, and three of four timeline events
   are metadata-only under the rule the table itself states. That is an evidence
   gap, not a checker failure — but the table claims "every row verified against
   the landed clusters", and this asymmetry is undisclosed.

4. **Draft residue in the delivered table.** `r88-sourced-inspiration-decision-table.md:5`
   still reads `Draft destination: corpus/knowledge/r88-sourced-inspiration-decision-table.md`
   — a self-referential draft line left in a landed file (`draft_destination_line_present= True`).

5. **Minor attribution imprecision (externally checked).** `r88-m3-maya-cluster/inspiration-note.md:5`
   cites `Chapter V, "The Maya," … printed p. 209`. Chapter V's actual title is
   "MYTHS OF THE MAYA" ("The Maya" is a Chapter IV subsection). Chapter number,
   subsection "The Creation-Story", and printed page 209 are all correct and
   externally verified, so the citation resolves; only the quoted chapter title
   is imprecise.

### Comparison with C7B.md and M5-compliance.json

Agreements:

- Both clusters replay `CLEAN` exit 0; the checker is structural only (C7B:41-67;
  M5 `baseline_measurements`).
- OBS-1 repair: Gate named in the delivered hymn, `8/8` map clause matches,
  claim stays `lowwater-hymn` (C7B:165-175; M5 `m4_obs1_alternatives.excerpt`).
- M3 attribution limited to Spence's English account; rights and training left
  open and distinct (C7B:99-136; M5 M3 `Attribution, rights, and AI-training` pass).
- Clause→element index is editorial and bounded, not canon (C7B:209; M5
  `pass_with_punctuation_note`).
- Kotodama boundary is a bounded pass with the integration contract absent
  (C7B:212; M5 `scope_evidence.formal_integration_contract_present=false`).
- M1/M2's metadata-only in-world claims are an evidence gap, not a violation
  (C7B/M5 M1/M2 `fail` rows; my finding 3 extends this to the landed r87 cluster).
- Census grows and a second inspiration note lands (C7B:177-196 measured 145→146
  in scratch; delivered is 149 — the extra 3 are C1 calibration fixtures).

Disagreements:

- **Quote glyphs (my finding 1).** C7B normalized with
  `norm = re.findall(r'[a-z0-9]+', s.lower())` (C7B:80-86) so its
  `row1 … =True`; M5 labels the index `pass_with_punctuation_note`. Both
  *disclosed* the punctuation issue, but classified it as a note. I classify it
  as a named defect against the table's own `grep -nF` rule: the cell as
  delivered does not match verbatim.
- **r87 metadata-only claims (my finding 3).** C7B:211 calls the repaired r87
  cluster a clean "PASS" and M5's r87 coverage discusses only OBS-1; neither
  names that 4 of 5 r87 source IDs have no delivered prose. I record that as an
  undisclosed gap under the table's own scope note.
- **Passage-locator bar.** C7B:208 marks it PARTIAL (only one printed-page
  locator delivered); M5's M3 row marks the locator requirement `pass`. The
  wave-spec says "passage-level locators" (plural). I side with C7B: one page
  locator for one passage is delivered, so the plural bar is partially met.
- No disagreement with M5's `recommend_m3` selection: M3 is the only candidate
  whose external and in-world claims are supported by delivered excerpts.

### Verdict recommendation

- **Coverage axis: improved (bounded).** A second sourced-mythology cluster
  landed with a passage-level locator, a clause→element index, and externally
  verified source text; OBS-1 is repaired in the delivered excerpt; census
  145→149, notes 1→2, both clusters exit 0. The gain is real and non-traded.
- **Province discipline: no refusal-list violation; bounded passes with named
  debt.** The three-question rule and the kotodama boundary hold in the
  delivered prose; the only boundary gap is the still-absent formal handoff
  contract (upstream, not lore's to manufacture).
- Do **not** promote coverage to fully "verified": carry findings 1–4 as named
  debt. Findings 2 and 3 are the ones a fresh-eyes audit adds to the round's
  record; finding 2 is the one that most directly implicates province discipline
  (a delivered description not resolvable in the delivered text).

## Handoff

- Integrator: adopt the coverage verdict **improved (bounded)** and carry
  findings 1–4 as named debt. If any prose sweep is authorized in a later round,
  the two minimal edits are `r87-myth-cluster/inspiration-note.md:5` and
  `reference-ledger.md:8` ("shore threshold" → language the delivered verse
  supports), plus aligning the r88 map's first clause cell to the excerpt's
  double-quote form so `grep -nF` resolves verbatim.
- Do not treat the kotodama handoff contract as closed; it remains absent in the
  sibling lane and is not lore's to write.
- This seat wrote only `.ufo/waves/round-88/followup/JCOV4.md`. No tracked file,
  patch, registry, commit, or push was touched; sibling repos were read-only.
