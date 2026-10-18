# F22 — verdict-coverage (COVERAGE axis verdict)

**Seat role:** FOLLOW-UP leaf, independent per-axis verdict for **COVERAGE**. Scope: what admitted surface actually grew in the r94 candidate (new fixture class, new tool surface), the evidence commands, and the bounds. Not in scope (other seats): whole-claim entailment, comparison review, depth/calibration verdicts, admission. One verdict, no scalar.

**Tree under test:** HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (`git rev-parse HEAD`); WORK candidate `abbc3e0`, baseline `9c2eea3`. Corpus bytes at HEAD are byte-identical to `abbc3e0`: `git diff --stat abbc3e0..HEAD -- corpus/` printed **0 lines**, and `git rev-parse HEAD:corpus/fixtures/r94-paired-crossing/timeline.json` = `git rev-parse abbc3e0:...` = `bd25265efbd21257b54c0a7893edcdba3e2c30a2`. `git status --short` showed only `?? .ufo/waves/round-94/followup/`. All commands from repo root with `python3`. No corpus edits, no scratch files; this report is the only file written.

---

## Verdict

**COVERAGE — improved (bounded).** Two admitted surfaces grew, each verified by its own command, and each with an observed limit; nothing else grew.

---

## 1. Fixture surface — one new fixture class, verified

`git diff --name-status 9c2eea3..abbc3e0 -- corpus/` printed exactly 13 lines, all `A` (10 fixture files, 1 knowledge doc, 2 tool files); `| grep -cv "^A"` returned `0`. Fixture directories: 167 at `9c2eea3` → 168 at `abbc3e0` (`git ls-tree -d --name-only <rev> corpus/fixtures/ | wc -l`), i.e. exactly one new fixture dir, consistent with the r93 census figure at `corpus/fixtures/README.md:1125`.

Counts and inheritance (`python3` on the two fixture dirs): entities 4→5, relations 0→1, timeline 2→3; `new_e[:4]==old_e` and `new_t[:2]==old_t` both printed `True`; the single new entity is `chalk-stair`, the single new event is `paired-crossing-decision`.

The new fixture is admitted into the **existing** enforced surfaces, not only the new tool:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations        EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
... PASS J01..J14, S01, S02 ... RESULT PASS                        EXIT=0
```

Three components of the "new fixture class" claim, each checked against the whole corpus:

1. **Well-formed multi-parent dependency is new.** A `python3` census of every fixture's `timeline.json` found 8 fixtures containing an event with more than one `depends_on` entry — and every one outside r94 carries an invalid, malformed, or anomalous parent (full census output, abridged to one representative row per family):

| fixture | event | depends_on | role of that fixture |
|---|---|---|---|
| `r20-mixed-edges` | `r20-valid-c` | `['r20-negative-b','r20-valid-a']` | invalid-prerequisite **control** — `corpus/fixtures/README.md:421` "tests an invalid prerequisite edge and a separate valid-to-valid inversion on one row" |
| `r22-mixed-first` / `r22-mixed-last` / `r22-multiple-invalid` / `r22-self-repeated` / `r22-unknown-mixed` | `r20-dependent` | `[None,'r20-prereq']`, `['r20-prereq',None]`, `[None,{},[],'r20-prereq']`, `['r20-dependent','r20-dependent',None]`, `['missing',None]` | malformed/self/unknown element controls |
| `r8-deps-anomalous` | `arrival` | `['departure','departure','arrival']` | duplicated/self-edge anomaly control |
| `r94-paired-crossing` | `paired-crossing-decision` | `['aru-ninth-bell','evin-ninth-bell']` | **first positive-path fixture** with two distinct, valid, earlier named events |

   So a cross-event dependency per se is not new (it is broad: `consistent`, `r15-carbon-followup`, `r87-myth-cluster`, `r93-m2-kojiki-cluster` all chain one parent); what is new is a *well-formed two-parent* dependency in a clean fixture, which the map declares as such (`corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md`, "Timeline normalization and scope").

2. **Agreement-type sourced relation is new.** A census of `type` values across all 155 `relations.json` rows found 10 distinct types (`carries`, `allied_with`, `consults`, `records_departure`, `keeps_watch_with`, `records_at`, `wields`, `filed_at`, `annotates`, `agreed_co_stewardship_for_this_crossing`); `agreed_co_stewardship_for_this_crossing` occurs exactly once, in `r94-paired-crossing`. Sourced relations as a surface are *not* new (`r87-myth-cluster` `keeps_watch_with`/`records_at`, `r93-m2-kojiki-cluster` `filed_at`/`annotates`); the new element is the agreement semantic with an explicit "this crossing only" bound, anchored at `fictional-excerpts.md:19` (`support_check` `PASS J11 ... anchor=found`).

3. **Explicit cross-fixture continuation is new.** `grep -rn "continuation of" corpus/fixtures/*/README.md` matched only `corpus/fixtures/r94-paired-crossing/README.md:3` ("This is an explicit continuation of `r88-m3-maya-cluster` ..."). No earlier fixture README declares itself a continuation of another fixture (r93's cluster is described as a *distinct* third family, `corpus/fixtures/README.md:1099-1101`).

## 2. Tool surface — one new comparison class, verified

`corpus/tools/map_obligations.py` + `corpus/tools/map-obligations-contract.json` are the only tool files added (name-status above). The class is genuinely new in this lane: `grep -n "entities.json\|relations.json\|timeline.json\|json.load" corpus/tools/support_check.py` produced a single hit, a map-path candidate at `support_check.py:400` — the pre-existing support checker never reads raw JSON, so raw-JSON-obligation↔map comparison did not exist before this round.

Observed behavior (four independent invocations):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14 / RESULT PASS                        EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12 / RESULT PASS                        EXIT=0
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified / OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched / RESULT PASS         EXIT=0
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS complete/missing/duplicate/phantom/source_id_mismatch/malformed_json/
co_mapped_grammar/legacy_grammar/invalid_pointer/empty_segment/noncanonical_index/
noncanonical_claim_index/foreign_path/traversal_path/symlink_path/frozen_complete/
frozen_tampered/frozen_missing_digests/frozen_expected_failure/frozen_verdict_mismatch
RESULT PASS                                                        EXIT=0
```

The 20 self-test lines' exits and finding IDs match the 20 persisted cases in `map-obligations-contract.json` one-for-one (contract `self_test.cases`, 12 distinct `finding_ids`). Independently of the map's own header text, the tool's raw enumeration is 14 — the same 14 the map declares and the wave spec expects — so the obligation count is confirmed from the JSON side as well.

## 3. Bounds — what did not grow

- **One fixture, one tool.** Exactly 1 new fixture dir (167→168), 1 new tool (+1 contract), 1 knowledge doc; 13 `corpus/` additions, **0** modifications or deletions of prior corpus paths. No second fixture, no second tool.
- **Tool scope is canonical-form only.** `python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster` and `... corpus/fixtures/r87-myth-cluster` each printed `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` / `EXIT=2`. Legacy map grammars are could-not-evaluate, so no general migration surface was added — matching the declared limit in `map-obligations-contract.json` `scope` and `corpus/tools/map_obligations.py`.
- **No new checker finding template.** The new fixture is a gate-CLEAN input (`0 violations` above), so it adds no `check_bible` finding template — the lane's established coverage phrasing for a clean-input round (`SCORECARD.md:109`; `.ufo/waves/round-87/followup/JCOV1.md:242-243,278` "adds **no new checker finding template** ... positive-path surface"). The new tool's 12 contract-persisted finding IDs are its own error vocabulary, not a template for other checkers.
- **The new relation type is not gate-enforced.** `check_bible.py:28` types `relations.type` only as `str`; the sole type-specific enforcement is `allied_with` reciprocity (`check_bible.py:347-365`). The agreement relation is admitted by row shape + source citation only, so the "new relation type" element is a thin, vocabulary-unvalidated growth.
- **Documentation/index sub-axis unchanged.** `map_obligations`/`r94` mention counts are **0** in `corpus/tools/README.md`, `corpus/README.md`, and `corpus/fixtures/README.md` (which does carry a `## Round 93` section at line 1099 but no Round 94 section), and **0** in the `SKILL.md` gate registry. This is declared pending, not hidden: `.ufo/waves/round-94/work-receipt.json` `checkpoint_limits` — "W25 documentation/registry proposals remain unimplemented; the new gate has not been registered or admitted as a capability" — and `.ufo/waves/round-94/work/W25.md` is explicitly a proposal. So the growth is delivered in `corpus/` but not yet indexed or registered.

## 4. Observations that do not change the verdict

- `python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `FINDING invalid_arguments: --frozen cannot be combined with cluster or --map` / `EXIT=2`. Usage-error path only; `invalid_arguments` is not among the 12 contract-persisted `finding_ids` (the contract persists self-test case expectations, not the full vocabulary).
- `corpus/fixtures/r94-paired-crossing/contradictions.json` is `[]`, and the fixture's two inherited events keep empty `depends_on`; the new two-parent edge is the only dependency in the fixture.

---

**Bottom line: PASS — COVERAGE improved (bounded): exactly one new fixture class (first positive-path two-parent dependency, first agreement-type sourced relation, first explicit cross-fixture continuation; `check_bible` CLEAN, `support_check` 16/16 PASS) and one new tool surface (raw-JSON↔map obligation comparison: r94 14/14, r93 12/12, frozen replay 4 digests verified, 20/20 self-test cases matching the persisted contract, r88/r87 exit-2 `unsupported_map`), with 0 corpus modifications, no new checker finding template, an unvalidated free-text relation `type`, and documentation/registry indexing still unimplemented-but-declared.**
