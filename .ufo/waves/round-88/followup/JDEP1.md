# JDEP1 — Depth judge #1 (D1 table verification)

Judged tree: `2ea9ef1` (work commit), baseline `dfd1fbc`. Tree clean at start of work.
Artifact under test: `corpus/knowledge/r88-sourced-inspiration-decision-table.md`.
Landed clusters: `corpus/fixtures/r87-myth-cluster` (OBS-1 excerpt repair) and
`corpus/fixtures/r88-m3-maya-cluster` (new second-family cluster).

## Work performed

- Diffed the landed table against its source patch to isolate the integration edit:
  `diff .ufo/waves/round-88/patches/D1-table.md corpus/knowledge/r88-sourced-inspiration-decision-table.md`
  → the only difference is two prepended lines: an HTML comment carrying R1B's scope
  clarification plus a blank line. Every rule cell is byte-identical to D1's patch.
- Replayed every command the table cites, or a concrete instantiation of it, against
  **both** landed clusters: the row-5 fixed-string anchor search
  (`grep -nF -- 'anchor phrase' <excerpt-path>`), the r87 checker replay quoted in the
  table's closing paragraph, the row-6 ledger-shape probe, and `seed.md:26–29`.
- Re-ran the two D1 probe scripts the table's evidence column reports
  (r87 `clause_matches=8/8`; ledger `ETCSL_rows`/`Spence_rows`).
- Ran an operational test of R1B's scope clarification: applied the support rule to
  every source-attributed JSON fact in both landed clusters (entity claims,
  `first_appearance` pointers, relation edges, timeline events) and measured how many
  resolve to delivered prose.
- Read the seat reports that produced the artifact (`D1.md`, `R1B.md`, `R1.md`, `T1.md`,
  `D3.md`, `M3.md`) to separate what the table *claims* from what the tree *contains*.

## Before → after measurements

### Table shape and provenance

```sh
diff .ufo/waves/round-88/patches/D1-table.md corpus/knowledge/r88-sourced-inspiration-decision-table.md
```
```text
0a1,2
> <!-- Landed by L1 integration with R1B's scope clarification: the support rule below covers EVERY source-attributed in-world JSON fact — entity claims and first-appearance pointers, relation edges, timeline events, and equivalent records. -->
> 
diff-exit=1
```

```sh
python3 -c 'from pathlib import Path; s=Path("corpus/knowledge/r88-sourced-inspiration-decision-table.md").read_text(); rows=[x for x in s.splitlines() if x.startswith("|")]; w=[sum(c=="|" and (i==0 or r[i-1]!=chr(92)) for i,c in enumerate(r)) for r in rows]; print("decision_rows={} widths={} consistent={}".format(len(rows)-2,w,len(set(w))==1))'
```
```text
decision_rows=7 widths=[7, 7, 7, 7, 7, 7, 7, 7, 7] consistent=True
```
7 decision rows, 6 columns each, three distinct citation columns
(`Attribution`, `Rights status`, `AI-training permission`) present.

### Both landed clusters pass the checker (table's closing-paragraph replay)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster; echo "exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
```
```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```
The table's closing claim — that the checker does not read inspiration notes, excerpts,
or symbolism maps — is confirmed: `grep -n "\.md\|glob\|rglob" corpus/fixtures/check_bible.py`
returns only line 45, `rows = json.loads(path.read_text(...))`. The checker reads JSON only.

### Row-5 rule instantiated on the r87 cluster (OBS-1 repair) — PASS

```sh
grep -nF -- 'At low water we set the shell ring beside the bowl at the Mother-Tide Gate.' corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md
grep -nF -- 'Mother-Tide' corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md
sed -n '33p' corpus/fixtures/r87-myth-cluster/entities.json
```
```text
3:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
3:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
        "statement": "The Low-Water Hymn places the shell ring and bowl at the Mother-Tide Gate.",
```

D1's 8/8 clause replay, re-run verbatim on the delivered tree:
```text
gate_named=True; first_appearance=lowwater-hymn; claim_source=lowwater-hymn; clause_matches=8/8
```
The landed repair is the **excerpt** variant (source stays `lowwater-hymn`; the Gate phrase
is added to the hymn excerpt), not the repoint variant. The table's row-5 statement that
M4's repoint alternative "delivers no witness excerpt" also holds on the tree:
`grep -rn 'witness slip places' corpus/fixtures/r87-myth-cluster/` → exit 1, no match.

### Row-5 rule instantiated on the maya cluster — named anchors PASS, literal source clause FAILS

```sh
for a in 'Aru carried the north lantern at Quiet Rise' 'Evin held the south bell at Salt Court' 'Quiet Rise' 'Salt Court'; do grep -nF -- "$a" corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md; done
```
```text
10:> Tick 9: Aru carried the north lantern at Quiet Rise.
11:> Tick 9: Evin held the south bell at Salt Court.
10:> Tick 9: Aru carried the north lantern at Quiet Rise.
11:> Tick 9: Evin held the south bell at Salt Court.
```
All four entity claims, four `first_appearance` pointers, and two timeline events resolve
to `paired-clock` → `fictional-excerpts.md:10–11`. Named-anchor support: **PASS**.

The cluster's clause→element map, however, misquotes its own source:

```sh
grep -nF -- 'He called out ‘Earth,’' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md; echo "exit=$?"
grep -nF -- 'and the solid land appeared.' corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md; echo "exit=$?"
```
```text
exit=1
5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
```
Byte check: the map's `Cited clause` cell renders `He called out ‘Earth,’` (single curly
quotes) while `source-excerpt.md:5` has `He called out “Earth,”` (double curly quotes), so
`'He called out ‘Earth,’' in excerpt == False`. Raw fixed-string matching is **1/2**;
2/2 only after quote normalisation. T1 recorded exactly this (`External-clause matching is
1/2 raw and 2/2 after quote/whitespace normalization`) and recommended standardising it;
the delivered tree does not standardise it.

### Row-6 ledger shape and the unsatisfied registration

```sh
python3 -c 'from pathlib import Path; p=Path("corpus/knowledge/reference-ledger.md"); s=p.read_text(); rows=[x for x in s.splitlines() if x.startswith("|")]; data=rows[2:]; print("ledger_data_rows={}".format(len(data))); print("ETCSL_rows={}".format(sum("ETCSL" in x for x in data))); print("Spence_rows={}".format(sum("Spence" in x for x in data))); print("column_count={}".format(len(rows[0].split("|"))-2))'
```
```text
ledger_data_rows=4
ETCSL_rows=1
Spence_rows=0
column_count=4
```
```sh
grep -rn 'Spence' corpus/knowledge/
```
```text
corpus/knowledge/r88-sourced-inspiration-decision-table.md:11: ... M3 to Spence's English summary ...
corpus/knowledge/r88-sourced-inspiration-decision-table.md:14: ... M3 supplies a page-209 Spence excerpt ...
corpus/knowledge/r88-sourced-inspiration-decision-table.md:16: ... (Kojiki, Völuspá, and Spence) are not in D3's ETCSL-only append ...
```
Spence appears only inside the decision table, never as a ledger row. `git diff dfd1fbc..2ea9ef1
-- corpus/knowledge/reference-ledger.md` confirms the only ledger change is D3's ETCSL row
plus the heading/explanatory generalisation. `seed.md:26–29` was read verbatim: it requires
three distinct questions and a ledger, and defines no row syntax — the table's reading is correct.

### Operational test of R1B's scope clarification (both clusters)

Applying "every source-attributed JSON fact" (entity claims, `first_appearance` pointers,
relation edges, timeline events) to the delivered prose:

```text
r87-myth-cluster: entity_claims 1/7 have delivered prose; first_appearance 1/7; relation_edges 0/4; timeline_events 0/4
   prose files: ['README.md', 'inspiration-note.md', 'lowwater-hymn-excerpt.md', 'symbolism-clause-map.md']
r88-m3-maya-cluster: entity_claims 4/4 have delivered prose; first_appearance 4/4; relation_edges 0/0; timeline_events 2/2
   prose files: ['README.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md', 'symbolism-clause-map.md']
```
Only `lowwater-hymn` has delivered prose in the r87 cluster; `gate-witness`,
`dune-register`, `shell-charter`, `tide-bell-tally` have none. The new M3 cluster is fully
covered. `inspiration_note_files= 2` (r87 + r88-m3).

## Findings & named debt

**Row-by-row verdicts (7 rows, judged on the delivered tree only).**

| Row | Rule cell | Evidence cell on the delivered tree |
|---|---|---|
| 1 real-world parallel | sound; matches `PROVINCE.md` boundary | **partial** — r87 + M3 verified (Spence note, Ch. V, printed p. 209, excerpt delivered); M1 (Kojiki) / M2 (Völuspá) are not in the tree |
| 2 no outside source | sound | verified — both landed clusters name a specific source; neither exercises the optional branch |
| 3 citation field unknown | sound | verified — r87 and M3 notes both carry the three separate `## … question` headings |
| 4 passage-specific parallel | sound | **partial** — "r87 ETCSL gives lines 122–163, delivers no ETCSL text" TRUE; "M3 supplies a page-209 Spence excerpt" TRUE; the M1 six-locators/four-lines datum is not on the tree |
| 5 in-world claim → excerpt | sound and operational | **one overclaim** — "its external source clauses also resolve in a delivered excerpt" is 1/2 raw, 2/2 normalised; the 8/8 r87 clause replay and the OBS-1/`entities.json:33` description replay exactly |
| 6 register one ledger row | sound (four-column format matches the live header) | **unsatisfied on the tree** — the cell says "register the selected new reference(s) at integration"; integration landed the table but not the Spence row |
| 7 conflict preserved | sound | **partial** — r87 Hara/Sen contradiction verified present; M3 `contradictions.json` is `[]` (verified); M2's Hush Lantern datum is not on the tree |

**R1B scope clarification — present, but only semi-operational.** It is present verbatim in
spirit as `r88-sourced-inspiration-decision-table.md:1`, an HTML comment. R1B's own
instruction was to make the rule explicit *inside* the "An in-world claim is attributed to
a delivered excerpt" row (`R1B.md:8`, `R1B.md:95–97`). L1 landed it as a non-rendered
comment instead. Consequence: the row's Decision cell still reads conditionally ("An in-world
claim **is attributed to a delivered excerpt**") and never names `first_appearance` pointers,
relation edges, or timeline events; those four classes appear only in the comment. A reader
of the rendered table, or any consumer that strips comments, gets the narrower rule. The
clarification is therefore **stated but not operational in the rule text**.

**Disclosure gap exposed by the clarification.** With the rule applied at R1B's intended
breadth, the r87 cluster's support state is `1/7` entity claims, `1/7` first-appearance
pointers, `0/4` relation edges, `0/4` timeline events backed by delivered prose. The table's
row-5 evidence cell discloses only OBS-1 (the Gate claim) plus the M1/M2 gaps; the remaining
six r87 claims and all r87 edges/events are metadata-only and are not disclosed. The
underlying prose was never delivered, so this is an evidence gap, not a false claim — but the
table presents itself as the enforcement rule and under-reports its own cluster's gap.

**Verdict recommendation for depth: `improved`.** The move adds a six-column rule table with
three distinct citation fields, excerpt-delivery requirements, per-claim anchor procedure,
ledger registration, and conflict handling, and it registers the r87 ETCSL row in
`reference-ledger.md` (3 → 4 data rows, heading generalised from "method references"). When
the row-5 rule is actually executed it is operational on the new M3 cluster (4/4 + 4/4 + 2/2)
and reproduces the r87 8/8 clause result and the `CLEAN … 0 violations` replay exactly.
Nothing in the delivered tree is harmed.

**Counter-consideration for the L1.** The wave spec requires the table's "every row verified
against the landed clusters" (`wave-spec.md:33–34`). That is not met: rows 1, 4, 5, and 7
carry M1/M2 evidence that does not exist on the delivered tree (assertion-only cells), and
row 6's own registration instruction was not executed for the cluster the table was verified
against. If the round's judge holds that spec line strictly, depth should be scored
`unprovable-but-better` rather than `improved`. On the axis definition alone (a landed,
substantive depth artifact that harms nothing), `improved` is the honest call.

**Named debt (all on the delivered tree).**
1. **Row 6 unsatisfied:** register the Spence reference in `corpus/knowledge/reference-ledger.md`
   with the existing four-column header. The ledger on `2ea9ef1` has `Spence_rows=0` while the
   table's own row 6 requires one row per real-world reference used.
2. **Rows 1/4/5/7 assertion-only:** the M1 Kojiki and M2 Völuspá clusters cited as evidence are
   absent (`corpus/fixtures/r88-myth-cluster2` and `corpus/fixtures/r88-norse-cluster` do not
   exist; the only `r88-*` fixtures are `r88-m3-maya-cluster`, `r88-mixed-stop`,
   `r88-nonholder-stop`, `r88-shape-ambiguous-armed`). Either land those clusters or rewrite the
   cells to cite only landed evidence.
3. **Row 5 overclaim:** "its external source clauses also resolve in a delivered excerpt" is
   false under the row's own fixed-string preflight (1/2 raw). Fix the map's quotation marks in
   `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md:7` or state the normalisation step
   in the cell. T1 raised this in-wave and it was not integrated.
4. **Scope clarification placement:** move the R1B sentence into the row-5 rule cell so the
   named classes (entity claims, first-appearance pointers, relation edges, timeline events)
   survive comment stripping and Markdown rendering.
5. **Undisclosed r87 support gap:** if the clarification is adopted at R1B's breadth, the table
   should disclose the r87 `1/7 / 1/7 / 0/4 / 0/4` state, or the r87 cluster's remaining sources
   should get delivered prose. Today the table implies OBS-1 was the whole gap.
6. **Minor:** the row-5 OBS-1 sentence is written in the present tense ("the structural checker
   still returns `CLEAN`") about a state the delivered tree has partly repaired. The
   `entities.json:33` line number still resolves to the same claim, so the citation is not
   broken, but the cell reads as current rather than historical.
7. **T1's other M3 recommendation unintegrated:** `inspiration-note.md:7` still says the verse
   "explicitly rejects the source passage's world-making outcome"; T1 asked to soften this to
   "contrasts with" or mark it as interpretation. The clause map's own `Limit` column already
   says the reading "does not attribute … a rule", so the note and the map disagree in tone.

## Handoff

- Written: `.ufo/waves/round-88/followup/JDEP1.md` (this file). No other repository write; no
  commit or push; scratch work was in-shell only.
- Recommendation to the L1: **depth = `improved`**, with named debts 1–7 above; downgrade to
  `unprovable-but-better` only if the spec's "every row verified against the landed clusters"
  line is applied strictly, since rows 1/4/5/7 rest on M1/M2 evidence absent from `2ea9ef1`.
- Highest-value single fix if only one is taken: **debt 1** (register Spence in the ledger) —
  it is a one-row edit that makes the table's own row-6 rule true for the cluster it was
  verified against. Debt 4 (move the scope sentence into the row) is the second.
- Replay commands and observed outputs for every claim above are inline in
  "Before → after measurements"; the two 60-second dependency waits specified for this seat
  were not needed because the work commit and both landed clusters were already present.
- Sibling repos untouched; `corpus/knowledge/seed.md` and `reference-ledger.md` were read only.
