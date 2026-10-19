# R103Sources3 — gate for corpus/SOURCES.md (round 103, 2026-10-19)

Seat: W2RoundLore.R103Sources3 (third SOURCES dispatch). Wrote `corpus/SOURCES.md` (new; S001-S019). Every row's source was opened by this seat on 2026-10-19. Rows reserved for sibling seats (SKOS 2009 REC, Wikibase DataModel and Primer, TEI ND and att.datable, Wikidata Help:Aliases and Help:Ranking, OWL-Time, LoC EDTF, ISO 8601 70908, PROV-DM, Wikipedia Star Wars expanded media, Allen 1983) were not written. Downloads went to /var/tmp/r103src.pZzk only.

## Gate

- S001 — https://www.w3.org/TR/prov-o/ — accessed 2026-10-19 — "An prov:Entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary." (§3.1 Starting Point Terms)
- S002 — https://json-schema.org/draft/2020-12/json-schema-validation — accessed 2026-10-19 — "An object instance is valid against this keyword if every item in the array is the name of a property in the instance." (§6.5.3 required)
- S003 — https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter — accessed 2026-10-19 — "A complete topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph." (class graphlib.TopologicalSorter, intro paragraph)
- S004 — https://etcsl.orinst.ox.ac.uk/section1/tr141.htm — accessed 2026-10-19 — "When she entered the seventh gate, the pala dress, the garment of ladyship, was removed from her body." (lines 159-163)
- S005 — https://www.gutenberg.org/ebooks/53080 — accessed 2026-10-19 — "He called out “Earth,” and the solid land appeared." (Ch. V Myths of the Maya, The Creation-Story, printed p. 209; Gutenberg HTML pg53080-images.html)
- S006 — https://terebess.hu/english/kojiki.html — accessed 2026-10-19 — "closed behind her the door of the Heavenly Rock-Dwelling, made it fast and retired." (Part III, The Door of the Heavenly Rock-Dwelling, first sentence)
- S007 — https://doc.wikimedia.org/Wikibase/master/php/docs_topics_constraints.html — accessed 2026-10-19 — "it is not a violation of data integrity if an entity contains a “broken” reference." (Soft Constraints, second NOTE)
- S008 — https://www.w3.org/TR/2017/REC-shacl-20170720/ — accessed 2026-10-19 — "Conformance checking produces true if and only if a given focus node conforms to a given shape, and false otherwise." (§3.5 Conformance Checking)
- S009 — https://aclanthology.org/2024.naacl-long.391/ — accessed 2026-10-19 — "temporal relations such as after and before are mutually exclusive for any pair of events" (Abstract)
- S010 — https://aclanthology.org/2022.findings-emnlp.526/ — accessed 2026-10-19 — "A reader model infers what a human reader believes about the concepts, entities, and relations about the fictional story world." (Abstract, PDF p. 1)
- S011 — https://arxiv.org/abs/2504.11900 — accessed 2026-10-19 — "inconsistencies in a storyline that break the internal logic or rules of a story's world" (Abstract)
- S012 — https://arxiv.org/abs/2603.05890 — accessed 2026-10-19 — "The taxonomy comprises five top-level categories and 19 fine-grained error types" (§2.2 Consistency Error Taxonomy, arXiv HTML)
- S013 — https://www.wgfoundation.org/blog/2021/11/17/serialized-drama — accessed 2026-10-19 — "Episodes might have some self-contained elements, but for the most part, they’re pieces or fragments of a much bigger season and series narrative." (opening section)
- S014 — https://www.wgfoundation.org/blog/our-online-exhibits-broadcast-quality — accessed 2026-10-19 — "to the show bible for THE WIRE, where McNulty is referred to as McArdle" (exhibit paragraph after ALL IN THE FAMILY)
- S015 — https://www.wga.org/contracts/contracts/mba — accessed 2026-10-19 — "The MBA is the collective bargaining agreement that covers most of the work done by WGA writers." (page body, first paragraph)
- S016 — https://aclanthology.org/2025.acl-long.799/ — accessed 2026-10-19 — "we propose an evaluation criteria structure and conduct experiments to identify the most significant aspects among the 8 top-level criteria" (Abstract)
- S017 — https://arxiv.org/html/2603.05890 — accessed 2026-10-19 — "an automated LLM-as-judge pipeline for scalable and auditable consistency evaluation" (§2.3 Automated Error Detection Pipeline)
- S018 — corpus/fixtures/check_bible.py (base 6cec83a) — accessed 2026-10-19 — "CLEAN: schema, citations, relations, timeline; 0 violations" (`python3 -B corpus/fixtures/check_bible.py corpus/fixtures/consistent`, exit 0; `... corpus/fixtures/contradictions` printed "3 violation(s); no canon changed", exit 1)
- S019 — corpus/tools/dependency_freeze.py (base 6cec83a) — accessed 2026-10-19 — "FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1" then "RESULT PASS" (`python3 -B corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review`, exit 0)

## Census

Run from the lane root (`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/lore-shokunin`) with the contract's commands verbatim, 2026-10-19:

```
$ rows
19
$ malformed
0
$ tier
A=14 B=2 C=3 
$ status
mined=8 queued=8 rejected=3 
$ dup
$ enum
$ missing
$ end
```

Duplicate ids, enum/tier-inflation violations and missing used-by paths printed nothing. Mined used-by paths were taken from `git grep -l <url-fragment> -- corpus SKILL.md` (S001-S006) and `git grep -l <tool>.py -- corpus/knowledge` (S018, S019).
