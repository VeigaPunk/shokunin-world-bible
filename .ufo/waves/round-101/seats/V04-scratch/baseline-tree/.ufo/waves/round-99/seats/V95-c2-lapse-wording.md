# V95 — c2-lapse-wording (round 99)

Seat: **V95 c2-lapse-wording** — verifier. Mandate: quote every sentence of the lapse excerpt section; classify each as clerk-record vs world-assertion vs editorial; flag any sentence exceeding the clerk-record class.

Baseline: r98 closure `4265df5`. Working-tree HEAD at verification: `337f0fa` (wave tree uncommitted; not used as the byte source). All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report (absolute path) and `.ufo/waves/round-99/seats/V95-scratch/` (`poll.sh`, `poll.log`) only. No producer-owned file was written by this seat.

Classified artifact: `corpus/fixtures/r99-window-lapse/fictional-excerpts.md` lines 66–76, the span S4's map names as the appended lapse section (`claim-excerpt-map.md:18`, `:42`, `:69`). Quoted sentences below are the period-terminated units in that span. The heading on line 66 is not a sentence and is not classified. Blockquote markers (`> `) are markdown, not part of the sentence; the raw lines are quoted in section 2.

## 0. Poll-wait record (SELF subtracted; bounded stall-escape)

Poller `V95-scratch/poll.sh` (20 s cadence, logged to `V95-scratch/poll.log`). Success condition was the lapse section plus the r99 README/map plus both S5 knowledge notes plus S3/S4/S5 reports. SELF (this report) was never waited on.

- try 1 `2026-10-17T22:04:38-03:00` through try 15 `2026-10-17T22:09:18-03:00`: `fx=1 lapse=1 map=1 readme=1 know=0 S3=1 S4=1 S5=0`. The lapse section, the rewritten map, the rewritten README, and `S3-fixture-author.md` / `S4-fixture-docs.md` were present on every try. `corpus/knowledge/r99-lapse-scope-note.md` and `corpus/knowledge/r99-gate-blind-spot-table.md` were absent on every try. No S5 report.
- The poller was killed by the tool timeout at 300 s after try 15. It did not reach try 40 and did not print `ALL PRESENT` or `ABSENT after 40`.
- **Bounded stall-escape (recorded, not fatal):** this seat classifies the lapse excerpt, which S3 owns. That file's sha256 stayed `fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d` (5114 bytes, mtime `2026-10-17 22:01:13 -0300`) from the first read through a recheck at `2026-10-17T22:17:10-03:00`. S3's report was present from 22:01; S4's report from 22:03. S5 does not own the excerpt. Waiting out the remaining tries for S5's knowledge notes would not change the sentences classified here. S5's notes were still absent at the recheck (`ls corpus/knowledge/r99-*` → `No such file or directory`). They were not an input to the classification. This is not a verification of a plan: the section below is the delivered file.

## 1. Class criteria (operational; applied to every sentence)

Taken from the r99 declaration (LOG.md lines 3225–3232: a clerk lapse record; no resolution, no blame, no reconciliation asserted anywhere) and from the r98 clerk-filing precedent, whose quoted note is first-person recording speech throughout. Not taken from an r99 scope note (absent; section 0).

- **clerk-record:** the grammatical subject is the clerk (first person, or the clerk named as speaker) and the main verb is a recording or speech-act verb (`record`, `file`, `assert`, `assign`, `reach`, `reconcile`) or an explicit first-person denial of such an act. The sentence says what the record says. It does not state what the world did.
- **world-assertion:** an indicative statement of a world state (window closed, agreement unfulfilled, claim lodged or not, matter standing as a historical entry) with no recording verb and no first-person clerk subject.
- **editorial:** fixture-author metadata or scope prose outside the blockquote, or a gloss that tells the reader what the section means.

A sentence **exceeds the clerk-record class** if it is world-assertion or editorial. Editorial framing in the same slots as r98 (attribution line, scope line) is flagged as class-exceeding but is the delivery frame, not the in-world defect. An in-world quoted sentence that is not clerk-record is the defect this seat exists to catch.

r98 control, same file shape, quoted lines only (`corpus/fixtures/r98-clerk-filing/fictional-excerpts.md:59-62`):

- "Tick 14: I filed both pending accounts at the Chalk Stair registry." — clerk-record (`I filed`).
- "I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN." — clerk-record (`I am` / `I record`).
- "I assert no finding." — clerk-record.
- "I reach no verdict and reconcile nothing." — clerk-record.

All four r98 quoted sentences have a first-person subject and a recording or limit verb. That is the class the r99 lapse note was measured against.

## 2. Raw section (observed)

```
$ sha256sum corpus/fixtures/r99-window-lapse/fictional-excerpts.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
```

Recheck at `2026-10-17T22:17:10-03:00`: same digest, 5114 bytes, mtime `2026-10-17 22:01:13.842835114 -0300`. `python3` print of lines 66–76 (`repr`):

```
66  '## Round 99 lapse note (2026-10-17)'
67  ''
68  'Newly authored fictional first-person note, attributed to in-world source ID `clerk-lapse-note`, folio 9, lines 1–5. This section is appended after the preserved r98 text above; the inherited wording is unchanged.'
69  ''
70  '> Tick 15: The crossing-window named in the original minute has closed.'
71  '> The agreement was unfulfilled.'
72  '> No claim was lodged.'
73  '> The matter stands as a historical open entry.'
74  '> I record no resolution, assign no blame, and reconcile nothing.'
75  ''
76  "Scope: this appended section is the clerk's first-person lapse record. It records that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry. It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; the crossing-scoped agreement above is unchanged, and the matter stays open."
```

Token counts inside lines 66–76 only: `'I '` = 1, `'I record'` = 1, `'Maren'` = 0, `'clerk'` = 2 (both in the editorial scope line, not in the quote), `'unfulfilled'` = 2, `'historical'` = 2, `'blame'` = 2, `'resolution'` = 2, `'reconcil'` = 2, `'closed'` = 2, `'lodged'` = 2, `'first-person'` = 2. The single `I` is line 74.

Per quoted line, first-person scan (`\bI\b` on the prose after stripping `> `):

```
70 no_first_person 'Tick 15: The crossing-window named in the original minute has closed.'
71 no_first_person 'The agreement was unfulfilled.'
72 no_first_person 'No claim was lodged.'
73 no_first_person 'The matter stands as a historical open entry.'
74 first_person 'I record no resolution, assign no blame, and reconcile nothing.'
```

## 3. Every sentence, quoted and classified

Ten orthographic sentences (split on `.`). Semicolon-joined clauses are noted inside the sentence they belong to, not split into extra sentences.

1. **Line 68.** "Newly authored fictional first-person note, attributed to in-world source ID `clerk-lapse-note`, folio 9, lines 1–5."
   - **editorial.** Fixture attribution. Not clerk speech.
   - **Exceeds clerk-record** (delivery frame, same slot as r98 line 57). Additional overclaim: it calls the note first-person, but four of the five quoted sentences have no first person (section 2). The folio line-count "1–5" matches the five blockquote lines; that part is accurate.

2. **Line 68.** "This section is appended after the preserved r98 text above; the inherited wording is unchanged."
   - **editorial.** Both clauses (append notice; inherited-wording notice) are fixture-author metadata.
   - **Exceeds clerk-record** as delivery frame only. Not an in-world defect.

3. **Line 70.** "Tick 15: The crossing-window named in the original minute has closed."
   - **world-assertion.** Indicative perfect of a world event. No clerk subject, no recording verb. The `Tick 15:` token is an editorial tick label inside the sentence (same pattern as r98's `Tick 14:`), but r98's sentence stays clerk-record because of `I filed`. This one does not.
   - **Exceeds clerk-record.** Flag.

4. **Line 71.** "The agreement was unfulfilled."
   - **world-assertion.** Impersonal past. States non-performance as fact. No speaker, no recording verb.
   - **Exceeds clerk-record.** Flag. This is the strongest exceedance: it is a performance finding. It names no person, so it is not a named-blame sentence, but "unfulfilled" judges the agreement. Line 74's "assign no blame" does not retract it.

5. **Line 72.** "No claim was lodged."
   - **world-assertion.** Impersonal passive absence. A clerk could know a negative registry entry, but the sentence does not say "I record that no claim was entered." No speaker, no recording verb.
   - **Exceeds clerk-record.** Flag. Borderline on content (a negative entry is the sort of thing a clerk records); not borderline on grammar. Classified by the criteria in section 1, not by what a clerk could have meant.

6. **Line 73.** "The matter stands as a historical open entry."
   - **world-assertion.** "stands as" asserts a status. "historical" asserts external historicity. No recording verb, no first person.
   - **Exceeds clerk-record.** Flag. See the reliability-note contradiction in section 4.

7. **Line 74.** "I record no resolution, assign no blame, and reconcile nothing."
   - **clerk-record.** Subject `I` covers all three coordinated predicates (`record`, `assign`, `reconcile`). Each is a first-person limit, the same shape as r98's "I assert no finding" / "I reach no verdict and reconcile nothing."
   - **Does not exceed.** It does not retract sentences 3–6. It denies resolution, blame, and reconciliation; it does not reframe the window, the agreement, the claim, or the "historical" entry as entries rather than world facts.

8. **Line 76.** "Scope: this appended section is the clerk's first-person lapse record."
   - **editorial.** Class label written by the fixture author.
   - **Exceeds clerk-record** as scope frame. Additional overclaim: "first-person" is false of sentences 3–6 (section 2). Calling the section a lapse record does not make those four sentences clerk-record.

9. **Line 76.** "It records that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry."
   - **editorial.** Authorial gloss. "It records that" tries to pull sentences 3–6 back into a record. The quoted note does not use a recording verb for those four propositions. The gloss endorses them as the content of the record; it does not repair their grammar.
   - **Exceeds clerk-record.** Flag as an endorsement of the exceedance, not as a repair.

10. **Line 76.** "It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; the crossing-scoped agreement above is unchanged, and the matter stays open."
    - **editorial.** One orthographic sentence. Three independent stretches: the denial ("It asserts no resolution, no blame, and no reconciliation, and it creates no new duty"); "the crossing-scoped agreement above is unchanged"; "the matter stays open."
    - **Exceeds clerk-record** as scope frame, same slot as r98 line 64. "the matter stays open" matches the declaration's open-entry bound, but it is the author's sentence, not the clerk's. It does not repair sentences 3–6.

Heading, not a sentence: `## Round 99 lapse note (2026-10-17)` (line 66).

## 4. Flags (sentences that exceed clerk-record)

**In-world defect (quoted note, lines 70–73) — sentences 3, 4, 5, 6:**

| # | Quoted sentence | Class | Why it exceeds |
|---|---|---|---|
| 3 | The crossing-window named in the original minute has closed. | world-assertion | Window closure stated as fact, not as an entry the clerk records. |
| 4 | The agreement was unfulfilled. | world-assertion | Performance finding. Blame-adjacent. Not retracted by sentence 7. |
| 5 | No claim was lodged. | world-assertion | Impersonal absence, not a recorded negative entry. |
| 6 | The matter stands as a historical open entry. | world-assertion | Status plus external historicity. Contradicts the source reliability note (below). |

**Within the quoted note, only sentence 7 is clerk-record.**

**Editorial exceedances (expected frame, still not clerk-record):** sentences 1, 2, 8, 9, 10. Sentences 1 and 8 additionally mislabel the note as first-person. Sentence 9 endorses the four world-assertions as what the section records.

**Adjacent restatements are not part of the excerpt section and do not repair it.** Recorded so they are not mistaken for a fix:

- `timeline.json` event `clerk-lapse-recorded` description: "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry." The recording verb is in the JSON description, not in the quote.
- `sources.json` `clerk-lapse-note` reliability note: "Newly authored fictional note; the clerk reports that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry. It asserts no resolution, no blame, and no reconciliation; it is not evidence of a breach finding, a continuing duty, a winner between the accounts, or an external historical fact." The note denies external historical fact in the same source whose excerpt calls the entry "historical." That is an internal wording contradiction, not a class repair.
- `README.md:11` and `claim-excerpt-map.md:69` restate the same four world facts as the lapse bound. S4's report (line 119) says the J21 paragraph is an authored reading and that a verifier should re-read the section against it. This re-read is that check: the reading says the clerk records those facts; the quoted sentences 3–6 do not.

S3's report says the quoted note "asserts no resolution, assigns no blame, and reconciles nothing" and that those denials "are negations, not positive assertions of resolution, blame, reconciliation, or a new duty." That is true of sentence 7 and of the scope denials. It does not cover sentences 3–6. "The agreement was unfulfilled" is a positive assertion. "historical" is a positive assertion. S3's "first-person note" label matches sentences 1 and 8 and does not match sentences 3–6.

The declaration's topics are present (window closed per the minute, agreement unfulfilled, no claim lodged, matter open, no resolution/blame/reconciliation in the denial sentence). Presence of the topics is not the clerk-record class. Four of the five in-world sentences assert those topics as world facts.

No checker was re-run. `support_check` / `map_obligations` do not read this classification; S4's lexical PASS on J21 (anchor found at line 70) is not evidence that line 70 is clerk-record.

## 5. Non-claims

I did not judge canon, rights, chronology truth, or whether the window in fact closed. I did not treat S5's absent scope note as a delivered class definition. I did not edit the excerpt, the map, the README, or any JSON file. Census, freeze pins, and the blind-spot table were not this seat's measurement.

## Bottom line

FAIL — four of the five in-world sentences in the lapse excerpt section (lines 70–73) are world-assertions and exceed the clerk-record class; only line 74 is clerk-record.
