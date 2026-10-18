# V50 — byte-prefix (round 95)

Seat: V50 byte-prefix. Mandate: after P3/P4, `cmp` r94 vs r95 for every file claimed copied —
`entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`,
`source-excerpt.md` byte-identical; `fictional-excerpts.md` is r94's exact byte-prefix plus an
appended section only; `sources.json`/`timeline.json` differ only by appended rows (JSON diff).
Read-only seat: no repository writes other than this report; no commits; no network; no nested
agents.

Baseline: r94 closure `fb118c4` (working tree at start `M LOG.md`, `?? .ufo/waves/round-95/`).
Targets: `corpus/fixtures/r94-paired-crossing/` (r94 side) vs
`corpus/fixtures/r95-crossing-aftermath/` (r95 side). All commands run from repo root with
`python3` / `cmp` / `git`.

## Poll-wait record

- 16:18:01 — `corpus/fixtures/r95-crossing-aftermath/` appeared with 8 files, all still
  byte-identical in size to r94 (P3 mid-copy; `README.md`/`claim-excerpt-map.md` absent).
- 16:18:34 — `fictional-excerpts.md`, `sources.json`, `timeline.json` grew (append done).
- 16:21:10 / 16:21:27 — P4's `claim-excerpt-map.md` (8563 B) and `README.md` (4070 B) landed.
- 16:21 / 16:22 — P3 and P4 seat reports present (`P3-fixture-json.md`, `P4-fixture-docs.md`).
- 16:22:41–16:23:41 — 60 s stability re-check: all ten r95 digests unchanged, harness still PASS.
- Verification ran at 16:23–16:24 local (19:23–19:24 UTC) on the frozen fixture.

## 1. Five files claimed as byte copies — PASS

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s corpus/fixtures/r94-paired-crossing/$f corpus/fixtures/r95-crossing-aftermath/$f; echo "$f $?"; done
entities.json 0
relations.json 0
contradictions.json 0
inspiration-note.md 0
source-excerpt.md 0
```

sha256 pairs (r94 == r95):

| file | bytes | sha256 |
|---|---|---|
| entities.json | 1449 | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| relations.json | 139 | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| contradictions.json | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| inspiration-note.md | 1956 | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| source-excerpt.md | 640 | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |

Independent byte-prefix check for the excerpt file's inherited region (Python byte compare on the
r94 length):

```
r94 bytes 1116 r95 bytes 1845 prefix_ok True appended 729
```

These five digests match P3's report table exactly (P3-fixture-json.md, "Delivered
(post-modification) sha256").

## 2. `fictional-excerpts.md` — r94 exact byte-prefix + append only — PASS

```
$ cmp -n 1116 corpus/fixtures/r94-paired-crossing/fictional-excerpts.md corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
(no output; exit 0)
```

`r95[:1116] == r94` exactly; the remaining 729 bytes are one appended section, verbatim:

```
\n## Round 95 aftermath note (2026-10-17)\n\nNewly authored fictional first-person note, attributed to in-world source ID `aru-aftermath-note`, folio 5, lines 1–4. This section is appended after the preserved r94 text above; the inherited wording is unchanged.\n\n> Tick 11: I waited at the Chalk Stair through the agreed bell.\n> Evin did not come.\n> The agreement we chalked covered this crossing only.\n> I assert no other duty, no breach, and no obligation beyond this crossing.\n\nScope: this appended section is Aru's first-person report of one non-arrival at the Chalk Stair. It asserts no breach and no perpetual or continuing obligation; the crossing-scoped agreement above is unchanged, and the record supplies no other duty.\n
```

Raw diff line accounting (0 removed lines = pure append; the leading `\n` is the separator, so
the added text starts at line 21 with a blank line and the heading is line 22):

```
$ git diff --no-index --numstat corpus/fixtures/r94-paired-crossing/fictional-excerpts.md corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
11	0	corpus/fixtures/{r94-paired-crossing => r95-crossing-aftermath}/fictional-excerpts.md
$ ... | grep -c '^-[^-]'   # removed lines
0
```

r94 sha256 `585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2`; delivered r95
sha256 `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` (matches P3's report).

## 3. `sources.json` / `timeline.json` — differ only by appended rows — PASS

Parsed-JSON element check (each r94 element must be value-identical and in the same position;
only appends permitted):

```
JSON-APPEND-ONLY sources.json: PASS rows 3->4; added=[{"id": "aru-aftermath-note", "title": "Aru's Chalk Stair Aftermath Note", "kind": "fictional first-person note", "reliability_note": "Newly authored fictional note; Aru reports waiting at the Chalk Stair through the agreed bell and that Evin did not come. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact."}]
JSON-APPEND-ONLY timeline.json: PASS rows 3->4; added=[{"id": "aftermath-missing-evin", "tick": 11, "entity_id": "aru", "place_id": "chalk-stair", "depends_on": ["paired-crossing-decision"], "description": "At the Chalk Stair at tick 11, Aru reports waiting through the agreed bell and that Evin did not come; the note scopes the agreement to this crossing only and asserts no other duty or breach.", "source_id": "aru-aftermath-note"}]
```

Raw diff line accounting (0 removed lines each):

```
6	0	.../{r94-paired-crossing => r95-crossing-aftermath}/sources.json
11	0	.../{r94-paired-crossing => r95-crossing-aftermath}/timeline.json
removed-line counts: 0 and 0
```

The single appended timeline row matches the declared C2 spec exactly: id
`aftermath-missing-evin`, tick `11`, entity `aru`, place `chalk-stair`, `depends_on`
`["paired-crossing-decision"]`, source `aru-aftermath-note`. Delivered digests:
sources.json `fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a` (798→1225 B),
timeline.json `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` (826→1254 B) —
both match P3's declared delivered digests.

## 4. Extra guard — r94 side untouched by P3/P4 — PASS

Pre-P3 baseline digests were captured before the fixture existed; all ten r94 files still match,
and every r94 file still matches its `fb118c4` blob:

```
$ git status --porcelain corpus/fixtures/r94-paired-crossing/     # empty
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md fictional-excerpts.md sources.json timeline.json claim-excerpt-map.md README.md; do disk=$(git hash-object corpus/fixtures/r94-paired-crossing/$f); head=$(git rev-parse HEAD:corpus/fixtures/r94-paired-crossing/$f); [ "$disk" = "$head" ] && echo "$f MATCH" || echo "$f MISMATCH"; done
entities.json MATCH ... README.md MATCH   (all 10 MATCH)
R94-UNTOUCHED <all 10 files>: PASS (baseline sha256 prefixes unchanged)
```

`INFO r95 extra files vs r94: []` — the new fixture has exactly the same file set as r94, no
stragglers.

## Secondary corroboration (adjacent, not this seat's claim)

Run for context on the delivered revision; other seats own these verdicts:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations        exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                        exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing   → 14/14 PASS exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster → 12/12 PASS exit=0
$ ls -d corpus/fixtures/*/ | wc -l → 169 ; git ls-tree HEAD corpus/fixtures/ → 168 trees
```

(Tool revision at measurement: `corpus/tools/map_obligations.py` sha256 prefix
`8eb5051db751cd44…`, i.e. P1's landed revision, differing from HEAD's `5801192b60f29053…`.
The byte comparisons above do not depend on tool revisions — they compare fixture bytes only.
My pre-P3 baseline for reference, run with the HEAD tool copied to /tmp: r94 14/14 PASS,
r93 12/12 PASS, r88 exit 2 `unsupported_map`, `--self-test` 20/20 PASS.)

## Adjacent observations (no verdict claimed)

1. `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` is **not** a byte copy of the
   r94 map (it is not in my seat's byte-copy list). SequenceMatcher on the two maps: 50→53
   lines, with replacements at the title, the "14/15 obligations" scope line, the expected
   inventory line, the JSON-facts heading, J01–J14 (namespace cell `r94-paired-crossing:` →
   `r95-crossing-aftermath:`, pointers/spans/modes/anchors unchanged) plus the new J15 row and
   two new prose lines. P4's report declares this namespace rewrite explicitly; C2's "14
   inherited rows carried unchanged" therefore holds at pointer/span/mode/anchor level, not at
   byte level of the map file. Flagging for the map-diff seats to judge.
2. `README.md` also differs (3426→4070 B), as expected — it is a new document, not a copy.
3. P3 flagged one interpretation risk (`"kind": "fictional first-person note"` vs a literal
   `"kind": "note"`); my byte checks neither confirm nor refute that choice — it is a schema
   question for the schema/dialect seats.

## Bottom line

PASS — all five byte-copy files are `cmp`-identical to r94, `fictional-excerpts.md` is r94's
exact 1116-byte prefix plus a 729-byte appended section (0 removed lines), `sources.json` and
`timeline.json` differ from r94 only by one appended row each (0 removed lines, parsed r94 rows
value-identical), the r94 side is untouched vs `fb118c4`, and the fixture was stable across a
60 s re-check.
