# F20 — anti-overclaim critic (round 94, FOLLOW-UP)

**Seat:** F20, adversarial overclaim critic. **Candidate judged:** `abbc3e0` (`lore r94: checkpoint Luna WORK candidate pending DeepSeek review`), diff scope `9c2eea3..abbc3e0` = 154 files / 7,554 insertions (added: 152 files; modified: `LOG.md`, `SCORECARD.md`). Lane `HEAD` at run time `65a9329` (declaration commit; `git status --porcelain` showed only the untracked `.ufo/waves/round-94/followup/` tree). No file outside this report was written.

**Method.** (1) Full-text token sweeps for each hunted class over every changed path, including all 31 seat reports, the tool, its contract, the frozen snapshot, the new fixture, the new knowledge record, `LOG.md` and `SCORECARD.md`. (2) Re-execution of every executable claim in the added bytes against the delivered tree. Three artifacts are machine-generated bulk data (`W04-baseline.json`, `W05-baseline-corpus.sha256`, `W22-evidence.json`); those were verified by re-running their producers/aggregates and their claimed digests rather than read line-by-line (stated as a coverage limit, not claimed as a line-by-line read).

---

## 1. Class sweep — suspect phrases and whether they are bounded in place

### canon-truth
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "It is not an in-world source and supplies no fictional canon." | `corpus/fixtures/r94-paired-crossing/inspiration-note.md:21` | Yes — explicit non-claim in the same sentence |
| "they do not make Spence an in-world witness, assign cultural meaning, or add canon." | `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md:39` | Yes |
| "not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review." | `corpus/fixtures/r94-paired-crossing/README.md:19` | Yes |
| "This is a sourced editorial decision record, not merged canon or a cultural-history claim." | `corpus/knowledge/r94-cross-myth-design-comparison.md:7` | Yes |
| "## JSON facts (14 canonical pointers)" / "canonical JSON-pointer rows" | `claim-excerpt-map.md:16`; `corpus/tools/map-obligations-contract.json:3` | Yes — "canonical" is grammar terminology, and the contract's `scope` line forbids canon judgment |
| "The new authored minute supports Chalk Stair, Aru/Evin's one-crossing agreement, and the tick-10 decision after/dependent on both tick-9 entries." | `LOG.md:2668` | Yes — same entry adds "Author-side proposition review is not outside non-author verification or the required FOLLOW-UP"; `SCORECARD.md:373` adds "author-side whole-proposition review and three bounded mythology design comparisons are delivered, not independent judgment" |

No added byte asserts fictional canon as true or treats a checker receipt as a truth verdict.

### rights
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "The rights status of this edition, its presentation, and the delivered excerpt has not been determined for all jurisdictions." | `corpus/fixtures/r94-paired-crossing/inspiration-note.md:15` | Yes — open question, no grant |
| "Rights and AI-training permission remain unassessed; neither is granted or inferred here." | `README.md:17` | Yes |
| "Rights and AI-training permission are not assessed by this record" | `corpus/knowledge/r94-cross-myth-design-comparison.md:17` | Yes |
| "Gutenberg's eBook page says public domain in the USA; this is not a global rights determination or AI-training permission." | `.ufo/waves/round-94/work/W07.md:8` | Yes — trailing clause bounds it; not reproduced here (network barred for this seat), and no product or `LOG`/`SCORECARD` claim relies on it |

### AI-training-permission
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "AI-training permission has not been assessed or established. Public accessibility, attribution, or a possible copyright conclusion does not imply permission for training; this question remains separate and unanswered." | `corpus/fixtures/r94-paired-crossing/inspiration-note.md:19` | Yes — the strongest and most explicit bound in the added bytes |

No added byte grants, implies, or infers training permission.

### perpetual-performance / alliance
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| `"type": "agreed_co_stewardship_for_this_crossing"` | `corpus/fixtures/r94-paired-crossing/relations.json:5` | Yes — the value itself is scoped "for this crossing" |
| "It is not evidence of an alliance, a continuing practice, or perpetual performance." | `README.md:9` | Yes |
| "not evidence of continuing performance, a standing alliance, or an external historical fact." | `corpus/fixtures/r94-paired-crossing/sources.json:18` | Yes |
| "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance." | `claim-excerpt-map.md:48` | Yes |
| "This is not an alliance or proof of later performance." | `corpus/knowledge/r94-cross-myth-design-comparison.md:35` | Yes |

### authenticated-testimony
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "not an authenticated K'iche-language primary text" | `README.md:17`; `claim-excerpt-map.md:39` | Yes |
| "This is Spence's English prose about a story he labels 'Kiche,' not a quotation from a K'iche-language edition." | `corpus/fixtures/r94-paired-crossing/source-excerpt.md:7` | Yes |
| "No R5 support or R9 manual-review PASS is claimed." | `corpus/knowledge/r94-cross-myth-design-comparison.md:13` | Yes |
| "This is my author-side inspection, not independent validation or source authentication." | `corpus/knowledge/r94-cross-myth-design-comparison.md:36` | Yes |

### identity-inference
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction." | `README.md:7` | Bounded, but ambiguous — see F20-2 |
| "are distinct path-qualified references, not identity evidence." | `corpus/knowledge/r94-cross-myth-design-comparison.md:23` | Yes |
| "The raw source ID is `paired-clock`, resolved here as `r94-paired-crossing:paired-clock`; the prior namespace is `r88-m3-maya-cluster:paired-clock`." | `claim-excerpt-map.md:18` | Yes — namespace statement, no identity claim |

### Blue-Seal-style inference drift / occupied-slot-misnomer class
- `grep -rn "occupied-slot"` over the added bytes returns **no** occurrence: the corrected misnomer is not repeated. It survives only in the frozen inherited snapshot `corpus/fixtures/r88-m3-maya-cluster/README.md:5` ("an occupied-slot near-miss, not a double-booking"), which the round contract made read-only. The r88 closure correction is at `SCORECARD.md:139` ("the 'occupied-slot near-miss' is a shared-tick near-miss (slot key is `(entity_id, tick)`) — naming corrected at closure") and `SCORECARD.md:145-146`.
- One new phrase falls in this class and is **not** bounded in place — F20-1 below.
- Positive note: the requirement owned by the failed W20 seat is independently satisfied in the product at `README.md:13` ("`first_appearance: crossing-minute` identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses "chalk stair" as an unowned crossing metaphor"), so the W20 failed-output gap does not leave that drift unguarded.

---

## 2. Items not bounded in place (all low severity; none is an overclaim of the hunted classes)

**F20-1 — unbounded interpretive label "their near-miss" (`corpus/fixtures/r94-paired-crossing/README.md:9`).**
Quoted: "It adds a consequence; it does not change the earlier locations or turn their near-miss into a contradiction."
The inherited register says only two same-tick entries at distinct places (`corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:12-13`; map restatement at `claim-excerpt-map.md:48`: "separate occasions at distinct places"). "Near-miss" is an authorial label for the pair, carries no in-place caveat, and drops the "shared-tick" qualifier recorded as the corrected name at r88 closure (`SCORECARD.md:139`). It asserts no canon fact, right, permission, identity, or performance — severity low; it is the only new phrase that describes a relation between the inherited entries that the excerpt does not state.

**F20-2 — ambiguous identity clause (`README.md:7`).**
Quoted: "path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction."
Read one way, "does not imply … entity identity" denies identity continuity for the inherited referents, which the continuation's own framing asserts (`README.md:3`, and `W11.md:13`: "reuse of `aru`, `evin`, place IDs, and inherited source IDs is identity continuity"). The clause's subject is source-ID qualification, so the "entity identity" item is a non-sequitur in the list. Direction of risk is under-claim/ambiguity, not overclaim.

**F20-3 — stale count in a seat report body (`W02.md:8`, `W02.md:13`).**
Quoted: "persisted expected exits and finding IDs for 12 isolated self-test cases" / "all 12 real-CLI subprocess cases passed". The delivered contract has 20 cases (`corpus/tools/map-obligations-contract.json:24-46`) and `--self-test` runs 20/20. Bounded only by the appended addendum `W02.md:26` ("The original 12-case self-test observations above are retained as historical. This continuation expands the persisted suite to 20 real CLI cases"); not in place.

**F20-4 — stale prospective prose in the new knowledge record (`corpus/knowledge/r94-cross-myth-design-comparison.md:12`, `:17`).**
Quoted: "The planned r94 minute may reuse this contrast only after its authored excerpt is delivered; its wording, source dependencies, and claim support are currently unverified." and "The planned r94 minute is an intended design target only until delivered and checked against its actual in-world source."
Both are now false of the delivered fixture and are overridden only by the dated addendum at `:19-21` ("This addendum overrides only the preceding prospective statements that the minute was not yet delivered or checked"), not in place. This is a stale under-claim (false-negative), the safe direction for this seat.

**F20-5 — negative result disclosed only in the seat report (`W30.md:8`).**
Quoted: "`node .ufo/waves/round-9/corpus-gate.mjs --repo lore-shokunin --round 94 --label lore-shokunin` exited 1 overall. Its summary reports `findings=6 rules=r4,r10` … Thus the SHONEN form check was clean, but the full gate was **not** clean."
Neither `LOG.md:2663-2673` nor `SCORECARD.md:369-383` mentions this exit-1 gate run; the `LOG` gate sentence cites only the runs that exit 0. Nothing asserts the gate was clean, so this is a disclosure gap, not an overclaim.

**F20-6 — externally-sourced claim unreproducible in this seat (`W07.md:8`).**
Quoted: "`python3 .ufo/waves/round-94/work/W07-gutenberg-check.py` returned HTTP 200 and PASS … A read-only sweep of the Gutenberg transcription found zero `George G. Harrap` hits".
This seat is barred from network calls, so the fetch and the publisher-absence finding could not be re-run. The claim is bounded in place, is not cited by `LOG`/`SCORECARD`/product, and no product claim depends on it. Recorded as a reproducibility boundary for the record, not as a defect.

**F20-7 — nuance on the lane's own negative claim (no defect; verified).**
`LOG.md:2673` and `SCORECARD.md:383` call W20's return "malformed tool-call-like text with extensive repetition, not a usable review". Measured: the W20 record in `work-results.xml` is 212,610 bytes vs 990–3,446 bytes for each of the other 31 records, contains 52,517 repeated `"}"}` tokens, and has no `RESULT`/`PASS`/`Conclusion` line. Nuance worth keeping: it does open with one coherent bounded status payload (`{"title":"The round-94 candidate is not present yet", … "this is not a product verdict"}`), so "not a usable review" is accurate for the assigned review task rather than a claim that the bytes are pure noise.

---

## 3. Executable claims re-run against the delivered tree (all reproduced)

| Claim (source) | Command | Observed |
|---|---|---|
| C1/C2 map obligation counts | `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` | `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS`, exit 0 |
| r93 positive (`LOG.md:2669`) | `… corpus/fixtures/r93-m2-kojiki-cluster` | `OBLIGATIONS raw=12 mapped=12` / `RESULT PASS`, exit 0 |
| 20 real-CLI self-test cases (`LOG.md:2669`) | `… --self-test` | 20 `SELF-TEST PASS` lines (each case exit/finding-ID matched), `RESULT PASS`, exit 0 |
| digest-pinned snapshot (`LOG.md:2669`) | `… --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified`; `FROZEN expected=PASS/0 findings=none matched`; exit 0 |
| frozen snapshot is the r93 input | `diff -q` frozen vs live r93 for all four files | `IDENTICAL` ×4 |
| structural check (`LOG.md:2668`) | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` | `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 |
| lexical support 14/2/16/12 (`r94-cross-myth-design-comparison.md:29`) | `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` | `JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12` … `RESULT PASS`, exit 0 — matches the quoted receipt byte-for-byte in substance |
| inherited equality + 5/1/3 + 14 pointers (`LOG.md:2668`) | `python3 .ufo/waves/round-94/work/W01-preservation.py` | `INHERITED: 4/4 … 2/2 … 2/2`; `COUNTS: 4/0/2 -> 5/1/3`; `MAP: 14 unique canonical JSON pointers`; exit 0 |
| lexical blind spot vs raw obligation (`LOG.md:2669`) | `python3 .ufo/waves/round-94/work/W02-unmapped-demo.py` | `support_check exit=0 terminal=['RESULT PASS']`; `map_obligations exit=1 findings=['FINDING missing_obligation: entities.json#/0/claims/1 has no map row']`; `counterexample=PASS`, exit 0 |
| tamper control (`LOG.md:2669`) | `python3 .ufo/waves/round-94/work/W02-frozen-demo.py` | `frozen_baseline exit=0`; `mutated_copy exit=2 finding=['FINDING snapshot_tampered: … entities.json']`; `mutation_to_tamper=PASS`, exit 0 |
| 984 baseline pins unchanged (`LOG.md:2671`) | `sha256sum -c .ufo/waves/round-94/work/W05-baseline-corpus.sha256` | 984 lines, **zero** mismatches |
| 168 dirs / 34 clean / 134 negative / 421 violations / no stderr (`LOG.md:2671`, `SCORECARD.md:375`) | per-directory `check_bible.py` loop over `corpus/fixtures/*/` | `clean=34 negative=134 violation_lines=421`, stderr 0 bytes |
| 167 → 168 fixture directories (`SCORECARD.md:375`) | `git ls-tree -d --name-only <rev> corpus/fixtures/ \| wc -l` at both revs | `167` at `9c2eea3`, `168` at `abbc3e0` |
| raw-result digest (`work-receipt.json:11`) | `sha256sum .ufo/waves/round-94/work-results.xml` | `06bdafa04cdd8132e280270061719ab8df08e2a348b522e05cfb9979e5bec3bc` — matches |
| 32 dispatched seats (`work-receipt.json:7-9`) | parse `<subagent …>` records in `work-results.xml` | 32 records, 32 unique `agent-*` ids |
| checker hash unchanged (`LOG.md:2671`) | `sha256sum corpus/fixtures/check_bible.py` | `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` — matches `W21-c9-checker-hash.out` |
| boundary/discriminator gates (`LOG.md:2671`) | `boundary_doc_check.py`; `… --self-test`; `discriminate_check.py`; `… --checker e97613c` | exits `0`, `0`, `0`, `2` with `REGRESSION-DETECTED` — all match |

No claim in the added bytes failed to reproduce. Where a claim could not be re-run (W07's network fetch, F20-6), that is stated rather than smoothed over.

---

## 4. Bottom line

**PASS** — no canon-truth, rights, AI-training-permission, perpetual-performance, authenticated-testimony, or identity-inference overclaim survives unbounded in the added bytes of `9c2eea3..abbc3e0`, and every executable claim in that diff reproduced exactly; the sole new phrase not bounded in place is the low-severity interpretive label "their near-miss" (`corpus/fixtures/r94-paired-crossing/README.md:9`, F20-1), alongside five lower-severity stale/ambiguous/disclosure items (F20-2…F20-6) that assert nothing about canon, rights, permission, identity, or performance.
