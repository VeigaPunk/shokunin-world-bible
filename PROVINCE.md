# lore province

Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration.

Sources (read-only):
- in-world documents under corpus/ (world bible, once rounds produce it)
- real-world reference works, cited with the art ledger's discipline: attribution, rights, and AI-training permission kept as distinct questions

Refuses: claiming canon without an in-world citation; silently resolving contradictions; real-world rights claims (art-east-asian-design); game mechanics verification (game-dev-2d).

Only writes this standalone lane repository (`lore-shokunin/`), its own fleet round report, and allowed append-only L0 questions. Sibling repositories and domain source trees remain read-only.

## Province map (round 103, 2026-10-19 — appended; earlier text stands)

### Core

- Governed surfaces per corpus/README.md `## Coverage map (round 103, 2026-10-19)`: mechanical checks CM-01 (entity schema+references), CM-02 (relations+reciprocity), CM-03 (timeline ticks/depends_on/inversion/double-booking), CM-04 (contradictions ledger), CM-05 (source-ID resolution), CM-06 (provenance chains), CM-08 (R9 claim→excerpt support), CM-10 (dependency-edge freeze), CM-11 (boundary-document certification); manual gates CM-09 (R10 cross-cluster comparison), CM-12 (real-world reference ledger); plus CM-b free-text semantic contradictions (manual, partial).
- Method coverage admitted this round (Q06 sealed gate): CM-c in-world dating/uncertain time (corpus/knowledge/r103-in-world-dating-and-uncertain-time.md), CM-e canon status/supersession (corpus/knowledge/r103-canon-status-and-supersession.md). CM-a aliases/name variants stays `uncovered`: its r103 candidate was rejected (no decision delta) — corpus/lessons/round-103.md `## Gate`.
- CM-d in-world source reliability stays `partial` (nonempty free-text note only, no grading); CM-f reveal order vs chronology and CM-g kotodama packet intake stay `uncovered`.

### Frontier

- Pointed at corpus/README.md `## Frontier` (round 103): reveal order vs chronology, in-world source reliability grading, character knowledge/memory state over time, continuity-error taxonomy crosswalk vs ConStory-Bench, kotodama packet intake.

### Adjacent

- chousa — research method, not lore canon: `chousa-shokunin/SKILL.md` (exists under the fleet root; lore consumes its evidence per corpus/knowledge/r88-sourced-inspiration-decision-table.md:120-125).
- kotodama — generated-content handoff packets: `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md` (exists; digest unacknowledged by lore — coverage row CM-g). Kotodama also owns name generation (`kotodama-shokunin/corpus/knowledge/linguistics/naming-systems.md`, `.../verification/naming-collision-gate.md`) and calendar/era design (`kotodama-shokunin/corpus/knowledge/culture-material/calendar-festival-systems.md`, `.../culture-material/era-periodization-models.md`); lore owns the names and dates recorded on landed entities and events. Paths are fleet-root-relative.
- game-dev-2d — mechanics verification, refused by this lane: `game-dev-2d-shokunin/` (exists).

### Corrections (dated, addendum only)

- 2026-10-19: the refusal line above names `art-east-asian-design`, a lane absent from the fleet roster — from the fleet root, `grep -c 'art-east-asian' MANIFEST.json` → 0. The rights/permission refusal stands unchanged; only the named owner does not resolve to a lane.
- 2026-10-19: the Sources line "in-world documents under corpus/ (world bible, once rounds produce it)" is stale — fixture bibles now exist: `echo $(( $(find corpus/fixtures -maxdepth 1 -type d | wc -l) - 1 ))` → 174 (K15 census).
