# Round 59 prior-scout — malformed-input and ambiguity precedent

## Scope and evidence

This is a prior-art audit only. No checker, fixture, README, or LOG changes were made. Evidence was read from `.shokunin/lore/LOG.md`, `corpus/fixtures/check_bible.py`, `corpus/knowledge/2026-10-12-malformed-error-patterns.md`, fixture README, and temporary probes outside the repository.

- The loader calls `json.loads(path.read_text(encoding="utf-8"))` in `check_bible.py:18-26`; only file/read/decode exceptions are reported as `cannot load JSON`. It then validates the decoded array and rows (`:28-43`). Python's default JSON object handling accepts repeated member names and keeps the last value. No hook currently retains the raw member sequence.
- r5 measured missing file, invalid JSON, wrong top-level type, non-object row, and unknown citation as separate bounded classes (LOG.md:60-68; malformed-error-patterns.md:11-20). It documented grouped load errors and portability limits, not exhaustive malformed semantics. A duplicate member is neither syntactically invalid JSON nor any existing r5 malformed class.
- r9 establishes order-invariance precedent for repeated *timeline row IDs*: baseline duplicate `same` rows reversed changed the last-wins dependency chronology result, and the adopted rule diagnoses ambiguity rather than choosing a row (LOG.md:119-132). This concerns distinct array rows/IDs, not repeated keys inside one JSON object.
- r12 similarly withholds definite same-actor occupancy inference when valid entity rows reuse an ID (LOG.md:166-178). r26 counts only schema-admitted rows: malformed duplicate target stays raw but is screened out, with no admitted-target ambiguity (LOG.md:383-402; README.md:554-570). These support careful use of admitted records, not automatically rejecting raw duplicate object members.
- README explicitly documents duplicate-ID and admitted-row policy (lines 121-140, 554-570); it does not define a duplicate JSON object-member policy. Duplicate member names are distinct from duplicate row IDs: the former are keys repeated in one object, the latter IDs repeated in separate array rows.

## Actual raw behavior

I copied `consistent/` to temporary directories, inserted a second `place_id` member into the second timeline object with the two valid values `harbor` and `tower` in swapped orders, and ran the unchanged checker. Both runs exited 0 and printed `CLEAN: schema, citations, relations, timeline; 0 violations`. The decoder retained the final member; the resulting decoded row has one `place_id` and passes schema checks. This establishes silent acceptance/last-wins for this probe, not a real place fact or story claim.

Proposed raw behavior would be different: a decoder using `object_pairs_hook` (or equivalent) could preserve pairs and flag any repeated member name, producing a deterministic input-ambiguity error rather than selecting either value. That would likely make the current clean output an error for this case. The precise scope (all objects, only schema rows, nested objects), diagnostic and cascade-suppression behavior remain policy decisions; they have not been tested or implemented here. A duplicate where the earlier value is wrong-typed and later value valid could likewise be masked under current last-wins behavior, but is only a probe proposal.

## Calibration decision: NO-GO (provisional)

The raw behavior is genuinely lossy, but r5/r9/r12/r26 precedent alone does not prove a material calibration gain or establish that repeated JSON member names are forbidden by this corpus's input contract. r5 classified parse/top-level/row/citation errors; r9 and r12 resolved ambiguity across admitted rows; r26's boundary is specifically schema admission. None is a direct member-name convention. A global parse-time rejection could add noisy errors in nested `claims`/ledger structures or suppress useful independent findings, unless bounded semantics and output behavior are demonstrated. Prior-scout therefore does **not** recommend executor/build on this evidence alone.

**Falsifier / reversal condition:** produce a narrowly controlled, independently replayed pair showing that duplicate-member order changes a consequential checker decision or masks a schema error; establish that this input is unsupported/ambiguous under an explicit format convention; define bounded deterministic diagnostics (including nested objects and cascade behavior); and show unique-key controls plus all prior raw CLI tuples remain exact, or enumerate justified deltas with no disproportionate noise. If a prior authoritative format convention already specifies last-wins, that falsifies the proposed gain. No claim about fictional truth, canon, rights, or source support follows either result.

## Risks

- Reject-all-object-duplicates may change behavior beyond the required top-level row fields, including nested free-form/claim structures; silently selecting one value is also a risk.
- Parser-level rejection before row admission may prevent r26-style field diagnostics and unrelated checks. Duplicate-key findings should not be presented as duplicate row-ID findings.
- Standard JSON decoder wording/offsets vary; diagnostics should be deterministic and tests should assert stable classes rather than brittle parser text.
- Neither a row's `place_id` nor duplicate member values establish actual story location, canon, rights, or source-text entailment.
