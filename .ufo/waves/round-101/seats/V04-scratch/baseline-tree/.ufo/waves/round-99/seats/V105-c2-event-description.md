# V105 c2-event-description — round 99

Seat: V105 (verifier). Question: `clerk-lapse-recorded` description vs the lapse-note wording — no description clause out-claims the note; the phrase `historical open entry` appears in both or is flagged. Baseline: r98 closure `4265df5`. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V105-scratch/poll.log` only.

Axes scored: (1) no-out-claim — every positive clause of the description is in the lapse note, or is the chain's already-declared editorial tick encoding; (2) phrase-identity — `historical open entry` in the description and in the note, else flagged in the delivered map/README; (3) evidence — quoted commands and observed output only.

## Poll record

| Time (local) | Observation |
|---|---|
| 22:01:41 | Fixture dir present. `timeline.json` / `fictional-excerpts.md` / `sources.json` already the lapse bytes (`2cdb9fda…` / `fefebaf9…` / `8c215b38…`). `README.md` and `claim-excerpt-map.md` still the r98 placeholders (`32efc78f…` 5829 B, `c1099d0e…` 15028 B). `S3-fixture-author.md` present. `S4-fixture-docs.md` absent. `S5-*.md` absent. `corpus/knowledge/r99-*` absent. |
| 22:05:05 | S4 report present. README `b9320941…` 6176 B and map `d2fe20e5…` 17119 B, matching the hashes S4's report declares. S3 files unchanged. S5 and `corpus/knowledge/r99-*` still absent. |
| 22:07:51–22:08:11 | One 20 s stability wait (artifacts for this seat already present; not a 40-try stall). Hashes unchanged. S5 still absent. |

No stall-escape. S5's knowledge notes are not the scored object (description vs excerpt). They were absent at the stability read; this seat does not treat that absence as ABSENT for the description comparison, and does not treat S4's scratch `map-namespace-swap.md` as delivered text.

S3's report (written while README/map were still r98 copies) says the description records the four note clauses. It does not mention the locative. Judged bytes are the stable files below, not that summary.

## Frozen bytes (sha256, stable 22:05:05 and 22:08:11)

```
$ sha256sum corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
    corpus/fixtures/r99-window-lapse/sources.json \
    corpus/fixtures/r99-window-lapse/README.md \
    corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
```

## Description and note (quoted)

`timeline.json:77-85`:

```
"id": "clerk-lapse-recorded",
"tick": 15,
"entity_id": "clerk-maren",
"place_id": "chalk-stair",
"depends_on": ["clerk-filing-open"],
"description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.",
"source_id": "clerk-lapse-note"
```

Lapse section `fictional-excerpts.md:66-76` (the note). Quote lines 70-74:

```
> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.
```

Scope line 76: "this appended section is the clerk's first-person lapse record. It records that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry. It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; the crossing-scoped agreement above is unchanged, and the matter stays open."

## Phrase criterion — holds

```
$ grep -nF "historical open entry" \
    corpus/fixtures/r99-window-lapse/timeline.json \
    corpus/fixtures/r99-window-lapse/fictional-excerpts.md
corpus/fixtures/r99-window-lapse/timeline.json:84:    "description": "… the matter stands as a historical open entry.",
corpus/fixtures/r99-window-lapse/fictional-excerpts.md:73:> The matter stands as a historical open entry.
corpus/fixtures/r99-window-lapse/fictional-excerpts.md:76:Scope: … the matter stands as a historical open entry. …
```

The phrase is in the description and in the quoted note (line 73), repeated in the scope (line 76). No flag is required. It is the note's own wording inside "the clerk records that …", not an upgrade to an external historical fact. The description does not add "historical fact", "proved", or "as world truth".

## Clause check — one locative out-claims

Python containment against the quote lines (70-74) and against the scope paragraph (76), run at 22:05:05:

```
IN_QUOTES=False  'At the Chalk Stair at tick 15'
IN_QUOTES=False  'the clerk records that'
IN_QUOTES=True   'the crossing-window named in the original minute has closed'
IN_QUOTES=True   'the agreement was unfulfilled'
IN_QUOTES=True   'no claim was lodged'
IN_QUOTES=True   'the matter stands as a historical open entry'

IN_SCOPE=False  'At the Chalk Stair at tick 15'
IN_SCOPE=False  'the clerk records that'
IN_SCOPE=True   'the crossing-window named in the original minute has closed'
IN_SCOPE=True   'the agreement was unfulfilled'
IN_SCOPE=True   'no claim was lodged'
IN_SCOPE=True   'the matter stands as a historical open entry'
```

Description words absent from the quote lines: `at`, `chalk`, `stair`, `clerk`, `records`, `that`.

Whole lapse section (lines 66-76), re-checked at 22:08:11:

```
lapse_section_has_Chalk_Stair False
lapse_section_has_chalk_stair_ci False
```

`Tick 15` is in the section (line 70). `records that` is in the scope (line 76: "It records that"). `the clerk` is in the scope ("the clerk's first-person lapse record"). `Chalk Stair` is in neither the quotes nor the scope.

| Clause in the description | In quote lines 70-74 | In scope line 76 | Verdict |
|---|---|---|---|
| the crossing-window named in the original minute has closed | yes, line 70 | yes | in the note; not an out-claim |
| the agreement was unfulfilled | yes, line 71 | yes | in the note; not an out-claim |
| no claim was lodged | yes, line 72 | yes | in the note; not an out-claim |
| the matter stands as a historical open entry | yes, line 73 | yes | in the note; not an out-claim |
| the clerk records that | no (quotes are first person) | paraphrase of "the clerk's … record. It records that" | attribution frame, weaker than the quotes' declarative mood; not an out-claim |
| at tick 15 | "Tick 15:" line 70 | no | editorial tick encoding of the note's own label; same class the map already declares for tick integers; not an out-claim |
| At the Chalk Stair | no | no | **out-claim.** The locative modifies the recording act ("At the Chalk Stair at tick 15, the clerk records that …"). The lapse note does not place that act at the Chalk Stair. |

Control, same file, prior beat: tick-14 description also opens "At the Chalk Stair at tick 14", and its note does say the place (`fictional-excerpts.md:59` "I filed both pending accounts at the Chalk Stair registry."). Tick 15 copies that template without a matching sentence. `place_id: "chalk-stair"` is the schema slot the declaration required; putting the same place into the description as the location of the act is a propositional claim the note does not make. The prior filing note names Maren "clerk of the Chalk Stair registry"; that is an office in a different section, not a statement that the tick-15 recording happened at the stair. The lapse-note source title ("Maren's Chalk Stair Lapse Note") is not excerpt wording. `sources.json` reliability note repeats the four clauses and does not say "at the Chalk Stair".

The description does not say the matter closed. "has closed" has the same subject as the note (the crossing-window). It does not say resolution, blame, reconciliation, breach, verdict, or a new duty. Those negatives are in quote line 74 and scope line 76 and are absent from the description. That is an omission, not an added claim: the description does not assert the opposites. Not scored as an out-claim.

The map does not flag the locative. `claim-excerpt-map.md:55` says the tick-15 event "encodes only" the four note clauses. That "only" is false of the description string, which also encodes "At the Chalk Stair". J21 (`claim-excerpt-map.md:69`) restates the four clauses and the line-74 negatives; it does not mention or bound the locative. So the out-claim is unflagged in the delivered map.

## Adjacent, not scored as the description

README:11 and map:69 add "per the original minute's terms" / "per that minute's terms". The description does not. The note says the window is "named in the original minute" and "has closed"; it does not say the closure follows the minute's terms. That gloss is an out-claim in the docs, outside this seat's scored string. Recorded so it is not mistaken for description wording.

S5 knowledge notes were still absent at 22:08:11 (`ls .ufo/waves/round-99/seats/S5-*.md corpus/knowledge/r99-*` → both "No such file or directory"). They were not required to compare the description to the note, and they were not read as a plan.

## Bottom line

FAIL — the description's locative "At the Chalk Stair" is not in the lapse note (quotes or scope) and is not flagged; the four recorded clauses match the note, and "historical open entry" appears in both.
