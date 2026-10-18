## Work performed

- Seat JCOV2, whole-claim audit of the r93 Kojiki cluster `corpus/fixtures/r93-m2-kojiki-cluster/` at HEAD `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` on `main` (clean tracked tree). Axes: **anchor validity**, **R9 mode discipline**, **three-distinct-open-questions discipline**, **external attribution accuracy (live-source fetch)**, **symbolism-thread boundedness**, **rights-claim absence**, plus lexical corroboration of the zero-shared-referents claim.
- Read all 12 committed cluster files; re-ran both committed validators; replayed all 15 claim-map anchors line-by-line with an independent script (checker-free); fetched the live cited source page and compared all three quoted clauses verbatim, plus the Part/section locator and the elision marker; ran an independent normalized-key overlap scan against both prior clusters; audited the one reference-ledger row the cluster added (`corpus/knowledge/reference-ledger.md:14`).
- Dependency wait-checks (two 60s polls per wave rule; both targets present on first check, no gaps).
- Verdict evidence from the committed tree at `65838f8`; the Terebess fetch and the overlap scan are probes. Wrote only `followup/JCOV2.md`. No commit, no push; no other tracked file touched.

## Before → after measurements

**Baseline identity** — exact command:

```sh
cd lore-shokunin && git rev-parse HEAD && git status --porcelain
```

Observed:

```text
65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
(no output — tree clean)
```

**Committed validators on the cluster** — exact commands (README's replay block):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster
```

Observed (both exit 0):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS
```

**Independent anchor replay (all 15 map anchors, no checker code reused)** — embedded script, per row: needle substring-tested on the cited line, and hits counted across the file to detect line-span drift. Observed: `E1..E12: OK` each with single-line hits exactly at the cited line; `S1..S3: OK` likewise; `ANCHOR-FAILS=0`; spans `archive-record-excerpt.md:5-12` and `kojiki-chamberlain-excerpt.md:8-10` fully nonempty; `Central Land of Reed-Plains` appears at line 8 (spaced) and `Central-Land-of-Reed-Plains` at line 10 (hyphenated) — the README's `:8,10` reference covers both source-faithful variants, and the hyphenation difference is in the source translation itself (see fetch below).

**Live-source fetch (attribution accuracy)** — fetched `https://terebess.hu/english/kojiki.html` on 2026-10-17. Observed, against the cluster's claims:

- Page header: `THE KOJIKI [B.H. Chamberlain, translator 1882]` — matches the claimed translator/year attribution; note the page gives initials only.
- Section heading `DOOR OF THE HEAVENLY ROCK-DWELLING` present; it falls after `PART III. AMATERASU, THE SUN-GODDESS, AND THE STORM-GOD` and before `PART IV.- THE BEAST-LEGENDS`, so the cluster's locator "Part III" is correct.
- All three quoted clauses are verbatim matches to the page text (page line wraps aside):
  - excerpt line 8 = page: "Then the whole Plain of High Heaven was obscured and all the Central Land of Reed-Plains darkened. Owing to this, eternal night prevailed." (exact)
  - excerpt line 9 = page prefix "Therefore did the eight hundred myriad deities assemble in a divine assembly in the bed of the Tranquil River of Heaven," followed on the page by "and bid the deity Thought-Includer, …" — the `[…]` elision is legitimate and the elided span is the long assembly passage.
  - excerpt line 10 = page: "So when the Heaven-Shining-Great-August deity had come forth, both the Plain of High Heaven and the Central-Land-of-Reed-Plains of course again became light." (exact, including the hyphenated variant).
- Full name: "Basil" appears 0 times on the page; the full-name expansion "Basil Hall Chamberlain" is an external (standard, historically corroborated) identification, not page text — the excerpt file and the ledger row hedge correctly ("attributed by the source page to …"), README line 3 states the full name directly.

**Independent zero-shared-referent lexical scan** — embedded script collecting normalized (casefolded) keys for entity ids/names/aliases/epithets, event ids, relation/timeline endpoints, and source ids/titles across `r93-m2-kojiki-cluster`, `r87-myth-cluster`, `r88-m3-maya-cluster`. Observed:

```text
M2 keys: E:id:lorn-index E:id:orni E:id:slate-table E:id:teva E:name:* (4) R:* (4) S:id:m2-record-archive S:title:m-17 margin register T:* (5)
r87 ∩ M2: []
r88 ∩ M2: []
```

Census corroboration: `find corpus/fixtures -maxdepth 1 -type d` = 168 entries (167 cluster dirs + the fixtures root), matching H4's 167-row after-census and the wave's "167 dirs (0 changed + 1 new)".

**Dependency wait-checks** — exact commands and observed output:

```sh
bash .ufo/waves/poll_wait.sh .ufo/waves/round-93/M2.md 60
bash .ufo/waves/poll_wait.sh .ufo/waves/round-93/M4.md 60
```

```text
POLL_HIT path=.ufo/waves/round-93/M2.md elapsed=0s checks=0   (exit 0)
POLL_HIT path=.ufo/waves/round-93/M4.md elapsed=0s checks=0   (exit 0)
```

## Findings & named debt

Per-axis verdicts (whole-claim audit of the Kojiki cluster):

- **Anchors — verified.** All 15 map anchors resolve at their cited lines, each unique in its excerpt file; both committed validators pass (12/12 JSON facts, 3/3 editorial rows, 15/15 distinct anchors, 0 repeated references, 0 duplicate rows). JSON pointer/field lists in the map match the actual JSON (`entities.json#/0..3`, `relations.json#/0..1`, `timeline.json#/0..1` all checked row-by-row; E8's claim is an exact textual match, E2/E4 are faithful attributed paraphrases consistent with excerpt lines 6/8).
- **R9 modes — verified.** Both declared modes (`verbatim` for the M-17 register, `translation` for the Chamberlain excerpt) are in the checker's vocabulary (`support_check.py:11`), excerpt-level inline declarations match the map, the three translation rows are carried as `EDITORIAL-ANCHORS` only, `RETELLING-SUPPORT-ONLY 0`, and no R9 manual-review PASS is asserted anywhere for the translation (explicitly negated in README.md:5 and claim-excerpt-map.md:41). The one manual-gate-adjacent PASS in the receipt is absent by design — correct for this cluster.
- **Three distinct open questions — verified.** inspiration-note.md carries three separate, genuinely distinct questions: Attribution (exact printed copy/edition behind the transcription not independently identified), Rights (not assessed; no rights grant asserted), AI-training permission (not assessed; no permission inferred). Convention matches `r87-myth-cluster` and `r88-m3-maya-cluster` inspiration notes.
- **Chamberlain/Kojiki attribution — verified at its claimed strength (live fetch).** Page attribution label, 1882 year, Part III placement, section heading, and all three quoted clauses confirmed against the live Terebess transcription; the elision marker is honest. Two nuances, both already hedged in-tree: (1) the page gives only "B.H." — the expansion to "Basil Hall Chamberlain" is standard external identification, and the excerpt/ledger word it as "attributed by the source page to"; (2) the specific printed edition behind the transcription remains unidentified — named as the "Source-version limit" in `kojiki-chamberlain-excerpt.md:5` and as debt in M2.md.
- **Symbolism thread — verified bounded.** symbolism-clause-map.md's three rows map exactly the same three clauses as the map's S1–S3 with consistent archive line references (7,12 / 8,11 / 11-12, all re-verified), each row carries a limited reading plus an explicit limit clause; no causal, cultural-meaning, retelling, or canon-import claim is made ("This is not a claim that the folio causes or ends darkness…", "Teva and Orni are fictional clerks, not deities…", "The fictional folio does not restore light…"). The `Reed`-word lookalike is explicitly dismissed as lexical-only in README's R10 section.
- **No rights claims — verified.** Grep over the whole cluster finds zero grant, permission, public-domain, license, or fair-use assertions; the only rights/permission language is the open-question framing (inspiration-note.md:17-23, README.md:5), mirrored by the reference-ledger row (`corpus/knowledge/reference-ledger.md:14`: "Open question — not assessed; no rights grant asserted… no permission inferred"). No improvement or regression to the corpus's rights posture: the cluster adds a sourced external text with the question discipline intact (unchanged on that axis by design, unprovable-but-better in coverage).
- **Zero shared referents — lexically corroborated, semantically still open.** My independent normalized-key scan reproduces the author-side result: no exact key shared with r87 or r88 (ids, display names, aliases, epithets, event ids, endpoints, path-qualified source ids). **Named debt (already flagged in-tree, correctly not closed):** the semantic half of the zero-referent claim — identity/occasion review, including the dismissed `Reed` overlap — is M6's pending M2-specific review; `.ufo/waves/round-93/M6.md` covers M1's `r93-myth-cluster3`, not M-17 (README.md:15 and M2.md/M4.md handoffs all say so consistently). Do not promote the cluster's zero-shared-referents claim from "lexical, author-side + JCOV2-corroborated" to "independently semantically verified" until that review lands.
- No fabricated receipts found: every number I re-derived (15/15 anchors, 12/12+3/3 rows, 0 overlaps, 167 dirs) matched the committed claims.

## Handoff

- Written: `.ufo/waves/round-93/followup/JCOV2.md` only. No commit, no push; no scratch left behind (probe fetch output lived in the session tool-result store; scan scripts were inline heredocs, no /tmp residue).
- **Verdict for the parent:** the Kojiki cluster's auditable claims hold at HEAD `65838f8` — anchors 15/15 verified independently of the checker, R9 mode discipline intact, three open questions present and distinct, attribution verified against the live source page (including Part III locator and verbatim clauses), symbolism thread bounded, no rights claims. Remaining blocker for a wholesale "zero shared referents" statement is M6's M2-specific semantic review (named debt, tracked in README/M2/M4) plus the standing source-edition/rights/training unknowns, which the cluster correctly leaves open.
- Suggested r94 carry (already named in-tree, no new debt introduced): M2-specific M6 review before the claim is strengthened; optionally cite the page's initials-only "B.H." form when tightening README's full-name phrasing.
