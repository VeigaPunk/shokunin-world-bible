# V58 — claim-text-audit (round 95)

Seat: V58 `claim-text-audit`. Scope: read the r95 LOG declaration line by line
(`LOG.md:2751-2806`) and compare every phrase with delivered reality; flag any phrase that
overclaims what the round can demonstrate (denominator slips, "closed" vs "bounded",
canonical-scope wording). Leaf seat: no nested agents, no commits, no network; only this
report written. Scratch used `/tmp/v58-mut/` (no repo scratch declared for this seat).

Baseline: r94 closure `fb118c4` (`git log --oneline -1` → `fb118c4 lore r94: close round …`).

Artifacts audited at freeze (sha256, first 16 chars):

```
d1c239ccb2140449  corpus/tools/map_obligations.py          (P1, stable across ~30 min of checks)
8173bb97592a3777  corpus/tools/map-obligations-contract.json (P2)
5d033c9db8a72801  corpus/tools/README.md                    (P2 addendum)
30281ff1a497bbe6  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md (P4)
f87ed42ad4d42143  corpus/knowledge/r95-aftermath-scope-note.md (P5)
```

Poll-wait: 20 s cadence, 40 tries; ALL_PRESENT at try=37 (tool+contract+README changed,
fixture present, P5 note present, 5/5 producer reports). Nothing verified before the
artifact looked complete; P1's mid-flight broken revision (`ca05159e…`, `ValueError` on
r93/r94) was observed and is reported below as mid-flight evidence, not as the deliverable.

## 1. Verdict table — declaration phrase vs delivered reality

| LOG line | Declared phrase (abridged) | Delivered reality | Verdict |
|---|---|---|---|
| 2755 | Baseline = `fb118c4` | HEAD = `fb118c4` | TRUE |
| 2759 | "Scores remain unmeasured" | no scalar anywhere; per-axis verdicts only | TRUE |
| 2764 | "close … BR-02 (schema-drift class)" | delivered class is entity-claim-container-bounded; see F2 | TRUE (bounded; wording) |
| 2764 | "close … BR-03 (self-test coverage gaps)" | 2 new persisted cases; one map_missing variant missing; see F3 | TRUE (partial; wording) |
| 2765-2767 | Before: renamed `claims` + removed row → silent PASS exit 0; self-test 20 cases | independently reproduced; 20 cases at baseline | TRUE |
| 2768 | After: exit 1 with stable `schema_drift` FINDING ID | `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claims_renamed'`, exit 1; two runs byte-identical | TRUE |
| 2769 | persisted contract carries 22 cases incl. `map_missing`, `invalid_arguments` | contract 22 ids; `--self-test` 22/22 `RESULT PASS` exit 0 | TRUE |
| 2770-2771 | r93 12/12, r94 14/14, frozen replay, r87/r89 fail-closed unchanged | all verified; 169-fixture sweep shows exactly one change (r88) | TRUE |
| 2772-2773 | counting commands (old tool vs delivered; `--self-test` exit 0) | both run; see §3 | TRUE |
| 2775 | "first reported non-performance against a crossing-scoped agreement" | no counterexample in 6-phrase corpus sweep; r23 witnessed-absence is a distinct class (P5 note §Precedent) | TRUE (novelty not exhaustively provable) |
| 2776-2781 | fixture path, `aru-aftermath-note`, tick-11 `aftermath-missing-evin` (aru / chalk-stair / depends_on), bounded wording | all fields verified in delivered JSON and excerpt text | TRUE |
| 2782-2783 | Before 5/1/3 + 3 sources, 14 obligations | measured 5/1/3, 3 sources, `raw=14` | TRUE |
| 2783-2785 | After 5/1/4, 4 sources, 15 obligations (14 inherited + 1 new), no new claims/entities/relations | measured 5/1/4, 4 sources, `raw=15`; entities/relations byte-identical; 14 inherited rows parsed-value identical, new row `timeline.json#/3` | TRUE (see F4) |
| 2785 | `check_bible` CLEAN exit 0 | my own run: `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 | TRUE |
| 2786 | census 168→169 | 168 dirs excluding r95; 169 with | TRUE |
| 2786-2787 | No perpetual-breach, canon-truth, or identity inference | excerpt: "I assert no other duty, no breach, and no obligation beyond this crossing"; sources reliability_note and README bound it identically | TRUE |
| 2789-2792 | r88 Before exit 2 `unsupported_map`; After "12/12 PASS over the r88 map's obligations" | Before verified; After = `OBLIGATIONS raw=10 mapped=10` + `INVENTORY … TOTAL-ROWS 12/12`; see F1 | DENOMINATOR SLIP |
| 2792-2793 | "with the same anchors/spans/modes" | tool parses only pointer + source-ID columns; means map unmodified; see F5 | TRUE (wording ambiguity) |
| 2793 | r87/r89 legacy forms remain exit 2 fail-closed | r87-myth `unsupported_map` exit 2; r89-inspiration-paraphrase `unsupported_map` exit 2; mapless r89 `map_missing` exit 2 | TRUE |
| 2794-2795 | support_check receipts on r88 (10 JSON + 2 editorial) and r93/r94 unchanged | r88 `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12` + `MODES 12/12`; r93 `12/12`+`15/15`; r94 `14/14`+`16/16` — identical before and after delivery | TRUE |
| 2799-2801 | no `[x]`, no promotion, no capability row before demonstrated result | `SHONEN.md`, `SCORECARD.md`, `PROVINCE.md` untouched (`git status`) | TRUE |
| 2801-2805 | producer byte-ownership P1…P5 | final `git status` shows exactly the declared files; nothing else in `corpus/` modified | TRUE |
| 2806 | everything else read-only except seat reports | `git status --porcelain`: `M LOG.md`, `M corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}`, `?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md`, `?? .ufo/waves/round-95/` — nothing else | TRUE |

## 2. Findings to flag for L1's closure note (append-only)

**F1 — C3 denominator slip (highest-value finding; `LOG.md:2792`).**
"After: 12/12 PASS over the r88 map's obligations" attributes 12 to *obligations*. r88 has
**10** raw source-attributed obligations (4 `first_appearance` + 4 entity claims + 0
relations + 2 timeline). 12 is the r88 map's declared **total row count** (10 JSON facts +
2 editorial rows — its own inventory line reads "10 JSON facts; 2 editorial rows; 12 total
mapped rows; 8 distinct excerpt anchors"). The delivered tool prints both numbers, correctly
labeled, on an exit-0 PASS:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS   (exit 0)
```

This is inconsistent with the round's own convention (r93 "12/12" and r94 "14/14" are raw
obligation counts). Independently corroborated: P1 report §6.1 ("The round's `12/12` for
r88 is the map's total row count, not an obligation count") and P2 report note 2.
*Suggested closure note:* restate as "10/10 obligations (+ inventory TOTAL-ROWS 12/12)".

**F2 — C1 "close … BR-02 (schema-drift class)" is bounded (`LOG.md:2764`).**
Delivered detection (`map_obligations.py:357` `claim_shaped`, `:377-388`) scans
**entities only** and fires only on a non-empty list of claim-shaped records (non-empty
`statement` + `source_id`) under a key other than `claims`. Name-independent for the BR-02
instance, but: relations/timeline unknown keys are not scanned; a rename that also changes
the inner record shape stays a silent PASS (P1 probe 2); scalar renames are not detected.
The declaration's own After clause hedges correctly ("that exact mutation class yields exit
1"), and P1 §6.3 + P2's README addendum state the bound ("not general JSON-schema or
unknown-key validation"). *Suggested closure note:* "BR-02 closed for the entity
claims-container mutation class (shape-based); broader unknown-key validation remains open".

**F3 — C1 "close … BR-03 (self-test coverage gaps)" is partial under the ledger's own
enumeration (`LOG.md:2764, 2769`).** The r94 ledger names the gap as "`map_missing`
(nonexistent map file / map path is a directory) and `invalid_arguments`"
(`.ufo/waves/round-94/followup/F29-debt.md:44`). Delivered persisted cases exercise:
`map_missing` = absent-map-file variant only (`prepare_test_case` does
`(cluster / "claim-excerpt-map.md").unlink()`, `map_obligations.py:651`); `invalid_arguments`
= missing-cluster path only (invoked with no argument, `:728`). The directory variant and
the two usage-combination variants remain externally exercised only. *Suggested closure
note:* record the persisted variant per case.

**F4 — C2 "14 inherited rows carried unchanged" needs its own qualifier (`LOG.md:2784`).**
Rows J01-J14 are parsed-value identical but not byte-identical: the path-qualification
column changed (`r94-paired-crossing:paired-clock` → `r95-crossing-aftermath:paired-clock`,
and the `crossing-minute` rows likewise). Verified with the tool's own parser:

```
inherited parsed-value identical (pointer,source_id): True
new parsed rows: ['timeline.json#/3']
```

The next clause ("inherited r94 rows parsed-value identical", `LOG.md:2785-2786`) supplies
the accurate reading, and P4's report discloses the column change explicitly. Low severity;
no correction strictly required.

**F5 — C3 "with the same anchors/spans/modes" (`LOG.md:2792-2793`) can be misread.**
`map_obligations` reads only the pointer and source-ID columns (`parse_map_text`,
`map_obligations.py:273-322`); it does not parse anchor/span/mode columns at all. The phrase
is only true in the sense "the r88 map is unchanged (zero corpus modifications)" — verified:
`git status --porcelain corpus/fixtures/` is empty and the r88 map bytes are untouched.
Anchors/spans/modes are validated by `support_check` instead (`MODES 12/12`, unchanged).
Low severity wording.

**Minor observations (not declaration overclaims):**
- P1 report §4 says "All other 150 fixtures identical"; my independent sweep compared **169**
  fixtures (old-tool histogram `{2:166, 0:3}` → delivered `{2:165, 0:4}`), i.e. 168 identical
  + exactly 1 changed (r88). Producer-report arithmetic slip; the LOG declaration is unaffected.
- BR-05 witnessed live: transient `map-obligations-self-test-*/` scratch directories appeared
  in `git status` during the round (e.g. `map-obligations-self-test-tue_okix/`, and
  `map-obligations-self-test-i91syily/` observed after my final battery); P2's addendum
  states BR-05 is unchanged in r95 — consistent, no overclaim.
- Seat reports observed at final check: 33 `.md` reports (5/5 producers) vs 64 declared
  seats — process witness only (verifier seats may still be writing; the declaration's
  ABSENT-reporting rule covers this).
- P1's mid-flight revision `ca05159e…` (before its report) crashed on r93/r94 with
  `ValueError: too many values to unpack (expected 2, got 12)` at `compare()`; the delivered
  revision `d1c239cc…` does not. Disclosed in P5's note and P1's report; not a deliverable defect.

## 3. Independent evidence for the verified clauses (commands + observed outputs)

Baseline before-state (tool = `git show fb118c4:corpus/tools/map_obligations.py`, run from
`/tmp/v58-mut/`):

```
$ python3 map_obligations.baseline.py /tmp/v58-mut/fixture     # entity[0].claims renamed + its map row removed
OBLIGATIONS raw=13 mapped=13
RESULT PASS                      (exit 0 — the declared silent PASS, reproduced)
```

Delivered after-state (my mutation, same scratch fixture):

```
$ python3 corpus/tools/map_obligations.py /tmp/v58-mut/fixture
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claims_renamed'
RESULT FAIL                      (exit 1)
finding-hash run1=73d9f8eacd3548a5 run2=73d9f8eacd3548a5 stable=yes
```

Self-test and frozen replay:

```
$ python3 corpus/tools/map_obligations.py --self-test
… 22 SELF-TEST PASS lines including:
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
RESULT PASS                      (exit 0)
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified / OBLIGATIONS raw=12 mapped=12 / FROZEN expected=PASS/0 findings=none matched / RESULT PASS  (exit 0)
```

Fixture receipts: r93 `12/12`, r94 `14/14`, r95 `15/15` all PASS exit 0 (with matching
INVENTORY lines); r87-myth-cluster and r89-inspiration-paraphrase exit 2 `unsupported_map`;
r89-fn2-control exit 2 `map_missing`.

Full-corpus regression, baseline tool vs delivered, every `corpus/fixtures/*/` (169 dirs):

```
swept 169  changes 1  [('corpus/fixtures/r88-m3-maya-cluster/', 2, 0)]
old histogram {2: 166, 0: 3}   new histogram {2: 165, 0: 4}
```

C2 evidence: byte-identity of `entities/relations/contradictions/inspiration-note/
source-excerpt` vs r94 (`cmp` → IDENTICAL); `sources.json` +1 entry
(`aru-aftermath-note`, reliability_note bounds breach/perpetual/external fact);
`timeline.json` +1 event (`aftermath-missing-evin`, tick 11, `entity_id aru`,
`place_id chalk-stair`, `depends_on ["paired-crossing-decision"]`, `source_id
aru-aftermath-note`, depends_on resolves to an existing id); `check_bible` CLEAN exit 0;
census 168→169; 6-phrase corpus sweep (`did not come|did not arrive|never came|failed to
appear|non-arrival|did not show`) matches only the new r95 text.

C3 evidence: `git status --porcelain corpus/fixtures/` empty (zero corpus modifications);
support_check receipts measured identically before and after delivery (r88 `10/10` +
`MODES 12/12`, r93 `12/12` + `15/15`, r94 `14/14` + `16/16`).

## 4. Bottom line

PASS — every falsifiable before→after clause of the r95 declaration verifies on the
delivered revision (tool `d1c239cc`, contract `8173bb97`, README `5d033c9d`); one
denominator slip (F1: "12/12 … obligations" should be 10/10 + inventory 12/12) and two
"close BR-02/BR-03" scope bounds (F2/F3) plus two low-severity wording items (F4/F5) are
flagged for L1's append-only closure note; none changes the delivered substance.
