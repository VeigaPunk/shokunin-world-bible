# Round 28 — final non-author axis adjudication

**Verdict: admit.** Depth **improved**; coverage **unchanged**; calibration **unchanged**. No axis harmed. The admitted improvement is a manually inspectable, fixture-local source-to-record reading for one existing `carries` relation, not a new checker capability or an authenticated source claim.

## Independent checks

I read the r28 LOG declaration, post-scout policy, executor result, reviewer, verifier (including its corrected `.shokunin` exclusion), excerpt, map, and fixture README. The verifier child gave no explicit reply; its written report is substantive evidence, not a settlement/reply substitute. Its initial `.shokhin` exclusion typo was corrected in the report. I independently extracted the baseline fixture tree from `aaa8d724f5820b07a5cb2d498777306763001441` and compared its checker against the current checker on each of **78/78** old fixture directories: stdout, stderr and exit status matched exactly. All **389/389** baseline JSON paths remain byte-identical. The new fixture's five JSON tables are byte-identical to `consistent/`; its checker exits **0**, prints `CLEAN: schema, citations, relations, timeline; 0 violations` and has empty stderr. These structural checks do not read either Markdown file.

The selected JSON record is exactly `relations[0] = {from: mira, to: seal, type: carries, source_id: courier-log}`. The complete newly authored fictional excerpt states “I, Mira, carried the blue seal.” “I, Mira” identifies the speaker *in the sentence*, “carried” supplies the carrying action, and “the blue seal” supplies its grammatical object. Mapping the speaker to entity ID `mira` and that object to ID `seal` is explicitly **editorial fixture-local alignment**, not something the lexemes alone prove. Conditional on those alignments, the verb directly supports the narrow directed `carries` encoding. `courier-log` is an in-world source-reference ID, not independent proof that the sentence is authentic or the action true.

The map's negative near-miss “the seal was near Mira” gives proximity, not Mira carrying the seal; it cannot support `carries`. The map selects no other relation. Existing entity claims and timeline events copied from `consistent/` are neither justified nor negated by this single clause. The sentence does not establish ownership, destination, duration, provenance, source authenticity, distinct real identities, or canon. The reviewer independently reached the same bounded reading. The README likewise distinguishes the structural checker result from manual interpretation.

## Axis decision

- **Depth improved:** unlike a bare `courier-log` reference for this existing relation, the constructed excerpt and exact clause map make the actor/action/object reading inspectable and expose the editorial ID assumptions. This is a narrow additional manual evidence layer, not automatic prose validation; earlier witnessed-absence and other excerpt fixtures are not erased or claimed as absent.
- **Coverage unchanged:** no checker rule, JSON record, or new input shape was added; the new directory is a copy of the clean control with two Markdown artifacts.
- **Calibration unchanged:** the near-miss and limits prevent an unsupported inference, but no separately measured calibration capability is claimed. No structural regression or prose overclaim identified.

Admission follows the declared rule: at least one axis improved and none harmed. Do not infer canon, promote a checkmark, or present this synthetic excerpt as recovered testimony.
