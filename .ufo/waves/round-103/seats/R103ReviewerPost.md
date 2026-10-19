<!-- L1 note: the literal vault-reference scheme string was replaced by [vault-ref-scheme] in this persisted copy so the credential sweep prints nothing; no credential was present. -->
# R103 post-landing falsification review (reviewer seat)

Scope: lane worktree `kaika/round` (base 6cec83a), uncommitted tree. Read-only; no commits; no gate run with `--freeze`. Commands run from the lane root.

## Checks

| # | Check | Command | Observed | Verdict |
|---|---|---|---|---|
| 1a | C1–C3 measurement, tree | `bash .ufo/waves/round-103/measure.sh` | CM rows 19; governed CM-a..g 2 (CM-c, CM-e); coverage-row knowledge entries 2; Frontier rows 5; PROVINCE Core/Frontier/Adjacent 3; Q rows 10 (10 cite a lesson); M rows 10 (10 captured-by Q##); Gate Admitted+Rejected headings 2; SOURCES rows 31; admitted r103 entries with all sources mined and naming the entry 2/2 | PASS (matches declared claims) |
| 1b | Same, before | `bash .ufo/waves/round-103/measure.sh 6cec83a` | all counters 0 | PASS |
| 1c | SOURCES census (contract lines 68–80) | the seven census commands, lane root | rows 31; malformed 0; tiers A=23 B=3 C=5; status mined=16 queued=12 rejected=3; duplicate ids none; enum/tier-inflation none; missing mined used-by paths none | PASS |
| 2 | path:line citations in both entries, QUALITY.md, lessons, README coverage/Frontier, PROVINCE section, SKILL rows | resolved each token against the tree and printed the cited lines (≈90 distinct tokens; all line-anchored entry cites included) | all resolve; check_bible cites (29, 2, 26, 31, 118, 119–150, 146–150, 156–161, 259–262, 323–326, 384–392, 393–395, 396–411, 412–414, 426, 428, 79–83) say what the claim says; LOG/SCORECARD cites resolve; defects D2, D5, D8 below | PASS with defects |
| 3a | S### cited anywhere exist and match | every S### in SOURCES, entries, lessons, README, PROVINCE, SKILL, QUALITY | S001–S031 all present; body IDs in entries (S020–S027) are in each header and in used-by; S012 and S009 Frontier citations checked against rows | PASS, except D5 |
| 3b | Gate records S001–S031, quote ≤25 words | parsed `## Gate` | 31 records; longest quote 25 words | PASS |
| 3c | Gate quotes vs live sources (28 pages fetched to /var/tmp, tags stripped, normalized, grepped) | curl + python grep | verbatim: S001, S002, S003, S004, S006, S007, S008, S009, S011, S012, S013, S014, S015, S016, S017, S020, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031; S005 checked as prefix only; S010 NOT verbatim (D3); S021 unverifiable (loc.gov 403; Wayback fetch returned binary) | PARTIAL, D3 |
| 4a | No prior tracked line modified except SHONEN and SKILL insertion | `git diff 6cec83a -- . ':!.ufo'` plus `^-` grep | PROVINCE +23/−0; corpus/README +47/−0; SKILL +4/−0; SHONEN +4/−4 (only SHONEN removals, all Evidence lines) | PASS |
| 4b | SHONEN seed vs PROTOCOL.md 425–432 | line compare after normalizing marks/name/indent | identical after `[ ]`→`[~]`, `<name>`→`lore-shokunin`, 4-space dedent, and removing the protocol-required `Evidence:` pointer lines | PASS (note: byte-identity holds only modulo Evidence lines) |
| 5 | Gate battery (verify modes, `python3 -B`) | check_bible r100-docket-review; support_check r87-myth-cluster; map_obligations r100-docket-review; dependency_freeze ×8 (r88, r94–r100); discriminate_check; boundary_doc_check; boundary_doc_check --self-test | check_bible exit 0 CLEAN; support_check exit 0 RESULT PASS (14/14); map_obligations exit 0 PASS (24/24); dependency_freeze ×8 exit 0 PASS, events/edges r88 2/2 0/0, r94 3/3 2/2, r95 4/4 3/3, r96 5/5 4/4, r97 6/6 5/5, r98 7/7 6/6, r99 8/8 7/7, r100 9/9 8/8; discriminate_check exit 0 HELD; boundary_doc_check exit 0 CERTIFIED; self-test exit 0 PASS. corpus/tools and corpus/fixtures have no diff vs 6cec83a | PASS |
| 6a | Credential sweep, tracked diff | `git diff 6cec83a \| grep -nE '<pattern>'` | no output | PASS |
| 6b | Credential sweep, untracked files | same pattern over `git ls-files -o --exclude-standard` | `.ufo/waves/round-103/seats/R103Planner.md:34` and `:76` (literal `[vault-ref-scheme]` in a planning receipt; no credential) | FAIL (benign), D1 |
| 6c | Q09 sweep on new entries | `grep -e '[-]scratch/' -e '[.]shokunin/' -e '/home/' -e '/tmp/'` | none in both entries | PASS (QUALITY/lessons trip it, D9) |
| 7 | README CM verify commands | run each as written | CM-01 exit 0; CM-02 exit 1; CM-04 exit 1; CM-06 exit 1; CM-05 match 1; CM-07 6 hits; CM-09 9 hits; CM-12 3 hits; CM-a exit 1; CM-c/CM-e 1 hit each; CM-f exit 1; CM-g exit 1 | PASS |
| 8 | Known-gaps numbers | K16 pipeline; debt-ledger JSON | 24 dead seat-scratch pointers; ledger 264 items, 361 source entries, 45 carried | PASS |
| 9 | Knowledge-header debt | `head -n3` over 24 tracked notes | missing source: 13; verified-at: 13; recheck: 14 (any-missing 14 matches lesson M10) | FAIL, D4 |

## Defects (severity order)

1. **D1 FAIL (gate)** `.ufo/waves/round-103/seats/R103Planner.md:34,76` — literal `[vault-ref-scheme]` pattern in an untracked receipt trips the mandatory credential sweep (benign). Fix: write the pattern without the literal (split it or name it "1Password reference"), then re-run the sweep to empty output.
2. **D2 quote not verbatim** `corpus/knowledge/r103-in-world-dating-and-uncertain-time.md:7` — quotes "the checker does not check … competing in-world dating systems"; source `corpus/knowledge/2026-10-12-lore-decision-table.md:17-18` reads "does not yet check aliases, free-text semantic contradictions, source reliability, or competing in-world dating systems". Fix: quote "does not yet check … competing in-world dating systems".
3. **D3 gate quote mismatch** `corpus/lessons/round-103.md:78` (S010) — "fictional story world"; source abstract reads "fictional storyworld". Fix: change to "storyworld".
4. **D4 count mismatch** `corpus/README.md:83` — "12 lack source:, 12 lack verified-at:, 13 lack recheck:"; reproduces as 13/13/14 over the 24 tracked notes. Fix: correct to 13/13/14 or name the window K11/K12 used.
5. **D5 registry/claim mismatch** `corpus/README.md:92` (Frontier row 3) cites S012 for "memory/knowledge contradiction subtypes"; the S012 teaches cell (`corpus/SOURCES.md:20`) does not say it (the source page does mention character memory). S009 (`corpus/SOURCES.md:17`) is temporal-only but is cited for knowledge-state. Fix: add "character memory" to S012's teaches cell; re-justify or drop S009 in that row.
6. **D6 path claim without citation** `corpus/SOURCES.md:47-48` — the in-world-time path starts at S003 and the canon path at S001 and both "feed" their entries; neither entry cites them and S003 (`:11`) and S001 (`:9`) used-by omit the entries. Fix: remove S003/S001 from those paths, or cite them in the entries and add used-by.
7. **D7 stale sweep output** `corpus/knowledge/r103-in-world-dating-and-uncertain-time.md:19` — "Observed output (2 hits, both inert)" holds only for pre-r103 files; the same command now also hits `SKILL.md:27`, `corpus/README.md:69`, `PROVINCE.md:28` and the entry itself. Fix: state the scope or exclude r103 files in the command.
8. **D8 wrong line cite** `corpus/README.md:71` (CM-07) — "manual rows cited at SKILL.md:24,44"; SKILL.md:44 has no r88 reference (hits are 9, 22–26). Fix: "SKILL.md:22-26".
9. **D9 self-violating test** `corpus/QUALITY.md:20` (Q09 test) and `corpus/lessons/round-103.md:19` (M09 quoted dead pointer) match Q09's own grep. Fix: reword the test so the criterion text and quoted dead pointer are exempt, or describe the pattern without the literals.
10. **D10 entry points** `corpus/README.md:90,94` — Frontier rows 1 and 3 name the CM-c dating entry as entry point for reveal-order and knowledge-state work, which it does not address. Fix: point to the row-specific sources only.
11. **D11 nit** `corpus/README.md:52` — "Each `governed by` cell names a real tracked path"; the CM-c and CM-e paths are untracked until commit. Fix: "a real path (tracked after commit)".

## Residual risk and verification gaps

- S021 (EDTF quote) not verified live: loc.gov returned 403; the Wayback fetch returned binary. The lane's own note discloses this.
- S005 checked by prefix only; LOG.md:1500 commit `3e2b28bf…` is not in the local object store, so that pointer is textual only.
- Lesson header "49 CONFIRMED, 2 SHIFTED, 0 WRONG" and SCORECARD:634/667 (M08 ×3) were not re-derived.
- SHONEN passes the seed comparison only with the protocol-required Evidence lines removed.
- Gate battery is unchanged by construction (no diff under corpus/tools or corpus/fixtures), and its outputs were re-observed above.
