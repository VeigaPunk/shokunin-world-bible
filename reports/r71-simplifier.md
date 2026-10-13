# Round 71 simplifier — bounded slate reading

## Recommendation

A small depth candidate is plausible, but the gain is narrow and must be judged as characterization, not as added world certainty. Add one new fictional Vela report to the declared r43-derived `r71-*` fixture. Suggested excerpt:

> I, Vela, could read “KEEP THE EAST GATE CLEAR” on the registry slate by the east steps. The cramped letters made me think the writer was in a hurry, but I never saw who wrote them.

This adds a distinct partial-witness beat: Vela reports legible wording, then marks a tentative inference from its appearance and explicitly withholds identifying the writer. The quoted words and all scene details are newly authored fiction for this candidate, not a claim about existing canon or source material. Depth is not guaranteed: if a reviewer sees this as arbitrary detail rather than a meaningful limit on Vela’s perspective, reject it.

## Minimum mapping

Clone `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/` into the declared new fixture. Preserve the five inherited JSON tables and prior excerpts/maps. Add a fictional, unverified `vela-slate-note` source row; append one claim to existing character `vela` citing that source; and append one timeline report event with `entity_id: "vela"`, `place_id: "harbor"`, matching `source_id`, and no dependencies. A new short clause map should quote the excerpt and map each clause to the exact appended row(s):

| Excerpt clause | Proposed row alignment and limit |
|---|---|
| “I, Vela” | Existing `vela` entity; first-person attribution, not identity authentication. |
| “could read ‘KEEP THE EAST GATE CLEAR’ on the registry slate by the east steps” | The Vela claim and event may report that she says she read these words at that place. This is not proof that the slate or inscription objectively existed. `harbor` is only the fixture’s broad place alignment; do not equate the east steps with the registry desk. |
| “The cramped letters made me think the writer was in a hurry” | Attribute the inference to Vela. The described letter appearance is her reported basis; haste is her interpretation, not a fact about the writer. |
| “but I never saw who wrote them” | Attribute this observational limit to Vela; it does not establish who wrote the words or when. |
| `vela-slate-note` / new event | Cite only the new fictional source. Tick, if required, is a local editorial sequence value, not authenticated time or synchronization with Bell-7/Jorin’s event. |

Keep inference explicitly separate in the entity claim/event prose—e.g. report the reading and say Vela *thought* the writer was in a hurry. Do not turn either into omniscient description. Use no new relation or contradiction row.

## Evidence, limits, and falsifier

The baseline declaration identifies the gap as no separate contemporaneous Vela response about the wording on the east-step registry slate and requires a five-table r43 clone, a sourced claim/event, and an auditable clause map (`.shokunin/lore/LOG.md`, “Round 71”). The inherited fixture has Vela’s first-person report (`.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/vela-note-excerpt.md:1`) and her existing attributed character claim/event (`.../entities.json`, `vela` row; `.../timeline.json`, `vela-listening-report`). Jorin’s account places Vela on the east steps but does not report slate wording (`.../jorin-note-excerpt.md:1`; `.../jorin-clause-map.md`). The older Vela map also cautions that east steps map only broadly to `harbor`, not the registry desk (`.../vela-clause-map.md`).

Prior experience warns against equating extra text or sharper wording with depth: r43’s simplifier calls another witness/location assertion a possible row-count increase rather than meaningful novelty (`.shokunin/lore/reports/r43-simplifier.md`, “Risks and no-go conditions”); r41 treats a stronger Vela identification as a narrow calibration move, not objective proof (`.shokunin/lore/reports/r41-simplifier.md`, “Risks and bounds”). Here the candidate’s possible value is the explicitly bounded interpretation of readable text, not a new witness, corroboration, or slate provenance.

A non-author reviewer should compare the exact excerpt against every new claim/event field and verify every factual clause is sourced and correctly attributed, with inference visibly marked. Reject if the excerpt or map implies Vela knows the writer, proves the slate’s authorship/date/provenance, asserts a Blue Seal connection, or converts “in a hurry” into objective fact. Also reject if the slate sentence is merely decorative or duplicates Jorin’s report without a distinct partial perspective. The checker at `.shokunin/lore/corpus/fixtures/check_bible.py` can establish required structure and resolvable IDs only; it cannot establish source-text support, truth, chronology, canon, rights, or game mechanics. Preserve prior fixture behavior with the declared raw-tuple regression check; this report does not claim that check was run.

Scope: recommendation only. No fixture, corpus, checker, or LOG changes; no authorship claim beyond the proposed fictional excerpt; no commit, push, or merge.
