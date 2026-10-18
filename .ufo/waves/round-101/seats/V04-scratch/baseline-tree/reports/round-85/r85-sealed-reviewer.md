# r85 Sealed Reviewer — provenance-mask probe pair

Sealed non-author review. Lane checker: `.shokunin/lore/corpus/fixtures/check_bible.py`
(the copy under `corpus/live/rejected-r4/` is a rejected-run artifact, not the lane
checker). Invoked as `python3 check_bible.py <fixture-dir>` from `corpus/fixtures/`.

## Step 1 — verbatim checker outputs

`probe-inputs/r85-masked-ambiguous/` (exit 1):

```
VIOLATION: entities[5].id: duplicate entities id 'vault'
1 violation(s); no canon changed
```

`probe-inputs/r85-unique-break-control/` (exit 1):

```
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'
1 violation(s); no canon changed
```

## Step 2 — sealed first-repair choices (written before unsealing; unedited)

**masked-ambiguous → first repair: `entities.json`, the `entities[5]` row — the
second `vault` entity.** Delete it outright (it is a byte-for-byte surplus row) or
merge it into the canonical `vault`. Why first: it is the only violation reported,
the checker names index 5 as the surplus, and dedup is a small deterministic edit.
My sealed defect model: exactly one defect in this file.

**unique-break-control → first repair: `entities.json`, `entities[3]` (item `seal`),
`provenance[2].from_holder`: `'harbor'` → `'vault'`.** The checker states the
previous hop ended at `vault`, so the `from_holder` field is the broken link; if
inspection showed the story actually intends harbor→tower custody, I would instead
fix `provenance[1].to_holder` — but the checker's "expected 'vault'" framing makes
`from_holder` the first touch.

## Step 3 — unsealed reassessment

`diff` of the two `entities.json` files: the masked file is the control **plus one
byte-identical second `vault` place row** appended at index 5 (masked lines 82–93).
Both files carry the **same** provenance chain break in `seal` (`entities[3]`):
`provenance[1]` `to_holder: 'vault'` (tick 3) is followed by `provenance[2]`
`from_holder: 'harbor'` (tick 4).

What `check_bible.py` does with duplicated holders:

- L82 — the `duplicate entities id 'vault'` error is emitted in an early pass. This
  is the *only* violation the masked file ever shows.
- L157–159 — `entity_id_counts` counts id occurrences; in the masked file
  `vault` → 2.
- L212–216 — a `to_holder` whose id count is ≠1 sets `valid = False` **silently**
  (count==0 gets a "dangling entity" error; count≥2 gets no message at all).
  `seal`'s `provenance[1]` (`to_holder: 'vault'`) hits this branch.
- L220–224 — the same silent invalidation for `from_holder`.
- L234–237 — any invalid record resets `previous_holder`/`previous_tick` and sets
  `can_check_chain = False`, then `continue`s; the flag is never re-enabled for
  the rest of that item's records.
- L238–243 — the chain-break comparison runs only under `can_check_chain`, so
  `provenance[2]`'s `'harbor'`-vs-`'vault'` break is never even evaluated.
- Corroboration: `relations.json` in the masked fixture has a single `mira→seal`
  row with no `vault` endpoint, so the *voiced* ambiguity error at L167–168
  (`ambiguous entity 'vault'`) never fires. The only consumer of the ambiguity is
  the provenance path — the one that stays silent.

**Did my step-2 first repair target the real defect?** Mechanically yes,
diagnostically no. Removing the duplicate `vault` row is the correct first
*action* under full information too — the chain check cannot run while
`entity_id_counts['vault'] != 1`, so dedup is a prerequisite to even detecting the
break. But the defect this probe pair is built around — the one the control
exposes — is the chain break at `entities[3].provenance[2]`, and the masked output
gave **zero** signal of it. My sealed model ("one defect total, at entities[5]")
was wrong: the file has two defects, and the reported one is the mask, not the
masked.

**Did the masked output change a mistaken action?** No — and that is the subtler
finding. Under both information states my first physical edit is the same (dedup
`vault`), so the mask did not redirect my first move. What it changed was the
*stopping point*: trusting the single-violation output, I would have deleted the
row and considered the file clean — shipping a corpus still containing the
injected chain break. The mask is recoverable only by re-running the checker
after dedup (the break then surfaces verbatim, as in the control). So the output
did not lead me to a wrong first action; it led me to a correct first action with
a false sense of finality. The silent-invalidation design (L215–216, L223–224) is
the mechanism: an ambiguous holder produces no finding of its own inside
provenance, it just turns the chain check off.

## UNKNOWNs

- Author intent was not consulted (`probe-r85-*.txt`, `manifest.txt`,
  `reports/round-85/r85-author.md` all unread per the seal); that the pair was
  *designed* to demonstrate this masking is inferred from fixture names plus the
  code path, not stated by the author.
- Whether the lane's repair protocol mandates a checker re-run after each fix —
  I ran one pass per dir as instructed. Single-pass trust is what makes the mask
  dangerous; iterative re-check neutralizes it.
- The `rejected-r4` copy of `check_bible.py` was not diffed against the fixtures
  copy; assumed stale by directory name alone.
- Whether deleting `entities[5]` vs `entities[4]` (the first `vault`) has any
  downstream difference — they are byte-identical, so none is expected, but no
  re-run after a hypothetical fix was performed.
- Behavior of the same mask through `from_holder` ambiguity (L220–224) rather
  than `to_holder` — symmetric in code, not exercised by this fixture pair.
