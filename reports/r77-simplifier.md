# Round 77 simplifier — minimal Neri report and clause map

## Recommendation: design GO; depth remains unproven

The smallest candidate matching the declaration is one short, newly authored fictional account, one new source row, and one claim on a new `neri` character in an r73 fixture clone. No event, timeline tick, place/entity link, relation, contradiction, or comparison that connects Neri to Vela or Jorin is needed.

> I, Neri, tended a gate. Its latch caught only after I lifted it twice.

This is proposed fiction, not a recovered or authenticated record. It attributes both the claimed activity and latch behavior to Neri; it does not establish that Neri, the gate, the latch, or the reported incident exists in any prior material. “A gate” deliberately leaves its identity and location unspecified. Do not call it the east gate, equate it with a notice-bearing gate or any other gate, assign a watch/time/place, or link it to “CLEAR,” “OPEN,” Bell-7, or the registry. The account supplies no cause for the latch behavior and no claim about a notice, order, compliance, or what the latch means for access.

### Minimal fixture mapping (proposal only)

Clone the delivered `r73-jorin-slate-claim` fixture. Append a clearly labeled newly authored, fictional, unverified source row (proposed ID `neri-gate-note`, `sources.json` `/8`) and a new character row `neri` with one claim (proposed `entities.json` `/8`, `/8/claims/0`) citing that source. Example claim wording: “Neri reports tending a gate and reports that its latch caught only after Neri lifted it twice.” The source pointer attributes the statement; it does not corroborate or authenticate it. Add a clause map only if implementing the candidate; no checker change is needed for this account.

| Exact excerpt span | Proposed alignment | Limit |
|---|---|---|
| “I, Neri” | New `neri` character row and the attribution in its cited claim. | Self-identification in invented fiction; not identity or role verification. |
| “tended a gate” | Same attributed claim. | Does not identify a location, gate object, employer, watch, date, or relation to another account. |
| “Its latch caught only after I lifted it twice.” | Same claim, preserving the report as Neri’s account. | Does not establish actual gate condition, cause, duration, repair, access outcome, or any connection to a notice or order. |
| Proposed source `neri-gate-note` | `sources.json` `/8`; cite from `entities.json` `/8/claims/0/source_id`. | New fictional attribution only; not independent evidence. |

## What is new, and the material editorial question

The delivered r73 Jorin account says he was sent to copy a gate notice and read “KEEP THE EAST GATE OPEN” on a slate at the east steps; its claim is `r73-jorin-slate-claim/entities.json` `/7/claims/1`, citing source `/7`. Vela’s r72 report gives “KEEP THE EAST GATE CLEAR” (`r72-vela-slate-claim/vela-slate-note-excerpt.md`; claim `/6/claims/1`, source `/6`). These are attributed, unverified reports, not authenticated wording or evidence of one slate, one gate, or a shared occasion. R74’s table gives only conditional future evidence questions about possible surface identity, readings, and report accuracy; it does not supply gate-operability evidence.

The sole new content in the proposal is Neri’s invented, first-person latch-handling account. The distinct editorial question is whether a practical, embodied gate-tending detail gives a useful character/setting perspective beyond the existing slate-reading and notice-copying reports. It is an editorial judgment about the usefulness of a fictional perspective—not a factual question answerable from these excerpts, and not a claim that latch condition explains either notice. The detail is deliberately small and non-causal, but its usefulness is not demonstrated by the source material. A non-author reviewer should reject the depth move if it reads as arbitrary color, merely repeats “gate” vocabulary, or invites readers to connect latch behavior to the notices despite the missing identity/time/link evidence.

**GO/NO-GO:** GO only for this minimal, explicitly fictional design as a candidate to review; **NO-GO on claiming a depth gain now**. Existing citations establish the prior reports and their limits, not Neri or the latch detail. Depth requires independent review to find the added perspective materially useful; a new source ID and claim pointer cannot supply that evidence. Coverage is not targeted by this move; calibration must not be harmed by treating invented attribution as corroboration or world fact. No corpus/LOG edit, candidate, test, commit, push, or merge is made in this report. No source truth, canon, rights, mechanics, shared occasion, chronology, or common object is inferred.

Scope: this report only.
