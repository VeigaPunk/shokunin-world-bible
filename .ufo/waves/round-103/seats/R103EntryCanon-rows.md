# R103EntryCanon — CM-e seat output (rows, gate records, search log, self-check)

Delivered file: `corpus/knowledge/r103-canon-status-and-supersession.md` (new, 95 lines).
Coverage row: CM-e — canon tiers, retcons, supersession of in-world records.
All four sources were opened in this session on 2026-10-19 (Wikibase Primer via
mediawiki.org reader, Help:Ranking via wikidata.org reader, PROV-DM via w3.org
plus a local curl + section extraction for the full REC text, Wikipedia article
via Wikipedia API). Placeholder ids SXE1–SXE4 are for L1 renumbering to S### at merge.

## SOURCES.md rows (11 columns; append to Registry after renumber)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| SXE1 | Wikibase DataModel Primer — https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer | docs | A | statement ranks; references vs truth in structured claims | §Statements and §Ranks, oldid 8399774 | A knowledge base models attributed statements, not truth; preferred/normal/deprecated ranks select query-visible values while deprecated statements stay listed for completion | mined | 2026-10-19 | 180d | corpus/knowledge/r103-canon-status-and-supersession.md |
| SXE2 | Help:Ranking — https://www.wikidata.org/wiki/Help:Ranking | docs | A | Wikidata rank usage and deprecation policy | §What ranks are not and §Deprecated rank, accessed 2026-10-19 | Deprecated statements are retained rather than deleted (three named benefits); ranks express consensus and are not a way of asserting a view on a disputed value | mined | 2026-10-19 | 180d | corpus/knowledge/r103-canon-status-and-supersession.md |
| SXE3 | PROV-DM: The PROV Data Model — https://www.w3.org/TR/prov-dm/ | spec | A | provenance relations revision, invalidation, alternate, specialization | §5.1.8 Invalidation, §5.2.2 Revision, §5.5.2 Alternate; REC-prov-dm-20130430 | Revision names a derived revised version coexisting with its original; invalidation marks an entity's end by an activity; alternateOf models two accounts of one thing | mined | 2026-10-19 | 180d | corpus/knowledge/r103-canon-status-and-supersession.md |
| SXE4 | Star Wars in other media — https://en.wikipedia.org/wiki/Star_Wars_expanded_to_other_media | community | C | illustration: declared canon-tier conventions | §Holocron database and canonicity, accessed 2026-10-19 | Canon tiers exist only as owner declarations (Holocron five levels; 2014 non-canonical rebranding), never derivable from content; illustration only, never sole support | mined | 2026-10-19 | 180d | corpus/knowledge/r103-canon-status-and-supersession.md |

Tier notes: SXE1–SXE3 are tier-A for their scopes only (official docs / W3C REC);
the tier is scoped, not global. SXE4 is a tertiary encyclopedia article marked
kind=community per contract vocabulary; it carries tier-C and is cited only as an
illustration, never as support for an in-world claim. All four rows were written
after opening the source this round.

## Gate records (for corpus/lessons/round-103.md ## Gate)

- SXE1 — https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer — accessed 2026-10-19 — "Wikibase will not be about the truth, but about statements and their references." (§Statements, requirement quote)
- SXE2 — https://www.wikidata.org/wiki/Help:Ranking — accessed 2026-10-19 — "Marking erroneous statements as deprecated instead of simply deleting such statements has three benefits" (§Deprecated rank)
- SXE3 — https://www.w3.org/TR/prov-dm/ — accessed 2026-10-19 — "Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity." (§5.1.8)
- SXE4 — https://en.wikipedia.org/wiki/Star_Wars_expanded_to_other_media — accessed 2026-10-19 — "The Holocron was divided into five levels of canon (in order of precedence)" (§Holocron database and canonicity)

## Search-log note

Question: how should an append-only world bible encode canon tiers, retcons and
declared supersession of in-world records (CM-e)? Searched: W1 ART dossier leads
plus direct primary sources — mediawiki.org, wikidata.org, w3.org (2026-10-19).
Identified 5 candidates; screened 5; opened 4 (Wikibase DataModel Primer,
Wikidata Help:Ranking, W3C PROV-DM REC, Wikipedia Star Wars in other media);
excluded 1 (Wookieepedia Star Wars Legends — HTTP 403 on fetch, community-tier
anyway, never required since tier-C may only illustrate). Included all 4 opened
sources. Stop rationale: two tier-A sources cover the retention/rank method and
one spec covers revision/invalidation/alternate semantics; one tier-C
illustration suffices for the declared-convention point, and community material
is never sole support. The failed fetch was recorded, not substituted.

## Q01–Q10 self-check

- Q01 convention-backed rules: table row 4 makes tier ordering binding only under a declared convention; absent one, warn/route, never fail. Check.
- Q02 no self-authentication: `superseded`/`retcon`/`deprecated` labels must cite a declaring source or declared convention; explicitly stated in table rows 2–3 and falsifier 3. Check.
- Q03 attributed reporting: identity, custody, and the declaration each carry their own source; stated in the R10 section. Check.
- Q04 encoding ≤ excerpt: editorial markers are labelled editorial and kept out of `sources.json` in-world rows. Check.
- Q05 prior-art sweep: negative sweep run before drafting (`grep -rniE 'retcon'` → 0; `canon[ -](tier|status)` → 0 in corpus); the entry cites the sweep command. Check.
- Q06 decision delta on uncovered ground: entry opens with the concrete unsettled decision (overwrite vs retain on contradictory/superseding records) plus sweep command and observed 0-hit output. Check.
- Q07 definite stays definite: undecidable inputs are named — undeclared conventions, absent declaring source — and routed to warn/L0 rather than asserted. Check.
- Q08 counts from receipts: all counts quoted (0 hits, ~100 lines, 4 rows) were measured this session; no closure counts claimed. Check.
- Q09 durable citations: every cited path is tracked and lane-root-relative (`corpus/fixtures/check_bible.py`, `corpus/knowledge/r88-…:93-97`, `corpus/knowledge/r101-…:25`, `corpus/tools/README.md:296`, SKILL registry `:102-103`); no `*-scratch/` or `.shokunin/` cites. Check.
- Q10 opened tiered headed sources: entry opens with `source:`/`verified-at:`/`recheck:`/`coverage-row:`; cites three tier-A rows opened this round with ≤25-word located quotes; tier-C SXE4 used as illustration only, never sole support; outside art informs method, never in-world canon. Check.
