source: S020 — https://www.w3.org/TR/owl-time/ — abstract + §TRS + vocabulary :hasTRS, CRD 2022-11-15; S021 — https://www.loc.gov/standards/datetime/ — "Level 1" + "Level 2" sections, spec dated 2019-02-04 (opened via Wayback capture 2024-12-31; live loc.gov 403); S022 — https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.datable.html — attribute table + class note, TEI P5 4.12.0 rev 113e933e2; S023 — https://www.iso.org/standard/70908.html — abstract + lifecycle, ISO 8601-2:2019 confirmed 2024-12-05
verified-at: 2026-10-19
recheck: `grep -rniE 'calendar|notBefore|notAfter|EDTF|era' corpus/fixtures/check_bible.py` plus a path-existence check of every cited lane path; re-run whenever check_bible.py, the timeline schema, or any cited fixture changes; open-source recheck cadence 180d (S020 on-release, since the W3C draft is a moving Candidate Recommendation)
coverage-row: CM-c
# In-world dating, competing calendars, and uncertain time (r103, coverage row CM-c)

Coverage row **CM-c**: competing in-world dating systems, calendars, and uncertain or relative time — declared uncovered in `corpus/knowledge/2026-10-12-lore-decision-table.md:17-18` ("does not yet check … competing in-world dating systems"). This note is an editorial encoding method for the lane's `timeline.json`, not a new checker pass and not a canon claim.

## Decision this settles

Baseline problem: the timeline schema gives every event exactly one integer `tick` (`corpus/fixtures/check_bible.py:29`) and no date/calendar field, so an author encoding an in-world date had three silent failure paths: reuse `tick` as a year (overreach, the r71 lesson, LOG.md:1271-1272), silently translate between calendars, or drop the date. This entry settles one concrete decision the baseline leaves unsettled: **how to encode a sourced in-world date string, an uncertain date, a competing-calendar date, or a relative time without asserting more than the excerpt supports.**

Negative sweep (run 2026-10-19 from lane root):

```sh
grep -rniE 'calendar|notBefore|notAfter|EDTF|dating system|era name' corpus/knowledge/ corpus/README.md SKILL.md PROVINCE.md
```

Observed output, run before any r103 file existed (2 hits, both inert; later r103 surfaces — this entry, SKILL.md, corpus/README.md, PROVINCE.md — now match by design): `2026-10-12-lore-decision-table.md:18` (the uncovered-row declaration itself) and `r91-c9-watch.md:211` (the real-world calendar date 2026-10-17 used to disambiguate re-check identities — not an in-world dating rule). No existing row governs named-calendar claims, uncertainty, or relative time.

## Decision table — encoding in-world time into timeline.json

| In-world input | Lane encoding | Boundary |
|---|---|---|
| Event with no sourced date; author needs an ordering slot | Integer `tick` is an **editorial ordinal**, not a date, year, era, or clock value. Tick 1 after "first bell" is "an authoring convention, not independent proof of simultaneity or a clock conversion" (decision-table round 10, line 110). Equal ticks mean one shared editorial slot; they do not assert in-world simultaneity beyond the checker-local double-booking convention. | Never read a tick as a date in any calendar; never infer tick-gap magnitude as elapsed in-world time. r71 was rejected because tick 4 "encodes succession … unsupported" by the excerpt (LOG.md:1272) — the M4 encoding-overreach lesson. |
| Source gives a date in a named in-world calendar or era | Preserve the date string verbatim in the event's sourced `description`/claim, tagged with the calendar name, with its own `source_id`. OWL-Time: positions "may be expressed … using another temporal reference system such as Unix-time, geologic time, or different calendars" (S020, abstract); a named fictional calendar is a temporal reference system, and OWL-Time's `:hasTRS` binds each position to its own TRS — the analogue here is: every date claim names its calendar. | The date string is a sourced claim about what a document says, never a tick and never a decoded real-world date. |
| Same event dated in two different in-world calendars, or two sources give different dates in one calendar | Keep both claims attributed (M3). File a `contradictions.json` candidate preserving both — PROVINCE.md:9 refuses "silently resolving contradictions". | Never pick a winner, merge, or drop one date. Never convert one date into the other's calendar without a separately sourced correlation claim inside the fiction. |
| Uncertain or approximate date ("perhaps the third reign", "around midwinter") | Keep it uncertain (Q07). Encode an editorial bounded interval — a `not_before`/`not_after`-style pair — **labelled editorial** in the clause map (Q04), never a point. EDTF keeps uncertainty inside the value: `'?', '~' and '%' are used to mean "uncertain", "approximate", and "uncertain" as well as "approximate"' (S021, Level 1). TEI `att.datable` supplies `@when`, `@notBefore`, `@notAfter`, `@from`, `@to` for exactly this bounds shape (S022, attribute table). | Never replace an uncertain date with a single tick position that pretends precision; the interval endpoints are editorial bounds on the claim, not a new sourced fact. |
| Unspecified portion ("the year of the flood", "sometime in the 40s") | Keep the unspecified part unspecified: a claim text may carry a partial value (EDTF `X` digits, "in place of one or more rightmost digits … the value of that digit is unspecified", S021, Level 1); do not fill digits. | Partial values stay partial; an unspecified year is not year zero and not a guess to be resolved. |
| Relative time ("three winters after the crossing", "in his father's third year") | Encode ordering only: a `depends_on` edge (or an existing event reference) gives precedence; the tick gap is editorial. Allen-style interval relations — OWL-Time's "topological (ordering) relations among instants and intervals" (S020, abstract) — license `before`/`after`/`meets` semantics, all of which the lane's `depends_on` + strict-earlier tick already expresses for well-formed rows. | Never assert a tick-gap magnitude equal to the stated span ("three winters" ≠ `tick + 3`) unless a sourced unit correlation exists inside the fiction. A declared era-length or calendar-correlation convention is required before any duration arithmetic. |
| In-world date needing real-world conversion (e.g., author asks "what Gregorian date is this?") | Refuse the conversion. ISO 8601-2 explicitly "excludes the representation of date elements from non-Gregorian calendars" (S023, abstract); even the interchange standard treats calendar-to-calendar mapping as out of scope, and the lane has no real-time axis at all. | Out of scope: lane records in-world claims, never a real-world timeline placement. |

## What check_bible.py does not do, and why no checker change this round

The checker's entire time apparatus is:

- schema: `tick` must be `int` (`corpus/fixtures/check_bible.py:29`);

- `timeline` rows: `tick < 0` → `must be nonnegative` (line 384-385);
- same `(entity_id, tick)` at different places → `double-booked` (lines 386-392);
- `depends_on` member type (lines 393-395), self/repeated/unknown/ambiguous targets (lines 396-411), and prerequisite `tick >=` event tick → `timeline inversion` (lines 412-414);
- provenance records: invalid tick (lines 259-262) and `tick <= previous tick` → `provenance tick … must be greater than previous tick` (lines 323-326).

There is no calendar, era, date-string, or uncertainty check. Observed: `grep -niE 'calendar|date|era|ordinal' corpus/fixtures/check_bible.py` returns only substring coincidences inside `validate`, `candidate`, `enumerate`, `dep_index` — zero genuine hits. So CM-c is unenforced by construction.

No checker change is justified this round (Q01, Q06): no declared in-world or schema convention makes a calendar property obligatory, so a hard rule would be the M1 false-positive class; and no fixture yet carries a named-calendar claim, so no concrete input would change a non-author action — the M6 bar for new diagnostics. The method above governs hand-encoding under the existing schema until a real fixture exercises it.

## Term crosswalk — outside art to lane fields

| Outside concept | Lane analogue | Status |
|---|---|---|
| OWL-Time `:TRS` / `:hasTRS` (temporal reference system bound per position) | The calendar name recorded inside a sourced date claim | method analogue only — no RDF or OWL is introduced |
| OWL-Time Allen interval relations (`before`, `after`, `meets`, …) | `depends_on` edges plus the strict-earlier tick inversion rule | already governed; the lane needs no new relation vocabulary |
| EDTF `?` `~` `%` uncertainty/approximation qualifiers | Uncertainty kept in the verbatim claim text; optional editorial `not_before`/`not_after` bounds | method analogue; bounds are labelled editorial, never sourced fact |
| EDTF `X` unspecified digits and `..`/null open intervals | Partial claims stay partial; open-ended spans stay open | method analogue; no digit-filling or invented endpoints |
| TEI `att.datable` `@when`/`@notBefore`/`@notAfter`/`@from`/`@to` | The bound-pair shape for editorial date bounds | method analogue; TEI also supplies `att.datable.custom` (`@when-custom`, `@datingMethod`, `@datingPoint`) for non-Gregorian systems — evidence that dating claims should carry their calendar name |
| ISO 8601-2 exclusion of non-Gregorian calendars | The lane's refusal of calendar conversion without a sourced correlation | supports the refusal; the lane is stricter, having no real-time axis at all |

## Worked encoding sketch (editorial illustration; no fixture changed)

Suppose a source `annals-iv` says: *"The crossing was sworn on the Third Day of Longwinter, in the seventh year of the Compact."* and a second source `ledger-b` dates the same occasion to *"Frostmonth the twenty-eighth"*. Under the method above the two stay as separate sourced claims — nothing is converted:

```json
{ "id": "crossing-sworn", "tick": 9, "entity_id": "aru", "place_id": "chalk-stair",
  "depends_on": ["envoy-arrives"], "source_id": "annals-iv",
  "description": "annals-iv: sworn on Third Day of Longwinter, seventh year of the Compact" }
```

The ledger-b date enters as a second claim attributed to `ledger-b` (or a `contradictions.json` row pointing at both), not as a merged date. `tick: 9` remains an editorial ordinal shared with other tick-9 slots; the Compact-year string is verbatim claim text, not a tick and not a real-world year. If the excerpt had instead said only *"three winters after the envoy arrived"*, the encodable residue is exactly `depends_on: ["envoy-arrives"]` — ordering, no magnitude.

## Why a method note and not a schema field

A `calendar` or `date` column in `timeline.json` would tempt exactly the silent conversions this note forbids, and the r71 history shows the lane pays for unsupported structure. Keeping the calendar name inside sourced claim text preserves the fiction's own reference system per claim — the OWL-Time `:hasTRS` idea expressed in the lane's existing vocabulary — while the checker continues to verify only what is mechanically checkable: citations, endpoints, ordering, and occupancy.

## Falsifiable claims and falsifiers

| Claim | Falsifier |
|---|---|
| Every rule above is encodable under the current five-table schema without checker modification | A fixture whose sourced dating requires a field the schema lacks while staying Q04-excerpt-faithful — that fixture, not this note, would justify a schema/checker round |
| No admitted knowledge row already governs named-calendar claims, uncertainty, or relative time | The negative sweep above re-run with an additional substantive hit on a pre-r103 file |
| This settles a decision the baseline leaves unsettled | An existing fixture or map that already encodes a named-calendar, uncertain, or relative date with a documented convention (sweep found none) |
| Uncertainty is preserved, never resolved to a point | A counterexample row in this entry that silently converts an uncertain/relative expression into a definite tick or date |

## Scope limits

- Editorial method only: no canon claim, no source-text entailment, no reliability ranking (CM-d), no real-world dating or Gregorian default.
- Outside art (OWL-Time, EDTF, TEI, ISO 8601-2) informs encoding **method**; it establishes no in-world canon (Q10).
- Allen 1983 (DOI 10.1145/182.358434) was not opened — ACM landing page returned HTTP 403 this session; the interval-relation claim above rests on OWL-Time's own abstract instead.
- Checker behavior is unchanged; the r91 C9 watch ruling on provenance-tick inversion is untouched.

## Adjacent

Boundary, reported not absorbed: kotodama-shokunin owns calendar and era **design** for generated worlds (`kotodama-shokunin/corpus/knowledge/culture-material/calendar-festival-systems.md`, `kotodama-shokunin/corpus/knowledge/culture-material/era-periodization-models.md`, verified present under the fleet kaika worktree). Lore owns **recorded chronology**: ticks, dated in-world claims, and ordering in `timeline.json`. This entry imports none of kotodama's design rules; a fictional calendar authored by generation work is treated here as a named TRS string like any other sourced claim.

## Rejected at post-review re-grade (round 103, 2026-10-19 — appended; text above stands)

Admitted in `33173138` and withdrawn here. The decisive rule (decision table, row "Relative time") writes `depends_on` for pure temporal precedence. In this lane `depends_on` lists **stated prerequisites**: "direction is `depends_on` (prerequisite → event)" (`corpus/knowledge/2026-10-12-lore-decision-table.md:19`; inversion row at `:12`). "Three winters after X" orders two events; it does not say X is a prerequisite. Encoding it as one asserts more than the excerpt supports — the M04 class, now criterion Q13 in `corpus/QUALITY.md`.

The sealed comparison admitted this entry only on qC2 (`.ufo/waves/round-103/seats/R103Adjudicator.md:13`), and qC2 is exactly that edge. Under the corrected rule the proposal action equals the baseline's: keep the phrase in the sourced description, place the event at an editorial tick on the stated side of its anchor, add no edge. With qC2 SAME, every question is SAME and the entry fails Q11 (supersedes Q06). It moved here from `corpus/knowledge/` by `git mv`; the bytes and history are kept.

Corrected rule for a future entry: relative time → editorial tick order only; `depends_on` only where the excerpt states a prerequisite; a stated span never becomes a tick-gap magnitude. Flip: a sealed case on which the base corpus decides wrongly — for example, an author who converts a named-calendar date into a tick without a sourced correlation.
