# Round 43 simplifier — conditional location corroboration

## Smallest meaningful depth move

If proceeding, clone the r41 fixture and add only one newly authored Jorin source/excerpt, a minimal Jorin entity claim, and one cited observation event; add a short clause map only if needed to make review traceable. Preserve the inherited Vela, Tarin, Sella, ledger, and other rows unchanged. The one bounded assertion should be that Jorin independently reports seeing Vela on the Lantern Harbor east steps during what Jorin calls Bell-7, while explicitly saying Jorin did not see who (if anyone) struck a bell. Do not add a relation, second event, or new contradiction-ledger row: the observation concerns Vela’s reported location, not Sella’s act or a competing Sella location.

Evidence: Vela’s excerpt gives her own account of standing at the east steps (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1`); the inherited source labels it newly authored and unverified (`.../sources.json:27-30`). Its entity claim and event preserve the hearing/non-sighting as Vela’s report (`.../entities.json:75-82`; `.../timeline.json:41-47`). Round 41 changed the excerpt to Vela’s direct bell identification but left those JSON claims weaker, which the adjudicator classed as compatible but under-specific (`.shokunin/lore/reports/r41-axis-adjudicator.md`, “Round 41” verdict). Thus Jorin’s narrowly matching location report could add another character’s attributed perspective, not repair or verify the bell claim.

## Risks and no-go conditions

This is not verified shared-occasion corroboration: “during what Jorin called Bell-7” does not establish that Jorin and Vela witnessed the same occasion, or authenticate the label/date. It does not corroborate what Vela heard, establish that a bell objectively rang, or establish Sella/envelope absence. The preserved r35 ledger compares Tarin’s and Sella’s conditional place claims only (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:1-`); do not reinterpret this report as settling that conflict. The source is authored fiction, not independent real-world evidence; no claims about canon, rights, or AI-training permission follow. A checker-clean result would establish structure/references only.

Novelty is doubtful: r10 already used a separate, cited witness account to add depth, and r33 proposed a single-sighting witness pattern (`.shokunin/lore/reports/r10-simplifier.md`, “Least new assertion set”; `.shokunin/lore/reports/r33-simplifier.md`, “Minimum artifact recommendation”). Round 40 already added Vela as an additional attributed account, and round 41 varied that same account’s strength (`.shokunin/lore/LOG.md:706-724`). A new name/source plus another location sighting risks being witness-count inflation, not meaningful depth. Recommend no-go unless independent review identifies a concrete narrative distinction that adds depth beyond these precedents without implying shared occasion or objective truth.

## Falsifiable test

A non-author reviewer must map the sole new assertion to Jorin’s exact excerpt, verify source/entity/event IDs and actor/place references, and confirm inherited rows remain unchanged. Ask whether the new report conveys a distinct, useful perspective rather than merely repeating Vela’s self-report; if not, reject depth. The reviewer must specifically reject each inference that the two accounts share a verified occasion, a bell objectively rang, or Sella/envelope were absent. Any such inference in the authored claim or map, unsupported wording, or failure to show meaningful novelty falsifies the depth case. Checker success alone is not the test.

Scope: report only; no fixture, checker, README, LOG, or commit changes.
