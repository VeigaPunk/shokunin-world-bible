# V12 — c2-whole-claim (round 96)

Seat: V12 `c2-whole-claim`. Scope per seat spec: independent **manual whole-proposition
review of the response note** — every proposition in Evin's r96 note traced to excerpt
clauses and JSON rows; no accusation / winner / contradiction assertion anywhere in the
new bytes; description fields stay scoped; identity alignments labeled editorial.
Poll-wait for Q4/Q5 per protocol. Leaf seat: no nested agents, no commits, no pushes,
no network; only this report and the seat scratch dir were written.

Baseline: r95 closure `dcb2d92` (HEAD `60dba0c`). Lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` for every command and path below.
Working tree at seat start: ` M LOG.md` + `?? .ufo/waves/round-96/` only.

## Poll-wait record (observed, 20 s cadence, `.ufo/waves/round-96/seats/scratch/V12/poll.log`)

```
CHECK t=20s  missing=[all 10 fixture files] q4=[] q5=[]
CHECK t=40s  missing=[sources.json timeline.json fictional-excerpts.md README.md claim-excerpt-map.md]
CHECK t=60s..220s missing=[README.md claim-excerpt-map.md]      # Q4 bytes staged 17:38-17:40
CHECK t=240s missing=[README.md claim-excerpt-map.md] q4=[Q4-fixture-json.md]
CHECK t=260s..320s missing=[README.md] q4=[Q4-fixture-json.md]
CHECK t=340s..460s missing=[] q4=[Q4-fixture-json.md] q5=[]     # Q5 docs landed 17:43, report pending
CHECK t=480s missing=[] q4=[Q4-fixture-json.md] q5=[Q5-fixture-docs.md]
POLL_READY t=480s
```

No plan was verified; nothing was reviewed as delivered until Q4's and Q5's bytes and
both producer reports existed. Early read-only probes taken before Q5 landed were
re-taken at the frozen revision (see §8, F4 — a pre-freeze probe of `map_obligations`
ran against an in-flight tool revision).

## Frozen revision (sha256, 2026-10-17 ~17:46–17:48 -03:00)

| File | sha256 | mtime |
|---|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` | 17:38:26 |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | 17:38:26 |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 17:38:26 |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | 17:38:26 |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | 17:38:26 |
| fictional-excerpts.md | `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3` | 17:38:43 |
| sources.json | `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` | 17:40:16 |
| timeline.json | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` | 17:40:16 |
| README.md | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` | 17:43:17 |
| claim-excerpt-map.md | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` | 17:43:09 |

All ten match the hashes Q4 and Q5 report for their own artifacts. Q4's pre-receipt
rewrite of `sources.json`/`timeline.json` (joining comma moved off its own line) is
visible as the 17:40 mtimes; my first probe (~17:39) saw the discarded intermediate
(`sources.json` `10da97ee…`, `timeline.json` `50e3d2b6…`) and no receipt below uses it.

Tool revisions observed during the window (all receipts below are bracketed to a
before/after-stable hash):

- `corpus/tools/map_obligations.py`: `d1c239cc…` (17:43) → `8cbcdb51…` (17:45) →
  `c2c284c0…` (17:46) → **`6634e1768f1f05db63b537862d90eca39eec44a77e0079e81a793b215cc6b16c`**
  (final receipts; stable across the run). Q1's C1 hardening was still landing.
- `corpus/tools/support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` (stable).
- `corpus/fixtures/check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (stable).

## 1. Whole-proposition trace — the r96 response note

Excerpt section `fictional-excerpts.md:33-42` (heading 33, attribution 35, quoted lines
37-40, scope 42). Four quoted propositions; each traced to excerpt clauses **and** to
JSON rows:

| # | Proposition (line) | JSON row/field it maps to | Trace verdict |
|---|---|---|---|
| R1 | "Tick 12: I was at Salt Court through the same agreed bell." (37) | `timeline.json#/4`: `tick=12`, `place_id=salt-court`, `entity_id=evin`, `description`; `sources.json#/4` `title`/`kind` | "Tick 12" literal; "at Salt Court" literal; "I"=evin via the attribution line 35 + `sources.json#/4` title "Evin's Salt Court Response Note" / kind "fictional first-person note"; "the same agreed bell" is the note's own in-world sameness claim whose referent is the inherited line 26 (see O3) |
| R2 | "I make no accusation against Aru." (38) | `timeline.json#/4.description` ("the note asserts no accusation against Aru"); `sources.json#/4.reliability_note` ("It asserts no accusation against Aru"); scope line 42 | negation, self-supported by the note's own text; no positive accusation anywhere |
| R3 | "I select no winner between our two accounts." (39) | `timeline.json#/4.description` ("selects no winner"); `sources.json#/4.reliability_note` ("selects no winner"); scope line 42 | negation; "our two accounts" pairs with the inherited Aru note (line 26 area) and with `timeline.json#/3` |
| R4 | "Both accounts stand unresolved." (40) | `timeline.json#/4.description` ("states that both first-person accounts stand unresolved"); `sources.json#/4.reliability_note`; scope line 42 | status statement about the two notes, mirrored in the docs (README:9, README:11, map:54); asserts no contradiction and no truth of either account |

Reverse direction (no orphan JSON): every field of the two new rows has an excerpt or
attribution counterpart —

- `timeline.json#/4`: `tick` ← "Tick 12" (editorial encoding, labeled); `entity_id` ←
  attribution (actor-slot convention, labeled); `place_id` ← "at Salt Court";
  `depends_on` ← editorial edge (labeled); `description` ← lines 37-40;
  `source_id` ← attribution.
- `sources.json#/4`: `id`/`title`/`kind` ← attribution line 35; `reliability_note` ←
  lines 37-40 plus the inherited disclaimer pattern.

## 2. Paratext checks

- Attribution line 35: "attributed to in-world source ID `evin-response-note`, folio 6,
  lines 1–4" — ID equals `sources.json#/4.id`; exactly four quoted lines; the sentence
  "This section is appended after the preserved r95 text above; the inherited wording is
  unchanged." is verified true (byte prefix, §6).
- Scope line 42 traces to lines 37-40 ("one crossing occasion", "asserts no accusation",
  "selects no winner", "does not resolve the two first-person accounts against each
  other", "the crossing-scoped agreement above is unchanged", "supplies no other duty").
  Its "no breach" clause has no counterpart in lines 37-40 — see O2.

## 3. Description / reliability-note vs excerpt — no out-claiming

`timeline.json#/4.description`, clause by clause:

| Description clause | Excerpt counterpart | Verdict |
|---|---|---|
| "Evin reports being at Salt Court through the same agreed bell" | L37 (+ attribution frame "reports") | exact |
| "the note asserts no accusation against Aru" | L38 | exact |
| "selects no winner" | L39 | exact |
| "and states that both first-person accounts stand unresolved" | L40 | exact |

Every description clause has a counterpart; no clause lacks one. The description adds no
place, tick, motive, verdict, or third account.

`sources.json#/4.reliability_note`: "Evin reports being at Salt Court through the same
agreed bell." ← L37; "It asserts no accusation against Aru, selects no winner, and states
that both first-person accounts stand unresolved." ← L38-40; "It records one crossing
occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation,
or an external historical fact." ← scope line 42 + inherited r95 disclaimer pattern
(all negating). `title`/`kind` trace to attribution. No field out-claims the excerpt.

## 4. Accusation / winner / contradiction audit (new bytes + docs)

```
$ grep -n -i -E "accus|winner|contradict|liar|lied|blame|fault|guilt|prove|proof|refut|disprov|resolve|wrong|correct|truth|verdict|adjudicat|duty|breach|perpetual|forever|always|standing|identity|alliance|obligat|continuing|canon|same" \
    sources.json timeline.json fictional-excerpts.md
```

All hits classified by polarity:

- **accusation** (4 hits: `sources.json:31`, `timeline.json:52`, `fictional-excerpts.md:38,42`):
  every one negated — "no accusation", "asserts no accusation". No positive accusation
  constructible from the new bytes.
- **winner** (4 hits: same four lines): every one negated — "selects no winner",
  "no winner". Neither account is ranked or preferred.
- **contradict**: **0 occurrences in the fixture bytes.** `contradictions.json` is `[]`
  and byte-identical to r95 (`37517e5f…`). The README/map state "no contradiction is
  asserted and `contradictions.json` remains empty" (README:11, map:54) — a statement
  about the record, not an assertion of contradiction.
- **duty / breach / perpetual / continuing / obligation / alliance / standing / canon /
  identity**: all hits are inside negations or inherited disclaimers (e.g.
  `timeline.json:40` "asserts no other duty or breach", `sources.json:31` "not evidence
  of a breach, a continuing duty, a perpetual obligation"; `fictional-excerpts.md:42`
  "no breach … no other duty"). The only non-negated uses are the technical term "map
  obligations" (README:21, map:3) — not in-world obligations.
- **"same"** (3 hits): only inside the phrase "the same agreed bell"
  (`sources.json:31`, `timeline.json:52`, `fictional-excerpts.md:37`), i.e. the note's own
  wording or a report of it (see O3). No other identity/sameness assertion in the bytes.
- Zero occurrences of `liar`, `lied`, `blame`, `fault`, `guilt`, `prove`, `refute`,
  `disprove`, `correct`, `wrong`, `truth`, `verdict`, `adjudicate` in the new bytes.

`check_bible` CLEAN (§7) confirms the two accounts create no structural conflict (the
same-tick occupancy rule is not triggered: tick 9 aru/quiet-rise + evin/salt-court, tick
10 aru/chalk-stair, tick 11 aru/chalk-stair, tick 12 evin/salt-court).

## 5. Identity alignments and editorial labeling

Labeled as editorial / convention in the delivered docs:

- tick integers and `depends_on` edges: README:13 and map:50 — "editorial encodings of
  the excerpts' tick labels and stated order/dependence, not literal JSON wording in the
  sources". Covers `tick: 12` and `depends_on: ["aftermath-missing-evin"]`.
- cluster-path qualification: README:7 — "names the lookup namespace and does not imply a
  separate source, entity identity, or contradiction".
- actor-slot convention: README:11 and map:54 — "`entity_id` is Evin because the schema
  has one actor slot; its description names Aru's account, so the field does not exclude
  the other participant".
- the Spence comparison rows: README:19, map:39-46.

The occasion-sameness alignment ("Evin's second account of the same occasion", README:9;
map:54) is presented as **what the note records** ("it records only Evin's second account
of the same occasion: that he was at Salt Court through the same agreed bell"), whose
in-world source wording is the note's own "the same agreed bell" (line 37) referring to
line 26. It is attributed rather than asserted as an editorial fact, but the word
"editorial" is not used for it — recorded as trace note O3, non-blocking.

The docs' supporting comparison "The accounts name different actors at different places
(Aru at the Chalk Stair, Evin at Salt Court)" (README:11, map:54) is directly verifiable
from `timeline.json#/3` (aru/chalk-stair) and `timeline.json#/4` (evin/salt-court), so it
is a supported content comparison, not an unlabeled identity inference.

## 6. Inheritance integrity

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    cmp -s corpus/fixtures/r96-crossing-response/$f corpus/fixtures/r95-crossing-aftermath/$f \
      && echo "IDENTICAL $f" || echo "DIFFER $f"; done
IDENTICAL entities.json
IDENTICAL relations.json
IDENTICAL contradictions.json
IDENTICAL inspiration-note.md
IDENTICAL source-excerpt.md
```

Parsed-value identity of inherited rows (python3, values parsed from the frozen files):

```
entities.json: r95=5 r96=5 inherited-equal=True
relations.json: r95=1 r96=1 inherited-equal=True
contradictions.json: r95=0 r96=0 inherited-equal=True
sources.json: r95=4 r96=5 inherited-equal=True
timeline.json: r95=4 r96=5 inherited-equal=True
excerpts prefix: True 1845 -> 2588
sources.json byte-prefix to last inherited close: True
r95 sha 0ef6734a… ; r96 prefix sha 0ef6734a…  (same digest)
```

`diff` of the extended files against the r95 originals shows pure appends:
`sources.json` `24a25,30`, `timeline.json` `41a42,52`, `fictional-excerpts.md` `31a32,42`.
Inherited map rows J01-J15 are unchanged modulo cluster-path qualification and the counts
line (verified by `diff <(sed 's/r95-crossing-aftermath/r96-crossing-response/g' r95map) r96map`:
only title, scope counts, R9 row, J16 row, and the normalization paragraphs differ).

## 7. Gate receipts (commands + observed outputs, frozen revision)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … J15 (inherited anchors at lines 12/13/17/18/19/20/26 unchanged)
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS S01 / PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> …
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response   # tool sha 6634e176…, stable before/after
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
EXIT=0
```

Control on the inherited fixture at the same tool revision:
`python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath` →
`OBLIGATIONS raw=15 mapped=15` / `INVENTORY … 15/15; 2/2; 17/17` / `RESULT PASS`, exit 0.

## 8. Findings and observations

**F1 — map editorial-table delimiter row has one cell too many (minor, delivered bytes;
Q5's file).** `claim-excerpt-map.md:44` is `|---|---|---|---|---|---:|---|---|` (8 cells)
while its header line 43 and data rows 45-46 have 7 cells; r95's equivalent line was
`|---|---|---|---|---:|---|---|` (7 cells, matching). Under strict GFM a delimiter row whose
cell count differs from the header row prevents the table from being recognized, so the
S01/S02 editorial table would render as plain paragraphs. No gate is affected: both
`support_check` and `map_obligations` count editorial rows without parsing that table
(`EDITORIAL-ROWS 2/2` on every run). Cosmetic defect in the delivered map; flagged for
the integrator, does not affect the C2 claim's substance.

**O2 — scope line 42 asserts "no breach" not present in the quoted lines (trace note,
safe direction).** Lines 37-40 never mention breach; the claim "It asserts no accusation
and no breach" (line 42) draws "no breach" from the reliability-note disclaimer
("not evidence of a breach"). r95's parallel scope line drew "no breach" from a quoted
line (r95 line 29). It is an added negation, consistent with `sources.json#/4`, and
constructs no positive assertion.

**O3 — "the same agreed bell": sameness is the note's own in-world claim (trace note).**
The phrase occurs only in Evin's note (line 37), in its `description`, and in its
reliability note. Its referent is the inherited Aru line 26 ("through the agreed bell"),
which is unchanged r95 bytes. No source row records a bell agreement (the crossing-minute
records the stewardship agreement and the route mark); neither the fixture nor the docs
claim such a record exists. The docs restate the sameness as recorded content, and no
byte treats the occasion identity as an established fact — but the docs do not use the
word "editorial" for it. Non-blocking; recorded so a later round can pin the labeling
explicitly if desired.

**F4 — concurrency artifact, not a C2 artifact (observed, must not be attributed to the
delivered revision).** At ~17:44, while Q1's C1 hardening was mid-landing, one probe ran
against an intermediate `map_obligations.py` revision and failed on the r96 fixture:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
FINDING missing_obligation: entities.json#/0/claims/0 has no map row
… (16 missing_obligation + 16 phantom_obligation lines) …
RESULT FAIL
EXIT=1
```

The phantom lines were formatted `('entities.json#/0/claims/0', None) is not a raw
source-attributed obligation` — a tuple-shaped message that the tool's source does not
produce (`f"{pointer} is not a raw source-attributed obligation"` at `map_obligations.py:484`),
proving a code-side intermediate revision rather than a defect in the map's bytes (the
same map bytes parse to `rows[0] = ('entities.json#/0/first_appearance', 'paired-clock')`
and pass at `8cbcdb51…`, `c2c284c0…`, and `6634e176…`). The C1/C3 seats and the integrator
should re-take `map_obligations` receipts at the final pinned Q1 revision; this report
does not judge C1.

## 9. Cross-checks against producer reports

- Q4's delivered hashes for `sources.json` (`9f973f63…`) and `timeline.json`
  (`ea0225f9…`) and for the five byte copies reproduce exactly; Q4's claimed counts
  (5/1/0/5/5, 16 raw obligations), its diffs, its `check_bible` receipt, and its
  documented pre-receipt comma rewrite all reproduce.
- Q5's hashes for `README.md` (`ff52ced4…`) and `claim-excerpt-map.md` (`5093d72e…`)
  reproduce exactly; Q5's "J01-J15 all SAME, exactly one extra row J16
  (`timeline.json#/4`, span 33-42, anchor line 37)" reproduces via my own diff; Q5's
  caveat that `map_obligations` was changing under it matches F4.
- Q6's `corpus/knowledge/r96-response-scope-note.md` exists (17:47) and is outside this
  seat's declared scope; not reviewed here.

## Bottom line

PASS — every proposition of the r96 response note (lines 37-40) traces to exact excerpt
clauses and to `timeline.json#/4` / `sources.json#/4` with no orphan clause or field; no
accusation, winner, or contradiction is asserted anywhere in the new bytes
(`contradictions.json` stays `[]`), the description and reliability note out-claim
nothing, and the JSON identity alignments (ticks, edges, actor slot, namespace) are
labeled editorial; check_bible CLEAN exit 0, support_check 18/18 PASS exit 0,
map_obligations 16/16 PASS exit 0 at pinned tool revision `6634e176…` — with one minor
non-blocking delivered-bytes defect (F1, Q5's map editorial-table delimiter cell count)
and three trace notes (O2, O3, F4).
