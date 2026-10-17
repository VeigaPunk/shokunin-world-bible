# F28 — shonen-format (round-94 FOLLOW-UP verification seat, lore-shokunin)

**Seat role:** closure-mechanics check — (a) the round-94 fleet report contract (work performed / landed changes / before→after measurements / SHONEN section and content bar), (b) the current `SHONEN.md` box states (expected four `[~]`/`[ ]`, no `[x]` without a named non-author verifier), (c) what the integrator must land for a contentful `.ufo/reports/round-94/lore.md`. LEAF scope: read-only checks; this report is my only write.

**Revision tested:** lane HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (`65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch`); candidate `abbc3e0186c89016d5cbe68b37a2c027bf11d548` (`abbc3e0`). Ancestry confirmed:

```
$ git merge-base --is-ancestor abbc3e0 HEAD && echo "abbc3e0 is ancestor of HEAD(65a9329)"
abbc3e0 is ancestor of HEAD(65a9329)
```

## 1. Current `SHONEN.md` box states — four `[~]`, no `[x]`

Read of `SHONEN.md` (12 lines, full file):

```
5  - [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
7  - [~] At least one end-to-end domain task executed and logged in LOG.md
9  - [~] Instructions executable by an agent without oral context
11 - [~] No cross-domain bleed (PROVINCE.md still accurate)
```

All four boxes are `[~]`, each with exactly one evidence line, and each evidence line ends `Lane assertion, not external promotion verification.` (`SHONEN.md:6,8,10,12`). Zero `[x]`:

```
$ grep -n "\[x\]" SHONEN.md
(no output; exit 1)
```

Mechanical replay of the canonical-form checker at this revision — **exit 0**, 10/10 PASS:

```
$ python3 .ufo/waves/round-93/deepseek/F29-shonen-format-check.py
PASS title matches seed modulo <name>
PASS seed frame (blank + manifest line)
PASS four boxes, seed order and text
PASS marks confined to box character
PASS no [x] promotion claim present
PASS at most one evidence line per box
PASS both [~] boxes carry their required pointer
PASS box2 evidence names the LOG.md entry
PASS box2 evidence names reports/round-1/baseline-probes.json
PASS box4 evidence cites PROVINCE.md:3-11 within range
SHA256 SHONEN.md 03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1
SHA256 SKILL.md 20c2590157821fa68b0bf1f31e5ef551bbc0921d0c6dd1f0d4c1b1442b45210b
SHA256 PROVINCE.md 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
EXIT=0
```

Every path named in the four evidence lines resolves (13/13 `OK`, e.g. `SKILL.md`, `.ufo/waves/round-93/recovery/R08-skill-check.py`, `.ufo/waves/round-93/deepseek/F21.md`, `reports/round-1/baseline-probes.json`, `.ufo/waves/round-93/deepseek/F25-replay.py`, `.ufo/waves/round-93/deepseek/F14-postrepair-check.py`, `PROVINCE.md:3-11`). `SHONEN.md` is tracked and the lane tree is clean apart from this seat's untracked `followup/` directory (`git ls-files SHONEN.md SKILL.md PROVINCE.md` → three paths; `git status --short` → `?? .ufo/waves/round-94/followup/`).

**Gate text that governs `[x]`:** `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did not author the round's changes, and "a subagent the lane dispatched is still the lane"; "any `[x]` carrying no named non-author verifier is author attestation counting as `[~]`". Canonical form and seed: `PROTOCOL.md:417` and `PROTOCOL.md:423-435` (seed byte-identical modulo `<name>`, marks confined to the box character plus one indented evidence line per box). The round's own invariants repeat the bar: "No capability row or final verdict is entered before its demonstrated final result; no promotion or `[x]`" (`.ufo/waves/round-94/wave-spec.md:34`), and the r94 declaration commits to the same (`LOG.md:2683-2701`, esp. the closing line "No r95 start before this closure; no capability row before a demonstrated final result."). **Consequence for r94:** the DeepSeek FOLLOW-UP seats are lane-dispatched subagents, so even a clean 40-seat wave cannot convert any box to `[x]`; all four boxes must stay `[~]` in the r94 report unless an outside non-author verifier is named.

## 2. The round-94 fleet report contract

The operative text is the shipped round-prompt template, `templates/round-prompt.md:60-78` (§4 "Report contract"), and its protocol mirror at `PROTOCOL.md:144-153` + `PROTOCOL.md:175-183`.

- **Path and name:** `{{FLEET_ROOT}}/.ufo/reports/round-{{ROUND}}/{{LANE}}.md` on the fleet repo (`templates/round-prompt.md:62-63`); `PROTOCOL.md:138-139`: "Every dispatched lane writes its report at `.ufo/reports/round-<N>/<id>.md` in the main repo" — a report under any other name does not satisfy the contract. For this round: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-94/lore.md`.
- **Required sections, in order** (`templates/round-prompt.md:64-74`): **Work performed** — opens by naming the round's declared claims (1–3) and their target axes or capability, then one bullet per work item, each with an evidence pointer (path:line, command output, or commit hash); **Landed changes** — every change tied to a `LOG.md` entry and to the commit hash that carries it; **Before → after measurements** — one per claim, each with the counting command and the commit it was measured against; **SHONEN** — one line per box of the lane's `SHONEN.md` checklist: `[x]` only with a named non-author verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched.
- **Content bar / marker rule** (`templates/round-prompt.md:75-78`): "a contentless report (placeholder text, missing required sections, no evidence pointers) counts as the round **failed** — the driver relaunches the same round. A report that names real committed work but skips the required sections is `ok` plus a minimum-content conformance defect, logged as one."
- **Protocol minimum content** (`PROTOCOL.md:144-153`): work performed and evidence pointers; changes landed in the child repo each tied to a `LOG.md` entry; cross-domain evidence with its domain; the `SHONEN` checklist assessment "under a `SHONEN` heading with one line per box". "A report without this heading does not satisfy the contract even if the same facts appear elsewhere in it"; the omission is a conformance defect **and** disqualifies the report as promotion evidence, re-filed under the heading in the next round's report (the r91 report's omission and r93's re-filing are the precedent: `.ufo/reports/round-93/lore.md:79`).
- **Commit-hash citation rule** (`PROTOCOL.md:117-127`): the report lands last, only after the lane's child-repo work is committed; it must cite that commit's hash; the cited hash must exist in the repo and be an ancestor of `HEAD` at closure (`git merge-base --is-ancestor <hash> HEAD`); corrections land as new commits, never by amending a cited one. The report commit itself must carry the lane identity (`PROTOCOL.md:125-127`).
- **Driver content check as written** (`PROTOCOL.md:175-183`): the completion signal requires the `SHONEN` heading with one `[x]`/`[ ]`/`[~]` line per box **and** the minimum substance (work performed, at least one evidence pointer, landed changes each tied to a `LOG.md` entry, a checkable commit-hash citation). "A contentless **completion marker** at that path closes nothing."

**Observed discrepancy (report exactly as found):** `PROTOCOL.md:176-177` states that "the driver's completion check (`report_of()` in `scripts/shokunin-watchdog.sh`) validates report **content**, not merely the path's existence", but the shipped script does not. Full 118-line read of `/home/vgpnk/Projects/shokunin/scripts/shokunin-watchdog.sh`; its only `report_of()` is:

```
45: report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }
```

There is no content validation anywhere in the file (no `SHONEN`, no `grep` over report bytes; the only greps are at lines 80 and 95 over launch/status output). Additionally the fleet-level watchdog's `LANES` list (line 14) does not contain `lore` at all (`protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama`), so this driver does not gate the lore lane's rounds; `lore.round` sits at 1 (`.ufo/state/lore.round` → `1`) while the lane is on its 94th steered round. Net effect: for r94 the content bar is normative for the integrator's closure judgment but is **not mechanically enforced** by the shipped watchdog in this checkout — the integrator must apply it by review, and this gap is itself a candidate protocol/appendix defect (same class as the "Unlanded report" row, `PROTOCOL-APPENDIX.md:41`).

## 3. What the integrator must land for a contentful `.ufo/reports/round-94/lore.md`

Current state: the report does not exist, in either repo.

```
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-94/
ls: cannot access '/home/vgpnk/Projects/shokunin/.ufo/reports/round-94/': No such file or directory
$ ls lore-shokunin/.ufo/reports/
round-86
```

Fleet-repo HEAD is `0941d7422c287162cf44f941a37263f382568d98` (`0941d74 protocol: close lore r93 and append historical record corrections`); the last lore closure entry in `MANIFEST.json` is round 93 (`{"round": 93, ..., "lanes": {"lore": "ok"}, ..., "admitted": true, "verdicts": {...}}`), so round 94 is unclosed in the ledger. The r93 report (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-93/lore.md`, committed at `2255b87` by the lane identity) is the working exemplar: title line, L1 ruling, lane HEAD citation, then `## Work performed`, `## Landed changes`, `## Before → after measurements`, `## SHONEN`, `## Axis and learning verdicts`, and continuation notes.

Minimum checklist for a contentful r94 report, each item with its governing pointer:

1. **Exact path/name**: `.ufo/reports/round-94/lore.md` on the fleet repo (`templates/round-prompt.md:62-63`, `PROTOCOL.md:138-139`).
2. **Four required sections in order**, with Work performed opening on the declared claims C1/depth and C2/calibration (`templates/round-prompt.md:64-74`; claims recorded in `.ufo/waves/round-94/wave-spec.json` `claims` and `.ufo/waves/round-94/wave-spec.md:9-27`).
3. **Evidence pointer per work item; counting command + measured commit per before→after measurement** (`templates/round-prompt.md:65-72`). The r94 candidate facts to measure against: counts 4/0/2 → 5/1/3 entities/relations/events, 14 map obligations, `check_bible.py` CLEAN, `support_check.py` PASS, `map_obligations.py` r93 12/12 and r94 14/14, `--self-test` exit 0, frozen r93 exit 0 (LOG.md:2664-2682).
4. **Landed changes each tied to a `LOG.md` entry and its commit hash** (`templates/round-prompt.md:67-68`). Lane commits so far: `9c2eea3` (pre-round baseline), `abbc3e0` (WORK checkpoint), `65a9329` (follow-up declaration, `LOG.md:2683`); any follow-up repair commit must be named too, and the report must not claim an unfiled hash.
5. **Cite the lane HEAD when the report is written and keep it checkable** — `PROTOCOL.md:117-127`; current HEAD `65a9329` (`git rev-parse HEAD`), with `abbc3e0` proven an ancestor (command output above).
6. **`## SHONEN` section with one line per box** — four lines, all `[~]` with resolvable pointers, no `[x]` (see §1; `PROTOCOL.md:63-68,148-153`). The section must be present even if the same facts appear elsewhere in the report (`PROTOCOL.md:148-153`).
7. **Content bar satisfied end-to-end**: work performed, ≥1 evidence pointer, landed changes tied to `LOG.md`, checkable commit-hash citation, `SHONEN` heading (`PROTOCOL.md:178-181`). Otherwise the report is a marker: the round counts **failed**, not ok (`templates/round-prompt.md:75-78`).
8. **Report committed path-limited under lane identity on the fleet repo**, after the lane work commit (`PROTOCOL.md:117-127`), with `.ufo/waves/` and `.ufo/reports/` durable in the round's integration commit (`PROTOCOL.md:455-457`). Wave-spec invariant: "Report existence is not completion; the fleet report lands only after committed work and actual FOLLOW-UP" (`.ufo/waves/round-94/wave-spec.md:33`); actual results and agent IDs are recorded only after the dispatch returns (`.ufo/waves/round-94/wave-spec.md:35`).
9. **The report must account for the recorded defects honestly**: the W20 failed-output gap (32 tool-completed labels vs 31 usable reports; `.ufo/waves/round-94/work-receipt.json:56-64`, `known_seat_output_defects`), and the actual FOLLOW-UP receipt (counts, call IDs) once dispatched. The r94 checkpoint LOG entry already models this (`LOG.md:2664-2682`).
10. **Separately, the integrator-of-record (protocol lane) appends the `MANIFEST.json` `rounds[]` entry** — shape `{round, date, type, lanes: {lore: ok|failed|in-flight|not-dispatched}, promotions, minted, notes}` (`PROTOCOL.md:237-242`); an `ok` row needs no pointer, non-ok rows carry theirs in `notes` (`PROTOCOL.md:290-292`); `in-flight` is debt answered by the next protocol round (`PROTOCOL.md:273-279`); appends are append-only with `closure-correction` type for fixes (`PROTOCOL.md:299-306`); the history pin is checked at closure (`PROTOCOL.md:307-310`). This is the integrator's act, not the lane's file (`PROTOCOL.md:448-454`).

## 4. Side observations (for the integrator, not verdict-bearing)

- **Follow-up report path divergence:** `.ufo/waves/round-94/followup/F02-c1-support.md` was filed at the **fleet repo root** (untracked there: `git status --short` at `/home/vgpnk/Projects/shokunin` → `?? .ufo/waves/round-94/`), while this seat's and F01/F06/F08/F09/F11/F32/F33/F34/F36 reports are landing under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-94/followup/`. Since `.ufo/waves/` is committed with the round's integration commit (`PROTOCOL.md:455-457`), the fleet-root copy needs an explicit durability decision or the seat's evidence is attribution-defective; recorded here as observed, not adjudicated.
- **`PROTOCOL.md:417` seed fidelity holds at the byte level** for `SHONEN.md` apart from box marks and the four evidence lines (checker PASS set above; `SHONEN.md` SHA-256 `03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1`). Any regeneration that adds prose would fail the mechanical check.

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]` boxes, one evidence line each, zero `[x]`, and the mechanical form checker replays exit 0 at `65a9329`; the r94 report contract and its content bar are located with exact pointers, and the integrator's required landing set for a contentful `.ufo/reports/round-94/lore.md` is enumerated — with the one observed defect that the shipped watchdog's `report_of()` is existence-only, contrary to `PROTOCOL.md:176-177`, so the content bar rests on integrator review rather than the driver.
