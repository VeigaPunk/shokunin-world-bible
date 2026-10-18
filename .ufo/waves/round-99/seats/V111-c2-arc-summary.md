# V111 — c2-arc-summary (round 99)

Seat: V111. Leaf verifier. No commits, no pushes, no network, no nested agents. Exclusive write: this report. Scratch: `.ufo/waves/round-99/seats/V111-scratch/` (`poll.log`, `poll.pid`). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands below ran from that root with `python3` unless noted. Baseline commit `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at measurement: `337f0fa` (blocked-dispatch commit; prior-beat fixtures and r94–r98 knowledge notes are clean against `4265df5`).

This seat produces the arc cross-reference. It does not author fixture or knowledge bytes. Every cell below was checked against the files named. `support_check` / `map_obligations` receipts are lexical, not whole-claim entailment.

## Poll-wait (artifacts and producer reports; never a plan)

Needed for this seat: the six fixture directories, and the knowledge notes that cross-reference them. S3 and S4 reports were already on disk before the timed poll (`S3-fixture-author.md` 22:01, `S4-fixture-docs.md` 22:03). S5’s `corpus/knowledge/r99-lapse-scope-note.md`, `corpus/knowledge/r99-gate-blind-spot-table.md`, and any `S5*.md` report were absent at poll start (22:07:12) and after 40 tries.

```
try=1  22:09:49 note=[ABSENT] report=[ABSENT]
try=40 22:22:49 note=[ABSENT] report=[ABSENT]
ABSENT after 40 tries 22:23:09
```

Full log: `.ufo/waves/round-99/seats/V111-scratch/poll.log`. No stall-escape. ENDGAME subtract-SELF was not reached: this seat did not poll other verifier reports. Re-check at 22:23:09 and again before this write: still no `corpus/knowledge/r99*` and no `S5*.md`. The r99 knowledge-note cell is ABSENT. The table does not invent that note.

S3’s report says README and claim-excerpt-map were still r98 copies. That was true at S3’s write. S4 rewrote both. This pass measured the post-S4 bytes (README sha256 `b9320941…`, map `d2fe20e5…`, both unchanged from S4’s report and stable through 22:23).

## Numbering

The declaration calls `r99-window-lapse` the fifth beat. `corpus/knowledge/r98-clerk-scope-note.md:14` calls r98 the fourth beat and counts r95, r96, r97, r98. The seat brief lists six stages (minute plus five continuation beats). The table has six rows. Beat index below follows the r98 note (r95 = beat 1 … r99 = beat 5). r94 is the originating minute, not one of those five.

## Cross-reference table (verified this pass)

| Stage | Fixture | Knowledge record | E/R/Ev/S | Terminal event | Tick / actor / place / depends_on | Map | Unresolved-throughout |
|---|---|---|---|---|---|---|---|
| Origin minute | `corpus/fixtures/r94-paired-crossing` | `corpus/knowledge/r94-cross-myth-design-comparison.md` addendum `:19-23` (body `:12` is superseded prospective text; do not cite it as current) | 5/1/3/3 | `paired-crossing-decision` | 10 / `aru` / `chalk-stair` / `aru-ninth-bell`,`evin-ninth-bell` | 14/14 | No dispute yet. No resolution, blame, finding, or winner token. Relation is crossing-only. `contradictions.json` `[]`. |
| Beat 1 aftermath | `corpus/fixtures/r95-crossing-aftermath` | `corpus/knowledge/r95-aftermath-scope-note.md` class “Reported non-performance” `:11` | 5/1/4/4 | `aftermath-missing-evin` | 11 / `aru` / `chalk-stair` / `paired-crossing-decision` | 15/15 | Report of non-arrival. Asserts no breach and no other duty. Does not use the word “unresolved”. Does not resolve. `[]`. |
| Beat 2 response | `corpus/fixtures/r96-crossing-response` | `corpus/knowledge/r96-response-scope-note.md` class “Second first-person account … unresolved” `:11` | 5/1/5/5 | `response-evin-salt-court` | 12 / `evin` / `salt-court` / `aftermath-missing-evin` | 16/16 | First explicit “Both accounts stand unresolved.” No accusation, no winner. `[]`. |
| Beat 3 acknowledgment | `corpus/fixtures/r97-crossing-acknowledgment` | `corpus/knowledge/r97-acknowledgment-scope-note.md` “third beat” `:14` | 5/1/6/6 | `acknowledgment-aru-records` | 13 / `aru` / `chalk-stair` / `response-evin-salt-court` | 17/17 | Receipt only. “both accounts stand unresolved.” No accusation, no reconciliation, no winner, no new duty. `[]`. |
| Beat 4 filing | `corpus/fixtures/r98-clerk-filing` | `corpus/knowledge/r98-clerk-scope-note.md` “fourth beat” `:14` | 6/1/7/7 | `clerk-filing-open` | 14 / `clerk-maren` / `chalk-stair` / `acknowledgment-aru-records` | 20/20 | Matter recorded OPEN. “no finding and no resolution.” No verdict, reconciles nothing. `[]`. |
| Beat 5 lapse | `corpus/fixtures/r99-window-lapse` | **ABSENT** — `corpus/knowledge/r99-lapse-scope-note.md` not on disk after 40 polls. Fixture README `:11` and excerpt `:66-76` are the delivered record. | 6/1/8/8 | `clerk-lapse-recorded` | 15 / `clerk-maren` / `chalk-stair` / `clerk-filing-open` | 21/21 | Window-closed is the clerk’s report, not matter-closed. “no resolution”, “no blame”, “reconcile nothing”, “matter stays open”. `[]`. |

Catalog cross-refs in `corpus/fixtures/README.md` (unchanged this round; no Round 99 section; file ends at the r98 census declaration): Round 94 `:1154`, Round 95 `:1177`, Round 96 `:1198`, Round 97 `:1221`, Round 98 `:1244`. Directory census measured here is 173; that README still says 172. The README is unowned this round. The +1 is only `r99-window-lapse`.

## Per-beat records (quotes checked in the named file)

**Origin — r94 minute.** Relation, identical in all six fixtures (`relations.json` sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`, 139 bytes): `from: aru`, `to: evin`, `type: agreed_co_stewardship_for_this_crossing`, `source_id: crossing-minute`. Minute text, byte-identical at `fictional-excerpts.md:17-20` in r94 and in r99:

> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
> Their tick-10 decision depends on both ninth-bell entries: …

`sources.json` reliability note for `crossing-minute`: “records one bounded crossing decision and agreement, not evidence of continuing performance, a standing alliance, or an external historical fact.” Event description: “At the Chalk Stair, Aru and Evin agree to share stewardship for this crossing only, then chalk one temporary route mark.” The token `window` does not occur in this minute, in r94 `sources.json`, or in r94 `timeline.json`.

**Beat 1 — r95.** New source `aru-aftermath-note`. Excerpt `:26-29`: “Tick 11: I waited at the Chalk Stair through the agreed bell. / Evin did not come. / The agreement we chalked covered this crossing only. / I assert no other duty, no breach, and no obligation beyond this crossing.” Those four strings are in the r95 excerpt (`True` this pass). Knowledge note `:11` defines the class as a report, not world-absence, fault, or a broken obligation. Prefix: `entities`/`relations`/`timeline[:3]`/`sources[:3]` equal r94. Map J01–J14 inherited with 0 non-namespace diffs; new row J15 `timeline.json#/3`.

**Beat 2 — r96.** New source `evin-response-note`. Excerpt `:37-40`: “Tick 12: I was at Salt Court through the same agreed bell. / I make no accusation against Aru. / I select no winner between our two accounts. / Both accounts stand unresolved.” Present in the r96 excerpt. Knowledge note `:11` and `:20` match. Prefix equal to r95. New map row J16 `timeline.json#/4`. Different actor and place from tick 11 (`aru`/`chalk-stair` vs `evin`/`salt-court`); no contradiction row added.

**Beat 3 — r97.** New source `aru-acknowledgment-note`. Excerpt `:48-51`: “Tick 13: I received Evin's response at the Chalk Stair. / I hold to my own account; both accounts stand unresolved. / I make no accusation against Evin, and I select no winner between us. / I assert no reconciliation, no new duty, and no obligation beyond this crossing.” Present. Knowledge note `:14` names this the third beat and says the arc still carries exactly two accounts. Prefix equal to r96. New map row J17 `timeline.json#/5`. `entities.json` still byte-identical to r94 (sha256 `026af0bc…`).

**Beat 4 — r98.** New entity `clerk-maren`, new source `clerk-filing-note`, new event `clerk-filing-open`. Excerpt `:59-62`: “Tick 14: I filed both pending accounts at the Chalk Stair registry. / I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN. / I assert no finding. / I reach no verdict and reconcile nothing.” Scope `:64`: “the two first-person accounts stand unresolved”. Timeline description: “recorded the matter OPEN, asserting no finding and no resolution.” Knowledge note `:14` names this the fourth beat; `:23-25` match those quotes (re-checked `True` in the r98 files). Inherited prefix: entities `[:5]` equal r97, sources `[:6]` equal r97, timeline `[:6]` equal r97, relation unchanged. New map rows J18–J20 (first appearance, claim, event). Obligations 17 inherited + 3 = 20.

**Beat 5 — r99.** No new entity. New source `clerk-lapse-note` (“Maren's Chalk Stair Lapse Note”). New event `clerk-lapse-recorded`, tick 15, `entity_id: clerk-maren`, `place_id: chalk-stair`, `depends_on: ["clerk-filing-open"]`, `source_id: clerk-lapse-note`. Description: “the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.” Excerpt `:70-74`:

> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.

Scope `:76`: “the matter stays open.” Reliability note in `sources.json`: asserts no resolution, no blame, and no reconciliation; “not evidence of a breach finding, a continuing duty, a winner between the accounts, or an external historical fact.” README `:3` states 6/1/8/8. README `:11` states the lapse bound (window closed per the minute’s terms; agreement unfulfilled; no claim lodged; historical open entry; matter stays open; no resolution, no blame, no reconciliation; closes no one). Map declares 21 JSON facts; J21 is `timeline.json#/7`, span 66-76, anchor the tick-15 sentence, hit at excerpt line 70. Inherited J01–J20: 0 diffs outside the namespace column; 20/20 namespace rewrites are `r98-clerk-filing:` → `r99-window-lapse:` only (sample J01 `paired-clock`, J20 `clerk-filing-note`). Excerpt byte-prefix: r98 `fictional-excerpts.md` (4187 bytes) is a prefix of r99 (5114); the next byte is a newline. `entities.json` byte-identical to r98 (`db2d8e5d…`). Relation, `contradictions.json`, `inspiration-note.md`, and `source-excerpt.md` are the same payload in all six fixtures.

“No claim was lodged” is the clerk’s in-world sentence. It is not a statement that `entities.json` has zero claims. The fixture still has the inherited entity claims (six claim rows: five from r94 plus Maren’s filing claim). Do not conflate those JSON claims with a lodged crossing-claim.

## Unresolved-throughout invariant

Definition used: no beat’s delivered record asserts a resolution, a finding that closes the matter, blame, a winner, a reconciliation, or a non-empty contradiction ledger. The relation stays the crossing-only agreement. “Window closed” is a different predicate from “matter closed.”

| Predicate | r94 | r95 | r96 | r97 | r98 | r99 |
|---|---|---|---|---|---|---|
| Token `unresolved` in fixture prose/JSON | no | no | yes | yes | yes | yes |
| Positive resolution / winner / blame / finding | none found | none found | none found | none found | none found | none found |
| Explicit non-resolution | (no dispute yet) | no breach / no other duty | both accounts unresolved; no accusation; no winner | no reconciliation; unresolved | matter OPEN; no finding; no resolution | no resolution; no blame; reconcile nothing; matter stays open |
| `contradictions.json` | `[]` | `[]` | `[]` | `[]` | `[]` | `[]` |
| Relation payload | origin | equal | equal | equal | equal | equal |

A sentence scanner flagged `claim-excerpt-map.md:18` in every beat for the word “resolved”. Those lines are namespace wording (“resolved here as `r99-window-lapse:…`”), not a canon resolution. They are not invariant breaks. The only non-negated `closed` hits in r99 are the crossing-window sentences (excerpt `:70`, map J21, timeline description). The same note, same section, says the matter stays open (`:73`, `:76`).

**Bound, not a minute-text fact:** the lapse note says the crossing-window was “named in the original minute.” The minute bytes (`fictional-excerpts.md:17-20`, identical in r94 and r99) contain no token `window`. `rg -i window` over r94–r98 fixtures and r94–r98 knowledge notes returned no hits. The minute’s own terms are “for this crossing only” and a bounded decision, not a named window. README `:11` “per the original minute’s terms” is an editorial gloss. The verified fact is the clerk’s report, not a lexical naming in the minute. That gap does not resolve the matter and does not add blame.

## Commands and observed output

Census and baseline:

```
$ git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l
172
$ ls -d corpus/fixtures/*/ | wc -l
173
$ comm -13 <(git ls-tree -d --name-only 4265df5:corpus/fixtures | sort) <(ls -d corpus/fixtures/*/ | sed 's#corpus/fixtures/##;s#/##' | sort)
r99-window-lapse
$ git diff --stat 4265df5 -- corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r98-clerk-filing corpus/knowledge/r94-cross-myth-design-comparison.md corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md corpus/knowledge/r97-acknowledgment-scope-note.md corpus/knowledge/r98-clerk-scope-note.md
(empty)
```

Gates, this pass, each exit 0:

```
r94  check_bible CLEAN; support JSON-FACTS 14/14 TOTAL-ROWS 16/16 RESULT PASS; map raw=14 mapped=14 PASS
r95  check_bible CLEAN; support JSON-FACTS 15/15 TOTAL-ROWS 17/17 RESULT PASS; map raw=15 mapped=15 PASS
r96  check_bible CLEAN; support JSON-FACTS 16/16 TOTAL-ROWS 18/18 RESULT PASS; map raw=16 mapped=16 PASS
r97  check_bible CLEAN; support JSON-FACTS 17/17 TOTAL-ROWS 19/19 RESULT PASS; map raw=17 mapped=17 PASS
r98  check_bible CLEAN; support JSON-FACTS 20/20 TOTAL-ROWS 22/22 RESULT PASS; map raw=20 mapped=20 PASS
r99  check_bible CLEAN; support JSON-FACTS 21/21 EDITORIAL-ROWS 2/2 TOTAL-ROWS 23/23 DISTINCT-ANCHORS 19/19 SOURCE-SUPPORT 21/21 RESULT PASS; map raw=21 mapped=21 PASS
```

r99 `support_check` J21 line, quoted: `PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.`

Prefix script (parsed JSON equality, not a string compare of whitespace): each beat’s entities/timeline/sources are a prefix of the next; relations equal at every step; contradictions equal at every step; new counts are 0 entities except r97→r98 (+1 `clerk-maren`), and +1 event and +1 source at each continuation. Excerpt prefixes all `True` with the following byte a newline. Map inheritance diffs outside namespace: 0 at every step. r98→r99 namespace rewrites: 20, unexpected: 0.

r99 sha256 at 22:23 (unchanged from the gate run and from S4’s report):

```
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
```

Knowledge-note sha256 (byte-identical to `4265df5`; r95/r96 match the r98 V56 closure hashes):

```
e039c57764678be35d922a2736f4c9732304a1cd241adcb37275c709ba112402  r94-cross-myth-design-comparison.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  r96-response-scope-note.md
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  r97-acknowledgment-scope-note.md
47a5967bb0d674a6cc2c60d4be3150d315bd66578627c3192cde8fea1f4931a7  r98-clerk-scope-note.md
```

## Not verified

- `corpus/knowledge/r99-lapse-scope-note.md` and `corpus/knowledge/r99-gate-blind-spot-table.md`: ABSENT. No cell in this table cites them.
- `corpus/fixtures/README.md` has no Round 99 section. Directory census 173 is measured; the README’s 172 figure is the r98 declaration, not re-measured by a full clean/negative corpus run this seat.
- Freeze pins and C1 Markdown-tamper behavior are S1’s contract. Not run here.
- `support_check` PASS is not proof that the minute lexically names a window. That negative finding is the `rg` result above.

PASS — six-stage arc verified on delivered fixture bytes (5/1/3 → 6/1/8, maps 14→21, gates exit 0, prefixes hold, unresolved-throughout holds); r99 knowledge-note cell ABSENT after 40 polls; “window named in the minute” is the clerk’s report, not a minute token.
