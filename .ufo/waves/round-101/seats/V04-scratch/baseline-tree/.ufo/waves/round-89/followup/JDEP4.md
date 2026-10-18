# JDEP4 — Depth judge #4 (capabilities assessment), round 89

Seat JDEP4. Judged on the DELIVERED tree only: HEAD `1b09f3ff8016b26a2259e086f673d0112f4f54e5`
(baseline `51b286b`), `git status --short` shows only the untracked `followup/` directory
(no tracked modification). All probes ran from the repository root
`/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline probes ran on a
`git archive 51b286b` extraction under `/tmp/jdep4-base` (read-only on the repo).

**Question posed to this seat:** recommend for or against a second `capabilities` row,
*in-world excerpt support verification* — the D1 support rule plus the grep-anchor
machinery, now demonstrated on 22/22 facts and by the R9 demo. Evidence must be a
runnable command.

**Recommendation: FOR** — the capability is real, distinct from row 1, and I ran it on
the delivered tree; it must enter with two preconditions and three recorded bounds (see
Findings).

## Work performed

- Read `AXES.md` §Capabilities (row contract: name → what it can do → evidence pointer
  (command or path) → first-working round; rows enter only through a round that
  demonstrates the capability running), the delivered `SCORECARD.md` (both the
  structured `## Capabilities` table and the r87/r88 narrative rows), and the delivered
  D1 rule at `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (rows R5
  in-world support, R8 rights-blocked disposition, R9 delivery-mode, R10 cross-cluster).
- Established what row 1 already covers (`provenance stop-cause assessment`: which cause
  latched inside a provenance chain, structural) so the candidate row is not a duplicate.
- Built and ran a single reproducible support sweep over the delivered r87 cluster:
  fact census + 14 fixed-string anchors replayed from the committed anchor map
  `.ufo/waves/round-89/patches/M4-verify.json` + the pre-existing hymn claim.
- Ran the same machinery over the r88 Maya cluster (breadth check) and re-ran the R9
  negative demo (`corpus/fixtures/r89-inspiration-paraphrase/`).
- Ran the identical sweep against baseline `51b286b` in `/tmp` for the before-state.
- Audited the discoverability of the capability's evidence on the delivered tree
  (fixtures README, r87 cluster README, SCORECARD table, ledger row order).
- No repository file was modified except this report and `JDEP4-evidence.json`. No
  commit, no push.

**The runnable command (evidence pointer candidate).** From the repository root:

```sh
python3 - <<'PY'
import json, pathlib
cluster = pathlib.Path("corpus/fixtures/r87-myth-cluster")
sources = {s["id"] for s in json.loads((cluster/"sources.json").read_text())}
entities = json.loads((cluster/"entities.json").read_text())
relations = json.loads((cluster/"relations.json").read_text())
events = json.loads((cluster/"timeline.json").read_text())
prose = {p.stem.removesuffix("-excerpt"): p.read_text() for p in cluster.glob("*-excerpt.md")}
anchors = json.loads(pathlib.Path(".ufo/waves/round-89/patches/M4-verify.json").read_text())["after"]["checks"]
pointers = [e["first_appearance"] for e in entities]
claims = sum(len(e["claims"]) for e in entities)
hymn = int("Mother-Tide Gate" in prose.get("lowwater-hymn", ""))
anchored = sum(c["anchor"] in pathlib.Path(c["excerpt"]).read_text() for c in anchors)
ptr_ok = sum(s in sources for s in pointers)
facts = len(pointers) + claims + len(relations) + len(events)
print(f"r87 D1 support: facts={facts} OK={ptr_ok+hymn+anchored} not-OK={facts-(ptr_ok+hymn+anchored)} (pointers {ptr_ok}/{len(pointers)}, hymn {hymn}/1, anchored {anchored}/{len(anchors)})")
PY
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
```

Observed, delivered tree `1b09f3f`, exit 0:

```text
r87 D1 support: facts=22 OK=22 not-OK=0 (pointers 7/7, hymn 1/1, anchored 14/14)
CLEAN: schema, citations, relations, timeline; 0 violations
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
```

The third line is the point of the R9 half: the checker is `CLEAN` and the anchor hits,
yet `claim-to-excerpt-map.md` records the claim as **failing** support because the
delivered text is a paraphrase, not the source's own words. The capability returns
negative verdicts, which is what separates verification from assertion.

## Before → after measurements

**M1 — r87 cluster support sweep, baseline vs delivered.**

```sh
git ls-tree -r --name-only 51b286b -- corpus/fixtures/r87-myth-cluster
mkdir -p /tmp/jdep4-base && git archive 51b286b corpus/fixtures/r87-myth-cluster | tar -x -C /tmp/jdep4-base
cd /tmp/jdep4-base && python3 <the sweep above, run with cwd here>
```

Baseline `51b286b` (9 files; the only delivered excerpt is `lowwater-hymn-excerpt.md`):

```text
facts=22 OK=8 not-OK=14 (pointers 7/7, hymn claim 1/1, anchored facts 0/14)
```

Delivered `1b09f3f`: `facts=22 OK=22 not-OK=0 (pointers 7/7, hymn 1/1, anchored 14/14)`.
Delta: +14 supported facts, 0 regressions. The 14 are 6 entity claims (E1–E6), 4 relation
edges (R1–R4), 4 timeline events (T1–T4).

**M2 — the 14 anchors are real fixed-string hits, not substring luck in one file.**

```sh
bash <14-line grep -nF loop, one check per fact, /tmp/jdep4-anchors.sh>
```

Observed: `OK E1..T4` for all fourteen, `anchors: OK=14 FAIL=0`. Each anchor resolves in
the excerpt named by the committed map (gate-witness ×3, dune-register ×4, shell-charter
×5, tide-bell-tally ×2). Note: M4's map still carries the pre-integration R3 anchor
`Shellweavers keep watch with the Reed Bell`; the delivered line 11 is the pledge-framed
`Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.`,
so the map's anchor is a substring of the delivered sentence and still hits. Stale-anchor
risk is real but did not bite here.

**M3 — breadth: the same machinery on the r88 Maya cluster.**

```sh
python3 <per-fact sweep: 4 claims + 2 events anchored in fictional-excerpts.md, 4 pointers>
```

Observed: `r88 D1 support: facts=10 OK=10 not-OK=0 (pointers 4/4, anchored facts 6/6 drawn
from 2 delivered lines)`. Two clusters, 32/32 facts. (The r88 cluster has no in-tree
claim-to-excerpt map; its mapping lives in the r88 follow-up evidence, so this replay is
mine, not a re-run of a delivered map.)

**M4 — the R9 demo commands.** `python3 corpus/fixtures/check_bible.py
corpus/fixtures/r89-inspiration-paraphrase` → `CLEAN: schema, citations, relations,
timeline; 0 violations`, exit 0; `grep -nF -- 'moved to the west stair'
corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md` → line 9 hit, exit 0.
Both match the fixture README's stated expectations.

**M5 — discoverability of the capability on the delivered tree.**

| probe | command | observed |
|---|---|---|
| structured capabilities table | `git show 1b09f3f:SCORECARD.md \| sed -n '72,78p'` | `\| — none yet — \| \| \| \|` |
| row 1 recorded anywhere | `grep -n "provenance stop-cause" SCORECARD.md` | only line 146 (r88 narrative section) |
| fixtures README round section | `grep -n "Round 89" corpus/fixtures/README.md` | no match, exit 1 (last section is Round 88) |
| r87 cluster README lists the new excerpts | `grep -n "gate-witness\|dune-register\|shell-charter\|tide-bell-tally" corpus/fixtures/r87-myth-cluster/README.md` | no match, exit 1 |
| work commit touches round record | `git show --stat 1b09f3f \| grep -cE "SCORECARD.md\|LOG.md\|corpus/fixtures/README.md"` | `0` |
| ledger row order | `grep -n "^\|" corpus/knowledge/reference-ledger.md \| tail -3` | ETCSL row line 8 (in table, marker present), Spence row line 13 (after the table's closing prose) |

## Findings & named debt

**F1 — the candidate row is distinct from row 1 and passes the `AXES.md` entry test.**
Row 1 (`provenance stop-cause assessment`) reports which cause latched inside a
provenance chain — a structural judgement made by `check_bible.py`. The candidate judges
whether delivered *prose* supports a source-attributed claim: resolve `source_id` →
locate the excerpt → fixed-string anchor preflight → whole-claim review → delivery-mode
screen. Different inputs, different machinery, different failure modes, and it can return
a negative verdict where the checker is `CLEAN` (M4). It is not a re-description of row 1.

**F2 — the demonstration is real and reproducible, but it is procedure-shaped, not
tool-shaped.** The sweep in Work performed runs green on the delivered tree, and the
machinery has already produced a real find (the r87 hymn attribution was unsupported at
r87, detected under this rule, repaired at r88, and the remaining 14 facts closed at r89).
The rule itself says a match "is only a lexical preflight"; the whole-claim review is
human. That is the same shape as row 1's evidence (a `for` loop plus a reading), so it
meets the precedent — but the row must not be worded as if the command decides support.

**F3 — precondition 1: the structured `## Capabilities` table must be repaired in the same
edit.** At `1b09f3f` the table still reads `— none yet —`, while the r88 narrative section
claims the first row entered (`SCORECARD.md:145-154`, closure commit message included).
Row 1 exists only as prose. Adding row 2 into a table that still denies row 1 would land
a self-contradicting SCORECARD. Both rows must be written into the table together.

**F4 — precondition 2: the evidence command must appear in the round report.** `AXES.md`
requires a passing demonstration in the round report; a row with a pointer nobody ran is
pre-claiming. The command block in Work performed is what I actually executed.

**F5 — bound to record in the row: the anchor map is wave-resident, not corpus-resident.**
For r87 the claim→anchor map lives in `.ufo/waves/round-89/patches/M4-verify.json`
(committed, so durable, but wave evidence). No landed cluster carries a
`claim-to-excerpt-map.md` in its own directory — only the R9 demo does. Cheap repair if
the parent wants the row's pointer corpus-resident: land a map in the r87 cluster in the
R9 demo's format. Until then, the row's evidence pointer must cite the wave path
explicitly, and the r88 half of the breadth claim is my replay, not a delivered map.

**F6 — bound to record: the R9 half is demonstrated only negatively.** The only delivered
excerpt carrying a delivery-mode declaration is the paraphrase demo, and it must fail.
No delivered excerpt declares `verbatim` or `translation`, so the positive mode path
(declared mode → eligible source anchor) is not exercised anywhere on the delivered tree;
R8/R9/R10 are prospective per the table's own integration notes. The row must say
"delivery-mode screen demonstrated on the paraphrase-failure class only".

**F7 — documentation-parity debt (r88 precedent says this counts as harm at closure).**
(a) `corpus/fixtures/README.md` has no `## Round 89` section, and the r87 cluster README
still names only `lowwater-hymn-excerpt.md` and `symbolism-clause-map.md`, so the four
excerpts that make 22/22 true are undiscoverable from the fixture docs. (b) Carried over
from r88: the Spence ledger row sits at line 13, after the table's closing paragraph, so
it renders outside the table; the ETCSL row (line 8) is correctly in-table and carries
`external-only / text not delivered at lore`. (c) The work commit `1b09f3f` touches
neither `SCORECARD.md`, `LOG.md`, nor `corpus/fixtures/README.md` — expected if the
closure commit owns the round record, but all three must land before admission.

**Per-axis verdicts (this seat's remit).** depth: **improved (bounded)** — the support
rule is executable on the delivered tree and returns both positive (22/22, 10/10) and
negative (R9 paraphrase) verdicts; bounds F5/F6. coverage: **improved (bounded)** — 32/32
source-attributed facts supported across two clusters, ETCSL marker present; bound:
r88 cluster mapping is not delivered as a map. calibration: **unchanged** — no
self-assessment artifact changed in this work commit. No axis harmed by the capability
itself; F7 is the outstanding parity item.

## Handoff

- **Verdict: FOR a second capabilities row, `in-world excerpt support verification`**,
  conditional on F3 (repair the structured table with row 1 + row 2 in one edit) and F4
  (the command lands in the round report). Suggested row text, using the measured values:
  *"For an in-world claim attributed to a source, resolve the `source_id`, locate the
  delivered excerpt, run a fixed-string anchor preflight over the recorded anchors, and
  return a support verdict — including refusal when the delivered representation is a
  paraphrase/summary or the source text is undelivered."* Evidence pointer: the three-line
  command in Work performed (r87 `facts=22 OK=22`, R9 demo `CLEAN` + anchor hit + support
  withheld). First-working round: r89. Bounds: F2, F5, F6 verbatim.
- If the parent will not repair the table this closure, the honest alternative is to
  defer the row one round rather than enter it into a table that still says "none yet".
- Repair F7(a)/(b) before admission; F7(c) is the closure commit's normal job.
- Reproduce anything here with `bash /tmp/jdep4-final.sh` (three commands above, exit 0)
  and `followup/JDEP4-evidence.json` (commands + raw outputs).
- Not done by this seat: no SCORECARD/LOG/README edit (not authorized), no commit, no
  push, no sibling-repo writes.
