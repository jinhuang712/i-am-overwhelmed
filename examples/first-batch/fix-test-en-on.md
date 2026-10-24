Fixed `test_retry`. I haven't seen CI itself, but the tests passed 200 runs in a row locally.

## Cause
- `retry.py` sleeps for a random time between retries. With 2 failures, those sleeps can add up to 0.06s.
- The test required the whole call to finish in under 0.03s, so it failed whenever the random sleeps came out long.
- The bug was in the test, not in `retry.py`.

## Fix (`tests/test_retry.py`)
- Both tests now mock `time.sleep`, so they no longer wait or depend on timing.
- `test_retry` now checks that there were exactly 2 sleeps. It also checks that the first is within 0.02s and the second within 0.04s, the backoff limits in `retry.py`.
- `retry.py` is unchanged.

## Notes
- The `.pyc` files under `__pycache__` are tracked in git and show as modified. I didn't touch them on purpose. You may want to untrack them and add them to `.gitignore`.
- I haven't committed or pushed anything.

Do you want me to commit this and untrack the `.pyc` files?
- A. Commit the test fix only. I'd pick this one because it keeps the change small.
- B. Commit the test fix and untrack the `.pyc` files.
- C. Leave everything uncommitted.
