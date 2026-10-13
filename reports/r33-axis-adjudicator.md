# Round 33 — final non-author axis adjudication

## Independent evidence

I read the round 33 declaration and post-scout policy in `LOG.md`, the executor observation, non-author reviewer and independent verifier, critic and province scout, both corpus READMEs, all seven new fixture files, and the r10/r23 precedent excerpts. The newly authored `tarin-note-excerpt.md` contains exactly: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.” The manual `clause-map.md` is not checker input.

I separately reproduced the regression using the documented `python3`, not the verifier report's `python` alias. I extracted `check_bible.py` from baseline report commit `56f924458673e86cd82588ceb7818c1cdaad44a8` using `git show`, enumerated baseline fixtures and JSON paths using `git ls-tree`, and invoked both baseline and current checker with the **same absolute current fixture argument** for each of 84 baseline directories. Raw stdout, stderr, and exit status match **84/84**. Comparing baseline `git show` bytes to the current paths gives **419/419** pre-existing JSON files unchanged. Current checker on `r33-tarin-envelope/` exits **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations\n`, stderr empty. Relative checker path and `python3` invocation follow `fixtures/README.md`; absolute equal fixture arguments in the replay avoid checker-path-dependent output differences.

Against `consistent/`, parsed old rows are preserved in order: `sources.json` 2→3, `entities.json` 4→6, `timeline.json` 2→3; `relations.json` and `contradictions.json` are byte-identical. The only new rows are:

| New row | Trace and boundary |
| --- | --- |
| `sources[2]` `tarin-note` | Title, kind and reliability note are **editorial fictional-source metadata**, not claims quoted from the sentence. The note explicitly calls the observation reported, not omniscient. |
| `entities[4]` `tarin` | “I, Tarin” supports the name and first-person observer; `tarin` and first-appearance source ID are fixture-local editorial alignments. Its sole `tarin-note`-cited claim retains “reports seeing”; “saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk” supplies its action, object and place words. |
| `entities[5]` `sella` | “Sella” supports the name; `sella` and first-appearance ID are editorial alignments. Its `tarin-note`-cited claim explicitly attributes the placement to **Tarin's report** rather than Sella's testimony or established fact. |
| `timeline[2]` `tarin-envelope-observation` | `entity_id=tarin` aligns to “I, Tarin”; `place_id=harbor` aligns to “Lantern Harbor”; both IDs and the event ID are editorial. Its description says Tarin **reports seeing** Sella place the described envelope on that desk, and cites `tarin-note`. `depends_on=[]` imposes no causal edge. `tick=3` is an arbitrary local sequence label; the excerpt gives no observed time or chronology. |

This is distinct from **r10**, where Sella herself records seeing Mira depart, leaves the registry destination blank, and keeps a carbon; r10 is Sella's own account, not a named third party seeing Sella perform this placement. It is distinct from **r23**, where Sella says she looked for a route strip and did not find it; that is Sella's bounded negative search, not Tarin's positive placement report. The manual mapping method, another authored source, and mere new names/rows are not themselves novel. The limited depth gain is the traceable observer/actor/action configuration: one named third party reports witnessing another named character's positive physical placement. This is a constructed first-person report, **not** independent corroboration or evidence that the fictional act happened.

## Axis verdict and admission

| Axis | Verdict | Reason |
| --- | --- | --- |
| Depth | **Improved** | New attributed third-party positive placement report, with each new claim/event clause matched to the sole excerpt and each new assertion source-cited; distinct from r10's own account and r23's non-finding. |
| Coverage | **Unchanged** | No checker rule or broader input class added; the new fixture is one bounded source-to-record observation. |
| Calibration | **Unchanged** | Editorial IDs and arbitrary tick are labeled, and report attribution is retained. No claim of verified action, content, causation, rights or canon. |

**Admit the narrow depth move:** at least one axis improved and none harmed. Clean checker output establishes structure and citation-ID resolution only; it does not read the Markdown or prove prose truth. “Unlabeled paper envelope” says nothing about contents, ownership, recipient, delivery, motive, destination, Blue Seal, carbon, route strip, or a relation to previous events. No envelope entity, new relation, contradiction, real-world rights/AI-training permission or canon finding is warranted. This verdict is not a SHONEN checkmark, promotion, push, or merge.
