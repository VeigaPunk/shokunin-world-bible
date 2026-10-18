import os
checks = [
 ("corpus/fixtures/r96-crossing-response/sources.json", 27, '"id": "evin-response-note"'),
 ("corpus/fixtures/r96-crossing-response/sources.json", 30, 'It asserts no accusation against Aru, selects no winner'),
 ("corpus/fixtures/r96-crossing-response/timeline.json", 44, '"id": "response-evin-salt-court"'),
 ("corpus/fixtures/r96-crossing-response/timeline.json", 45, '"tick": 12'),
 ("corpus/fixtures/r96-crossing-response/timeline.json", 49, '"aftermath-missing-evin"'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 37, 'Tick 12: I was at Salt Court through the same agreed bell.'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 38, 'I make no accusation against Aru.'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 39, 'I select no winner between our two accounts.'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 40, 'Both accounts stand unresolved.'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 33, '## Round 96 response note'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 42, 'Scope: this appended section is Evin'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 26, 'Tick 11: I waited at the Chalk Stair through the agreed bell.'),
 ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 19, 'for this crossing only'),
 ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 37, 'J16'),
 ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 37, '`timeline.json#/4`'),
 ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 54, "J16's anchor is the tick-12 response sentence (line 37)"),
 ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 5, '**Expected inventory:** 16 JSON facts'),
 ("corpus/fixtures/r96-crossing-response/README.md", 3, '5 entities / 1 relation / 5 events / 5 sources'),
 ("corpus/fixtures/r96-crossing-response/README.md", 11, 'no contradiction is asserted'),
 ("corpus/fixtures/r96-crossing-response/README.md", 21, '16 source-attributed JSON pointer obligations'),
 ("corpus/fixtures/r95-crossing-aftermath/sources.json", 21, '"id": "aru-aftermath-note"'),
 ("corpus/fixtures/r95-crossing-aftermath/timeline.json", 33, '"id": "aftermath-missing-evin"'),
 ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 22, '## Round 95 aftermath note'),
 ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 27, 'Evin did not come.'),
 ("corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md", 36, 'J15'),
 ("corpus/fixtures/README.md", 746, '## Round 35: two cited reports, one unresolved Bell-7 conflict'),
 ("corpus/fixtures/README.md", 761, 'Neither wins.'),
 ("corpus/fixtures/README.md", 1177, '## Round 95'),
 ("corpus/knowledge/2026-10-12-lore-decision-table.md", 226, '## Round 23 — witnessed-absence note class'),
 ("corpus/knowledge/r95-aftermath-scope-note.md", 5, '# Reported non-performance against a crossing-scoped agreement — round 95'),
 ("corpus/fixtures/r35-bell7-conflict/contradictions.json", 3, '"id": "bell7-location-reports"'),
 ("corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md", 3, 'Both authored excerpts are fictional reports'),
]
bad=0
for path,ln,frag in checks:
    if not os.path.exists(path):
        print("MISSING-FILE", path); bad+=1; continue
    lines=open(path,encoding='utf-8').read().split("\n")
    ok = ln-1 < len(lines) and frag in lines[ln-1]
    print(("OK   " if ok else "FAIL "), f"{path}:{ln}", "|", repr(frag[:40]))
    if not ok:
        bad+=1
        print("      actual:", repr(lines[ln-1][:120]) if ln-1 < len(lines) else "<EOF>")
print("BAD:", bad)
