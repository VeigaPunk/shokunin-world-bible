# Round 72 simplifier — Vela reading, without an event

## Minimal candidate

Proposed newly authored fictional excerpt:

> I, Vela, read “KEEP THE EAST GATE CLEAR” on the slate. The cramped letters made me think the writer might have been in a hurry; I did not see who wrote them.

Add one fictional, unverified source row (for example, `vela-slate-note`) and append exactly one claim to existing `vela` in `entities.json`, citing that source:

> Vela reports reading “KEEP THE EAST GATE CLEAR” on a slate and taking its cramped letters as a possible sign that the writer was in a hurry; she did not see who wrote it.

The quotation is Vela’s reported observation; haste is explicitly her tentative inference, not a fact about the writer. “I, Vela” attributes the account to the fixture’s existing character ID, not independently authenticates identity. The claim reports what she says she read; it does not establish that a slate or inscription objectively existed, where or when it existed, or who wrote it. Keep the claim in the existing character entity, cite only the new source, and add no event, relation, dependency, or contradiction. No timeline position is supplied or implied.

## Why this is the smallest plausible depth move

The baseline explicitly seeks a separately authored first-person reading/inference account represented by a source and one cited Vela entity claim, with no timeline event (`.shokunin/lore/LOG.md`, “Round 72”). The r43 fixture already gives Vela an attributed hearing/non-sighting claim and a separate excerpt, while Jorin reports seeing Vela on the east steps (`.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/vela-note-excerpt.md`; `entities.json`, `vela` and `jorin` claims; `jorin-note-excerpt.md`). The proposed report adds a distinct, bounded perspective—reading words and interpreting their appearance—rather than another witness or corroboration. The existing clause map warns that east steps map only broadly to `harbor`, not to a registry desk (`vela-clause-map.md`); therefore this proposal does not locate the slate at either place.

Round 71’s simplifier proposed similar slate-reading prose plus an event. Its reviewer/adjudicator found narrow depth potential but rejected that candidate because tick 4 encoded unsupported succession; the quotation-map mismatch was also noted (`reports/r71-simplifier.md`; `LOG.md`, “Round 71 — closed”). This proposal removes the event and all shared-timeline placement, addressing that specific calibration failure, but does not itself prove depth. Its similar wording also risks feeling like a recycled decorative beat; a non-author reviewer should decide whether the observation/inference distinction materially deepens Vela rather than merely adding color.

## Evidence limits and falsifier

Map the excerpt’s exact quoted words and tentative inference to the single new claim and its source; verify that only the source and Vela claim are appended and inherited r43 rows remain unchanged. Reject if the claim turns the reading into objective slate/inscription fact, turns haste into fact, implies knowledge of the writer, introduces unsupported location or chronology, or fails to provide meaningful character perspective. Judge depth, coverage, and calibration separately; no scalar score.

The fixture checker (`.shokunin/lore/corpus/fixtures/check_bible.py`) validates schema, citations, relations, and timeline structure; a clean result cannot establish source-text support, meaningful depth, truth, chronology, canon, rights, or game mechanics. The baseline separately requires preserving the old 130 fixture raw CLI tuples; this report has not run that regression check. This is a recommendation, not an implementation or verification result.

Scope: report only. No fixture, checker, README, or LOG edits; no commits, push, or merge.
