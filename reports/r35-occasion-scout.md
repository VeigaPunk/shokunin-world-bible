# Round 35 occasion scout — shared named bell

## Evidence and precedent
- `.shokunin/lore/LOG.md:549` requires two accounts expressly tied to the same named bell, with a Sella event at Tower and a two-sided unresolved ledger; it says not to infer checker-proven semantic conflict.
- `.shokunin/lore/LOG.md:139-144` records the r10 warning that “first bell” does not establish numeric tick 1, synchronization, exact simultaneity, or within-tick order. Equal fixture ticks are local sequence labels, not a conversion from bell language.
- `.shokunin/lore/reports/r33-clause-scout.md:15-24` says a witness's “saw” is a reported perception, not independent confirmation, and forbids synchronizing its tick with another account absent text.
- `.shokunin/lore/reports/r3-ledger-scout.md:13-29` recommends pointers to cited existing records and a `why` that explains the conflict without verdict; the ledger is editorial, not canon selection.

## Proposed shared wording (newly authored fictional excerpts)
Use the exact shared occasion phrase **“at the sounding of the third bell”** in both speakers' accounts. Tarin's line can be:

> I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk at the sounding of the third bell.

Sella's independent-in-fiction first-person line can be:

> I, Sella, was at North Tower, not Lantern Harbor, at the sounding of the third bell.

The shared named phrase supports an explicit same-occasion claim at the level of what these two reports say. It does not establish a universally synchronized bell, a clock time, duration, ordering within the sounding, or objective simultaneity. Keep each report attributed to its speaker; retain both without selecting truth. The r35 shared fixture tick is only a local representation choice, not evidence that bell number maps to tick number.

## Ledger wording and caveats
Point `claim_a` to Tarin's event `place_id` and `claim_b` to Sella's event `place_id` (using the repository's established `timeline#<id>.place_id` pointer form). `why` should state that Tarin reports Sella at Lantern Harbor and Sella reports herself at North Tower **at the sounding of the third bell**, conditional on the editorial alignments of the named speakers and places. This is an apparent incompatible location pair under that shared-occasion reading, not a finding by the structural checker and not a verdict about either account. Preserve both source citations and both event rows.

Avoid formulations such as “simultaneously,” “at exactly the same time,” “third bell = tick 3,” or “proved contradiction.” “Same named bell occasion as each account states it” is the bounded claim. Do not infer the bell was audible at both locations, that either narrator heard it, any travel feasibility, or which account is mistaken. Tarin's envelope remains only unlabeled paper envelope; no contents, recipient, owner, Blue Seal/carbon/strip association, or motive.

## Risks
1. A shared phrase can be mistaken for external timekeeping. Treat “third bell” as fictional wording in both accounts, not an established synchronized signal.
2. “At the sounding” gives an occasion, not precision within that occasion. It cannot order placement relative to Sella's arrival or other events.
3. The names and place IDs are editorial alignments; wording should not imply independent identity verification.
4. Ledger `why` could silently promote two reported claims into world facts. Retain “Tarin reports” and “Sella reports,” and state assumptions explicitly.
5. The checker validates pointer structure, not whether the prose entails a conflict or whether either source is reliable.

## Falsifiable check
A non-author reviewer should inspect both exact excerpts, event rows, citations, and ledger pointers. The proposal passes only if both excerpts literally use the identical “at the sounding of the third bell” phrase; Tarin's sentence reports seeing Sella at Harbor, Sella's sentence explicitly places herself at Tower and says “not Lantern Harbor”; both accounts remain attributed and the ledger points to the two corresponding `place_id` fields while preserving both claims. It fails if the phrase differs, a location/identity is not stated, either claim is converted to fact, tick 3 is described as the bell's numeric time, or the ledger chooses a winner. A checker exit 0 alone cannot establish this semantic check.
