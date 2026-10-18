=== EVIDENCE LOG (to be quoted in final report) ===

[baseline]
$ git rev-parse HEAD → ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026
$ git rev-parse 6f86bf2 → 6f86bf26c26abfd76b7f489ad4a5bb447e7cbc5d
$ git merge-base --is-ancestor 6f86bf2 HEAD → exit 0 (baseline_is_ancestor=true)
$ git log --oneline -3 → ebec6bb (r101 declaration), a04f986 (r100 close), 6f86bf2 (r100 freeze)
$ git diff --stat 6f86bf2..HEAD → LOG.md +46, SCORECARD.md +35 (declaration only)

[protected files vs baseline — all SAME]
PROVINCE.md 94a7a77e… SHONEN.md 03b832c7… README.md ad4adb1e… l0-questions.md 93105c95… corpus/fixtures/check_bible.py ff9fd2aa… (cur==base each)

[wave tree at receipt time]
$ git status --porcelain (minus .ufo/.scratch noise):
 M SKILL.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/knowledge/r101-r10-register-first-entry.md
→ tracked modifications are exactly U1's four owned files; U2's file is new; nothing else touched.

[C1 pin presence]
$ python3 -c "json.load(contract)['pins']" → 8 pins incl. new `r100-docket-review`; top-level revision field = ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026 (the disclosed writer-managed refresh).
All ten corpus/fixtures/r100-docket-review/* files sha256-identical to 6f86bf2 (SAME × 10) — pin covers an unchanged fixture.
$ python3 corpus/tools/dependency_freeze.py --help → exit 0.

[C3 case presence]
contract self_test.expected → 19 cases; `repointed_edge` = {"exit": 1, "finding_ids": ["ADDITION-DETECTED","REDUCTION-DETECTED"], "forbid_traceback": true}.
SKILL.md freeze row: "19 cases … r101 added `repointed_edge`, the wrong-but-earlier repointed dependency edge".

[C2 artifact presence]
corpus/knowledge/r101-r10-register-first-entry.md present (20565 bytes, mtime 2026-10-18 00:20 -03:00 = 03:20Z).
Header: "R10 register — first worked entry: an examined NON-conflict at the agreed bell"; record `r101-crossing-agreed-bell-nonconflict-01`; Outcome row: "Examined NON-conflict. Shared referent demonstrated; … the two assertions are COMPATIBLE as stated; no conflict; both claims preserved. No winner, no world-truth assertion, no register entry"; register destination remains uncreated by design.
(Presence-level only; C2 adjudication belongs to verifier seats.)

[poll trajectory — all-reports polls subtract SELF (V25)]
budget 1/2 (poll-1..40, 03:06:15–03:19:16Z): 1→5, exhausted → STALL-ESCAPE-1 (recorded, not fatal)
budget 2/2 (poll-41..80, 03:19:49–03:32:50Z): 5→19, exhausted → STALL-ESCAPE-2 (recorded, not fatal)
budget 3/3 (poll-81..120): final; completion or exhaustion recorded either way.
Excess seat observed from poll ≤80: `V28` (V28-late-bookkeeper.md) — outside declared roster U1,U2,V01–V26 → roster erratum recorded (cf. r100 erratum precedent), report NOT dropped.
