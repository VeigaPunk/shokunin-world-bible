# Round 81 verification scout — non-mutating preflight tests

## Evidence inspected

- Round 81 LOG declaration specifies an identity preflight that must distinguish inherited FAIL from explicit lore-identity PASS, and a role gate that keeps report-only workers from committing or pushing.
- Round 80 incident evidence in `r80-independent-verifier.md` records a report-only worker committing as `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>` and reporting a push to `lore`. The LOG says the local commit identity was confirmed, but remote receipt was not independently verified. This is evidence of the reported conformance incident, not proof of remote delivery.
- Read-only probes in this checkout:
  - `git var GIT_AUTHOR_IDENT` → `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local> ...`
  - `git var GIT_COMMITTER_IDENT` → same identity.
  - `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local var GIT_AUTHOR_IDENT` → `lore-shokunin <lore@shokunin.local> ...`
  - Same explicit `-c` options with `GIT_COMMITTER_IDENT` → lore identity.
  - `git config --show-origin --get-all user.name` and `user.email` show the conflicting repository-level identity in `/home/vgpnk/Projects/prymeagnt/.git/config`; the inherited user config is `ci` / `ci@local`. I did not alter any config.
- At inspection, `git status --short --branch` showed branch `craft/lore-r1` and pre-existing `M .shokunin/lore/LOG.md`. It was already modified; this report does not attribute or alter that change.

## Safe test plan

Use read-only identity probes as the positive/negative test inputs; do not test by making a commit or push. A future preflight can accept an explicit identity string and role, and return a decision without invoking Git mutation commands.

1. **Inherited identity must FAIL for an authorized lore commit:** capture the result of `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` without `-c`. Compare both names/emails to the exact expected `lore-shokunin <lore@shokunin.local>`. In this checkout both currently mismatch, so the expected gate result is `FAIL / DO NOT COMMIT`. This validates the negative branch using the observed inherited identity.
2. **Explicit identity must PASS the identity check only:** repeat both probes with `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local ...`. Both returned identities currently match; expected result is `PASS identity`. This does not authorize this report-only worker to commit.
3. **Role decision must be independent of identity:** feed role `report-only` with either identity result; expected action is `DO NOT COMMIT OR PUSH`. Feed `authorized parent commit` plus matching explicit author and committer identities; expected action may be `COMMIT ONLY IF OTHERWISE AUTHORIZED`, still no push. Mismatched identities always fail closed. Keep this decision logic pure/read-only (e.g. unit assertions against a function or table); do not implement it here.
4. **Assert non-mutation:** run only `git var`, `git config --show-origin --get-all`, and status probes for this validation. Do not invoke `git commit`, `git push`, `git config` writes, checkout/reset, or merge. If a future gate is executable, test it with stubs/mocks that fail if it invokes mutation commands, or isolated temporary test inputs outside the repository; inspect status before and after and ensure this test writes no project files.

Suggested assertions: (a) inherited identity → FAIL; (b) both explicit identities exact → PASS identity; (c) report-only role → DO-NOT-COMMIT/PUSH even after identity PASS; (d) no decision output claims a push receipt; (e) validation leaves repository state untouched by the test. Test author and committer separately; passing just one is insufficient. Do not infer status based on a substring when exact identity is required.

## Limits

These are proposals for testing a preflight, not validation of a preflight implementation: no such code was exercised here. The identity probes establish the current Git-resolved identities only. `git var` does not prove what a later command, alternate environment, `--author`, hook, wrapper, or remote would do. `-c` demonstrates a command-scoped identity override; it does not change repo config, validate all commit metadata, or make a report-only role authorized. A status snapshot is not a complete audit of concurrent activity. No commit/push was attempted; no remote receipt was tested. No source authenticity, canon, fictional-world truth, rights, or mechanics inference is made.

Only this report was written. No LOG, corpus, checker, or Git configuration was edited; no commit, push, merge, or spawn was performed.
