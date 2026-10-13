# Round 54 schema scout — isolated r15 clone

## Recommendation: conditional NO-GO on material depth; schema-safe candidate is feasible

The data model can carry a narrow Jorin-reported visual observation without any item-provenance/holder transition. But feasibility is not evidence of depth. On current evidence I recommend **NO-GO / depth unchanged**: an authored Jorin account of seeing a blurred oval on a sheet Sella identified as her retained carbon could establish a bounded, attributed comparison, but it risks reading as manufactured corroboration of the exact same physical mark on a document whose identity is not verified. It adds no consequence, discovery, or changed uncertainty beyond Sella’s existing reported inspection. A non-author could reverse this only if exact proposed text makes a distinct, meaningful comparison (not simply “another witness also saw blue”) while preserving the limits below.

## Schema-safe minimal mapping (if a distinct textual move is justified)

Use an isolated byte-preserving clone of `corpus/fixtures/r15-carbon-followup/`; retain all inherited JSON rows and both existing excerpts. Add one `jorin-note` row to `sources.json`, with reliability note explicitly saying newly authored, fictional, unverified first-person report—not omniscient truth. Add a `jorin` character to `entities.json`, first appearance `jorin-note`, with one source-cited claim limited to Jorin’s self-identification and reported viewing of the displayed sheet/oval. Add one timeline row sourced to `jorin-note`, actor `jorin` (observer, not carbon holder), using only a place actually named in the new Jorin text; if text names no existing place, do not assume Lantern Harbor, add a place, or assign one. An event is optional: only include it if the clause map and chosen scene-place are textually supported. Choose a fresh fixture-local tick after the existing maximum as editorial ordering only, and no dependency unless the source explicitly supports sequence. No `relations.json` change is needed. Do not add a carbon item or provenance array; schema provenance records holder transitions and has no report-attribution semantics.

## Source/claim/event map and bounds

| Textual clause (proposed, not authored evidence) | Safe representation | Not established |
|---|---|---|
| Jorin identifies himself and says Sella showed him a sheet she called the carbon she kept | `jorin` source-cited claim; new note excerpt | Jorin’s identity/role; that Sella actually showed it; physical identity as r10/r15 carbon; transfer or receipt |
| Jorin says he saw a blurred blue oval on the displayed sheet | Same Jorin claim; optionally one Jorin-observer event description | The mark’s origin, maker, timing, actual same mark/carbon, independent authentication, or Blue Seal connection |
| Jorin states limits/uncertainty in his own words | Preserve in claim/event clause map and source reliability note | Any assertion that Sella’s earlier observation was independently confirmed |

A place/event must follow the new excerpt literally. `source_id` merely points to a source row; the checker does not inspect excerpt clauses, validate claim support, or determine the speaker’s truth. Existing timeline ticks are fixture sequencing, not absolute chronology; a new tick cannot date Sella’s later look or Jorin’s presentation relative to it. Do not link events by `depends_on` merely to imply a handoff or same-object chronology.

## Evidence and precedent

- r10 excerpt exact wording: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” (`corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`, lines 1–5). This is Sella’s fictional report of keeping a carbon, not authenticated custody.
- r15 excerpt: “Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.” (`corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md`, lines 1–5). The speaker reports her own later inspection; source note explicitly labels it newly authored fiction.
- r49 closure rejects an unqualified provenance chain and judges the imagined Sella-only handoff to Jorin not materially deeper; provenance lacks report-status semantics. That is a hard schema/semantics constraint, not a ban on a separately attributed visual report.
- r43 closure admitted narrow depth for Jorin’s separate reported sighting of Vela at the east steps, where Vela herself reports standing. This current candidate is weaker: Sella already reports the mark, and the proposed scene/document/mark relationship is explicitly uncertain. r43 does not establish that every second account is depth.

## Falsifier and assumptions

Falsifier: reject if a clause-level non-author review finds Jorin’s only new content is seeing the same blue oval on an object Sella identified, with no distinct uncertainty-bearing detail or consequence; reject any mapping that asserts verified same carbon, actual showing/transfer/receipt, same physical mark, timing relative to Sella’s inspection, mark origin, Blue Seal link, objective canon, or rights/permission. I assume a new source excerpt and exact claim text would be authored later; no Jorin excerpt/fixture/checker result currently exists. The Round 54 proposed Jorin excerpt is hypothetical, and no same-carbon identity, handoff, receipt, mark origin, Blue Seal link, objective canon, or rights/permission is established.

No fixture, checker, README, LOG, or commit changed; this is schema scouting only.
