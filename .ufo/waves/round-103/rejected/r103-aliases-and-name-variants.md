source: SXA1 — https://www.w3.org/TR/2009/REC-skos-reference-20090818/ — §5 Lexical Labels, integrity conditions S13–S14 (W3C Recommendation 2009-08-18); SXA2 — https://www.mediawiki.org/wiki/Wikibase/DataModel — EntityDescription lexical information section (current page); SXA3 — https://tei-c.org/release/doc/tei-p5-doc/en/html/ND.html — TEI P5 Guidelines version 4.12.0, rev 113e933e2, ch. 14 (task context said ch. 13; the current release numbers the names module 14); SXA4 — https://www.wikidata.org/wiki/Help:Aliases — community help page, practice corroboration only
verified-at: 2026-10-19
recheck: re-run the negative sweep command in §Decision delta and `grep -n "name" corpus/fixtures/check_bible.py`; re-open SXA1–SXA3 whenever this entry is cited or the named sources ship a new release (TEI: on-release); SXA4 is community text and may be re-read but never sole support
coverage-row: CM-a

# Aliases, name variants and homonyms — round 103

This entry governs how the lane records **names on entities** in
`entities.json` (`{id, kind, name, first_appearance, claims[]}`). It is a
record convention, not a canon claim, and it changes no checker behavior
this round.

## Decision delta (Q06)

The baseline corpus leaves three decisions unsettled and `l0-questions.md:1`
has carried an open operator question on them since r4:

1. How to record a second or later name for one entity — no alias field or
   convention exists.
2. What two entities sharing one display name *means* — the only record is
   the r4 rejection (LOG.md:52-55; SCORECARD.md:14 `retired:`), which
   settled what we must *not* do (hard-fail) and left the affirmative rule
   open.
3. Whether a name or alias can attest identity — implicit in R10
   (SKILL.md:26) but never stated for entity `name` fields.

Negative sweep run on this tree 2026-10-19:

```sh
grep -rniE 'alias|homonym|name.?variant|alt.?label|preferred name|display name' \
  corpus/knowledge corpus/README.md SKILL.md PROVINCE.md corpus/fixtures/README.md l0-questions.md
# 9 hits, all records of absence: the unmeasured seed row
# (2026-10-12-lore-consistency-checklist.md:8), the "does not yet check
# aliases" scope line (2026-10-12-lore-decision-table.md:17), the r4
# rejection records, and the open L0 question. No governing convention.
```

Decision 1 settles this: alternate names are carried as sourced claims on
the entity, `name` stays the single preferred display name.

## What the primary art says (opened 2026-10-19)

- **SKOS** (SXA1) separates label roles by integrity conditions: "S13
  `skos:prefLabel`, `skos:altLabel` and `skos:hiddenLabel` are pairwise
  disjoint properties" and "S14 A resource has no more than one value of
  `skos:prefLabel` per language tag" (§5.4). Nothing in the SKOS data model
  stops *two different* concepts from sharing a preferred label — S14 binds
  one resource, not the scheme; the only uniqueness *convention* in the
  spec is for notations: "By convention, no two concepts in the same
  concept scheme are given the same notation" (§6.5.3).
- **Wikibase** (SXA2) models the same split: "for any given language, an
  EntityDescription may have at most one label and at most one
  description, but any number of aliases" and "description: a brief
  description to clarify the meaning of the label (which may be
  ambiguous)" — the label alone is not a key; *label+description* is
  declared the per-language key "if both label and description are set",
  which presupposes shared labels are legal.
- **TEI P5 v4.12.0** (SXA3) marks multiple name forms on one referent
  (`persName`/`placeName`, `type` distinguishes e.g. married/birth/pen
  names) and carries attribution inline: "`resp` (responsible party)
  indicates the agency responsible for the intervention or interpretation"
  and "`cert` (certainty) signifies the degree of certainty associated
  with the intervention or interpretation" (§14.1.1).
- **Wikidata help** (SXA4, community) corroborates practice: "Aliases are
  alternative names, like nicknames, acronyms, or translations."

## Decision table (maps onto `entities.json` fields)

| Situation | Decision | Source / boundary |
|---|---|---|
| One entity has one attested name | `name` holds it; `claims` need no name rows. | baseline schema (`check_bible.py:27`) |
| One entity has several attested names (variant, translation, nickname, former name) | `name` = the single preferred display name; every other attested name is its own `claims` row (`statement: "<id> is also known as <variant>"`, `source_id` required). Never pack alternates into `name`. | SKOS prefLabel/altLabel split, S13–S14 (SXA1); Wikibase one-label/many-aliases (SXA2); TEI multi-name `@type` (SXA3) |
| The preferred name is itself a choice between attested forms | Pick one for `name`; the rejected forms stay in `claims`. The choice is editorial and reversible; it asserts no canon. | SKOS S14 is per-language, not per-truth (SXA1) |
| Two distinct entity `id`s share the same `name` (homonyms) | **Warn-class finding, never a hard fail** — and only where a declared in-world or schema convention makes names unique does it fail at all. No such convention is declared anywhere in this lane, so today homonyms are *legal data*: keep both rows, disambiguate via `id` and a distinguishing claim, never merge. | r4 rejection (LOG.md:52-55; SCORECARD.md:14 `retired:`); SKOS has no cross-resource prefLabel constraint (SXA1); Wikibase keys on label+description, not label (SXA2); TEI keeps two `person` records for two bearers (SXA3) |
| An "alias" is asserted by an ID, label, or matching string alone | Names never establish identity: matching `name` values do not merge entities, and an alias string is not evidence the bearer is the same entity. Identity needs referent + field + occasion (R10, SKILL.md:26). | Q02 / R10; SXA2 description disambiguation |
| An alias claim has no resolvable `source_id` | Existing citation check already reports it; each name variant needs its own in-world source — an unattributed alias is not admitted. | Q03; existing claim rule (`check_bible.py:301`) |
| Attribution or certainty of a name is contested in-world | Keep each sourced form as its own claim row naming its source; the `statement` text may carry the in-world qualifier (e.g. "the clerk calls her …"). The schema has no `cert`/`resp` field; do not invent silent ones. | TEI `@cert`/`@resp` pattern (SXA3), mapped onto claims, not new fields |

## What the checker does NOT do today

`corpus/fixtures/check_bible.py` (428 lines, replayed this round):

- `name` appears only as a required nonempty string
  (`check_bible.py:27` schema map, `:80` required-field report).
- No code path compares `name` values across entity rows — the only
  cross-row key checks are entity/timeline `id` counts and the JSON
  duplicate-member guard at load (`check_bible.py:49`).
- `check()` collects findings in a single `errors` list
  (`check_bible.py:35`, `:415`) and `__main__` prints every finding as
  `VIOLATION:` then exits 1 (`check_bible.py:423-427`). **There is no warn
  channel** — every emitted finding is fatal.

**Why no checker change is proposed this round.** The r4 experiment proved
the only available channel (`VIOLATION`, exit 1) is harmful for homonyms,
and L0 (`l0-questions.md:1`) holds the warn-vs-convention design question
open for the operator. A warn-class name-collision report is therefore a
*future, separately claimed* move — it would need a non-fatal output class
the checker does not have. This entry governs authoring and review without
it: reviewers apply the table by hand; the checker's existing citation and
ID rules already cover the sourced-claim mechanics.

## Falsifiable claims and their falsifiers

- **F1.** Every alternate name admitted under this convention appears as a
  `claims` row with a resolvable `source_id`. *Falsifier:* a fixture or
  map encoding an alias with no claim row or an unknown `source_id`.
- **F2.** Under this convention, two entities sharing a `name` yield no
  new `VIOLATION` and no merge. *Falsifier:* any rule, fixture or note
  that fails or merges on equal `name` alone — that would repeat r4.
- **F3.** This entry changes zero checker behavior. *Falsifier:* any diff
  to `check_bible.py` or fixture JSON attributed to r103.
- **F4.** External models inform method only. *Falsifier:* any claim row
  citing SKOS/Wikibase/TEI/Wikidata as an in-world source, or any canon
  assertion resting on them.

## Scope limits

- SKOS, Wikibase, TEI and Wikidata help are **method evidence**: they show
  how mature knowledge systems separate preferred labels from alternates
  and where they do and do not require uniqueness. None of them
  establishes anything about this lane's fictional records.
- The lane's schema has no language/script field; `name` is unqualified
  text. Per-language preferred names are an unmodeled surface, noted for
  the frontier, not decided here.
- Kotodama owns name *generation*; see `## Adjacent` below. This entry
  governs only names *recorded on landed entities*.

## Adjacent

Name generation — derivation rules, slot grammars, and the collision gate
at authoring time — is kotodama's province, not this lane's:
`kotodama-shokunin/corpus/knowledge/linguistics/naming-systems.md`,
`kotodama-shokunin/corpus/knowledge/synthesis/naming-canon-workflow.md`,
`kotodama-shokunin/corpus/knowledge/verification/naming-collision-gate.md`
(all present at fleet root 2026-10-19). Lore records and consistency-checks
the names those systems produce; it does not re-derive or re-judge their
generation rules, and this paragraph reports the boundary without restating
kotodama's criteria.

## Plain-statement boundary (per r4 / LOG.md:52-55)

A `name` value is a display label on a record. Equal names between two
entity IDs never establish shared identity, never establish a canon error,
and never justify a hard failure — unless and until a declared in-world or
schema convention makes names unique. No such convention is declared in
this lane today; the open L0 question (`l0-questions.md:1`) is where a
future warn-only or convention-gated design belongs.
