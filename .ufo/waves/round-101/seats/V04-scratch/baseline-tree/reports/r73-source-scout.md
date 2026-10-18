# Round 73 source scout — r72 Vela and inherited Jorin accounts

## Scope

Report-only source map for the Round 73 declaration in `.shokunin/lore/LOG.md` (Round 73, 2026-10-13). I read the declaration and its stated r72/Jorin premise; the active `r72-vela-slate-claim` and inherited `r43-jorin-vela-sighting` five-table fixtures; relevant Round 72 executor, reviewer, verifier and adjudicator reports; the Round 72 clause/prior/calibration scouts; the r43 source scout; and `corpus/fixtures/check_bible.py`. I made no fixture/checker/LOG changes and ran no checker. This report maps existing prose only; it does not assess a not-yet-authored Jorin slate excerpt.

## Exact r72 Vela account and pointers

`corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md` reads, literally:

> I leaned close to the slate and could read, “KEEP THE EAST GATE CLEAR.” The cramped letters made me wonder if whoever wrote them had been in a hurry. I could not tell who wrote them.

The associated `vela-slate-clause-map.md` divides it into three exact spans:

1. `I leaned close to the slate and could read, “KEEP THE EAST GATE CLEAR.”` — Vela reports close reading and the words she says she could read.
2. `The cramped letters made me wonder if whoever wrote them had been in a hurry.` — Vela's explicitly tentative inference, not an established writer state.
3. `I could not tell who wrote them.` — Vela's limit; not proof that nobody else can identify the writer.

All three map to the paraphrased claim at `entities.json` `/6/claims/1`, whose `source_id` points to `vela-slate-note`; that source is `sources.json` `/6`. The claim says Vela reports reading “KEEP THE EAST GATE CLEAR” on a slate, tentatively inferring from cramped letters that its unknown writer might have been hurried, and says she could not tell who wrote it. The map labels the claim alignment a paraphrase. The excerpt/map use curly double quotation marks around the reported words. Round 72 reviewer and verifier report that clause spans match the excerpt character-for-character; the nested outer/inner quote styling can be visually awkward, but was not found to be a text mismatch.

This is Vela's attributed account, not an authenticated slate, inscription, wording, author, location, or time. It does not say when the slate was written, that the words remained there, or that anyone else saw this slate or reading.

## Exact inherited Jorin account and pointers

The r72 clone inherits `jorin-note-excerpt.md` byte-for-byte from r43. Its full prose is:

> I, Jorin, am a registrar, and I stood at the Lantern Harbor registry doorway. I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7. I did not see who, if anyone, struck a bell.

The inherited `jorin-clause-map.md` says this is Jorin's stated vantage and claimed visual sighting; the doorway is not equated with the east steps or registry desk, and the event's broad `harbor` place is editorial scene alignment. It says the shared label “Bell-7” does not establish a shared occasion, chronology, or objective ringing. It explicitly cautions that this does not verify Vela's report. The excerpt does **not** mention a slate, written words, a reading, or an inscription.

The inherited source is `jorin-note` (`sources.json` `/5` in the r72 clone); the Jorin claim is `entities.json` `/7/claims/0`, citing that source. The claim paraphrases Jorin's self-identification as registrar, sighting of Vela on the east steps during what he called Bell-7, and his not seeing who struck a bell. The inherited timeline includes `jorin-vela-sighting` at tick 3, but that event is only the existing location report; no slate-reading event or time for the inscription is encoded. Tick 3 is not evidence of the time of either slate reading. The Round 72 fixture adds Vela's slate source/claim, but leaves the inherited Jorin prose and claim unchanged.

## Can the readings be compared?

Only in a narrow, text-level sense once a new Jorin account actually supplies its reported wording: Vela's extant report says she could read **“KEEP THE EAST GATE CLEAR.”** A Jorin report that says he read different words would be a discrepancy between the wording attributed to the two reports. The present inherited Jorin account offers no second wording, so it cannot itself be compared to Vela's inscription text.

Even if a new Jorin report gives different words, the two accounts cannot be treated as readings of the **same slate/inscription at the same time** on current evidence. Neither current source identifies a shared slate, says when its reading occurred, or says whether the inscription changed or remained visible. Jorin's Bell-7 statement concerns when he says he saw Vela on the east steps, not when he read a slate; Vela's slate excerpt supplies no Bell-7/date linkage. The matching east-steps setting in Jorin's sighting does not show that he witnessed Vela reading, or that his own hypothetical reading happened during that sighting. No shared time, artifact identity, persistence, direct contradiction, or correction follows from different reported wording alone. A bounded comparison should preserve both attributed accounts and leave identity/time/source unresolved; it should not claim Jorin witnessed Vela's reading.

## Checker and evidence limits

`check_bible.py` validates the five JSON tables, including nonempty entity claim statements and resolvable source IDs; it does not parse Markdown excerpts/maps, compare prose, establish clause support, or determine whether two sources describe the same object or occasion. The Round 72 reports likewise distinguish structural cleanliness and literal map checks from source truth. Exact prose comparison and any new source-to-claim/map alignment require manual review against the eventual candidate.

**Finding:** r72 supplies one explicit Vela-attributed slate wording; inherited Jorin supplies no slate wording. A future different Jorin-reported wording can be compared as two reports' text, but not as two readings of one identified inscription at one shared time. No inference here about source truth, canon, rights, or game mechanics.
