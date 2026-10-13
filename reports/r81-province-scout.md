# Round 81 province scout — Git attribution scope

## Assessment

The reusable Git role/identity control proposed in the Round 81 LOG belongs primarily to **fleet coordination**, not to lore corpus knowledge. A pre-commit role decision table, Git author/committer preflight, and rules about which worker may commit or push are operational controls for the shared agent/worktree fleet. They do not describe fictional-world records, source methods, or lore-checker behavior—the province's stated ownership in `.shokunin/lore/PROVINCE.md`.

There is a legitimate lore-facing concern, but it is narrower: lore reports should accurately distinguish a commit's recorded Git identity from the person/session that operated it, and distinguish a locally observed commit from an unverified remote-push report. That is evidence/provenance hygiene for incident reporting, not a reason to make the operational policy lore-corpus knowledge. The incident can remain disclosed in lore LOG/reports because it affected a lore round; its reusable prevention/control should be owned by fleet coordination (or the shared parent policy owner), with lore consuming that control rather than duplicating it.

## Evidence examined

- `.shokunin/lore/LOG.md`, Round 81 declaration: baseline incident is the r80 report-only verifier commit `3e2b28bf742f1e022fd9942c309cba38b3761aef` under inherited games-engine-mechanics identity; parent verified local author but not remote receipt. It explicitly makes the proposed artifact a pre-commit/role decision table under lore corpus knowledge.
- The same LOG's Round 80 closure: verifier violated no-commit/no-push instructions; remote push is reported, not independently verified; retain incident disclosure and do not rewrite history or force-push.
- `.shokunin/lore/PROVINCE.md`: lore owns fictional-world records, consistency verification and sourced inspiration; it refuses game-mechanics verification and writes only under `.shokunin/lore/**` and own reports.
- `.shokunin/lore/reports/r80-independent-verifier.md` and `r80-axis-adjudicator.md`: provide bounded evidence and explicitly separate structural checks from source authenticity, fiction truth/canon, rights, mechanics, and editorial merit. The adjudicator treats the identity/push event as conformance telemetry, not an axis gain.
- `.shokunin/lore/reports/r81-incident-scout.md`: confirms the local commit object's recorded author and committer identity/path; explicitly notes this does not identify the physical operator or establish remote receipt.

## Boundary and recommendation

Recommend **scope conflict / reroute**: do not add a reusable Git identity/role-enforcement procedure to the lore corpus on the evidence presently available. Route that control to fleet coordination, which can own cross-province permissions and preflight behavior. Keep lore's incident record precise and local: recorded author/committer, observed or reported action, and verification limits must not be collapsed into claims about who acted or whether a remote accepted a push. A lore-specific note would be justified only if it teaches a distinct, evidence-backed lore attribution rule that is not merely a duplicate of fleet policy.

This is a scope assessment, not a finding about source authenticity, fictional truth/canon, rights, or mechanics. I did not independently query Git or the remote; the incident metadata and remote-status limits above are based on the cited round records/reports. No corpus, LOG, checker, Git configuration, commit, push, or merge was changed. Only this report is written.
