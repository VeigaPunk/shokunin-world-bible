# R103EntryAliases — SOURCES rows, gate record, search log (CM-a)

Seat: W2RoundLore.R103EntryAliases, 2026-10-19. Every row below was opened
by me this session (`curl -sL`, content greps over the fetched HTML).
Placeholder ids SXA1–SXA4 are for L1 to renumber to S### at merge.

## Rows (11-column contract format)

| id | source (title — URL) | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| SXA1 | SKOS Simple Knowledge Organization System Reference — https://www.w3.org/TR/2009/REC-skos-reference-20090818/ | spec | A | lexical label roles, preferred-vs-alternate separation, label integrity conditions | §5 Lexical Labels, §5.4 integrity conditions S13–S14, §6.5.3 notation convention; W3C REC 2009-08-18 | One preferred label per resource per language tag; alternates and hidden labels are disjoint properties; uniqueness across resources exists only where a scheme declares it (notations), never for prefLabel | mined | 2026-10-19 | on-release | corpus/knowledge/r103-aliases-and-name-variants.md |
| SXA2 | Wikibase DataModel — https://www.mediawiki.org/wiki/Wikibase/DataModel | docs | A | entity lexical model: labels, descriptions, aliases | EntityDescription section, "labels, descriptions, and aliases" paragraph; current page opened 2026-10-19 | At most one label and one description per language but any number of aliases; label+description is the per-language key, so shared labels are legal and names alone are not keys | mined | 2026-10-19 | 90d | corpus/knowledge/r103-aliases-and-name-variants.md |
| SXA3 | TEI P5 Guidelines, ch. 14 Names, Dates, People, and Places — https://tei-c.org/release/doc/tei-p5-doc/en/html/ND.html | spec | A | encoding multiple name forms on one referent, attribution and certainty of names | ch. 14 §14.1.1 att.global.responsibility (resp, cert), §14.2 persName/placeName @type; version 4.12.0, rev 113e933e2, updated 2026-07-28 | Name elements carry @type for variant kinds and inherit cert/resp/source so each name assertion can record its agent and certainty; two bearers keep separate records | mined | 2026-10-19 | on-release | corpus/knowledge/r103-aliases-and-name-variants.md |
| SXA4 | Wikidata Help:Aliases — https://www.wikidata.org/wiki/Help:Aliases | community | C | operational alias intake practice | lead paragraphs, "Aliases" section; current page opened 2026-10-19 | Community corroboration that aliases are alternative names (nicknames, acronyms, translations), searched like labels but unlimited per item; never sole support | mined | 2026-10-19 | 90d | corpus/knowledge/r103-aliases-and-name-variants.md |

## Gate (record per new row)

- SXA1 — https://www.w3.org/TR/2009/REC-skos-reference-20090818/ — accessed 2026-10-19 — "A resource has no more than one value of skos:prefLabel per language tag." (§5.4 Integrity Conditions, S14)
- SXA2 — https://www.mediawiki.org/wiki/Wikibase/DataModel — accessed 2026-10-19 — "for any given language, an EntityDescription may have at most one label and at most one description, but any number of aliases" (EntityDescription, lexical-information paragraph)
- SXA3 — https://tei-c.org/release/doc/tei-p5-doc/en/html/ND.html — accessed 2026-10-19 — "resp (responsible party) indicates the agency responsible for the intervention or interpretation" (§14.1.1, attribute definitions)
- SXA4 — https://www.wikidata.org/wiki/Help:Aliases — accessed 2026-10-19 — "Aliases are alternative names, like nicknames, acronyms, or translations" (lead paragraph, nutshell box context)

## Search log

Question: how do mature knowledge-organization, wiki and text-encoding
systems record preferred names, alternate names and homonyms — and where
do they place the uniqueness burden? Query terms: "SKOS prefLabel altLabel
integrity condition", "Wikibase labels descriptions aliases data model",
"TEI P5 persName placeName multiple names cert resp", "Wikidata help
aliases". Where searched: primary spec/docs pages named in the L1 task
prompt, opened directly via `curl` on 2026-10-19 (no search engine; the
candidate list was given). Identified 4, screened 4 (all fetched and grepped
for the named sections), included 4, excluded 0. The TEI chapter is
numbered 14 (not 13) in the current 4.12.0 release — recorded in the entry.
A fifth candidate, the legacy SKOS Primer, was not needed: the Reference
itself carries S13/S14 and the notation-uniqueness convention. Stop
rationale: the three tier-A models converge on the same shape —
preferred/alternate split is a schema-level distinction, while cross-record
name uniqueness is always a declared scheme convention, never a data-model
default — which is exactly the boundary the r4 rejection needs. Further
sources would add instances, not distinctions.

## Self-check (Q01–Q10)

- Q01 convention-backed hard rules: the entry fails nothing; homonyms are
  warn-class only where a declared convention exists (none does), matching
  r4 (LOG.md:52-55).
- Q02 no self-authentication: name/ID/label never confer provenance or
  identity; R10 referent+field+occasion restated for the `name` field.
- Q03 reports stay attributed: each alternate name is its own sourced
  `claims` row; unattributed aliases are not admitted.
- Q04 encoding ≤ excerpt: every claim row still requires a mapped
  source_id; the editorial `name` choice is labelled editorial and
  reversible.
- Q05 prior-art sweep: r4 rejection, retired line (SCORECARD.md:14),
  L0 question and R10 all cited; the sweep command is in §Decision delta.
- Q06 decision delta: names the three unsettled decisions and the negative
  sweep output (9 hits, all records of absence) on this tree.
- Q07 definite stays definite: findings are definite (schema has no alias
  field; checker has no warn channel, `check_bible.py:423-427`); the only
  deferred question is the L0-owned warn-vs-convention design, named.
- Q08 counts from receipts: all counts (9 sweep hits, 428-line checker,
  cited line numbers) were computed on this worktree 2026-10-19.
- Q09 durable citations: every lane citation is a tracked
  lane-root-relative path; no `*-scratch/` or `.shokunin/lore/` cites; the
  three kotodama paths were existence-checked at fleet root.
- Q10 opened, tiered, headed sources: entry opens with the 4 contract
  lines; cites SXA1–SXA3 (tier A, opened in-round, ≤25-word located quotes
  in §Gate); SXA4 is tier C and cited only as corroboration, never sole
  support; external art informs method, never canon (§Scope limits, F4).
