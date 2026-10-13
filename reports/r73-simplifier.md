# Round 73 simplifier — Jorin’s slate-reading report

## Minimal proposal

Keep the move to one newly authored, fictional, first-person Jorin account, one new source row, and one appended claim on the existing `jorin` entity. A compact excerpt could be:

> I, Jorin, read “KEEP THE EAST GATE OPEN” on a slate at the east steps.

This is a proposed report, not an assertion that a slate or inscription existed. Its wording differs from Vela’s account, which says she could read “KEEP THE EAST GATE CLEAR” on a slate (`corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md`). Preserve the attribution in the single claim, e.g. “Jorin reports reading ‘KEEP THE EAST GATE OPEN’ on a slate at the east steps.” Cite only the new fictional source. Do not add a timeline event, tick, relation, dependency, or contradiction row; do not claim Jorin watched Vela read, or that either account corroborates the other.

A short editorial comparison note can say: “Vela reports ‘KEEP THE EAST GATE CLEAR’; Jorin reports ‘KEEP THE EAST GATE OPEN.’ The reported wording differs. The accounts do not establish whether they concern the same slate or inscription, or when either reading occurred; those questions remain open.” Treat this as a comparison of reports, not a finding that one inscription changed, that both readers saw one object, or that either report is false. The shared east-steps reference is not evidence of shared time or object.

## Evidence and limits

The Round 73 declaration calls for a new source and cited Jorin claim in an r72 five-table clone, with no new timeline event, shared-time claim, or automatic contradiction (`.shokunin/lore/LOG.md`, “Round 73 — 2026-10-13T08:24:52.862998+00:00”). In the inherited Jorin excerpt, he says he stood at the registry doorway, saw Vela on the east steps during what he called Bell-7, and did not see who struck a bell; he says nothing about reading slate text (`corpus/fixtures/r72-vela-slate-claim/jorin-note-excerpt.md`). Its clause map explicitly says the matching Bell-7 labels do not establish a shared occasion or chronology (`jorin-clause-map.md`). Vela’s slate excerpt supplies the other reported wording, but neither it nor its map authenticates the slate, inscription, or writer (`vela-slate-note-excerpt.md`; `vela-slate-clause-map.md`).

The checker validates table shape and cited source resolution; it does not compare source prose, verify a clause map, or decide whether accounts refer to one object or occasion (`corpus/fixtures/check_bible.py`). Thus a clean checker result would not establish the proposed words as fact or make the difference a direct contradiction. The proposal is not an implementation or verification result. Non-author review should reject it if the wording difference reads as arbitrary decoration, the text implies a shared inscription/time, or the comparison silently resolves identity or reliability. Depth, coverage, and calibration should be judged separately; no source-truth, canon, rights, or game-mechanics inference follows.

Scope: this report only. No other files, fixtures, or checker changes; no commit, push, or merge.
