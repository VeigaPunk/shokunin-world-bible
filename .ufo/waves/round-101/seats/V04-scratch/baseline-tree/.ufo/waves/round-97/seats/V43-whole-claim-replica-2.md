# V43 — whole-claim-replica-2: constructibility of reconciliation / blame readings

Seat: V43, round 97, lane `lore-shokunin`. Scope of this seat: second independent
whole-claim replica review of the r97 C3 fixture (`corpus/fixtures/r97-crossing-acknowledgment/`),
with one explicit obligation — **attempt to construct reconciliation and blame readings over
the delivered bytes and report their constructibility** — plus a bounded extension to
resolution/winner readings (the arc's stated "dispute preserved unresolved"). The r96 cosmetic
repair is the same claim's second half and is receipted in §4.

All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.
Writes: this report plus `.ufo/waves/round-97/seats/V43-scratch/` only (absolute paths). No corpus
file was modified by this seat; probes ran on scratch copies. No nested agents, no commits, no
pushes, no network. Baseline HEAD `f3e09f9` (r96 closure).

## 0. Poll-wait record

Cadence 20 s, 40 tries, `V43-scratch/poll.sh` → `V43-scratch/poll.log`. Ready condition:
r97 fixture complete (10 files) AND producer reports R1–R6 present. Observed curve (lane time):

```
POLL_START 2026-10-17T18:43:17-03:00
CHECK i=1..3  fixture_ok=0 miss=[all 10 files] producers=0/6 total_reports=0
CHECK i=4  t=80s  fixture_ok=1 miss=[] producers=0/6     # fixture bytes landed 18:44:16-30
CHECK i=12 t=240s fixture_ok=1 miss=[] producers=0/6     # R5's map still the r96 copy
# manual bounded waits: producers 1/6 (R2 18:49:31), 2/6 (R4 18:50:14), 3/6 (R5 18:51:25),
# 4/6 (R1 18:52:25), 5/6 (R6 18:53:37)
CHECK i=40 t=800s fixture_ok=1 miss=[] producers=5/6 missing_reports=[ R3] total_reports=36
POLL_ABSENT after 40 tries                                # final check ~18:56:17
# R3-freeze-hardening.md landed 18:56:23 (between the final check and the ABSENT echo);
# manual confirmation 18:56:5x: producers=6/6, total_reports=37
```

R3's report landed seconds after the 40-try window's final check; all six producer reports exist
at this seat's freeze. Nothing was verified before its producer's bytes and report existed; no
plan was verified; no ABSENT condition survived. R3's artifact is `dependency_freeze` (C2 scope)
and was not used in any C3 receipt below.

## 1. Frozen revision identity (final snapshot 2026-10-17 ~18:57 -03:00)

```
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  sources.json
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  timeline.json
```

These equal R4's and R5's reported hashes; R5 documented byte stability 18:45:07 → 18:50:36 and my
snapshot at 18:57 reproduces the same values. r96 repaired map:
`e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de`. Tools at my receipts:
`check_bible.py` `ff9fd2aa…` (unchanged all round), `support_check.py` `55a5eb27…` (unchanged),
`map_obligations.py` `86b52949…` (R1's delivered revision; the tool moved during the round
`2b0ba815…` → `c1881149…` → `86b52949…` — every receipt below is pinned to `86b52949…`, and R4's
frozen-revision runs agree on the r96 side).

## 2. Gate receipts on the delivered r97 fixture

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J16 (inherited anchors at 12/13/17/18/19/20/26/37)
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS S01 / PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> …
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                             exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                             exit=0
```

The map's declared `**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows;
15 distinct excerpt anchors` (`claim-excerpt-map.md:5`) matches the tool receipts exactly.

## 3. Claim numbers and preservation (C3, this seat's independent computation)

```
counts: entities 5 / relations 1 / timeline 6 / sources 6; contradictions.json = []
independent raw obligations: 5 first_appearance + 5 claims + 1 relation + 6 timeline = 17
census: git ls-tree -d f3e09f9 corpus/fixtures/ | wc -l = 170 ; ls -d corpus/fixtures/*/ | wc -l = 171
```

- Five byte-copy files `entities/relations/contradictions.json`, `inspiration-note.md`,
  `source-excerpt.md`: byte-identical to r96 (`IDENTICAL`, sizes 1449/139/3/1956/640).
- `sources.json` and `timeline.json`: inherited prefix parsed-equal `True` (`s97[:5]==s96`,
  `t97[:5]==t96`); byte seam is an append after the join comma — common prefix 1738/1741 and
  1674/1677 bytes, r96 remainder `\n]\n`, r97 continuation `,\n  {`.
- `fictional-excerpts.md`: r96 file (2588 B) is a strict byte prefix of r97 (3410 B); append
  starts line 43; new section lines 44-53, quoted note lines 48-51.
- Map inheritance: `sed 's/r96-crossing-response/r97-crossing-acknowledgment/g'` of the r96
  post-repair map vs the r97 map — J01–J16 rows identical (16/16), only `J17` added; S01/S02 rows
  identical; all other differences are exactly title/scope/inventory/R9-row/line-18/line-51/
  line-57 (enumerated by full diff). J17 = `timeline.json#/5`, source `aru-acknowledgment-note`,
  span 44-53, mode `verbatim`, anchor line 48 — and the anchor is found at line 48 by
  `support_check` (PASS J17 above).
- README claims reproduce: counts 5/1/6/6 (`README.md:3`), added source/event names (`:7`),
  17 obligations "16 inherited rows carried unchanged plus the new tick-13 event row" (`:21`),
  replay commands point at the r97 fixture (`:26-28`).

## 4. r96 cosmetic repair (same claim, repair half) — verified

```
$ git show f3e09f9:…r96…/claim-excerpt-map.md > scratch-baseline ; diff scratch-baseline corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
44c44
< |---|---|---|---|---|---:|---|---|
---
> |---|---|---|---|---:|---|---|
50c50
< …The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
---
> …The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.
```

Exactly two hunks; `grep -c "new relation"` = 0 on the delivered map. Data-row discipline:

```
$ grep -E '^\| (J|S)[0-9]' baseline > rows-baseline ; grep -E '^\| (J|S)[0-9]' delivered > rows-repaired
$ diff rows-baseline rows-repaired   → empty ; cmp → identical (18 rows)
```

Receipts unchanged by the repair — I re-ran both tools on two scratch copies (one carrying the
committed pre-repair map, one the delivered post-repair map) at tool revision `86b52949…`:

```
support_check outputs IDENTICAL (diff empty; exit 0 both)
map_obligations outputs IDENTICAL (diff empty; exit 0 both) → OBLIGATIONS raw=16 mapped=16 / RESULT PASS
```

R4's own before/after snapshots (`R4-scratch/r96-support-{before,after}.txt`,
`r96-map-ob-{before,after}.txt`) also diff clean; R4 additionally proved the same under the frozen
`f3e09f9` tool revisions. r96 map sha: `5093d72e…` → `e851f068…`. Note (cross-seat context, not a
C3 verdict): R3 reports the r96 freeze digest is unchanged by this repair because the pin's file
set is the five JSON tables — the LOG's "digest" parenthetical is R3's C2 territory.

## 5. Whole-proposition trace — the r97 acknowledgment note

Excerpt section `fictional-excerpts.md:44-53` (heading 44, attribution 46, quoted lines 48-51,
scope 53). Four quoted propositions, each traced to excerpt clauses **and** JSON rows:

| # | Proposition (line) | JSON row/field it maps to | Trace verdict |
|---|---|---|---|
| A1 | "Tick 13: I received Evin's response at the Chalk Stair." (48) | `timeline.json#/5`: `tick=13`, `entity_id=aru`, `place_id=chalk-stair`, `depends_on=["response-evin-salt-court"]`, `description`, `source_id`; `sources.json#/5` title/kind | "Tick 13" literal; "at the Chalk Stair" literal; "I"=aru via attribution line 46 + `sources.json#/5` title "Aru's Chalk Stair Acknowledgment Note"; "Evin's response" = the inherited `response-evin-salt-court` record |
| A2 | "I hold to my own account; both accounts stand unresolved." (49) | `timeline.json#/5.description` ("states that both first-person accounts stand unresolved"); `sources.json#/5.reliability_note` (same); retained-account clause quoted in `claim-excerpt-map.md:57` and paraphrased in `README.md:9` ("while holding to his own account") | second clause exact; first clause carried by map/README, not verbatim in JSON — trace note O2, safe direction |
| A3 | "I make no accusation against Evin, and I select no winner between us." (50) | `description` ("asserts no accusation, no reconciliation, no winner between the accounts"); `reliability_note` ("not evidence of … an accusation, a winner between the accounts"); map `:57` quotes the line | negation, self-supported; no positive accusation anywhere |
| A4 | "I assert no reconciliation, no new duty, and no obligation beyond this crossing." (51) | `description` ("no reconciliation, no winner …, and no new duty beyond this crossing"); `reliability_note` ("not evidence of a resolution, a reconciliation, … a continuing duty"); map `:57` quotes the line; `README.md:11` ("asserts no reconciliation") | negation; crossing-only bound inherited from `relations.json#/0` / line 19 |

Paratext: attribution line 46 gives source ID `aru-acknowledgment-note` (equals `sources.json#/5.id`),
folio 7 lines 1–4 (exactly four quoted lines), and the sentence "This section is appended after the
preserved r96 text above; the inherited wording is unchanged." — verified true by the byte-prefix
test (§3). Scope line 53 traces clause by clause to lines 48-51 ("receipt only"; "no accusation";
"no reconciliation"; "no winner"; "no new duty"; agreement unchanged) and adds nothing.

Reverse direction (no orphan JSON): every field of the two new rows has an excerpt/attribution
counterpart — `timeline#/5`: `tick` ← "Tick 13" (editorial encoding, labeled), `entity_id` ←
attribution actor slot (labeled), `place_id` ← "at the Chalk Stair", `depends_on` ← editorial edge
(labeled), `description` ← lines 48-51, `source_id` ← attribution; `sources#/5`: `id`/`title`/`kind`
← attribution line 46, `reliability_note` ← lines 48-51 plus the receipt-only disclaimer. The
description and reliability note out-claim nothing: no new place, tick, motive, third account,
verdict, or truth claim; all added negations ("no accusation", "no reconciliation", "no winner",
"not evidence of a resolution …") are consistent with the quoted lines.

## 6. Core: constructibility of reconciliation / blame readings

Method: (a) lexical scan over every text surface and every JSON string with negation-context
flagging (`V43-scratch/scan.py` → `scan-final.txt`: 72 class hits, 6 `neg=False`, all benign — §9 O4);
(b) structural scan over `timeline.json` (same-entity/same-tick/different-place pairs;
`depends_on` resolution and forward-time order); (c) hand clause analysis of lines 44-53 and of
every surface that describes them (`sources.json#/5`, `timeline.json#/5`, `README.md:9,11,21`,
map `:18,38,51,57`, knowledge note); (d) schema probes on scratch copies (§7).

### 6.1 Reconciliation — NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| R1 | Receipt as acceptance: "I received Evin's response" read as recognition/acceptance of Evin's account | the same note bounds it: `:49` "I hold to my own account"; `:51` "I assert no reconciliation"; `sources.json#/5` "records receipt only and is not evidence of a resolution, a reconciliation" | fails — receipt ≠ endorsement; explicitly refused |
| R2 | Return to the scene: Aru at the Chalk Stair (tick 13) read as returning to reconcile | structural: no tick-13 Evin event (Evin's last is tick 12, salt-court), no meeting row, no relation or contradiction added (1 relation, `[]`); `README.md:9` "adds one receipt record; it does not change earlier locations" | fails |
| R3 | Pending resolution: "both accounts stand unresolved" + "between us" read as a live joint question awaiting settlement | unresolvedness is the record's stated stance, not a scheduled resolution; `:51` asserts none; map `:57`/README `:11` restate "remain unresolved" | fails as assertion |
| R4 | Absolution: "I make no accusation against Evin" read as clearing Evin | not accusing ≠ reconciling; negation; `:51`; the reliability note lists "an accusation" under "not evidence of" | fails |
| R5 | Exchange of notes as de facto reconciliation (reply-to-response shape) | no apology, no concession, no meeting, no merged account anywhere; every class token in the new bytes is negated (§6.3 scan) | fails |
| R6 | "Acknowledgment" itself read as acknowledging the other account's validity | `:53` "It records receipt only"; `sources.json#/5` same; the retained-account clause (`:49`) declines adoption | fails |

### 6.2 Blame — NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| B1 | Inherited "Evin did not come." (`:27`, r95 bytes) read as blame for non-arrival | inherited and bounded by `:29` "I assert no other duty, no breach"; reliability notes; not part of the new bytes | fails (inherited, already bounded at r95) |
| B2 | "I hold to my own account" (`:49`) read as implicitly charging Evin's account as false | no falsity/wrong/lied token anywhere; symmetry (Aru retains his own account without judging Evin's); `:50` "I make no accusation against Evin" | fails |
| B3 | Dismissal shape: receipt + no concession read as "your response changes nothing" (rebuke) | dismissal is not an accusation; `:50` asserts none; the record's own line blocks the reading | fails as assertion |
| B4 | Duty-presupposition: "no new duty" read as implying a duty existed and was breached | `:51` is a negation; crossing-only relation (`:19`); `sources.json#/4-5` disclaimer pattern "not evidence of a breach, a continuing duty"; presupposition only | constructible as *presupposition*; fails as assertion |
| B5 | Blame by omission: Aru's silence about Evin's alibi read as implicit doubt | absence of comment is not an assertion; `:50`; no surface asserts fault | fails |
| B6 | Fault/guilt/breach tokens in the new bytes | zero non-negated hits; every `accus`/`breach`/`blam`/`fault`/`guilt` occurrence lies under negation (scan §6.3) | fails |

Token corroboration (tight-window check on the new surfaces only — excerpt lines 44-53,
`sources.json#/5`, `timeline.json#/5`): every hit is negated — "no reconciliation" ×2,
"stand unresolved", "no accusation" ×2, "no winner" ×2, "not evidence of a resolution, a
reconciliation, an accusation, a winner". No `blame/fault/guilt/wrong/lied/liar/forgive/pardon/
settle` token exists in the new bytes at all.

### 6.3 Resolution / winner — bounded extension, also NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| S1 | Supersession: tick-13 event depends on the tick-12 response → later account wins | dependence ≠ truth precedence; `README.md:13` / map `:51` disclose ticks/edges as editorial encodings; `:50` "I select no winner between us" | fails |
| S2 | "Unresolved" read as a pending resolution | no scheduled resolution; `:51`; map `:57` "remain unresolved" | fails |
| S3 | Structural conflict: same actor at two places at one tick, or forward/unresolvable edges | scan: zero same-actor/same-tick/different-place pairs; all `depends_on` edges resolve backward (9<10<11<12<13); `contradictions.json` `[]` | fails |

**Result:** on the delivered bytes no reading survives in which the fixture *asserts* a
reconciliation, a blame/fault, or a resolution/winner. The closest constructions (R6, B4) are
presuppositional residues, each blocked by the record's own explicit negations; the record
positively asserts unresolvedness ("both accounts stand unresolved", `:49`), which is stronger
than mere absence and holds.

## 7. Schema probes — the restraint is editorial, not schema-forced

On scratch copies only (`V43-scratch/probe-*/`, built from the frozen fixture; script
`V43-scratch/probes.py`):

- **Reconciliation probe**: appended an entity claim "Aru and Evin reconciled at the Chalk Stair
  and the two accounts were merged into one settled record." plus a relation
  `reconciled_after_crossing_dispute` → `check_bible` `CLEAN: schema, citations, relations,
  timeline; 0 violations`, exit 0.
- **Blame probe**: appended an entity claim "Aru blames Evin for the non-arrival and asserts Evin
  breached the crossing agreement." → `CLEAN … 0 violations`, exit 0.
- **Contradiction probe**: appended a `contradictions.json` ledger row over the two accounts →
  `CLEAN … 0 violations`, exit 0.

So all three classes are mechanically encodable and would pass the delivered gate. The fixture's
empty ledger and its negated surfaces are an *editorial choice*; the claim "not asserted" is an
editorial-content claim that no structural gate can confirm — only manual review can. This seat
performed that review; the delivered bytes decline all three classes.

## 8. Cross-checks against producer reports

- **R4 (fixture-author)**: delivered hashes, counts 5/1/6/6, census 171, the repair diff, the
  byte-prefix append, and the pre-R5 `raw=17 mapped=16 / missing_obligation: timeline.json#/5`
  state all reproduce. R4's frozen-tool before/after receipt proof agrees with mine.
- **R5 (fixture-docs)**: map `49d4834e…` and README `d9387b7d…` reproduce; declared inventory
  17/2/19/15, J17 row, anchors-at-identical-lines, and the parser-level inherited-row identity all
  reproduce. R5's caveat about `corpus/fixtures/README.md` still stating the r96 census is true
  (§9 O5).
- **R6 (knowledge note)**: `corpus/knowledge/r97-acknowledgment-scope-note.md` exists; I ran R6's
  own path/line verifier (`R6-scratch/verify_note.py`) → `BASIC BAD: 0`, and its cited map lines
  (J17 at `:38`, bounded reading at `:57`) match the delivered map. Its class definition ("receipt
  only; no resolution, no reconciliation") matches the delivered bytes.
- **R1/R2 (C1 tools)**: my `map_obligations` receipts are pinned to R1's declared delivered
  revision `86b52949…` with contract `2142b991…`; C1's self-test/loader claims are not judged by
  this seat.
- **R3 (C2 gate)**: report landed seconds after my poll window (18:56:23); C2 claims are not judged
  here. One cross-seat context note: R3 records that the r96 freeze digest is unchanged by R4's
  cosmetic repair (the pin's file set is the five JSON tables), i.e. the LOG's "digest" parenthetical
  is inaccurate — that correction belongs to R3's seat and the integrator, not to C3.

## 9. Bounded observations (not failures; for later rounds / other seats)

- **O1 — map line 18 wording is precise for r97.** "The 16 inherited rows carry the r96 JSON
  pointers … unchanged" is true for all 16 (every pointer existed in r96); the r96 map's analogous
  "r94" sentence was the imprecise one (J15 was created at r95) and this round's repair replaced
  the other stale sentence. No issue in the delivered r97 map.
- **O2 — trace note, safe direction.** `timeline.json#/5.description` and
  `sources.json#/5.reliability_note` summarize lines 48-51 without the retained-account clause
  "I hold to my own account" verbatim; that clause is quoted in map `:57` and paraphrased in
  README `:9`. No out-claiming; recorded so a later round can decide whether the JSON summaries
  should carry it.
- **O3 — disclaimer paraphrase.** `sources.json#/5` says "not evidence of a resolution …" while the
  note says "no reconciliation"; "resolution" is disclaimer vocabulary consistent with the
  unresolved/reconciliation negations. Non-blocking.
- **O4 — six `neg=False` lexical hits, all benign.** `README.md:9` "convert either account into a
  verdict" (negated by "does not … resolve or create a contradiction, or convert"); map `:18`
  "resolved here as"/"resolves as" ×2 (namespace-resolution terminology); `source-excerpt.md:7`
  "The locator resolves to the printed-page marker" (bibliographic); `sources.json:36`
  "not evidence of a resolution, a reconciliation, an accusation, a winner" (the whole list is
  negated by "not evidence of"; window artifact). No positive assertion.
- **O5 — fixtures README freshness (doc-side).** `corpus/fixtures/README.md` still carries only the
  Round-96 section (no Round-97 append) and its census text at `:1217` states 170 (measured now:
  171); its `:1213` "r97 candidates" debt text (delimiter cell, "new relation") is now stale since
  this round fixed both. The measured C3 numbers hold; the README text update is a closure-side
  documentation task, read-only for this seat.
- **O6 — tool churn under seats.** `map_obligations.py` moved `2b0ba815…` → `c1881149…` →
  `86b52949…` during the round; all receipts above are pinned to `86b52949…` and agree with R1's
  declared delivered revision. Re-run at closure before citing.
- **O7 — the repair's new sentence is a true negation.** The r96 map's replacement sentence
  ("asserts no reconciliation, selects no winner …") adds the word "reconciliation" to the r96
  map; it is a negative statement consistent with the r96 bytes and is the declared C3 repair
  (receipts unchanged, §4). No over-claim.

## 10. Limits of this seat

Same-lane replica review on the delivered bytes; lexical/structural plus hand clause analysis.
Not source authentication, not canon truth, not rights or permission review, not an admission
decision, and not a verdict on C1 (map_obligations pinning) or C2 (dependency_freeze hardening).
Producer reports and the R6 knowledge note were read for cross-consistency only. Probes ran on
scratch copies; no corpus file was written by this seat.

**Bottom line: PASS — the r97 C3 whole claim replicates on the delivered bytes: the new note's
four propositions (lines 48-51) trace clause-by-clause to `timeline.json#/5` and `sources.json#/5`
with no orphan field or out-claim; no reconciliation, blame, or resolution/winner reading is
constructible as an assertion (all class tokens in the new bytes lie under negation, the ledger is
empty, all edges resolve backward, and appended reconciliation/blame/contradiction rows pass
`check_bible` CLEAN — so the restraint is editorial and was verified by manual review, not by gate
outcomes); the r96 cosmetic repair is byte-minimal (two lines, 18 data rows byte-identical,
receipts unchanged); and the C3 numbers reproduce (5/1/6, 6 sources, 17 obligations, census 171,
`check_bible` CLEAN, `support_check` 17/17 / 19/19 / 15/15 PASS, `map_obligations` raw=17 mapped=17
PASS, all exit 0) — with bounded observations O1–O7 for later rounds.**
