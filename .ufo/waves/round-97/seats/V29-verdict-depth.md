# V29 — verdict-depth (round 97)

Seat: V29 `verdict-depth`. Scope per seat spec: read the C3 seats, run 2 own replays,
issue exactly one DEPTH verdict on the declared C3 before→after
("acknowledgment-without-reconciliation class", 5/1/5→5/1/6) with named bounds.

Baseline: r96 closure `f3e09f9` (HEAD `2393934`). Lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below; all commands run
from there with `python3`. Writes by this seat: this report plus scratch
`.ufo/waves/round-97/seats/V29-scratch/` (`poll.sh`, `poll.log`, `replay.py`,
`map-rows.py`, `r96-pre-repair.txt`, `r96-post-repair.txt`,
`r96-and-adjacent-at-current-tools.txt`, `r97-receipts-1.txt`, `r97-receipts-2.txt`,
`r97-hashes.txt`, `r97-hashes-post-r5.txt`, `map-rows-1.txt`, `replay-1.txt`).
No commits, no pushes, no network, no nested agents.

## 1. Poll record and method

Poll-wait protocol: background poller (20 s cadence, 40 tries) launched 18:42:42 on
(a) the 10-file r97 fixture and (b) producer reports. Observed timeline (lane clock,
-03:00):

- 18:43:04 — my pre-repair r96 receipt capture (map still `5093d72e…`, tools frozen).
- 18:43:42 — R4's r96 map repair landed (map `5093d72e…` → `e851f068…`; `git diff`
  = 2 lines, §5).
- 18:44:16–18:44:30 — r97 fixture dir appeared with 10 files; at 18:44:36 the
  `README.md`/`claim-excerpt-map.md` inside it were still byte copies of the r96
  files (map `e851f068…`, README `ff52ced4…`), i.e. R5's work was pending.
  My mid-write probe at that instant: `map_obligations` → `OBLIGATIONS raw=17
  mapped=16` / `FINDING missing_obligation: timeline.json#/5 has no map row` /
  `RESULT FAIL` exit 1 — recorded as mid-flight (R4's own report shows the same
  pre-R5 state), not a defect; the delivered revision passes (§4).
- 18:48:56 / 18:49:14 — R5's map (`49d4834e…`) and README (`d9387b7d…`) landed.
- ~18:51 — R6's `corpus/knowledge/r97-acknowledgment-scope-note.md` landed
  (`56981af5…`; rewritten by R6 later the same round to `5e3b4225…`, §addendum).
- 18:50:14 / ~18:51 — R4 and R5 reports landed; R6's report landed ~18:54. The R6
  artifact is read in §6; late-landing C3 seats (V15/V16/V17/V18/V42) are folded in
  in the addendum.

Revision frozen for verification: 10-file sha256 capture at 18:51:32
(`V29-scratch/r97-hashes-post-r5.txt`) plus the R6 note hash; re-verified unchanged at
my final pass (§9). Key hashes: `timeline.json` `73063a86…`, `sources.json`
`438fb513…`, `fictional-excerpts.md` `8ba491cb…`, map `49d4834e…`, `README.md`
`d9387b7d…`, `entities.json` `026af0bc…`, `relations.json` `c279254b…`,
`contradictions.json` `37517e5f…`, `inspiration-note.md` `58f5390e…`,
`source-excerpt.md` `b5edc2fd…` — all equal R4/R5/V13/V50/V51 captures.

## 2. Before-state baseline (r96, replayed by me)

r96 at the pre-repair revision (`5093d72e…`, 18:43:04) and at the post-repair
revision (`e851f068…`, 18:44:09), same tool revisions both sides
(`map_obligations.py` `2b0ba815…`, `check_bible.py` `ff9fd2aa…`,
`support_check.py` `55a5eb27…`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; … MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                           exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                           exit=0
```

Parsed r96 counts: entities 5 / relations 1 / events 5 / sources 5 / contradictions 0.
The same three receipts reproduce on the repaired r96 at the current hardened tool
revision (`map_obligations.py` `86b52949…`, `V29-scratch/r96-and-adjacent-at-current-tools.txt`):
`CLEAN` exit 0, `16/16 … RESULT PASS` exit 0, `raw=16 mapped=16 … RESULT PASS` exit 0.

## 3. Replay 1 — check_bible on the delivered r97 fixture, counts, census

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ ls -d corpus/fixtures/*/ | wc -l
171                                                                    # 170 at r96 closure
```

`check_bible.py` is byte-unchanged all round (`ff9fd2aa…` = the r96 C9-watch pin).

My own parsed checks on the delivered `timeline.json` (`V29-scratch/replay-1.txt`):

```
ticks: [9, 9, 10, 11, 12, 13]
edges: 5 strictly backward: True
ids: ['aru-ninth-bell','evin-ninth-bell','paired-crossing-decision',
      'aftermath-missing-evin','response-evin-salt-court','acknowledgment-aru-records']
counts e/r/ev/s/c: 5/1/6/6/0        (r96: 5/1/5/5/0)
```

Before → after: CLEAN exit 0 → CLEAN exit 0; the new terminal event extends the
dependency chain one strict-backward edge (5 edges total).

## 4. Replay 2 — map_obligations + support_check + preservation battery

Delivered revision, tool revisions recorded with each run (`V29-scratch/r97-receipts-2.txt`):

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -4
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                           exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                           exit=0
```

Preservation battery (my own runs, `V29-scratch/replay.py`):

```
five copies (entities/relations/contradictions.json, inspiration-note.md, source-excerpt.md):
  byte-identical r97 vs post-repair r96 = True ×5
r97 timeline[:-1] == r96 timeline: True
r97 sources[:-1]  == r96 sources:  True
r96 excerpts is byte-prefix of r97: True   (r96 2588 B / r97 3410 B, delta 822 B)
census: 171
```

New rows (parsed, exact): `timeline.json#/5` = `acknowledgment-aru-records`, tick 13,
`entity_id aru`, `place_id chalk-stair`, `depends_on ["response-evin-salt-court"]`,
`source_id aru-acknowledgment-note`; `sources.json#/5` = `aru-acknowledgment-note`
(fictional first-person note; reliability note = "receipt only … not evidence of a
resolution, a reconciliation, an accusation, a winner between the accounts, a
continuing duty, or an external historical fact").

Map-row inheritance (my own column parse, `V29-scratch/map-rows-1.txt`):

```
r96 row ids: J01..J16, S01, S02 ; r97 row ids: J01..J17, S01, S02
new rows: ['J17']  gone rows: []
inherited rows compared: 18; differing: 0      (modulo r96-…: → r97-…: in the namespace column)
new row J17: ['J17','`timeline.json#/5` (tick, entity_id, place_id, depends_on, description, source_id)',
  '`aru-acknowledgment-note`','`r97-crossing-acknowledgment:aru-acknowledgment-note`',
  '`fictional-excerpts.md`','44-53','`verbatim`',"`Tick 13: I received Evin's response at the Chalk Stair.`"]
```

Non-harm: `git diff --stat f3e09f9 -- corpus/fixtures/r94-paired-crossing
corpus/fixtures/r95-crossing-aftermath` → empty (untouched); the only corpus diffs vs
`f3e09f9` are the r96 map repair and the C1/C2 tool files; `git status` shows no stray
corpus writes.

## 5. The r96 cosmetic repair (repair half, independently captured)

I captured the r96 receipts before the repair landed (18:43:04, map `5093d72e…`) and
after (18:44:09, map `e851f068…`) at identical tool revisions: the three receipts are
byte-identical before vs after (CLEAN exit 0; `support_check` `16/16 … RESULT PASS`
exit 0; `map_obligations` `raw=16 mapped=16 … RESULT PASS` exit 0).

`git diff` on the map shows exactly two changed lines and nothing else:

```
-|---|---|---|---|---|---:|---|---|          (line 44 delimiter, 8 cells)
+|---|---|---|---|---:|---|---|            (7 cells)
-… The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+… The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no
+  reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not
+  perpetual performance or alliance.
```

Post-repair cell counts: header 7 / delimiter 7 / S01 7 / S02 7. Data rows (J01–J16,
S01–S02), pointers, anchors, spans, and modes are byte-unchanged (`git diff` touches no
`| J`/`| S` line). The r97 fixture's inherited copies were taken from this post-repair
revision (`entities/relations/contradictions/inspiration-note/source-excerpt`
byte-identical to it).

## 6. "Acknowledgment without reconciliation" — independent bounding

- **The class's records (delivered bytes).** Note text
  `fictional-excerpts.md:44-53` (quoted lines 48-51): "Tick 13: I received Evin's
  response at the Chalk Stair. / I hold to my own account; both accounts stand
  unresolved. / I make no accusation against Evin, and I select no winner between us. /
  I assert no reconciliation, no new duty, and no obligation beyond this crossing."
  Source reliability note (`sources.json:36`), event description (`timeline.json:62`),
  README `:9`/`:11`, map `:51`/`:57`, and the R6 scope note carry the same bound.
- **Receipt-only, no third account.** The note re-asserts Aru's own prior account
  ("I hold to my own account") and records receipt; the arc therefore still carries
  exactly two accounts of the occasion, and the dispute stays unresolved in-record.
- **Scope audit (my grep over all 10 fixture files + the R6 note).** Every occurrence of
  accusation/winner/reconciliation/resolution/breach/duty/obligation/alliance/perpetual
  is inside a negating or scoping clause; zero occurrences of betray/fault/guilt/blame/
  forgiveness/apology/concession/admission/surrender; the only non-negated "resolves"
  is `source-excerpt.md:7` ("locator resolves to the printed-page marker"), an editorial
  provenance sentence. `contradictions.json` = `[]` (3 B, byte-identical across
  r95/r96/r97).
- **Novelty bound (my own scan).** `grep -rni "acknowledg" corpus/` outside the r97
  fixture and the R6 note → **0** matches; the term/class is corpus-first in that
  literal sense, and the "third beat" framing is the record's own (README `:3`, R6 note
  §"The observation class"). Distinct from r35 (which asserts an editorial conflict
  ledger row) and from r96 (which adds a second account; r97 adds none).

## 7. C3 seats read (statuses at my report time)

- **V13 c3-checker — PASS**: CLEAN exit 0; counts exactly 5/1/6/6; tick-13 event fields
  exact; zero dangling/duplicate ids; r96 CLEAN post-repair; independent census
  170→171 with 36→37 clean, 134 negative, 421 violation lines, zero non-0/1 exits.
- **V14 c3-inherited-equality — PASS (final revision of its report)**: key-order-sensitive
  parsed-value equality of every inherited row, five byte-identical copies, byte-prefix
  probes, r96 JSON tables byte-unchanged vs `f3e09f9`; checks proven load-bearing by
  three negative controls.
- **V19 c3-r96-repair-scope — PASS**: repair is byte-minimal (exactly two lines, 18 data
  rows identical, 56 lines both sides); r96 `support_check`/`map_obligations` receipts
  byte-identical before vs after under frozen and current tool revisions.
- **V20 c3-dependency-probe — PASS**: four mandated probes (dropped key, unknown id,
  tick inversion, removed predecessor) each exit 1 on the delivered bytes; **bounds**:
  an emptied `depends_on` (P1b), a wrong-but-earlier edge (P8), and a deleted terminal
  row (P9) all stay CLEAN — the checker polices the edge only partially.
- **V50 byte-prefix-2 — PASS**: five copies `cmp`-identical; `sources`/`timeline` strict
  EOF appends (1 hunk, 0 deletions, inherited prefix deep-equal); excerpts strict
  byte-prefix (2588 B prefix / 822 B tail); synthetic positive + negative controls.
- **V51 relation-scope-2 — PASS (with one bounded prose observation)**: relations.json
  byte-identical across r94–r97 (`c279254b…`); J11 unchanged outside the namespace cell;
  no new relation semantics (10-type census unchanged). Observation: the mandated repair
  removed the r96 map's standalone relation-bound sentence from the normalization prose;
  the bound survives in the J11 anchor, README `:11`, `sources.json` reliability note,
  and both scope notes — flagged for closure, no data row affected.
- **V52 support-regression — PASS (C3-adjacent)**: every `support_check` receipt
  r87→r97 replays as declared (r97 `17+2`); the r96 repair proven receipt-neutral by
  diffing the frozen `f3e09f9` map against the repaired map (identical output,
  `ca7a6815…`).
- **V15 c3-support-map — PASS**: r97 receipts exactly as claimed (`17/17; 2/2; 19/19;
  15/15` PASS, `raw=17 mapped=17` PASS, exit 0); r96 receipts byte-identical across the
  repair and across the tool churn (`2b0ba815…`→`86b52949…`); independent raw recount
  16→17 obligations; notes `support_check` skips delimiter rows before its cell-count
  check, so the repair's receipt-neutrality is expected but was still measured.
- **V16 c3-anchors — PASS**: own `grep -nF` + pure-Python resolver — all 17 J anchors +
  2 S anchors in-span, occurrence count 1, no outside-span hits; 18 inherited anchors
  identical and at the same resolved lines as r96 (J01–J15/S also vs r95); J17 occurs
  only at `fictional-excerpts.md:48` inside span 44-53; zero drift.
- **V17 c3-whole-claim — PASS**: manual clause-by-clause trace of the four note lines to
  `timeline.json#/5`/`sources.json#/5` and the map row; resolution/accusation/
  reconciliation/new-duty/contradiction/verdict readings all NOT CONSTRUCTIBLE from any
  delivered byte.
- **V18 c3-anti-overclaim — PASS**: repair byte-minimal (data-row block `1f58fdb9…`
  identical before/after; receipts diff-identical at one tool revision); r97 verified
  end-to-end; two independent load-bearing constructions (pre-R5 map → `missing_obligation`
  FAIL exit 1; J17 span corrupted 44-53→44-46 → anchor-outside-span FAIL exit 1); census
  171/37/134/421/0 independently reproduced. Bounded notes: the line-50 edit is a full
  sentence replacement (not a phrase swap); the editorial delimiter's right-align colon
  sits on the "R9 delivery mode" cell (pre-existing, render-only).
- **V42 anchor-replica-2 — PASS**: tool-free re-implementation; 17/17 in-span, 16/16
  inherited rows preserved against both the post-repair and the committed `f3e09f9`
  baselines, 15/15 distinct anchors, J17 span 44-53 hit 48.
- **V53 cross-seat-audit — INTERIM PASS (5/5 reproduced)**: independently re-ran V13's
  census (171/37/134/421/0) and V19's repair quotes (numstat `2 2`, two hunks,
  data-rows block `1ff29a75…`), plus r97 gate receipts and preserving-copy structure —
  all REPRODUCED; its C2 items held open at its last poll (R3 mid-flight, not my axis).
- **Producers**: R4 report **PASS** (repair byte-minimal; r97 pure-append continuation;
  its pre-R5 `raw=17 mapped=16 … FAIL` capture matches my mid-write observation);
  R5 report **PASS** (16 inherited rows byte-exact with anchors at identical line
  numbers; J17 span 44-53; all three receipts); R6 report **PASS** (70-line note; 52
  citations resolved 0 BAD, 19 content probes 0 BAD; three receipts PASS; inheritance
  and repair independently confirmed).

## 8. DEPTH VERDICT (exactly one)

**DEPTH — IMPROVED (bounded).** On the delivered revision, the crossing arc gains its
third beat — a participant's **receipt-only acknowledgment, dispute preserved
unresolved**: before r96 = 5/1/5 entities/relations/events, 5 sources, 16 map
obligations; after r97 = 5/1/6, 6 sources, 17 map obligations (16 inherited rows
carried unchanged + the new tick-13 event row J17), with the tick-13 event
dependency-linked to the tick-12 response, the unresolved status re-asserted in-record
("both accounts stand unresolved"), no accusation, no winner, no reconciliation claim,
an empty contradiction ledger, `check_bible` CLEAN exit 0, `map_obligations raw=17
mapped=17` PASS exit 0, `support_check` 19/19 PASS exit 0, census 170→171 with zero
inherited changes (byte-identical five copies; parsed-prefix timeline/sources; strict
byte-prefix excerpts; column-level map-row inheritance modulo the declared namespace
re-qualification). No harm observed in my scope: r94/r95 fixtures, `check_bible.py`,
`support_check.py` byte-unchanged vs `f3e09f9`; no new claims, entities, or relations
(three tables byte-identical); no contradiction created.

Named bounds:

1. **Structural/lexical only.** The verdict rests on delivered bytes (hashes §1) plus
   hand scope review; no testimony truth, canon adjudication, chronology, rights, or
   identity claim.
2. **"Acknowledgment-without-reconciliation" is an authored in-record status.** No gate
   reads prose; the class label is corpus-bounded (the literal term occurs nowhere
   outside r97), and the "third beat" arc framing is the record's own description.
3. **Receipt-only is record-bounded.** "I received Evin's response at the Chalk Stair"
   is the note's own wording; the tick integer, event ID, and `depends_on` edge are
   editorial encodings (README `:13`, map `:51`); no external chronology or delivery
   fact is proven.
4. **Dispute-preserved is an assertion, not a proof.** "Both accounts stand unresolved"
   is stated by the notes; the empty ledger rests on the different-actor/different-place
   reasoning recorded editorially, not on a checker outcome.
5. **Checker blind spots (carried, V20 P1b/P8/P9).** `check_bible` cannot see an
   emptied `depends_on`, a wrong-but-earlier edge, or a deleted terminal row; the
   tick-13→tick-12 edge is verified as bytes + prose + map row, not by a rule.
6. **Tool-revision flux (sampled, not settled).** `map_obligations.py` moved
   `2b0ba815…` → `86b52949…` during the round (C1 hardening); the r97 fixture-path
   receipts were produced at `86b52949…` (and the r96 repair-half receipts at
   `2b0ba815…`), with fixture-path output stable at both sampled revisions.
7. **Preserving continuation at named levels.** Byte-level for the five copies,
   parsed-value prefix for `timeline`/`sources`, strict byte-prefix for the excerpts,
   column-level equality modulo namespace re-qualification for the 17 inherited map
   rows — not map-file byte equality.
8. **Delivered-corpus bookkeeping.** `corpus/fixtures/README.md` still states the r96
   census (170) while the tree has 171 (flagged by R5/V51/V26); freshness/doc-parity is
   another axis, but it bounds the "delivered corpus" statement here.

## 9. Non-axis observations (for the integrator)

- **Host condition:** `/tmp` inode exhaustion (100 %, 1048576/1048576) hit several
  seats this round (V20's probe run, V26's self-test); seats re-ran with `TMPDIR` under
  repo scratch. Recorded as a host condition, not a repo finding.
- **Mid-flight states observed and superseded:** r97 map/README were r96 byte copies
  until 18:48:56/18:49:14, and `map_obligations` correctly failed on the missing row
  then (`raw=17 mapped=16 … missing_obligation: timeline.json#/5` exit 1). Recorded as
  evidence that the J17 row is load-bearing, not as a defect.
- **Repaired-map prose (V51 observation 1):** the r96 normalization section no longer
  carries a standalone relation-bound sentence; the bound survives in the J11 anchor
  and README/sources/scope-note. Flagged for the closure pass.
- **R6 note rewrite:** the note landed at ~18:51 as `56981af5…` and was rewritten later
  the same round to `5e3b4225…` (adds a `citation-convention:` line, updates the receipt
  tool revisions to `86b52949…`, reworded the repair paragraph). My §6 citations were
  re-checked against the rewritten bytes and hold; the old hash is superseded.
- Final fixture stability: 10-file hash set unchanged 18:51:32 → final pass; the R6 note
  was the only post-capture change (see above); no fixture drift observed.
- **Late C3 seats landed after my first write** (V15/V16/V17/V18/V42 PASS, R6 report PASS,
  V53 INTERIM 5/5 reproduced); folded in below.
- **Other seats' bounded observations (not my axis):** `corpus/fixtures/README.md:1217`
  still states the r96 census (170) vs on-disk 171; `SKILL.md:87`/`corpus/README.md:37`
  still say "24 cases" after the C1 contract moved to 25 (V53); r97 is intentionally not
  in the freeze chain (V53/R6) — C2 territory.

## Bottom line

**PASS — DEPTH verdict: improved (bounded)** — the delivered r97 fixture verifies as
the crossing arc's third beat, an acknowledgment of receipt that leaves both accounts
unresolved and asserts no reconciliation (5/1/5→5/1/6, 5→6 sources, 16→17 map
obligations, J17 load-bearing, CLEAN/PASS receipts on the delivered revision, byte/
value/prefix/column preservation, empty contradiction ledger, adversarial scope
discipline), with the named bounds in §8 (structural-only evidence, corpus-bounded
class label, record-bounded receipt, assertion-level unresolved status, checker
dependency blind spots, sampled tool revisions) and the C3 seats read in §7 (V13/V14/
V15/V16/V17/V18/V19/V20/V42/V50/V51 PASS, V52 PASS, V53 interim 5/5 reproduced; R4/R5/R6
producer reports PASS).

---

## Addendum (after my first write) — late C3 seats, R6 note rewrite, final freeze

The first version of this report was written at 18:54 with R6's report and five C3
verifier seats still pending. All of them landed within the poll budget and are folded
into §7 above; this addendum records the revision deltas.

1. **R6's note was rewritten** (`56981af5…` → `5e3b4225…`, mtime ~18:54). Re-read in
   full: the class definition, records table, repair paragraph, bounds, precedents, and
   receipts are substantively unchanged; it adds a `citation-convention:` metadata line
   and updates its receipt tool revisions to `map_obligations.py` `86b52949…` (contract
   `2142b991…`), noting an earlier identical run at `70795150…`. Every element I cite in
   §6 still holds on the rewritten bytes; the note's own hash in §1/§9 is superseded by
   `5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5`.
2. **Late C3 seats read (full reports, §7):** V15 c3-support-map PASS, V16 c3-anchors
   PASS, V17 c3-whole-claim PASS, V18 c3-anti-overclaim PASS (with two independent
   load-bearing constructions), V42 anchor-replica-2 PASS; V53 cross-seat-audit INTERIM
   PASS (5/5 reproduced; its two C2 items open on R3, outside C3); R6 report PASS.
   V14's report was finalized from PRELIMINARY to PASS in place. **V54 crosscheck-depth
   — PASS, crosscheck AGREE**: an independent depth derivation from the delivered bytes
   (own scripts, own `git archive f3e09f9` baseline) reproduces every shared
   measurement of mine (5/1/5→5/1/6, 17/17 + 19/19 receipts, census 170→171,
   namespace-modulo inheritance, byte-minimal receipt-neutral repair, pre-R5
   `missing_obligation` mid-flight, class-label novelty 0 matches) and reports no
   material divergence from this report's verdict or bounds.
3. **Final freeze re-check (18:54+):** `sha256sum -c V29-scratch/r97-hashes-post-r5.txt`
   → all 10 r97 fixture files `OK` (unchanged since 18:51:32); the R6 note is the only
   post-capture artifact change (recorded above); `git status --porcelain` shows only
   the declared producers' paths, the untracked r97 fixture, the R6 note, and
   `.ufo/waves/round-97/` — no stray write from this seat (the r94-F01 class did not
   recur).
4. **Nothing in the late seats changes the verdict or the bounds.** Their findings are
   concordant with mine on every overlapping measurement (hashes, counts, receipts,
   inheritance levels, census, load-bearing proofs). Two bounded items worth carrying to
   closure (already named in §9): the stale census text in `corpus/fixtures/README.md`
   and the pre-existing render-only colon position in the repaired r96 editorial
   delimiter (V18; not introduced by the repair).

**Bottom line (updated): PASS — DEPTH verdict: improved (bounded)** — the delivered r97
fixture verifies as the crossing arc's third beat, an acknowledgment of receipt that
leaves both accounts unresolved and asserts no reconciliation (5/1/5→5/1/6, 5→6 sources,
16→17 map obligations, J17 load-bearing, CLEAN/PASS receipts on the delivered revision,
byte/value/prefix/column preservation, empty contradiction ledger, adversarial scope
discipline), with the named bounds in §8 and the full C3 seat set read in §7 (V13–V20,
V42, V50–V53 PASS or interim-reproduced; R4/R5/R6 producer reports PASS); the R6 note
rewrite (`5e3b4225…`) and the late-landing seats are recorded in this addendum.
