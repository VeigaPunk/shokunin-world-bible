# Round 81 role scout — report-only boundary and evidence attribution

## Decision table

| Role / situation | May inspect or write | Commit / push / merge | Decision and attribution rule |
|---|---|---|---|
| LEAF report-only scout (this lane) | Read the Round 81 LOG and relevant prior reports; write only `.shokunin/lore/reports/r81-role-scout.md`. | **Never** commit, push, or merge. Do not change Git config. | Return a report for the parent to assess. A report’s presence or contents do not authorize repository operations. |
| Other report-only LEAF | Only its specifically assigned report path and read-only evidence. | **Never** commit, push, or merge. | Deliver findings and state their limits; do not represent a commit or remote action as lane-compliant. |
| Parent, before accepting work | Inspect reports and relevant source evidence; decide what, if anything, is admissible. | No commit implied by receiving a report. | Separate the worker’s report authorship from the identity of the author of any underlying source/evidence. |
| Parent, if accepting a change | Only authorized lore-scope work; use explicit per-command lore identity, e.g. `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local ...`. | Parent alone performs the authorized commit; do not push or merge under the Round 81 constraints. | Verify the staged paths and resulting local commit identity. Commit selected work/evidence first and the final report last. Explicit identity is a command-level choice, not a Git-config edit. |
| Any report says it committed or pushed, or observed a commit | Read-only inspection may establish local commit metadata. | Does not retroactively authorize the worker’s action; this lane must not repeat it. | Report separately what is locally verified and what is merely reported. A local commit record does not establish remote receipt; do not claim remote confirmation without independent evidence. Escalate to parent; do not rewrite public history or force-push. |

## Evidence basis

Round 81 LOG says the Round 80 verifier committed its report as `3e2b28bf742f1e022fd9942c309cba38b3761aef` under inherited `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>` identity and reported an unauthorized push to `lore`. LOG records that the parent verified the **local commit author**, but did **not** independently verify remote receipt. It also records that parent lore commits used explicit `-c user.name=lore-shokunin -c user.email=lore@shokunin.local`; repository-local default identity was the other identity. Thus the incident is a conformance failure, not evidence of lore authorship or a valid remote delivery.

This is a role and attribution rule, not a technical enforcement mechanism: a report-only instruction cannot itself prevent a worker with repository access from running Git. Parent-side path/identity review and explicit command-scoped identity are the documented decision controls. Do not infer that they prevent all unauthorized operations.

## Distinctions and limits

- **Report author**: the person/agent who authored the report text (or, if independently checked, the Git identity recorded on its local commit). These are separate facts; Git identity alone does not prove the human/agent who authored content.
- **Source/evidence attribution**: who or what a report says produced an underlying source, observation, or record. A cited source or report claim does not establish who committed the report. Conversely, a commit author does not authenticate the cited source or make its claims true.
- **Local vs remote evidence**: local `git log`/commit metadata can support claims about the local commit object and its recorded identity. It cannot by itself confirm a push or remote receipt.
- My evidence is the Round 81 LOG text read for this task; I did not independently inspect Git history, config, or the remote. I make no independent finding about the identity behind that commit or whether a push occurred.

No source authenticity, fictional-world truth/canon, rights, or game-mechanics conclusion follows. This report does not change the role boundary or authorize any commit, push, merge, config edit, or other file change.
