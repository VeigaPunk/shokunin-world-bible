# Round 10 source/claim scout

## Scope and observations

Read `.shokunin/lore/LOG.md` Round 10 declaration and the existing clean fixture files `.shokunin/lore/corpus/fixtures/consistent/{sources,entities,relations,timeline}.json`, plus checker `.shokunin/lore/corpus/fixtures/check_bible.py`. No source-excerpt text file exists in the observed fixture tree yet. I made no fixture or checker changes.

- `sources.json` describes `courier-log` as a fictional first-person personal log and `archive-ledger` as a fictional municipal record that records movements, “not omniscient truth.” Neither entry contains excerpt wording.
- `entities.json` attributes Mira's “Mira carried the blue seal” claim to `courier-log`; Harbor's registry and North Tower's watch bell claims to `archive-ledger`; and the seal's accompaniment claim to `courier-log`.
- `relations.json` cites Mira `carries` seal to `courier-log`.
- `timeline.json` cites Mira's departure from Harbor at tick 1 and arrival at North Tower at tick 2 to `courier-log`; arrival depends on departure.
- The checker verifies source IDs are present/unique and structural constraints. Its source-ID checks do not read or compare excerpt text. Thus these current rows are cited, not textually substantiated by this checker. Source metadata's reliability note is a declared limitation, not proof that a record is accurate.

## Proposed excerpt and mapping (recommendation, not observed canon)

Use a fictional, compact entry explicitly signed in-world, with date/tick aligned to departure. For example, append this text as a clearly labeled invented excerpt for `archive-ledger`:

> **Lantern Harbor Registry, year 12, Tide 3, first bell — entry signed “Iven, Registry clerk”**
> “Iven: I saw courier Mira leave Lantern Harbor by the east gate at first bell. I entered her departure in this registry.”

This gives a reader a direct textual comparison for a second perspective. Recommended claim-to-text mapping:

| Proposed bible assertion | Source and exact excerpt support | Limit |
|---|---|---|
| `iven` is a registry clerk (new entity claim, e.g. “Iven signed this registry entry as clerk.”) | `archive-ledger`, heading “entry signed ‘Iven, Registry clerk’”; first-person signature “Iven” | Shows what the invented record attributes to its signer; not independent proof of a real identity. |
| Mira departed Lantern Harbor at first bell via east gate (existing departure event, if adding detail) | `archive-ledger`, sentence 1: “I saw courier Mira leave Lantern Harbor by the east gate at first bell.” | A report of an observation, not an omniscient guarantee. Keep existing `courier-log` citation as the other account rather than treating this as truth adjudication. |
| Iven witnessed Mira's departure (new `witnessed_departure` relation from `iven` to `mira`) | Same sentence's “I saw … leave”; attribution “Iven” in the entry heading identifies the first-person speaker within the fiction | It supports the relation as the record's assertion. It does not prove the witness was honest or the event occurred. |
| Iven entered a record of the departure (optional new event for Iven, if needed to meet event expansion) | Sentence 2: “I entered her departure in this registry.” | Supports the act of recording, not Mira's departure independently. Cite the event to `archive-ledger`; do not misdescribe it as a second departure. |

A simpler shape avoids unnecessary event/entity proliferation: introduce `iven`, one claim that the entry is signed by a registry clerk, and a `witnessed_departure` relation; cite both to `archive-ledger`, while retaining the existing Mira departure event and `courier-log` citation. If an actual second timeline row is required, make it Iven's contemporaneous recording action (tick 1), not a duplicate Mira-departure event that risks pretending two accounts are separate events. Ensure the new record's invented-text label is visible to readers and its source ID is present in `sources.json`.

## Authorship, identity, and truth are separate

1. **Authorship/attribution:** The proposed signature lets the excerpt attribute words to “Iven” inside the fictional document. The source file's actual author is the project author, who invented both the document and its speaker. Do not present Iven as the real-world author or as an independently verified witness.
2. **Identity:** A signed title can support the in-world claim “the record identifies its signer as Iven, Registry clerk.” It does not establish a unique historical person, legal identity, or even that the signer held the stated office beyond the fiction's own assertion. Avoid using an unsupported identity claim as corroboration for itself.
3. **Truth:** The prose is intentionally invented. It makes the correspondence legible and offers an in-world second account; it cannot establish external historical truth. The existing reliability note correctly limits the ledger to recording movements rather than omniscient truth. The checker only validates structured references and does not assess authorship, witness credibility, textual entailment, or whether the narrated event is true.

These are recommendations for the executor and later non-author review, not claims that the excerpt or proposed Iven rows already exist. A reviewer can compare each quoted sentence against the exact assertion and flag overreach (especially turning “I entered her departure” into proof of departure).
