# V13 — c2-anti-overclaim (round 96)

**Seat:** V13, adversarial anti-overclaim critic for C2. **Artifacts judged (delivered bytes):**
`corpus/fixtures/r96-crossing-response/` (10 files: Q4's 8 + Q5's `README.md`,
`claim-excerpt-map.md`) and `corpus/knowledge/r96-response-scope-note.md` (Q6). Baseline r95
closure `dcb2d92`; HEAD at seat time `60dba0c`. Lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below. No file outside this report
and `.ufo/waves/round-96/V13-scratch/` was written by this seat. Leaf seat: no nested agents, no
commits, no network.

**Poll record (Q4–Q6).** Two 20 s-cadence background polls (logs kept in
`.ufo/waves/round-96/V13-scratch/poll.log` / `poll2.log`): Q4's five byte copies 17:38, its
modified `sources.json`/`timeline.json`/`fictional-excerpts.md` 17:38–17:40 (a documented
pre-receipt rewrite), Q4's report 17:42:03; Q5's two docs from 17:43:37, Q5's report 17:45:37;
Q6's note 17:44:17, Q6's report 17:45:57 (`ALL-PRESENT` at 17:45:57). Nothing was verified
before its producer bytes existed and its producer report was written; no ABSENT condition
arose. Two transient observations are reported in §5.6–5.7. The Q6 note was revised once after
my first read (citation `README.md:9`→`:7`, plus a receipts-paragraph update); all findings
below are against the final revision `6db32ca2…`, re-read in full after the revision.

**Frozen revisions (sha256, this seat's own reads, stable across ≥2 checks ~20 s apart and
unchanged at final re-check):**

```
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
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

Q5's and Q6's reports declare `ff52ced4…` and `5093d72e…` (Q5) and 61 lines (Q6); both match
my independent reads. Producer reports read: `Q4-fixture-json.md`, `Q5-fixture-docs.md`,
`Q6-knowledge-note.md`. `git status` at seat end: only ` M LOG.md`, Q1/Q2's two tool files,
Q3's two new tool files, `?? corpus/fixtures/r96-crossing-response/`,
`?? corpus/knowledge/r96-response-scope-note.md`, `?? .ufo/waves/round-96/` — no stray writes
by this seat and no change to r88/r94/r95 fixtures (`git diff --stat HEAD` over the three
inherited fixtures: empty).

---

## 1. Relation row byte-identity to r95 (C2 core confirmation) — CONFIRMED

```
$ cmp corpus/fixtures/r95-crossing-aftermath/relations.json corpus/fixtures/r96-crossing-response/relations.json && echo "cmp: IDENTICAL r95 vs r96"
cmp: IDENTICAL r95 vs r96
$ sha256sum .../r95-crossing-aftermath/relations.json .../r96-crossing-response/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  …/r95-crossing-aftermath/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  …/r96-crossing-response/relations.json
$ git hash-object corpus/fixtures/r96-crossing-response/relations.json \
    corpus/fixtures/r95-crossing-aftermath/relations.json corpus/fixtures/r94-paired-crossing/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
```

The four other preserving copies are byte-identical too (`cmp -s` exit 0 for `entities.json`,
`contradictions.json`, `inspiration-note.md`, `source-excerpt.md`; hashes above match r95's).
The scope bound is carried verbatim: `type` is still
`agreed_co_stewardship_for_this_crossing`, excerpt anchor still
`There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`
(`fictional-excerpts.md:19`).

**Map J11 row (r96 vs r95, cell-by-cell, python3 parse of both delivered maps):** the anchor
cell is **byte-equal**; pointer `relations.json#/0` (`from`,`to`,`type`,`source_id`), in-world
source ID `crossing-minute`, span `19`, and mode `verbatim` are all identical; the only
differing cell is the path-qualification column (`r95-crossing-aftermath:crossing-minute` →
`r96-crossing-response:crossing-minute`), which the map's own scope rule requires. Across all
**15 inherited rows J01–J15 the only cell difference is that same namespace cell** (15/15
namespace-only), and **J16 is the sole new row**.

## 2. Inheritance checks on the other new bytes — CONFIRMED

```
$ diff <(r95 sources.json) <(r96 sources.json)      → 24a25,30  (insert `  },` + one new row before `]`)
$ diff <(r95 timeline.json) <(r96 timeline.json)    → 41a42,52  (insert `  },` + one new event before `]`)
$ diff <(r95 fictional-excerpts.md) <(r96 …)        → 31a32,42  (append only)
python3: sources 4→5, r96[:4]==r95 → True; timeline 4→5, r96[:4]==r95 → True
         entities/relations/contradictions parsed-equal → True ×3; contradictions rows = 0
         excerpts 1845→2588 B, r96[:1845]==r95 → True (strict byte-prefix; first differing byte: None)
         common-prefix sources=1222/1225, timeline=1251/1254 (comma inserted at the last inherited row close; parsed rows unchanged)
```

Counts verified 5 entities / 1 relation / 5 events / 5 sources; census
`ls -d corpus/fixtures/*/ | wc -l` → **170** (169 at r95 closure). Q4's own report notes the
17:39 comma-style rewrite; the delivered bytes carry the r95-convention `  },\n  {` style, and
no receipt of mine was taken against the discarded intermediate.

## 3. Class sweep — new bytes only (no unnegated overclaim found)

Swept: `sources.json#/4` (`:27–31`), `timeline.json#/4` (`:44–53`), `fictional-excerpts.md`
(`:32–42`), `README.md` (30 lines), `claim-excerpt-map.md` (57 lines), the knowledge note
(61 lines), plus the copied `inspiration-note.md` (byte-unchanged; carries the inherited
rights/AI-training language verbatim).

| Hunted class | Occurrences in new bytes | Bounded in place? |
|---|---|---|
| breach | `sources.json:30` "not evidence of a breach"; `fictional-excerpts.md:42` "asserts no accusation and no breach"; README:11 "no breach" | Yes — every hit negated |
| perpetual / continuing / standing duty / alliance | `sources.json:30` "a continuing duty, a perpetual obligation" inside "not evidence of"; README:11 "no continuing obligation… not evidence of an alliance, a continuing practice, perpetual performance, a standing duty"; map:50 "not perpetual performance or alliance"; note:32 "Do not infer fault, guilt, an alliance failure, or a standing duty" | Yes — all negated |
| canon-truth | README:19 "supplies no … fictional canon"; map:40 "do not … add canon"; note:7 "not merged canon, not a contradiction finding, and not a verdict on any character" | Yes |
| rights / AI-training permission | README:19 "Rights and AI-training permission remain unassessed; neither is granted or inferred here"; map:56 "not … rights, permission, or canon review"; note:35, note:57 "Rights and AI-training permission remain unassessed here" | Yes |
| identity-inference | README:7 "does not imply a separate source, entity identity, or contradiction" (inherited wording; r94 F20-2 / r95 V13-3 residual); note:57 "path-qualified comparisons are not identity evidence" | Yes — negated |
| accusation / winner / verdict | `fictional-excerpts.md:38–40` "no accusation… no winner… stand unresolved"; `sources.json:30`, `timeline.json:51`, README:11, map:54, note:33 | Yes — all negated; no byte ranks or credits either account |
| truth / corroboration / evidence | `sources.json:30` "not evidence of … an external historical fact"; note:30 "Neither corroborates the other; neither is proof of any world fact"; note:32 "does not establish that Evin was at Salt Court as world fact" | Yes — no byte asserts confirmation of either account |
| absolutes (`always|forever|never|prove|proven|guarantee|definitiv|exactly`) | only README:21/map:56 disclaimers and note:39's "answers exactly that record" (see §5.5) | Yes, one residual noted |

No added byte upgrades a label, resemblance, or report into identity continuity, canon truth,
rights status, permission, or a performance verdict. The one new referent ("the same agreed
bell", `fictional-excerpts.md:37`) appears only inside Evin's first-person report and is kept
inside the report frame in every product byte (`sources.json:30` "Evin reports being at Salt
Court through the same agreed bell"; `timeline.json:51`; README:9; map:54).

## 4. Adversarial construction attempts — no contradiction or winner-selection reading is constructible

Criteria used: the lane's own r35 ledger `why` (`corpus/fixtures/r35-bell7-conflict/contradictions.json#/0`)
requires two reports asserting conflicting values of the **same field for the same person/event**
("Tarin reports observing Sella at Lantern Harbor … while Sella reports her own physical presence
at North Tower"), and `corpus/knowledge/r89-cross-cluster-contradiction.md` requires shared event
identity and occasion to be supported by the cited accounts.

1. **Single-attribute conflict.** Candidates: `aftermath-missing-evin` (`place_id` `chalk-stair`,
   Aru) vs `response-evin-salt-court` (`place_id` `salt-court`, Evin). Fails: the fields belong to
   **different actors**; Aru's report asserts a non-arrival, not Evin's location; nothing takes two
   values. Per r35's own `why`, an observation-scene `place_id` is not a claim about the other
   person's location.
2. **Alibi reading** (Evin's Salt Court presence rebuts Aru's non-arrival). Fails: it needs an
   unrecorded premise that the agreed bell obliged Evin at the Chalk Stair; the record says the
   opposite ("covered this crossing only", "asserts no other duty", `fictional-excerpts.md:28–29`;
   README:11). Even granting the premise, "was at Salt Court" and "did not come to the Chalk
   Stair" are compatible.
3. **Winner by consistency** (Evin's account explains/vindicates). Fails: no byte asserts
   explanation, causation, or vindication; README:11 "does not overturn, confirm, or adjudicate
   the first"; note:32 "does not establish whether Evin came to the Chalk Stair".
4. **Tie the bell to the inherited south bell** (Evin's tick-9 station) and read the pair as
   competing accounts of one ringing. Fails: no byte makes that identification; and even with it
   the two claims (Aru waited; Evin stayed) do not conflict.

Result: `contradictions.json` `[]` is the correct state; "no contradiction is asserted"
(README:11; map:54) and "selects no winner" are accurate at the record level, and no byte
selects one implicitly. The only shared referent across the two accounts is the in-world phrase
"the same agreed bell" — the residual is discussed at §5.4.

## 5. Residuals and observations (all low severity; none is an overclaim)

**5.1 — stale inheritance attribution.** `claim-excerpt-map.md:18`: "The 15 inherited rows carry
the **r94** JSON pointers …". The 15 rows are r95's rows; J15's pointer `timeline.json#/3` was
new at r95 (r94's map had 14 rows). Wording carried from r95's map where it was accurate;
should read r95. Doc-fidelity nit, no anchor or count affected.

**5.2 — stale "new relation" adjective.** `claim-excerpt-map.md:50` still says "The new relation
encodes only the agreement for this crossing…" while the relation is now inherited twice over
(r95 V51 observation 1, carried forward). Bound itself accurate.

**5.3 — "explicit … dependence wording" generalised.** `claim-excerpt-map.md:50` and `README.md:13`
describe `depends_on` edges as editorial encodings of the excerpts' "explicit tick/order/dependence
wording". J16's edge (`response-evin-salt-court` → `aftermath-missing-evin`) has no literal
"depends on" clause in Evin's note (the note references "our two accounts" but states no
dependence); this is r95 O2 carried forward. The same sentences declare the edges "editorial
encodings … not literal JSON syntax", so no out-claim results.

**5.4 — the shared occasion rests on the two notes themselves.** "the same occasion" appears at
`README.md:9`, `claim-excerpt-map.md:54`, note:11/13/39, and "same agreed crossing occasion" at
note:11. Its only support is the in-world phrase "the same agreed bell" in both notes — which is
source-supported under r89's criterion (each account asserts the shared bell), but the bell
appointment has **no record in the tick-10 agreement**, and neither note is independent of the
other. This is the r95 V13-4/O1 presupposition, now appearing in two sources rather than one.
No byte claims the bell was recorded, that the accounts corroborate each other, or that the
occasion identity is established independently (note:30 explicitly denies mutual corroboration),
so this is a bounded residual, not an overclaim.

**5.5 — "answers exactly that record".** `corpus/knowledge/r96-response-scope-note.md:39` says
the r96 response note "answers exactly that record". Evin's note names Aru and "our two accounts"
but never names the r95 record; the same note bounds the `depends_on` edge as editorial at `:34`.
Mild editorial framing, low severity.

**5.6 — observed transient in the fixture directory (unattributed).** My first poll recorded
`README.md` + `claim-excerpt-map.md` **present** at 17:38:43 and **absent** at 17:39:03, then
present from 17:43:37; Q5's report describes authoring only after Q4's report (17:42). I did not
hash the transient bytes (existence only), so the cause is unattributed (possibly author
staging). The delivered bytes were verified stable over three freezes spanning 17:46–17:53 and
match Q5's declared hashes; no verification of mine used the transient state.

**5.7 — tool-revision churn and a self-test scratch dir (context, not this seat's verdict).**
`corpus/tools/map_obligations.py` changed under me: `d1c239cc… → 8cbcdb51… → 6634e176… → 2b0ba815…`
(my final gate runs are pinned at `2b0ba815…`, identical before and after the runs). Q6's note
discloses its own earlier revision honestly. During one `--self-test` invocation at 17:53 a
`map-obligations-self-test-l8gnb7zg/` directory appeared in the repo root in `git status` and was
gone on the next check — observed evidence for the carried BR-05 (self-test scratch location)
debt; recorded here only as observation.

## 6. Executable claims re-run (final revisions) and citation spot-checks

| Claim (source) | Command | Observed |
|---|---|---|
| structural CLEAN (README:26 replay block; note receipts) | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response` | `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 (`check_bible.py` sha `ff9fd2aa…`, unchanged) |
| lexical receipt 16/2/18/14 (README:21; map:5; note) | `python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response` | `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14`; `RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18`; `SOURCE-SUPPORT 16/16; … MODES 18/18; VALIDATED-ROWS 18/18`; `RESULT PASS` exit 0 (`support_check.py` `55a5eb27…`); J16 anchor found at `37:> Tick 12: I was at Salt Court through the same agreed bell.` |
| 16 obligations (README:21; map:5) | `python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response` | `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS` exit 0, pinned tool revision `2b0ba815…` |
| census 170 (note) | `ls -d corpus/fixtures/*/ \| wc -l` | `170` |

**Citation spot-checks (all resolve on the delivered revision):** `sources.json:27` (id
`evin-response-note`), `:30` (reliability note), `timeline.json:44` (id `response-evin-salt-court`),
`fictional-excerpts.md:19/28–29/37–40/42`, `claim-excerpt-map.md:18/36/37/50/54`,
`README.md:3/7/9/11/13/21`; Q6's cross-references `r35-bell7-conflict/manual-clause-pointer-map.md:3`
and `:21` (the "no winner is selected" bound), `corpus/fixtures/README.md:746` (Round 35 heading),
`:761` ("Neither wins."), `:771`, `r35 contradictions.json#/0` id `bell7-location-reports`, r35
`timeline.json#/2–3` (tarin-envelope-observation / sella-bell7-presence, tick 3). Q6's note was
revised once mid-round (a citation `:9`→`:7` and a receipts-paragraph update); I re-read and
re-verified the final revision rather than judging the earlier text.

## 7. Bottom line

**PASS** — the r96 relation row is byte-identical to r95's (cmp + sha256 `c279254b…` + identical
git blob `2804ae91…`, transitively equal to r94's), the map's J11 anchor cell is byte-equal and
all 15 inherited map rows differ only in the required namespace cell (J16 the sole new row), the
five preserving copies are byte-identical, the three extended files are additive with
parsed-value-identical inherited rows, and **no breach, perpetual/alliance, canon-truth,
rights/AI-training, identity, accusation, winner-selection, or truth-corroboration overclaim
survives unbounded in any new byte**; every attempted contradiction and winner-selection reading
fails against the lane's own r35/r89 criteria, and the six residuals recorded in §5 (stale
inheritance wording ×2, the generalised "explicit dependence wording" bound, the bell/occasion
presupposition carried from r95 and now doubled, one editorial "answers exactly that record"
phrase, plus transient observations) are low-severity, bounded, and do not affect admission of C2.
