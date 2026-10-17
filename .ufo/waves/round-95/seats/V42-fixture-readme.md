# V42 — fixture-README review (round 95)

Seat: V42 fixture-README-review. Target: `corpus/fixtures/r95-crossing-aftermath/README.md`
(P4). Task: run every command in that README exactly as written; check its counts/scope wording
against the delivered bytes; flag any mismatch. Read-only elsewhere; no commits, no network.
Repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r94 closure `fb118c4`.

## Poll-wait

Two poll-waits at 20 s cadence. First (40 tries) for P4's two artifacts: `READY` when both
`README.md` and `claim-excerpt-map.md` existed (landed ~16:21). A second wait ran until P1/P2
landed, because the README's third command invokes `map_obligations.py`, which P1 owned and was
mid-flight at first measurement (22 self-test cases present, `schema_drift` not yet). Final
replay was taken after `schema_drift` appeared in the tool and the contract carried 22 cases.

Hashes at final measurement (md5):

```
d31b8182953e9088a155f4ed2978af5b  corpus/tools/map_obligations.py        (P1, post-landing)
5ccf979d845c20d00ad34e8462ef3b90  corpus/fixtures/r95-crossing-aftermath/README.md
a872889e86a10127750ba0647e4829ff  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8af8b5f73b73dd25eab20b467c1ebdb4  corpus/fixtures/check_bible.py
90b6a73940c00173495c5cbe1b69ec35  corpus/tools/support_check.py
```

## 1. Every README command, run exactly as written

The README has exactly one fenced block (3 commands; 0 inline `python3` mentions outside it).
All were run from the repository root, verbatim:

**CMD1**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

**CMD2**

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01..J15 (all: source-support; mode=verbatim; anchor=found; lines 12,13,12,13,17,12,13,12,13,18,19,12,13,20,26)
PASS S01, PASS S02 (editorial-row; mode=verbatim; anchor=found; source-excerpt.md:5)
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0
```

J15 line quoted in the receipt: `26:> Tick 11: I waited at the Chalk Stair through the agreed bell.`

**CMD3**

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

(The extra `INVENTORY` line is P1's new post-landing output; the r94-baseline tool emitted only
`OBLIGATIONS raw=15 mapped=15` + `RESULT PASS`. Both revisions PASSed the README command.)

Result: **all three commands are executable exactly as written and pass, exit 0, on the final
delivered revision.** No command in the README is stale, wrong-pathed, or missing a flag.

## 2. Counts / scope wording vs delivered bytes

Measured with `json.load` on the delivered files and by parsing both maps' JSON-facts tables.

| README claim (line) | Delivered evidence | Verdict |
|---|---|---|
| counts 5 entities / 1 relation / 4 events / 4 sources (L3) | entities 5, relations 1, timeline 4, sources 4, contradictions 0 | MATCH |
| "five inherited entity records and the one inherited relation are copied by JSON value" (L3) | `cmp` r94→r95: `entities.json`, `relations.json` IDENTICAL (stronger than value-equal) | MATCH |
| source IDs / paired-clock + crossing-minute wording / Spence excerpt / inspiration context retained (L3) | `source-excerpt.md`, `inspiration-note.md` IDENTICAL; `fictional-excerpts.md` diff is a pure append (`20a21,31`), r94 lines 1–20 byte-preserved | MATCH |
| added source `aru-aftermath-note`, Aru's first-person note (L7) | `sources.json` new entry id `aru-aftermath-note`, kind `fictional first-person note` | MATCH |
| added event `aftermath-missing-evin` (L7) | `timeline.json#/3` id `aftermath-missing-evin` | MATCH |
| tick-11 ordered after and depends on `paired-crossing-decision` (L9) | `tick: 11`, `depends_on: ["paired-crossing-decision"]` | MATCH |
| records Aru's report he waited through the agreed bell, Evin did not come (L9) | excerpt lines 26–27; event description; source reliability_note | MATCH |
| does not change earlier locations / create a contradiction (L9) | timeline diff is pure append; `contradictions.json` IDENTICAL (empty) | MATCH |
| crossing-only bound; asserts no other duty, no breach, no continuing obligation, no obligation beyond this crossing (L11) | excerpt lines 28–29 verbatim; note reliability_note; map prose J15 | MATCH |
| event `entity_id` Aru (one actor slot); description and note name the second participant (L11) | description: "…Evin did not come…"; note line 27: "Evin did not come." | MATCH |
| inherited empty `depends_on` arrays mean no represented earlier dependency (L13) | entries 0–1 unchanged, `depends_on: []` | MATCH |
| r88 verse already uses "chalk stair" as unowned crossing metaphor (L15) | `r88-m3-maya-cluster/fictional-excerpts.md:7` = `> The chalk stair stays a crossing, never a map.`; retained at r95 line 7 | MATCH |
| Spence passage is English prose about a story he labels "Kiche" (L19) | `source-excerpt.md`: "a story he labels “Kiche,” not a quotation from a K'iche-language edition" | MATCH |
| "15 source-attributed JSON pointer obligations (the 14 inherited rows carried unchanged plus the new tick-11 event row)" (L21) | 15 J-rows; J15 is the only new row; 14 inherited rows differ from r94 in exactly one column | MATCH with one wording nuance, see §3 |
| "separately labeled editorial comparisons" (L21) | S01/S02 under `## Editorial rows`; support_check EDITORIAL-ROWS 2/2 | MATCH |

Additional independent checks:

- File set of `r95-crossing-aftermath/` equals `r94-paired-crossing/` (10 files); no stray or
  missing artifact.
- Map J15 span `22-31` is exactly the appended section (line 21 is the blank separator; heading
  at 22; four quoted sentences at 26–29; scope sentence at 31); the anchor on line 26 is in-span
  and support_check confirmed it.
- `map_obligations` raw enumeration agrees with the map: raw=15 mapped=15, no findings.
- Fixture-directory census now 169 (`find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l`),
  consistent with the round's 168→169 declaration (other seats own that claim; recorded here as
  corroboration only).
- r94 replay unaffected: `check_bible` CLEAN exit 0; `support_check` 14/14 + 2/2, RESULT PASS,
  exit 0.

## 3. Flags

**F1 (minor, wording precision — not a factual error).** README L21 says the 14 inherited rows
are "carried unchanged", but the delivered map's rows are not textually identical to r94's: all
14 inherited rows differ in exactly one cell — the path-qualification column — from
`r94-paired-crossing:paired-clock` / `:crossing-minute` to `r95-crossing-aftermath:*`. Parsed
comparison: `r94 rows 14 r95 rows 15; columns that differ for inherited rows: {3: 14}`;
`r95-only rows: ['J15']`. The substantive fields (pointer, source ID, excerpt path, span, mode,
anchor) are identical in all 14 rows, and the map's own prose states this precisely ("only the
path-qualification column names this fixture's cluster path"), so a reader who follows the
pointer into `claim-excerpt-map.md` is not misled. Recommendation: none required; if the judge
wants byte-level precision, L21 could read "14 inherited rows carried with pointers/anchors/
spans/modes unchanged (namespace column re-qualified)".

**F2 (observation, not a defect).** The README states no expected outputs or exit codes for its
replay block, so there is nothing in the README that could go stale if a checker's receipt text
changes; the three commands were verified against the final delivered tool revision
(`map_obligations.py` md5 `d31b8182…`, i.e. post-P1), not only the pre-P1 one.

No other mismatch found. No claim in the README contradicts the delivered bytes.

## 4. Boundaries

This seat verified command executability, receipt outcomes, counts, and scope wording. It did not
judge semantic entailment, canon truth, source authenticity, rights, or permission; the
support/map receipts are lexical/structural checks only. Nothing was written outside this report
and `.ufo/waves/round-95/seats/scratch/V42/` (a count helper script); no P1–P5 file was modified.

## Bottom line

PASS — all 3 README commands run verbatim, exit 0 (check_bible CLEAN; support_check 15/15+2/2
PASS; map_obligations raw=15 mapped=15 PASS), and every numeric/scope claim in the README matches
the delivered bytes; one minor wording nuance flagged (F1: "14 inherited rows carried unchanged"
ignores the map's re-qualified namespace column, disclosed in the map's own prose).
