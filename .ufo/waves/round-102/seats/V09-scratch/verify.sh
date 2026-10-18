#!/bin/bash
# V09 addendum verification — run after U2 lands
cd /home/vgpnk/Projects/shokunin/lore-shokunin
echo "== git status corpus/knowledge =="; git status --short -- corpus/knowledge/
echo; echo "== numstat (mods must be additions-only: deletions=0) =="
git diff --numstat -- corpus/knowledge/
echo; echo "== any deletion lines in diffs? =="
git diff -U0 -- corpus/knowledge/ | grep -E '^-' | grep -v '^---' || echo "NONE (purely additive)"
echo; echo "== added blocks with dates/rounds =="
git diff -U3 -- corpus/knowledge/ | grep -E '^\+' | grep -vE '^\+\+\+' | grep -nE '2026-10|round|Round' | head -40
echo; echo "== sha-like tokens inside added lines =="
git diff -U0 -- corpus/knowledge/ | grep -E '^\+' | grep -oE '\b[0-9a-f]{8,64}\b' | sort | uniq -c
