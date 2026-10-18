#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
echo "=== A. LANE GIT STATUS BUCKETED ==="
git status --porcelain=v1 | sort > /tmp/v12-status.txt
echo "-- tracked modifications (M in col1-2) --"
grep -E '^ ?[MDARC]' /tmp/v12-status.txt || echo "(none)"
echo "-- untracked (??) --"
grep '^??' /tmp/v12-status.txt || echo "(none)"
echo
echo "=== B. PRODUCER-BYTE OWNERSHIP ==="
echo "-- tracked modifications outside corpus/knowledge/ (must be none) --"
grep -E '^ ?[MDARC]' /tmp/v12-status.txt | grep -v ' corpus/knowledge/' || echo "(none)"
echo "-- tracked modifications inside corpus/knowledge/ (U2 addenda only; verify dated) --"
grep -E '^ ?[MDARC]' /tmp/v12-status.txt | grep ' corpus/knowledge/' || echo "(none)"
echo "-- new untracked files under corpus/ (must be exactly the 3 producer artifacts) --"
grep '^??' /tmp/v12-status.txt | grep ' corpus/' || echo "(none)"
echo
echo "=== C. UNTRACKED OUTSIDE WAVE-SCRATCH NAMESPACES (violations) ==="
grep '^??' /tmp/v12-status.txt | grep -vE ' \.ufo/waves/round-102/| \.scratch/| \.ufo/waves/round-98/' || echo "(none)"
echo
echo "=== D. SEATS DIR INVENTORY ==="
find .ufo/waves/round-102/seats -maxdepth 1 -mindepth 1 -printf '%y %f\n' | sort
echo "-- seats/ entries NOT matching seat-report or scratch pattern --"
find .ufo/waves/round-102/seats -maxdepth 1 -mindepth 1 -printf '%f\n' | grep -vE '^(U1|U2|V[0-9]{2})-[a-z0-9-]+(\.md)?$' | grep -vE '^(U1|U2|V[0-9]{2})-[a-z0-9-]+-scratch$' || echo "(none)"
echo
echo "=== E. PARENT-TREE STRAYS (fresh outside lore-shokunin) ==="
find /home/vgpnk/Projects/shokunin -path '*/lore-shokunin' -prune -o -type f -newermt '2026-10-18 06:19' -print 2>/dev/null > /tmp/v12-parent-fresh.txt
wc -l < /tmp/v12-parent-fresh.txt
awk -F/ '{print $5}' /tmp/v12-parent-fresh.txt | sort | uniq -c | sort -rn | head
echo "-- non-kotodama strays --"
grep -v '/kotodama-shokunin/' /tmp/v12-parent-fresh.txt || echo "(none)"
echo "-- round-102-referencing strays outside lore --"
xargs -d '\n' grep -lE 'round-102' /tmp/v12-parent-fresh.txt 2>/dev/null || echo "(none)"
