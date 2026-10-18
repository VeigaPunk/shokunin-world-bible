# Round 16 executor report

Scope: changed only `corpus/fixtures/check_bible.py`; no fixtures, docs, LOG, or commits changed. Added `place_id_count != 0` to the existing `actor_id_count == 1` occupied-slot condition. The dangling-place check still runs earlier and remains unchanged. Count-zero place rows therefore neither compare nor enter `occupied`; ambiguous (`>1`) and unique non-place IDs keep their prior behavior. The unique-actor guard is retained.

## r16 fixture CLI results
Command for each: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`; stderr was empty in all cases.

- `r16-missing-first`: exit 1; stdout:
  ```
  VIOLATION: timeline[0].place_id: dangling entity 'unlisted'
  1 violation(s); no canon changed
  ```
- `r16-missing-place`: exit 1; stdout:
  ```
  VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
  1 violation(s); no canon changed
  ```
- `r16-mixed-three`: exit 1; stdout:
  ```
  VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
  VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
  2 violation(s); no canon changed
  ```
  The absent-place middle row does not mask the known-place collision.
- `r16-valid-places`: exit 1; stdout:
  ```
  VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
  1 violation(s); no canon changed
  ```

## Regression comparison
Loaded baseline checker source with `git show 3995486:.shokunin/lore/corpus/fixtures/check_bible.py` and ran both that source and the modified checker against all 29 non-r16 fixture directories. For every fixture, exit code, stdout bytes, and stderr bytes matched exactly (29/29). Independently compared modified CLI output against the saved prior run at `corpus/live/runs/20261012T181828Z`; all 29 saved output files matched exactly.

Limitations: this is a narrow count-zero exclusion only. Duplicate/ambiguous place IDs and uniquely resolved non-place IDs retain existing occupied-slot behavior. A missing location is not shown to equal either known place, and this check does not establish the absence of a real conflict, resolve canon, or validate source truth.
