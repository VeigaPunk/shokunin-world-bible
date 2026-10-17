# V46 — whole-claim-replica-2: constructibility of accusation / winner / contradiction readings

Seat: V46, round 96, lane `lore-shokunin`. Scope of this seat: second independent
whole-claim replica review of the r96 C2 fixture, with one explicit obligation —
**attempt to construct accusation, winner, and contradiction readings over the delivered
bytes and report their constructibility**. Target claim (LOG.md r96 C2): "second account,
same occasion, UNRESOLVED (no accusation, no winner, no contradiction asserted)".

All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`;
scratch and probe copies under `.ufo/waves/round-96/seats/V46-scratch/`. No corpus file
was modified by this seat (`git status --porcelain` after my work: ` M LOG.md` (pre-seat),
` M corpus/tools/map_obligations.py` (Q1, in flight), `?? .ufo/waves/round-96/`,
`?? corpus/fixtures/r96-crossing-response/`, `?? corpus/knowledge/r96-response-scope-note.md`,
`?? corpus/tools/dependency-freeze-contract.json`, `?? corpus/tools/dependency_freeze.py`).

## 0. Poll-wait log

Poll cadence 20 s, 40 tries. First check 17:38: fixture directory absent (Q1 tool not yet
in tree either). Q4's eight files landed 17:38–17:40; README/map 17:43–17:44; Q4 report
17:42; Q5/Q6 reports 17:45; POLL_HIT check=22 elapsed=440s (20:45:49 UTC). No ABSENT
condition arose. One in-flight artefact noted and handled: `map_obligations.py` was being
rewritten by Q1 across my receipt window (hashes seen: `d1c239cc…` r95 revision →
`965c1ec4…` → `44a6ffd4…` → `c2c284c0…` → `6634e176…`); at two intermediate revisions the
tool crashed (`ValueError: too many values to unpack (expected 4, got 5)` on r95/r94) or
returned all-`None` source IDs on r96. Those are in-flight states of Q1's own claim, not
the delivered r96 revision; every receipt below is labelled with the revision it ran at.

## 1. Delivered revision identity

```
$ sha256sum corpus/fixtures/r96-crossing-response/*
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  timeline.json
```

These equal Q4's reported hashes (five byte-copies, `sources.json`, `timeline.json`,
`fictional-excerpts.md`) and Q5's reported hashes (`README.md` `ff52ced4…`, map
`5093d72e…`); the revision I reviewed is the delivered one. Preservation vs r95
(`cmp` / byte-prefix test, python3):

```
BYTE-IDENTICAL: entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md
sources.json : len r95=1225 r96=1741; r95-minus-final-'\n]' is byte prefix=True
               r95[1222:1230]=b'\n]\n'  r96[1222:1230]=b',\n  {\n  '
timeline.json: len r95=1254 r96=1677; r95-minus-final-'\n]' is byte prefix=True
fictional-excerpts.md: len r95=1845 r96=2588; whole r95 file is a byte prefix=True
```

So the five byte-copies are exact; the two extended tables have every inherited byte
preserved with the new record appended after the join comma; the excerpt file is a pure
append (append starts line 32). Q4's documented pre-receipt correction (join comma moved
off its own line, rewritten 17:39) is consistent with the delivered seam `},\n  {`.

## 2. Gate receipts on the delivered fixture

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations                 exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; …; MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                                 exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                                 exit=0
```

Tool revisions at my receipts: `check_bible.py` `ff9fd2aa…` and `support_check.py`
`55a5eb27…` (unchanged all round); `map_obligations.py` `c2c284c0…` and `6634e176…`
(Q1's hardening still in flight; PASS reproduced at both, and Q5 recorded PASS at its
bracketed `8cbcdb51…`). Post-report re-check at the newest tool revision `2b0ba815…`
(17:49): r96 `raw=16 mapped=16 … RESULT PASS exit=0` again; fixture bytes unchanged
(`README` `ff52ced4…`, map `5093d72e…`, `sources.json` `9f973f63…`, `timeline.json`
`ea0225f9…`). The `map_obligations` receipt is therefore bracketed, not pinned;
the C2 count it confirms (16 raw obligations) I also computed independently from the raw
JSON: 5 `first_appearance` + 5 entity claims + 1 relation + 5 timeline rows = 16.

Inheritance and census (this seat):

```
r95 map rows: J01..J15,S01,S02 (17)   r96 map rows: J01..J16,S01,S02 (18)
rows differing after cluster-prefix normalization (r95:→r96:): []      (zero)
only r96: ['J16']   only r95: []
census: now=170  baseline(dcb2d92)=169   new dirs vs baseline: r96-crossing-response (exactly one)
```

Counts: entities 5 / relations 1 / timeline 4→5 / sources 4→5; `contradictions.json`
byte-identical to r95 (`[]`). All C2 numeric claims replicate.

## 3. Core: constructibility of the three readings

Method: (a) lexical scan over every text surface and every JSON string (classes =
accusation / winner / contradiction token sets, with negation-context flagging,
`.ufo/waves/round-96/seats/V46-scratch/scan3.txt`); (b) structural scan over `timeline.json`
(same-entity/same-tick/different-place pairs; `depends_on` resolution and forward-time
order); (c) hand clause analysis of the new section (lines 33–42) and of every surface
that describes it (`sources.json#/4`, `timeline.json#/4`, `README.md:9,11`, map J16
paragraph `:54`, `corpus/knowledge/r96-response-scope-note.md`); (d) schema probes on
scratch copies (see §4).

### 3.1 Accusation — NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| A1 | "Evin did not come" (`fictional-excerpts.md:27`) read as an accusation of non-performance | the same note bounds it: `:28-29` "no other duty, no breach, no obligation beyond this crossing"; `sources.json:24` "not evidence of a breach" | fails — requires deleting the note's own bound (r95 V36 §4D, inherited) |
| A2 | Evin's note read as a counter-accusation | `:38` "I make no accusation against Aru."; `:39-40` no winner, unresolved | fails — explicitly refused |
| A3 | **Strongest**: `:37` "I was at Salt Court through the same agreed bell" has alibi shape; an alibi presupposes a charge | the only charge-shaped surfaces are negated; no surface names any charge against either actor; "no accusation against Aru" presupposes accusability but the record supplies no fillable content | constructible as *presupposition*; fails as assertion (bounded, §5 O3) |
| A4 | Fixture prose as accusation | `README.md:11`, map `:54`, `sources.json:30`, `timeline.json:52` — all negated | fails |

Token scan corroboration: every `accus*`/`breach`/`blam*`/`fault`/`guilt*` hit in the
whole fixture lies inside a negation (`neg-before=True` in scan3.txt; the four
`neg-before=False` hits are all benign — see §5 O1). No surface asserts a fault, charge,
or breach.

### 3.2 Winner — NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| B1 | Recency/supersession: tick-12 response `depends_on` tick-11 report → later account wins | `:39` "I select no winner between our two accounts."; `README.md:13` and map `:50` disclose ticks/edges as editorial encodings of stated order/dependence | fails — dependence ≠ truth precedence; refused explicitly |
| B2 | Corroboration of Evin by the inherited register (`paired-clock` places Evin at Salt Court, tick 9) | register covers tick 9 only; its reliability note: "does not establish a wider chronology"; the bell occasion is not covered | fails |
| B3 | Corroboration of Aru by the tick-10 minute (meeting at the Chalk Stair) | minute covers tick 10 only; consistency ≠ corroboration of the bell/waiting | fails (symmetric with B2) |
| B4 | "Both accounts stand unresolved" read as a pending resolution → a winner is coming | unresolvedness is the record's stated stance, not a selection | fails as assertion |
| B5 | Non-denial as concession (Evin does not deny "did not come") | Evin asserts only his own location; the two accounts are jointly satisfiable (§3.3 C2), so nothing is conceded | fails |

### 3.3 Contradiction — NOT constructible as an assertion

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| C1 | Ledger reading | `contradictions.json` = `[]`, byte-identical to r95/r94 (`37517e5f…`) | fails |
| C2 | Strict incompatibility: "Evin did not come [to the Chalk Stair]" ∧ "I was at Salt Court" | different places → jointly satisfiable (Evin can be at Salt Court and not come to the Chalk Stair); `README.md:11`: "The accounts name different actors at different places … so no contradiction is asserted" | fails |
| C3 | **Sharpest**: same-bell-two-ticks — Aru "through the agreed bell" (Tick 11) vs Evin "through the same agreed bell" (Tick 12); one bell occasion under two tick labels | both are "through" a bell duration; `README.md:13` / map `:50` disclose the tick integers as editorial encodings of the notes' tick labels; no surface asserts a bell is instantaneous or that tick = event time | bounded ambiguity; fails as asserted contradiction |
| C4 | "Both accounts stand unresolved" + "does not resolve the two first-person accounts against each other" (`:42`) presuppose a live question / opposition | unresolvedness ≠ incompatibility; the same surfaces state no contradiction is asserted and the ledger stays empty | constructible as *framing implication*; fails as assertion (bounded, §5 O3) |
| C5 | Structural: same actor at two places at the same tick | scan: zero candidate pairs; Aru quiet-rise(9)→chalk-stair(10,11); Evin salt-court(9,12) | fails |
| C6 | Structural: `depends_on` forward-time or unresolvable edges | all edges resolve; 11 < 12, 10 < 11, 9 < 10 | fails |

Structural scan output: `(end of structural candidates)` — no conflict candidates at all;
`contradictions.json = []`.

**Result:** on the delivered bytes no reading survives in which the fixture *asserts* an
accusation, a winner, or a contradiction. The three closest constructions (A3, C3, C4) are
presupposition/referent ambiguities, each blocked by the record's own explicit negations or
by the disclosed editorial tick encoding. C2's "UNRESOLVED" wording is also *stronger* than
mere absence and it holds: the record itself asserts unresolvedness (`:40`,
`sources.json:31`, `timeline.json:52`, `README.md:11`, map `:54`).

## 4. Schema probes — the restraint is editorial, not schema-forced

To bound the claim's meaning I tested whether the delivered structural gate could even
*speak* about these classes. On scratch copies only
(`.ufo/waves/round-96/seats/V46-scratch/probe-*/cluster`):

- **Contradiction probe**: appended one `contradictions.json` row over the account pair
  (`aftermath-missing-evin.place_id` vs `response-evin-salt-court.place_id`) →
  `check_bible` `CLEAN … 0 violations`, exit 0.
- **Accusation + winner probe**: appended an entity claim "Aru accuses Evin of breaking the
  chalked crossing agreement" and a relation `type: "winner_selected_aru_account_prevails"`
  → `check_bible` `CLEAN … 0 violations`, exit 0.

So all three classes are mechanically encodable and would pass the delivered gate. The
fixture's empty ledger and its negated surfaces are an *editorial choice*, and the claim
"not asserted" is an editorial-content claim that no structural gate can confirm — only
manual review can. This seat performed that review; the delivered bytes decline all three.

## 5. Bounded observations (not failures; for later rounds / other seats)

- **O1 — map wording, one row.** `claim-excerpt-map.md:18`: "The 15 inherited rows carry the
  r94 JSON pointers, excerpt anchors, spans, and delivery modes unchanged". J15's pointer
  `timeline.json#/3` was created at r95, not r94, so "r94" is imprecise for that one row
  (the r95 map's equivalent sentence covered J01–J14 and was exact). Row *content* is
  unaffected: after cluster-prefix normalization all 15 inherited rows are identical to
  r95's (my diff: zero differences), and the count is 16 = 15 + 1. Cosmetic doc fidelity.
- **O2 — carried referent gap.** The r95 "the agreed bell" gap (r95 V36 §4A) persists:
  Evin's "the same agreed bell" (`:37`) asserts referent identity with Aru's bell but no
  row states which agreement established the bell. It is not an accusation/winner/
  contradiction reading and does not harm C2.
- **O3 — presuppositional residues.** "I make no accusation against Aru" presupposes
  accusability; "our two accounts"/"unresolved"/"against each other" presuppose a live
  question. All are denials or framing, none is a positive assertion; recorded as the
  closest surviving constructions (A3, C4).
- **O4 — Q4's pre-receipt seam rewrite.** Only the delivered revision was reviewed
  (seam `},\n  {`, valid JSON, `check_bible` CLEAN). No receipt in this report was taken
  against the discarded intermediate.
- **O5 — four `neg-before=False` lexical hits, all benign.** `README.md:7` and `:9`
  ("…or contradiction", "resolve or create a contradiction") are negated in the fuller
  sentence but outside my 30-char window; `claim-excerpt-map.md:18` "resolved here as
  `r96-crossing-response:paired-clock`" uses "resolved" for namespace resolution; `:56`
  "not manual whole-claim entailment or a verdict on …" is negated. No positive assertion.

## 6. Limits of this seat

Same-lane replica review on the delivered bytes; lexical/structural plus hand clause
analysis. Not source authentication, not canon truth, not rights or permission review, not
an admission decision, and not a verdict on C1/C3 (their tools were in flight during this
seat). Q6's knowledge note and Q4/Q5 reports were read for cross-consistency only. I wrote
only this report plus scratch under `.ufo/waves/round-96/seats/V46-scratch/`; probes ran on
scratch copies, never on corpus files.

**Bottom line: PASS — the r96 C2 fixture's whole claim replicates on the delivered bytes: no accusation, winner, or contradiction reading is constructible as an assertion (all class tokens appear only under negation; the ledger is empty; the two accounts are jointly satisfiable at different actors/places/ticks), and the closest surviving constructions — Evin's alibi-shaped sentence, the same-bell-two-ticks question, and the "unresolved" framing presupposition — each collapse against the record's own explicit negations and the disclosed editorial tick encoding; the structural gate cannot detect these classes (probes pass CLEAN), so the restraint is editorial and was verified by manual review, not by gate outcomes.**
