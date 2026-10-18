# Round 74 simplifier — editorial decision table

## Minimal proposal

Use a three-row table in a new editorial note, with each row framed as a **nonexclusive hypothesis to investigate**, not a finding. Cite the two report inputs directly: Vela’s wording is in `corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md` (source `vela-slate-note`; entity claim `entities.json` `/6/claims/1`), and Jorin’s is in `corpus/fixtures/r73-jorin-slate-claim/jorin-slate-note-excerpt.md` (source `jorin-slate-note`; claim `/7/claims/1`). The comparison already establishes only that the reports differ: `corpus/fixtures/r73-jorin-slate-claim/editorial-comparison.md` explicitly leaves slate/inscription identity, reading times, and source relationship unresolved.

| Working hypothesis (not exclusive) | What it would make worth checking next | Status / limit |
|---|---|---|
| **Separate surfaces**: the reports may concern different slates or notices. | Seek independently attributable descriptions or placement details that could distinguish the surfaces; compare only if such evidence is found. | Open. “On a slate” and “at the east steps” do not identify one or two objects. No second surface is established. |
| **One surface, different readings**: if both reports concern one surface, its wording may have differed between their unverified readings. | Seek evidence that independently identifies the same surface and bears on each reading’s occasion or wording; do not infer persistence, alteration, or sequence from the two excerpts alone. | Open. Neither excerpt dates a reading or establishes an inscription’s identity, persistence, or change. |
| **At least one report is inaccurate**: a report may not accurately reflect what was on a surface. | Seek evidence independent of either report that bears on the reported wording, and assess each report’s access and provenance without presuming which reporter is wrong. | Open. Different reported words alone do not establish error, unreliability, or which account—if either—is inaccurate. |

Rows are not mutually exclusive: for example, different surfaces would not by themselves establish either report’s accuracy. This table helps an editor choose what *kind* of evidence to seek next; it does not identify evidence that exists or choose among explanations. Keep the comparison at “different reported wording,” not “contradiction.”

## Evidence and limits

The exact excerpts and attribution pointers are cited above; the r73 comparison note supplies the current editorial boundary. The inherited Jorin sighting excerpt and map (`corpus/fixtures/r73-jorin-slate-claim/jorin-note-excerpt.md`, `jorin-clause-map.md`) concern seeing Vela and do not say he witnessed her reading. They cannot fill the identity or timing gaps. Existing knowledge-table precedent (`corpus/knowledge/2026-10-12-lore-decision-table.md`) uses condition / decision / evidence-and-limit rows, but governs checker conventions; it does not establish facts about these reports. This proposal is only an editorial structure, not a claim about in-world records.

The table should be rejected as a depth move if the rows merely restate the comparison without guiding a distinct next evidence check, imply any evidence or artifact already exists, treat alternatives as exhaustive or exclusive, privilege one witness, or infer shared identity/time, inscription persistence/change, source truth, canon, rights, or mechanics. The fixture checker validates structured records and citations, not these prose hypotheses or their truth. No hypothesis is established by the citations. No checker/fixture/LOG change, implementation, or verification is proposed here.

Scope: this report only. No other files, commits, push, or merge.
