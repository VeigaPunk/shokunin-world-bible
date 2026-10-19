# Lessons — round 103 · lane lore (world bible)

- mined: 2026-10-19 — from LOG.md, SCORECARD.md, corpus/knowledge/ and the kaika W1 STATE dossier §4–§5 (fleet repo, fleet-root-relative: `.ufo/waves/kaika-w1/lore-state.md`, branch `kaika/ledger`); pointers re-graded by the r103 reviewer seat, `.ufo/waves/round-103/seats/R103Reviewer-pre.md` (49 CONFIRMED, 2 SHIFTED, 0 WRONG)
- every evidence pointer was re-verified in this worktree with `sed -n '<line>p' <file>`; quoted fragments are verbatim, ≤20 words
- `captured-by` names the `corpus/QUALITY.md` criterion that now covers the class; every class below was uncaptured before r103 (`corpus/QUALITY.md` did not exist)

## Mistakes

| M## | class | evidence pointer (file:line + verbatim fragment) | captured-by criterion (Q## or none before r103) | fix |
|---|---|---|---|---|
| M01 | Unsupported hard rule: a structural predicate enforced as an error without a convention that makes the property mandatory, causing false positives | LOG.md:54 — "a legitimate homonym gets `VIOLATION` and exit 1 indistinguishable from true checker failures" (r4 closure correction, LOG.md:52) | Q01 (none before r103) | a predicate fails a bible only where a declared in-world or schema convention makes the property obligatory; otherwise it warns (exit 0) or routes an L0 question |
| M02 | Self-authentication: new authored text restates or justifies its own premise; a label treated as provenance | LOG.md:205 — "the new prose only restates already encoded assertions and is circularly authored" (r14 rejected, LOG.md:203); LOG.md:1398 — "a registry label cannot authenticate independent provenance" (r76 rejected, LOG.md:1397) | Q02 | new fiction admitted only for a consequence not already encoded and not justified by its own premise; IDs, labels and registry rows never confer provenance |
| M03 | Report upgraded to fact: a reported observation, allegation or non-finding treated as receipt, identity, custody or absence | LOG.md:840 — "a possible reported allegation, not authenticated receipt" (r49 rejected, LOG.md:839); LOG.md:950 — "reported placement does not establish continued presence or negate a later non-finding" (r55 rejected, LOG.md:949) | Q03 | encode reports as attributed claims; identity, occasion, custody and absence each need their own in-world source |
| M04 | Encoding overreach: a field (tick, place, dependency) asserts more than its excerpt supports | LOG.md:232 — "reject as submitted (depth unchanged, coverage unchanged, calibration harmed overall)" (r16, LOG.md:231); correction limits prose to "an unresolved place ID, without asserting Harbor, Tower" (LOG.md:233); r71 tick succession trade rejected (LOG.md:1271) | Q04 | every encoded value supported by its mapped excerpt; editorial encodings labelled editorial in the map and README |
| M05 | Prior-art failure: the candidate repeats an exercised branch or applies an already-admitted distinction | LOG.md:633 — "warned the axis claim might repeat r7" (r38 rejected, LOG.md:632); LOG.md:782 — "reads r34/r41/r43 prior art … reject if no material novelty" (r46 rejected, LOG.md:784) | Q05 | before declaring, sweep LOG.md, reports/ and corpus/knowledge/ for the same branch or rule; a repeat is not a gain; cite the sweep |
| M06 | No decision delta: a diagnostic or table adds output, but no non-author makes a different repair or editorial choice | LOG.md:1530 — "the baseline independently chose **substantially the same actions**" (r82 rejected, LOG.md:1537); r56 candidate "rejected and rolled back" (LOG.md:970) | Q06 | admit only on a sealed baseline-vs-proposal comparison by readers who did not author it showing a different first action, or a seeded case the baseline decides wrongly or leaves undecided |
| M07 | Hedging a definite finding: over-qualification is itself a calibration harm | SCORECARD.md:356 — "r89 calibration is **harmed** … null-chain/tick findings are definite at `51b286b`, wrongly qualified at `e97613c`" (r89 admitted then reclassified harmed) | Q07 | definite structural findings stay definite; qualify only where the checker cannot decide, and name the undecidable input |
| M08 | Accounting and process errata: declared≠dispatched counts, phantom IDs, unusable reports, foreign writes | SCORECARD.md:600 — "ROSTER ERRATUM (recorded append-only in LOG)" (×3: 600, 634, 667); SCORECARD.md:383 — "32 tool-terminal `completed` labels do not mean 32 usable reviews"; LOG.md:1500 — "committed … under wrong inherited games-engine-mechanics-shokunin identity and verifier says it pushed" | Q08 | closure counts computed from dispatch receipts, never typed; every cited seat/report/ID resolves to a file before closure; verifiers never write pinned surfaces |
| M09 | Evidence durability: pointers into transient or parent-repo paths | corpus/tools/README.md:331 cites `.ufo/waves/round-99/seats/S2-scratch/…` — `ls` → No such file (deleted by f553a27; 24 such dead pointers, dossier D7); corpus/knowledge/r102-freshness-sweep.md:67 — "F1 — dangling commit pin (corrected)" | Q09 | durable corpus cites only tracked, non-transient, lane-root-relative paths — never `*-scratch/` or `.shokunin/<lane>/`; freshness sweeps check path existence alongside digests |
| M10 | Unopened or headerless citation: notes missing the header triplet; a citation that resolves to nothing | LOG.md:3603 — "the C2 source citation "r100 V33" was a phantom — no V33 seat exists in round-100" (r102 closure erratum); header gaps: 14/24 `corpus/knowledge/*.md` lack `source:`/`verified-at:`/`recheck:` in lines 1–3 (dossier D6) | Q10 | every admitted entry opens with source:/verified-at:/recheck:; every cited artifact is opened in-round and located with a verbatim quote; every cited ID resolves to an existing file |

### Outside checks that disagreed with the gate

- **r16** — LOG.md:232 — "First independent `reports/r16-axis-adjudicator.md` verdict: **reject as submitted**"; a corrected re-adjudication followed.
- **r45** — LOG.md:768 — "first replayed only two controls, then after an explicit scope correction"; the verifier's first pass was narrower than the gate's need.
- **r53** — LOG.md:908 — "its “496 files (all corpus JSON plus checker)” is not the fixture-JSON count"; the verifier miscounted from fixtures-cwd argv.
- **r55** — LOG.md:950 — "seven no-go judgments and one scribe conditional-GO"; the scribe's conditional GO ran against seven no-gos; the adjudicator sided with the no-gos.
- **r89** — SCORECARD.md:356 — the closure gate admitted it; the r93 replay found calibration harm and reclassified the round.
- **r94** — SCORECARD.md:408-409 — "F15 bounded not re-rolled; F39 superseded by later-landing F04/F05; F40 not credited".
- **r96** — SCORECARD.md:480 — "V23's confirmed FAIL discharged at closure (foreign `c3red` scratch pin written by verifier V41's `--freeze` probe — removed)".
- **r97** — SCORECARD.md:544 — "r97's recorded V46 FAIL discharged — the exact r97 mutation bytes now exit 1 `REDUCTION-DETECTED`".
- **r99** — SCORECARD.md:582 — "eleven standing FAILs recorded, none re-rolled".
- **r100** — SCORECARD.md:616 — "V15/V18/V20 FAILs discharged or bounded, none re-rolled".

## Gate

Round 103 gate, run by L1 lore against `corpus/QUALITY.md` Q01–Q10 (2026-10-19). Every decision below names its criterion and evidence. Receipts live under `.ufo/waves/round-103/seats/`.

### Candidates considered

- 3 knowledge entries: `r103-aliases-and-name-variants.md` (CM-a), `r103-in-world-dating-and-uncertain-time.md` (CM-c), `r103-canon-status-and-supersession.md` (CM-e) — seats R103EntryAliases, R103EntryDating, R103EntryCanon.
- 32 source rows drafted (19 by seat R103Sources3, 13 by the entry seats); 31 were opened and became registry rows, 1 (Allen 1983) was never opened and became a lead. The SOURCES seat ran three times: R103Sources and R103Sources2 died on provider capacity (`resource_exhausted`, `turn_rate_limit_exceeded`) before writing; R103Sources3 wrote the file.

### Admitted

- **`corpus/knowledge/r103-in-world-dating-and-uncertain-time.md` (CM-c).** Q06: sealed comparison qC2 DIFFERENT — with the entry, relative time ("third winter after the Salt Accord") becomes a `depends_on` edge to the Salt Accord event; the sealed baseline reader kept it as prose only (`R103SealedC-baseline.md` vs `R103SealedC-proposal.md`; adjudication `R103Adjudicator.md`). Q01/Q04/Q07: no checker change, editorial bounds labelled editorial, uncertainty never collapsed to a point. Q10: opens with the header triplet; cites S020–S023 (tier A, mined, opened in-round). Q09: cited lane paths resolve (re-checked at merge). Self-check: `R103EntryDating-rows.md` `## Q01–Q10 self-check`.
- **`corpus/knowledge/r103-canon-status-and-supersession.md` (CM-e).** Q06: qE2 DIFFERENT (an in-world amendment is encoded as its own sourced declaration citing the declaring record, where the baseline put it only in an event description) and qE5 DIFFERENT (tier order only by a declared convention record, where the baseline only deferred to L0). Q01/Q02: no tier is enforced without a declared convention; a `superseded` label never authenticates itself. Q10: cites S024, S026 (tier A), S025 (tier B), S027 (tier C, illustration only, never sole support). Self-check: `R103EntryCanon-rows.md`.

### Rejected

- **`r103-aliases-and-name-variants.md` (CM-a) — rejected under Q06.** The sealed comparison graded all five questions SAME (qA1–qA5): without the entry, the baseline reader already kept both homonyms, recorded the alias as a sourced claim, refused identity transfer and left the checker alone — the r82 pattern (LOG.md:1530). The entry's method was sound (SKOS, Wikibase, TEI; no repeat of the r4 homonym harm), but it changed no action, so it is not admitted. Preserved, not deleted, at `.ufo/waves/round-103/rejected/r103-aliases-and-name-variants.md`; its four source rows (S028–S031) stay `queued` with no `used-by`. Flip: a seeded case on which the base corpus decides wrongly (e.g. a cluster where a name variant must be distinguished from a distinct homonym under a declared uniqueness convention).
- **Source rows S015, S016, S017 — rejected for the scope named in each row** (WGA MBA as a world-bible standard; LongStoryEval as a continuity source; the ConStory-Checker model judge as canon authority). Reasons and flips are in their `teaches` cells.
- **Allen 1983 (dl.acm.org, HTTP 403) — not a row.** The seat drafted it as a rejected row; L1 moved it to `## Leads (unopened)` because contract rule 1 forbids a row for an unopened source.

### Merge decisions (L1, before first commit)

- Placeholder ids renumbered: SXC1–SXC4 → S020–S023; SXE1–SXE4 → S024–S027; SXA1–SXA4 → S028–S031.
- S025 (Wikidata Help:Ranking) re-tiered A → B: community-maintained project help, strong secondary for rank practice.
- S028–S031 drafted `mined` → `queued`, `used-by` → `—`: the entry they served was rejected.
- No row of an existing registry changed (the registry is new this round).

### Where the gate learned before landing

- **Q06 carve-out removed.** The pre-registration critic (`R103Critic-pre.md` item 4) showed the declared Q06 exempted uncovered ground from the decision-delta test, which would have recreated r82. Q06 was rewritten to apply on any ground before any entry was judged, and the sealed comparison was dispatched because of it. That comparison then rejected one of three candidates.
- **"Leaves undecided" made precise — after the results, in the stricter direction (disclosed).** The adjudicator counted 8/15 baseline answers as `own judgment` that matched the proposal anyway and graded them SAME under the r82 precedent. Q06's earlier wording ("…or leaves undecided") would have let the CM-a entry pass on those answers. Q06 was reworded after the sealed results to match the adjudication (an own-judgment match is SAME; explicitness is not a delta). The change is stricter, never looser: it rejected one candidate and changed no admit — CM-c (qC2) and CM-e (qE2, qE5) carry DIFFERENT questions under both readings (`R103Adjudicator.md`). The post-landing critic flagged the timing (`R103CriticPost.md`, C2); the non-author spot-check should rule on it.

### Source gate records (contract rule 1 — URL, access date, located quote ≤25 words)

- S001 — https://www.w3.org/TR/prov-o/ — accessed 2026-10-19 — "An prov:Entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary." (§3.1 Starting Point Terms)
- S002 — https://json-schema.org/draft/2020-12/json-schema-validation — accessed 2026-10-19 — "An object instance is valid against this keyword if every item in the array is the name of a property in the instance." (§6.5.3 required)
- S003 — https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter — accessed 2026-10-19 — "A complete topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph." (class graphlib.TopologicalSorter, intro paragraph)
- S004 — https://etcsl.orinst.ox.ac.uk/section1/tr141.htm — accessed 2026-10-19 — "When she entered the seventh gate, the pala dress, the garment of ladyship, was removed from her body." (lines 159-163)
- S005 — https://www.gutenberg.org/ebooks/53080 — accessed 2026-10-19 — "He called out “Earth,” and the solid land appeared." (Ch. V Myths of the Maya, The Creation-Story, printed p. 209; Gutenberg HTML pg53080-images.html)
- S006 — https://terebess.hu/english/kojiki.html — accessed 2026-10-19 — "closed behind her the door of the Heavenly Rock-Dwelling, made it fast and retired." (Part III, The Door of the Heavenly Rock-Dwelling, first sentence)
- S007 — https://doc.wikimedia.org/Wikibase/master/php/docs_topics_constraints.html — accessed 2026-10-19 — "it is not a violation of data integrity if an entity contains a “broken” reference." (Soft Constraints, second NOTE)
- S008 — https://www.w3.org/TR/2017/REC-shacl-20170720/ — accessed 2026-10-19 — "Conformance checking produces true if and only if a given focus node conforms to a given shape, and false otherwise." (§3.5 Conformance Checking)
- S009 — https://aclanthology.org/2024.naacl-long.391/ — accessed 2026-10-19 — "temporal relations such as after and before are mutually exclusive for any pair of events" (Abstract)
- S010 — https://aclanthology.org/2022.findings-emnlp.526/ — accessed 2026-10-19 — "A reader model infers what a human reader believes about the concepts, entities, and relations about the fictional storyworld." (Abstract, PDF p. 1)
- S011 — https://arxiv.org/abs/2504.11900 — accessed 2026-10-19 — "inconsistencies in a storyline that break the internal logic or rules of a story's world" (Abstract)
- S012 — https://arxiv.org/html/2603.05890 — accessed 2026-10-19 — "The taxonomy comprises five top-level categories and 19 fine-grained error types" (§2.2 Consistency Error Taxonomy, arXiv HTML)
- S013 — https://www.wgfoundation.org/blog/2021/11/17/serialized-drama — accessed 2026-10-19 — "Episodes might have some self-contained elements, but for the most part, they’re pieces or fragments of a much bigger season and series narrative." (opening section)
- S014 — https://www.wgfoundation.org/blog/our-online-exhibits-broadcast-quality — accessed 2026-10-19 — "to the show bible for THE WIRE, where McNulty is referred to as McArdle" (exhibit paragraph after ALL IN THE FAMILY)
- S015 — https://www.wga.org/contracts/contracts/mba — accessed 2026-10-19 — "The MBA is the collective bargaining agreement that covers most of the work done by WGA writers." (page body, first paragraph)
- S016 — https://aclanthology.org/2025.acl-long.799/ — accessed 2026-10-19 — "we propose an evaluation criteria structure and conduct experiments to identify the most significant aspects among the 8 top-level criteria" (Abstract)
- S017 — https://arxiv.org/html/2603.05890 — accessed 2026-10-19 — "an automated LLM-as-judge pipeline for scalable and auditable consistency evaluation" (§2.3 Automated Error Detection Pipeline)
- S018 — corpus/fixtures/check_bible.py (base 6cec83a) — accessed 2026-10-19 — "CLEAN: schema, citations, relations, timeline; 0 violations" (`python3 -B corpus/fixtures/check_bible.py corpus/fixtures/consistent`, exit 0; `... corpus/fixtures/contradictions` printed "3 violation(s); no canon changed", exit 1)
- S019 — corpus/tools/dependency_freeze.py (base 6cec83a) — accessed 2026-10-19 — "FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1" then "RESULT PASS" (`python3 -B corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review`, exit 0)
- S020 — https://www.w3.org/TR/owl-time/ — accessed 2026-10-19 — "Time positions and durations may be expressed using either the conventional (Gregorian) calendar and clock, or using another temporal reference system" (abstract, CRD 2022-11-15).
- S021 — https://www.loc.gov/standards/datetime/ — accessed 2026-10-19 via Wayback capture 2024-12-31 (live page HTTP 403) — "The characters '?', '~' and '%' are used to mean "uncertain", "approximate", and "uncertain" as well as "approximate", respectively" (Level 1, Qualification of a date).
- S022 — https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.datable.html — accessed 2026-10-19 — "@when-custom @notBefore-custom @notAfter-custom @from-custom @to-custom @datingPoint @datingMethod" (Attributes row, att.datable.custom listing).
- S023 — https://www.iso.org/standard/70908.html — accessed 2026-10-19 (the recheck seat found the live page behind a bot challenge and re-verified the quote in Wayback capture 20241230054021) — "This document excludes the representation of date elements from non-Gregorian calendars, or times not from the 24-hour clock." (abstract).
- S024 — https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer — accessed 2026-10-19 — "Wikibase will not be about the truth, but about statements and their references." (§Statements, requirement quote)
- S025 — https://www.wikidata.org/wiki/Help:Ranking — accessed 2026-10-19 — "Marking erroneous statements as deprecated instead of simply deleting such statements has three benefits" (§Deprecated rank)
- S026 — https://www.w3.org/TR/prov-dm/ — accessed 2026-10-19 — "Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity." (§5.1.8)
- S027 — https://en.wikipedia.org/wiki/Star_Wars_expanded_to_other_media — accessed 2026-10-19 — "The Holocron was divided into five levels of canon (in order of precedence)" (§Holocron database and canonicity)
- S028 — https://www.w3.org/TR/2009/REC-skos-reference-20090818/ — accessed 2026-10-19 — "A resource has no more than one value of skos:prefLabel per language tag." (§5.4 Integrity Conditions, S14)
- S029 — https://www.mediawiki.org/wiki/Wikibase/DataModel — accessed 2026-10-19 — "for any given language, an EntityDescription may have at most one label and at most one description, but any number of aliases" (EntityDescription, lexical-information paragraph)
- S030 — https://tei-c.org/release/doc/tei-p5-doc/en/html/ND.html — accessed 2026-10-19 — "resp (responsible party) indicates the agency responsible for the intervention or interpretation" (§14.1.1, attribute definitions)
- S031 — https://www.wikidata.org/wiki/Help:Aliases — accessed 2026-10-19 — "Aliases are alternative names, like nicknames, acronyms, or translations" (lead paragraph, nutshell box context)

### Spot-check

Pending: a non-author (the orchestrator) spot-checks ≥1 admit and ≥1 reject after the round lands (`corpus/QUALITY.md` `## Admission procedure` step 4). The lane's own critic, adjudicator and reviewer seats are still the lane (LEARNING.md "Discernment is checked from outside") and are not counted as the spot-check.


## Post-review corrections (round 103, 2026-10-19 — appended; everything above stands)

Trigger: the orchestrator's adjudication after landing (a non-author reviewer reproduced the counts and held for corrections; a non-author critic would reject as claimed). Work commits under review: `33173138`, `74384c94`.

### Mistakes (appended)

| M## | class | evidence pointer (file:line + verbatim fragment) | captured-by criterion | fix |
|---|---|---|---|---|
| M11 | Criterion rewritten in place after results: a gate criterion edited once the outcomes it would decide were known | corpus/QUALITY.md Q06 at `33173138` — "Explicitness is not a delta" — wording added after `.ufo/waves/round-103/seats/R103Adjudicator.md:25` counted 8/15 own-judgment answers | Q11 (supersedes Q06; restoration note in corpus/QUALITY.md) | criteria are frozen before a gate runs; a change after results is a new row naming the row it replaces, dated, with its direction (stricter or looser) stated |
| M12 | Gate applied the encoding bar to fixture data but not to a method entry's own rules | `.ufo/waves/round-103/rejected/r103-in-world-dating-and-uncertain-time.md:30` — "a `depends_on` edge (or an existing event reference) gives precedence"; the field means "prerequisite → event" (`corpus/knowledge/2026-10-12-lore-decision-table.md:19`) | Q13 (supersedes Q04) | every rule an entry tells authors to encode is checked against the declared meaning of the field it writes |
| M13 | Line-anchor drift from an in-ledger insertion | `74384c94` inserted `SCORECARD.md:80` (capability row), so every cited SCORECARD line ≥80 moved down by one, including the five in M07/M08 | Q12 (supersedes Q09) | append below cited content; after any insertion, re-resolve every `file:N` anchor into that file |

### Corrected pointers (appended; the original cells above stand)

Cause: M13. Each fragment was re-printed at the new line on `74384c94`.

| where cited | was | now | fragment at the new line |
|---|---|---|---|
| lesson M07 (and QUALITY Q07) | SCORECARD.md:356 | SCORECARD.md:357 | "r89 calibration is **harmed**" |
| lesson M08 | SCORECARD.md:383 | SCORECARD.md:384 | "32 tool-terminal `completed` labels do not mean 32 usable reviews" |
| lesson M08 (and QUALITY Q08) | SCORECARD.md:600 | SCORECARD.md:601 | "ROSTER ERRATUM (recorded append-only in LOG)" |
| lesson M08 (and QUALITY Q08) | SCORECARD.md:634 | SCORECARD.md:636 | "declared 28, dispatched" (the R103Reviewer-pre seat already had 634 one line early, SHIFTED(635), before the insertion) |
| lesson M08 (and QUALITY Q08) | SCORECARD.md:667 | SCORECARD.md:668 | "ROSTER ERRATUM (third of" |
| outside checks r89 / r94 / r96 / r97 / r99 / r100 | SCORECARD.md:356, 408-409, 480, 544, 582, 616 | SCORECARD.md:357, 409-410, 481, 545, 583, 617 | same fragments as quoted in `### Outside checks that disagreed with the gate` |

### Q06 history and the re-grade against the final bar

`corpus/QUALITY.md` Q06 is restored to its first text. Q11 supersedes it with the post-results wording, which is stricter. Q13 supersedes Q04. Re-grade of all 15 sealed questions under Q11 and Q13 (receipts: `.ufo/waves/round-103/seats/R103Sealed{A,C,E}-{baseline,proposal}.md`; first grades: `R103Adjudicator.md`):

| q | first grade | final grade | reason |
|---|---|---|---|
| qA1–qA5 | SAME ×5 | SAME ×5 | unchanged; no record, checker or routing difference |
| qC1, qC3, qC4, qC5 | SAME | SAME | unchanged |
| qC2 | DIFFERENT | SAME (proposal action fails Q13) | the proposal's `depends_on` edge to the Salt Accord encodes a prerequisite the chronicle does not state; under the corrected rule the action is the baseline's (phrase kept, no edge) |
| qE1, qE3, qE4 | SAME | SAME | unchanged |
| qE2 | DIFFERENT | DIFFERENT | a separate sourced declaration citing `docket-2`; the excerpt "entry 1 amended" supports it; the field stays within its meaning (Q13) |
| qE5 | DIFFERENT | DIFFERENT (not decisive) | a declared editorial convention record; acceptable only when labelled editorial (Q13), so admission rests on qE2 |

Result under the final bar: CM-a **rejected** (unchanged); CM-c **rejected** (was admitted); CM-e **admitted** (qE2 decisive). Under the first Q06 text the outcome is the same, because the CM-c change comes from Q13, not from the Q06 wording.

### CM-c rejection (append-only record)

- The entry moved by `git mv` from `corpus/knowledge/` to `.ufo/waves/round-103/rejected/r103-in-world-dating-and-uncertain-time.md`, with an appended rejection section. Bytes and history are kept.
- `SKILL.md:27` was replaced in place by a WITHDRAWN row with the corrected guidance. This is the one non-append edit of this pass. Inserting a correction row would have shifted every later SKILL line anchor (M13); leaving the row would have left a falsified rule standing (PROTOCOL.md §Evidence standard, "Corrections sweep every mention"). The withdrawn row's verbatim text (pipes escaped `\|` only):

  \| A source dates an event in a named in-world calendar, approximately, or relative to another event \| Keep the date string verbatim in the sourced claim, naming its calendar; never convert between calendars or into a tick without a sourced in-world correlation. Relative time ("three winters after X") becomes a `depends_on` edge to X's existing event id (it must resolve and sit at an earlier tick), never a tick-gap magnitude. Uncertain dates get editorial-labelled bounds in the clause map only — never a point, never a new timeline field. \| `corpus/knowledge/r103-in-world-dating-and-uncertain-time.md:21-31` (CM-c). \|

- Downstream corrections are appended: `corpus/README.md` `## Coverage map corrections`, `PROVINCE.md` (last Corrections bullet), `corpus/SOURCES.md` (Paths correction bullet), `SCORECARD.md`, `LOG.md`.

### SOURCES cell changes (contract rule 2, logged old → new)

| row | cell | old | new | reason |
|---|---|---|---|---|
| S020, S021, S022, S023 | status | mined | queued | their only citing entry (CM-c) was rejected |
| S020, S021, S022, S023 | used-by | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md | — | path no longer in corpus/knowledge |
| S023 | recheck | annual | 365d | cadence normalised to the census form |

New row **S032** (`supersedes S023 —`). Gate record:

- S032 — https://www.iso.org/standard/70908.html — accessed 2026-10-19 via Wayback captures 20241230054021 and 20260102081905 (live page behind a bot challenge) — "This publication was last reviewed and confirmed in 2024. Therefore this version remains current." (General information / lifecycle, both captures)

S023's anchor "confirmed 2024-12-05" appears in neither capture. The 2026-01-02 capture shows "ISO 8601-2:2019/Amd 1:2025", so the seat's first "Amendment 1:2025 noted" was supported by the later page. The pre-commit rewrite to "Amd 1 under development" described the 2024 capture only. S032 records both.

**S012 and S017** share `https://arxiv.org/html/2603.05890` and both stand: they have different scopes (§2.2 taxonomy, tier A, queued; §2.3 LLM judge as canon authority, tier C, rejected). The fleet census flags S017 E04, and append-only rule 2 forbids editing S017's source cell; the explanation is in `corpus/SOURCES.md` `## Search log`.

**S027** (tier C, mined; census W01) is not sole support for any admitted entry: CM-e's tier rule rests on Q01 and S025 (appended correction in `corpus/knowledge/r103-canon-status-and-supersession.md`).

Census: `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate .` from the lane root prints `E04 S017` and `W01 S027` and exits 1. Both findings are explained above; no other finding is printed.

### Q01 and Q05 test commands — first text (pre-commit spelling repairs, meaning unchanged)

- Q01 test, first text: enumerate the checker's fail classes — `grep -nE 'VIOLATION\|sys.exit\|exit\(' corpus/fixtures/check_bible.py` — each must name its declared convention; a name/alias-style predicate has none, so it may only warn or become an L0 question
- Q05 test, first text: the candidate names its sweep pattern; replay it — e.g. `grep -nE 'already (exercised\|admitted\|corrected)\|prior art' LOG.md` — and confirm no hit repeats the claim

(Pipes are escaped `\|` here only. The repairs replaced in-cell `|` alternation, which split the table columns, with `grep -e` forms.)

### C1 restated

C1 (coverage) is credited only with work a reader can verify without C2 or C3: the coverage map (0 → 19 rows; all `verify` cells replay their stated exits), `## Frontier` (0 → 1, 5 rows, plus CM-c returned), and PROVINCE Core/Frontier/Adjacent (0 → 3). The admission (now CM-e only) is a joint C1+C2+C3 outcome and is not credited to C1.

### Spot-check (post-review)

The orchestrator's non-author reviewer and critic reviewed this round after landing. They disagreed with the gate on one admit (CM-c). That disagreement is learned here as M12 → Q13, and as M11 → Q11 for the post-results wording. The required non-author spot-check of ≥1 admit (CM-e) and ≥1 reject (CM-a or CM-c) on the corrected record remains the orchestrator's.
