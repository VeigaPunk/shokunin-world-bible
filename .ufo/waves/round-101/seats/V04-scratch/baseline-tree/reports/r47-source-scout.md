# Round 47 source scout — intake-slip wording and limits

## Finding

Conditional go on a deliberately modest, newly authored **in-world fictional slip** whose first-person recorder reports only an envelope's presence and the record's blank depositor field. This supplies a document-shaped, object-specific comparison to Tarin's sighting, but is not proof of a second envelope, shared Bell-7 occasion, depositor identity, or Tarin's account. The actor of an observation/recording event, if represented, is the slip's editorially named reporter/recorder only when the text explicitly says “I”; the envelope is never an actor or established mover. If the schema cannot encode those distinctions without misleading fields, no-go rather than inventing ontology.

## Proposed literal excerpt (newly authored fiction; not recovered)

> **Lantern Harbor Registry — intake slip (newly authored in-world text)**> I, Jorin, found an unlabeled paper envelope lying on the registry desk during what I called Bell-7. The depositor was not recorded on this slip.

“Found … lying” reports the writer's finding/presence claim, not observation of placement or arrival. “During what I called Bell-7” attributes the occasion label to the writer; it does not synchronize this slip with Tarin's Bell-7 wording. “Not recorded on this slip” is strictly a statement about this slip's contents. It does not assert that no depositor existed, that no one placed it, or that the registry has no other record. Jorin is a proposed fictional speaker label for the slip, not a verified person, and must be omitted/reworked if the fixture cannot justify reuse of that identity.

## Evidence and distinction

- The r47 declaration describes Tarin's attributed sighting as “saw Sella place” an unlabeled paper envelope at the harbor registry desk (`.shokunin/lore/LOG.md:788-790`; exact existing excerpt: `.shokunin/lore/corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1`). The proposed slip's grammatical predicate is presence/finding, not placement: it neither identifies the envelope as Tarin's nor supports Sella as depositor.
- r33's event already preserves Tarin as reporter/actor and says he reports seeing Sella place the envelope (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/timeline.json:22-30`); its source labels the excerpt newly authored fiction, not omniscient truth (`.../sources.json:15-19`). Do not overwrite or upgrade that account.
- The r47 baseline itself warns that R43 Jorin's separate sighting concerns Vela's reported location only and cannot bridge to this envelope (`.shokunin/lore/LOG.md:788-790`). Reusing Jorin as a fictional speaker is not evidence of identity continuity or event continuity; safest representation may use a distinct slip-recorder ID if schema needs one, without implying it is the R43 Jorin.
- r10's source scout states its proposed registry entry is invented and separates authorship, in-world identity, and truth; source IDs/citations do not authenticate content (`.shokunin/lore/reports/r10-source-scout.md`, “Authorship, identity, and truth are separate”). r23 distinguishes a bounded report of an absence from proof that an item was removed (`.shokunin/lore/reports/r23-note-scout.md`, “Risks”). The proposed blank depositor field is narrower still: absence of a name in one authored slip, not witnessed absence of a person.

## Mapping constraints

| Text span | Permissible mapping | Do not infer |
| --- | --- | --- |
| “I, Jorin” | Slip's self-attributed speaker, only if represented; identity alignment is fixture-local editorial convention | Same Jorin as r43, actual/authenticated Jorin, independent source or witness |
| “found … envelope lying” | A separately cited, attributed object-presence/finding report; if the timeline schema requires an event actor, actor is the explicitly attributed recorder/observer, not the envelope | Who brought/placed it; that it is Tarin's object; that it moved or arrived during Bell-7 |
| “unlabeled paper envelope … registry desk” | Object kind/description and broad place only if existing schema permits faithful attribution; otherwise retain prose/source alone | Contents, owner, sender, addressee, seal, carbon/strip/Blue Seal relation, exact desk identity beyond wording |
| “during what I called Bell-7” | Recorder's own occasion label | Same Bell-7/ringing as Tarin or R35, absolute time, simultaneity, date, objective bell event |
| “depositor was not recorded on this slip” | A source-text assertion about the omission in this one document | No depositor, no placement, Sella's absence/identity, completeness of registry, independent confirmation |

Every added claim/event must cite only the new fictional source. The source metadata and excerpt must label it newly authored. A citation proves only fixture attribution; the checker cannot establish prose entailment, actual authorship, documentary authenticity, independence, truth, rights, or canon.

## Risks and falsifiable go/no-go

**Go only if** an executor can preserve the exact distinction between object-presence report and placement/depositor, cite the invented slip, map every structured assertion to an exact phrase, and represent the reporting actor without treating the envelope as an actor or silently equating the source with R43 Jorin. A non-author reviewer must be able to answer “no” to each: Does the artifact say Sella placed it? Does it establish that this is Tarin's envelope? Does it establish the same Bell-7 occasion? Does blank depositor text prove no depositor? Any “yes” falsifies the bounded mapping and requires repair or rejection. Structural checker CLEAN and old-fixture replay are necessary but do not prove depth or text support.

**No-go** if the schema forces an unqualified envelope event, a depositor/placer identity, or a Jorin identity merge; if the only alleged gain is another cited witness/source row; or if the non-author reviewer finds no material narrative value beyond witness-count growth. The potential distinct value is a documentary **presence plus explicit local record omission** compared with Tarin's placement report—not corroboration of placement or an identified shared object. If admitted, depth alone may improve narrowly; calibration and coverage should remain unchanged. Otherwise reject; do not claim checker or source authenticity as evidence of the axis.
