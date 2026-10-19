# Round 103 dispatch receipt — lore (L1 W2RoundLore, 2026-10-19)

Counts below are computed from this table (Q08), not typed. Every seat is a leaf; no seat committed. Models were assigned by the session route table by role; none was passed.

| # | seat id (W2RoundLore.*) | role | dispatch | status | output |
|---|---|---|---|---|---|
| 1 | R103Planner | planner | batch 1 | completed | seats/R103Planner.md (persisted by L1) |
| 2 | R103Connector | connector | batch 1 | completed | seats/R103Connector.md (persisted by L1) |
| 3 | R103Scout | scout | batch 1 | completed | seats/R103Scout.md (persisted by L1) |
| 4 | R103Scribe | scribe | batch 1 | completed | seats/R103Scribe-before-receipt.md |
| 5 | R103Sources | executor | batch 1 | failed — provider `resource_exhausted` after 30m16s, no file written | none |
| 6 | R103Quality | executor | batch 1 | completed | corpus/QUALITY.md, corpus/lessons/round-103.md (## Mistakes) |
| 7 | R103EntryAliases | executor | batch 1 | completed | rejected/r103-aliases-and-name-variants.md (moved from corpus/knowledge/ after the Q06 reject), seats/R103EntryAliases-rows.md |
| 8 | R103EntryDating | executor | batch 1 | completed | corpus/knowledge/r103-in-world-dating-and-uncertain-time.md, seats/R103EntryDating-rows.md |
| 9 | R103EntryCanon | executor | batch 1 | completed | corpus/knowledge/r103-canon-status-and-supersession.md, seats/R103EntryCanon-rows.md |
| 10 | R103CoverageMap | executor | batch 1 | completed | corpus/README.md, PROVINCE.md (appended sections) |
| 11 | R103Reviewer | reviewer | batch 1 | completed | seats/R103Reviewer-pre.md (persisted by L1) |
| 12 | R103Critic | critic | batch 1 | completed | seats/R103Critic-pre.md (persisted by L1) |
| 13 | R103SealedA_base | labrat | batch 2 | completed | seats/R103SealedA-baseline.md |
| 14 | R103SealedA_prop | labrat | batch 2 | completed | seats/R103SealedA-proposal.md |
| 15 | R103SealedC_base | labrat | batch 2 | completed | seats/R103SealedC-baseline.md |
| 16 | R103SealedC_prop | labrat | batch 2 | completed | seats/R103SealedC-proposal.md |
| 17 | R103SealedE_base | labrat | batch 2 | completed | seats/R103SealedE-baseline.md |
| 18 | R103SealedE_prop | labrat | batch 2 | completed | seats/R103SealedE-proposal.md |
| 19 | R103Adjudicator | critic | single | completed | seats/R103Adjudicator.md |
| 20 | R103Sources2 | executor | single (re-dispatch of #5) | failed — `turn_rate_limit_exceeded` after 48.5s, no file written | none |
| 21 | R103Sources3 | task (executor function; executor route at capacity) | single (re-dispatch of #5) | completed | corpus/SOURCES.md, seats/R103Sources3-gate.md |
| 22 | R103ReviewerPost | reviewer | batch 3 | completed | seats/R103ReviewerPost.md |
| 23 | R103CriticPost | critic | batch 3 | completed | seats/R103CriticPost.md |
| 24 | R103SourceRecheck | reviewer | batch 3 | completed | seats/R103SourceRecheck.md |

- Seats dispatched: 24 (batch 1 = 12 in one batched call, meeting the ≥8 floor with planner, connector, scout, scribe, 5 executors, reviewer, critic).
- Completed: 22. Failed on provider capacity: 2 (#5, #20), both re-dispatched; #21 delivered the work.
- Roles: planner 1, connector 1, scout 1, scribe 1, executor 7 (incl. 2 failed), task-as-executor 1, labrat 6, reviewer 3, critic 3.
- "Persisted by L1": read-only seats return their result as a message; L1 wrote it verbatim under seats/ with a header comment. Two persisted copies (R103Planner, R103ReviewerPost) had the literal vault-reference scheme string replaced by `[vault-ref-scheme]` so the credential sweep prints nothing; no credential was present.
- Writes outside the lane worktree reported by seats: none. Downloads went to mktemp dirs under /var/tmp or /tmp, outside every repository.
