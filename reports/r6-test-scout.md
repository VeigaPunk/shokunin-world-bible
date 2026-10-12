# Round 6 test scout: raw CLI replay and bounded negative probes

## Observed repository behavior

- `.shokunin/lore/corpus/fixtures/check_bible.py` loads five required arrays in `FIELDS`: `sources`, `entities`, `relations`, `timeline`, `contradictions`. Its CLI takes one bible directory and prints `CLEAN`/exit 0 or `VIOLATION` rows/exit 1. It currently has no transfer table or item holder validation.
- Raw baseline replay from the repository root:
  - `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` → exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`.
  - `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions` → exit 1, three existing findings: dangling `missing-map`, timeline inversion, and double-booked `mira`.
  These exact outputs are recorded in `.shokunin/lore/corpus/live/runs/20261012T164316Z/consistent.txt` and `contradictions.txt`.
- The clean fixture's `seal` entity (`corpus/fixtures/consistent/entities.json`) has a cited claim that it accompanied Mira; its `relations.json` has a `carries` relation. The checker does not turn either into a transfer history. `corpus/fixtures/README.md` likewise says citations are in-world records and do not verify truth.

## Recommended raw CLI replay matrix (not run; implementation/fixtures not present yet)

Run each command from the repository root, capture stdout, stderr, and exit status separately, and compare baseline diagnostics byte-for-byte where noted. Proposed fixture names are illustrative; align them with the committed round-6 fixture names if they differ.

| Case | Command suffix | Expected result / purpose |
|---|---|---|
| Existing clean control | `consistent` | Exit 0; exact existing clean output. Proves an absent optional transfer table does not invalidate an unrelated old bible. |
| Existing contradiction regression | `contradictions` | Exit 1; same three pre-existing diagnostics, no new transfer diagnostic. |
| Explicit valid two-record chain | `r6-transfer-valid` | Exit 0. Two cited transfers for one item where the second `from_holder` equals the first `to_holder`; verifies accepted continuity. |
| Explicit broken predecessor | `r6-transfer-broken` | Exit 1 with a local chain-break diagnostic at the later transfer. Change only that later `from_holder` from the valid case; retain all citations and other fields. |
| No transfer assertions | `r6-transfer-absent` (or use `consistent`) | Exit 0 with no provenance finding. Absence is not evidence of a broken chain and must not make transfer records mandatory. |

For each proposed round-6 pair, retain raw JSON fixtures and record the exact command, exit code, stdout, and stderr. If possible, derive `r6-transfer-broken` by changing exactly one holder field from `r6-transfer-valid`; avoid unrelated schema edits that obscure the tested boundary. Check that the checker does not modify fixtures (e.g. compare input hashes before/after).

## Recommended negative boundary probes (bounded, not exhaustive)

These test narrowly stated validation boundaries, rather than purporting to validate all possible provenance semantics:

1. **No inferred history:** use the existing clean bible unchanged, with no transfer records. It should pass; do not infer a prior holder from `seal.first_appearance`, the “accompanied Mira” claim, the `carries` relation, timeline prose, or gameplay.
2. **Missing citation on an otherwise valid transfer:** remove/blank one transfer's `source_id`. Expect the ordinary required-field or unknown-source error at that row, not a chain-break verdict. This checks required citation shape only, not source support.
3. **Unknown item or holder reference:** make one record refer to a nonexistent item (and, separately if budget permits, holder). Expect a local dangling-reference error; do not reinterpret it as evidence of a different chain. Skip or qualify this probe if the chosen schema deliberately does not expose separate holder/entity references.
4. **Non-item entity used as item:** substitute an existing character ID for `item_id`. Expect a kind-boundary error if the schema defines `item_id` as an item entity. This is a schema/reference check, not provenance proof.

The transfer table's exact field names and whether it includes explicit acquisition records are not yet established by active checker evidence. Do not assert test outcomes for these proposed negative probes until a concrete schema is implemented. In particular, a first transfer's `from_holder` cannot be proven to be the true prior holder without a cited acquisition/seed convention; at most, a transfer-only sequence can check continuity between listed records. The round's claim requires cited acquisition/previous-transfer grounding, so resolve this design boundary before treating a valid fixture as proof of a complete chain.

## Interpretation limits

A passing replay would establish only that the tested explicit records satisfy the implemented narrow convention. It would not establish complete item provenance, source reliability or truth, custody between recorded ticks, or any event inferred from prose/gameplay. The probe list is intentionally small and is not exhaustive of malformed schemas, duplicate records, equal ticks, conflicting citations, or all provenance edge cases.
