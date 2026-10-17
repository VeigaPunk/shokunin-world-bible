# JCAL2 — Watch judge (r92 follow-up, world-bible lane)

Judgment surface: committed tree at `c4d4823b9a8165a88e8199af136e62d6e961b6b9` (baseline `396c568`); `git status --porcelain` was empty (0 lines) at measurement start. Judged artifact: `corpus/knowledge/r91-c9-watch.md` (SHA-256 `a6b2b9db92d494f390a414d1d84bfc4f074865f93e4ad4874cbfa7b9c95d9c77`). Checker `corpus/fixtures/check_bible.py` SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` — matches the run row and the pin. No waits were needed: every dependency (committed watch, checker, fixtures, r90 recipe) was present; the poll helpers hit immediately. Verdict evidence is committed-tree only; `/tmp` was scratch and is removed.

## Work performed

- Re-ran the watch's full probe suite against the delivered checker: pinned hash; the durable pair `r91-c1-null-chain` / `r91-c1-tick-unresolved`; all four C5 semantic probes independently reconstructed from the tracked recipe `.ufo/waves/round-90/patches/C9-rerun-probes.sh` (SHA-256 `2814861959bcf04c52a373b14995cdd55eaa84144a9e71c3c8e8b6ae148bd7d7`) with one disposable fixture at a time under `/tmp`, each removed after its run.
- Re-ran the four-gate evidence commands verbatim: the item/holder count command and the sequence-scope evidence command.
- Checked the census/path-convention notes: enumerated fixture dirs missing a required section file, and spot-checked the absolute-vs-relative stdout claim.
- Verified the receipts transfer to the judgment surface: `git diff --stat 396c568 c4d4823 -- <checker + both durable fixtures + r89 base fixture>` is empty.
- Searched the committed tree and the two proposal patches for a next-recheck pointer; ran CB's successor probe on the committed watch.
- Writes: this report and `followup/JCAL2-receipts.json` only. No commit, no push. Scratch dirs (`/tmp/lore-jcal2-c9-*`) were removed; `/tmp` inode pressure was pre-existing (99%, 15411 free), and this seat left no files there.

## Before → after measurements

**Surface and pin.**

```sh
git rev-parse HEAD
git status --porcelain | wc -l
sha256sum corpus/fixtures/check_bible.py
```

```text
c4d4823b9a8165a88e8199af136e62d6e961b6b9
0
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

**Durable pair** (run from `lore-shokunin/`; exit and stderr captured separately):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

```text
r91-c1-null-chain: exit=1 stderr_bytes=0 stdout_sha256=615dc0564f531352a574ef2f53c48be42f4e53ad1fac4aa88756e4bba2fada5b
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
r91-c1-tick-unresolved: exit=1 stderr_bytes=0 stdout_sha256=d754e96f7c01e6fb6eff12168a732d5a6125f428a9207bd74fc49bbdcbb25d88
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

Both stdout hashes are byte-identical to the r91 JCAL2 delivered receipts (`615dc056…`, `d754e96f…` in `.ufo/waves/round-91/followup/JCAL2.md`). The check-log blocks match line-for-line.

**Four C5 probes (independent reconstruction).** Mutation tuples read from the tracked recipe and used exactly: `chain-unresolved`=None, `tick-relevant-unresolved`=`((3,None,'f3-dup'),(1,'f3-dup','harbor'))`, `null-from-chain`=`((0,None,'mira'),(1,None,'harbor'))`, `unrelated-duplicate-tick`=`((3,None,'mira'),(1,'mira','mira'))`; base `corpus/fixtures/r89-fn2-unresolved-chain-break`, sections symlinked, cwd `lore-shokunin/`. Observed (each exit 1, stderr empty):

```text
--- P1-unresolved-chain exit=1 stderr_bytes=0 sha=66ed1438c6d1af003492d29569492ec0990e5b01b041fba1b4e21147eab4327a
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
2 violation(s); no canon changed
--- P2-tick-relevant-unresolved exit=1 stderr_bytes=0 sha=5137f7fd378b9c9cc103df61f69751c5c6eb4d084a84557e55ea406724a42929
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed
--- P3-null-from-chain exit=1 stderr_bytes=0 sha=fd8eb05099a1e3af0ac4fc075f049722e60efe1f51c1355ad8bc70232ea4cacb
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got None
2 violation(s); no canon changed
--- P4-unrelated-duplicate-tick exit=1 stderr_bytes=0 sha=5137f7fd378b9c9cc103df61f69751c5c6eb4d084a84557e55ea406724a42929
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed
scratch_removed=YES
```

All four outputs are byte-identical to the check-log blocks and to the r91 delivered-checker references recorded in `.ufo/waves/round-91/followup/H3-r91-replay.json` (`c9-chain-unresolved-stays-qualified`, `c9-tick-relevant-unresolved-tick-definite`, `c9-null-from-chain-definite`, `c9-unrelated-duplicate-tick-definite`). H3's `matches_c9_x1_stdout: false` on the tick-relevant row compares against the superseded r90 X1 candidate's identity-qualified stdout, not against the r91 ruling — consistent with the watch text ("The r90 X1 candidate's P2 identity qualifier is not the current expected output").

**Gate evidence.** Count command (verbatim from the watch):

```sh
python3 - <<'PY'
import json
from pathlib import Path

def admitted(row):
    fields={'id':str,'kind':str,'name':str,'first_appearance':str,'claims':list}
    return isinstance(row,dict) and all(field in row and type(row[field]) is kind and (kind is not str or bool(row[field].strip())) for field,kind in fields.items())
for label,path,holder,ticks in [
    ('P2 unresolved','corpus/fixtures/r91-c1-tick-unresolved','f3-dup',None),
    ('P4 control','corpus/fixtures/r89-fn2-unresolved-chain-break','mira',[3,1]),
]:
    rows=json.loads((Path(path)/'entities.json').read_text(encoding='utf-8'))
    item_rows=[r for r in rows if r.get('id')=='f3-seal' and r.get('kind')=='item' and admitted(r)]
    holder_rows=[r for r in rows if r.get('id')==holder]
    indexed=[r for r in holder_rows if admitted(r)]
    if ticks is None:
        ticks=[r.get('tick') for r in item_rows[0].get('provenance',[])] if len(item_rows)==1 else []
    print(f'{label}: item=f3-seal admitted_matches={len(item_rows)} ticks={ticks} holder={holder} raw_rows={len(holder_rows)} resolved_rows={len(indexed)}')
PY
```

```text
P2 unresolved: item=f3-seal admitted_matches=1 ticks=[3, 1] holder=f3-dup raw_rows=2 resolved_rows=1
P4 control: item=f3-seal admitted_matches=1 ticks=[3, 1] holder=mira raw_rows=1 resolved_rows=1
```

Sequence-scope command (verbatim) and output:

```text
excerpt_files=
readme_line3=Fixture scaffolding only; not sourced story evidence.
```

**Receipts transfer to the judgment surface.**

```sh
git diff --stat 396c568 c4d4823 -- corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-unresolved-chain-break corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved
```

```text
(no output; exit 0)
```

The checker and all four fixture bases are unchanged between the section's stated run HEAD `396c568` and the committed tree `c4d4823`, so the check-log receipts hold verbatim on the judgment surface.

**Poll receipts** (replayed from `lore-shokunin/`; both hit immediately):

```text
POLL_HIT path=corpus/fixtures/check_bible.py elapsed=0s checks=0
POLL_HIT path=corpus/knowledge/r91-c9-watch.md elapsed=0s checks=0
```

**Census/path-convention notes.** Enumerated the 166 direct fixture dirs for a missing required section file: exactly 5 (`r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-control`, `r67-claim-source-unavailable-empty`, `r67-claim-source-unavailable-whitespace`), and each echoes its argv path in stdout. Spot check `r5-missing-file`:

```text
relative: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
absolute: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
stdout_equal=False (both exit 1)
```

**Next-recheck pointer search.** Exact search (committed tree + the two proposal patches):

```sh
grep -rn -i "next re-check\|next recheck\|next periodic\|successor" corpus/ .ufo/waves/round-92/patches/X1-recheck.patch .ufo/waves/round-92/patches/E3-c3-wording.patch
```

```text
(no output)
```

CB's successor probe on the committed watch (exact command shape recorded at `.ufo/waves/round-92/CB.md:210`, re-executed on `c4d4823`):

```text
watch_e97613c_sha_pinned=False watch_ambiguous_source_wording=False watch_successor_named=False tick_parent_or_composition_note=False
checker_e97613c_hash_in_watch=False
```

## Findings & named debt

- **Check-log row 1 — verified: dated, accurate, matches observation.** Date `2026-10-17` (same day as this re-check and the integration commit); checker hash column equals the observed file hash and the pin; `DISCRIMINATION HELD` is independently reproduced on `c4d4823`; the four C5 distinctions are exactly as claimed — P1's unresolved chain stays qualified, P2's integer inversion is definite without identity context, P3's null chain break is definite, P4's unrelated duplicate does not qualify the tick finding. "No drift alarm" is consistent with the re-derived gates: gates 1–2 met, gate 3 not met, gate 4 therefore not a counterexample.
- **Bounded, not absolute.** The discrimination claim covers the six named probes (pinned checker + durable pair + P1–P4), not semantic coverage of every checker/corpus path; P2/P4 are a near-control, not a single-field pair (the watch states the inherited invalid `first_appearance` and E3/C5 recorded the near-control bound). P2/P4 target outputs are hash-identical by design (same tick finding), and the target diagnostic — not the nonzero exit alone — carries the discrimination.
- **Replayability.** The P1–P4 commands in the section use removed `/tmp` paths; replay rests on the tracked mutation recipe (`C9-rerun-probes.sh`, SHA-256 above) plus the base fixture, exactly as the section says. The recipe is sufficient: my independent reconstruction reproduced all four blocks byte-for-byte.
- **Next-recheck pointer — ABSENT in the committed tree (named debt).** The check-log records the first periodic re-check but points to no next owner, round, or due point; the only successor language in the watch is the unchanged r91 Owner sentence ("hands it to the next C1 calibration owner at closure", unnamed). The fixtures README's r92 section likewise records the first re-check without a next pointer. This matches CB's pre-integration R3 audit (`.ufo/waves/round-92/CB.md:246`; `CB-audit.json:126`), whose successor probe still returns False at `c4d4823`; the two other R3 watch gaps (the `e97613c` checker hash `e2bb9639…` and the explicit ambiguous-SOURCE wording) also remain absent. The r92 integration did land the re-check and path notes themselves, so only the pointer/naming part of R3 stays open. Recommended at the next authorized watch touch: add an explicit next-recheck pointer (owner + due point) and, per CB R3, pin the e97613c checker hash and the ambiguous-SOURCE wording. Low severity — no drift or ruling implication; no write authority for the watch in this seat.
- **Verdict (C3 calibration, watch re-check): improved (bounded).** The delivered row is accurate against independent observation, the discrimination claim holds, and the artifacts are unchanged from the stated run HEAD to the judgment surface. The missing next-recheck pointer is a named governance gap, not an observed harm to any axis.

## Handoff

- `lore-shokunin/.ufo/waves/round-92/followup/JCAL2.md` — this report.
- `lore-shokunin/.ufo/waves/round-92/followup/JCAL2-receipts.json` — machine-readable receipts (hashes, probe outputs, pointer-check results).
- No commit or push; no tracked writes beyond these two files. `/tmp` scratch removed (no `lore-jcal2-c9-*` remains); pre-existing `/tmp` inode load unchanged.
- Mid-run, sibling follow-up artifacts appeared untracked (`H4-*.json`, `JCAL1-delta.json`, `JCAL3.md`, `JCAL5-delta.json`); they were not used as evidence and did not alter the measurements. The judgment surface remained `c4d4823` throughout.
- Open item for the parent: the next-recheck pointer (and CB's two other R3 watch gaps) need an authorized decision at the next watch touch; nothing in the committed tree schedules the next periodic re-check.