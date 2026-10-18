# Round 56 — independent Sol axis adjudication

**Verdict: REJECT; roll back the candidate checker, fixture README, and `r56-holder-ambiguous/` changes.** The two new diagnostics accurately point to structurally ambiguous references, but this constructed case does not show a *material* improvement in operator calibration beyond the already reported duplicate ID and the already withheld chain comparison. Keep the round reports as records of the rejected experiment. No source, fixture, checker, README, LOG, or SCORECARD edit was made by this adjudicator.

## Independent pinned-baseline audit

I independently extracted pinned r55 report baseline `0170e88e7706f77a10348c9896bdb9913ff4c490` using `git archive` into `/tmp/r56-sol-r55-3j_xm2sr`, separate from the working tree. Before any temporary probe copy, I inventoried every file under `.shokunin/lore/corpus/` and compared **relative paths and actual bytes**, not merely sizes. Pinned: **1,149 files**; current: **1,154**. All **1,147 shared files other than** `fixtures/README.md` and `fixtures/check_bible.py` match byte-for-byte. No old path is missing. Exactly five new files occur at `fixtures/r56-holder-ambiguous/{contradictions,entities,relations,sources,timeline}.json`; four match their `item-chain-valid` counterparts byte-for-byte, and `entities.json` adds a copied schema-admitted `harbor` entity row. All **474/474 old fixture JSON paths and bytes** match (230,650 aggregate bytes). This byte audit fills the independent verifier's size-only limitation for non-JSON paths. The checker diff is exactly two inserted `errors.append(...)` lines, at the existing `entity_id_counts[to_holder] != 1` and `entity_id_counts[from_holder] != 1` branches; both existing `valid = False` statements, global duplicate detection, and chain-state reset remain intact. README's sole diff is the new Round 56 paragraph, correctly describing one clone, not isolated directions.

I then independently ran all **95 pinned OLD fixture directories in each repository root** with identical repo-root-relative argv, `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>`. For each run I separately captured and compared raw stdout bytes, stderr bytes and exit code: **95/95 exact triples match**, with 24 exit-0 and 71 exit-1 cases. This establishes old-case regression preservation, not new diagnostic value. The archive-root candidate replay below used a temporary copy of the candidate fixture *after* the corpus inventory; it was not counted as an old baseline file or a repository edit.

## Candidate behavior and competing judgments

Current `item-chain-valid` control: exit 0, stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`, empty stderr. With identical relative checker/fixture argv in each root, the copied candidate exits 1 in both roots. Pinned old checker output is exactly:

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
2 violation(s); no canon changed
```

Current checker output is exactly:

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
4 violation(s); no canon changed
```

Both have empty stderr. The copied `harbor` place row makes both unchanged adjacent provenance references ambiguous, **not** a `to_holder`-only and `from_holder`-only pair. It also triggers a timeline-place ambiguity from the existing checker. Both holder records were already invalidated by the pinned checker, which withheld their chain comparison; the new branch adds only field-local explanations. The global error names the duplicated `harbor` ID, while the retained short raw chain shows exactly its two uses. The two added lines improve navigability in the literal sense of displaying field paths, but do not resolve an identity, change a chain decision, uncover an otherwise accepted endpoint, or demonstrate a changed operator decision. The collateral timeline message and doubling of the displayed violation count make the incremental signal particularly hard to separate from repeated reporting. This is a risk of noise, not proof of material harm.

I considered all eight scouts (`checker`, `precedent`, `pair`, `regression`, `critic`, `simplifier`, `scribe`, `citation`), executor and parent integration note, independent verifier, and non-author reviewer. The checker/pair/critic/regression/citation **GO countercase** is real: a global declaration error does not itself point to each consuming holder field, and field-local ambiguity is consistent with relation/timeline diagnostics. The candidate indeed produces precisely those two field paths without selecting a holder or lifting the chain gate. However, relation-local precedent addressed a previously accepted/misleading consumer result; this provenance consumer was already guarded. The scribe/precedent/simplifier cautions and reviewer **FAIL** prevail on *materiality*, not on accuracy or implementability. No demonstrated consumer task shows the added field paths changing a diagnosis/action compared with the duplicate ID, preserved raw records, and suppressed chain; the sole candidate also lacks directional isolation and has timeline collateral. The reviewer’s malformed duplicate negative control yielded only a required-name error, supporting admitted-row screening, but does not establish added operator value. The independent verifier's exact old-case replay similarly establishes safety, not calibration gain.

## Per-axis disposition and next falsifier

- **Calibration: unchanged materially.** Precise new diagnostics are a small convenience, but the same unresolved ID and already withheld comparison were present; no material improvement established. Added repetition is a possible cost, not proved material harm.
- **Depth: unchanged.** No new source-level interpretation, supported claim, or independently reviewed comparison.
- **Coverage: unchanged.** One cloned test case and two report lines do not expand the underlying checker decision or provide a new class of source evidence; do not count fixture count or output count as an axis gain.

**No axis is materially improved; none is proved materially harmed. REJECT under the stated admission rule.** A future fresh move would need a schema-admitted, collateral-free, independently isolated holder-reference case and a concrete operator task showing that reference-local location changes an otherwise mistaken action/interpretation; exact old-case replay still would be necessary. Do not equate a structurally valid fixture, a source ID, or a provenance field with textual support, actual custody/transfer, owner identity, canon, or rights/permission. No objective custody or source truth is established here.
