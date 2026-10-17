# JDEP3 — Depth judge #3 (table attacker)

Seat: JDEP3. Wave: round-88 follow-up (world-bible lane), fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Judged on the DELIVERED tree at `2ea9ef13a928475b13fd578740ea521bed4bd649` (`2ea9ef1`), baseline `dfd1fbc`. Never on intent or scratch patches; scratch is used for probes/controls only.
Target under attack: `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (7 decision rows, lines 11–17; sha256 `f85b63e4…13b873`).
Scratch: `/tmp/jdep3-B/`, `/tmp/jdep3-C/`. Receipts: `.ufo/waves/round-88/followup/JDEP3-probes.json`.
Tracked tree at measure: `git status --porcelain --untracked-files=no` → empty.

## Work performed

- Read the delivered table, both landed clusters (`corpus/fixtures/r87-myth-cluster`, `corpus/fixtures/r88-m3-maya-cluster`), the delivered `corpus/knowledge/reference-ledger.md`, and `corpus/fixtures/check_bible.py`.
- Constructed three inspired-content situations the table may not govern, each grounded in a delivered-tree state: (S1) a rights-blocked real-world source, (S2) a fictional source presented as excerpted but paraphrased, (S3) a mythology parallel that conflicts with landed canon.
- For each, ran a table-text scan (`grep -ci`) for the governing terms and, where a probe is possible, built a scratch cluster under `/tmp` and ran the delivered checker plus the table's own R5 fixed-string anchor check.
- Ran three **covered** controls on the delivered tree to confirm the attacks land on genuine residual classes rather than on already-governed ones.
- No tracked file was written; the only repository writes are this report and `JDEP3-probes.json`.

## Before → after measurements

Baseline for "before" is the r87 tree with **no** sourced-inspiration decision table; the table itself is the round-88 addition. All commands run from `lore-shokunin/`.

**S1 — rights-blocked real-world source. Classification: uncovered** (citation side covered, element side not).

```sh
for t in 'may not land' 'must not ship' 'blocked' 'withhold' 'may remain' 'disposition' 'materiality'; do
  printf '%-16s %s\n' "$t" "$(grep -ic -- "$t" corpus/knowledge/r88-sourced-inspiration-decision-table.md)"; done
```

```text
may not land     0
must not ship    0
blocked          0
withhold         0
may remain       0
disposition      0
materiality      0
```

R4 (`:14`) governs the **citation**: "mark the passage `external-only / unverified` … if text cannot be delivered, retain the citation as a research lead, not as verified support." R6 (`:16`) governs the **ledger row**: its `Use here` cell must state "whether text is delivered or external-only." Neither governs the **element**. No row states whether a materially-informed element whose required source text is undeliverable may land, what the cluster must record about it, or how the R1-vs-R2 trigger ("materially informs") is established when the text that would prove materiality cannot be delivered. The table's own R4 evidence cell names this exact state for r87 — "r87's ETCSL note gives `lines 122–163` but delivers no ETCSL text" — and still supplies no disposition row for the element that note informed.

**S2 — paraphrased in-world excerpt. Classification: uncovered.**

Scratch cluster `/tmp/jdep3-B/paraphrase2`: in-world source `ash-ledger` (`kind: fictional register`), one entity claim "The Ash-Stair Ledger records the tide-mark moved to the west stair", delivered "excerpt" is a modern summary:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3-B/paraphrase2
grep -nF -- 'moved to the west stair' /tmp/jdep3-B/paraphrase2/ash-ledger-excerpt.md
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
3:> The keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
```

The checker is `CLEAN` (exit 0) and R5's fixed-string anchor matches — because the anchor is chosen from the delivered text, a self-consistent paraphrase passes trivially. Table scan: `paraphrase` 0, `verbatim` 0, `derivative` 0, `delivery mode` 0. R5 (`:15`) requires a `source_id` resolution and a "distinctive exact phrase" match, but no row requires the delivered excerpt to be the source's own words, and there is no verbatim/translation/paraphrase/summary field. R5's "A match is only a lexical preflight … review that the passage supports the whole claim" reviews *support*, not *fidelity*; a paraphrase can support the whole claim. Note the asymmetry: R4's attribution column already says "do not infer an ancient author from a modern host or translation" — the table considered derivative delivery for real-world sources but never extended a delivery-mode concept to in-world excerpts.

**S3 — parallel conflicts with landed canon (cross-cluster). Classification: uncovered.**

Scratch `/tmp/jdep3-C/`: `landed-canon` (Foundation Roll places the first low-water signal at the West Stair) and `inspired-cluster` (Gate Hymn places it at the Mother-Tide Gate, inspired by an external parallel).

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3-C/landed-canon
python3 corpus/fixtures/check_bible.py /tmp/jdep3-C/inspired-cluster
python3 corpus/fixtures/check_bible.py --help
ls corpus/knowledge/ | grep -i 'contradict\|registry'
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations     (landed-canon, exit 0)
CLEAN: schema, citations, relations, timeline; 0 violations     (inspired-cluster, exit 0)
usage: check_bible.py [-h] bible                                 (one directory only)
no cross-cluster contradiction registry in corpus/knowledge/
```

Each cluster has its own `contradictions.json` (both `[]`); passing two directories → `error: unrecognized arguments`, exit 2. Table scan: `cross-cluster` 0, `another cluster` 0, `landed canon` 0, `prior fixture` 0, `aggregate` 0. R7 (`:17`) governs "Inspired content conflicts with another in-world account", but its record lives inside one fixture directory and the checker reads one directory. A conflict between a new cluster and already-landed canon is invisible to R7 and to the checker. R7's evidence cell exercises only intra-cluster disagreements (Hara vs Sen; two Hush Lantern first-light locations).

**Covered controls (the attacks are residual, not already-governed).**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   # CLEAN, exit 0; locator_page=True, excerpt_delivered=True, clause_map_cols=True
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster      # CLEAN, exit 0; gate_named=True, clause_matches=8/8
python3 -c '…r87 contradictions…'                                            # r87_intra_cluster_contradictions=1, id=moon-basin-vow-location
```

The table **does** govern the delivered-text passage parallel (R4), the in-world claim→excerpt mapping (R5, r87 8/8), and intra-cluster contradiction (R7). My three findings sit outside those.

## Findings & named debt

- **Depth verdict: improved (bounded).** The landed table is a genuine depth gain over the no-table baseline — it operationalises the three citation questions, locator/delivered-text rules, ledger registration, and intra-cluster conflict handling. It carries **three uncovered inspired-content classes**, none of which is a harm to a previously working surface:
  - **F1 (S1) — no disposition for a materially-informed element when the required source text is undeliverable**, and no evidentiary test for the R1/R2 "materially informs" trigger. Citation status is covered by R4/R6; the element is not.
  - **F2 (S2) — no delivery-mode rule for in-world excerpts.** R5's anchor check passes a self-consistent paraphrase; the checker stays `CLEAN`.
  - **F3 (S3) — contradiction handling is single-fixture.** A parallel-driven conflict with landed canon has no registry and no checker path.
- **Named debt — probe scope.** S2/S3 were demonstrated on scratch clusters in `/tmp` (allowed as controls); no delivered fixture yet exercises a paraphrase-delivery or cross-cluster conflict, so the findings are "ungoverned situation," not "delivered-tree violation." The delivered r87 OBS-1 case (R4's own evidence cell) is the one delivered-tree instance of S1.
- **r89 candidates** (recorded here; this seat is not authorised to write `l0-questions.md`):
  1. Add a decision row/field for "required source text undeliverable": define the R1-vs-R2 materiality test and the element's disposition (may land as unverified-support with an explicit cluster marker, or must be re-derived), plus a required marker in the inspiration note and ledger `Use here` cell.
  2. Add a delivery-mode field to R5 (verbatim / translation / paraphrase / summary), require it declared in the excerpt file and the clause→element map, and rule that a paraphrase is not the source's own text for support purposes unless linked to the underlying text.
  3. Extend R7 with a cross-cluster branch: name where an inspired-content-vs-landed-canon conflict is recorded, require both cluster paths, forbid a real-world parallel from overwriting landed canon, and consider a checker extension (or documented manual register) for cross-fixture contradictions.

## Handoff

- **Artifacts:** `.ufo/waves/round-88/followup/JDEP3.md` (this report) and `.ufo/waves/round-88/followup/JDEP3-probes.json` (probe receipts: hashes, table row map, three probes with exact commands + observed output, three covered controls, verdict). No tracked file was written; no commit or push.
- **For the integrator:** the table lands as-is; the three uncovered classes are r89 scope, not blockers. If r89 takes them, S1 needs a decision (element disposition + materiality test), S2 needs a delivery-mode field in R5 and the excerpt format, S3 needs a cross-cluster contradiction record (the checker's single-directory CLI is the mechanical limit).
- **Distinct from JDEP2** (ledger verification) and from the C3 work-wave seats; complementary to the D1/D2/R1B table drafts.
