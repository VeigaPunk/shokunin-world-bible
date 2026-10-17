# F21 — verdict-depth

**Seat:** F21, per-axis verdict for the **DEPTH** axis, round-94 FOLLOW-UP (lore-shokunin). LEAF seat: this report is the only file this seat wrote; no corpus edit, no commit, no nested agent. Verdict vocabulary: improved / harmed / unchanged / unprovable-but-better. **This verdict covers the depth axis only; other axes (coverage, calibration, operability, freshness, adjacency) are separate seats and are not averaged, restated, or implied here.**

**Pins observed:** `git rev-parse HEAD` → `65a93298cb100fdbf5732ac6de55f01a683c02d8` (declaration `65a9329`); candidate `abbc3e0`; baseline `9c2eea3`. `git status --porcelain` → only `?? .ufo/waves/round-94/followup/` (untracked report tree); no corpus byte dirty.

**Input digests** (`sha256sum`, run from repo root):

```
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r94-paired-crossing/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r94-paired-crossing/relations.json
f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c  corpus/fixtures/r94-paired-crossing/timeline.json
ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47  corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md
585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2  corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790  corpus/tools/map_obligations.py
```

The fixture hashes match the independent pins in F01/F03/F20 (same digests quoted there), so all seats below judged the same delivered bytes.

## 1. Spec acceptance lines under this verdict

From `.ufo/waves/round-94/wave-spec.md`:

- `:7` — "Depth/coverage/calibration remain an unmeasured score tie; C1 depth and C2 calibration work the weakest-axis obligation **without inventing a numerical rubric**."
- `:9` — C1 is "**depth: supported relational consequence, not just another motif note**".
- `:11` — the fixture is "an explicit continuation of `r88-m3-maya-cluster`, not an unrelated cluster or a silent change to that history."
- `:13` — "Before: four entities, zero relations, two tick-9 events at distinct places. After: five entities, one source-supported agreement/co-stewardship relation and three events, including a tick-10 crossing decision depending explicitly on BOTH named tick-9 entries."
- `:19` — "Verification: parsed entity/relation/event counts 4/0/2→5/1/3; inherited-record equality; explicit two-event dependency and excerpt proposition review; `check_bible.py` CLEAN; `support_check.py` PASS over the declared mapped rows; independent manual whole-claim and comparison review in FOLLOW-UP. **Counts alone do not prove source support.**"

The falsifiable before→after this verdict must test is therefore: **parsed counts 4/0/2 at r88-m3-maya-cluster → 5/1/3 at r94-paired-crossing, with the one new relation source-supported and the new tick-10 event depending on both named tick-9 events, on an inherited-record-preserving continuation.**

## 2. Peer reports read (inputs, not substitutes for §3)

| Seat | Bottom line as filed | Depth-relevant content |
|---|---|---|
| F01-c1-checker | **PASS** | `check_bible.py` CLEAN exit 0; parsed 5/1/3 vs r88 4/0/2; tick-10 `depends_on` set-equality True, no dangling refs; 8 shared r88 rows parsed-value identical, key order identical, 0 field-level diffs (`.ufo/waves/round-94/followup/F01-c1-checker.md:151-161`) |
| F02-c1-support | **PASS** | `support_check.py` RESULT PASS exit 0, JSON-FACTS 14/14, TOTAL-ROWS 16/16, MODES 16/16; relation row `J11 = relations.json#/0` encodes only "for this crossing only" (`F02-c1-support.md:14-42,64-68`) |
| F03-c1-map | **PASS** | 14 raw obligations one-to-one with map rows (5 first-appearance + 5 claims + 1 relation + 3 events); all anchors in-span; editorial rows separate; `raw=14 mapped=14` (`F03-c1-map.md:20-63,152-155`) |
| F04-c1-whole-claim | **PASS** | Independent manual review: all four new `crossing-minute` obligations entailed by `fictional-excerpts.md:17-20` or labeled editorial metadata; no contents/perpetual/alliance overreach (`F04-c1-whole-claim.md:22-64,92-94`) |
| F05-c1-comparison | **PASS** | Knowledge doc comparators exact, boundaries explicit, Spence contrast matches r88 delivered wording; no cultural-fact/shared-canon/rights claim (`F05-c1-comparison.md:180-182`) |
| F06-c1-continuity | **PASS** | Value- and byte-preserving continuation; tick-9 places distinct; relation agreement-only; check_bible CLEAN, support PASS 14/14, map_obligations raw=14 mapped=14 (`F06-c1-continuity.md:170-172`) |
| F20-anti-overclaim-critic | **PASS** | No unbounded canon-truth / rights / AI-training-permission / perpetual-performance / authenticated-testimony / identity-inference overclaim in the r94 diff; every executable claim re-ran exactly; sole new unbounded phrase is low-severity "their near-miss" (`F20-anti-overclaim-critic.md:125-127`) |

No seat among F01–F06 or F20 reports a failed check or a contradiction of the C1 depth claim. F20's items F20-1…F20-7 are all low-severity and none asserts a canon/performance/identity claim; F20-1 (`README.md:9` "their near-miss") is an interpretive label, not a depth artifact defect.

## 3. My own three spot replays (independent of the seat reports)

**Replay A — checker clean.**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing; echo "EXIT=$?"
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

**Replay B — counts 5/1/3 and inherited-record equality (raw `json.load`, not grep).**

```
$ python3 - <<'EOF'  (json.load of both fixtures, whole-row equality)
entities=5 relations=1 events=3
r88 counts: entities=4 relations=0 events=2
inherited entities identical: True
inherited events identical: True
EOF
```

**Replay C — tick-10 depends on BOTH named tick-9 events.**

```
tick10 depends_on: ['aru-ninth-bell', 'evin-ninth-bell'] both tick9 ids present: True
tick9 ids: ['aru-ninth-bell', 'evin-ninth-bell'] dependency subset of tick9: True
tick10 tick > tick9: True
relation source_id: crossing-minute
```

Both depended-on IDs resolve to the two real inherited tick-9 rows (`timeline.json#/0`, `#/1`), and `check_bible.py`'s timeline-ordering rule is satisfied by the CLEAN run in Replay A. The dependence is not merely structural: the minute states it in words — `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:20` "Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court."

**Corroborating replays (free, run by this seat):**

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
EXIT=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
EXIT=0

$ git diff --stat 9c2eea3 abbc3e0 -- corpus/fixtures/r88-m3-maya-cluster
(empty output; r88 fixture byte-identical across baseline and candidate)
$ git diff --name-status 9c2eea3 abbc3e0 -- corpus/
A corpus/fixtures/r94-paired-crossing/… (10 files)
A corpus/knowledge/r94-cross-myth-design-comparison.md
A corpus/tools/map-obligations-contract.json
A corpus/tools/map_obligations.py
(no M / D rows)
$ diff corpus/fixtures/r88-m3-maya-cluster/inspiration-note.md corpus/fixtures/r94-paired-crossing/inspiration-note.md
(diff-exit=0, identical)
```

The relation's support is concrete: `relations.json#/0` carries `"source_id": "crossing-minute"`, and the authored minute at `fictional-excerpts.md:19` says "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair." The new entity/claim/event pointers (`entities.json#/4`, `entities.json#/4/claims/0`, `timeline.json#/2`) map to anchors at `fictional-excerpts.md:17`, `:18`, `:20` (`claim-excerpt-map.md:26,31,35`).

## 4. Verdict: **improved**

**Falsifiable before→after (as declared at `wave-spec.md:19`):** parsed counts **4 entities / 0 relations / 2 events** at `r88-m3-maya-cluster` → **5 / 1 / 3** at `r94-paired-crossing`, where the one new relation is source-supported and the new tick-10 event depends on both named tick-9 events, on a continuation that preserves the inherited records. **Observed on the delivered revision: the claim is not falsified** — Replays A/B/C above reproduce every component (counts, inherited equality, both-event dependency, checker clean, 14/14 support, 14/14 map obligations), and no check run by this seat failed.

**Why this is an axis improvement, not a motif addition.** The C1 obligation was a "supported relational consequence, not just another motif note" (`wave-spec.md:9`). Before, the r88 snapshot had `relations.json = []` and two independent tick-9 entries: motif-level co-presence only, no relational record and no consequence event. After, the delivered bible format carries (i) one relation whose type itself encodes the scoped agreement (`agreed_co_stewardship_for_this_crossing`) and (ii) one event that is ordered after and explicitly dependent on **both** prior events. That is a demonstrated capability change at the artifact level — a supported relation and a dependent consequence now exist and are fully mapped — not another isolated motif note. The improvement direction is the declared one, and the deliverable is a strict extension of the r88 history (byte-prefix excerpt file, value-identical inherited rows, r88 fixture untouched in the diff).

**Why "improved" rather than "unprovable-but-better".** The improvement claim is provable at the artifact level and was proved: the counts, the source support, and the dependency are each independently observable and were observed by three of my replays plus F01–F06's receipts. Nothing in the verdict depends on taste or an invented score.

## 5. Named bounds of this verdict

- **B1 — one-fixture scope.** The improvement is bounded to `corpus/fixtures/r94-paired-crossing/` (one authored minute, one relation, one event). It is not a general depth metric, not a corpus-wide claim, and no numerical rubric is invented (`wave-spec.md:7`).
- **B2 — support bound.** Counts alone do not prove source support (`wave-spec.md:19`). The support qualifier rests on the mapped anchors (`claim-excerpt-map.md` J05/J10/J11/J14) and F04's independent whole-proposition review; that review is bounded to entailment of the new propositions — not source authentication, chronology truth, rights, permission, or canon (`F04-c1-whole-claim.md:92-94`).
- **B3 — semantic bound.** The relation records the agreement "for this crossing only" and is explicitly not an alliance, continuing practice, or perpetual performance (`README.md:9`; `sources.json:18`; `claim-excerpt-map.md:48`).
- **B4 — encoding bound.** Tick integers and `depends_on` event IDs are labeled editorial encodings of the minute's explicit tick/order/dependence wording, not literal JSON syntax in the source (`claim-excerpt-map.md:48`; `README.md:11`).
- **B5 — residue bound.** F20-1 ("their near-miss", `README.md:9`) is a low-severity interpretive label; F20-2…F20-7, F06 O1–O3 and F04 O1–O6 are scope/presentation/staleness notes. None removes an inherited capability and none weakens the supported-relation or both-dependency evidence; r94 is a value- and byte-preserving extension of r88 (Replay B, diff above), so no depth-harm path exists inside this diff.
- **B6 — axis bound.** This is the depth verdict only. It does not certify C2, any other axis, or round admission; those are other seats' judgments and the final adjudicator's decision.

## Bottom line

**IMPROVED (depth) — the falsifiable before→after 4/0/2 → 5/1/3 at the explicit `r88-m3-maya-cluster` continuation verifies on the delivered revision (my 3/3 spot replays green: `check_bible.py` CLEAN exit 0, parsed 5/1/3 with inherited records identical, tick-10 `depends_on` = both named tick-9 events; plus `support_check.py` 14/14 PASS and `map_obligations.py` raw=14 mapped=14 PASS), and F01–F06 + F20 all report PASS with no contradicting evidence — bounded to this one authored-minute fixture, to support demonstrated by the mapped minute plus F04's bounded whole-claim review, and to an agreement scoped "for this crossing only".**
