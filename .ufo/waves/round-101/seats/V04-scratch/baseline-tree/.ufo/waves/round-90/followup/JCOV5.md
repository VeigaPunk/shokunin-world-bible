# JCOV5 — Coverage judge #5 (sibling adjacency), round 90 follow-up

Seat scope: read-only check of the round-90 coverage surface (maps, support script, R9 mode
labels) against the chousa and kotodama provinces; rejected-fit reasoning per sibling for the
NEW artifacts; and the K1 cross-reference landing question. Axis judged: **coverage**
(sibling adjacency). Judged tree: `HEAD = ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`
(baseline `e97613c`), tree clean at the wait-check boundaries (untracked sibling follow-up
files only). No sibling file was written; this seat wrote only
`.ufo/waves/round-90/followup/JCOV5.md` and `JCOV5-probes.json`. Scratch and controls under
`/tmp`, removed after each run.

## Work performed

- Ran the mandated two 60-second wait-checks (HEAD, tree state, artifact hashes); both stable,
  so the delivered tree is the judged tree.
- Ran the delivered support command on both clusters and re-measured exit codes via
  `PIPESTATUS`, not `tail`.
- Built four `/tmp` negative controls for the script's claimed semantics: paraphrase
  (retelling-only), verbatim twin, mode mismatch, and out-of-declared-span anchor on a copy of
  r87; plus a substring-edge probe against the anchor class chousa's r4 note documents.
- Freeze-then-verify: applied `X2-c1-nullonly.patch` + `X3-c1-tickonly.patch` to the baseline
  `check_bible.py` in `/tmp` and hash-compared with the delivered file.
- K1 cross-reference landing check across both D1 surfaces: the wave artifact
  `.ufo/waves/round-90/patches/D1-decisions.md` and the governing
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md`; spot-checked K1's cited
  chousa line ranges; `git apply --check` of the K1 patch against the delivered wave file.
- Read the three provinces (`lore-shokunin/PROVINCE.md`, `chousa-shokunin/PROVINCE.md`,
  `kotodama-shokunin/PROVINCE.md` + both sibling `AGENTS.md`) and, for the resolved
  r88-discovered debt, the now-present kotodama handoff contract
  (`kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`).

## Before → after measurements

Baseline `e97613c` (r89 closure, pre-work) → delivered `ca7f9ef`. Before-states that r90
created (maps, script, crossref lines) did not exist at baseline; that is stated per item
rather than inferred.

**1. Delivered support receipts (mission's r87 22/22, r88-m3 10/10 claim).**

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for c in r87-myth-cluster r88-m3-maya-cluster; do python3 corpus/tools/support_check.py "corpus/fixtures/$c" | tail -2; echo "exit=${PIPESTATUS[0]}"; done
```

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
exit=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
exit=0
```

**2. R9-mode enforcement controls (self-built `/tmp` clusters, one row each).** Paraphrase row:
`SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1`, exit 0.
Verbatim twin with the same anchor: `SOURCE-SUPPORT 1/1`, exit 0. Row `verbatim` vs declared
`paraphrase`: `FAIL X1 ... excerpt-mode=paraphrase`, `SOURCE-SUPPORT 0/1`, **exit 1**. So a
paraphrase can never add source support; the same bytes count differently only by declared mode.

**3. Span enforcement (M5 fix), `/tmp` copy of r87 with E1 locator `:7` → `:1`.**

```text
FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, ...; span=1; outside-span=7
SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
exit=1
```

**4. Substring-edge probe (script vs chousa r4 anchor class).** Two mid-word anchors
(`The springfl`, `flood came early`) inside the delivered line `The springflood came early.`:

```text
PASS X1: source-support; mode=verbatim; anchor=found; 3:> The springflood came early.
PASS X2: source-support; mode=verbatim; anchor=found; 3:> The springflood came early.
SOURCE-SUPPORT 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 2/2
RESULT PASS
exit=0
```

The script accepts occurrences whose outer edges sit inside a word; chousa's
`anchor-boundaries-r4.md:31-37` records that class and its r4 token-boundary fix. Named limit,
not a delivery defect (current maps use full-clause/space-bounded anchors; README bounds the
checker as lexical preflight).

**5. Freeze-then-verify (r88-I1).**

```sh
scratch=$(mktemp -d /tmp/lore-jcov5-ftv-XXXX)
git archive e97613c corpus/fixtures/check_bible.py | tar -x -C "$scratch"
(cd "$scratch" && patch -p1 --quiet < .../X2-c1-nullonly.patch && patch -p1 --quiet < .../X3-c1-tickonly.patch)
sha256sum "$scratch/corpus/fixtures/check_bible.py" corpus/fixtures/check_bible.py
```

```text
baseline_sha=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
composed_X2X3_sha=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered_sha=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
FREEZE-THEN-VERIFY=PASS
```

No blocking finding.

**6. K1 cross-reference landing (the mission's check).**

```sh
grep -n "chousa\|Adjacent" .ufo/waves/round-90/patches/D1-decisions.md
grep -rn "chousa" corpus/
git apply --check .ufo/waves/round-90/patches/K1-d1-crossrefs.patch
```

```text
.ufo/waves/round-90/patches/D1-decisions.md:60:**Adjacent method reference (not a transfer of lore authority):** chousa's source boundary ...
.ufo/waves/round-90/patches/D1-decisions.md:61:**Adjacent fidelity/anchor limits (reference only):** chousa documents that a clean conversion ...
<corpus grep: no output — zero "chousa" mentions in the delivered corpus>
K1_APPLY_CHECK=PASS
```

Both K1 lines landed verbatim in the D1 **wave artifact** (proposal stage: its own text says
"This is a proposed governance clarification ... No corpus ... artifact is changed by this
patch"). They did **not** land in the governing table
`corpus/knowledge/r88-sourced-inspiration-decision-table.md`, whose merged R8/R9 appendices
(lines 28-47, marked "decided r90") contain no chousa/adjacent reference. K1's citations are
accurate where they point: `claim-verification-r2.md:45-58` (URL refusal + byte-exact span),
`archives-verified-r9.md:177-185` ("verifying a conversion is not verifying the original"),
`anchor-boundaries-r4.md:31-37` (substring anchors, token-boundary fix) all check out.

**7. Delivered maps and mode labels (inventory).** r87 map: 5 excerpt declarations +
22 rows (14 JSON facts + 8 hymn clauses), every mode `verbatim`; r88 map: 3 declarations +
10 rows, all `verbatim`, with `external-only` correctly confined to the Status cell (the
K1-flagged r89 problem is repaired in the delivered map); excerpt files carry inline
`**Delivery mode (R9):**` declarations. All delivered data rows are `verbatim`; the
translation/paraphrase paths are enforced by script code and my controls, not exercised by
delivered rows — stated as a coverage bound, not a defect.

**8. Sibling surfaces.** kotodama handoff contract now exists (commit `49ac1a5`,
2026-10-17 04:00:57, sha256 `e834f50309bd93b11894e7f96d03f7000fc224a3a3ea4d654fd4d1aaaa0831f7`,
contract_id `kotodama-lore-adjacency` rev 1.0.0, §1 pins the canonical copy in kotodama and
requires a lore-side read/record before first transfer). Lore references: `l0-questions.md:4-5`
(two tracked lines, operator question open), `SCORECARD.md:217`; zero kotodama/chousa mentions
inside `corpus/`. `grep -rn "kotodama-lore-adjacency"` finds no lore acknowledgement record.
`corpus/fixtures/README.md` now has `## Round 87`, `## Round 88`, `## Round 89` sections, so
r88's D-JCOV5-2 premise ("no r87/r88 section") no longer holds.

**9. Wait-check receipt.** Check 01 `2026-10-17T06:54:59-03:00`, check 02
`06:55:59-03:00`: `head=ca7f9ef`, `status_porcelain=` empty, and identical sha256 for
`support_check.py` (`66a3c4bb…`), r87 map (`8c1b600d…`), r88 map (`d314d22e…`) at both checks.

## Findings & named debt

**Coverage-axis verdict: improved (bounded).** The C2 surface is now reproducible in the
delivered tree: the advertised receipts reproduce byte-for-byte with exit 0 on first run, the
R9 rule is actually enforced (paraphrase counts zero source support; mismatch fails closed),
span enforcement is real (M5 fix verified by the out-of-span control; the r89 un-integrated
receipt problem is gone), and the two maps cover both clusters as claimed. No trade was
detected against another axis within my block's scope; bounds are named below instead of
scored.

**Rejected-fit reasoning per sibling — the NEW r90 artifacts specifically (maps, script, mode
labels):**

- **kotodama — NOT its province (clearer than r88, contract now present).** The maps index
  in-world JSON claims to delivered excerpts; the script is lore-side verification of lore's
  own fixture corpus; the R9 mode vocabulary is lore's governance row. None is a generative
  system, naming ledger, or myth-symbol register in the contract's envelope (§4/§5); no packet
  fields (`packet_id`, `claim_ledger`, …) exist and none is required, because no transfer was
  made. The contract's §3 stop conditions are *upheld* by the new artifacts: "matching strings
  do not prove matching entities" matches the R10 appendix's "Shared names/IDs trigger
  comparison but do not prove identity", and §6's claim-kind/canon separation matches the R8/R9
  appendices' withholding rules — independently stated, no conflict. r90 added no new verse or
  symbolic material (only the pre-existing `symbolism-clause-map.md` is referenced; it is
  untouched by `ca7f9ef`), so no handoff obligation is triggered.
- **chousa — NOT its province (consumed method, one traceability gap).** The script's span
  primitive is adjacent to chousa's `verify-claims` (`CLAIM_SPAN_*`); but chousa's gate runs
  over research records with `claims.jsonl` ground truth and refuses non-research surfaces,
  while this checker runs over in-world claim→excerpt maps inside the world bible — the
  boundary r88 JCOV5 already ruled, unchanged. The rejection is *not affected* by the K1 lines
  having landed only in the wave file: those lines explicitly say "not a transfer of lore
  authority". The one real gap is traceability, not scope.

**Named debt:**

- **ND-1 (new; the K1 landing answer):** the two K1 chousa cross-reference lines are delivered
  only in the proposal-stage wave artifact (`patches/D1-decisions.md:60-61`); the governing D1
  table's merged appendices carry none. Q89-047's "delivered governance cross-reference" half
  therefore remains open (the L0 half was never triggered). Any repair is a write to the
  canonical table by the owning lane — not made by this seat, and not a freeze blocker
  (checker hash matched).
- **ND-2 (new):** delivered `support_check.py` anchors are plain `grep -nF` substrings;
  mid-word/truncated occurrences pass (probe above). chousa's r4 token-boundary hardening is
  exactly the cited-but-unlanded crossref's subject. Current receipts are unaffected (all
  delivered anchors are clause/space bounded); the limit is named for future authoring, or the
  governance line should point at `anchor-boundaries-r4.md` when it lands.
- **ND-3 (carried, rescoped):** r88's D-JCOV5-1 ("handoff contract absent") is resolved by
  delivery (contract present, hash above, tracked in `l0-questions.md:5`). What remains is
  lore's §1 read/record duty — untriggered, no record exists; carried as Q89-048. Do not
  manufacture an acknowledgement.
- **D-JCOV5-2 (premise obsolete):** `corpus/fixtures/README.md` now has Round 87/88/89
  sections; remaining content-enumeration quality is Q1's Q89-030 (partial), outside this
  seat's block.
- **Observed, untouched:** untracked `corpus/tools/__pycache__/` exists in the working tree
  (not created by this seat; run-as-script does not emit pycache). Relates to Q89-044; no
  `.gitignore` repair was in scope here.

## Handoff

- Artifacts: `.ufo/waves/round-90/followup/JCOV5.md` (this report) and
  `.ufo/waves/round-90/followup/JCOV5-probes.json` (machine receipts for items 1–6, 8–9).
  Only these allowed paths were written; sibling repos read-only; no commit or push.
- Coverage: **improved (bounded)** — receipts reproduce, R9 and span enforcement verified by
  independent controls, freeze-then-verify PASSES (no blocking finding).
- Integrator: (1) treat ND-1 as the open half of Q89-047 — if the crossrefs are wanted as
  governance, they must be added to `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
  by the owning lane; (2) keep ND-2/ND-3 in the round record as named; (3) do not record a
  kotodama acknowledgement or a governance crossref as closed on the strength of the wave file.
