# V15 — c2-anti-overclaim (round 99)

Seat: **V15 c2-anti-overclaim** — verifier. Axes named and judged: (1) whether a "the clerk ruled" reading is constructible from delivered new bytes; (2) relation-row byte identity to r98; (3) ruling / verdict / resolution / canon / rights / identity overclaims in new bytes; (4) evidence completeness — quoted commands, no plan verified.

Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`); working HEAD at seat start `337f0fa` (blocked-dispatch note, ancestor of the baseline). Every command below ran from the lane root with `python3` unless noted. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V15-scratch/` only (`poll.sh`, `poll.log`, `poll-start.txt`, `s3-snapshot.txt`, `bible.out`, `support.out`, `map.out`).

## Poll outcome — S5 ABSENT

Content-gated poll (not existence-only; r98 placeholder hazard). Script `.ufo/waves/round-99/seats/V15-scratch/poll.sh`, 20 s cadence, 40 tries. Markers required together: `clerk-lapse-note` in `sources.json`, `clerk-lapse-recorded` in `timeline.json`, `Round 99 lapse note` in `fictional-excerpts.md`, `r99-window-lapse` in `README.md`, `clerk-lapse` in `claim-excerpt-map.md`, non-empty `corpus/knowledge/r99-gate-blind-spot-table.md`, non-empty `corpus/knowledge/r99-lapse-scope-note.md`, and seat reports `S3-*.md` / `S4-*.md` / `S5-*.md`.

A first poll (started 22:02:15) was killed by this seat at try 4 because its tool timeout was 300 s, short of the 40-try budget. It is not the verdict poll. Restarted poll:

```
POLL_START 2026-10-17T22:03:37-03:00
try=1 22:03:37 missing: table note S4rep S5rep
try=2 22:03:57 missing: table note S5rep
try=40 22:16:37 missing: table note S5rep
ABSENT after 40 tries 2026-10-17T22:16:37-03:00
```

S3 and S4 cleared inside that window (S3 report already present at restart; S4 report present by try 2). S5 never cleared. Recheck after the deadline, not a 41st poll try:

```
$ date -Is
2026-10-17T22:27:31-03:00
$ ls corpus/knowledge/r99* .ufo/waves/round-99/seats/S5*.md
ls: cannot access 'corpus/knowledge/r99*': No such file or directory
ls: cannot access '.ufo/waves/round-99/seats/S5*.md': No such file or directory
$ ls corpus/knowledge | grep -Ei 'r99|lapse|blind|gate'
NONE
```

No stall-escape. No all-reports poll (ENDGAME subtract-SELF not triggered). A later existence check at `2026-10-17T22:44:28-03:00` still found neither knowledge file nor any `S5*.md`. **S5's table, lapse-scope note, and report were not verified. No plan was verified.**

S3/S4 bytes below were judged only after their producer reports existed (`S3-fixture-author.md` 22:01, `S4-fixture-docs.md` 22:03) and were re-hashed at 22:21 and 22:25 with no drift.

## Delivered revision (S3/S4), sha256 at 22:21:33 and still at 22:25:39

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
```

S3's report hashes for the three edited files match (`sources.json` 3293 B, `timeline.json` 2998 B, `fictional-excerpts.md` 5114 B). S4's report hashes match (`claim-excerpt-map.md` `d2fe20e5…`, `README.md` `b9320941…`).

Placeholder hazard observed, same class as r98: at 22:01 the directory existed with README and map still byte-identical to r98 (5829 B / 15028 B, mtime 21:36) while excerpts/sources/timeline were already the lapse bytes. An existence-only poll would have been satisfied. This seat's poll required the S4 markers and did not judge the placeholders.

## Check 1 — relation row byte-identical to r98 — HOLDS

```
$ cmp corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r99-window-lapse/relations.json && echo REL_IDENTICAL_R98
REL_IDENTICAL_R98
$ cmp <(git show 4265df5:corpus/fixtures/r98-clerk-filing/relations.json) corpus/fixtures/r99-window-lapse/relations.json && echo REL_IDENTICAL_4265df5
REL_IDENTICAL_4265df5
$ sha256sum corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r99-window-lapse/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
```

The single JSON row is `{"from":"aru","to":"evin","type":"agreed_co_stewardship_for_this_crossing","source_id":"crossing-minute"}`. No second relation. Map row J11 differs from r98 in the namespace cell only (`r98-clerk-filing:crossing-minute` → `r99-window-lapse:crossing-minute`). Pointer, source ID, path, span `19`, mode `verbatim`, and anchor are equal. Anchor: `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`

Also byte-identical to r98 working tree and to `4265df5`: `contradictions.json`, `entities.json`, `inspiration-note.md`, `source-excerpt.md`.

## Check 2 — inherited prefixes — HOLDS

```
sources.json base 7 new 8 prefix True
timeline.json base 7 new 8 prefix True
entities.json base 6 new 6 prefix True
excerpt startswith True base 4187 new 5114
```

New source `clerk-lapse-note` only. New event `clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. No new entity, no new claim, no new relation. Excerpt append starts at the preserved r98 trailing newline, section "Round 99 lapse note (2026-10-17)", quoted lines 70–74.

Map: 22 r98 rows → 23 r99 rows. Inherited J01–J20 and S01–S02: 20 cell diffs, every one column 3 (path-qualified namespace) only. New row J21 only: pointer `timeline.json#/7`, source `clerk-lapse-note`, namespace `r99-window-lapse:clerk-lapse-note`, span `66-76`, mode `verbatim`, anchor `Tick 15: The crossing-window named in the original minute has closed.`

Census (supporting, not the seat's core): `git ls-tree -d --name-only 4265df5 corpus/fixtures/ | wc -l` = 172; `ls -d corpus/fixtures/*/ | wc -l` = 173; `comm` adds exactly `corpus/fixtures/r99-window-lapse`.

Gates on that revision, 22:04:13, exit 0 each (hashes unchanged at 22:25):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
```

These receipts are lexical. They do not prove the absence of a ruling reading.

## Check 3 — "the clerk ruled" construction — NOT constructible

Attempted reading R: "The clerk ruled that the crossing-window closed under the original minute's terms, ruled the agreement unfulfilled, and entered that as an official determination."

The phrases that make R tempting are real and are quoted:

- Excerpt `fictional-excerpts.md:70-73` is declarative, not "I report": "The crossing-window named in the original minute has closed." / "The agreement was unfulfilled." / "No claim was lodged." / "The matter stands as a historical open entry." Only line 74 is a first-person denial.
- `timeline.json` description (the new object): "the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry." The report-frame governs the first clause; the semicolon clauses can be detached as bare facts.
- `README.md:11` states as record fact, not as report: "the window closed per the original minute's terms; the agreement was unfulfilled; no claim was lodged".
- `claim-excerpt-map.md:69` attributes to the clerk a gloss the quote does not contain: "the clerk records that the crossing-window named in the original minute has closed per that minute's terms".

```
$ grep -nEi 'ruled|ruling' corpus/fixtures/r99-window-lapse/*
NO_RULED
$ grep -nF "per the original minute" corpus/fixtures/r99-window-lapse/*
README.md:11 only
$ grep -nF "per that minute" corpus/fixtures/r99-window-lapse/*
claim-excerpt-map.md:69 only
```

Neither gloss appears in `fictional-excerpts.md`, `sources.json`, or `timeline.json`. The excerpt says the window is "named in the original minute", not that closure followed "per the minute's terms."

R still requires ignoring counter-text that is in the same records:

1. `fictional-excerpts.md:74` "I record no resolution, assign no blame, and reconcile nothing."
2. `fictional-excerpts.md:76` "It asserts no resolution, no blame, and no reconciliation, and it creates no new duty … and the matter stays open."
3. `sources.json` new reliability note: "the clerk reports that … It asserts no resolution, no blame, and no reconciliation; it is not evidence of a breach finding, a continuing duty, a winner between the accounts, or an external historical fact."
4. `README.md:9` "it records only that the crossing-window named in the original minute has closed. It adds one lapse record; it does not change earlier locations, resolve or create a contradiction, assign blame, or convert either account into a verdict."
5. `README.md:11` same paragraph as the gloss: "does not overturn, confirm, adjudicate, or reconcile the accounts" and "it closes no one" and "assigns blame to neither" and "not evidence of … an adjudication, or an external historical fact."
6. `claim-excerpt-map.md:55` "it asserts no resolution, no blame, and no reconciliation, and it closes no one."
7. `claim-excerpt-map.md:69` same paragraph as "per that minute's terms": "It asserts no resolution, no blame, and no reconciliation; the matter stays open."
8. Relation type unchanged (`agreed_co_stewardship_for_this_crossing`). No new entity. `contradictions.json` remains `[]`.

**Verdict on R: not constructible.** Each variant needs at least one of those counter-texts ignored. There is no sentence in which the clerk rules, enters a verdict, closes a person, or adjudicates the two accounts.

### Soft spots (recorded, not findings)

1. **Terms gloss.** "per the original minute's terms" (`README.md:11`) and "per that minute's terms" (`claim-excerpt-map.md:69`) are not in the excerpt. They are the cheapest hook for R. They do not survive the no-adjudicate sentences in the same paragraphs. Wording debt for the next beat, not a delivered ruling.
2. **Denial promoted to world-fact.** `README.md:11`: "The lapse note asserts no resolution, no blame, and no reconciliation, so nothing is resolved". The "so" turns a speaker denial into an editorial conclusion. It is the absence of a resolution, which the declaration requires, not a positive resolution. Still stronger than the r98 pattern ("asserts no finding" kept as a speaker bound plus "not proof" of world fact).
3. **Act-framing, r98 class.** The new timeline description report-frames only the window clause, then states unfulfilled / no-claim / open-entry as bare clauses. The reliability note report-frames all four. Same class as r98 V14's tick-14 "the clerk filed" note. Not an overclaim on its own.
4. **"no breach" narrowed to "no breach finding".** r98 `README.md:11` said the record "asserts no other duty, no breach". r99 `README.md:11` says "no other duty, no breach finding". A hostile reader can hear "a breach occurred; no finding was entered," especially next to "unfulfilled." The text does not say a breach occurred. The reliability note says the note "is not evidence of a breach finding," which does not assert a breach. Recorded as a weaker bound than r98, not as a constructed breach.

## Check 4 — other overclaim axes on delivered new bytes

- **Verdict / resolution / blame.** Present only as negations or as the declared lapse facts (window closed, agreement unfulfilled, no claim lodged, matter stays open). "closes no one" is in `README.md:11` and `claim-excerpt-map.md:55`. No winner, no guilt, no fault, no binding judgment in the new lines.
- **Canon.** Map title `# r99 window-lapse: canonical claim-to-excerpt map` and "21 canonical pointers" continue the r98 genre label (`# r98 clerk-filing: canonical claim-to-excerpt map`). Not a fictional-canon claim. `README.md:19` "supplies no in-world witness, cultural authority, or fictional canon". `claim-excerpt-map.md:46` "do not … add canon". `inspiration-note.md` byte-identical to r98, including "supplies no fictional canon."
- **Rights / permission.** `README.md:19` "Rights and AI-training permission remain unassessed; neither is granted or inferred here." Map line 70: receipt "not … a verdict on source authenticity, truth, rights, permission, or canon." Inspiration-note rights and AI-training sections unchanged (byte-identical file).
- **Identity.** No new entity. `entities.json` byte-identical to r98. `README.md:15` keeps `first_appearance: clerk-filing-note` as the source that first presents Maren "in this JSON bible" and says the lapse note "does not re-present that first appearance, and it asserts no office beyond the filing, no finding, and no resolution." Namespace prose (`README.md:7`) still says path qualification "does not imply a separate source, entity identity, or contradiction."
- **S1 new prose, swept because it is delivered new bytes, not because this seat owns C1.** `git diff` on `dependency-freeze-contract.json` scope text still ends "no chronology truth, entailment, source, rights, or canon judgment". Provenance adds "BR-01's prose half is edit-detectable, not semantics-provable." That is a bound, not a canon or rights claim. No ruling/verdict language in the diff hits. S2 `corpus/tools/README.md` and `SKILL.md` were unmodified vs HEAD at 22:25 (`git diff --stat` empty). Not swept as new bytes; not treated as a plan.

`git status --porcelain -- corpus SKILL.md LOG.md SCORECARD.md` at 22:25: `M` on the two S1 freeze files, `?? corpus/fixtures/r99-window-lapse/`, plus this seat's `.ufo/waves/round-99/` tree. No V15 corpus write.

## Limits

- S5 `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md` were absent through 22:27:31. Their overclaim status is **ABSENT**, not clean.
- C1 freeze behavior was not re-run. Only the delivered contract prose was scanned for the forbidden vocabulary.
- Gates quoted above are structure/anchor receipts, not entailment.

## Bottom line

**ABSENT** — S5's blind-spot table, lapse-scope note, and report never landed (40 content-gated tries, 22:03:37–22:16:37; rechecked 22:27:31 and 22:44:28), so those bytes were not swept and no plan was verified; on the delivered S3/S4 bytes the relation row is byte-identical to r98 (`c279254b…`) and a "the clerk ruled" reading is not constructible without ignoring explicit counter-text, which is a partial result, not a pass of the whole seat.
