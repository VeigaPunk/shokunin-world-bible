# Round 42 scribe — selector versus prose decision table

## Decision

**No-go on a calibration claim from this candidate.** The useful boundary is real, but it is not new: Round 3 already specified that ledger references select only `place_id`, `tick`, or `depends_on`, and explicitly said the checker does not prove `why` (fixtures/README.md:43-54; LOG.md:33-41). The README also says citations validate pointers and required text, not whether `why` explains a semantic contradiction (fixtures/README.md:48-54). A fresh `description` negative would re-execute an already-tested unsupported-field rejection, not establish new behavior or materially new calibration.

| Input / question | Decision | Evidence and boundary |
|---|---|---|
| `claim_a.field` is `place_id`, `tick`, or `depends_on` | Permitted ledger selector, subject to event/source pointer checks | Checker allowlist at `check_bible.py:76-90`; README:48-52. This is a structural reference, not proof that the selected assertion is true or contradictory. |
| `claim_a.field` is `description` | Rejected as an unsupported ledger selector | `description` is a required timeline event string (`check_bible.py:12-14`), but it is not in the allowlist (`:76-90`). Round 3 already documented allowed fields and malformed ledger pointers (`LOG.md:34-40`; README:48-54), and its reviewer reportedly tested an unsupported field (LOG.md:700). The rejection says nothing about whether the prose is useful or true. |
| Event `description` text | Free-form, attributed report text available to human reading; not a ledger-selected assertion under this schema | Timeline shape includes `description` (`check_bible.py:12-14`); the ledger selector list is narrower (`:76-90`). README says the checker validates pointers, not semantic conflict (`fixtures/README.md:53-54`). |
| `contradictions[i].why` | Required nonempty editorial rationale; its semantic adequacy is not checked | Required string shape (`check_bible.py:14`, `:39-43`); README explicitly disclaims validation of whether `why` accurately explains a semantic contradiction (`fixtures/README.md:53-54`). |
| Human asks whether two selected reports semantically conflict | Manual, conditional interpretation; not determined by selector validity or clean checker output | R35 describes the conflict as conditional on identity/place/occasion assumptions and says neither account wins (`fixtures/README.md:746-771`). The reference ledger separates fictional canon from method citations (`reference-ledger.md:1-11`). |

## Risks / limits

- Calling `description` a “free-text field” must not imply it is excluded from timeline records: it is part of their required shape. It is only excluded as a contradiction-ledger selector.
- Do not infer that an unsupported selector makes the underlying event description false, useless, or forbidden. Do not infer that an accepted pointer establishes a semantic contradiction.
- Do not claim this is new coverage: the allowlist rejection is explicit in Round 3 documentation, and LOG round 42 states the r3 reviewer already probed unsupported fields (LOG.md:700-701).
- `why` remains editorial free text; neither its nonemptiness nor selector validity authenticates sources, proves source support, or decides canon (README:53-54; reference-ledger.md:9-11).

## Falsifiable check

A minimal audit can clone `r35-bell7-conflict` twice and change only `contradictions[0].claim_a.field` in the negative from `place_id` to `description`. Run the checker on both with the documented command (`fixtures/README.md:3-8`, and the r35 command at `:763-771`). The control should retain its baseline result; the negative should report `contradictions[0].claim_a.field: expected one of ...` before event/source dereference, while `claim_b` remains unchanged. Compare all other files byte-for-byte. If the negative is accepted, crashes, or gives a different diagnostic/order, this prediction fails. A successful result merely reconfirms the documented guard; it does not justify a new calibration claim absent evidence that r3's prior probe/documentation was insufficient.
