# R103EntryDating — seat outputs (CM-c: in-world dating and uncertain time)

Entry written: `corpus/knowledge/r103-in-world-dating-and-uncertain-time.md` (93 lines, coverage-row: CM-c).

## SOURCES rows (placeholder ids; L1 renumbers to S### at merge)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| SXC1 | Time Ontology in OWL — https://www.w3.org/TR/owl-time/ | spec | A | temporal reference systems and interval ordering for in-world date claims | Abstract + TRS section + :hasTRS; W3C CRD 2022-11-15 (latest version page opened 2026-10-19) | A temporal position may name a non-Gregorian temporal reference system; ordering relations are separable from calendar position, so a fictional calendar is a per-claim TRS tag, never a silent conversion | mined | 2026-10-19 | on-release | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md |
| SXC2 | Extended Date/Time Format (EDTF) Specification — https://www.loc.gov/standards/datetime/ | spec | A | encoding uncertain, approximate, and unspecified dates | "Differences" + "Level 1" + "Level 2" sections; spec dated 2019-02-04; live loc.gov returned HTTP 403, opened via Wayback capture 2024-12-31 | Uncertainty qualifiers ('?' '~' '%'), unspecified digits ('X'), and open or unknown interval ends ('..' / null) keep doubt inside the value instead of forcing a point | mined | 2026-10-19 | 180d | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md |
| SXC3 | TEI P5 att.datable — https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.datable.html | docs | A | bound attributes and non-Gregorian dating for recorded dates | Attribute table + class note; TEI P5 version 4.12.0, revision 113e933e2 (generated 2026-07-28) | @when, @notBefore, @notAfter, @from, @to give a bound-pair shape for editorial bounds; att.datable.custom (@when-custom, @datingMethod, @datingPoint) shows dating claims carry their own calendar/method name | mined | 2026-10-19 | on-release | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md |
| SXC4 | ISO 8601-2:2019 Date and time — Representations for information interchange — Part 2: Extensions — https://www.iso.org/standard/70908.html | spec | A | current scope and exclusions of date-time interchange extensions | Abstract + lifecycle; published 2019-02, confirmed current 2024-12-05, Amendment 1:2025 noted | The standard extends to uncertain/approximate dates and unspecified portions while explicitly excluding non-Gregorian calendar elements — an authoritative precedent for refusing silent calendar conversion | mined | 2026-10-19 | annual | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md |
| SXC5 | Maintaining Knowledge about Temporal Intervals (Allen 1983, CACM 26(11)) — https://dl.acm.org/doi/10.1145/182.358434 | paper | A | interval algebra for event ordering | DOI landing page | REJECTED: ACM landing page returned HTTP 403 in this environment on 2026-10-19; no content was read; the entry's ordering claims rest on OWL-Time's abstract instead. flip: a reachable ACM page or an openly readable copy of the same paper | rejected | 2026-10-19 | on-release | — |

## Gate

- SXC1 — https://www.w3.org/TR/owl-time/ — accessed 2026-10-19 — "Time positions and durations may be expressed using either the conventional (Gregorian) calendar and clock, or using another temporal reference system" (abstract, CRD 2022-11-15).
- SXC2 — https://www.loc.gov/standards/datetime/ — accessed 2026-10-19 via Wayback capture 2024-12-31 (live page HTTP 403) — "The characters '?', '~' and '%' are used to mean "uncertain", "approximate", and "uncertain" as well as "approximate", respectively" (Level 1, Qualification of a date).
- SXC3 — https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.datable.html — accessed 2026-10-19 — "@when-custom @notBefore-custom @notAfter-custom @from-custom @to-custom @datingPoint @datingMethod" (Attributes row, att.datable.custom listing).
- SXC4 — https://www.iso.org/standard/70908.html — accessed 2026-10-19 — "This document excludes the representation of date elements from non-Gregorian calendars, or times not from the 24-hour clock." (abstract).
- SXC5 — no gate line: not opened (HTTP 403); recorded as a rejected row, not evidence.

## Search log (one note)

Question: how should a world-bible timeline record sourced in-world dates, competing calendars, and uncertain or relative time without overreach? Query terms: OWL-Time, temporal reference system, EDTF, uncertain date encoding, TEI datable, Allen interval algebra. Searched: direct opens of w3.org, loc.gov, tei-c.org, iso.org, dl.acm.org on 2026-10-19. Identified 5 primary candidates; screened 5; included 4; excluded/blocked 1 (Allen 1983 — HTTP 403 at dl.acm.org, no content read). loc.gov blocked live fetch (HTTP 403); the identical spec text was read via a 2024-12-31 Wayback capture and the canonical URL is cited as the source. Stop rationale: three orthogonal authorities (TRS naming, uncertainty-preserving syntax, bound attributes) plus one scoping exclusion are sufficient for the decision table; the negative local sweep (`grep -rniE 'calendar|notBefore|notAfter|EDTF|dating system|era name' corpus/knowledge/ corpus/README.md SKILL.md PROVINCE.md` → 2 inert hits) confirms no competing local convention to reconcile.

## Q01–Q10 self-check

- Q01 convention-backed hard rules: PASS — entry adds no predicate; it explains why no checker change is justified (no obligatory convention, M1 class avoided).
- Q02 no self-authentication: PASS — every claim cites an opened tier-A source or an observed command output; placeholder ids are not proof of anything.
- Q03 reports stay attributed: PASS — competing dates and relative phrases are encoded only as attributed claims; no resolution, merge, or winner.
- Q04 encoding ≤ excerpt: PASS — tick is declared an editorial ordinal; uncertain dates keep editorial bounds labelled editorial; verbatim date strings preserved in sourced claim text.
- Q05 prior-art sweep: PASS — negative sweep command and observed 2-hit output recorded in the entry; decision-table:17-18 and LOG.md:1271-1272 cited as the prior art.
- Q06 decision delta: PASS — uncovered-ground clause used: one concrete decision settled (how to encode named-calendar, uncertain, competing, and relative dates) with the negative sweep; checker unchanged because no fixture exercises a named calendar (M6).
- Q07 definite stays definite: PASS — uncertainty preserved rather than qualified-away; the undecidable input is named (absence of a sourced unit correlation or calendar correlation).
- Q08 counts from receipts: PASS — every cited path was opened/read this session; sweep outputs transcribed from actual runs; no closure counts claimed.
- Q09 durable citations: PASS — all cited paths are tracked, lane-root-relative (or fleet-worktree-relative for the two verified kotodama files); no scratch or transient paths.
- Q10 opened, tiered, headed sources: PASS — 4 header lines present; four tier-A rows opened this session each carry a located ≤25-word verbatim quote; no tier-C or community source is sole support; outside art informs method only, never in-world canon.
