## Work performed

- Axes: **over-claim containment** (new governance text claims only what receipts support), **misread resistance** (the R9 receipt boundary cannot be read as checker capability; the manual gate cannot be read as optional), **text integrity / landing fidelity** (labels and section scoping of the new R8/R9 block and the check-log entry).
- Swept the three new governance surfaces at the committed tree `c4d4823` (clean): `corpus/knowledge/r88-sourced-inspiration-decision-table.md` R8 failed-gate paragraph (line 40) and the R9 Manual-gate / Required-record / Receipt-boundary / Worked-example block (lines 42-48); `corpus/knowledge/r91-c9-watch.md` check-log entry (lines 45-206); plus the support-command strings the text cites (`corpus/tools/support_check.py`) and the mutation recipe the check-log cites (`.ufo/waves/round-90/patches/C9-rerun-probes.sh`).
- Compared the landed text against the seat proposals to attribute defects: E1/E2 copy-ready wording (`patches/E1-edges.md`, `patches/E2-wording.md`), E3's consolidated patch (`patches/E3-c3-wording.patch`) with C5's critique, and X1/X2 patches (`patches/X1-recheck.patch`, `patches/X2-note.patch`). F1 is a composition artifact of the label replacement; F2/F4 come from integrating X1+X2 instead of E3's consolidated patch; F3 is X1's caption, which C5/E3 had already corrected.
- Two dependency wait-checks (default): both artifacts were present immediately; receipts below. Scratch under `/tmp` was two diff captures, removed after use. Repo writes: this report and `JCAL4-receipts.json` only. No commit, no push.

## Before → after measurements

All "after" rows from the committed tree at `c4d4823` (tree clean, `git status --short` empty). "Before" is `396c568` (r91 closure).

**B1. R8 label duplication (new).** Command:

```sh
cd lore-shokunin && f=corpus/knowledge/r88-sourced-inspiration-decision-table.md
grep -o 'Failed-gate disposition (clarified r92)' "$f" | wc -l
git show 396c568:"$f" | grep -o 'Failed-gate disposition' | wc -l
sed -n '40p' "$f" | head -c 110
```

```text
2
1
**Failed-gate disposition (clarified r92):** **Failed-gate disposition (clarified r92):** **Owner:** the lore 
```

E1/E2's replacement text carries the label once (`patches/E1-edges.md:11`, `patches/E2-wording.md:11`).

**B2. R9 block section scoping (new).** Command and output:

```sh
grep -n '^### \|^\*\*Manual R9 gate\|^\*\*Required record\|^\*\*Receipt boundary\|^\*\*Worked example' "$f"
```

```text
28:### R8 appendix — plausible but unrecorded influence (decided r90)
42:**Manual R9 gate (required for translation-backed R5 claims):** ...
44:**Required record:** ...
46:**Receipt boundary:** ...
48:**Worked example:** the submitter maps a line from a privately held 2011 reprint ...
50:### R9 appendix — translator known, source/version unknown (decided r90; reprint boundary clarified r91)
79:**Worked example:** A delivered line from a copy marked "2011 reprint of the 1901 translation"
94:### R10 appendix — matching name/ID, different occasions (decided r90)
```

The entire R9 gate block sits inside the R8 appendix section (after line 28, before the line-50 heading). E1/E2 specify placement "within the R9 appendix, after its existing **Decision** paragraph and before **Worked example**" (`E1-edges.md:19`), i.e. at ~line 78. The R9 appendix's old worked example (line 79) was not replaced; the new worked example landed at line 48, so the file now carries two R9 worked examples under different headings. E1/E2's R8 worked example did not land:

```sh
grep -c 'Kesh Hymn' "$f"; grep -c 'separate per-claim R9 manual-review record' "$f"
```

```text
0
0
```

**B3. Check-log over-claim retained (P4 caption).** Command and output:

```sh
grep -n 'paired resolved-holder control' corpus/knowledge/r91-c9-watch.md
grep -c 'near-control' corpus/knowledge/r91-c9-watch.md
```

```text
140:**P4 — unrelated duplicate does not qualify the tick inversion (paired resolved-holder control)**
0
```

The committed mutation recipe (`.ufo/waves/round-90/patches/C9-rerun-probes.sh:36-38`) defines P2 = `tick-relevant-unresolved` `((3, None, 'f3-dup'), (1, 'f3-dup', 'harbor'))` and P4 = `unrelated-duplicate-tick` `((3, None, 'mira'), (1, 'mira', 'mira'))`; applying both to `corpus/fixtures/r89-fn2-unresolved-chain-break/entities.json` and diffing:

```text
P2 provenance[0]: {'tick': 3, 'from_holder': None, 'to_holder': 'f3-dup', 'source_id': 'courier-log'}
P4 provenance[0]: {'tick': 3, 'from_holder': None, 'to_holder': 'mira', 'source_id': 'courier-log'}
P2 provenance[1]: {'tick': 1, 'from_holder': 'f3-dup', 'to_holder': 'harbor', 'source_id': 'archive-ledger'}
P4 provenance[1]: {'tick': 1, 'from_holder': 'mira', 'to_holder': 'mira', 'source_id': 'archive-ledger'}
record0 differing keys: ['to_holder']
record1 differing keys: ['from_holder', 'to_holder']
```

So P2/P4 are not a one-variable pair; C5/E3's "near-control" wording and caveat did not land (`grep -c 'these six probes'` → `0`; `grep -c 'establishes byte identity'` → `0`).

**B4. Check-log receipts reproduce at the committed tree.** Command and output:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
exit=1
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
exit=1
```

Matches the check-log's pasted outputs (watch lines 82-96) exactly; the hash matches the pin (line 6) and the log row (line 49). The r91 side of "retained their r91 distinctions" is corroborated by `.ufo/waves/round-91/C5.md:67` (`Discrimination verified: 4/4`) and the pinned ruling (watch line 7).

**B5. Receipt-boundary strings vs the delivered command.** `support_check.py` emits `RESULT PASS` / `RESULT PASS WITH WARNINGS` (line 376), `SOURCE-SUPPORT ...` (line 364), `RESULT FAIL` + return 1 (lines 374-375), `RESULT ERROR` + return 2 (lines 396-397, 406-407, 415-416). Live checks:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "rc=$?"
```

```text
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
...
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
rc=0
```

```sh
python3 corpus/tools/support_check.py corpus/fixtures/does-not-exist; echo "rc=$?"
```

```text
FAIL: cluster directory not found: corpus/fixtures/does-not-exist
RESULT ERROR
rc=2
```

No WARN lines from the r88-m3 run, so the README's "close its unreferenced-declaration warning" claim holds against the delivered command.

**B6. Census convention reproduces.** The check-log/README advice says repo-relative argv; B1's tuple stores `stdout_sha256`. Command and output:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r5-missing-file | sha256sum
python3 corpus/fixtures/check_bible.py "$PWD/corpus/fixtures/r5-missing-file" | sha256sum
```

```text
430d8efb9e124261fbfadb4a2b2a7295bcb9385316e994c012c2f03e3dbf8755  -
7a81d5020245c2e6c95b53b8ef6a1ed41e96ea9da638cd57d3226c673a18026b  -
```

B1's recorded `stdout_sha256` for that key is `430d8efb...` (match, repo-relative); the absolute invocation changes the hash exactly as the text warns. All five named fixtures are B1 keys (166 total).

**B7. Dependency wait-checks.**

```sh
bash .ufo/waves/poll_wait.sh .ufo/waves/round-92/followup/SF1-freeze.json 120
bash .ufo/waves/poll_wait.sh .ufo/waves/round-92/followup/SF1.md 120
```

```text
POLL_HIT path=.ufo/waves/round-92/followup/SF1-freeze.json elapsed=0s checks=0
POLL_HIT path=.ufo/waves/round-92/followup/SF1.md elapsed=0s checks=0
```

## Findings & named debt

**Axis verdicts (committed tree only; no trade counts as an improvement):**

- **Over-claim containment — improved, bounded; not clean.** The R8 whole-element hold and the R9 receipt boundary are explicitly bounded (the hold is stated as not proving source use and not establishing R1; the lexical receipt is stated as necessary-not-sufficient). Residual over-claim: **F3** (P4 caption, below); minor under-enumeration: **F6**.
- **Misread resistance — improved, bounded; not clean.** The R9 receipt-boundary's operative sentences (1-4) cannot be read as checker capability: they name the command, list what it checks, deny translation-version/printing/bibliographic/fidelity/manual-outcome establishment, and require the separate per-claim manual record — answering the seat's specific test affirmatively. One closing sentence is referent-ambiguous (**F5**); its error direction is safe (it denies capability), so it is an accuracy/clarity defect, not a capability over-claim.
- **Text integrity / landing fidelity — harmed (bounded).** **F1** (doubled label) and **F2** (R9 block under the R8 heading; R8 worked example and R9 evidence-cell append absent; old R9 worked example unreplaced) are defects on the face of the new text. E1/E2's proposal (`E1-edges.md:15,31`; `E2-wording.md`) and E3's consolidation (`E3-c3-wording.patch`) show the intended shape; the committed text deviates.

**F1 — doubled label (defect, cosmetic).** `r88-sourced-inspiration-decision-table.md:40` carries `**Failed-gate disposition (clarified r92):**` twice. Repair: delete one instance.

**F2 — R9 block mispositioned / proposal pieces missing (defect, scope).** Lines 42-48 (Manual R9 gate, Required record, Receipt boundary, new Worked example) sit inside the R8 appendix section; `### R9 appendix` (line 50) contains none of the mandatory-gate text, and a reader navigating to that heading will miss it. The old worked example (line 79) remains alongside the new one. E1/E2's R8 worked example and the R9 evidence-cell append (`separate per-claim R9 manual-review record`) did not land. Repair: move lines 42-48 after the R9 appendix's Decision paragraph (~line 78), merge/replace the two R9 worked examples, and either land the two missing pieces or record the omission as a deliberate scope cut in the landing record.

**F3 — retained over-claim: "paired resolved-holder control" (defect, precision).** Watch line 140; evidence B3 shows the P2/P4 pair differs in more than the holder-resolution variable. C5's critique and E3's correction (`near-control`, plus the two-field caveat and the "exit 1 alone is not a C9 discriminator" sentence) were not integrated. Repair: retitle to "resolved-holder near-control" and paste E3's caveat sentence.

**F4 — scope sentences absent (defect, low).** The check-log table row (line 49) lacks E3's probe-scope bound ("these six probes" / byte identity ≠ semantic coverage). The row already scopes to "all four C5 scenarios", so the over-read risk is reduced, not eliminated. Repair: adopt E3's scope sentence.

**F5 — receipt-boundary closing sentence referent ambiguity (defect, low-medium).** Decision-table line 46, last sentence: "The existing verification command checks wording completeness only and cannot perform this review." The only in-file "Verification command" is the R9 appendix's textual-completeness scan at line 88 (it checks `.ufo/waves/round-91/patches/D2-edges.patch` for key presence; that path exists and is tracked). But the paragraph's own antecedent ("that command" = `support_check.py`) invites the other reading, under which "checks wording completeness only" contradicts the paragraph's preceding "map/inventory/mode/anchor checks" enumeration and understates the command. Because the block is mispositioned (F2), the intended referent is a section away. Cross-reference: JDEP4's carried debt D-JDEP2r91-4 records that this command still reads `.ufo/waves/round-91/patches/D2-edges.patch` rather than the delivered r92 text; whichever referent is intended, the closing sentence points at a stale-input scan, strengthening the case for naming it explicitly or dropping it. Repair: name it ("The R9 appendix's textual-completeness command ...") or relocate the sentence into the R9 appendix, adjacent to line 88.

**F6 — span checks not enumerated (nit).** Line 46 says the receipt reports "map/inventory/mode/anchor checks"; the command also fails rows on declared-line-span validity and outside-span hits (`support_check.py:283-294, 336-347, 350-351`). Under-claim direction only; optional polish.

**Named debt (unrepaired in the committed tree):** F1, F2, F3, F4, F5, F6. All are textual; none touches checker behavior, and none of the receipts the round relies on is fabricated or misattributed.

**Limits.** This seat did not re-audit the boundary document (C1's certified surface; its grep shows no R8/R9 governance text) nor re-verify C2's Spence-row receipts beyond the support run above. The E3 patch was evaluated read-only as patch text; post-hoc applicability to the committed tree was not tested (moot once repairs are made). Four of the five missing-file fixtures were shown echoing the repo-relative argv path; the fifth (`r5-missing-file`) additionally had its recorded B1 hash reproduced exactly.

## Handoff

- Deliverables: this report and `.ufo/waves/round-92/followup/JCAL4-receipts.json` (machine-readable receipts for B1-B7).
- For the parent: the governance substance of C1's R8/R9 edges and the C3 check-log row 1 is verified sound and receipt-reproducible; the six defects above are textual repairs, ordered F1 (one line) → F2 (block move + two-piece landing decision) → F3/F4 (adopt E3 wording) → F5 (one sentence) → F6 (optional). Re-verify after repair with the B1/B2/B3 greps and the B4 durable pair.
- If the parent prefers minimal-touch repair: F1 + F5 are single-line edits; F2's block move is the only structural change and should be paired with the F3/F4 wording adoption from `E3-c3-wording.patch`.
- Cross-seat notes: JCOV2 independently confirmed F1 (same doubled header; single occurrence in both E1/E2 source patches) — two seats found it, it is not a misread. JDEP4's content-level gaps (R8 reviewer independence, D-JDEP4r92-1; R9 lapsed access, D-JDEP4r92-3) are adjacent but non-overlapping with this seat's wording defects. JCAL3 independently confirmed the census guidance my B6 reproduces (`430d8efb…`). F5 carries the D-JDEP2r91-4 cross-reference above.